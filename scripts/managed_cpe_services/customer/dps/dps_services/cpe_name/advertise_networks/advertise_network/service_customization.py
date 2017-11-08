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
                                                           |
                                                           advertise-networks
                                                                             |
                                                                             advertise-network
                                                                                              
Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/advertise-networks/advertise-network
"""
"""
Names of Leafs for this Yang Entity
                name
              prefix
           route-map
"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr
from servicemodel.controller.devices.device import vrfs

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
            adv_networks(entity, smodelctx, sdata, device_ip, **kwargs)

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
      #raise Exception('Update forbidden for node advertise-network at path managed-cpe-services/customer/dps/dps-services/cpe-name/advertise-networks/advertise-network')
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


def adv_networks(entity, smodelctx, sdata, device_ip, **kwargs):
    device = devicemgr.getDeviceById(device_ip)
    inputdict = kwargs['inputdict']
    prefix = inputdict['prefix']
    route_map = inputdict['route_map']
    prefix = util.IPPrefix(prefix)
    ip_address = prefix.address
    netmask = prefix.netmask
    adv_networks_obj = vrfs.vrf.router_bgp.network.network()
    adv_networks_obj.ip_address = ip_address
    adv_networks_obj.netmask = netmask
    if util.isNotEmpty(route_map):
        adv_networks_obj.route_map = route_map
    vrf = inputdict['vrf_name']
    # obj = getLocalObject(sdata, 'cpe-name')
    # if hasattr(obj.cpe_name, 'vrf'):
    #     vrf = obj.cpe_name.vrf
    if vrf is None or util.isEmpty(vrf):
        obj = getLocalObject(sdata, 'dps-services')
        uri = sdata.getRcPath()
        uri_list = uri.split('/',5)
        url = '/'.join(uri_list[0:4])
        if hasattr(obj.dps_services, 'single_cpe_site'):
            if obj.dps_services.single_cpe_site == "true":
                site = obj.dps_services.single_cpe_sites
                site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '', sdata.getTaskId())
                conf = util.parseXmlString(site_output)
                # if hasattr(conf.single_cpe_site_services.cpe, 'vrf_name'):
                #     vrf = conf.single_cpe_site_services.cpe.vrf_name
                if hasattr(conf.single_cpe_site_services.cpe_lan, 'end_points'):
                    for endpoint in util.convert_to_list(conf.single_cpe_site_services.cpe_lan.end_points):
                        endpoint_ip = endpoint.device_ip
                        if device_ip == endpoint_ip:
                            if endpoint.dps == 'true':
                                if hasattr(endpoint, 'vrf'):
                                    vrf = endpoint.vrf
        elif hasattr(obj.dps_services, 'dual_cpe_site'):
            if obj.dps_services.dual_cpe_site == "true":
                site = obj.dps_services.dual_cpe_sites
                site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                conf = util.parseXmlString(site_output)
                config = getLocalObject(sdata, 'cpe-name')
                if config.cpe_name.cpe == 'cpe-primary':
                    # if hasattr(conf.dual_cpe_site_services.cpe_primary, 'vrf_name'):
                    #     vrf = conf.dual_cpe_site_services.cpe_primary.vrf_name
                    if hasattr(conf.dual_cpe_site_services.cpe_lan, 'end_points'):
                        for endpoint in util.convert_to_list(conf.dual_cpe_site_services.cpe_lan.end_points):
                            endpoint_ip = endpoint.device_ip
                            if device_ip == endpoint_ip:
                                if endpoint.dps == 'true':
                                    if hasattr(endpoint, 'vrf'):
                                        vrf = endpoint.vrf
                elif config.cpe_name.cpe == 'cpe-secondary':
                    # if hasattr(conf.dual_cpe_site_services.cpe_secondary, 'vrf_name'):
                    #     vrf = conf.dual_cpe_site_services.cpe_secondary.vrf_name
                    if hasattr(conf.dual_cpe_site_services.cpe_lan, 'end_points'):
                        for endpoint in util.convert_to_list(conf.dual_cpe_site_services.cpe_lan.end_points):
                            endpoint_ip = endpoint.device_ip
                            if device_ip == endpoint_ip:
                                if endpoint.dps == 'true':
                                    if hasattr(endpoint, 'vrf'):
                                        vrf = endpoint.vrf
                elif config.cpe_name.cpe == 'cpe-secondary-only':
                    # if hasattr(conf.dual_cpe_site_services.cpe_secondary, 'vrf_name'):
                    #     vrf = conf.dual_cpe_site_services.cpe_secondary.vrf_name
                    if hasattr(conf.dual_cpe_site_services.cpe_lan, 'end_points'):
                        for endpoint in util.convert_to_list(conf.dual_cpe_site_services.cpe_lan.end_points):
                            endpoint_ip = endpoint.device_ip
                            if device_ip == endpoint_ip:
                                if endpoint.dps == 'true':
                                    if hasattr(endpoint, 'vrf'):
                                        vrf = endpoint.vrf
        elif hasattr(obj.dps_services, 'single_cpe_dual_wan_site'):
            if obj.dps_services.single_cpe_dual_wan_site == "true":
                site = obj.dps_services.single_cpe_dual_wan_sites
                site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                conf = util.parseXmlString(site_output)
                # if hasattr(conf.single_cpe_dual_wan_site_services.cpe, 'vrf_name'):
                #     vrf = conf.single_cpe_dual_wan_site_services.cpe.vrf_name
                if hasattr(conf.single_cpe_dual_wan_site_services.cpe_lan, 'end_points'):
                    for endpoint in util.convert_to_list(conf.single_cpe_dual_wan_site_services.cpe_lan.end_points):
                        endpoint_ip = endpoint.device_ip
                        if device_ip == endpoint_ip:
                            if endpoint.dps == 'true':
                                if hasattr(endpoint, 'vrf'):
                                    vrf = endpoint.vrf
        elif hasattr(obj.dps_services, 'dual_cpe_dual_wan_site'):
            if obj.dps_services.dual_cpe_dual_wan_site == "true":
                site = obj.dps_services.dual_cpe_dual_wan_sites
                site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                conf = util.parseXmlString(site_output)
                config = getLocalObject(sdata, 'cpe-name')
                if config.cpe_name.cpe == 'cpe-primary':
                    # if hasattr(conf.dual_cpe_site_services.cpe_primary, 'vrf_name'):
                    #     vrf = conf.dual_cpe_site_services.cpe_primary.vrf_name
                    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_lan, 'end_points'):
                        for endpoint in util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_lan.end_points):
                            endpoint_ip = endpoint.device_ip
                            if device_ip == endpoint_ip:
                                if endpoint.dps == 'true':
                                    if hasattr(endpoint, 'vrf'):
                                        vrf = endpoint.vrf
                elif config.cpe_name.cpe == 'cpe-secondary':
                    # if hasattr(conf.dual_cpe_site_services.cpe_secondary, 'vrf_name'):
                    #     vrf = conf.dual_cpe_site_services.cpe_secondary.vrf_name
                    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_lan, 'end_points'):
                        for endpoint in util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_lan.end_points):
                            endpoint_ip = endpoint.device_ip
                            if device_ip == endpoint_ip:
                                if endpoint.dps == 'true':
                                    if hasattr(endpoint, 'vrf'):
                                        vrf = endpoint.vrf
                elif config.cpe_name.cpe == 'cpe-secondary-only':
                    # if hasattr(conf.dual_cpe_site_services.cpe_secondary, 'vrf_name'):
                    #     vrf = conf.dual_cpe_site_services.cpe_secondary.vrf_name
                    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_lan, 'end_points'):
                        for endpoint in util.convert_to_list(conf.dual_cpe_dual_wan_site_services.cpe_lan.end_points):
                            endpoint_ip = endpoint.device_ip
                            if device_ip == endpoint_ip:
                                if endpoint.dps == 'true':
                                    if hasattr(endpoint, 'vrf'):
                                        vrf = endpoint.vrf
        elif hasattr(obj.dps_services, 'triple_cpe_site'):
            if obj.dps_services.triple_cpe_site == "true":
                site = obj.dps_services.triple_cpe_sites
                site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '', sdata.getTaskId())
                conf = util.parseXmlString(site_output)
                config = getLocalObject(sdata, 'cpe-name')
                if config.cpe_name.cpe == 'cpe-primary-only':
                    # if hasattr(conf.dual_cpe_site_services.cpe_primary, 'vrf_name'):
                    #     vrf = conf.dual_cpe_site_services.cpe_primary.vrf_name
                    if hasattr(conf.triple_cpe_site_services.cpe_lan, 'end_points'):
                        for endpoint in util.convert_to_list(conf.triple_cpe_site_services.cpe_lan.end_points):
                            endpoint_ip = endpoint.device_ip
                            if device_ip == endpoint_ip:
                                if endpoint.dps == 'true':
                                    if hasattr(endpoint, 'vrf'):
                                        vrf = endpoint.vrf

    if vrf is None or util.isEmpty(vrf):
        vrf = 'GLOBAL'
    adv_networks_url1 = device.url + '/vrfs/vrf=%s' % (vrf)
    yang.Sdk.createData(adv_networks_url1, '<router-bgp/>', sdata.getSession())

    adv_networks_url = device.url + '/vrfs/vrf=%s/router-bgp' % (vrf)
    yang.Sdk.createData(adv_networks_url, adv_networks_obj.getxml(filter=True), sdata.getSession())


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
