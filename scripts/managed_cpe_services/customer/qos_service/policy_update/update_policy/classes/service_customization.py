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
                                    qos-service
                                               |
                                               policy-update
                                                            |
                                                            update-policy
                                                                         |
                                                                         classes
                                                                                
Schema Representation:

/services/managed-cpe-services/customer/qos-service/policy-update/update-policy/classes
"""
"""
Names of Leafs for this Yang Entity
               class
          percentage
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
            class_name = inputdict['class1']
            if class_name is None:
                raise Exception('Select class')
            percentage = inputdict['percentage']
            if percentage is None:
                raise Exception('Select percantage')
            obj = getLocalObject(sdata, 'update-policy')
            policy_name = obj.update_policy.policy_name
            packet_handling = obj.update_policy.packet_handling
            if obj.update_policy.single_cpe_site == "true":
                if len(obj.update_policy.single_cpe_sites) > 0:
                    if isinstance(obj.update_policy.single_cpe_sites, list) is True:
                        for site in obj.update_policy.single_cpe_sites:
                            update_percentage(site, policy_name, class_name, packet_handling, percentage, sdata)
                    else:
                        site = obj.update_policy.single_cpe_sites
                        update_percentage(site, policy_name, class_name, packet_handling, percentage, sdata)
            if obj.update_policy.dual_cpe_site == "true":
                if len(obj.update_policy.dual_cpe_sites) > 0:
                    if isinstance(obj.update_policy.dual_cpe_sites, list) is True:
                        for site in obj.update_policy.dual_cpe_sites:
                            update_percentage_dual(site, policy_name, class_name, packet_handling, percentage, sdata)
                    else:
                        site = obj.update_policy.dual_cpe_sites
                        update_percentage_dual(site, policy_name, class_name, packet_handling, percentage, sdata)
            if obj.update_policy.single_cpe_dual_wan_site == "true":
                if len(obj.update_policy.single_cpe_dual_wan_sites) > 0:
                    if isinstance(obj.update_policy.single_cpe_dual_wan_sites, list) is True:
                        for site in obj.update_policy.single_cpe_dual_wan_sites:
                            update_percentage_single_dual(site, policy_name, class_name, packet_handling, percentage, sdata)
                    else:
                        site = obj.update_policy.single_cpe_dual_wan_sites
                        update_percentage_single_dual(site, policy_name, class_name, packet_handling, percentage, sdata)
            if obj.update_policy.triple_cpe_site == "true":
                if len(obj.update_policy.triple_cpe_sites) > 0:
                    if isinstance(obj.update_policy.triple_cpe_sites, list) is True:
                        for site in obj.update_policy.triple_cpe_sites:
                            update_percentage_triple(site, policy_name, class_name, packet_handling, percentage, sdata)
                    else:
                        site = obj.update_policy.triple_cpe_sites
                        update_percentage_triple(site, policy_name, class_name, packet_handling, percentage, sdata)
            if obj.update_policy.dual_cpe_dual_wan_site == "true":
                if len(obj.update_policy.dual_cpe_dual_wan_sites) > 0:
                    if isinstance(obj.update_policy.dual_cpe_dual_wan_sites, list) is True:
                        for site in obj.update_policy.dual_cpe_dual_wan_sites:
                            update_percentage_dual_dual(site, policy_name, class_name, packet_handling, percentage, sdata)
                    else:
                        site = obj.update_policy.dual_cpe_dual_wan_sites
                        update_percentage_dual_dual(site, policy_name, class_name, packet_handling, percentage, sdata)

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
        inputkeydict = kwargs['inputkeydict']
        devbindobjs = kwargs['devbindobjs']

    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      raise Exception('Update forbidden for node classes at path managed-cpe-services/customer/qos-service/policy-update/update-policy/classes')
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


