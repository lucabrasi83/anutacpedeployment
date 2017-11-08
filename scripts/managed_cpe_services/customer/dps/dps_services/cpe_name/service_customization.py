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
                                    dps
                                       |
                                       dps-services
                                                   |
                                                   cpe-name
                                                           
Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name
"""
"""
Names of Leafs for this Yang Entity
                 cpe
                 vrf
                  rd
           rt-import
           rt-export
       lan-interface
      inbound-policy
          pbr-policy
         vrf-receive
       b2b-interface
             vlan-id
                cidr
        interface-ip
     b2b-description
            loopback
loopback-interface-id
         description
       cidr-loopback
                ospf
             ospf-id
           router-id
    static-route-map
 connected-route-map
            vrf-lite
                 bgp
         qppb-policy
redistribute-connected
 redistribute-static
    import-route-map
              tunnel
                 hub
       dmvpn-profile
tunnel-interface-ip-address
    tunnel-bandwidth
"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr
from servicemodel.controller.devices.device import vrfs
from servicemodel.controller.devices.device import interfaces
from servicemodel.controller.devices.device import dmvpntunnels
from servicemodel.controller.devices.device import policy_maps
from servicemodel.controller.devices.device import class_maps

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log,route_maps
from cpedeployment.endpoint_lib import access_group_def,IpamPoolID,get_used_ip_list_from_ippool
from cpedeployment.endpoint_lib import get_freeip_from_cidr,add_ipaddress_entries,modifiedGetLocalObject
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
            obj = getLocalObject(sdata, 'dps-services')
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
                    if inputdict['cpe'] == 'cpe-primary':
                        entity = 'cpe_primary'
                    elif inputdict['cpe'] == 'cpe-secondary':
                        entity = 'cpe_secondary'
                    elif inputdict['cpe'] == 'cpe-secondary-only':
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
                    if inputdict['cpe'] == 'cpe-primary':
                        entity = 'cpe_primary_dual'
                    elif inputdict['cpe'] == 'cpe-secondary':
                        entity = 'cpe_secondary_dual'
                    elif inputdict['cpe'] == 'cpe-secondary-only':
                        entity = 'cpe_secondary_only_dual'
            elif hasattr(obj.dps_services, 'triple_cpe_site'):
                if obj.dps_services.triple_cpe_site == "true":
                    site = obj.dps_services.triple_cpe_sites
                    site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '', sdata.getTaskId())
                    conf = util.parseXmlString(site_output)
                    if inputdict['cpe'] == 'cpe-primary':
                        entity = 'cpe_primary_triple'
                    elif inputdict['cpe'] == 'cpe-secondary':
                        entity = 'cpe_secondary_triple'
            dps(entity, conf, sdata, **kwargs)

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
      #raise Exception('Update forbidden for node cpe-name at path managed-cpe-services/customer/dps/dps-services/cpe-name')
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

    @staticmethod
    def process_service_delete_data(smodelctx, sdata, **kwargs):
        """callback called for delete operation"""
        modify = True
        if modify and kwargs is not None:
            for key, value in kwargs.iteritems():
                log("%s == %s" %(key,value))
        entity = None
        conf = None
        config = util.parseXmlString(sdata.getPayload())
        config = config.cpe_name
        obj = getLocalObject(sdata, 'dps-services')
        uri = sdata.getRcPath()
        uri_list = uri.split('/',5)
        url = '/'.join(uri_list[0:4])
        single_cpe_site = str(getattr(obj.dps_services, 'single_cpe_site', None)).lstrip()
        dual_cpe_site = str(getattr(obj.dps_services, 'dual_cpe_site', None)).lstrip()
        triple_cpe_site = str(getattr(obj.dps_services, 'triple_cpe_site', None)).lstrip()
        single_cpe_dual_wan_site = str(getattr(obj.dps_services, 'single_cpe_dual_wan_site', None)).lstrip()
        dual_cpe_dual_wan_site = str(getattr(obj.dps_services, 'dual_cpe_dual_wan_site', None)).lstrip()

        if single_cpe_site == 'true':
            site = getattr(obj.dps_services, 'single_cpe_sites', None)
            site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)
            entity = 'cpe'
        elif dual_cpe_site == 'true':
            site = getattr(obj.dps_services, 'dual_cpe_sites', None)
            site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)
            if config.cpe == 'cpe-primary':
                entity = 'cpe_primary'
            elif config.cpe == 'cpe-secondary':
                entity = 'cpe_secondary'
            elif config.cpe == 'cpe-secondary-only':
                entity = 'cpe_secondary_only'
        elif single_cpe_dual_wan_site == 'true':
            site = getattr(obj.dps_services, 'single_cpe_dual_wan_sites', None)
            site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)
            entity = 'cpe_dual'
        elif dual_cpe_dual_wan_site == 'true':
            site = getattr(obj.dps_services, 'dual_cpe_dual_wan_sites', None)
            site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)
            if config.cpe == 'cpe-primary':
                entity = 'cpe_primary_dual'
            elif config.cpe == 'cpe-secondary':
                entity = 'cpe_secondary_dual'
            elif config.cpe == 'cpe-secondary-only':
                entity = 'cpe_secondary_only_dual'
        elif triple_cpe_site == 'true':
            site = getattr(obj.dps_services, 'triple_cpe_sites', None)
            site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)
            if config.cpe == 'cpe-primary-only':
                entity = 'cpe_primary_triple'

        if config.cpe != 'cpe-secondary':
            if config.lan_interface == 'true':
                delete_interface(entity, smodelctx, sdata, conf, **kwargs)
            delete_route_map_from_redistribute_dps(entity, conf, sdata, **kwargs)


