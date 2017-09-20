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
                                    single-cpe-dual-wan-site
                                                            |
                                                            single-cpe-dual-wan-site-services
                                                                                             |
                                                                                             failover-fallback-service
                                                                                                                      |
                                                                                                                      failover-fallback
                                                                                                                                       
Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/failover-fallback-service/failover-fallback
"""
"""
Names of Leafs for this Yang Entity
                name
              device
cpe-primary-wan-neighbor
cpe-secondary-wan-neighbor
        failover-wan
        fallback-wan
        failover-lan
        fallback-lan

"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import getPreviousObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log
from servicemodel.controller.devices.device import vrfs
from servicemodel.controller.devices.device import interfaces

class ServiceDataCustomization:

    @staticmethod
    def process_service_create_data(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the inputs"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']

    @staticmethod
    def process_service_device_bindings(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the device bindings or Call the Business Login Handlers"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']
        devbindobjs = kwargs['devbindobjs']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']
        fail_fall(smodelctx, sdata, **kwargs)

    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']

        #Previous config and previous inputdict
        pconfig = kwargs['pconfig']
        pinputdict = kwargs['pinputdict']

        dev = kwargs['dev']

    @staticmethod
    def process_service_delete_data(smodelctx, sdata, **kwargs):
      """callback called for delete operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        dev = kwargs['dev']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']


def fail_fall(smodelctx, sdata, **kwargs):
    inputdict = kwargs['inputdict']
    device = inputdict['device']
    dev = devicemgr.getDeviceById(device)
    failover_lan = inputdict['failover_lan']
    fallback_lan = inputdict['fallback_lan']

    cpe_primary_wan_neighbor = inputdict['cpe_primary_wan_neighbor']
    cpe_secondary_wan_neighbor = inputdict['cpe_secondary_wan_neighbor']
    failover_wan = inputdict['failover_wan']
    fallback_wan = inputdict['fallback_wan']
    vrf = None
    obj_prim = getLocalObject(sdata, 'single-cpe-dual-wan-site-services=')
    if device == obj_prim.single_cpe_dual_wan_site_services.cpe.device_ip:
        if hasattr(obj_prim.single_cpe_dual_wan_site_services.cpe_primary_wan, 'end_points'):
            endpoints = util.convert_to_list(obj_prim.single_cpe_dual_wan_site_services.cpe_primary_wan.end_points)
            for endpoint in endpoints:

                if hasattr(endpoint, 'ivrf'):
                    vrf = endpoint.ivrf
                if hasattr(endpoint, 'vrf'):
                    vrf = endpoint.vrf
                if vrf is None:
                    vrf = "GLOBAL"
                if hasattr(endpoint, 'bgp_peers'):
                    bgppeers = util.convert_to_list(endpoint.bgp_peers)
                    for bgppeer in bgppeers:
                        if cpe_primary_wan_neighbor == bgppeer.peer_ip:
                            primobj = vrfs.vrf.router_bgp.neighbor.neighbor()
                            primobj.ip_address = cpe_primary_wan_neighbor
                            if failover_wan == 'true':
                                primobj.shut = "true"
                            if fallback_wan == 'true':
                                primobj.shut = "false"
                            router_bgp_neighbor_url = dev.url + '/vrfs/vrf=%s/router-bgp' % (vrf)
                            yang.Sdk.createData(router_bgp_neighbor_url, primobj.getxml(filter=True), sdata.getSession(), False)

    vrf = None
    if device == obj_prim.single_cpe_dual_wan_site_services.cpe.device_ip:
        if hasattr(obj_prim.single_cpe_dual_wan_site_services.cpe_secondary_wan, 'end_points'):
            endpoints = util.convert_to_list(obj_prim.single_cpe_dual_wan_site_services.cpe_secondary_wan.end_points)
            for endpoint in endpoints:

                if hasattr(endpoint, 'ivrf'):
                    vrf = endpoint.ivrf
                if hasattr(endpoint, 'vrf'):
                    vrf = endpoint.vrf
                if vrf is None:
                    vrf = "GLOBAL"
                if hasattr(endpoint, 'bgp_peers'):
                    bgppeers = util.convert_to_list(endpoint.bgp_peers)
                    for bgppeer in bgppeers:
                        if cpe_secondary_wan_neighbor == bgppeer.peer_ip:
                            primobj = vrfs.vrf.router_bgp.neighbor.neighbor()
                            primobj.ip_address = cpe_secondary_wan_neighbor
                            if failover_wan == 'true':
                                primobj.shut = "true"
                            if fallback_wan == 'true':
                                primobj.shut = "false"
                            router_bgp_neighbor_url = dev.url + '/vrfs/vrf=%s/router-bgp' % (vrf)
                            yang.Sdk.createData(router_bgp_neighbor_url, primobj.getxml(filter=True), sdata.getSession(), False)

    obj = getLocalObject(sdata, 'single-cpe-dual-wan-site-services=')
    if hasattr(obj.single_cpe_dual_wan_site_services.cpe_lan, 'end_points'):
        endpoints = util.convert_to_list(obj.single_cpe_dual_wan_site_services.cpe_lan.end_points)
        for endpoint in endpoints:
            if device == endpoint.device_ip:
                if endpoint.interface_type == 'Physical':
                    interface_name = endpoint.interface_name
                elif endpoint.interface_type == 'Sub-Interface':
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if failover_lan == 'true':
                    failobj = interfaces.interface.interface()
                    failobj.name = interface_name
                    failobj.long_name = interface_name
                    failobj.admin_state = 'DOWN'
                    yang.Sdk.createData(dev.url + '/interfaces', failobj.getxml(filter=True), sdata.getSession(), False)

                if fallback_lan == 'true':
                    fallobj = interfaces.interface.interface()
                    fallobj.name = interface_name
                    fallobj.long_name = interface_name
                    fallobj.admin_state = 'UP'
                    yang.Sdk.createData(dev.url + '/interfaces', fallobj.getxml(filter=True), sdata.getSession(), False)


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