def update_percentage(site, policy_name, class_name, packet_handling_input, percentage_input, sdata):
    percent_pattern = '^([0-9]|[1-9][0-9]|100)$';
    if re.match(percent_pattern,percentage_input) == None:
        raise Exception("Please provide valid percentage, should be between 1-100")

    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
    conf = util.parseXmlString(site_output)
    device = devicemgr.getDeviceById(conf.single_cpe_site_services.cpe.device_ip)

    xml_output = yang.Sdk.getData(url+"/qos-service/policies/policy="+str(policy_name), '',sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    print "obj: ",obj
    print "xml of policy map obj: ",obj.toXml()
    policy_name = obj.policy.name
    print "policy_name is:",policy_name
    map_obj = devices.device.policy_maps.policy_map.policy_map()
    map_obj.name = policy_name
    policy_name_exist = None
    if hasattr(conf.single_cpe_site_services.cpe_wan, 'child_qos_policy'):
        policy_name_exist = conf.single_cpe_site_services.cpe_wan.child_qos_policy
    if hasattr(conf.single_cpe_site_services.cpe_wan, 'outbound_policer'):
        policy_name_exist = conf.single_cpe_site_services.cpe_wan.outbound_policer
        print "policy_name_exist is:",policy_name_exist
    if policy_name_exist == policy_name:
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Check policy name in cpe_wan: ", site


def update_percentage_dual(site, policy_name, class_name, packet_handling_input, percentage_input, sdata):
    percent_pattern = '^([0-9]|[1-9][0-9]|100)$';
    if re.match(percent_pattern,percentage_input) == None:
        raise Exception("Please provide valid percentage, should be between 1-100")

    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '',sdata.getTaskId())
    conf = util.parseXmlString(site_output)
    xml_output = yang.Sdk.getData(url+"/qos-service/policies/policy="+str(policy_name), '',sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    print "obj: ",obj
    print "xml of policy map obj: ",obj.toXml()
    policy_name = obj.policy.name
    map_obj = devices.device.policy_maps.policy_map.policy_map()
    map_obj.name = policy_name
    policy_name_exist = None
    if hasattr(conf.dual_cpe_site_services.cpe_primary_wan, 'child_qos_policy'):
        policy_name_exist = conf.dual_cpe_site_services.cpe_primary_wan.child_qos_policy
    if hasattr(conf.dual_cpe_site_services.cpe_primary_wan, 'outbound_policer'):
        policy_name_exist = conf.dual_cpe_site_services.cpe_primary_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_primary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe primary: ", site
    policy_name_exist = None
    if hasattr(conf.dual_cpe_site_services.cpe_secondary_wan, 'child_qos_policy'):
        policy_name_exist = conf.dual_cpe_site_services.cpe_secondary_wan.child_qos_policy
    if hasattr(conf.dual_cpe_site_services.cpe_secondary_wan, 'outbound_policer'):
        policy_name_exist = conf.dual_cpe_site_services.cpe_secondary_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_secondary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe secondary: ", site


def update_percentage_single_dual(site, policy_name, class_name, packet_handling_input, percentage_input, sdata):
    percent_pattern = '^([0-9]|[1-9][0-9]|100)$';
    if re.match(percent_pattern,percentage_input) == None:
        raise Exception("Please provide valid percentage, should be between 1-100")

    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '',sdata.getTaskId())
    conf = util.parseXmlString(site_output)

    xml_output = yang.Sdk.getData(url+"/qos-service/policies/policy="+str(policy_name), '',sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    print "obj: ",obj
    print "xml of policy map obj: ",obj.toXml()
    policy_name = obj.policy.name
    map_obj = devices.device.policy_maps.policy_map.policy_map()
    map_obj.name = policy_name
    policy_name_exist = None
    if hasattr(conf.single_cpe_dual_wan_site_services.cpe_primary_wan, 'child_qos_policy'):
        policy_name_exist = conf.single_cpe_dual_wan_site_services.cpe_primary_wan.child_qos_policy
    if hasattr(conf.single_cpe_dual_wan_site_services.cpe_primary_wan, 'outbound_policer'):
        policy_name_exist = conf.single_cpe_dual_wan_site_services.cpe_primary_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.single_cpe_dual_wan_site_services.cpe.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe: ", site

    policy_name_exist = None
    if hasattr(conf.single_cpe_dual_wan_site_services.cpe_secondary_wan, 'child_qos_policy'):
        policy_name_exist = conf.single_cpe_dual_wan_site_services.cpe_secondary_wan.child_qos_policy
    if hasattr(conf.single_cpe_dual_wan_site_services.cpe_secondary_wan, 'outbound_policer'):
        policy_name_exist = conf.single_cpe_dual_wan_site_services.cpe_secondary_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.single_cpe_dual_wan_site_services.cpe.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe: ", site


def update_percentage_dual_dual(site, policy_name, class_name, packet_handling_input, percentage_input, sdata):
    percent_pattern = '^([0-9]|[1-9][0-9]|100)$';
    if re.match(percent_pattern,percentage_input) == None:
        raise Exception("Please provide valid percentage, should be between 1-100")

    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '',sdata.getTaskId())
    conf = util.parseXmlString(site_output)

    xml_output = yang.Sdk.getData(url+"/qos-service/policies/policy="+str(policy_name), '',sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    print "obj: ",obj
    print "xml of policy map obj: ",obj.toXml()
    policy_name = obj.policy.name
    map_obj = devices.device.policy_maps.policy_map.policy_map()
    map_obj.name = policy_name
    policy_name_exist = None
    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary_inet_wan, 'child_qos_policy'):
        policy_name_exist = conf.dual_cpe_dual_wan_site_services.cpe_primary_inet_wan.child_qos_policy
    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary_inet_wan, 'outbound_policer'):
        policy_name_exist = conf.dual_cpe_dual_wan_site_services.cpe_primary_inet_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe: ", site

    policy_name_exist = None
    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary_mpls_wan, 'child_qos_policy'):
        policy_name_exist = conf.dual_cpe_dual_wan_site_services.cpe_primary_mpls_wan.child_qos_policy
    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary_mpls_wan, 'outbound_policer'):
        policy_name_exist = conf.dual_cpe_dual_wan_site_services.cpe_primary_mpls_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe: ", site

    policy_name_exist = None
    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary_inet_wan, 'child_qos_policy'):
        policy_name_exist = conf.dual_cpe_dual_wan_site_services.cpe_secondary_inet_wan.child_qos_policy
    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary_inet_wan, 'outbound_policer'):
        policy_name_exist = conf.dual_cpe_dual_wan_site_services.cpe_secondary_inet_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe: ", site

    policy_name_exist = None
    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary_mpls_wan, 'child_qos_policy'):
        policy_name_exist = conf.dual_cpe_dual_wan_site_services.cpe_secondary_mpls_wan.child_qos_policy
    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_secondary_mpls_wan, 'outbound_policer'):
        policy_name_exist = conf.dual_cpe_dual_wan_site_services.cpe_secondary_mpls_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe: ", site