def delete_route_map_from_redistribute_dps(entity, conf, sdata, **kwargs):
    device = None
    interface_name = None
    mode = None
    bgp_as = None
    bgp_address_family = None
    int_name = None
    lan_vrf = None
    redistribute_connected_route_policy = None
    redistribute_static_route_policy = None
    is_new_site = 'false'
    if entity == 'cpe':
        device = devicemgr.getDeviceById(conf.single_cpe_site_services.cpe.device_ip)
        if hasattr(conf.single_cpe_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.single_cpe_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if hasattr(endpoint, 'dps'):
                    if endpoint.dps == 'true':
                        if hasattr(endpoint, 'vrf'):
                            lan_vrf = endpoint.vrf
                else:
                    if hasattr(conf.single_cpe_site_services.cpe, 'vrf_name'):
                        lan_vrf = conf.single_cpe_site_services.cpe.vrf_name
        if hasattr(conf.single_cpe_site_services.cpe, 'vrfs'):
            is_new_site = 'true'
            if hasattr(conf.single_cpe_site_services.cpe.vrfs, 'vrf'):
                obj = util.convert_to_list(conf.single_cpe_site_services.cpe.vrfs.vrf)
                for eachvrf in obj:
                    if hasattr(eachvrf, 'vrf_name'):
                        vrf = eachvrf.vrf_name
                    else:
                        vrf = None
                    if vrf == lan_vrf:
                        if hasattr(eachvrf, 'redistribute_connected_route_policy'):
                            redistribute_connected_route_policy = eachvrf.redistribute_connected_route_policy
                        if hasattr(eachvrf, 'redistribute_static_route_policy'):
                            redistribute_static_route_policy = eachvrf.redistribute_static_route_policy
        else:
            if hasattr(conf.single_cpe_site_services.cpe, 'vrf_name'):
                lan_vrf = conf.single_cpe_site_services.cpe.vrf_name
            if hasattr(conf.single_cpe_site_services.cpe, 'redistribute_connected_route_policy'):
                redistribute_connected_route_policy = conf.single_cpe_site_services.cpe.redistribute_connected_route_policy
            if hasattr(conf.single_cpe_site_services.cpe, 'redistribute_static_route_policy'):
                redistribute_static_route_policy = conf.single_cpe_site_services.cpe.redistribute_static_route_policy
        bgp_as = conf.single_cpe_site_services.bgp_as
        if hasattr(conf.single_cpe_site_services.cpe, 'vrfs'):
            if hasattr(conf.single_cpe_site_services.cpe.vrfs, 'vrf'):
                if hasattr(conf.single_cpe_site_services.cpe.vrfs.vrf, 'bgp_address_family'):
                    bgp_address_family = conf.single_cpe_site_services.cpe.vrfs.vrf.bgp_address_family
    elif entity == 'cpe_primary':
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_primary.device_ip)
        if hasattr(conf.dual_cpe_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.dual_cpe_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.dual_cpe_site_services.cpe_primary.device_ip:
                    if hasattr(endpoint, 'dps'):
                        if endpoint.dps == 'true':
                            if hasattr(endpoint, 'vrf'):
                                lan_vrf = endpoint.vrf
                    else:
                        if hasattr(conf.dual_cpe_site_services.cpe_primary, 'vrf_name'):
                            lan_vrf = conf.dual_cpe_site_services.cpe_primary.vrf_name
        if hasattr(conf.dual_cpe_site_services.cpe_primary, 'vrfs'):
            is_new_site = 'true'
            if hasattr(conf.dual_cpe_site_services.cpe_primary.vrfs, 'vrf'):
                obj = util.convert_to_list(conf.dual_cpe_site_services.cpe_primary.vrfs.vrf)
                for eachvrf in obj:
                    if hasattr(eachvrf, 'vrf_name'):
                        vrf = eachvrf.vrf_name
                    else:
                        vrf = None
                    if vrf == lan_vrf:
                        if hasattr(eachvrf, 'redistribute_connected_route_policy'):
                            redistribute_connected_route_policy = eachvrf.redistribute_connected_route_policy
                        if hasattr(eachvrf, 'redistribute_static_route_policy'):
                            redistribute_static_route_policy = eachvrf.redistribute_static_route_policy
        else:
            if hasattr(conf.dual_cpe_site_services.cpe_primary, 'vrf_name'):
                lan_vrf = conf.dual_cpe_site_services.cpe_primary.vrf_name
            if hasattr(conf.dual_cpe_site_services.cpe_primary, 'redistribute_connected_route_policy'):
                redistribute_connected_route_policy = conf.dual_cpe_site_services.cpe_primary.redistribute_connected_route_policy
            if hasattr(conf.dual_cpe_site_services.cpe_primary, 'redistribute_static_route_policy'):
                redistribute_static_route_policy = conf.dual_cpe_site_services.cpe_primary.redistribute_static_route_policy
        bgp_as = conf.dual_cpe_site_services.bgp_as
        if hasattr(conf.dual_cpe_site_services.cpe_primary, 'vrfs'):
            if hasattr(conf.dual_cpe_site_services.cpe_primary.vrfs, 'vrf'):
                if hasattr(conf.dual_cpe_site_services.cpe_primary.vrfs.vrf, 'bgp_address_family'):
                    bgp_address_family = conf.dual_cpe_site_services.cpe_primary.vrfs.vrf.bgp_address_family
    elif entity == 'cpe_secondary' or entity == 'cpe_secondary_only':
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_secondary.device_ip)
        if hasattr(conf.dual_cpe_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.dual_cpe_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.dual_cpe_site_services.cpe_secondary.device_ip:
                    if hasattr(endpoint, 'dps'):
                        if endpoint.dps == 'true':
                            if hasattr(endpoint, 'vrf'):
                                lan_vrf = endpoint.vrf
                    else:
                        if hasattr(conf.dual_cpe_site_services.cpe_secondary, 'vrf_name'):
                            lan_vrf = conf.dual_cpe_site_services.cpe_secondary.vrf_name
        if hasattr(conf.dual_cpe_site_services.cpe_secondary, 'vrfs'):
            is_new_site = 'true'
            if hasattr(conf.dual_cpe_site_services.cpe_secondary.vrfs, 'vrf'):
                obj = util.convert_to_list(conf.dual_cpe_site_services.cpe_secondary.vrfs.vrf)
                for eachvrf in obj:
                    if hasattr(eachvrf, 'vrf_name'):
                        vrf = eachvrf.vrf_name
                    else:
                        vrf = None
                    if vrf == lan_vrf:
                        if hasattr(eachvrf, 'redistribute_connected_route_policy'):
                            redistribute_connected_route_policy = eachvrf.redistribute_connected_route_policy
                        if hasattr(eachvrf, 'redistribute_static_route_policy'):
                            redistribute_static_route_policy = eachvrf.redistribute_static_route_policy
        else:
            if hasattr(conf.dual_cpe_site_services.cpe_secondary, 'vrf_name'):
                lan_vrf = conf.dual_cpe_site_services.cpe_secondary.vrf_name
            if hasattr(conf.dual_cpe_site_services.cpe_secondary, 'redistribute_connected_route_policy'):
                redistribute_connected_route_policy = conf.dual_cpe_site_services.cpe_secondary.redistribute_connected_route_policy
            if hasattr(conf.dual_cpe_site_services.cpe_secondary, 'redistribute_static_route_policy'):
                redistribute_static_route_policy = conf.dual_cpe_site_services.cpe_secondary.redistribute_static_route_policy
        bgp_as = conf.dual_cpe_site_services.bgp_as
        if hasattr(conf.dual_cpe_site_services.cpe_secondary, 'vrfs'):
            if hasattr(conf.dual_cpe_site_services.cpe_secondary.vrfs, 'vrf'):
                if hasattr(conf.dual_cpe_site_services.cpe_secondary.vrfs.vrf, 'bgp_address_family'):
                    bgp_address_family = conf.dual_cpe_site_services.cpe_secondary.vrfs.vrf.bgp_address_family
    elif entity == 'cpe_dual':
        device = devicemgr.getDeviceById(conf.single_cpe_dual_wan_site_services.cpe.device_ip)
        if hasattr(conf.single_cpe_dual_wan_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.single_cpe_dual_wan_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if hasattr(endpoint, 'dps'):
                    if endpoint.dps == 'true':
                        if hasattr(endpoint, 'vrf'):
                            lan_vrf = endpoint.vrf
                else:
                    if hasattr(conf.single_cpe_dual_wan_site_services.cpe, 'vrf_name'):
                        lan_vrf = conf.single_cpe_dual_wan_site_services.cpe.vrf_name
        if hasattr(conf.single_cpe_dual_wan_site_services.cpe, 'vrfs'):
            is_new_site = 'true'
            if hasattr(conf.single_cpe_dual_wan_site_services.cpe.vrfs, 'vrf'):
                obj = util.convert_to_list(conf.single_cpe_dual_wan_site_services.cpe.vrfs.vrf)
                for eachvrf in obj:
                    if hasattr(eachvrf, 'vrf_name'):
                        vrf = eachvrf.vrf_name
                    else:
                        vrf = None
                    if vrf == lan_vrf:
                        if hasattr(eachvrf, 'redistribute_connected_route_policy'):
                            redistribute_connected_route_policy = eachvrf.redistribute_connected_route_policy
                        if hasattr(eachvrf, 'redistribute_static_route_policy'):
                            redistribute_static_route_policy = eachvrf.redistribute_static_route_policy
        else:
            if hasattr(conf.single_cpe_dual_wan_site_services.cpe, 'vrf_name'):
                lan_vrf = conf.single_cpe_dual_wan_site_services.cpe.vrf_name
            if hasattr(conf.single_cpe_dual_wan_site_services.cpe, 'redistribute_connected_route_policy'):
                redistribute_connected_route_policy = conf.single_cpe_dual_wan_site_services.cpe.redistribute_connected_route_policy
            if hasattr(conf.single_cpe_dual_wan_site_services.cpe, 'redistribute_static_route_policy'):
                redistribute_static_route_policy = conf.single_cpe_dual_wan_site_services.cpe.redistribute_static_route_policy
        bgp_as = conf.single_cpe_dual_wan_site_services.bgp_as
        if hasattr(conf.single_cpe_dual_wan_site_services.cpe, 'vrfs'):
            if hasattr(conf.single_cpe_dual_wan_site_services.cpe.vrfs, 'vrf'):
                if hasattr(conf.single_cpe_dual_wan_site_services.cpe.vrfs.vrf, 'bgp_address_family'):
                    bgp_address_family = conf.single_cpe_dual_wan_site_services.cpe.vrfs.vrf.bgp_address_family
    elif entity == 'cpe_primary_dual':
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip)
        if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip:
                    if hasattr(endpoint, 'dps'):
                        if endpoint.dps == 'true':
                            if hasattr(endpoint, 'vrf'):
                                lan_vrf = endpoint.vrf
                    else:
                        if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary, 'vrf_name'):
                            lan_vrf = conf.dual_cpe_dual_wan_site_services.cpe_primary.vrf_name
        if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary, 'vrfs'):
            is_new_site = 'true'
            if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary.vrfs, 'vrf'):
                obj = util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_primary.vrfs.vrf)
                for eachvrf in obj:
                    if hasattr(eachvrf, 'vrf_name'):
                        vrf = eachvrf.vrf_name
                    else:
                        vrf = None
                    if vrf == lan_vrf:
                        if hasattr(eachvrf, 'redistribute_connected_route_policy'):
                            redistribute_connected_route_policy = eachvrf.redistribute_connected_route_policy
                        if hasattr(eachvrf, 'redistribute_static_route_policy'):
                            redistribute_static_route_policy = eachvrf.redistribute_static_route_policy
        else:
            if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary, 'vrf_name'):
                lan_vrf = conf.dual_cpe_dual_wan_site_services.cpe_primary.vrf_name
            if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary, 'redistribute_connected_route_policy'):
                redistribute_connected_route_policy = conf.dual_cpe_dual_wan_site_services.cpe_primary.redistribute_connected_route_policy
            if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary, 'redistribute_static_route_policy'):
                redistribute_static_route_policy = conf.dual_cpe_dual_wan_site_services.cpe_primary.redistribute_static_route_policy
        bgp_as = conf.dual_cpe_dual_wan_site_services.bgp_as
        if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary, 'vrfs'):
            if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary.vrfs, 'vrf'):
                if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary.vrfs.vrf, 'bgp_address_family'):
                    bgp_address_family = conf.dual_cpe_dual_wan_site_services.cpe_primary.vrfs.vrf.bgp_address_family
    elif entity == 'cpe_secondary_dual' or entity == 'cpe_secondary_only_dual':
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip)
        if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip:
                    if hasattr(endpoint, 'dps'):
                        if endpoint.dps == 'true':
                            if hasattr(endpoint, 'vrf'):
                                lan_vrf = endpoint.vrf
                    else:
                        if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary, 'vrf_name'):
                            lan_vrf = conf.dual_cpe_dual_wan_site_services.cpe_secondary.vrf_name
        if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary, 'vrfs'):
            is_new_site = 'true'
            if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary.vrfs, 'vrf'):
                obj = util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_secondary.vrfs.vrf)
                for eachvrf in obj:
                    if hasattr(eachvrf, 'vrf_name'):
                        vrf = eachvrf.vrf_name
                    else:
                        vrf = None
                    if vrf == lan_vrf:
                        if hasattr(eachvrf, 'redistribute_connected_route_policy'):
                            redistribute_connected_route_policy = eachvrf.redistribute_connected_route_policy
                        if hasattr(eachvrf, 'redistribute_static_route_policy'):
                            redistribute_static_route_policy = eachvrf.redistribute_static_route_policy
        else:
            if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary, 'vrf_name'):
                lan_vrf = conf.dual_cpe_dual_wan_site_services.cpe_secondary.vrf_name
            if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary, 'redistribute_connected_route_policy'):
                redistribute_connected_route_policy = conf.dual_cpe_dual_wan_site_services.cpe_secondary.redistribute_connected_route_policy
            if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary, 'redistribute_static_route_policy'):
                redistribute_static_route_policy = conf.dual_cpe_dual_wan_site_services.cpe_secondary.redistribute_static_route_policy
        bgp_as = conf.dual_cpe_dual_wan_site_services.bgp_as
        if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary, 'vrfs'):
            if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary.vrfs, 'vrf'):
                if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary.vrfs.vrf, 'bgp_address_family'):
                    bgp_address_family = conf.dual_cpe_dual_wan_site_services.cpe_secondary.vrfs.vrf.bgp_address_family
    elif entity == 'cpe_primary_triple':
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_primary.device_ip)
        if hasattr(conf.triple_cpe_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.triple_cpe_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.triple_cpe_site_services.cpe_primary.device_ip:
                    if hasattr(endpoint, 'dps'):
                        if endpoint.dps == 'true':
                            if hasattr(endpoint, 'vrf'):
                                lan_vrf = endpoint.vrf
                    else:
                        if hasattr(conf.triple_cpe_site_services.cpe_primary, 'vrf_name'):
                            lan_vrf = conf.triple_cpe_site_services.cpe_primary.vrf_name
        if hasattr(conf.triple_cpe_site_services.cpe_primary, 'vrfs'):
            is_new_site = 'true'
            if hasattr(conf.triple_cpe_site_services.cpe_primary.vrfs, 'vrf'):
                obj = util.convert_to_list(conf.triple_cpe_site_services.cpe_primary.vrfs.vrf)
                for eachvrf in obj:
                    if hasattr(eachvrf, 'vrf_name'):
                        vrf = eachvrf.vrf_name
                    else:
                        vrf = None
                    if vrf == lan_vrf:
                        if hasattr(eachvrf, 'redistribute_connected_route_policy'):
                            redistribute_connected_route_policy = eachvrf.redistribute_connected_route_policy
                        if hasattr(eachvrf, 'redistribute_static_route_policy'):
                            redistribute_static_route_policy = eachvrf.redistribute_static_route_policy
        else:
            if hasattr(conf.triple_cpe_site_services.cpe_primary, 'vrf_name'):
                lan_vrf = conf.triple_cpe_site_services.cpe_primary.vrf_name
            if hasattr(conf.triple_cpe_site_services.cpe_primary, 'redistribute_connected_route_policy'):
                redistribute_connected_route_policy = conf.triple_cpe_site_services.cpe_primary.redistribute_connected_route_policy
            if hasattr(conf.triple_cpe_site_services.cpe_primary, 'redistribute_static_route_policy'):
                redistribute_static_route_policy = conf.triple_cpe_site_services.cpe_primary.redistribute_static_route_policy
        bgp_as = conf.triple_cpe_site_services.bgp_as
        if hasattr(conf.triple_cpe_site_services.cpe_primary, 'vrfs'):
            if hasattr(conf.triple_cpe_site_services.cpe_primary.vrfs, 'vrf'):
                if hasattr(conf.triple_cpe_site_services.cpe_primary.vrfs.vrf, 'bgp_address_family'):
                    bgp_address_family = conf.triple_cpe_site_services.cpe_primary.vrfs.vrf.bgp_address_family

    inputdict = kwargs['inputdict']

    if inputdict['bgp'] == 'true':
        vrf_bgp = inputdict['bgp_vrf']
        bgpobj1 = vrfs.vrf.router_bgp.router_bgp()
        if util.isNotEmpty(bgp_as):
            bgpobj1.as_number = bgp_as
            if bgp_address_family is not None or util.isNotEmpty(bgp_address_family):
                bgpobj1.address_family = bgp_address_family
        #bgpobj1.address_family = "ipv4"
        if util.isNotEmpty(inputdict['qppb_policy']):
            bgpobj1.qppb_policy._empty_tag = True
            if vrf_bgp is None:
                vrf_global = 'GLOBAL'
                router_bgp_url = device.url + '/l3features:vrfs/vrf=%s/router-bgp' % (vrf_global)
                yang.Sdk.patchData(router_bgp_url, bgpobj1.getxml(filter=True), sdata, add_reference=False)
            else:
                router_bgp_url = device.url + '/l3features:vrfs/vrf=%s/router-bgp' % (vrf_bgp)
                yang.Sdk.patchData(router_bgp_url, bgpobj1.getxml(filter=True), sdata, add_reference=False)

    vrf = inputdict['bgp_vrf']
    if vrf is None:
        vrf = lan_vrf
    if vrf is None:
        vrf = 'GLOBAL'
    if vrf == 'GLOBAL' and is_new_site == 'false':
            vrf_glo_url = '/controller:devices/device=%s/l3features:vrfs/vrf=%s' % (device.device.id, vrf)
            output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+vrf_glo_url+'</rc-path></input>')
            ref = util.parseXmlString(output)
            util.log_debug("xml_op_vrf:%s" %(ref))
            if hasattr(ref.output, 'references'):
                if hasattr(ref.output.references, 'reference'):
                    for each_ref_ref in util.convert_to_list(ref.output.references.reference):
                        if hasattr(each_ref_ref, 'src_node'):
                            for each_ref in util.convert_to_list(each_ref_ref.src_node):
                                yang.Sdk.removeReference(each_ref, each_ref_ref.dest_node)
    if util.isNotEmpty(inputdict['redistribute_connected']) and redistribute_connected_route_policy is not None:
            rebgpredisobj1 = vrfs.vrf.router_bgp.redistribute.redistribute()
            rebgpredisobj1.protocol = 'connected'
            rebgpredisobj1.route_map = redistribute_connected_route_policy
            route_map_ref_url = device.url + '/l3features:vrfs/vrf=%s/router-bgp' % (vrf)
            yang.Sdk.createData(route_map_ref_url, rebgpredisobj1.getxml(filter=True), sdata.getSession(), addReference=False)
    elif util.isNotEmpty(inputdict['redistribute_connected']) and redistribute_connected_route_policy is None:
            # rebgpredisobj1 = vrfs.vrf.router_bgp.redistribute.redistribute()
            # rebgpredisobj1.protocol = 'connected'
            # rebgpredisobj1.route_map = redistribute_connected_route_policy
            #try:
            route_map_ref_url = device.url + '/l3features:vrfs/vrf=%s/router-bgp/redistribute=%s' % (vrf, 'connected')
            #    yang.Sdk.deleteData(route_map_ref_url, '', sdata.getTaskId(), sdata.getSession())
            #except DataNodeNotFoundException:
            #    print "Redistribute connected not configured already"
            if not yang.Sdk.dataExists(route_map_ref_url):
                print "Redistribute connected not configured already"
            else:
                yang.Sdk.deleteData(route_map_ref_url, '', sdata.getTaskId(), sdata.getSession())            

    if util.isNotEmpty(inputdict['redistribute_static']) and redistribute_static_route_policy is not None:
            rebgpredisobj1 = vrfs.vrf.router_bgp.redistribute.redistribute()
            rebgpredisobj1.protocol = 'static'
            rebgpredisobj1.route_map = redistribute_static_route_policy
            route_map_static_ref_url = device.url + '/l3features:vrfs/vrf=%s/router-bgp' % (vrf)
            yang.Sdk.createData(route_map_static_ref_url, rebgpredisobj1.getxml(filter=True), sdata.getSession(), addReference=False)
    elif util.isNotEmpty(inputdict['redistribute_static']) and redistribute_static_route_policy is None:
            # rebgpredisobj1 = vrfs.vrf.router_bgp.redistribute.redistribute()
            # rebgpredisobj1.protocol = 'static'
            # rebgpredisobj1.route_map = redistribute_static_route_policy
            #try:
            route_map_static_ref_url = device.url + '/l3features:vrfs/vrf=%s/router-bgp/redistribute=%s' % (vrf, 'static')
            #    yang.Sdk.deleteData(route_map_static_ref_url, '', sdata.getTaskId(), sdata.getSession())
            #except DataNodeNotFoundException:
            #    print "Redistribute static not configured already"
            if not yang.Sdk.dataExists(route_map_static_ref_url):
                print "Redistribute static not configured already"
            else:
                yang.Sdk.deleteData(route_map_static_ref_url, '', sdata.getTaskId(), sdata.getSession())            


