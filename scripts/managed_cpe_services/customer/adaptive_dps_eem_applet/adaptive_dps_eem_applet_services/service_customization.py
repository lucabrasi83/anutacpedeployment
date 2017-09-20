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
from servicemodel.controller.devices.device import eem_applets

from cpedeployment.cpedeployment_lib import getLocalObject,modifiedGetLocalObject
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
            obj = modifiedGetLocalObject(sdata, 'adaptive-dps-eem-applet-services')
            uri = sdata.getRcPath()
            applet_name = obj.adaptive_dps_eem_applet_services.applet_name
            inputdict['applet_name'] = applet_name
            uri_list = uri.split('/',5)
            url = '/'.join(uri_list[0:4])
            entity = None
            conf = None
            if hasattr(obj.adaptive_dps_eem_applet_services, 'single_cpe_site'):
                if obj.adaptive_dps_eem_applet_services.single_cpe_site == "true":
                    site = obj.adaptive_dps_eem_applet_services.single_cpe_sites
                    site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '', sdata.getTaskId())
                    conf = util.parseXmlString(site_output)
                    entity = 'cpe'
            elif hasattr(obj.adaptive_dps_eem_applet_services, 'dual_cpe_site'):
                if obj.adaptive_dps_eem_applet_services.dual_cpe_site == "true":
                    site = obj.adaptive_dps_eem_applet_services.dual_cpe_sites
                    site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                    conf = util.parseXmlString(site_output)
                    if obj.adaptive_dps_eem_applet_services.cpe == 'cpe-primary':
                        entity = 'cpe_primary'
                    elif obj.adaptive_dps_eem_applet_services.cpe == 'cpe-secondary':
                        entity = 'cpe_secondary'
            elif hasattr(obj.adaptive_dps_eem_applet_services, 'single_cpe_dual_wan_site'):
                if obj.adaptive_dps_eem_applet_services.single_cpe_dual_wan_site == "true":
                    site = obj.adaptive_dps_eem_applet_services.single_cpe_dual_wan_sites
                    site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                    conf = util.parseXmlString(site_output)
                    entity = 'cpe_dual'
            elif hasattr(obj.adaptive_dps_eem_applet_services, 'dual_cpe_dual_wan_site'):
                if obj.adaptive_dps_eem_applet_services.dual_cpe_dual_wan_site == "true":
                    site = obj.adaptive_dps_eem_applet_services.dual_cpe_dual_wan_sites
                    site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                    conf = util.parseXmlString(site_output)
                    if obj.adaptive_dps_eem_applet_services.cpe == 'cpe-primary':
                        entity = 'cpe_primary_dual'
                    elif obj.adaptive_dps_eem_applet_services.cpe == 'cpe-secondary':
                        entity = 'cpe_secondary_dual'
            elif hasattr(obj.adaptive_dps_eem_applet_services, 'triple_cpe_site'):
                if obj.adaptive_dps_eem_applet_services.triple_cpe_site == "true":
                    site = obj.adaptive_dps_eem_applet_services.triple_cpe_sites
                    site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '', sdata.getTaskId())
                    conf = util.parseXmlString(site_output)
                    if obj.adaptive_dps_eem_applet_services.cpe == 'cpe-primary':
                        entity = 'cpe_primary_triple'
                    elif obj.adaptive_dps_eem_applet_services.cpe == 'cpe-secondary':
                        entity = 'cpe_secondary_triple'
                    elif obj.adaptive_dps_eem_applet_services.cpe == 'cpe-tertiary':
                        entity = 'cpe_tertiary_triple'
            adaptive_dps_def(entity, conf, sdata, **kwargs)

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
      raise Exception('Update forbidden for node cpe-name at path managed-cpe-services/customer/dps/dps-services/cpe-name')
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

def adaptive_dps_def(entity, conf, sdata, **kwargs):
    interface_name = None
    mode = None
    inputdict = kwargs['inputdict']
    if entity == 'cpe':
        device = devicemgr.getDeviceById(conf.single_cpe_site_services.cpe.device_ip)
    elif entity == 'cpe_primary':
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_primary.device_ip)
    elif entity == 'cpe_secondary':
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_secondary.device_ip)
    elif entity == 'cpe_dual':
        device = devicemgr.getDeviceById(conf.single_cpe_dual_wan_site_services.cpe.device_ip)
    elif entity == 'cpe_primary_dual':
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip)
    elif entity == 'cpe_secondary_dual':
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip)
    elif entity == 'cpe_primary_triple':
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_primary.device_ip)
    elif entity == 'cpe_secondary_triple':
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_secondary.device_ip)
    elif entity == 'cpe_tertiary_triple':
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_tertiary.device_ip)

    applet_obj = eem_applets.event_manager_applet.event_manager_applet() 
    applet_obj.applet_name = inputdict['applet_name']
    yang.Sdk.createData(device.url+"/eem-applets", applet_obj.getxml(filter=True), sdata.getSession())
    
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
