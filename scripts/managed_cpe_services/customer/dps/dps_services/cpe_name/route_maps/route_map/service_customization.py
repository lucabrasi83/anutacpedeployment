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
                                                           route-maps
                                                                     |
                                                                     route-map
                                                                              
Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/route-maps/route-map
"""
"""
Names of Leafs for this Yang Entity
      route-map-name
"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr
from servicemodel.controller.devices.device import route_maps

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log,route_map


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
            route_maps(inputdict['route_map_name'], device_ip, sdata)

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
      raise Exception('Update forbidden for node route-map at path managed-cpe-services/customer/dps/dps-services/cpe-name/route-maps/route-map')
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


def route_maps(redistroutepolicy, device_ip, sdata, int_name=None):
    device = devicemgr.getDeviceById(device_ip)
    device.addRouteMapsContainer(sdata.getSession())
    obj = getLocalObject(sdata, 'customer')
    print "obj of routemap is: ",obj
    print "xml of route map obj: ",obj.toXml()
    print "route map obj is:",obj.customer.route_maps
    if hasattr(obj.customer.route_maps, 'route_map'):
        obj.customer.route_maps.route_map = util.convert_to_list(obj.customer.route_maps.route_map)
        print "route map obj is:",obj.customer.route_maps.route_map
        for route_map_obj in obj.customer.route_maps.route_map:
            route_map_name = route_map_obj.get_field_value('route_map_name')
            if redistroutepolicy == route_map_name :
                print "route_map_name is:",route_map_name
                route_maps_url = device.url + '/route-maps'
		from servicemodel.controller.devices.device import route_maps
                routemap_obj = route_maps.route_map.route_map()
                if route_map_name is not None:
                    routemap_obj.name = route_map_name
                    yang.Sdk.createData(route_maps_url, routemap_obj.getxml(filter=True), sdata.getSession())
                    if hasattr(route_map_obj,'route_map_entries'):
                        print "Enter into route_map_entry"
                        route_map_entries = util.convert_to_list(route_map_obj.route_map_entries)
                        for route_map_entry in route_map_entries:
                            route_map(route_map_name, route_map_entry, device, sdata, int_name)


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
