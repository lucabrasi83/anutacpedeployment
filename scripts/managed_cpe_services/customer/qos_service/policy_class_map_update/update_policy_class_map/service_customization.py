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
                                               policy-class-map-update
                                                                      |
                                                                      update-policy-class-map
                                                                                             
Schema Representation:

/services/managed-cpe-services/customer/qos-service/policy-class-map-update/update-policy-class-map
"""
"""
Names of Leafs for this Yang Entity
                name
         policy-name
               class
     packet-handling
          percentage
         queue-limit
             packets
           qos-group
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
from servicemodel.controller.devices.device import policy_maps

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
                            update_percentage(site, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        update_percentage(site, sdata, **kwargs)
            if inputdict['dual_cpe_site'] == "true":
                if len(inputdict['dual_cpe_sites']) > 0:
                    if isinstance(inputdict['dual_cpe_sites'], list) is True:
                        for site in inputdict['dual_cpe_sites']:
                            update_percentage_dual(site, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        update_percentage_dual(site, sdata, **kwargs)
            if inputdict['single_cpe_dual_wan_site'] == "true":
                if len(inputdict['single_cpe_dual_wan_sites']) > 0:
                    if isinstance(inputdict['single_cpe_dual_wan_sites'], list) is True:
                        for site in inputdict['single_cpe_dual_wan_sites']:
                            update_percentage_single_dual(site, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        update_percentage_single_dual(site, sdata, **kwargs)
            if inputdict['triple_cpe_site'] == "true":
                if len(inputdict['triple_cpe_sites']) > 0:
                    if isinstance(inputdict['triple_cpe_sites'], list) is True:
                        for site in inputdict['triple_cpe_sites']:
                            update_percentage_triple(site, sdata, **kwargs)
                    else:
                        site = inputdict['triple_cpe_sites']
                        update_percentage_triple(site, sdata, **kwargs)
            if inputdict['dual_cpe_dual_wan_site'] == "true":
                if len(inputdict['dual_cpe_dual_wan_sites']) > 0:
                    if isinstance(inputdict['dual_cpe_dual_wan_sites'], list) is True:
                        for site in inputdict['dual_cpe_dual_wan_sites']:
                            update_percentage_dual_dual(site, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        update_percentage_dual_dual(site, sdata, **kwargs)

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
      raise Exception('Update forbidden for node update-policy-class-map at path managed-cpe-services/customer/qos-service/policy-class-map-update/update-policy-class-map')
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


def update_percentage(site, sdata, **kwargs):
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
    conf = util.parseXmlString(site_output)
    device = devicemgr.getDeviceById(conf.single_cpe_site_services.cpe.device_ip)

    # xml_output = yang.Sdk.getData(url+"/qos-service/policies/policy="+str(policy_name), '',sdata.getTaskId())
    # obj = util.parseXmlString(xml_output)
    # print "obj: ",obj
    # print "xml of policy map obj: ",obj.toXml()
    # policy_name = obj.policy.name
    # print "policy_name is:",policy_name
    inputdict = kwargs['inputdict']
    policy_name = inputdict['policy_name']
    class_name = inputdict['class1']
    packet_handling = inputdict['packet_handling']
    percentage = inputdict['percentage']
    queue_limit = inputdict['queue_limit']
    packets = inputdict['packets']
    qos_group = inputdict['qos_group']

    map_obj = policy_maps.policy_map.policy_map()
    map_obj.name = policy_name
    policy_name_exist = None
    if hasattr(conf.single_cpe_site_services.cpe_wan, 'child_qos_policy'):
        policy_name_exist = conf.single_cpe_site_services.cpe_wan.child_qos_policy
    if hasattr(conf.single_cpe_site_services.cpe_wan, 'outbound_policer'):
        policy_name_exist = conf.single_cpe_site_services.cpe_wan.outbound_policer
        print "policy_name_exist is:",policy_name_exist
    if policy_name_exist == policy_name:
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)

        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
    else:
        print "Check policy name in cpe_wan: ", site


def update_percentage_dual(site, sdata, **kwargs):
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '',sdata.getTaskId())
    conf = util.parseXmlString(site_output)
    # xml_output = yang.Sdk.getData(url+"/qos-service/policies/policy="+str(policy_name), '',sdata.getTaskId())
    # obj = util.parseXmlString(xml_output)
    # print "obj: ",obj
    # print "xml of policy map obj: ",obj.toXml()
    inputdict = kwargs['inputdict']
    policy_name = inputdict['policy_name']
    class_name = inputdict['class1']
    packet_handling = inputdict['packet_handling']
    percentage = inputdict['percentage']
    queue_limit = inputdict['queue_limit']
    packets = inputdict['packets']
    qos_group = inputdict['qos_group']

    map_obj = policy_maps.policy_map.policy_map()
    map_obj.name = policy_name
    policy_name_exist = None
    if hasattr(conf.dual_cpe_site_services.cpe_primary_wan, 'child_qos_policy'):
        policy_name_exist = conf.dual_cpe_site_services.cpe_primary_wan.child_qos_policy
    if hasattr(conf.dual_cpe_site_services.cpe_primary_wan, 'outbound_policer'):
        policy_name_exist = conf.dual_cpe_site_services.cpe_primary_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_primary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
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
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
    else:
        print "Policy is not in cpe secondary: ", site


def update_percentage_single_dual(site, sdata, **kwargs):
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '',sdata.getTaskId())
    conf = util.parseXmlString(site_output)

    # xml_output = yang.Sdk.getData(url+"/qos-service/policies/policy="+str(policy_name), '',sdata.getTaskId())
    # obj = util.parseXmlString(xml_output)
    # print "obj: ",obj
    # print "xml of policy map obj: ",obj.toXml()
    # policy_name = obj.policy.name
    # map_obj = policy_maps.policy_map.policy_map()
    # map_obj.name = policy_name
    inputdict = kwargs['inputdict']
    policy_name = inputdict['policy_name']
    class_name = inputdict['class1']
    packet_handling = inputdict['packet_handling']
    percentage = inputdict['percentage']
    queue_limit = inputdict['queue_limit']
    packets = inputdict['packets']
    qos_group = inputdict['qos_group']
    map_obj = policy_maps.policy_map.policy_map()
    map_obj.name = policy_name
    policy_name_exist = None
    if hasattr(conf.single_cpe_dual_wan_site_services.cpe_primary_wan, 'child_qos_policy'):
        policy_name_exist = conf.single_cpe_dual_wan_site_services.cpe_primary_wan.child_qos_policy
    if hasattr(conf.single_cpe_dual_wan_site_services.cpe_primary_wan, 'outbound_policer'):
        policy_name_exist = conf.single_cpe_dual_wan_site_services.cpe_primary_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.single_cpe_dual_wan_site_services.cpe.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
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
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
    else:
        print "Policy is not in cpe: ", site


def update_percentage_dual_dual(site, sdata, **kwargs):
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '',sdata.getTaskId())
    conf = util.parseXmlString(site_output)

    inputdict = kwargs['inputdict']
    policy_name = inputdict['policy_name']
    class_name = inputdict['class1']
    packet_handling = inputdict['packet_handling']
    percentage = inputdict['percentage']
    queue_limit = inputdict['queue_limit']
    packets = inputdict['packets']
    qos_group = inputdict['qos_group']
    map_obj = policy_maps.policy_map.policy_map()
    map_obj.name = policy_name
    policy_name_exist = None
    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary_inet_wan, 'child_qos_policy'):
        policy_name_exist = conf.dual_cpe_dual_wan_site_services.cpe_primary_inet_wan.child_qos_policy
    if hasattr(conf.dual_cpe_dual_wan_site_services.cpe_primary_inet_wan, 'outbound_policer'):
        policy_name_exist = conf.dual_cpe_dual_wan_site_services.cpe_primary_inet_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
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
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
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
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
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
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
    else:
        print "Policy is not in cpe: ", site