def dps(entity, conf, sdata, **kwargs):
    device = None
    interface_name = None
    mode = None
    bgp_as = None
    bgp_address_family = None
    int_name = None
    lan_vrf = None
    if entity == 'cpe':
        device = devicemgr.getDeviceById(conf.single_cpe_site_services.cpe.device_ip)
        if hasattr(conf.single_cpe_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.single_cpe_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if endpoint.dps == 'true':
                    if hasattr(endpoint, 'vrf'):
                        lan_vrf = endpoint.vrf
                    if endpoint.interface_type == 'Physical':
                        interface_name = endpoint.interface_name
                        mode = 'l3-interface'
                    elif endpoint.interface_type == 'Sub-Interface':
                        interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                        mode = 'sub-interface'
                    elif endpoint.interface_type == 'SVI':
                        interface_name = "Vlan" + str(endpoint.vlan_id)
                        mode = 'vlan'
        bgp_as = conf.single_cpe_site_services.bgp_as
        if hasattr(conf.single_cpe_site_services.cpe.vrfs.vrf, 'bgp_address_family'):
            bgp_address_family = conf.single_cpe_site_services.cpe.vrfs.vrf.bgp_address_family
    elif entity == 'cpe_primary':
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_primary.device_ip)
        if hasattr(conf.dual_cpe_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.dual_cpe_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.dual_cpe_site_services.cpe_primary.device_ip:
                    if endpoint.dps == 'true':
                        if hasattr(endpoint, 'vrf'):
                            lan_vrf = endpoint.vrf
                        if endpoint.interface_type == 'Physical':
                            interface_name = endpoint.interface_name
                            mode = 'l3-interface'
                        elif endpoint.interface_type == 'Sub-Interface':
                            interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                            mode = 'sub-interface'
                        elif endpoint.interface_type == 'SVI':
                            interface_name = "Vlan" + str(endpoint.vlan_id)
                            mode = 'vlan'
        bgp_as = conf.dual_cpe_site_services.bgp_as
        if hasattr(conf.dual_cpe_site_services.cpe_primary.vrfs.vrf, 'bgp_address_family'):
            bgp_address_family = conf.dual_cpe_site_services.cpe_primary.vrfs.vrf.bgp_address_family
    elif entity == 'cpe_secondary' or entity == 'cpe_secondary_only':
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_secondary.device_ip)
        if hasattr(conf.dual_cpe_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.dual_cpe_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.dual_cpe_site_services.cpe_secondary.device_ip:
                    if endpoint.dps == 'true':
                        if hasattr(endpoint, 'vrf'):
                            lan_vrf = endpoint.vrf
                        if endpoint.interface_type == 'Physical':
                            interface_name = endpoint.interface_name
                            mode = 'l3-interface'
                        elif endpoint.interface_type == 'Sub-Interface':
                            interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                            mode = 'sub-interface'
                        elif endpoint.interface_type == 'SVI':
                            interface_name = "Vlan" + str(endpoint.vlan_id)
                            mode = 'vlan'
        bgp_as = conf.dual_cpe_site_services.bgp_as
        if hasattr(conf.dual_cpe_site_services.cpe_secondary.vrfs.vrf, 'bgp_address_family'):
            bgp_address_family = conf.dual_cpe_site_services.cpe_secondary.vrfs.vrf.bgp_address_family
    elif entity == 'cpe_dual':
        device = devicemgr.getDeviceById(conf.single_cpe_dual_wan_site_services.cpe.device_ip)
        if hasattr(conf.single_cpe_dual_wan_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.single_cpe_dual_wan_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if endpoint.dps == 'true':
                    if hasattr(endpoint, 'vrf'):
                        lan_vrf = endpoint.vrf
                    if endpoint.interface_type == 'Physical':
                        interface_name = endpoint.interface_name
                        mode = 'l3-interface'
                    elif endpoint.interface_type == 'Sub-Interface':
                        interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                        mode = 'sub-interface'
                    elif endpoint.interface_type == 'SVI':
                            interface_name = "Vlan" + str(endpoint.vlan_id)
                            mode = 'vlan'
        bgp_as = conf.single_cpe_dual_wan_site_services.bgp_as
        if hasattr(conf.single_cpe_dual_wan_site_services.cpe.vrfs.vrf, 'bgp_address_family'):
            bgp_address_family = conf.single_cpe_dual_wan_site_services.cpe.vrfs.vrf.bgp_address_family
    elif entity == 'cpe_primary_dual':
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip)
        if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip:
                    if endpoint.dps == 'true':
                        if hasattr(endpoint, 'vrf'):
                            lan_vrf = endpoint.vrf
                        if endpoint.interface_type == 'Physical':
                            interface_name = endpoint.interface_name
                            mode = 'l3-interface'
                        elif endpoint.interface_type == 'Sub-Interface':
                            interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                            mode = 'sub-interface'
                        elif endpoint.interface_type == 'SVI':
                            interface_name = "Vlan" + str(endpoint.vlan_id)
                            mode = 'vlan'
        bgp_as = conf.dual_cpe_dual_wan_site_services.bgp_as
        if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary.vrfs.vrf, 'bgp_address_family'):
            bgp_address_family = conf.dual_cpe_dual_wan_site_services.cpe_primary.vrfs.vrf.bgp_address_family
    elif entity == 'cpe_secondary_dual' or entity == 'cpe_secondary_only_dual':
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip)
        if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip:
                    if endpoint.dps == 'true':
                        if hasattr(endpoint, 'vrf'):
                            lan_vrf = endpoint.vrf
                        if endpoint.interface_type == 'Physical':
                            interface_name = endpoint.interface_name
                            mode = 'l3-interface'
                        elif endpoint.interface_type == 'Sub-Interface':
                            interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                            mode = 'sub-interface'
                        elif endpoint.interface_type == 'SVI':
                            interface_name = "Vlan" + str(endpoint.vlan_id)
                            mode = 'vlan'
        bgp_as = conf.dual_cpe_dual_wan_site_services.bgp_as
        if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary.vrfs.vrf, 'bgp_address_family'):
            bgp_address_family = conf.dual_cpe_dual_wan_site_services.cpe_secondary.vrfs.vrf.bgp_address_family
    elif entity == 'cpe_primary_triple':
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_primary.device_ip)
        if hasattr(conf.triple_cpe_site_services.cpe_lan, 'end_points'):
            obj = util.convert_to_list(conf.triple_cpe_site_services.cpe_lan.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.triple_cpe_site_services.cpe_primary.device_ip:
                    if endpoint.dps == 'true':
                        if hasattr(endpoint, 'vrf'):
                            lan_vrf = endpoint.vrf
                        if endpoint.interface_type == 'Physical':
                            interface_name = endpoint.interface_name
                            mode = 'l3-interface'
                        elif endpoint.interface_type == 'Sub-Interface':
                            interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                            mode = 'sub-interface'
                        elif endpoint.interface_type == 'SVI':
                            interface_name = "Vlan" + str(endpoint.vlan_id)
                            mode = 'vlan'
        bgp_as = conf.triple_cpe_site_services.bgp_as
        if hasattr(conf.triple_cpe_site_services.cpe_primary.vrfs.vrf, 'bgp_address_family'):
            bgp_address_family = conf.triple_cpe_site_services.cpe_primary.vrfs.vrf.bgp_address_family

    inputdict = kwargs['inputdict']
    vrf = inputdict['vrf']
    rd = inputdict['rd']
    rt_import = inputdict['rt_import']
    rt_export = inputdict['rt_export']
    if util.isEmpty(vrf):
        vrf = "GLOBAL"
    is_vrf_xml_output = yang.Sdk.getData(device.url, '', sdata.getTaskId())
    is_vrf_obj = util.parseXmlString(is_vrf_xml_output)
    util.log_debug("is_vrf_obj is:", is_vrf_obj)
    if not hasattr(is_vrf_obj.device, 'vrfs'):
        yang.Sdk.createData(device.url, '<vrfs/>', sdata.getSession(), False)

    if util.isNotEmpty(vrf):
        # vrfobj = vrfs.vrf.vrf()
        # vrfobj.name = vrf
        # if util.isNotEmpty(rd):
        #     vrfobj.rd = rd
        # if util.isNotEmpty(rt_import):
        #     vrfobj.rt_import.add(rt_import=rt_import)
        # if util.isNotEmpty(rt_export):
        #     vrfobj.rt_export.add(rt_export=rt_export)
        # yang.Sdk.createData(device.url + '/vrfs', vrfobj.getxml(filter=True), sdata.getSession())
        uri = sdata.getRcPath()
        uri_list = uri.split('/',5)
        url = '/'.join(uri_list[0:4])

        if vrf != 'GLOBAL':
            xml_output = yang.Sdk.getData(url+"/vrfs", '',sdata.getTaskId())
            obj = util.parseXmlString(xml_output)
            util.log_debug( "obj: ",obj)

            if hasattr(obj.vrfs, 'vrf'):
                obj.vrfs.vrf = util.convert_to_list(obj.vrfs.vrf)
                for vrf_local in obj.vrfs.vrf:
                    if vrf_local.vrf_name == vrf:
                        vrfobj = vrfs.vrf.vrf()
                        vrfobj.name = vrf_local.vrf_name
                        if util.isNotEmpty(vrf_local.rd):
                            vrfobj.rd = vrf_local.rd
                        if hasattr(vrf_local, 'description'):
                            if util.isNotEmpty(vrf_local.description):
                                vrfobj.description = vrf_local.description
                        if util.isNotEmpty(vrf_local.vrf_definition_mode):
                            vrfobj.vrf_definition_mode = vrf_local.vrf_definition_mode
                        yang.Sdk.createData(device.url + '/l3features:vrfs', vrfobj.getxml(filter=True), sdata.getSession())
                        if hasattr(vrf_local, 'rt_import'):
                            vrf_local.rt_import = util.convert_to_list(vrf_local.rt_import)
                            for rtimport in vrf_local.rt_import:
                                vrfobj1 = vrfs.vrf.rt_import.rt_import()
                                if util.isNotEmpty(rtimport.rt_import):
                                    vrfobj1.rt_import = rtimport.rt_import
                                import_url = device.url + '/l3features:vrfs/vrf=%s' % (vrf)
                                yang.Sdk.createData(import_url, vrfobj1.getxml(filter=True), sdata.getSession())
                        if hasattr(vrf_local, 'rt_export'):
                            vrf_local.rt_export = util.convert_to_list(vrf_local.rt_export)
                            for rtexport in vrf_local.rt_export:
                                vrfobj1 = vrfs.vrf.rt_export.rt_export()
                                if util.isNotEmpty(rtexport.rt_export):
                                    vrfobj1.rt_export = rtexport.rt_export
                                export_url = device.url + '/l3features:vrfs/vrf=%s' % (vrf)
                                yang.Sdk.createData(export_url, vrfobj1.getxml(filter=True), sdata.getSession())
                        if hasattr(vrf_local, 'import_map'):
                            vrf_local.import_map = util.convert_to_list(vrf_local.import_map)
                            for importmap in vrf_local.import_map:
                                vrfobj1 = vrfs.vrf.import_map.import_map()
                                if util.isNotEmpty(importmap.import_map):
                                    route_maps(importmap.import_map, device, sdata)
                                    vrfobj1.import_map = importmap.import_map
                                if hasattr(importmap, 'ipv4'):
                                    vrfobj1.ipv4 = importmap.ipv4
                                if hasattr(importmap, 'traffic'):
                                    if util.isNotEmpty(importmap.traffic):
                                        vrfobj1.table = importmap.traffic
                                if hasattr(importmap, 'upper_limit'):
                                    if util.isNotEmpty(importmap.upper_limit):
                                        vrfobj1.upper_limit = importmap.upper_limit
                                importmap_url = device.url + '/l3features:vrfs/vrf=%s' % (vrf)
                                yang.Sdk.createData(importmap_url, vrfobj1.getxml(filter=True), sdata.getSession())
                        if hasattr(vrf_local, 'export_map'):
                            vrf_local.export_map = util.convert_to_list(vrf_local.export_map)
                            for exportmap in vrf_local.export_map:
                                vrfobj1 = vrfs.vrf.export_map.export_map()
                                if util.isNotEmpty(exportmap.export_map):
                                    route_maps(exportmap.export_map, device, sdata)
                                    vrfobj1.export_map = exportmap.export_map
                                if hasattr(exportmap, 'ipv4'):
                                    vrfobj1.ipv4 = exportmap.ipv4
                                if hasattr(exportmap, 'traffic'):
                                    if util.isNotEmpty(exportmap.traffic):
                                        vrfobj1.table = exportmap.traffic
                                if hasattr(exportmap, 'upper_limit'):
                                    if util.isNotEmpty(exportmap.upper_limit):
                                        vrfobj1.upper_limit = exportmap.upper_limit
                                importmap_url = device.url + '/l3features:vrfs/vrf=%s' % (vrf)
                                yang.Sdk.createData(importmap_url, vrfobj1.getxml(filter=True), sdata.getSession())
        else:
            vrfobj = vrfs.vrf.vrf()
            vrfobj.name = vrf
            if not yang.Sdk.dataExists('/controller:devices/device=%s/l3features:vrfs/vrf=%s' %(device.device.id, vrf)):
                yang.Sdk.createData(device.url + '/l3features:vrfs', vrfobj.getxml(filter=True), sdata.getSession())

    if inputdict['lan_interface'] == 'true':
        intf_obj = interfaces.interface.interface()
        if util.isEmpty(interface_name) or interface_name is None:
            raise Exception('Please check DPS flag is checked on Site Service LAN interface')
        intf_obj.name = interface_name
        intf_obj.long_name = interface_name
        intf_obj.mode = mode
        if inputdict['hierarchical_inbound_policy'] == 'false':
            if util.isNotEmpty(inputdict['hierarchical_policy']):
                hierarchical_policy_class(entity, inputdict['hierarchical_policy'], device, sdata)
                intf_obj.inbound_qos = inputdict['hierarchical_policy']
        elif inputdict['hierarchical_inbound_policy'] == 'true':
            if util.isNotEmpty(inputdict['hierarchical_policy']):
                hierarchical_policy_class(entity, inputdict['hierarchical_policy'], device, sdata)
                intf_obj.inbound_qos = inputdict['hierarchical_policy']

        if inputdict['vrf_receive'] == 'true':
            if vrf is not None and vrf != 'GLOBAL':
                intf_obj.vrf_receive = vrf
        if inputdict['bgp_policy'] == 'true':
            intf_obj.bgp_policy = 'true'
        if inputdict['bgp_policy_qos'] == 'true':
            intf_obj.bgp_policy_qos = 'true'
        if util.isNotEmpty(inputdict['pbr_policy']):
            route_maps(inputdict['pbr_policy'], device, sdata)
            intf_obj.pbr_policy = inputdict['pbr_policy']
        yang.Sdk.createData(device.url+'/interface:interfaces', intf_obj.getxml(filter=True), sdata.getSession(), False)

    if inputdict['b2b_interface'] == 'true':
        if entity == 'cpe_primary':
            if lan_vrf is not None:
                vrf = lan_vrf
            obj = util.convert_to_list(conf.dual_cpe_site_services.cpe_primary_cpe_secondary_ic.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.dual_cpe_site_services.cpe_primary.device_ip:
                    if endpoint.dps == "true":
                        if endpoint.interface_type == 'Physical':
                            interface_name = endpoint.interface_name
                        if endpoint.interface_type == 'Sub-Interface':
                            interface_name = endpoint.interface_name
        elif entity == 'cpe_secondary':
            obj = util.convert_to_list(conf.dual_cpe_site_services.cpe_primary_cpe_secondary_ic.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.dual_cpe_site_services.cpe_secondary.device_ip:
                    if endpoint.dps == "true":
                        if endpoint.interface_type == 'Physical':
                            interface_name = endpoint.interface_name
                        if endpoint.interface_type == 'Sub-Interface':
                            interface_name = endpoint.interface_name
        elif entity == 'cpe_primary_dual':
            if lan_vrf is not None:
                vrf = lan_vrf
            obj = util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_primary_cpe_secondary_ic.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip:
                    if endpoint.dps == "true":
                        if endpoint.interface_type == 'Physical':
                            interface_name = endpoint.interface_name
                        if endpoint.interface_type == 'Sub-Interface':
                            interface_name = endpoint.interface_name
        elif entity == 'cpe_secondary_dual':
            obj = util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_primary_cpe_secondary_ic.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip:
                    if endpoint.dps == "true":
                        if endpoint.interface_type == 'Physical':
                            interface_name = endpoint.interface_name
                        if endpoint.interface_type == 'Sub-Interface':
                            interface_name = endpoint.interface_name
        elif entity == 'cpe_primary_triple':
            obj = util.convert_to_list(conf.triple_cpe_site_services.cpe_primary_cpe_secondary_ic.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.triple_cpe_site_services.cpe_primary.device_ip:
                    if endpoint.dps == "true":
                        if endpoint.interface_type == 'Physical':
                            interface_name = endpoint.interface_name
                        if endpoint.interface_type == 'Sub-Interface':
                            interface_name = endpoint.interface_name
        elif entity == 'cpe_secondary_triple':
            obj = util.convert_to_list(conf.triple_cpe_site_services.cpe_primary_cpe_secondary_ic.end_points)
            for endpoint in obj:
                if endpoint.device_ip == conf.triple_cpe_site_services.cpe_secondary.device_ip:
                    if endpoint.dps == "true":
                        if endpoint.interface_type == 'Physical':
                            interface_name = endpoint.interface_name
                        if endpoint.interface_type == 'Sub-Interface':
                            interface_name = endpoint.interface_name

        if util.isEmpty(interface_name) or interface_name is None:
            raise Exception('Please check DPS flag is checked on Site Service B2B interface')
        mode = 'sub-interface'
        interface_name = interface_name + '.' + str(inputdict['vlan_id'])
        cidr = inputdict['cidr']
        interface_ip = inputdict['interface_ip']
        ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr)
        ip_addr_obj = ip_addr.ipam_pool_obj
        prefix = util.IPPrefix(ip_addr_obj.cidr)
        netmask = prefix.netmask
        if util.isEmpty(interface_ip) or interface_ip == None:
            used_ips_list = get_used_ip_list_from_ippool(ip_addr_obj.name, sdata)
            interface_ip = get_freeip_from_cidr(ip_addr_obj.cidr, used_ips_list)
            add_ipaddress_entries(ip_addr_obj.name, interface_ip, sdata)
        else:
            add_ipaddress_entries(ip_addr_obj.name, interface_ip, sdata)
        payload = "<interface-ip>%s</interface-ip>" % interface_ip
        serv_uri = sdata.getRcPath()
        yang.Sdk.createData(serv_uri, payload, sdata.getSession())
        intf_obj = interfaces.interface.interface()
        if util.isEmpty(interface_name):
            raise Exception('Please check b2b interface on site')
        intf_obj.name = interface_name
        intf_obj.long_name = interface_name
        intf_obj.mode = mode
        if util.isNotEmpty(inputdict['b2b_description']):
            intf_obj.description = inputdict['b2b_description']
        intf_obj.vlan = inputdict['vlan_id']
        if vrf is not None and vrf != 'GLOBAL':
            uri1 = sdata.getRcPath()
            uri_list1 = uri1.split('/',5)
            url1 = '/'.join(uri_list1[0:4])
            xml_output = yang.Sdk.getData(url1+"/vrfs/vrf="+str(vrf), '', sdata.getTaskId())
            obj_local = util.parseXmlString(xml_output)
            util.log_debug("obj_local: ", obj_local)
            intf_obj.vrf_definition_mode = obj_local.vrf.vrf_definition_mode
            intf_obj.vrf = vrf
        intf_obj.ip_address = interface_ip
        intf_obj.netmask = netmask
        yang.Sdk.createData(device.url+'/interface:interfaces', intf_obj.getxml(filter=True), sdata.getSession())

    if inputdict['loopback'] == 'true':
        int_id = inputdict['loopback_interface_id']
        loopback_int_id = 'Loopback' + str(int_id)
        desc = inputdict['description']
        cidr = inputdict['cidr_loopback']
        ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr)
        ip_addr_obj = ip_addr.ipam_pool_obj
        prefix = util.IPPrefix(ip_addr_obj.cidr)
        netmask = prefix.netmask
        loopback_ip = inputdict['loopback_ip']
        if util.isEmpty(loopback_ip) or loopback_ip is None:
            used_ips_list = get_used_ip_list_from_ippool(ip_addr_obj.name, sdata)
            loopback_ip = get_freeip_from_cidr(ip_addr_obj.cidr, used_ips_list)
            add_ipaddress_entries(ip_addr_obj.name, loopback_ip, sdata)
        else:
            add_ipaddress_entries(ip_addr_obj.name, loopback_ip, sdata)
        payload = "<loopback-ip>%s</loopback-ip>" % loopback_ip
        serv_uri = sdata.getRcPath()
        yang.Sdk.createData(serv_uri, payload, sdata.getSession())
        intf_obj = interfaces.interface.interface()
        if util.isNotEmpty(loopback_int_id):
            print 'loopback_int_id:', loopback_int_id
            intf_obj.name = loopback_int_id
            intf_obj.long_name = loopback_int_id
        if util.isNotEmpty(desc):
            intf_obj.description = desc
        if util.isNotEmpty(loopback_ip):
            intf_obj.ip_address = loopback_ip
            intf_obj.netmask = netmask
        yang.Sdk.createData(device.url+'/interface:interfaces', intf_obj.getxml(filter=True), sdata.getSession())

    if inputdict['ospf'] == 'true':
        if entity == 'cpe_primary' or entity == 'cpe_primary_dual':
            if lan_vrf is not None:
                vrf = lan_vrf
        ospf_obj = vrfs.vrf.router_ospf.router_ospf()
        ospf_obj.process_id = inputdict['ospf_id']
        ospf_obj.router_id = inputdict['router_id']
        if inputdict['vrf_lite'] == 'true':
            ospf_obj.vrf_lite = inputdict['vrf_lite']
        ospf_url = device.url + '/l3features:vrfs/vrf=%s' % (vrf)
        yang.Sdk.createData(ospf_url, ospf_obj.getxml(filter=True), sdata.getSession())
        ospf_url1 = ospf_url + '/router-ospf=%s' %(inputdict['ospf_id'])
        yang.Sdk.createData(ospf_url1, '<redistribute/>', sdata.getSession())
        if util.isNotEmpty(inputdict['static_route_map']):
            route_maps(inputdict['static_route_map'], device, sdata)
            ospf_static_obj = vrfs.vrf.router_ospf.redistribute.ospf_redistribute.ospf_redistribute()
            ospf_static_obj.protocol = 'static'
            ospf_static_obj.route_map = inputdict['static_route_map']
            ospf_static_obj.bgp_as_number = None
            ospf_static_url = device.url + '/l3features:vrfs/vrf=%s/router-ospf=%s/redistribute' % (vrf, inputdict['ospf_id'])
            yang.Sdk.createData(ospf_static_url, ospf_static_obj.getxml(filter=True), sdata.getSession())

        if util.isNotEmpty(inputdict['connected_route_map']):
            if util.isEmpty(interface_name):
                raise Exception('Please check interface on cpe in site')
            route_maps(inputdict['connected_route_map'], device, sdata, interface_name)
            ospf_connect_obj = vrfs.vrf.router_ospf.redistribute.ospf_redistribute.ospf_redistribute()
            ospf_connect_obj.protocol = 'connected'
            ospf_connect_obj.route_map = inputdict['connected_route_map']
            ospf_connect_obj.bgp_as_number = None
            ospf_connect_url = device.url + '/l3features:vrfs/vrf=%s/router-ospf=%s/redistribute' % (vrf, inputdict['ospf_id'])
            yang.Sdk.createData(ospf_connect_url, ospf_connect_obj.getxml(filter=True), sdata.getSession())

        if inputdict['lan_ospf_redistribution'] == 'true':
            if util.isNotEmpty(inputdict['ospf_redistribution_id']):
                ospf_obj = vrfs.vrf.router_ospf.router_ospf()
                ospf_obj.process_id = inputdict['ospf_redistribution_id']
                ospf_obj.router_id = inputdict['router_id']
                ospf_url = device.url + '/l3features:vrfs/vrf=%s' % (vrf)
                #yang.Sdk.createData(ospf_url, ospf_obj.getxml(filter=True), sdata.getSession())
            else:
                inputdict['ospf_redistribution_id'] = inputdict['ospf_id']

            ospf_static_obj = vrfs.vrf.router_ospf.redistribute.ospf_redistribute.ospf_redistribute()
            ospf_static_obj.protocol = 'ospf'
            ospf_static_obj.bgp_as_number = None
            ospf_static_obj.process_id_entry = inputdict['ospf_redistribution_id']
            if util.isNotEmpty(inputdict['ospf_route_map']):
                route_maps(inputdict['ospf_route_map'], device, sdata)
                ospf_static_obj.route_map = inputdict['ospf_route_map']
            if util.isNotEmpty(inputdict['ospf_tag']):
                ospf_static_obj.tag = inputdict['ospf_tag']
            if util.isNotEmpty(inputdict['ospf_metric']):
                ospf_static_obj.value1 = inputdict['ospf_metric']
            if util.isNotEmpty(inputdict['ospf_metric_type']):
                ospf_static_obj.value2 = inputdict['ospf_metric_type']
            ospf_static_url = device.url + '/l3features:vrfs/vrf=%s/router-ospf=%s/redistribute' % (vrf, inputdict['ospf_id'])
            yang.Sdk.createData(ospf_static_url, ospf_static_obj.getxml(filter=True), sdata.getSession())

        if inputdict['lan_ebgp_redistribution'] == 'true':
            if util.isNotEmpty(inputdict['bgp_route_map']):
                route_maps(inputdict['bgp_route_map'], device, sdata)
            ospf_static_obj = vrfs.vrf.router_ospf.redistribute.ospf_redistribute.ospf_redistribute()
            ospf_static_obj.protocol = 'bgp'
            ospf_static_obj.bgp_as_number = bgp_as
            ospf_static_obj.route_map = inputdict['bgp_route_map']
            if util.isNotEmpty(inputdict['bgp_tag']):
                ospf_static_obj.tag = inputdict['bgp_tag']
            if util.isNotEmpty(inputdict['bgp_metric']):
                ospf_static_obj.value1 = inputdict['bgp_metric']
            if util.isNotEmpty(inputdict['bgp_metric_type']):
                ospf_static_obj.value2 = inputdict['bgp_metric_type']
            ospf_static_url = device.url + '/l3features:vrfs/vrf=%s/router-ospf=%s/redistribute' % (vrf, inputdict['ospf_id'])
            yang.Sdk.createData(ospf_static_url, ospf_static_obj.getxml(filter=True), sdata.getSession())

    if inputdict['bgp'] == 'true':
        bgpobj1 = vrfs.vrf.router_bgp.router_bgp()
        if util.isNotEmpty(bgp_as):
            bgpobj1.as_number = bgp_as
            if bgp_address_family is not None:
                bgpobj1.address_family = bgp_address_family
        #bgpobj1.address_family = "ipv4"
        if util.isNotEmpty(inputdict['qppb_policy']):
            route_maps(inputdict['qppb_policy'], device, sdata)
            bgpobj1.qppb_policy = inputdict['qppb_policy']
        if inputdict['bgp_vrf'] is None:
            vrf_global = 'GLOBAL'
            router_bgp_url = device.url + '/l3features:vrfs/vrf=%s' % (vrf_global)
        else:
            vrf_bgp = inputdict['bgp_vrf']
            router_bgp_url = device.url + '/l3features:vrfs/vrf=%s' % (vrf_bgp)

        yang.Sdk.createData(router_bgp_url, bgpobj1.getxml(filter=True), sdata.getSession(), False)

        """
        if entity != 'cpe_primary':
            bgpobj2 = vrfs.vrf.router_bgp.router_bgp()
            if util.isNotEmpty(bgp_as):
                bgpobj2.as_number = bgp_as
            if vrf != "GLOBAL":
                bgpobj2.address_family = "ipv4"
            router_bgp_url = device.url + '/vrfs/vrf=%s' % (vrf)
            yang.Sdk.createData(router_bgp_url, bgpobj2.getxml(filter=True), sdata.getSession())
        """

        vrf1 = inputdict['bgp_vrf']

        if vrf1 is None:
            vrf1 = 'GLOBAL'

        if util.isNotEmpty(inputdict['redistribute_connected']):
            if util.isEmpty(interface_name):
                raise Exception('Please check interface on cpe in site')
            route_maps(inputdict['redistribute_connected'], device, sdata, interface_name)
            rebgpredisobj1 = vrfs.vrf.router_bgp.redistribute.redistribute()
            rebgpredisobj1.protocol = 'connected'
            rebgpredisobj1.route_map = inputdict['redistribute_connected']
            router_bgp_redist_url = device.url + '/l3features:vrfs/vrf=%s/router-bgp' % (vrf1)
            yang.Sdk.createData(router_bgp_redist_url, rebgpredisobj1.getxml(filter=True), sdata.getSession(), False)

        if util.isNotEmpty(inputdict['redistribute_static']):
            route_maps(inputdict['redistribute_static'], device, sdata)
            rebgpredisobj1 = vrfs.vrf.router_bgp.redistribute.redistribute()
            rebgpredisobj1.protocol = 'static'
            rebgpredisobj1.route_map = inputdict['redistribute_static']
            router_bgp_redist_url = device.url + '/l3features:vrfs/vrf=%s/router-bgp' % (vrf1)
            yang.Sdk.createData(router_bgp_redist_url, rebgpredisobj1.getxml(filter=True), sdata.getSession(), False)

        if util.isNotEmpty(inputdict['import_route_map']):
            route_maps(inputdict['import_route_map'], device, sdata)

    if inputdict['tunnel'] == 'true':
        dmvpn_profile = inputdict['dmvpn_profile']
        tunnel_ip_address = inputdict['tunnel_interface_ip_address']
        bandwidth = inputdict['tunnel_bandwidth']
        tunnel_description = inputdict['tunnel_interface_description']
        tunnel_fvrf = inputdict['tunnel_fvrf']

        uri = sdata.getRcPath()
        uri_list = uri.split('/', 5)
        url = '/'.join(uri_list[0:4])

        xml_output = yang.Sdk.getData(url+"/dmvpn-tunnel-profiles/dmvpn-tunnel-profile="+str(dmvpn_profile), '', sdata.getTaskId())
        obj_dmvpn = util.parseXmlString(xml_output)
        yang.Sdk.createData(device.url, '<dmvpntunnels/>', sdata.getSession(), False)
        dmvpn_obj = dmvpntunnels.dmvpntunnel.dmvpntunnel()
        if vrf != 'GLOBAL':
            uri1 = sdata.getRcPath()
            uri_list1 = uri1.split('/',5)
            url1 = '/'.join(uri_list1[0:4])
            xml_output = yang.Sdk.getData(url1+"/vrfs/vrf="+str(vrf), '', sdata.getTaskId())
            obj_local = util.parseXmlString(xml_output)
            util.log_debug("obj_local: ", obj_local)
            dmvpn_obj.vrf_definition_mode = obj_local.vrf.vrf_definition_mode
            dmvpn_obj.vrf_name = vrf

        if tunnel_fvrf is not None:
            dmvpn_obj.front_vrf_name = tunnel_fvrf

        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'delay'):
            delay = obj_dmvpn.dmvpn_tunnel_profile.delay
        else:
            delay = None
        if delay is not None:
            dmvpn_obj.delay = delay

        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'no_nhrp_route_watch'):
            no_nhrp_route_watch = obj_dmvpn.dmvpn_tunnel_profile.no_nhrp_route_watch
        else:
            no_nhrp_route_watch = None
        if no_nhrp_route_watch is not None:
            dmvpn_obj.no_nhrp_route_watch = no_nhrp_route_watch

        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'nhrp_reg_no_uniq'):
            nhrp_reg_no_uniq = obj_dmvpn.dmvpn_tunnel_profile.nhrp_reg_no_uniq
        else:
            nhrp_reg_no_uniq = None
        if nhrp_reg_no_uniq is not None:
            dmvpn_obj.nhrp_reg_no_uniq = nhrp_reg_no_uniq

        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'nhrp_reg_timeout'):
            nhrp_reg_timeout = obj_dmvpn.dmvpn_tunnel_profile.nhrp_reg_timeout
        else:
            nhrp_reg_timeout = None
        if nhrp_reg_timeout is not None:
            dmvpn_obj.nhrp_reg_timeout = nhrp_reg_timeout

        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'nhrp_holdtime'):
            nhrp_holdtime = obj_dmvpn.dmvpn_tunnel_profile.nhrp_holdtime
        else:
            if obj_dmvpn.dmvpn_tunnel_profile.nhrp_holdtime == "600":
                nhrp_holdtime = None
            else:
               nhrp_holdtime = None
        if nhrp_holdtime is not None:
            dmvpn_obj.nhrp_holdtime = nhrp_holdtime

        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'nhrp_redirect'):
            nhrp_redirect = obj_dmvpn.dmvpn_tunnel_profile.nhrp_redirect
        else:
            nhrp_redirect = None
        if nhrp_redirect is not None:
            dmvpn_obj.nhrp_redirect = nhrp_redirect

        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'nhrp_shortcut'):
            nhrp_shortcut = obj_dmvpn.dmvpn_tunnel_profile.nhrp_shortcut
        else:
            nhrp_shortcut = None
        if nhrp_shortcut is not None:
            dmvpn_obj.nhrp_shortcut = nhrp_shortcut

        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'tunnel_keepalive_period'):
            tunnel_keepalive_period = obj_dmvpn.dmvpn_tunnel_profile.tunnel_keepalive_period
        else:
            tunnel_keepalive_period = None
        if tunnel_keepalive_period is not None:
            dmvpn_obj.tunnel_keepalive_period = tunnel_keepalive_period

        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'tunnel_keepalive_retries'):
            tunnel_keepalive_retries = obj_dmvpn.dmvpn_tunnel_profile.tunnel_keepalive_retries
        else:
            tunnel_keepalive_retries = None
        if tunnel_keepalive_retries is not None:
            dmvpn_obj.tunnel_keepalive_retries = tunnel_keepalive_retries

        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'if_state_nhrp'):
            if_state_nhrp = obj_dmvpn.dmvpn_tunnel_profile.if_state_nhrp
        else:
            if_state_nhrp = None
        if if_state_nhrp is not None:
            dmvpn_obj.if_state_nhrp = if_state_nhrp

        if util.isNotEmpty(bandwidth):
            dmvpn_obj.bandwidth = bandwidth
        if inputdict['hub'] == 'true':
            dmvpn_obj.type = "HUB"
        else:
            dmvpn_obj.type = "SPOKE"
        dmvpn_obj.name = obj_dmvpn.dmvpn_tunnel_profile.tunnel_id
        dmvpn_obj.nhrp_auth_key = obj_dmvpn.dmvpn_tunnel_profile.nhrp_authentication_key
        dmvpn_obj.nhrp_network_id = obj_dmvpn.dmvpn_tunnel_profile.nhrp_nw_id
        dmvpn_obj.tunnel_key = obj_dmvpn.dmvpn_tunnel_profile.tunnel_key
        dmvpn_obj.description = tunnel_description
        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'mtu'):
            mtu = obj_dmvpn.dmvpn_tunnel_profile.mtu
        else:
            mtu = None
        if util.isNotEmpty(mtu):
            dmvpn_obj.mtu = mtu
        else:
            dmvpn_obj.mtu = "1400"
        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'tcp_adjust_mss'):
            tcp_adjust_mss = obj_dmvpn.dmvpn_tunnel_profile.tcp_adjust_mss
        else:
            tcp_adjust_mss = None
        if util.isNotEmpty(tcp_adjust_mss):
            dmvpn_obj.tcp_adjust_mss = tcp_adjust_mss
        else:
            dmvpn_obj.tcp_adjust_mss = "1360"
        ip_addr = IpamPoolID(sdata.getTaskId(), sdata, obj_dmvpn.dmvpn_tunnel_profile.tunnel_prefix)
        ip_addr_obj = ip_addr.ipam_pool_obj
        if util.isEmpty(tunnel_ip_address):
            used_ips_list = get_used_ip_list_from_ippool(ip_addr_obj.name, sdata)
            tunnel_ip_address = get_freeip_from_cidr(ip_addr_obj.cidr, used_ips_list)
            add_ipaddress_entries(ip_addr_obj.name, tunnel_ip_address, sdata)
        else:
            add_ipaddress_entries(ip_addr_obj.name, tunnel_ip_address, sdata)

        if obj_dmvpn.dmvpn_tunnel_profile.wan_public_ip == tunnel_ip_address:
            add_ipaddress_entries(ip_addr_obj.name, tunnel_ip_address, sdata)
        if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'nhrp_maps'):
            obj_dmvpn.dmvpn_tunnel_profile.nhrp_maps = util.convert_to_list(obj_dmvpn.dmvpn_tunnel_profile.nhrp_maps)
            for nhrpmaps in obj_dmvpn.dmvpn_tunnel_profile.nhrp_maps:
                if nhrpmaps.wan_public_ip == tunnel_ip_address:
                    add_ipaddress_entries(ip_addr_obj.name, tunnel_ip_address, sdata)

        dmvpn_obj.ipaddress = tunnel_ip_address

        payload = "<tunnel-interface-ip-address>%s</tunnel-interface-ip-address>" % tunnel_ip_address
        serv_uri = sdata.getRcPath()
        yang.Sdk.createData(serv_uri, payload, sdata.getSession(), False)

        tunnel_prefix = ip_addr_obj.cidr
        netmask = util.IPPrefix(tunnel_prefix).netmask
        dmvpn_obj.netmask = netmask
        dmvpn_obj.tunnel_mode = 'gre'
        tunnel_source = 'Loopback' + str(inputdict['loopback_interface_id'])
        dmvpn_obj.tunnel_source = tunnel_source
        dmvpn_obj.routing_protocol = 'ospf'
        yang.Sdk.createData(device.url+'/dmvpn:dmvpntunnels', dmvpn_obj.getxml(filter=True), sdata.getSession())

        #Create Interface Node in device model
        intf_obj_tun = interfaces.interface.interface()
        intf_obj_tun.name = "Tunnel" + str(obj_dmvpn.dmvpn_tunnel_profile.tunnel_id)
        intf_obj_tun.long_name = "Tunnel" + str(obj_dmvpn.dmvpn_tunnel_profile.tunnel_id)

        yang.Sdk.createData(device.url+'/interface:interfaces', intf_obj_tun.getxml(filter=True), sdata.getSession(), True)

        if inputdict['hub'] != 'true':
            dmvpn_obj_nhrp = dmvpntunnels.dmvpntunnel.nhrp_maps.nhrp_maps()
            dmvpn_obj_nhrp.sourceip = obj_dmvpn.dmvpn_tunnel_profile.wan_tunnel_ip
            dmvpn_obj_nhrp.nhrp_type = 'nhs'
            dmvpn_obj_nhrp.destip = obj_dmvpn.dmvpn_tunnel_profile.wan_public_ip
            yang.Sdk.createData(device.url+'/dmvpn:dmvpntunnels/dmvpntunnel=%s' % (obj_dmvpn.dmvpn_tunnel_profile.tunnel_id), dmvpn_obj_nhrp.getxml(filter=True), sdata.getSession())
            if hasattr(obj_dmvpn.dmvpn_tunnel_profile, 'nhrp_maps'):
                obj_dmvpn.dmvpn_tunnel_profile.nhrp_maps = util.convert_to_list(obj_dmvpn.dmvpn_tunnel_profile.nhrp_maps)
                for nhrpmaps in obj_dmvpn.dmvpn_tunnel_profile.nhrp_maps:
                    dmvpn_obj_nhrp.sourceip = nhrpmaps.wan_tunnel_ip
                    dmvpn_obj_nhrp.nhrp_type = 'nhs'
                    dmvpn_obj_nhrp.destip = nhrpmaps.wan_public_ip
                    yang.Sdk.createData(device.url+'/dmvpn:dmvpntunnels/dmvpntunnel=%s' % (obj_dmvpn.dmvpn_tunnel_profile.tunnel_id), dmvpn_obj_nhrp.getxml(filter=True), sdata.getSession())

