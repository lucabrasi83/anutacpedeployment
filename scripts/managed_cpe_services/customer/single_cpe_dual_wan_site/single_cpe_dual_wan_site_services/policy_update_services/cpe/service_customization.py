#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2015-2016 Anuta Networks, Inc. All Rights Reserved.
#

#
#ALL THE CUSTOMIZATIONS REGARDING DATAPROCESSING SHOULD BE WRITTEN INTO THIS FILE
#
"""
Tree Structure of Handled XPATH:

services
        |
        managed-cpe-services
                            |
                            customer
                                    |
                                    single-cpe-dual-wan-site
                                                            |
                                                            single-cpe-dual-wan-site-services
                                                                                             |
                                                                                             policy-update-services
                                                                                                                   |
                                                                                                                   cpe
                                                                                                                      
Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/policy-update-services/cpe
"""
"""
Names of Leafs for this Yang Entity
           end-point
          end-point1
          end-point2
    import-route-map
    export-route-map
"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr
from servicemodel.controller import devices

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log


class ServiceDataCustomization:

    @staticmethod
    def process_service_create_data(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the inputs"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']

    @staticmethod
    def process_service_device_bindings(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the device bindings or Call the Business Login Handlers"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        devbindobjs = kwargs['devbindobjs']

    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

        config = kwargs['config']
        uri = sdata.getRcPath()
        parent_uri = uri[:uri.rfind('/policy-update-services')]
        print parent_uri

        inputdict = {}
        inputdict['end_point'] = config.get_field_value('end_point')
        inputdict['import_route_map'] = config.get_field_value('import_route_map')
        inputdict['export_route_map'] = config.get_field_value('export_route_map')

        if inputdict['end_point'] == 'cpe-primary-wan':
            inputdict['end_point1'] = config.get_field_value('end_point1')
            secondary_ic_uri = "%s/cpe-primary-wan/end-points=%s/bgp-peers" % (parent_uri, inputdict['end_point1'])
            ep_uri = "%s/cpe-primary-wan/end-points=%s" % (parent_uri, inputdict['end_point1'])
        else:
            inputdict['end_point2'] = config.get_field_value('end_point2')
            secondary_ic_uri = "%s/cpe-secondary-wan/end-points=%s/bgp-peers" % (parent_uri, inputdict['end_point2'])
            ep_uri = "%s/cpe-secondary-wan/end-points=%s" % (parent_uri, inputdict['end_point2'])

        ep_uri = ep_uri.replace(' ','%20')
        # checking if the url exists
        xpath = yang.Sdk.getXpath(secondary_ic_uri)
        rc_path_list_temp = yang.Sdk.getRcPathListForXPath(xpath, level=0, taskId=None)
        rc_path_list = [elem for elem in rc_path_list_temp if ep_uri in elem]
        print rc_path_list

        if not rc_path_list:
            raise Exception('Given end-point is not present')
        else:
            rc_path = rc_path_list[0]
            bgp = rc_path[rc_path.rfind('=')+1:]
            # trigger update on the entities
            prefix = "<bgp-peers><BGP-peer-name>%s</BGP-peer-name>" % bgp
            suffix = "</bgp-peers>"
            if not inputdict['import_route_map']:
                inputdict['import_route_map'] = ''
            payload = "%s<import-route-map>%s</import-route-map>%s" % (prefix, inputdict['import_route_map'], suffix)
            yang.Sdk.patchData(rc_path, payload, sdata, False)

            if not inputdict['export_route_map']:
                inputdict['export_route_map'] = ''
            payload = "%s<export-route-map>%s</export-route-map>%s" % (prefix, inputdict['export_route_map'], suffix)
            yang.Sdk.patchData(rc_path, payload, sdata, False)

            site_output = yang.Sdk.getData(ep_uri, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)
            device = devicemgr.getDeviceById(conf.end_points.device_ip)
            vrf = None
            if hasattr(conf.end_points, 'fvrf'):
                vrf = conf.end_points.fvrf
            if vrf is None:
                obj = getLocalObject(sdata, 'single-cpe-dual-wan-site-services')
                if hasattr(obj.single_cpe_dual_wan_site_services.cpe, 'vrf_name'):
                    vrf = obj.single_cpe_dual_wan_site_services.cpe.vrf_name
                if vrf is None:
                    vrf = "GLOBAL"
            peer_ip = conf.end_points.bgp_peers.peer_ip
            remote_as = conf.end_points.bgp_peers.remote_as
            bgp_neighbor_obj = devices.device.vrfs.vrf.router_bgp.neighbor.neighbor()
            if inputdict['import_route_map'] != "":
                bgp_neighbor_obj.in_route_map = inputdict['import_route_map']
            if inputdict['export_route_map'] != "":
                bgp_neighbor_obj.out_route_map = inputdict['export_route_map']
            bgp_neighbor_obj.ip_address = peer_ip
            bgp_neighbor_obj.remote_as = remote_as
            router_bgp_neighbor_url = device.url + '/vrfs/vrf=%s/router-bgp' % (vrf)
            yang.Sdk.createData(router_bgp_neighbor_url, bgp_neighbor_obj.getxml(filter=True), sdata.getSession(), False)

    @staticmethod
    def process_service_delete_data(smodelctx, sdata, **kwargs):
      """callback called for delete operation"""
      modify = False
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))


class DeletePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for Deletion"""
        log('operations: %s' % (operations))


class CreatePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for creation"""
        log('operations: %s' % (operations))
