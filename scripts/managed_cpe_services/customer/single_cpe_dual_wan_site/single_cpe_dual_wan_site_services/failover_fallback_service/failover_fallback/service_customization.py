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
    obj_prim = getLocalObject(sdata, 'single-cpe-dual-wan-site-services=')
    device = obj_prim.single_cpe_dual_wan_site_services.cpe.device_ip
    dev = devicemgr.getDeviceById(device)
    cpe_primary_wan_ebgp_neighbor = inputdict['cpe_primary_wan_ebgp_neighbor']
    cpe_secondary_wan_ebgp_neighbor = inputdict['cpe_secondary_wan_ebgp_neighbor']
    vrf = None
    pri_cpe_in_route_map = ""
    pri_cpe_out_route_map = ""
    pri_bgp_ep_name = None
    sec_bgp_ep_name = None
    pri_bgp_peer_name = None
    sec_bgp_peer_name = None
    sec_cpe_in_route_map = ""
    sec_cpe_out_route_map = ""
    
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
                    pri_router_bgp_neighbor_url = dev.url + '/l3features:vrfs/vrf=%s/router-bgp/neighbor=%s' % (vrf, cpe_primary_wan_ebgp_neighbor)

                    if yang.Sdk.dataExists(pri_router_bgp_neighbor_url):
                        bgppeers = util.convert_to_list(endpoint.bgp_peers)
                        for bgppeer in bgppeers:
                           # Check if Neighbor effectively exists on device
                        
                            bgppeers = util.convert_to_list(endpoint.bgp_peers)
                            for bgppeer in bgppeers:
                                if cpe_primary_wan_ebgp_neighbor == bgppeer.peer_ip:
                                    pri_bgp_ep_name = endpoint.endpoint_name
                                    pri_bgp_peer_name = bgppeer.BGP_peer_name
                                    if hasattr(bgppeer, 'import_route_map'):
                                        pri_cpe_in_route_map = bgppeer.import_route_map
                                    if hasattr(bgppeer, 'export_route_map'):
                                        pri_cpe_out_route_map = bgppeer.export_route_map

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
                    sec_router_bgp_neighbor_url = dev.url + '/l3features:vrfs/vrf=%s/router-bgp/neighbor=%s' % (vrf, cpe_secondary_wan_ebgp_neighbor)
                    if yang.Sdk.dataExists(sec_router_bgp_neighbor_url):
                        bgppeers = util.convert_to_list(endpoint.bgp_peers)
                        for bgppeer in bgppeers:
                            if cpe_secondary_wan_ebgp_neighbor == bgppeer.peer_ip:
                                sec_bgp_ep_name = endpoint.endpoint_name
                                sec_bgp_peer_name = bgppeer.BGP_peer_name
                                if hasattr(bgppeer, 'import_route_map'):
                                    sec_cpe_in_route_map = bgppeer.import_route_map
                                if hasattr(bgppeer, 'export_route_map'):
                                    sec_cpe_out_route_map = bgppeer.export_route_map

    parent_uri = sdata.getRcPath().split('/', 6)
    parent_uri = '/'.join(parent_uri[0:6])

    if inputdict['swap_bgp_route_maps'] == "true":

        if pri_bgp_ep_name is not None and pri_bgp_peer_name is not None:
            pri_bgp_peer_url = parent_uri + '/cpe-primary-wan/end-points=%s/bgp-peers=%s' % (pri_bgp_ep_name, pri_bgp_peer_name)

            pri_payload = """
                        <bgp-peers xmlns="http://anutanetworks.com/cpedeployment">
                        <BGP-peer-name>%s</BGP-peer-name>
                        <import-route-map>%s</import-route-map>
                        <export-route-map>%s</export-route-map>
                        </bgp-peers>
                          """ % (pri_bgp_peer_name, sec_cpe_in_route_map, sec_cpe_out_route_map)

            yang.Sdk.patchData(pri_bgp_peer_url, pri_payload, sdata, False)


        if sec_bgp_ep_name is not None and sec_bgp_peer_name is not None:

            sec_bgp_peer_url = parent_uri + '/cpe-secondary-wan/end-points=%s/bgp-peers=%s' % (sec_bgp_ep_name, sec_bgp_peer_name)

            sec_payload = """
                        <bgp-peers xmlns="http://anutanetworks.com/cpedeployment">
                        <BGP-peer-name>%s</BGP-peer-name>
                        <import-route-map>%s</import-route-map>
                        <export-route-map>%s</export-route-map>
                        </bgp-peers>
                           """ % (sec_bgp_peer_name, pri_cpe_in_route_map, pri_cpe_out_route_map)

            yang.Sdk.patchData(sec_bgp_peer_url, sec_payload, sdata, False)

    '''
    #Failover/Fallback DMVPN DPS Tunnel
    if failover_dps == 'true':
        failobj = interfaces.interface.interface()
        failobj.name = dps_tunnel_id
        failobj.long_name = dps_tunnel_id
        failobj.admin_state = 'DOWN'
        yang.Sdk.createData(dev.url + '/interface:interfaces', failobj.getxml(filter=True), sdata.getSession(), False)

    if fallback_dps == 'true':
        fallobj = interfaces.interface.interface()
        fallobj.name = dps_tunnel_id
        fallobj.long_name = dps_tunnel_id
        fallobj.admin_state = 'UP'
        yang.Sdk.createData(dev.url + '/interface:interfaces', fallobj.getxml(filter=True), sdata.getSession(), False)
    '''

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
        yang.moveOperations(operations, ['UpdateRouterBGPNeighbor'], ['CreateRouteMap','CreateRouteMapConditions'], True)