def update_percentage_triple(site, policy_name, class_name, packet_handling_input, percentage_input, sdata):
    percent_pattern = '^([0-9]|[1-9][0-9]|100)$';
    if re.match(percent_pattern,percentage_input) == None:
        raise Exception("Please provide valid percentage, should be between 1-100")

    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
    conf = util.parseXmlString(site_output)

    xml_output = yang.Sdk.getData(url+"/qos-service/policies/policy="+str(policy_name), '',sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    print "obj: ",obj
    print "xml of policy map obj: ",obj.toXml()
    policy_name = obj.policy.name
    map_obj = devices.device.policy_maps.policy_map.policy_map()
    map_obj.name = policy_name
    policy_name_exist = None
    if hasattr(conf.triple_cpe_site_services.cpe_primary_inet_wan, 'child_qos_policy'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_primary_inet_wan.child_qos_policy
    if hasattr(conf.triple_cpe_site_services.cpe_primary_inet_wan, 'outbound_policer'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_primary_inet_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_primary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe: ", site

    policy_name_exist = None
    if hasattr(conf.triple_cpe_site_services.cpe_primary_mpls_wan, 'child_qos_policy'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_primary_mpls_wan.child_qos_policy
    if hasattr(conf.triple_cpe_site_services.cpe_primary_mpls_wan, 'outbound_policer'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_primary_mpls_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_primary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe: ", site

    policy_name_exist = None
    if hasattr(conf.triple_cpe_site_services.cpe_secondary_inet_wan, 'child_qos_policy'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_secondary_inet_wan.child_qos_policy
    if hasattr(conf.triple_cpe_site_services.cpe_secondary_inet_wan, 'outbound_policer'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_secondary_inet_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_secondary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe: ", site

    policy_name_exist = None
    if hasattr(conf.triple_cpe_site_services.cpe_secondary_mpls_wan, 'child_qos_policy'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_secondary_mpls_wan.child_qos_policy
    if hasattr(conf.triple_cpe_site_services.cpe_secondary_mpls_wan, 'outbound_policer'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_secondary_mpls_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_secondary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe: ", site

    policy_name_exist = None
    if hasattr(conf.triple_cpe_site_services.cpe_tertiary_inet_wan, 'child_qos_policy'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_tertiary_inet_wan.child_qos_policy
    if hasattr(conf.triple_cpe_site_services.cpe_tertiary_inet_wan, 'outbound_policer'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_tertiary_inet_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_tertiary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe: ", site

    policy_name_exist = None
    if hasattr(conf.triple_cpe_site_services.cpe_tertiary_mpls_wan, 'child_qos_policy'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_tertiary_mpls_wan.child_qos_policy
    if hasattr(conf.triple_cpe_site_services.cpe_tertiary_mpls_wan, 'outbound_policer'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_tertiary_mpls_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_tertiary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        for cls in obj.policy.classes.get_field_value('class_name', True):
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            cls_name = cls.name
            if cls_name == class_name:
                cls_obj.class_name = cls_name
                packet_handling = cls.get_field_value('packet_handling')
                print "packet_handling: ",packet_handling
                if packet_handling is not None and hasattr(packet_handling, packet_handling_input):
                    if packet_handling_input == "bandwidth":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.bandwidth)
                        cls_obj.bandwidth_percentage = percentage_input
                    if packet_handling_input == "priority":
                        print "Old %s: %s" % (packet_handling_input, packet_handling.priority)
                        cls_obj.priority_percentage = percentage_input
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    print "Check packet handling input: ", site
    else:
        print "Policy is not in cpe: ", site


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