def hierarchical_policy_class(entity, hierarchical_policy, device, sdata):
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])

    xml_output = yang.Sdk.getData(url+"/qos-service/hierarchical-policy/policy="+str(hierarchical_policy), '',sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    util.log_debug( "obj: ",obj)
    device.addQosPolicyMapsContainer(sdata.getSession())

    map_obj = policy_maps.policy_map.policy_map()
    map_obj.name = obj.policy.name
    yang.Sdk.createData(device.url+"/qos:policy-maps", map_obj.getxml(filter=True), sdata.getSession())

    if hasattr(obj.policy, 'classes'):
        obj.policy.classes = util.convert_to_list(obj.policy.classes)
        log("classes sequence:%s" %(obj.policy.classes))
        for class_entry in obj.policy.classes:
            cls_obj = policy_maps.policy_map.class_entry.class_entry()
            if util.isNotEmpty(class_entry.class_name):
                class_map(entity, url, class_entry.class_name, device, sdata)
                cls_obj.class_name = class_entry.class_name
            if util.isNotEmpty(class_entry.child_qos_policy):
                cls_obj.service_policy = class_entry.child_qos_policy
                qos_child(entity, class_entry.child_qos_policy, device, sdata)
            yang.Sdk.createData(device.url+"/qos:policy-maps/policy-map=%s" %(obj.policy.name), cls_obj.getxml(filter=True), sdata.getSession())


def qos_child(entity, qos_policy, dev, sdata):
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])

    xml_output = yang.Sdk.getData(url+"/qos-service/policies/policy="+str(qos_policy), '',sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    print "obj: ",obj
    print "xml of policy map obj: ",obj.toXml()
    dev.addQosPolicyMapsContainer(sdata.getSession())
    policy_name = obj.policy.name
    map_obj = policy_maps.policy_map.policy_map()
    map_obj.name = policy_name
    yang.Sdk.createData(dev.url+"/qos:policy-maps", map_obj.getxml(filter=True), sdata.getSession())
    for cls in obj.policy.classes.get_field_value('class_name', True):
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_name = cls.name
        # Generates Configs for Class Maps
        if cls_name != 'class-default' and cls_name != 'CLASS-DEFAULT':
            class_map(entity, url, cls_name, dev, sdata)
            cls_obj.class_name = cls_name
        else:
            cls_obj.class_name = 'class-default'
        packet_handling = cls.get_field_value('packet_handling')
        print "packet_handling: ",packet_handling
        if packet_handling is not None and hasattr(packet_handling,"remarking") and packet_handling.remarking is not None:
            print "remarking: ",packet_handling.remarking
            remarking = packet_handling.remarking
            dscp_tunnel = remarking.get_field_value("dscp_tunnel")
            if util.isNotEmpty(dscp_tunnel):
                cls_obj.is_dscp_tunnel = dscp_tunnel
            mark_dscp = remarking.get_field_value("mark_dscp")
            if util.isNotEmpty(mark_dscp):
                cls_obj.dscp_value = mark_dscp
        if packet_handling is not None and hasattr(packet_handling,"bandwidth") and packet_handling.bandwidth is not None:
            print "bandwidth: ",packet_handling.bandwidth
            bandwidth = packet_handling.bandwidth
            rate_percentage = bandwidth.get_field_value("rate_percentage")
            if util.isNotEmpty(rate_percentage):
                cls_obj.bandwidth_remaining_percentage = rate_percentage
            percentage = bandwidth.get_field_value("percentage")
            if util.isNotEmpty(percentage):
                cls_obj.bandwidth_percentage = percentage
            bandwidth_remaining_ratio = bandwidth.get_field_value("bandwidth_remaining_ratio")
            if util.isNotEmpty(bandwidth_remaining_ratio):
                cls_obj.bandwidth_remaining_ratio = bandwidth_remaining_ratio
            if hasattr(bandwidth,"random_detect") and bandwidth.random_detect is not None:
                print "random_detect: ",bandwidth.random_detect
                random_detect = bandwidth.random_detect
                random_detect_value = random_detect.get_field_value("random_detect")
                if util.isNotEmpty(random_detect_value):
                    cls_obj.random_detect = random_detect_value
        if packet_handling is not None and hasattr(packet_handling,"priority") and packet_handling.priority is not None:
            print "priority: ",packet_handling.priority
            priority_value = packet_handling.priority.get_field_value("bandwidth_rate")
            if util.isNotEmpty(priority_value):
                cls_obj.priority_value = priority_value
            priority_percentage = packet_handling.priority.get_field_value("percentage")
            if util.isNotEmpty(priority_percentage):
                cls_obj.priority_percentage = priority_percentage
            priority_level = packet_handling.priority.get_field_value("priority_level")
            if util.isNotEmpty(priority_level):
                cls_obj.priority_level = priority_level
        if packet_handling is not None and hasattr(packet_handling,"police") and packet_handling.police is not None:
            print "police: ",packet_handling.police
            police = packet_handling.police
            bit_rate = packet_handling.police.get_field_value("bit_rate")
            if util.isNotEmpty(bit_rate):
                cls_obj.bit_rate = bit_rate
            police_cir_percentage = packet_handling.police.get_field_value("police_cir_percentage")
            if util.isNotEmpty(police_cir_percentage):
                cls_obj.police_cir_percentage = police_cir_percentage
        yang.Sdk.createData(dev.url+"/qos:policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession())

        if cls.get_field_value('queue_limit') is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            queue_limit = cls.queue_limit.get_field_value('queue_limit')
            packets = cls.queue_limit.get_field_value('packets')
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(dev.url+"/qos:policy-maps/policy-map=%s/class-entry=%s"%(policy_name,cls_name), queue_limit_obj.getxml(filter=True), sdata.getSession())

        if cls.get_field_value('qos_group') is not None:
            #qos_group_obj = policy_maps.policy_map.class_entry.class_entry()
            qos_group_value = cls.qos_group.get_field_value('qos_group')
            if util.isNotEmpty(qos_group_value):
                cls_obj.qos_group = qos_group_value

            yang.Sdk.createData(dev.url+"/qos:policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession())


def class_map(entity, url, cls_name, dev, sdata):
    xml_output = yang.Sdk.getData(url+"/qos-service/class-maps/class-map="+str(cls_name), '',sdata.getTaskId())
    obj_class = util.parseXmlString(xml_output)
    print "obj: ",obj_class
    print "xml of class map obj: ",obj_class.toXml()
    description = obj_class.class_map.get_field_value("description")
    match_type = obj_class.class_map.get_field_value("match_type")

    dev.addQOSClassMapsContainer(sdata.getSession())

    cls_map_obj = class_maps.class_map.class_map()
    cls_map_obj.name = cls_name
    if util.isNotEmpty(description):
        cls_map_obj.description = description
    if util.isNotEmpty(match_type):
        cls_map_obj.match_type = match_type
    yang.Sdk.createData(dev.url+"/qos:class-maps", cls_map_obj.getxml(filter=True), sdata.getSession())
    dscp = obj_class.class_map.get_field_value("dscp")
    if util.isNotEmpty(dscp):
        for ds in util.convert_to_list(dscp):
            match_obj = class_maps.class_map.class_match_condition.class_match_condition()
            match_obj.condition_type = "ip dscp"
            match_obj.match_value = ds
            yang.Sdk.createData(dev.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession())

    # protocol = obj_class.class_map.get_field_value("protocol")
    # if util.isNotEmpty(protocol):
    #     for pr in util.convert_to_list(protocol):
    #         match_obj = class_maps.class_map.class_match_condition.class_match_condition()
    #         match_obj.condition_type = "protocol"
    #         match_obj.match_value = pr
    #         yang.Sdk.createData(dev.url+"/class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession())

    protocol = obj_class.class_map.get_field_value("protocol")
    if util.isNotEmpty(protocol):
        for pr in util.convert_to_list(protocol):
            match_obj = class_maps.class_map.class_match_condition.class_match_condition()
            match_obj.condition_type = "protocol"
            match_obj.match_value = pr
            yang.Sdk.createData(dev.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession())
            if pr == "http":
                match_object = class_maps.class_map.class_match_condition.http_url.http_url()
                http_url = obj_class.class_map.get_field_value("http_url")
                print "http_url is:",http_url
                if util.isNotEmpty(http_url):
                    for url_http in util.convert_to_list(http_url):
                        match_object.url = url_http
                        yang.Sdk.createData(dev.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name,'protocol','http'), match_object.getxml(filter=True), sdata.getSession())
                else:
                    match_obj.only_http = 'true'
                    yang.Sdk.createData(dev.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession())

    access_group = obj_class.class_map.get_field_value("access_group")
    if util.isNotEmpty(access_group):
        for each_access_group in util.convert_to_list(access_group):
            access_group_def(url, each_access_group, dev, sdata)
            match_obj = class_maps.class_map.class_match_condition.class_match_condition()
            match_obj.condition_type = "access-group"
            match_obj.match_value = each_access_group
            yang.Sdk.createData(dev.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession())

    qos_group = obj_class.class_map.get_field_value("qos_group")
    if util.isNotEmpty(qos_group):
        match_obj = class_maps.class_map.class_match_condition.class_match_condition()
        match_obj.condition_type = "qos-group"
        match_obj.match_value = qos_group
        yang.Sdk.createData(dev.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession())


def delete_interface(entity, smodelctx, sdata, conf, **kwargs):
    device = None
    interface_name = None
    mode = None
    inputdict = kwargs['inputdict']

    if entity == 'cpe':
        device = devicemgr.getDeviceById(conf.single_cpe_site_services.cpe.device_ip)
    elif entity == 'cpe_primary':
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_primary.device_ip)
    elif entity == 'cpe_secondary' or entity == 'cpe_secondary_only':
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_secondary.device_ip)
    elif entity == 'cpe_dual':
        device = devicemgr.getDeviceById(conf.single_cpe_dual_wan_site_services.cpe.device_ip)
    elif entity == 'cpe_primary_dual':
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip)
    elif entity == 'cpe_secondary_dual' or entity == 'cpe_secondary_only_dual':
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip)
    elif entity == 'cpe_primary_triple':
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_primary.device_ip)

    if entity == 'cpe':
        obj = util.convert_to_list(conf.single_cpe_site_services.cpe_lan.end_points)
        for endpoint in obj:
            if hasattr(endpoint,"dps"):
                if endpoint.dps == 'true':
                    if endpoint.device_ip == device.device.id:
                        interface_name,mode = endpoint_def(endpoint)
            else:
                interface_name,mode = endpoint_def(endpoint)
    elif entity == 'cpe_primary':
        obj = util.convert_to_list(conf.dual_cpe_site_services.cpe_lan.end_points)
        for endpoint in obj:
            if hasattr(endpoint,"dps"):
                if endpoint.dps == 'true':
                    if endpoint.device_ip == device.device.id:
                        interface_name,mode = endpoint_def(endpoint)
            else:
                interface_name,mode = endpoint_def(endpoint)
    elif entity == 'cpe_secondary' or entity == 'cpe_secondary_only':
        obj = util.convert_to_list(conf.dual_cpe_site_services.cpe_lan.end_points)
        for endpoint in obj:
            if hasattr(endpoint,"dps"):
                if endpoint.dps == 'true':
                    if endpoint.device_ip == device.device.id:
                        interface_name,mode = endpoint_def(endpoint)
            else:
                interface_name,mode = endpoint_def(endpoint)
    elif entity == 'cpe_dual':
        obj = util.convert_to_list(conf.single_cpe_dual_wan_site_services.cpe_lan.end_points)
        for endpoint in obj:
            if hasattr(endpoint,"dps"):
                if endpoint.dps == 'true':
                    if endpoint.device_ip == device.device.id:
                        interface_name,mode = endpoint_def(endpoint)
            else:
                interface_name,mode = endpoint_def(endpoint)
    elif entity == 'cpe_primary_dual':
        obj = util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_lan.end_points)
        for endpoint in obj:
            if hasattr(endpoint,"dps"):
                if endpoint.dps == 'true':
                    if endpoint.device_ip == device.device.id:
                        interface_name,mode = endpoint_def(endpoint)
            else:
                interface_name,mode = endpoint_def(endpoint)
    elif entity == 'cpe_secondary_dual' or entity == 'cpe_secondary_only_dual':
        obj = util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_lan.end_points)
        for endpoint in obj:
            if hasattr(endpoint,"dps"):
                if endpoint.dps == 'true':
                    if endpoint.device_ip == device.device.id:
                        interface_name,mode = endpoint_def(endpoint)
            else:
                interface_name,mode = endpoint_def(endpoint)
    elif entity == 'cpe_primary_triple':
        obj = util.convert_to_list(conf.triple_cpe_site_services.cpe_lan.end_points)
        for endpoint in obj:
            if hasattr(endpoint,"dps"):
                if endpoint.dps == 'true':
                    if endpoint.device_ip == device.device.id:
                        interface_name,mode = endpoint_def(endpoint)
            else:
                interface_name,mode = endpoint_def(endpoint)

    intf_obj_phy = interfaces.interface.interface()
    intf_obj_phy.name = interface_name
    intf_obj_phy.long_name = interface_name
    intf_obj_phy.mode = mode
    if util.isNotEmpty(inputdict['hierarchical_policy']) or inputdict['hierarchical_policy'] is not None or util.isNotEmpty(inputdict['inbound_policy']) or inputdict['inbound_policy'] is not None:
        intf_obj_phy.inbound_qos._empty_tag = True
    intf_obj_phy.vrf_receive._empty_tag = True
    if util.isNotEmpty(inputdict['pbr_policy']) or inputdict['pbr_policy'] is not None:
        intf_obj_phy.pbr_policy._empty_tag = True
    intf_obj_phy.bgp_policy._empty_tag = True
    intf_obj_phy.bgp_policy_qos._empty_tag = True
    uri = device.url + '/interface:interfaces/interface=%s' % (str(interface_name).replace('/', '%2F'))
    payload = intf_obj_phy.getxml(filter=True)
    if device.isInterfaceInDeviceExists(interface_name):
        yang.Sdk.patchData(uri, payload, sdata, add_reference=False)