def update_percentage_triple(site, sdata, **kwargs):
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
    conf = util.parseXmlString(site_output)

    inputdict = kwargs['inputdict']
    policy_name = inputdict['policy_name']
    class_name = inputdict['class1']
    packet_handling = inputdict['packet_handling']
    percentage = inputdict['percentage']
    queue_limit = inputdict['queue_limit']
    packets = inputdict['packets']
    qos_group = inputdict['qos_group']
    map_obj = policy_maps.policy_map.policy_map()
    map_obj.name = policy_name
    policy_name_exist = None
    if hasattr(conf.triple_cpe_site_services.cpe_primary_inet_wan, 'child_qos_policy'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_primary_inet_wan.child_qos_policy
    if hasattr(conf.triple_cpe_site_services.cpe_primary_inet_wan, 'outbound_policer'):
        policy_name_exist = conf.triple_cpe_site_services.cpe_primary_inet_wan.outbound_policer
    if policy_name_exist == policy_name:
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_primary.device_ip)
        yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
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
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
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
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
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
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
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
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
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
        cls_obj = policy_maps.policy_map.class_entry.class_entry()
        cls_obj.class_name = class_name
        print "packet_handling: ",packet_handling
        if packet_handling is not None:
            if packet_handling == "bandwidth":
                cls_obj.bandwidth_percentage = percentage
            if packet_handling == "priority":
                cls_obj.priority_percentage = percentage
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
        if queue_limit is not None:
            queue_limit_obj = policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,class_name), queue_limit_obj.getxml(filter=True), sdata.getSession(), False)

        if qos_group is not None:
            if util.isNotEmpty(qos_group):
                cls_obj.qos_group = qos_group

            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession(), False)
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
