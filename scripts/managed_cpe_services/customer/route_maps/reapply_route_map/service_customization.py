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
                                    route-maps
                                              |
                                              update-route-maps
                                                               
Schema Representation:

/services/managed-cpe-services/customer/route-maps/update-route-maps
"""
"""
Names of Leafs for this Yang Entity
                  id
      route-map-name
     sequence-number
              action
               entry
      condition-type
               value
            set-type
                  ip
           set-value
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log
from com.anuta.api import DataNodeNotFoundException
import re




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
            if inputdict['single_cpe_site'] == "true":
                if len(inputdict['single_cpe_sites']) > 0:
                    if isinstance(inputdict['single_cpe_sites'], list) is True:
                        for site in inputdict['single_cpe_sites']:
                            uri = sdata.getRcPath()
                            uri_list = uri.split('/',5)
                            url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe'
                            reapply_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        reapply_route_map(entity, conf, sdata, **kwargs)

            if inputdict['dual_cpe_site'] == "true":
                if len(inputdict['dual_cpe_sites']) > 0:
                    if isinstance(inputdict['dual_cpe_sites'], list) is True:
                        for site in inputdict['dual_cpe_sites']:
                            uri = sdata.getRcPath()
                            uri_list = uri.split('/',5)
                            url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary'
                            reapply_route_map(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary'
                            reapply_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary'
                        reapply_route_map(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary'
                        reapply_route_map(entity, conf, sdata, **kwargs)

            if inputdict['single_cpe_dual_wan_site'] == "true":
                if len(inputdict['single_cpe_dual_wan_sites']) > 0:
                    if isinstance(inputdict['single_cpe_dual_wan_sites'], list) is True:
                        for site in inputdict['single_cpe_dual_wan_sites']:
                            uri = sdata.getRcPath()
                            uri_list = uri.split('/',5)
                            url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_dual'
                            reapply_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        reapply_route_map(entity, conf, sdata, **kwargs)

            if inputdict['triple_cpe_site'] == "true":
                if len(inputdict['triple_cpe_sites']) > 0:
                    if isinstance(inputdict['triple_cpe_sites'], list) is True:
                        for site in inputdict['triple_cpe_sites']:
                            uri = sdata.getRcPath()
                            uri_list = uri.split('/',5)
                            url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary_triple'
                            reapply_route_map(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_triple'
                            reapply_route_map(entity, conf, sdata, **kwargs)
                            entity = 'cpe_tertiary_triple'
                            reapply_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['triple_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_triple'
                        reapply_route_map(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_triple'
                        reapply_route_map(entity, conf, sdata, **kwargs)
                        entity = 'cpe_tertiary_triple'
                        reapply_route_map(entity, conf, sdata, **kwargs)

            if inputdict['dual_cpe_dual_wan_site'] == "true":
                if len(inputdict['dual_cpe_dual_wan_sites']) > 0:
                    if isinstance(inputdict['dual_cpe_dual_wan_sites'], list) is True:
                        for site in inputdict['dual_cpe_dual_wan_sites']:
                            uri = sdata.getRcPath()
                            uri_list = uri.split('/',5)
                            url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary_dual'
                            reapply_route_map(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_dual'
                            reapply_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_dual'
                        reapply_route_map(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_dual'
                        reapply_route_map(entity, conf, sdata, **kwargs)
                        
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
      #raise Exception('Update forbidden for node update-route-maps at path managed-cpe-services/customer/route-maps/update-route-maps')
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


def reapply_route_map(entity, conf, sdata, **kwargs):
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

    inputdict = kwargs['inputdict']
    route_map_name = inputdict['route_map_name']

    url_device_route_map = '/controller:devices/device=%s/l3features:route-maps' %(device.device.id)
    device_route_map = yang.Sdk.getData(url_device_route_map, '', sdata.getTaskId())
    conf_route = util.parseXmlString(device_route_map)

    device_route = []
    if hasattr(conf_route.route_maps, 'route_map'):
        conf_route.route_maps.route_map = util.convert_to_list(conf_route.route_maps.route_map)
        for routemap in conf_route.route_maps.route_map:
            device_route.append(routemap.name)
            

    if route_map_name in device_route:

        '''
        route_map_name_url = '/controller:devices/device=%s/l3features:route-maps/route-map=%s' %(device.device.id, route_map_name)
        
        device_route_map_entries = yang.Sdk.getData(route_map_name_url, '', sdata.getTaskId())
        conf_route_entries = util.parseXmlString(device_route_map_entries)
        if hasattr(conf_route_entries.route_map, 'route_map_entries'):
            conf_route_entries.route_map.route_map_entries = util.convert_to_list(conf_route_entries.route_map.route_map_entries)
            for routemapentry in conf_route_entries.route_map.route_map_entries:
                route_map_entries_url = route_map_name_url + '/route-map-entries=%s' % (routemapentry.seq)
                output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+route_map_entries_url+'</rc-path></input>')
                ref = util.parseXmlString(output)
                log("xml_op:%s" %(ref))
                if hasattr(ref.output, 'references'):
                    if hasattr(ref.output.references, 'reference'):
                            for eachreference in util.convert_to_list(ref.output.references.reference):
                                if hasattr(eachreference, 'src_node'):
                                    for each_ref in util.convert_to_list(eachreference.src_node):
                                        yang.Sdk.removeReference(each_ref, eachreference.dest_node, sdata.getSession())
        
               	#yang.Sdk.deleteData(route_map_entries_url, '', sdata.getTaskId(), sdata.getSession())
        '''
        route_maps(route_map_name, device, sdata)

    else:
        log("Route-map is not in device") 


def route_maps(redistroutepolicy, device, sdata, int_name=None, entity=None):
    device.addRouteMapsContainer(sdata.getSession())
    obj = getLocalObject(sdata, 'customer')
    log("obj of routemap is: %s" % (obj))
    log("xml of route map obj: %s" % (obj.toXml()))
    log("route map obj is: %s" % (obj.customer.route_maps))
    if hasattr(obj.customer.route_maps, 'route_map'):
        obj.customer.route_maps.route_map = util.convert_to_list(obj.customer.route_maps.route_map)
        util.log_debug( "route map obj is:",obj.customer.route_maps.route_map)
        for route_map_obj in obj.customer.route_maps.route_map:
            route_map_name = route_map_obj.get_field_value('route_map_name')
            if redistroutepolicy == route_map_name :
                util.log_debug( "route_map_name is:",route_map_name)
                route_maps_url = device.url + '/l3features:route-maps/route-map=%s' % (redistroutepolicy)
                from servicemodel.controller.devices.device import route_maps
                routemap_obj = route_maps.route_map.route_map()
                if route_map_name is not None:
                    routemap_obj.name = route_map_name
                    yang.Sdk.putData(route_maps_url, routemap_obj.getxml(filter=True), sdata, add_reference=False)
                    if hasattr(route_map_obj,'route_map_entries'):
                        print "Enter into route_map_entry"
                        route_map_entries = util.convert_to_list(route_map_obj.route_map_entries)
                        for route_map_entry in route_map_entries:
                            route_map(route_map_name, route_map_entry, device, sdata, int_name, entity)

def route_map(route_map_name, route_map_entries, device, sdata, int_name=None, entity=None):
    print "Entering into Route map"
    from servicemodel.controller.devices.device import route_maps
    routemapentry_obj = route_maps.route_map.route_map_entries.route_map_entries()
    action = route_map_entries.get_field_value('action')
    if action is not None:
        routemapentry_obj.action = action
    seq = route_map_entries.get_field_value('sequence_number')
    if seq is not None:
        routemapentry_obj.seq = seq
    routemap_entry_url = device.url + '/l3features:route-maps/route-map=%s/route-map-entries=%s' % (route_map_name, seq)
    yang.Sdk.putData(routemap_entry_url, routemapentry_obj.getxml(filter=True), sdata, add_reference=False)
    if hasattr(route_map_entries,'match_condition'):
        for match_obj in util.convert_to_list(route_map_entries.match_condition):
            matchcondition_obj = route_maps.route_map.route_map_entries.match_condition.match_condition()
            condition_type = match_obj.get_field_value('condition_type')
            if condition_type is not None:
                matchcondition_obj.condition_type = condition_type
            condition_value = match_obj.get_field_value('value')
            if condition_value is not None:
                if condition_value == 'LAN-INTERFACE' and condition_type == 'interface':
                    matchcondition_obj.value = int_name
                else:
                    matchcondition_obj.value = condition_value
            if condition_type == 'as-path' and condition_value is not None:
                as_path_acl(condition_value, device, sdata)
            if condition_type == 'community' and condition_value is not None:
                community_lists(condition_value, device, sdata)
            if condition_type == 'address' and condition_value is not None:
                from endpoint_lib import access_group_def
                uri = sdata.getRcPath()
                uri_list = uri.split('/',5)
                url = '/'.join(uri_list[0:4])

                acl_output = yang.Sdk.getData(url+"/access-lists", '', sdata.getTaskId())
                acl_obj = util.parseXmlString(acl_output)
                if hasattr(acl_obj, 'access_lists'):
                    if hasattr(acl_obj.access_lists, 'access_list'):
                        for acl_name in util.convert_to_list(acl_obj.access_lists.access_list):
                            if hasattr(acl_name, 'name'):
                                if acl_name.name == condition_value:
                                    access_group_def(url, condition_value, device, sdata)
            match_condition_url = device.url + '/l3features:route-maps/route-map=%s/route-map-entries=%s/match-condition=%s,%s' % (route_map_name, seq, condition_type, condition_value)
            if util.isNotEmpty(matchcondition_obj.value):
                yang.Sdk.putData(match_condition_url, matchcondition_obj.getxml(filter=True), sdata, add_reference=False)
    if hasattr(route_map_entries,'set_action'):
        for set_obj in util.convert_to_list(route_map_entries.set_action):
            set_ip = None
            set_obj1 = route_maps.route_map.route_map_entries.set_action.set_action()
            set_type = set_obj.get_field_value('set_type')
            if set_type is not None:
                set_obj1.set_type = set_type
                if set_type == 'ip':
                    set_ip = set_obj.get_field_value('ip')
                    if set_ip is None:
                        raise Exception("Please provide ip precedence/df/next-hop")
                    else:
                        set_obj1.ip = set_ip
            set_value = set_obj.get_field_value('value')
            bgp_as_regex = re.match(r'\bAS\b', set_value)
            if set_value is not None:
                if set_value == 'IP' and set_ip == 'next-hop':
                    obj = modifiedGetLocalObject(sdata, 'cpe-name')
                    if hasattr(obj.cpe_name, "next_hop_ip"):
                        set_obj1.value = obj.cpe_name.next_hop_ip
                #Handle Keywork 'AS' in Route-Map for AS-Path Prepending
                elif bgp_as_regex is not None and set_type == 'as-path prepend':
                    if entity == 'cpe':
                        obj_bgp_as = getLocalObject(sdata, 'single-cpe-site-services')
                        if hasattr(obj_bgp_as.single_cpe_site_services, 'bgp_as'):
                            bgpas = obj_bgp_as.single_cpe_site_services.bgp_as
                            set_obj1.value = re.sub(r'\bAS\b', bgpas, set_value)
                    elif entity == 'cpe_dual':
                        obj_bgp_as = getLocalObject(sdata, 'single-cpe-dual-wan-site-services')
                        if hasattr(obj_bgp_as.single_cpe_dual_wan_site_services, 'bgp_as'):
                            bgpas = obj_bgp_as.single_cpe_dual_wan_site_services.bgp_as
                            set_obj1.value = re.sub(r'\bAS\b', bgpas, set_value)
                    elif entity == 'cpe_primary' or entity == 'cpe_secondary':
                        obj_bgp_as = getLocalObject(sdata, 'dual-cpe-site-services')
                        if hasattr(obj_bgp_as.dual_cpe_site_services, 'bgp_as'):
                            bgpas = obj_bgp_as.dual_cpe_site_services.bgp_as
                            set_obj1.value = re.sub(r'\bAS\b', bgpas, set_value)
                    elif entity == 'cpe_primary_dual' or entity == 'cpe_secondary_dual':
                        obj_bgp_as = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
                        if hasattr(obj_bgp_as.dual_cpe_dual_wan_site_services, 'bgp_as'):
                            bgpas = obj_bgp_as.dual_cpe_dual_wan_site_services.bgp_as
                            set_obj1.value = re.sub(r'\bAS\b', bgpas, set_value)
                    elif entity == 'cpe_primary_triple' or entity == 'cpe_secondary_triple' or entity == 'cpe_tertiary_triple':
                        obj_bgp_as = getLocalObject(sdata, 'triple-cpe-site-services')
                        if hasattr(obj_bgp_as.triple_cpe_site_services, 'bgp_as'):
                            bgpas = obj_bgp_as.triple_cpe_site_services.bgp_as
                            set_obj1.value = re.sub(r'\bAS\b', bgpas, set_value)

                #Handle AS keyword for Set Community and replace by site service AS number
                elif 'AS' in set_value and set_type == 'community':
                    if entity == 'cpe':
                            obj_bgp_as = getLocalObject(sdata, 'single-cpe-site-services')
                            if hasattr(obj_bgp_as.single_cpe_site_services, 'bgp_as'):
                                bgpas = obj_bgp_as.single_cpe_site_services.bgp_as
                                set_obj1.value = set_value.replace('AS', bgpas)
                    elif entity == 'cpe_dual':
                            obj_bgp_as = getLocalObject(sdata, 'single-cpe-dual-wan-site-services')
                            if hasattr(obj_bgp_as.single_cpe_dual_wan_site_services, 'bgp_as'):
                                bgpas = obj_bgp_as.single_cpe_dual_wan_site_services.bgp_as
                                set_obj1.value = set_value.replace('AS', bgpas)
                    elif entity == 'cpe_primary' or entity == 'cpe_secondary':
                            obj_bgp_as = getLocalObject(sdata, 'dual-cpe-site-services')
                            if hasattr(obj_bgp_as.dual_cpe_site_services, 'bgp_as'):
                                bgpas = obj_bgp_as.dual_cpe_site_services.bgp_as
                                set_obj1.value = set_value.replace('AS', bgpas)
                    elif entity == 'cpe_primary_dual' or entity == 'cpe_secondary_dual':
                            obj_bgp_as = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
                            if hasattr(obj_bgp_as.dual_cpe_dual_wan_site_services, 'bgp_as'):
                                bgpas = obj_bgp_as.dual_cpe_dual_wan_site_services.bgp_as
                                set_obj1.value = set_value.replace('AS', bgpas)
                    elif entity == 'cpe_primary_triple' or entity == 'cpe_secondary_triple' or entity == 'cpe_tertiary_triple':
                            obj_bgp_as = getLocalObject(sdata, 'triple-cpe-site-services')
                            if hasattr(obj_bgp_as.triple_cpe_site_services, 'bgp_as'):
                                bgpas = obj_bgp_as.triple_cpe_site_services.bgp_as
                                set_obj1.value = set_value.replace('AS', bgpas)

                elif set_type == 'comm-list':
                    community_lists(set_value, device, sdata)
                    set_obj1.value = set_value
                else:
                    set_obj1.value = set_value
            
            set_action_url = device.url + '/route-maps/route-map=%s/route-map-entries=%s/set-action=%s,%s' % (route_map_name,seq, set_type, set_value)
            yang.Sdk.putData(set_action_url, set_obj1.getxml(filter=True), sdata, add_reference=False)

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
