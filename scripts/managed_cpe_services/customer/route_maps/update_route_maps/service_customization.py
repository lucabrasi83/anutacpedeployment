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
                            create_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        create_route_map(entity, conf, sdata, **kwargs)

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
                            create_route_map(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary'
                            create_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary'
                        create_route_map(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary'
                        create_route_map(entity, conf, sdata, **kwargs)

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
                            create_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        create_route_map(entity, conf, sdata, **kwargs)

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
                            create_route_map(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_triple'
                            create_route_map(entity, conf, sdata, **kwargs)
                            entity = 'cpe_tertiary_triple'
                            create_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['triple_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_triple'
                        create_route_map(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_triple'
                        create_route_map(entity, conf, sdata, **kwargs)
                        entity = 'cpe_tertiary_triple'
                        create_route_map(entity, conf, sdata, **kwargs)

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
                            create_route_map(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_dual'
                            create_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_dual'
                        create_route_map(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_dual'
                        create_route_map(entity, conf, sdata, **kwargs)
                        
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
      raise Exception('Update forbidden for node update-route-maps at path managed-cpe-services/customer/route-maps/update-route-maps')
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


def create_route_map(entity, conf, sdata, **kwargs):
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
    sequence_number = inputdict['sequence_number']
    action = inputdict['action']
    entry = inputdict['entry']
    condition_type = inputdict['condition_type']
    condition_value = inputdict['value']
    set_type = inputdict['set_type']
    set_ip = inputdict['ip']
    set_value = inputdict['set_value']
    if route_map_name in device_route:
        url_device_route_map_entries = '/controller:devices/device=%s/l3features:route-maps/route-map=%s' %(device.device.id, route_map_name)
        device_route_map_entries = yang.Sdk.getData(url_device_route_map_entries, '', sdata.getTaskId())
        conf_route_entries = util.parseXmlString(device_route_map_entries)
        device_route_entries = []
        if hasattr(conf_route_entries, 'route_maps_entries'):
            conf_route_entries.route_maps_entries = util.convert_to_list(conf_route_entries.route_maps_entries)
            for routemap_entries in conf_route_entries.route_maps_entries:
                device_route_entries.append(routemap_entries.seq)

        if sequence_number in device_route_entries:
            if entry == 'match-condition':
                matchcondition_obj = devices.device.route_maps.route_map.route_map_entries.match_condition.match_condition()
                if condition_type is not None:
                    matchcondition_obj.condition_type = condition_type
                if condition_value is not None:
                    matchcondition_obj.value = condition_value
                if condition_type == 'as-path' and condition_value is not None:
                    as_path_acl(condition_value, device, sdata)
                match_condition_url = device.url + '/route-maps/route-map=%s/route-map-entries=%s' % (route_map_name,sequence_number)
                yang.Sdk.createData(match_condition_url, matchcondition_obj.getxml(filter=True), sdata.getSession(), False)
            elif entry == 'set-action':
                set_obj1 = devices.device.route_maps.route_map.route_map_entries.set_action.set_action()
                if set_type is not None:
                    set_obj1.set_type = set_type
                    if set_type == 'ip':
                        if set_ip is None:
                            raise Exception("Please provide ip precedence/df/next-hop")
                        else:
                            set_obj1.ip = set_ip
                if set_value is not None:
                    set_obj1.value = set_value
                set_action_url = device.url + '/route-maps/route-map=%s/route-map-entries=%s' % (route_map_name,sequence_number)
                yang.Sdk.createData(set_action_url, set_obj1.getxml(filter=True), sdata.getSession(), False)
        else:
            entries_obj = devices.device.route_maps.route_map.route_map_entries.route_map_entries()
            entries_obj.seq = sequence_number
            entries_obj.action = action
            route_map_entries_url = device.url + '/route-maps/route-map=%s' % (route_map_name)
            yang.Sdk.createData(route_map_entries_url, entries_obj.getxml(filter=True), sdata.getSession(), False)
            if entry == 'match-condition':
                matchcondition_obj = devices.device.route_maps.route_map.route_map_entries.match_condition.match_condition()
                if condition_type is not None:
                    matchcondition_obj.condition_type = condition_type
                if condition_value is not None:
                    matchcondition_obj.value = condition_value
                if condition_type == 'as-path' and condition_value is not None:
                    as_path_acl(condition_value, device, sdata)
                match_condition_url = device.url + '/route-maps/route-map=%s/route-map-entries=%s' % (route_map_name,sequence_number)
                yang.Sdk.createData(match_condition_url, matchcondition_obj.getxml(filter=True), sdata.getSession(), False)
            elif entry == 'set-action':
                set_obj1 = devices.device.route_maps.route_map.route_map_entries.set_action.set_action()
                if set_type is not None:
                    set_obj1.set_type = set_type
                    if set_type == 'ip':
                        if set_ip is None:
                            raise Exception("Please provide ip precedence/df/next-hop")
                        else:
                            set_obj1.ip = set_ip
                if set_value is not None:
                    set_obj1.value = set_value
                set_action_url = device.url + '/route-maps/route-map=%s/route-map-entries=%s' % (route_map_name,sequence_number)
                yang.Sdk.createData(set_action_url, set_obj1.getxml(filter=True), sdata.getSession(), False)
    else:
        print "Route-map is not in device: ", device


def as_path_acl(condition_value, device, sdata):
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])

    xml_output = yang.Sdk.getData(url+"/as-path-acls", '',sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    print "obj: ",obj
    print "xml of as path acl obj: ", obj.toXml()
    yang.Sdk.createData(device.url, '<as-path-acls/>', sdata.getSession(), False)

    if hasattr(obj.as_path_acls, 'as_path_acl'):
        obj.as_path_acls.as_path_acl = util.convert_to_list(obj.as_path_acls.as_path_acl)
        for as_path_acl_obj in obj.as_path_acls.as_path_acl:
            number = as_path_acl_obj.get_field_value('number')
            if condition_value == number:
                condition = as_path_acl_obj.get_field_value('condition')
                expression = as_path_acl_obj.get_field_value('expression')
                as_path_obj = devices.device.as_path_acls.as_path_acl.as_path_acl()
                as_path_obj.number = number
                as_path_obj.condition = condition
                as_path_obj.expression = expression

                as_path_url = device.url + '/as-path-acls'
                yang.Sdk.createData(as_path_url, as_path_obj.getxml(filter=True), sdata.getSession(), False)


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
