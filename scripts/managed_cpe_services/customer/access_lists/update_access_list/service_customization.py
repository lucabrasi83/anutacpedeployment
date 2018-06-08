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
                                    access-lists
                                                |
                                                update-access-list
                                                                  
Schema Representation:

/services/managed-cpe-services/customer/access-lists/update-access-list
"""
"""
Names of Leafs for this Yang Entity
                  id
    access-list-name
   access-list-entry
           operation
            acl-name
              action
            protocol
    service-obj-name
    source-condition
       source-object
 source-object-group
destination-condition
  destination-object
destination-object-group
         port-number
       match-packets
          precedence
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
from servicemodel.controller.devices.device import object_groups_acl
from servicemodel.controller.devices.device import access_lists

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject
from cpedeployment.cpedeployment_lib import log
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
        inputkeydict = kwargs['inputkeydict']

    @staticmethod
    def process_service_device_bindings(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the device bindings or Call the Business Login Handlers"""
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
            inputkeydict = kwargs['inputkeydict']
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
                            if inputdict['operation'] == 'DELETE':
                                delete_acl(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_acl(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        if inputdict['operation'] == 'DELETE':
                            delete_acl(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_acl(entity, conf, sdata, **kwargs)

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
                            if inputdict['operation'] == 'DELETE':
                                delete_acl(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_acl(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary'
                            if inputdict['operation'] == 'DELETE':
                                delete_acl(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_acl(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary'
                        if inputdict['operation'] == 'DELETE':
                            delete_acl(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_acl(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary'
                        if inputdict['operation'] == 'DELETE':
                            delete_acl(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_acl(entity, conf, sdata, **kwargs)

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
                            if inputdict['operation'] == 'DELETE':
                                delete_acl(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_acl(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        if inputdict['operation'] == 'DELETE':
                            delete_acl(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_acl(entity, conf, sdata, **kwargs)

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
                            if inputdict['operation'] == 'DELETE':
                                delete_acl(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_acl(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_triple'
                            if inputdict['operation'] == 'DELETE':
                                delete_acl(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_acl(entity, conf, sdata, **kwargs)
                            entity = 'cpe_tertiary_triple'
                            if inputdict['operation'] == 'DELETE':
                                delete_acl(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_acl(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['triple_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_triple'
                        if inputdict['operation'] == 'DELETE':
                            delete_acl(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_acl(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_triple'
                        if inputdict['operation'] == 'DELETE':
                            delete_acl(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_acl(entity, conf, sdata, **kwargs)
                        entity = 'cpe_tertiary_triple'
                        if inputdict['operation'] == 'DELETE':
                            delete_acl(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_acl(entity, conf, sdata, **kwargs)

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
                            if inputdict['operation'] == 'DELETE':
                                delete_acl(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_acl(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_dual'
                            if inputdict['operation'] == 'DELETE':
                                delete_acl(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_acl(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_dual'
                        if inputdict['operation'] == 'DELETE':
                            delete_acl(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_acl(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_dual'
                        if inputdict['operation'] == 'DELETE':
                            delete_acl(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_acl(entity, conf, sdata, **kwargs)

            if util.isNotEmpty(inputdict['device_group']):
                dev_group_output = yang.Sdk.invokeRpc('controller:apply-data-grouping', '''<input><group-name>'''+ inputdict['device_group'] + '''</group-name></input>''')
                dev_group_obj = util.parseXmlString(dev_group_output)
                if hasattr(dev_group_obj, 'output'):
                    if hasattr(dev_group_obj.output, 'result'):
                        for each_dev in util.convert_to_list(dev_group_obj.output.result):
                            if hasattr(each_dev, 'device'):
                                if hasattr(each_dev.device, 'id'):
                                    if inputdict['operation'] == 'DELETE':
                                        delete_acl(each_dev.device.id, None, sdata, **kwargs)
                                    elif inputdict['operation'] == 'CREATE':
                                        create_acl(each_dev.device.id, None, sdata, **kwargs)
            modify_acl(sdata, **kwargs)

    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      #raise Exception('Update forbidden for node update-access-list at path managed-cpe-services/customer/access-lists/update-access-list')
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

def modify_acl(sdata, **kwargs):
    uri = sdata.getRcPath()
    uri_list = uri.split('/', 5)
    url = '/'.join(uri_list[0:4])
    inputdict = kwargs['inputdict']
    access_list_name = inputdict['access_list_name']
    if inputdict['operation'] == 'CREATE' and inputdict['update_acl_in_profile'] == 'true':
        url = url + "/access-lists/access-list=" + str(access_list_name)
        acl_sequence_num = '' if util.isEmpty(inputdict['acl_sequence_num']) else inputdict['acl_sequence_num']
        rule_name = '' if util.isEmpty(inputdict['rule_name']) else inputdict['rule_name']
        action = '' if util.isEmpty(inputdict['action']) else inputdict['action']
        protocol = '' if util.isEmpty(inputdict['protocol']) else inputdict['protocol']
        service_obj_name = '' if util.isEmpty(inputdict['service_obj_name']) else inputdict['service_obj_name']
        source_condition = '' if util.isEmpty(inputdict['source_condition']) else inputdict['source_condition']
        source_object = '' if util.isEmpty(inputdict['source_object']) else inputdict['source_object']
        source_object_group = '' if util.isEmpty(inputdict['source_object_group']) else inputdict['source_object_group']
        destination_condition = '' if util.isEmpty(inputdict['destination_condition']) else inputdict['destination_condition']
        destination_object = '' if util.isEmpty(inputdict['destination_object']) else inputdict['destination_object']
        destination_object_group = '' if util.isEmpty(inputdict['destination_object_group']) else inputdict['destination_object_group']
        port_number = '' if util.isEmpty(inputdict['port_number']) else inputdict['port_number']
        match_packets = '' if util.isEmpty(inputdict['match_packets']) else inputdict['match_packets']
        precedence = '' if util.isEmpty(inputdict['precedence']) else inputdict['precedence']
        dscp = '' if util.isEmpty(inputdict['dscp']) else inputdict['dscp']
        source_port = '' if util.isEmpty(inputdict['source_port']) else inputdict['source_port']
        dest_port_operator = '' if util.isEmpty(inputdict['dest_port_operator']) else inputdict['dest_port_operator']
        source_port_operator = '' if util.isEmpty(inputdict['source_port_operator']) else inputdict['source_port_operator']
        payload = '''
                    <access-list-rules>
                    <name>'''+rule_name+'''</name>
                    <action>'''+action+'''</action>
                    <protocol>'''+protocol+'''</protocol>
                    <acl-sequence-num>'''+acl_sequence_num+'''</acl-sequence-num>
                    <service-obj-name>'''+service_obj_name+'''</service-obj-name>
                    <source-condition>'''+source_condition+'''</source-condition>
                    <source-object>'''+source_object+'''</source-object>
                    <source-object-group>'''+source_object_group+'''</source-object-group>
                    <destination-condition>'''+destination_condition+'''</destination-condition>
                    <destination-object>'''+destination_object+'''</destination-object>
                    <destination-object-group>'''+destination_object_group+'''</destination-object-group>
                    <match-packets>'''+match_packets+'''</match-packets>
                    <dscp>'''+dscp+'''</dscp>
                    <precedence>'''+precedence+'''</precedence>
                    <port-number>'''+port_number+'''</port-number>
                    <dest-port-operator>'''+dest_port_operator+'''</dest-port-operator>
                    <source-port>'''+source_port+'''</source-port>
                    <source-port-operator>'''+source_port_operator+'''</source-port-operator>
                    </access-list-rules>
                  '''
        yang.Sdk.createData(url, payload, sdata.getSession(), False)

        uri_add_acl = sdata.getRcPath()
        add_acl_output = yang.Sdk.getData(uri_add_acl, '', sdata.getTaskId())
        add_acl_obj = util.parseXmlString(add_acl_output)

        if hasattr(add_acl_obj.update_access_list, 'additional_acl_entry'):
            add_acl_list = util.convert_to_list(add_acl_obj.update_access_list.additional_acl_entry)

            for add_rule in add_acl_list:
                add_acl_sequence_num = add_rule.acl_sequence_number if hasattr(add_rule, 'acl_sequence_number') and util.isNotEmpty(add_rule.acl_sequence_number) else ''
                add_rule_name = add_rule.rule_name if hasattr(add_rule, 'rule_name') and util.isNotEmpty(add_rule.rule_name) else ''
                add_action = add_rule.action if hasattr(add_rule, 'action') and util.isNotEmpty(add_rule.action) else ''
                add_protocol = add_rule.protocol if hasattr(add_rule, 'protocol') and util.isNotEmpty(add_rule.protocol) else ''
                add_service_obj_name = add_rule.service_obj_name if hasattr(add_rule, 'service_obj_name') and util.isNotEmpty(add_rule.service_obj_name) else ''
                add_source_condition = add_rule.source_condition if hasattr(add_rule, 'source_condition') and util.isNotEmpty(add_rule.source_condition) else ''
                add_source_object = add_rule.source_object if hasattr(add_rule, 'source_object') and util.isNotEmpty(add_rule.source_object) else ''
                add_source_object_group = add_rule.source_object_group if hasattr(add_rule, 'source_object_group') and util.isNotEmpty(add_rule.source_object_group) else ''
                add_destination_condition = add_rule.destination_condition if hasattr(add_rule, 'destination_condition') and util.isNotEmpty(add_rule.destination_condition) else ''
                add_destination_object = add_rule.destination_object if hasattr(add_rule, 'destination_object') and util.isNotEmpty(add_rule.destination_object) else ''
                add_destination_object_group = add_rule.destination_object_grouptin if hasattr(add_rule, 'destination_object_group') and  util.isNotEmpty(add_rule.destination_object_group) else ''
                add_port_number = add_rule.port_number if hasattr(add_rule, 'port_number') and util.isNotEmpty(add_rule.port_number) else ''
                add_match_packets = add_rule.match_packets if hasattr(add_rule, 'match_packet') and util.isNotEmpty(add_rule.match_packets) else ''
                add_precedence = add_rule.precedence if hasattr(add_rule, 'precedence') and util.isNotEmpty(add_rule.precedence) else ''
                add_dscp = add_rule.dscp if hasattr(add_rule, 'dscp') and util.isNotEmpty(ad_rule.dscp) else ''
                add_source_port = add_rule.source_port if hasattr(add_rule, 'source_port') and util.isNotEmpty(add_rule.source_port) else ''
                add_dest_port_operator = add_rule.dest_port_operator if hasattr(add_rule, 'dest_port_operator') and util.isNotEmpty(add_rule.dest_port_operator) else ''
                add_source_port_operator = add_rule.source_port_operator if hasattr(add_rule, 'source_port_operator') and util.isNotEmpty(add_rule.source_port_operator) else ''
                add_payload = '''
                    <access-list-rules>
                    <name>'''+add_rule_name+'''</name>
                    <action>'''+add_action+'''</action>
                    <protocol>'''+add_protocol+'''</protocol>
                    <acl-sequence-num>'''+add_acl_sequence_num+'''</acl-sequence-num>
                    <service-obj-name>'''+add_service_obj_name+'''</service-obj-name>
                    <source-condition>'''+add_source_condition+'''</source-condition>
                    <source-object>'''+add_source_object+'''</source-object>
                    <source-object-group>'''+add_source_object_group+'''</source-object-group>
                    <destination-condition>'''+add_destination_condition+'''</destination-condition>
                    <destination-object>'''+add_destination_object+'''</destination-object>
                    <destination-object-group>'''+add_destination_object_group+'''</destination-object-group>
                    <match-packets>'''+add_match_packets+'''</match-packets>
                    <dscp>'''+add_dscp+'''</dscp>
                    <precedence>'''+add_precedence+'''</precedence>
                    <port-number>'''+add_port_number+'''</port-number>
                    <dest-port-operator>'''+add_dest_port_operator+'''</dest-port-operator>
                    <source-port>'''+add_source_port+'''</source-port>
                    <source-port-operator>'''+add_source_port_operator+'''</source-port-operator>
                    </access-list-rules>
                  '''
                yang.Sdk.createData(url, add_payload, sdata.getSession(), False)

    if inputdict['operation'] == 'DELETE' and inputdict['update_acl_in_profile'] == 'true':
        acl_name = '' if util.isEmpty(inputdict['acl_name']) else inputdict['acl_name']
        action = '' if util.isEmpty(inputdict['action']) else inputdict['action']
        url = url + "/access-lists/access-list=" + str(access_list_name) + "/access-list-rules=" + str(acl_name) + "," +str(action)
        yang.Sdk.deleteData(url, '', sdata.getTaskId(), sdata.getSession())

def object_group_def(source_object_group, dev, sdata):
    uri = sdata.getRcPath()
    uri_list = uri.split('/', 5)
    url = '/'.join(uri_list[0:4])
    xml_output = yang.Sdk.getData(url+"/object-groups/object-group="+str(source_object_group), '', sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    objectgroup_obj = object_groups_acl.object_group.object_group()
    objectgroup_obj.name = obj.object_group.name
    objectgroup_obj.type = obj.object_group.type
    if hasattr(obj.object_group, 'description'):
        if util.isNotEmpty(obj.object_group.description):
            objectgroup_obj.description = obj.object_group.description
    objectgroup_url = dev.url + '/acl:object-groups-acl'
    #yang.Sdk.createData(dev.url, '<object-groups-acl/>', sdata.getSession())
    yang.Sdk.createData(objectgroup_url, objectgroup_obj.getxml(filter=True), sdata.getSession())
    if hasattr(obj.object_group, 'networks'):
        if hasattr(obj.object_group.networks, 'network'):
            for objectgroup in util.convert_to_list(obj.object_group.networks.network):
                net_url = dev.url + '/acl:object-groups-acl/object-group=%s' %(obj.object_group.name)
                #yang.Sdk.createData(net_url, '<networks/>', sdata.getSession())

                if hasattr(objectgroup, 'group_object'):
                    if util.isNotEmpty(objectgroup.group_object):
                        network_obj = object_groups_acl.object_group.networks.network.network()
                        network_obj.group_object = objectgroup.group_object
                        network_obj.name = "group-object" + " " + objectgroup.group_object
                        network_url = dev.url + '/acl:object-groups-acl/object-group=%s/networks' %(obj.object_group.name)
                        yang.Sdk.createData(network_url, network_obj.getxml(filter=True), sdata.getSession())

                if hasattr(objectgroup, 'host'):
                    if util.isNotEmpty(objectgroup.host):
                        network_obj1 = object_groups_acl.object_group.networks.network.network()
                        network_obj1.host = objectgroup.host
                        network_obj1.name = "host" + " " + objectgroup.host
                        network_url = dev.url + '/acl:object-groups-acl/object-group=%s/networks' %(obj.object_group.name)
                        yang.Sdk.createData(network_url, network_obj1.getxml(filter=True), sdata.getSession())

                if hasattr(objectgroup, 'prefix'):
                    if util.isNotEmpty(objectgroup.prefix):
                        network_obj2 = object_groups_acl.object_group.networks.network.network()
                        #Haulotte Specific Dual CPE Sites. Keyword 'GUEST_LAN_PROFILE' to be replaced by GUEST LAN Profile CIDR
                        if objectgroup.prefix == 'HAULOTTE-GUESTS':
                            obj_haulotte_guests = getLocalObject(sdata, 'dual-cpe-site-services')
                            log("haulotte guest obj is: %s" % (obj_haulotte_guests))
                            obj_haulotte_guests.dual_cpe_site_services.cpe_lan.lan_profile = util.convert_to_list(obj_haulotte_guests.dual_cpe_site_services.cpe_lan.lan_profile)
                            for lanprof in obj_haulotte_guests.dual_cpe_site_services.cpe_lan.lan_profile:
                                if lanprof.profile_name == 'GUEST_LAN_PROFILE':
                                    haulotte_guests_prefix = lanprof.get_field_value('cidr')
                                    prefix = util.IPPrefix(haulotte_guests_prefix)
                        else:
                            prefix = util.IPPrefix(objectgroup.prefix)
                        ip_address = prefix.address
                        netmask = prefix.netmask
                        network_obj2.ip_address = ip_address
                        network_obj2.netmask = netmask
                        network_obj2.name = ip_address + " " + netmask
                        network_url = dev.url + '/acl:object-groups-acl/object-group=%s/networks' %(obj.object_group.name)
                        yang.Sdk.createData(network_url, network_obj2.getxml(filter=True), sdata.getSession())

    if hasattr(obj.object_group, 'services'):
        
        if hasattr(obj.object_group.services, 'service'):

            port_dict = { '179': 'bgp', '19': 'chargen', '514': 'cmd', '13': 'daytime', '9': 'discard', '53': 'domain',
                          '3949': 'drip', '7': 'echo', '512': 'exec', '79': 'finger', '21': 'ftp', '20': 'ftp-data',
                          '70': 'gopher', '101': 'hostname', '113': 'ident', '194': 'irc', '543': 'klogin', '544': 'kshell',
                          '513': 'login', '515': 'lpd', '119': 'nntp', '15001': 'onep-plain', '15002': 'onep-tls', '496': 'pim-auto-rp',
                          '109': 'pop2', '110': 'pop3', '25': 'smtp', '111': 'sunrpc', '49': 'tacacs', '517': 'talk', '23': 'telnet',
                          '37': 'time', '540': 'uucp', '43': 'whois', '80': 'www', '135': 'msrpc'
                          }
            udp_port_dict = { '512': 'biff', '68': 'bootpc', '67': 'bootps', '9': 'discard', '195': 'dnsix',
                          '53': 'domain', '7': 'echo', '500': 'isakmp', '434': 'mobile-ip', '42': 'nameserver', '138': 'netbios-dgm',
                          '137': 'netbios-ns', '139': 'netbios-ss', '4500': 'non500-isakmp', '123': 'ntp', '496': 'pim-auto-rp',
                          '520': 'rip', '161': 'snmp', '162': 'snmptrap', '111': 'sunrpc', '514': 'syslog', '49': 'tacacs',
                          '517': 'talk', '69': 'tftp', '37': 'time', '513': 'who', '177': 'xdmcp', '135': 'msrpc'
                          }
            ip_prot_dict = { '47': 'gre', '1': 'icmp', '6': 'tcp', '17': 'udp', '51': 'ahp', '50': 'esp', '89': 'ospf',
                             '4': 'ipinip', '88': 'eigrp', '2': 'igmp', '94': 'nos', '103': 'pim'
                            }

            service_url = dev.url + '/acl:object-groups-acl/object-group=%s/services' %(obj.object_group.name)

            for objectgroup in util.convert_to_list(obj.object_group.services.service):
                if hasattr(objectgroup, 'group_object'):
                    if util.isNotEmpty(objectgroup.group_object):
                        service_obj = object_groups_acl.object_group.services.service.service()
                        service_obj.group_object = objectgroup.group_object
                        service_obj.name = "group-object" + " " + objectgroup.group_object
                        yang.Sdk.createData(service_url, service_obj.getxml(filter=True), sdata.getSession())

                if hasattr(objectgroup, 'protocol_type'):
                    if util.isNotEmpty(objectgroup.protocol_type):
                        if objectgroup.protocol_type == "IP-Protocol-Number":
                            service_obj1 = object_groups_acl.object_group.services.service.service()
                            if util.isNotEmpty(objectgroup.ip_protocol):
                                
                                ip_prot_num = objectgroup.ip_protocol
                                if ip_prot_num in ip_prot_dict:
                                    ip_prot_num = ip_prot_dict[ip_prot_num]
                                    service_obj1.protocol = ip_prot_num
                                    service_obj1.name = ip_prot_num
                                else:
                                    service_obj1.ip_protocol = ip_prot_num
                                    service_obj1.name = ip_prot_num

                                yang.Sdk.createData(service_url, service_obj1.getxml(filter=True), sdata.getSession())

                        if  objectgroup.protocol_type == "Protocol-Name":
                            service_obj_name_list = []
                            service_obj2 = object_groups_acl.object_group.services.service.service()
                            if util.isNotEmpty(objectgroup.protocol_name):
                                service_obj2.protocol = objectgroup.protocol_name
                                service_obj_name_list.append(objectgroup.protocol_name)

                            if hasattr(objectgroup, 'port_operation'):
                                if util.isNotEmpty(objectgroup.port_operation):
                                    service_obj2.operation = objectgroup.port_operation
                                    service_obj_name_list.append(objectgroup.port_operation)

                            if hasattr(objectgroup, 'operator'):
                                if util.isNotEmpty(objectgroup.operator):
                                    service_obj2.compare = objectgroup.operator
                                    service_obj_name_list.append(objectgroup.operator)

                            if hasattr(objectgroup, 'port_number'):
                                if util.isNotEmpty(objectgroup.port_number):
                                    port_num = objectgroup.port_number
                                    if objectgroup.protocol_name == "tcp":
                                        if port_num in port_dict:
                                            port_num = port_dict[port_num]
                                    elif objectgroup.protocol_name == "udp":
                                        if port_num in udp_port_dict:
                                            port_num = udp_port_dict[port_num]

                                    service_obj2.port = port_num
                                    service_obj_name_list.append(port_num)

                            if hasattr(objectgroup, 'end_port'):
                                if util.isNotEmpty(objectgroup.end_port):
                                    end_port_num = objectgroup.end_port
                                    if objectgroup.protocol_name == "tcp":
                                        if end_port_num in port_dict:
                                            end_port_num = port_dict[end_port_num]
                                    elif objectgroup.protocol_name == "udp":
                                        if end_port_num in udp_port_dict:
                                            end_port_num = udp_port_dict[end_port_num]
                                            
                                    service_obj2.end_port = end_port_num
                                    service_obj_name_list.append(end_port_num)

                            service_obj_name = ' '.join(service_obj_name_list)

                            service_obj2.name = service_obj_name

                            yang.Sdk.createData(service_url, service_obj2.getxml(filter=True), sdata.getSession())


def create_acl(entity, conf, sdata, **kwargs):
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
    else:
        device = devicemgr.getDeviceById(entity)

    inputdict = kwargs['inputdict']
    access_list_name = inputdict['access_list_name']
    rule_name = inputdict['rule_name']
    access_list_entry = inputdict['access_list_entry']
    acl_sequence_num = inputdict['acl_sequence_num']
    operation = inputdict['operation']
    #acl_name = inputdict['acl_name']
    action = inputdict['action']
    protocol = inputdict['protocol']
    service_obj_name = inputdict['service_obj_name']
    source_condition = inputdict['source_condition']
    source_object = inputdict['source_object']
    source_object_group = inputdict['source_object_group']
    destination_condition = inputdict['destination_condition']
    destination_object = inputdict['destination_object']
    destination_object_group = inputdict['destination_object_group']
    source_port_operator = inputdict['source_port_operator']
    dest_port_operator = inputdict['dest_port_operator']
    port_number = inputdict['port_number']
    match_packets = inputdict['match_packets']
    precedence = inputdict['precedence']
    dscp = inputdict['dscp']
    source_port = inputdict['source_port']

    url_device_acl = '/controller:devices/device=%s/acl:access-lists/access-list=%s' %(device.device.id, access_list_name)
    '''
    dev_acl = yang.Sdk.getData(url_device_acl, '', sdata.getTaskId())
    conf_acl = util.parseXmlString(dev_acl)

    device_acl = []
    if hasattr(conf_acl.access_lists, 'access_list'):
        conf_acl.access_lists.access_list = util.convert_to_list(conf_acl.access_lists.access_list )
        #for acl in conf_acl.access_lists.access_list:
            #device_acl.append(acl.name)
        device_acl = [acl.name for acl in conf_acl.access_lists.access_list]

    if access_list_name in device_acl:
    '''
    if yang.Sdk.dataExists(url_device_acl):
        name_rule = []
        access_rule_obj = access_lists.access_list.acl_rules.acl_rule.acl_rule()
        port_dict = { '179': 'bgp', '19': 'chargen', '514': 'cmd', '13': 'daytime', '9': 'discard', '53': 'domain',
                          '3949': 'drip', '7': 'echo', '512': 'exec', '79': 'finger', '21': 'ftp', '20': 'ftp-data',
                          '70': 'gopher', '101': 'hostname', '113': 'ident', '194': 'irc', '543': 'klogin', '544': 'kshell',
                          '513': 'login', '515': 'lpd', '119': 'nntp', '15001': 'onep-plain', '15002': 'onep-tls', '496': 'pim-auto-rp',
                          '109': 'pop2', '110': 'pop3', '25': 'smtp', '111': 'sunrpc', '49': 'tacacs', '517': 'talk', '23': 'telnet',
                          '37': 'time', '540': 'uucp', '43': 'whois', '80': 'www', '135': 'msrpc'
                          }
        udp_port_dict = { '512': 'biff', '68': 'bootpc', '67': 'bootps', '9': 'discard', '195': 'dnsix',
                          '53': 'domain', '7': 'echo', '500': 'isakmp', '434': 'mobile-ip', '42': 'nameserver', '138': 'netbios-dgm',
                          '137': 'netbios-ns', '139': 'netbios-ss', '4500': 'non500-isakmp', '123': 'ntp', '496': 'pim-auto-rp',
                          '520': 'rip', '161': 'snmp', '162': 'snmptrap', '111': 'sunrpc', '514': 'syslog', '49': 'tacacs',
                          '517': 'talk', '69': 'tftp', '37': 'time', '513': 'who', '177': 'xdmcp', '135': 'msrpc'
                          }
        access_rule_obj.action = action
        access_rule_obj.layer4protocol = protocol
        if util.isNotEmpty(acl_sequence_num):
            access_rule_obj.linenumber = acl_sequence_num
            #name_rule = acl_sequence_num + ' ' + action + ' ' + protocol
            #name_rule = action + ' ' + protocol
        if util.isNotEmpty(protocol):
            #name_rule = action + ' ' + protocol
            name_rule.append(action)
            name_rule.append(protocol)
        else:
            #name_rule = action
            name_rule.append(action)
        if util.isNotEmpty(service_obj_name):
            object_group_def(service_obj_name, device, sdata)
            access_rule_obj.service_obj_name = service_obj_name
            #name_rule += ' ' + service_obj_name
            name_rule.append(service_obj_name)
        access_rule_obj.source_condition_type = source_condition
        if source_condition == 'cidr':
            cidr_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])' + '/(([0-9])|([1-2][0-9])|(3[0-2]))$';
            if re.match(cidr_pattern,source_object) == None:
                raise Exception ("Please provide valid CIDR for source-object in access-list")
            prefix = util.IPPrefix(source_object)
            ip_address = prefix.address
            netmask = prefix.wildcard
            access_rule_obj.source_mask = netmask
            (addrStr, cidrStr) = source_object.split('/')
            addr = addrStr.split('.')
            cidr = int(cidrStr)
            mask = [0, 0, 0, 0]
            for i in xrange(cidr):
                mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
            #net = []
            #for i in range(4):
                #net.append(int(addr[i]) & mask[i])
            net = [int(addr[i]) & mask[i] for i in xrange(4)]

            network = ".".join(map(str, net))
            #name_rule += ' ' + network + ' ' + netmask
            name_rule.append(network)
            name_rule.append(netmask)
            access_rule_obj.source_ip = network
        if source_condition == 'host':
            host_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$';
            if re.match(host_pattern,source_object) == None:
                raise Exception ("Please provide valid ip-address for source-object in access-list")
            access_rule_obj.source_ip = source_object
            #name_rule += ' ' + 'host' + ' ' + source_object
            name_rule.append('host')
            name_rule.append(source_object)
        if source_condition == 'objectgroup':
            if util.isNotEmpty(source_object_group):
                object_group_def(source_object_group, device, sdata)
                access_rule_obj.source_obj_name = source_object_group
                #name_rule += ' ' + 'object-group' + ' ' + source_object_group
                name_rule.append('object-group')
                name_rule.append(source_object_group)
        if source_condition == 'any':
            #name_rule += ' ' + 'any'
            name_rule.append('any')
        if util.isNotEmpty(source_port):
                if util.isEmpty(source_port_operator):
                    raise Exception("Please provide Source Port Operator in acl")
                access_rule_obj.source_port_operator = source_port_operator
                each_port = source_port.split(' ')
                if protocol == 'tcp':
                    each_port = ([port_dict[each] if each in port_dict else each for each in each_port])
                elif protocol == 'udp':
                    each_port = ([udp_port_dict[each] if each in udp_port_dict else each for each in each_port])
                source_port = ' '.join(each_port)
                access_rule_obj.source_port = source_port
                #name_rule += ' ' + source_port_operator + ' ' + source_port
                name_rule.append(source_port_operator)
                name_rule.append(source_port)
        access_rule_obj.dest_condition_type = destination_condition
        if destination_condition == 'cidr':
            cidr_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])' + '/(([0-9])|([1-2][0-9])|(3[0-2]))$';
            if re.match(cidr_pattern,destination_object) == None:
                raise Exception ("Please provide valid CIDR for destination-object in access-list")
            prefix = util.IPPrefix(destination_object)
            ip_address = prefix.address
            netmask = prefix.wildcard
            access_rule_obj.dest_mask = netmask
            (addrStr, cidrStr) = destination_object.split('/')
            addr = addrStr.split('.')
            cidr = int(cidrStr)
            mask = [0, 0, 0, 0]
            for i in range(cidr):
                mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
            #net = []
            #for i in range(4):
                #net.append(int(addr[i]) & mask[i])
            net = [int(addr[i]) & mask[i] for i in xrange(4)]

            network = ".".join(map(str, net))
            #name_rule += ' ' + network + ' ' + netmask
            name_rule.append(network)
            name_rule.append(netmask)
            access_rule_obj.dest_ip = network
        if destination_condition == 'host':
            host_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$';
            if re.match(host_pattern,destination_object) == None:
                raise Exception ("Please provide valid ip-address for destination-object in access-list")
            access_rule_obj.dest_ip = destination_object
            #name_rule += ' ' + 'host' + ' ' + destination_object
            name_rule.append('host')
            name_rule.append(destination_object)
        if destination_condition == 'objectgroup':
            if util.isNotEmpty(destination_object_group):
                object_group_def(destination_object_group, device, sdata)
                access_rule_obj.dest_obj_name = destination_object_group
                #name_rule += ' ' + 'object-group' + ' ' + destination_object_group
                name_rule.append('object-group')
                name_rule.append(destination_object_group)
        if destination_condition == 'any':
            #name_rule += ' ' + 'any'
            name_rule.append('any')
        if util.isNotEmpty(port_number):
                if util.isEmpty(dest_port_operator):
                    raise Exception("Please provide Destination Port Operator in acl")
                access_rule_obj.dest_port_operator = dest_port_operator
                each_port = port_number.split(' ')
                if protocol == 'tcp':
                    each_port = ([port_dict[each] if each in port_dict else each for each in each_port])
                elif protocol == 'udp':
                    each_port = ([udp_port_dict[each] if each in udp_port_dict else each for each in each_port])
                port_number = ' '.join(each_port)
                access_rule_obj.dest_port = port_number
                #name_rule += ' ' + dest_port_operator + ' ' + port_number
                name_rule.append(dest_port_operator)
                name_rule.append(port_number)
        if util.isNotEmpty(match_packets):
            access_rule_obj.match_packets = match_packets
            #name_rule += ' ' + match_packets
            name_rule.append(match_packets)
        if match_packets == 'precedence':
            if util.isNotEmpty(precedence):
                access_rule_obj.precedence = precedence
                #name_rule += ' ' + precedence
                name_rule.append(precedence)
        else:
            if util.isNotEmpty(dscp):
                access_rule_obj.precedence = dscp
                #name_rule += ' ' + dscp
                name_rule.append(dscp)
        
        access_rule_obj.name = ' '.join(name_rule)
        #access_rules_url = device.url + "/access-lists/access-list=%s" %(access_list_name)
        #yang.Sdk.createData(access_rules_url, '<acl-rules/>', sdata.getSession())

        access_rule_url = device.url + '/acl:access-lists/access-list=%s/acl-rules' %(access_list_name)
        yang.Sdk.createData(access_rule_url, access_rule_obj.getxml(filter=True), sdata.getSession(), False)

        uri_add_acl = sdata.getRcPath()
        add_acl_output = yang.Sdk.getData(uri_add_acl, '', sdata.getTaskId())
        add_acl_obj = util.parseXmlString(add_acl_output)

        if hasattr(add_acl_obj.update_access_list, 'additional_acl_entry'):
            add_acl_list = util.convert_to_list(add_acl_obj.update_access_list.additional_acl_entry)

            for add_rule in add_acl_list:
                add_name_rule = []
                add_access_rule_obj = access_lists.access_list.acl_rules.acl_rule.acl_rule()
                port_dict = { '179': 'bgp', '19': 'chargen', '514': 'cmd', '13': 'daytime', '9': 'discard', '53': 'domain',
                                  '3949': 'drip', '7': 'echo', '512': 'exec', '79': 'finger', '21': 'ftp', '20': 'ftp-data',
                                  '70': 'gopher', '101': 'hostname', '113': 'ident', '194': 'irc', '543': 'klogin', '544': 'kshell',
                                  '513': 'login', '515': 'lpd', '119': 'nntp', '15001': 'onep-plain', '15002': 'onep-tls', '496': 'pim-auto-rp',
                                  '109': 'pop2', '110': 'pop3', '25': 'smtp', '111': 'sunrpc', '49': 'tacacs', '517': 'talk', '23': 'telnet',
                                  '37': 'time', '540': 'uucp', '43': 'whois', '80': 'www', '135': 'msrpc'
                                  }
                udp_port_dict = { '512': 'biff', '68': 'bootpc', '67': 'bootps', '9': 'discard', '195': 'dnsix',
                                  '53': 'domain', '7': 'echo', '500': 'isakmp', '434': 'mobile-ip', '42': 'nameserver', '138': 'netbios-dgm',
                                  '137': 'netbios-ns', '139': 'netbios-ss', '4500': 'non500-isakmp', '123': 'ntp', '496': 'pim-auto-rp',
                                  '520': 'rip', '161': 'snmp', '162': 'snmptrap', '111': 'sunrpc', '514': 'syslog', '49': 'tacacs',
                                  '517': 'talk', '69': 'tftp', '37': 'time', '513': 'who', '177': 'xdmcp', '135': 'msrpc'
                                  }
                add_access_rule_obj.action = add_rule.action
                if hasattr(add_rule, 'protocol') and util.isNotEmpty(add_rule.protocol):
                    add_access_rule_obj.layer4protocol = add_rule.protocol
                else:
                    add_access_rule_obj.layer4protocol = None
                if hasattr(add_rule, 'acl_sequence_num') and util.isNotEmpty(add_rule.acl_sequence_num):
                    add_access_rule_obj.linenumber = add_rule.acl_sequence_num
                    #name_rule = acl_sequence_num + ' ' + action + ' ' + protocol
                    #name_rule = action + ' ' + protocol
                if hasattr(add_rule, 'protocol') and util.isNotEmpty(add_rule.protocol):
                    #name_rule = action + ' ' + protocol
                    add_name_rule.append(add_rule.action)
                    add_name_rule.append(add_rule.protocol)
                else:
                    #name_rule = action
                    add_name_rule.append(add_rule.action)
                if hasattr(add_rule, 'service_obj_name') and util.isNotEmpty(add_rule.service_obj_name):
                    object_group_def(add_rule.service_obj_name, device, sdata)
                    add_access_rule_obj.service_obj_name = add_rule.service_obj_name
                    #name_rule += ' ' + service_obj_name
                    add_name_rule.append(add_rule.service_obj_name)
                add_access_rule_obj.source_condition_type = add_rule.source_condition
                if add_rule.source_condition == 'cidr':
                    cidr_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])' + '/(([0-9])|([1-2][0-9])|(3[0-2]))$';
                    if re.match(cidr_pattern,add_rule.source_object) == None:
                        raise Exception ("Please provide valid CIDR for source-object in access-list")
                    prefix = util.IPPrefix(add_rule.source_object)
                    ip_address = prefix.address
                    netmask = prefix.wildcard
                    add_access_rule_obj.source_mask = netmask
                    (addrStr, cidrStr) = add_rule.source_object.split('/')
                    addr = addrStr.split('.')
                    cidr = int(cidrStr)
                    mask = [0, 0, 0, 0]
                    for i in xrange(cidr):
                        mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
                    #net = []
                    #for i in range(4):
                        #net.append(int(addr[i]) & mask[i])
                    net = [int(addr[i]) & mask[i] for i in xrange(4)]

                    network = ".".join(map(str, net))
                    #name_rule += ' ' + network + ' ' + netmask
                    add_name_rule.append(network)
                    add_name_rule.append(netmask)
                    add_access_rule_obj.source_ip = network
                if add_rule.source_condition == 'host':
                    host_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$';
                    if re.match(host_pattern,add_rule.source_object) == None:
                        raise Exception ("Please provide valid ip-address for source-object in access-list")
                    add_access_rule_obj.source_ip = add_rule.source_object
                    #name_rule += ' ' + 'host' + ' ' + source_object
                    add_name_rule.append('host')
                    add_name_rule.append(add_rule.source_object)
                if add_rule.source_condition == 'objectgroup':
                    if util.isNotEmpty(add_rule.source_object_group):
                        object_group_def(add_rule.source_object_group, device, sdata)
                        add_access_rule_obj.source_obj_name = add_rule.source_object_group
                        #name_rule += ' ' + 'object-group' + ' ' + source_object_group
                        add_name_rule.append('object-group')
                        add_name_rule.append(add_rule.source_object_group)
                if add_rule.source_condition == 'any':
                    #name_rule += ' ' + 'any'
                    add_name_rule.append('any')
                if hasattr(add_rule, 'source_port') and util.isNotEmpty(add_rule.source_port):
                        if util.isEmpty(add_rule.source_port_operator):
                            raise Exception("Please provide Source Port Operator in acl")
                        add_access_rule_obj.source_port_operator = add_rule.source_port_operator
                        each_port = add_rule.source_port.split(' ')
                        if add_rule.protocol == 'tcp':
                            each_port = ([port_dict[each] if each in port_dict else each for each in each_port])
                        elif add_rule.protocol == 'udp':
                            each_port = ([udp_port_dict[each] if each in udp_port_dict else each for each in each_port])
                        source_port = ' '.join(each_port)
                        add_access_rule_obj.source_port = source_port
                        #name_rule += ' ' + source_port_operator + ' ' + source_port
                        add_name_rule.append(add_rule.source_port_operator)
                        add_name_rule.append(source_port)
                if hasattr(add_rule, 'destination_condition') and util.isNotEmpty(add_rule.destination_condition):
                    add_access_rule_obj.dest_condition_type = add_rule.destination_condition
                    if add_rule.destination_condition == 'cidr':
                        cidr_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])' + '/(([0-9])|([1-2][0-9])|(3[0-2]))$';
                        if re.match(cidr_pattern,add_rule.destination_object) == None:
                            raise Exception ("Please provide valid CIDR for destination-object in access-list")
                        prefix = util.IPPrefix(add_rule.destination_object)
                        ip_address = prefix.address
                        netmask = prefix.wildcard
                        add_access_rule_obj.dest_mask = netmask
                        (addrStr, cidrStr) = add_rule.destination_object.split('/')
                        addr = addrStr.split('.')
                        cidr = int(cidrStr)
                        mask = [0, 0, 0, 0]
                        for i in range(cidr):
                            mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
                        #net = []
                        #for i in range(4):
                            #net.append(int(addr[i]) & mask[i])
                        net = [int(addr[i]) & mask[i] for i in xrange(4)]

                        network = ".".join(map(str, net))
                        #name_rule += ' ' + network + ' ' + netmask
                        add_name_rule.append(network)
                        add_name_rule.append(netmask)
                        add_access_rule_obj.dest_ip = network
                    if add_rule.destination_condition == 'host':
                        host_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$';
                        if re.match(host_pattern,add_rule.destination_object) == None:
                            raise Exception ("Please provide valid ip-address for destination-object in access-list")
                        add_access_rule_obj.dest_ip = add_rule.destination_object
                        #name_rule += ' ' + 'host' + ' ' + destination_object
                        add_name_rule.append('host')
                        add_name_rule.append(add_rule.destination_object)
                    if add_rule.destination_condition == 'objectgroup':
                        if util.isNotEmpty(add_rule.destination_object_group):
                            object_group_def(add_rule.destination_object_group, device, sdata)
                            add_access_rule_obj.dest_obj_name = destination_object_group
                            #name_rule += ' ' + 'object-group' + ' ' + destination_object_group
                            add_name_rule.append('object-group')
                            add_name_rule.append(add_rule.destination_object_group)
                    if add_rule.destination_condition == 'any':
                        #name_rule += ' ' + 'any'
                        add_name_rule.append('any')
                if hasattr(add_rule, 'port_number') and util.isNotEmpty(add_rule.port_number):
                        if util.isEmpty(add_rule.dest_port_operator):
                            raise Exception("Please provide Destination Port Operator in acl")
                        add_access_rule_obj.dest_port_operator = add_rule.dest_port_operator
                        each_port = add_rule.port_number.split(' ')
                        if add_rule.protocol == 'tcp':
                            each_port = ([port_dict[each] if each in port_dict else each for each in each_port])
                        elif add_rule.protocol == 'udp':
                            each_port = ([udp_port_dict[each] if each in udp_port_dict else each for each in each_port])
                        port_number = ' '.join(each_port)
                        add_access_rule_obj.dest_port = port_number
                        #name_rule += ' ' + dest_port_operator + ' ' + port_number
                        add_name_rule.append(add_rule.dest_port_operator)
                        add_name_rule.append(port_number)
                if hasattr(add_rule, 'match_packets') and util.isNotEmpty(add_rule.match_packets):
                    add_access_rule_obj.match_packets = add_rule.match_packets
                    #name_rule += ' ' + match_packets
                    add_name_rule.append(add_rule.match_packets)
                    if add_rule.match_packets == 'precedence':
                        if hasattr(add_rule, 'precedence') and util.isNotEmpty(add_rule.precedence):
                            add_access_rule_obj.precedence = add_rule.precedence
                            #name_rule += ' ' + precedence
                            add_name_rule.append(precedence)
                    else:
                        if hasattr(add_rule, 'dscp') and util.isNotEmpty(add_rule.dscp):
                            add_access_rule_obj.precedence = add_rule.dscp
                            #name_rule += ' ' + dscp
                            add_name_rule.append(add_rule.dscp)
                
                add_access_rule_obj.name = ' '.join(add_name_rule)
                #access_rules_url = device.url + "/access-lists/access-list=%s" %(access_list_name)
                #yang.Sdk.createData(access_rules_url, '<acl-rules/>', sdata.getSession())

                add_access_rule_url = device.url + '/acl:access-lists/access-list=%s/acl-rules' %(access_list_name)
                yang.Sdk.createData(add_access_rule_url, add_access_rule_obj.getxml(filter=True), sdata.getSession(), False)


    else:
        yang.Sdk.append_taskdetail(sdata.getTaskId(), "Access-List " + str(access_list_name) + " not found on device " + str(device.device.id) + ". Skipping this device")


def delete_acl(entity, conf, sdata, **kwargs):
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
    access_list_name = inputdict['access_list_name']
    #acl_name = inputdict['acl_name']
    action = inputdict['action']
    protocol = inputdict['protocol']

    url_device_acl = '/controller:devices/device=%s/acl:access-lists/access-list=%s' %(device.device.id, access_list_name)
    '''
    dev_acl = yang.Sdk.getData(url_device_acl, '', sdata.getTaskId())
    conf_acl = util.parseXmlString(dev_acl)

    device_acl = []
    if hasattr(conf_acl.access_lists, 'access_list'):
        conf_acl.access_lists.access_list = util.convert_to_list(conf_acl.access_lists.access_list)
        #for acl in conf_acl.access_lists.access_list:
            #device_acl.append(acl.name)
        device_acl = [acl.name for acl in conf_acl.access_lists.access_list]
    if access_list_name in device_acl:
    '''
    #dev_acl_rule = []
    
    if yang.Sdk.dataExists(url_device_acl):
        '''
        url_device_acl_rule = '/controller:devices/device=%s/acl:access-lists/access-list=%s' %(device.device.id, access_list_name)
        device_acl_rule = yang.Sdk.getData(url_device_acl_rule, '', sdata.getTaskId())
        conf_acl_rule = util.parseXmlString(device_acl_rule)

        
        if hasattr(conf_acl_rule.access_list, 'acl_rules'):
            if hasattr(conf_acl_rule.access_list.acl_rules, 'acl_rule'):
                conf_acl_rule.access_list.acl_rules.acl_rule = util.convert_to_list(conf_acl_rule.access_list.acl_rules.acl_rule)
                #for rule in conf_acl_rule.access_list.acl_rules.acl_rule:
                    #dev_acl_rule.append(rule.name)
                dev_acl_rule = [rule.name for rule in conf_acl_rule.access_list.acl_rules.acl_rule]
        '''
        name_rule = []
        inputdict = kwargs['inputdict']
        access_list_name = inputdict['access_list_name']
        acl_sequence_num = inputdict['acl_sequence_num']
        action = inputdict['action']
        protocol = inputdict['protocol']
        service_obj_name = inputdict['service_obj_name']
        source_condition = inputdict['source_condition']
        source_object = inputdict['source_object']
        source_object_group = inputdict['source_object_group']
        destination_condition = inputdict['destination_condition']
        destination_object = inputdict['destination_object']
        destination_object_group = inputdict['destination_object_group']
        port_number = inputdict['port_number']
        source_port_operator = inputdict['source_port_operator']
        dest_port_operator = inputdict['dest_port_operator']
        match_packets = inputdict['match_packets']
        precedence = inputdict['precedence']
        dscp = inputdict['dscp']
        source_port = inputdict['source_port']

        access_rule_obj = access_lists.access_list.acl_rules.acl_rule.acl_rule()

        port_dict = { '179': 'bgp', '19': 'chargen', '514': 'cmd', '13': 'daytime', '9': 'discard', '53': 'domain',
                          '3949': 'drip', '7': 'echo', '512': 'exec', '79': 'finger', '21': 'ftp', '20': 'ftp-data',
                          '70': 'gopher', '101': 'hostname', '113': 'ident', '194': 'irc', '543': 'klogin', '544': 'kshell',
                          '513': 'login', '515': 'lpd', '119': 'nntp', '15001': 'onep-plain', '15002': 'onep-tls', '496': 'pim-auto-rp',
                          '109': 'pop2', '110': 'pop3', '25': 'smtp', '111': 'sunrpc', '49': 'tacacs', '517': 'talk', '23': 'telnet',
                          '37': 'time', '540': 'uucp', '43': 'whois', '80': 'www', '135': 'msrpc'
                          }
        udp_port_dict = { '512': 'biff', '68': 'bootpc', '67': 'bootps', '9': 'discard', '195': 'dnsix',
                          '53': 'domain', '7': 'echo', '500': 'isakmp', '434': 'mobile-ip', '42': 'nameserver', '138': 'netbios-dgm',
                          '137': 'netbios-ns', '139': 'netbios-ss', '4500': 'non500-isakmp', '123': 'ntp', '496': 'pim-auto-rp',
                          '520': 'rip', '161': 'snmp', '162': 'snmptrap', '111': 'sunrpc', '514': 'syslog', '49': 'tacacs',
                          '517': 'talk', '69': 'tftp', '37': 'time', '513': 'who', '177': 'xdmcp', '135': 'msrpc'
                          }
        access_rule_obj.action = action
        access_rule_obj.layer4protocol = protocol
        if util.isNotEmpty(acl_sequence_num):
            access_rule_obj.linenumber = acl_sequence_num
            #name_rule = acl_sequence_num + ' ' + action + ' ' + protocol
        if util.isNotEmpty(protocol):
            #name_rule = action + ' ' + protocol
            name_rule.append(action)
            name_rule.append(protocol)
        else:
            #name_rule = action
            name_rule.append(action)
        if util.isNotEmpty(service_obj_name):
            access_rule_obj.service_obj_name = service_obj_name
            #name_rule += ' ' + service_obj_name
            name_rule.append(service_obj_name)
        access_rule_obj.source_condition_type = source_condition
        if source_condition == 'cidr':
            cidr_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])' + '/(([0-9])|([1-2][0-9])|(3[0-2]))$';
            if re.match(cidr_pattern,source_object) == None:
                raise Exception ("Please provide valid CIDR for source-object in access-list")
            prefix = util.IPPrefix(source_object)
            ip_address = prefix.address
            netmask = prefix.wildcard
            access_rule_obj.source_mask = netmask
            (addrStr, cidrStr) = source_object.split('/')
            addr = addrStr.split('.')
            cidr = int(cidrStr)
            mask = [0, 0, 0, 0]
            for i in xrange(cidr):
                mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
            #net = []
            #for i in range(4):
                #net.append(int(addr[i]) & mask[i])
            net = [int(addr[i]) & mask[i] for i in range(4)]
            network = ".".join(map(str, net))
            #name_rule += ' ' + network + ' ' + netmask
            name_rule.append(network)
            name_rule.append(netmask)
            access_rule_obj.source_ip = network
        if source_condition == 'host':
            host_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$';
            if re.match(host_pattern,source_object) == None:
                raise Exception("Please provide valid ip-address for source-object in access-list")
            access_rule_obj.source_ip = source_object
            #name_rule += ' ' + 'host' + ' ' + source_object
            name_rule.append('host')
            name_rule.append(source_object)
        if source_condition == 'objectgroup':
            if source_object_group is not None:
                access_rule_obj.source_obj_name = source_object_group
                #name_rule += ' ' + 'object-group' + ' ' + source_object_group
                name_rule.append('object-group')
                name_rule.append(source_object_group)
        if source_condition == 'any':
            #name_rule += ' ' + 'any'
            name_rule.append('any')
        if util.isNotEmpty(source_port):
                if util.isEmpty(source_port_operator):
                    raise Exception("Please provide Source Port Operator in acl")
                access_rule_obj.source_port_operator = source_port_operator
                each_port = source_port.split(' ')
                if protocol == 'tcp':
                    each_port = ([port_dict[each] if each in port_dict else each for each in each_port])
                elif protocol == 'udp':
                    each_port = ([udp_port_dict[each] if each in udp_port_dict else each for each in each_port])
                source_port = ' '.join(each_port)
                access_rule_obj.source_port = source_port
                #name_rule += ' ' + source_port_operator + ' ' + source_port
                name_rule.append(source_port_operator)
                name_rule.append(source_port)
        access_rule_obj.dest_condition_type = destination_condition
        if destination_condition == 'cidr':
            cidr_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])' + '/(([0-9])|([1-2][0-9])|(3[0-2]))$';
            if re.match(cidr_pattern,destination_object) == None:
                raise Exception ("Please provide valid CIDR for destination-object in access-list")
            prefix = util.IPPrefix(destination_object)
            ip_address = prefix.address
            netmask = prefix.wildcard
            access_rule_obj.dest_mask = netmask
            (addrStr, cidrStr) = destination_object.split('/')
            addr = addrStr.split('.')
            cidr = int(cidrStr)
            mask = [0, 0, 0, 0]
            for i in xrange(cidr):
                mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
            #net = []
            #for i in range(4):
                #net.append(int(addr[i]) & mask[i])
            net = [int(addr[i]) & mask[i] for i in xrange(4)]

            network = ".".join(map(str, net))
            #name_rule += ' ' + network + ' ' + netmask
            name_rule.append(network)
            name_rule.append(netmask)
            access_rule_obj.dest_ip = network
        if destination_condition == 'host':
            host_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$';
            if re.match(host_pattern,destination_object) == None:
                raise Exception ("Please provide valid ip-address for destination-object in access-list")
            access_rule_obj.dest_ip = destination_object
            #name_rule += ' ' + 'host' + ' ' + destination_object
            name_rule.append('host')
            name_rule.append(destination_object)
        if destination_condition == 'objectgroup':
            if destination_object_group is not None:
                access_rule_obj.dest_obj_name = destination_object_group
                #name_rule += ' ' + 'object-group' + ' ' + destination_object_group
                name_rule.append('object-group')
                name_rule.append(destination_object_group)
        if destination_condition == 'any':
            #name_rule += ' ' + 'any'
            name_rule.append('any')
        if util.isNotEmpty(port_number):
                if util.isEmpty(dest_port_operator):
                    raise Exception("Please provide Destination Port Operator in acl")
                access_rule_obj.dest_port_operator = dest_port_operator
                each_port = port_number.split(' ')
                if protocol == 'tcp':
                    each_port = ([port_dict[each] if each in port_dict else each for each in each_port])
                elif protocol == 'udp':
                    each_port = ([udp_port_dict[each] if each in udp_port_dict else each for each in each_port])
                port_number = ' '.join(each_port)
                access_rule_obj.dest_port = port_number
                #name_rule += ' ' + dest_port_operator + ' ' + port_number
                name_rule.append(dest_port_operator)
                name_rule.append(port_number)
        if util.isNotEmpty(match_packets):
            access_rule_obj.match_packets = match_packets
            #name_rule += ' ' + match_packets
            name_rule.append(match_packets)
        if match_packets == 'precedence':
            if util.isNotEmpty(precedence):
                access_rule_obj.precedence = precedence
                #name_rule += ' ' + precedence
                name_rule.append(precedence)
        else:
            if util.isNotEmpty(dscp):
                access_rule_obj.precedence = dscp
                #name_rule += ' ' + dscp
                name_rule.append(dscp)
        name_rule = ' '.join(name_rule)
        access_list_url = '/controller:devices/device=%s/acl:access-lists/access-list=%s/acl-rules/acl-rule=%s' % (device.device.id, access_list_name, name_rule.replace(' ', '%20'))
        if yang.Sdk.dataExists(access_list_url):
            access_rule_obj.name = name_rule
            name_rule = name_rule.replace(' ', '%20')
            access_list_url = '/controller:devices/device=%s/acl:access-lists/access-list=%s/acl-rules/acl-rule=%s' % (device.device.id, access_list_name, name_rule)
            output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+access_list_url+'</rc-path></input>')
            ref = util.parseXmlString(output)
            log("xml_op:%s" %(ref))
            if hasattr(ref.output, 'references'):
                if hasattr(ref.output.references, 'reference'):
                    if hasattr(ref.output.references.reference, 'src_node'):
                        for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                            yang.Sdk.removeReference(each_ref, access_list_url)

            yang.Sdk.deleteData(access_list_url, access_rule_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
        else:
            yang.Sdk.append_taskdetail(sdata.getTaskId(), "Access-List  " + str(access_list_name) + " Rule " + str(name_rule) + " not found on device " + str(device.device.id) + ". Skipping this device")

        uri_add_acl = sdata.getRcPath()
        add_acl_output = yang.Sdk.getData(uri_add_acl, '', sdata.getTaskId())
        add_acl_obj = util.parseXmlString(add_acl_output)

        if hasattr(add_acl_obj.update_access_list, 'additional_acl_entry'):
            add_acl_list = util.convert_to_list(add_acl_obj.update_access_list.additional_acl_entry)

            for add_rule in add_acl_list:
                add_name_rule = []
                add_access_rule_obj = access_lists.access_list.acl_rules.acl_rule.acl_rule()
                port_dict = { '179': 'bgp', '19': 'chargen', '514': 'cmd', '13': 'daytime', '9': 'discard', '53': 'domain',
                                  '3949': 'drip', '7': 'echo', '512': 'exec', '79': 'finger', '21': 'ftp', '20': 'ftp-data',
                                  '70': 'gopher', '101': 'hostname', '113': 'ident', '194': 'irc', '543': 'klogin', '544': 'kshell',
                                  '513': 'login', '515': 'lpd', '119': 'nntp', '15001': 'onep-plain', '15002': 'onep-tls', '496': 'pim-auto-rp',
                                  '109': 'pop2', '110': 'pop3', '25': 'smtp', '111': 'sunrpc', '49': 'tacacs', '517': 'talk', '23': 'telnet',
                                  '37': 'time', '540': 'uucp', '43': 'whois', '80': 'www', '135': 'msrpc'
                                  }
                udp_port_dict = { '512': 'biff', '68': 'bootpc', '67': 'bootps', '9': 'discard', '195': 'dnsix',
                                  '53': 'domain', '7': 'echo', '500': 'isakmp', '434': 'mobile-ip', '42': 'nameserver', '138': 'netbios-dgm',
                                  '137': 'netbios-ns', '139': 'netbios-ss', '4500': 'non500-isakmp', '123': 'ntp', '496': 'pim-auto-rp',
                                  '520': 'rip', '161': 'snmp', '162': 'snmptrap', '111': 'sunrpc', '514': 'syslog', '49': 'tacacs',
                                  '517': 'talk', '69': 'tftp', '37': 'time', '513': 'who', '177': 'xdmcp', '135': 'msrpc'
                                  }
                add_access_rule_obj.action = add_rule.action
                if hasattr(add_rule, 'protocol') and util.isNotEmpty(add_rule.protocol):
                    add_access_rule_obj.layer4protocol = add_rule.protocol
                else:
                    add_access_rule_obj.layer4protocol = None
                if hasattr(add_rule, 'acl_sequence_num') and util.isNotEmpty(add_rule.acl_sequence_num):
                    add_access_rule_obj.linenumber = add_rule.acl_sequence_num
                    #name_rule = acl_sequence_num + ' ' + action + ' ' + protocol
                    #name_rule = action + ' ' + protocol
                if hasattr(add_rule, 'protocol') and util.isNotEmpty(add_rule.protocol):
                    #name_rule = action + ' ' + protocol
                    add_name_rule.append(add_rule.action)
                    add_name_rule.append(add_rule.protocol)
                else:
                    #name_rule = action
                    add_name_rule.append(add_rule.action)
                if hasattr(add_rule, 'service_obj_name') and util.isNotEmpty(add_rule.service_obj_name):
                    object_group_def(add_rule.service_obj_name, device, sdata)
                    add_access_rule_obj.service_obj_name = add_rule.service_obj_name
                    #name_rule += ' ' + service_obj_name
                    add_name_rule.append(add_rule.service_obj_name)
                add_access_rule_obj.source_condition_type = add_rule.source_condition
                if add_rule.source_condition == 'cidr':
                    cidr_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])' + '/(([0-9])|([1-2][0-9])|(3[0-2]))$';
                    if re.match(cidr_pattern,add_rule.source_object) == None:
                        raise Exception ("Please provide valid CIDR for source-object in access-list")
                    prefix = util.IPPrefix(add_rule.source_object)
                    ip_address = prefix.address
                    netmask = prefix.wildcard
                    add_access_rule_obj.source_mask = netmask
                    (addrStr, cidrStr) = add_rule.source_object.split('/')
                    addr = addrStr.split('.')
                    cidr = int(cidrStr)
                    mask = [0, 0, 0, 0]
                    for i in xrange(cidr):
                        mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
                    #net = []
                    #for i in range(4):
                        #net.append(int(addr[i]) & mask[i])
                    net = [int(addr[i]) & mask[i] for i in xrange(4)]

                    network = ".".join(map(str, net))
                    #name_rule += ' ' + network + ' ' + netmask
                    add_name_rule.append(network)
                    add_name_rule.append(netmask)
                    add_access_rule_obj.source_ip = network
                if add_rule.source_condition == 'host':
                    host_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$';
                    if re.match(host_pattern,add_rule.source_object) == None:
                        raise Exception ("Please provide valid ip-address for source-object in access-list")
                    add_access_rule_obj.source_ip = add_rule.source_object
                    #name_rule += ' ' + 'host' + ' ' + source_object
                    add_name_rule.append('host')
                    add_name_rule.append(add_rule.source_object)
                if add_rule.source_condition == 'objectgroup':
                    if util.isNotEmpty(add_rule.source_object_group):
                        object_group_def(add_rule.source_object_group, device, sdata)
                        add_access_rule_obj.source_obj_name = add_rule.source_object_group
                        #name_rule += ' ' + 'object-group' + ' ' + source_object_group
                        add_name_rule.append('object-group')
                        add_name_rule.append(add_rule.source_object_group)
                if add_rule.source_condition == 'any':
                    #name_rule += ' ' + 'any'
                    add_name_rule.append('any')
                if hasattr(add_rule, 'source_port') and util.isNotEmpty(add_rule.source_port):
                        if util.isEmpty(add_rule.source_port_operator):
                            raise Exception("Please provide Source Port Operator in acl")
                        add_access_rule_obj.source_port_operator = add_rule.source_port_operator
                        each_port = add_rule.source_port.split(' ')
                        if add_rule.protocol == 'tcp':
                            each_port = ([port_dict[each] if each in port_dict else each for each in each_port])
                        elif add_rule.protocol == 'udp':
                            each_port = ([udp_port_dict[each] if each in udp_port_dict else each for each in each_port])
                        source_port = ' '.join(each_port)
                        add_access_rule_obj.source_port = source_port
                        #name_rule += ' ' + source_port_operator + ' ' + source_port
                        add_name_rule.append(add_rule.source_port_operator)
                        add_name_rule.append(source_port)
                if hasattr(add_rule, 'destination_condition') and util.isNotEmpty(add_rule.destination_condition):
                    add_access_rule_obj.dest_condition_type = add_rule.destination_condition
                    if add_rule.destination_condition == 'cidr':
                        cidr_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])' + '/(([0-9])|([1-2][0-9])|(3[0-2]))$';
                        if re.match(cidr_pattern,add_rule.destination_object) == None:
                            raise Exception ("Please provide valid CIDR for destination-object in access-list")
                        prefix = util.IPPrefix(add_rule.destination_object)
                        ip_address = prefix.address
                        netmask = prefix.wildcard
                        add_access_rule_obj.dest_mask = netmask
                        (addrStr, cidrStr) = add_rule.destination_object.split('/')
                        addr = addrStr.split('.')
                        cidr = int(cidrStr)
                        mask = [0, 0, 0, 0]
                        for i in range(cidr):
                            mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
                        #net = []
                        #for i in range(4):
                            #net.append(int(addr[i]) & mask[i])
                        net = [int(addr[i]) & mask[i] for i in xrange(4)]

                        network = ".".join(map(str, net))
                        #name_rule += ' ' + network + ' ' + netmask
                        add_name_rule.append(network)
                        add_name_rule.append(netmask)
                        add_access_rule_obj.dest_ip = network
                    if add_rule.destination_condition == 'host':
                        host_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$';
                        if re.match(host_pattern,add_rule.destination_object) == None:
                            raise Exception ("Please provide valid ip-address for destination-object in access-list")
                        add_access_rule_obj.dest_ip = add_rule.destination_object
                        #name_rule += ' ' + 'host' + ' ' + destination_object
                        add_name_rule.append('host')
                        add_name_rule.append(add_rule.destination_object)
                    if add_rule.destination_condition == 'objectgroup':
                        if util.isNotEmpty(add_rule.destination_object_group):
                            object_group_def(add_rule.destination_object_group, device, sdata)
                            add_access_rule_obj.dest_obj_name = destination_object_group
                            #name_rule += ' ' + 'object-group' + ' ' + destination_object_group
                            add_name_rule.append('object-group')
                            add_name_rule.append(add_rule.destination_object_group)
                    if add_rule.destination_condition == 'any':
                        #name_rule += ' ' + 'any'
                        add_name_rule.append('any')
                if hasattr(add_rule, 'port_number') and util.isNotEmpty(add_rule.port_number):
                        if util.isEmpty(add_rule.dest_port_operator):
                            raise Exception("Please provide Destination Port Operator in acl")
                        add_access_rule_obj.dest_port_operator = add_rule.dest_port_operator
                        each_port = add_rule.port_number.split(' ')
                        if add_rule.protocol == 'tcp':
                            each_port = ([port_dict[each] if each in port_dict else each for each in each_port])
                        elif add_rule.protocol == 'udp':
                            each_port = ([udp_port_dict[each] if each in udp_port_dict else each for each in each_port])
                        port_number = ' '.join(each_port)
                        add_access_rule_obj.dest_port = port_number
                        #name_rule += ' ' + dest_port_operator + ' ' + port_number
                        add_name_rule.append(add_rule.dest_port_operator)
                        add_name_rule.append(port_number)
                if hasattr(add_rule, 'match_packets') and util.isNotEmpty(add_rule.match_packets):
                    add_access_rule_obj.match_packets = add_rule.match_packets
                    #name_rule += ' ' + match_packets
                    add_name_rule.append(add_rule.match_packets)
                    if add_rule.match_packets == 'precedence':
                        if hasattr(add_rule, 'precedence') and util.isNotEmpty(add_rule.precedence):
                            add_access_rule_obj.precedence = add_rule.precedence
                            #name_rule += ' ' + precedence
                            add_name_rule.append(precedence)
                    else:
                        if hasattr(add_rule, 'dscp') and util.isNotEmpty(add_rule.dscp):
                            add_access_rule_obj.precedence = add_rule.dscp
                            #name_rule += ' ' + dscp
                            add_name_rule.append(add_rule.dscp)
                
                add_name_rule = ' '.join(add_name_rule)
                #access_rules_url = device.url + "/access-lists/access-list=%s" %(access_list_name)
                #yang.Sdk.createData(access_rules_url, '<acl-rules/>', sdata.getSession())

                add_access_list_url = '/controller:devices/device=%s/acl:access-lists/access-list=%s/acl-rules/acl-rule=%s' % (device.device.id, access_list_name, add_name_rule.replace(' ', '%20'))

                if yang.Sdk.dataExists(add_access_list_url):
                    add_access_rule_obj.name = add_name_rule
                    add_name_rule = add_name_rule.replace(' ', '%20')
                    add_access_list_url = '/controller:devices/device=%s/acl:access-lists/access-list=%s/acl-rules/acl-rule=%s' % (device.device.id, access_list_name, add_name_rule)
                    output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+add_access_list_url+'</rc-path></input>')
                    ref = util.parseXmlString(output)
                    log("xml_op:%s" %(ref))
                    if hasattr(ref.output, 'references'):
                        if hasattr(ref.output.references, 'reference'):
                            if hasattr(ref.output.references.reference, 'src_node'):
                                for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                                    yang.Sdk.removeReference(each_ref, add_access_list_url)

                    yang.Sdk.deleteData(add_access_list_url, add_access_rule_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
                else:
                    yang.Sdk.append_taskdetail(sdata.getTaskId(), "Access-List  " + str(access_list_name) + " Rule " + str(add_name_rule) + " not found on device " + str(device.device.id) + ". Skipping this device")

    else:
       yang.Sdk.append_taskdetail(sdata.getTaskId(), "Access-List " + str(access_list_name) + " not found on device " + str(device.device.id) + ". Skipping this device")


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