def endpoint_def(endpoint):
    if endpoint.interface_type == 'Physical':
        interface_name = endpoint.interface_name
        mode = 'l3-interface'
    if endpoint.interface_type == 'Sub-Interface':
        interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
        mode = 'sub-interface'
    if endpoint.interface_type == 'SVI':
        interface_name = 'Vlan' + str(endpoint.vlan_id)
        mode = 'vlan'
    return interface_name,mode


class DeletePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for Deletion"""
        log('operations: %s' % (operations))
        yang.moveOperations(operations, ['DeleteRouterBGPNetwork'], ['DeleteRouterBGPRedistribute'], True)
        print 'pass: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteRouterBGPNeighbor'], ['DeleteRouterBGPNetwork'], True)
        print 'pass_0: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteInterface'], ['DeleteRouteMapConditions', 'UpdateInterface'], True)
        print 'pass0: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteVrf'], ['DeleteRouterBGPNetwork', 'DeleteVrfRTExport', 'DeleteVrfRTImport', 'DeleteVrfImportMap', 'DeleteVrfExportMap', 'DeleteRouterOspf', 'DeleteRouterOspfNetwork', 'DeleteInterface'], True)
        print 'pass0_1: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteQClassMapMatchCondition'], ['DeleteVrf'], True)
        print 'pass1: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteQPolicyMapClassEntry','UpdateQPolicyMapClassEntry'], ['DeleteQClassMapMatchCondition'], True)
        print 'pass2: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteQPolicyMap'], ['DeleteQPolicyMapClassEntry','UpdateQPolicyMapClassEntry'], True)
        print 'pass3: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteQClassMap'], ['DeleteQPolicyMap'], True)
        print 'pass4: operations: %s' % (operations)


class CreatePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for creation"""
        log('operations: %s' % (operations))
