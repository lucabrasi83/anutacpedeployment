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
                                              delete-route-maps
                                                               
Schema Representation:

/services/managed-cpe-services/customer/route-maps/delete-route-maps
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
from servicemodel.controller.devices.device import route_maps

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
            uri = sdata.getRcPath()
            uri_list = uri.split('/',5)
            url = '/'.join(uri_list[0:4])
            config = kwargs['config']
            inputdict = kwargs['inputdict']
            if inputdict['single_cpe_site'] == "true":
                if len(inputdict['single_cpe_sites']) > 0:
                    if isinstance(inputdict['single_cpe_sites'], list) is True:
                        for site in inputdict['single_cpe_sites']:
                            #uri = sdata.getRcPath()
                            #uri_list = uri.split('/',5)
                            #url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe'
                            delete_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        delete_route_map(entity, conf, sdata, **kwargs)

            if inputdict['dual_cpe_site'] == "true":
                if len(inputdict['dual_cpe_sites']) > 0:
                    if isinstance(inputdict['dual_cpe_sites'], list) is True:
                        for site in inputdict['dual_cpe_sites']:
                            #uri = sdata.getRcPath()
                            #uri_list = uri.split('/',5)
                            #url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary'
                            delete_route_map(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary'
                            delete_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary'
                        delete_route_map(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary'
                        delete_route_map(entity, conf, sdata, **kwargs)

            if inputdict['single_cpe_dual_wan_site'] == "true":
                if len(inputdict['single_cpe_dual_wan_sites']) > 0:
                    if isinstance(inputdict['single_cpe_dual_wan_sites'], list) is True:
                        for site in inputdict['single_cpe_dual_wan_sites']:
                            #uri = sdata.getRcPath()
                            #uri_list = uri.split('/',5)
                            #url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_dual'
                            delete_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        delete_route_map(entity, conf, sdata, **kwargs)

            if inputdict['triple_cpe_site'] == "true":
                if len(inputdict['triple_cpe_sites']) > 0:
                    if isinstance(inputdict['triple_cpe_sites'], list) is True:
                        for site in inputdict['triple_cpe_sites']:
                            #uri = sdata.getRcPath()
                            #uri_list = uri.split('/',5)
                            #url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary_triple'
                            delete_route_map(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_triple'
                            delete_route_map(entity, conf, sdata, **kwargs)
                            entity = 'cpe_tertiary_triple'
                            delete_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['triple_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_triple'
                        delete_route_map(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_triple'
                        delete_route_map(entity, conf, sdata, **kwargs)
                        entity = 'cpe_tertiary_triple'
                        delete_route_map(entity, conf, sdata, **kwargs)

            if inputdict['dual_cpe_dual_wan_site'] == "true":
                if len(inputdict['dual_cpe_dual_wan_sites']) > 0:
                    if isinstance(inputdict['dual_cpe_dual_wan_sites'], list) is True:
                        for site in inputdict['dual_cpe_dual_wan_sites']:
                            #uri = sdata.getRcPath()
                            #uri_list = uri.split('/',5)
                            #url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary_dual'
                            delete_route_map(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_dual'
                            delete_route_map(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_dual'
                        delete_route_map(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_dual'
                        delete_route_map(entity, conf, sdata, **kwargs)

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
      #raise Exception('Update forbidden for node delete-route-maps at path managed-cpe-services/customer/route-maps/delete-route-maps')
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


def delete_route_map(entity, conf, sdata, **kwargs):
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
    sequence_number = inputdict['sequence_number']

    url_device_route_map = '/controller:devices/device=%s/l3features:route-maps/route-map=%s' %(device.device.id, route_map_name)
    
    '''
    device_route_map = yang.Sdk.getData(url_device_route_map, '', sdata.getTaskId())
    conf_route = util.parseXmlString(device_route_map)

    
    device_route = []
    device_route_entries = []
    device_route_match = []
    device_route_set = []
    if hasattr(conf_route.route_maps, 'route_map'):
        conf_route.route_maps.route_map = util.convert_to_list(conf_route.route_maps.route_map)
        device_route = [routemap.name for routemap in conf_route.route_maps.route_map]
        #for routemap in conf_route.route_maps.route_map:
            #device_route.append(routemap.name)
        if hasattr(routemap, 'route_map_entries'):
            routemap.route_map_entries = util.convert_to_list(routemap.route_map_entries)
            device_route_entries = [entry.seq for entry in routemap.route_map_entries]
            #for entry in routemap.route_map_entries:
                #device_route_entries.append(entry.seq)
            if hasattr(entry, 'match_condition'):
                entry.match_condition = util.convert_to_list(entry.match_condition)
                device_route_match = [match.condition_type + ',' + match.value for match in entry.match_condition]
                        #for match in entry.match_condition:
                            #name = match.condition_type + ',' + match.value
                            #device_route_match.append(name)

            if hasattr(entry, 'set_action'):
                entry.set_action = util.convert_to_list(entry.set_action)
                device_route_set = [set1.set_type + ',' + set1.value for set1 in entry.set_action]
                        #for set1 in entry.set_action:
                            #set_name = set1.set_type + ',' + set1.value
                            #device_route_set.append(set_name)
        '''

    action = inputdict['action']
    entry = inputdict['entry']
    condition_type = inputdict['condition_type']
    condition_value = inputdict['value']
    set_type = inputdict['set_type']
    set_ip = inputdict['ip']
    set_value = inputdict['set_value']
    # if route_map_name in device_route:
    if yang.Sdk.dataExists(url_device_route_map):
        if entry == 'match-condition':
            matchcondition_obj = route_maps.route_map.route_map_entries.match_condition.match_condition()
            if condition_type is not None:
                matchcondition_obj.condition_type = condition_type
            if condition_value is not None:
                matchcondition_obj.value = condition_value
            # if condition_type == 'as-path' and condition_value is not None:
            #     as_path_acl(condition_value, device, sdata)
            if condition_type is not None and condition_value is not None:
                input_name = condition_type + ',' + condition_value
                condition_type = condition_type.replace(' ', '%20')
                condition_value = condition_value.replace(' ', '%20')
                match_condition_url = '/controller:devices/device=%s/l3features:route-maps/route-map=%s/route-map-entries=%s/match-condition=%s,%s' % (device.device.id, route_map_name, sequence_number,condition_type,condition_value)
                #if input_name in device_route_match:
                if yang.Sdk.dataExists(match_condition_url):
                    output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+match_condition_url+'</rc-path></input>')
                    ref = util.parseXmlString(output)
                    log("xml_op:%s" %(ref))
                    if hasattr(ref.output, 'references'):
                        if hasattr(ref.output.references, 'reference'):
                            if hasattr(ref.output.references.reference, 'src_node'):
                                for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                                    yang.Sdk.removeReference(each_ref, match_condition_url)

                    yang.Sdk.deleteData(match_condition_url, matchcondition_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
                else:
                    print "Match condition is not in device: ", device

            
        if entry == 'set-action':
            set_obj1 = route_maps.route_map.route_map_entries.set_action.set_action()
            if set_type is not None:
                set_obj1.set_type = set_type
                if set_type == 'ip':
                    if set_ip is None:
                        raise Exception("Please provide ip precedence/df/next-hop")
                    else:
                        set_obj1.ip = set_ip
            if set_value is not None:
                set_obj1.value = set_value
            if set_type is not None and set_value is not None:
                input_set_name = set_type + ',' + set_value
                set_type = set_type.replace(' ', '%20')
                set_value = set_value.replace(' ', '%20')
                set_action_url = '/controller:devices/device=%s/l3features:route-maps/route-map=%s/route-map-entries=%s/set-action=%s,%s' % (device.device.id, route_map_name,sequence_number,set_type,set_value)
                #if input_set_name in device_route_set:
                if yang.Sdk.dataExists(set_action_url):
                    output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+set_action_url+'</rc-path></input>')
                    ref = util.parseXmlString(output)
                    log("xml_op:%s" %(ref))
                    if hasattr(ref.output, 'references'):
                        if hasattr(ref.output.references, 'reference'):
                            if hasattr(ref.output.references.reference, 'src_node'):
                                for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                                    yang.Sdk.removeReference(each_ref, set_action_url)
                    yang.Sdk.deleteData(set_action_url, set_obj1.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
                else:
                    print "Set action is not in device: ", device

        #Delete Entire Route-Map sequence entry
        if entry == 'delete-sequence-entry':
                route_map_entry_url = '/controller:devices/device=%s/l3features:route-maps/route-map=%s/route-map-entries=%s' % (device.device.id, route_map_name, sequence_number) 
                # if sequence_number in device_route_entries:
                if yang.Sdk.dataExists(route_map_entry_url):
                    output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+route_map_entry_url+'</rc-path></input>')
                    ref = util.parseXmlString(output)
                    log("xml_op:%s" %(ref))
                    if hasattr(ref.output, 'references'):
                        if hasattr(ref.output.references, 'reference'):
                            for eachreference in util.convert_to_list(ref.output.references.reference):
                                if hasattr(eachreference, 'src_node'):
                                    for each_ref in util.convert_to_list(eachreference.src_node):
                                        yang.Sdk.removeReference(each_ref, eachreference.dest_node)
                    yang.Sdk.deleteData(route_map_entry_url, None, sdata.getTaskId(), sdata.getSession())
                else:
                    print "Set action is not in device: ", device
    else:
        yang.Sdk.append_taskdetail(sdata.getTaskId(), "Route-Map " + str(route_map_name) + " not found on device " + str(device.device.id) + ". Skipping this device")       
                
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
