#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2016-2017 Anuta Networks, Inc. All Rights Reserved.
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
                                    dps
                                       |
                                       dps-services
                                                   |
                                                   cpe-name
                                                           |
                                                           static-routes
                                                                        |
                                                                        static-route
                                                                                    |
                                                                                    options
                                                                                           
Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/static-routes/static-route/options
"""
"""
Names of Leafs for this Yang Entity
                  id
         next-hop-ip
              metric
      interface-name
                name
                 vrf
                 tag
               track

"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr
from servicemodel.controller.devices.device import vrfs
from servicemodel.controller.devices.device import routes

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log
from com.anuta.api import DataNodeNotFoundException


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
        inputkeydict = kwargs['inputkeydict']
        conf = None
        entity = None
        device = None
        obj = getLocalObject(sdata, 'dps-services')
        obj_cpe = getLocalObject(sdata, 'cpe-name')
        uri = sdata.getRcPath()
        uri_list = uri.split('/',5)
        url = '/'.join(uri_list[0:4])
        if hasattr(obj.dps_services, 'single_cpe_site'):
            if obj.dps_services.single_cpe_site == "true":
                site = obj.dps_services.single_cpe_sites
                site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '', sdata.getTaskId())
                conf = util.parseXmlString(site_output)
                entity = 'cpe'
        elif hasattr(obj.dps_services, 'dual_cpe_site'):
            if obj.dps_services.dual_cpe_site == "true":
                site = obj.dps_services.dual_cpe_sites
                site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                conf = util.parseXmlString(site_output)
                if obj_cpe.cpe_name.cpe == 'cpe-primary':
                    entity = 'cpe_primary'
                elif obj_cpe.cpe_name.cpe == 'cpe-secondary':
                    entity = 'cpe_secondary'
                elif obj_cpe.cpe_name.cpe == 'cpe-secondary-only':
                    entity = 'cpe_secondary_only'
        elif hasattr(obj.dps_services, 'single_cpe_dual_wan_site'):
            if obj.dps_services.single_cpe_dual_wan_site == "true":
                site = obj.dps_services.single_cpe_dual_wan_sites
                site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                conf = util.parseXmlString(site_output)
                entity = 'cpe_dual'
        elif hasattr(obj.dps_services, 'dual_cpe_dual_wan_site'):
            if obj.dps_services.dual_cpe_dual_wan_site == "true":
                site = obj.dps_services.dual_cpe_dual_wan_sites
                site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                conf = util.parseXmlString(site_output)
                if obj_cpe.cpe_name.cpe == 'cpe-primary':
                    entity = 'cpe_primary_dual'
                elif obj_cpe.cpe_name.cpe == 'cpe-secondary':
                    entity = 'cpe_secondary_dual'
                elif obj_cpe.cpe_name.cpe == 'cpe-secondary-only':
                    entity = 'cpe_secondary_only_dual'
        elif hasattr(obj.dps_services, 'triple_cpe_site'):
            if obj.dps_services.triple_cpe_site == "true":
                site = obj.dps_services.triple_cpe_sites
                site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '', sdata.getTaskId())
                conf = util.parseXmlString(site_output)
                if obj_cpe.cpe_name.cpe == 'cpe-primary-only':
                    entity = 'cpe_primary_triple'
        if entity == 'cpe':
            device_ip = conf.single_cpe_site_services.cpe.device_ip
        elif entity == 'cpe_primary':
            device_ip = conf.dual_cpe_site_services.cpe_primary.device_ip
        elif entity == 'cpe_secondary' or entity == 'cpe_secondary_only':
            device_ip = conf.dual_cpe_site_services.cpe_secondary.device_ip
        elif entity == 'cpe_dual':
            device_ip = conf.single_cpe_dual_wan_site_services.cpe.device_ip
        elif entity == 'cpe_primary_dual':
            device_ip = conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip
        elif entity == 'cpe_secondary_dual' or entity == 'cpe_secondary_only_dual':
            device_ip = conf.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip
        elif entity == 'cpe_primary_triple':
            device_ip = conf.triple_cpe_site_services.cpe_primary.device_ip
        staticroute(smodelctx, sdata, device_ip, **kwargs)

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
        inputkeydict = kwargs['inputkeydict']
        devbindobjs = kwargs['devbindobjs']

    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      raise Exception('Update forbidden for node options at path managed-cpe-services/customer/dps/dps-services/cpe-name/static-routes/static-route/options')
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']

    @staticmethod
    def process_service_delete_data(smodelctx, sdata, **kwargs):
      """callback called for delete operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']


def staticroute(smodelctx, sdata, device_ip, **kwarg):
    dev = devicemgr.getDeviceById(device_ip)
    vrf_name = kwarg['inputdict']['vrf']

    if vrf_name is not None:
        list_vrf = []
        vrf_url = '/app/restconf/data/controller:devices/device=%s/l3features:vrfs'% str(dev.device.id)
        xml_output = yang.Sdk.getData(vrf_url, '', sdata.getTaskId())
        obj = util.parseXmlString(xml_output)
        util.log_debug( "obj: ", obj)
        if hasattr(obj.vrfs, 'vrf'):
            obj.vrfs.vrf = util.convert_to_list(obj.vrfs.vrf)
            for vrf in obj.vrfs.vrf:
                list_vrf.append(vrf.name)
        if vrf_name not in list_vrf:
            raise Exception('VRF is not configured or not part of service')
        static_routes_url = dev.url + '/vrfs/vrf=%s' % (vrf_name)
        static_obj1 = vrfs.vrf.routes.route.route()
    else:
        static_routes_url = dev.url
        static_obj1 = routes.route.route()

    yang.Sdk.createData(static_routes_url, '<routes/>', sdata.getSession(), False)
    obj_local = getLocalObject(sdata, 'static-route=')
    util.log_debug("static route obj is:",obj_local.static_route)

    static_obj1.dest_ip_address = obj_local.static_route.dest_ip_address
    static_obj1.dest_mask = obj_local.static_route.dest_mask
    if vrf_name is not None:
        static_route_url = dev.url + '/vrfs/vrf=%s/routes' % (vrf_name)
        static_obj = vrfs.vrf.routes.route.options.options()
        get_static_route_url = dev.url + '/vrfs/vrf=%s/routes/route=%s,%s' % (vrf_name,obj_local.static_route.dest_ip_address,obj_local.static_route.dest_mask)
    else:
        static_route_url = dev.url + '/routes'
        static_obj = routes.route.options.options()
        get_static_route_url = dev.url + '/routes/route=%s,%s' % (obj_local.static_route.dest_ip_address,obj_local.static_route.dest_mask)
    try:
        xml_output = yang.Sdk.getData(get_static_route_url, '', sdata.getTaskId())
        obj_get = util.parseXmlString(xml_output)
        util.log_debug( "obj of route is: ",obj_get)
        yang.Sdk.createData(static_route_url, static_obj1.getxml(filter=True), sdata.getSession(), False)
    except DataNodeNotFoundException:
        yang.Sdk.createData(static_route_url, static_obj1.getxml(filter=True), sdata.getSession())

    id = 'ip route'
    if vrf_name is not None:
        id += ' vrf' + ' ' + vrf_name
    id += ' ' + obj_local.static_route.dest_ip_address + ' ' + obj_local.static_route.dest_mask
    interface_name = kwarg['inputdict']['interface_name']
    if interface_name is not None:
        id += ' ' + interface_name
        static_obj.interface_name = interface_name

    next_hop_ip = kwarg['inputdict']['next_hop_ip']
    if next_hop_ip is not None:
        id += ' ' + next_hop_ip
        static_obj.next_hop_ip = next_hop_ip

    if interface_name is None and next_hop_ip is None:
        raise Exception("Both Interface Name & Next Hop IP can not be empty in static routes")

    if vrf_name is not None:
        global_address = kwarg['inputdict']['global_address']
        if global_address is not None and global_address == 'true':
            id += ' ' + 'global'
            static_obj.global_address = global_address
        elif global_address is not None and global_address == 'false':
            static_obj.global_address = global_address

    metric = kwarg['inputdict']['metric']
    if metric is not None:
        id += ' ' + metric
        static_obj.metric = metric

    tag = kwarg['inputdict']['tag']
    if tag is not None:
        id += ' tag ' + tag
        static_obj.tag = tag

    permanent = kwarg['inputdict']['permanent']
    if permanent is not None and permanent == 'true':
        id += ' permanent'
        static_obj.permanent = permanent
    elif permanent is not None and permanent == 'false':
        static_obj.permanent = permanent

    name = kwarg['inputdict']['name']
    if name is not None:
        id += ' name ' + name
        static_obj.name = name

    track = kwarg['inputdict']['track']
    if track is not None:
        id += ' track ' + track
        static_obj.track = track

    static_obj.id = id

    if vrf_name is not None:
        static_url = dev.url + '/vrfs/vrf=%s/routes/route=%s,%s' % (vrf_name,obj_local.static_route.dest_ip_address,obj_local.static_route.dest_mask)
    else:
        static_url = dev.url + '/routes/route=%s,%s' % (obj_local.static_route.dest_ip_address,obj_local.static_route.dest_mask)
    yang.Sdk.createData(static_url, static_obj.getxml(filter=True), sdata.getSession())


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
