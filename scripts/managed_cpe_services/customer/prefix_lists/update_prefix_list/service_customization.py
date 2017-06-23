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
                                    prefix-lists
                                                |
                                                update-prefix-list
                                                                  
Schema Representation:

/services/managed-cpe-services/customer/prefix-lists/update-prefix-list
"""
"""
Names of Leafs for this Yang Entity
                  id
    prefix-list-name
           operation
         prefix-name
            rule-num
         ipv4-prefix
           condition
exact-matching-prefix-length
minimum-matching-prefix-length
maximum-matching-prefix-length
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
            inputkeydict = kwargs['inputkeydict']
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
                            if inputdict['operation'] == 'DELETE':
                                delete_prefix(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_prefix(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        if inputdict['operation'] == 'DELETE':
                            delete_prefix(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_prefix(entity, conf, sdata, **kwargs)

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
                            if inputdict['operation'] == 'DELETE':
                                delete_prefix(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_prefix(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary'
                            if inputdict['operation'] == 'DELETE':
                                delete_prefix(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_prefix(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary'
                        if inputdict['operation'] == 'DELETE':
                            delete_prefix(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_prefix(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary'
                        if inputdict['operation'] == 'DELETE':
                            delete_prefix(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_prefix(entity, conf, sdata, **kwargs)

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
                            if inputdict['operation'] == 'DELETE':
                                delete_prefix(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_prefix(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        if inputdict['operation'] == 'DELETE':
                            delete_prefix(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_prefix(entity, conf, sdata, **kwargs)

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
                            if inputdict['operation'] == 'DELETE':
                                delete_prefix(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_prefix(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_triple'
                            if inputdict['operation'] == 'DELETE':
                                delete_prefix(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_prefix(entity, conf, sdata, **kwargs)
                            entity = 'cpe_tertiary_triple'
                            if inputdict['operation'] == 'DELETE':
                                delete_prefix(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_prefix(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['triple_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_triple'
                        if inputdict['operation'] == 'DELETE':
                            delete_prefix(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_prefix(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_triple'
                        if inputdict['operation'] == 'DELETE':
                            delete_prefix(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_prefix(entity, conf, sdata, **kwargs)
                        entity = 'cpe_tertiary_triple'
                        if inputdict['operation'] == 'DELETE':
                            delete_prefix(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_prefix(entity, conf, sdata, **kwargs)

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
                            if inputdict['operation'] == 'DELETE':
                                delete_prefix(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_prefix(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_dual'
                            if inputdict['operation'] == 'DELETE':
                                delete_prefix(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_prefix(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_dual'
                        if inputdict['operation'] == 'DELETE':
                            delete_prefix(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_prefix(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_dual'
                        if inputdict['operation'] == 'DELETE':
                            delete_prefix(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_prefix(entity, conf, sdata, **kwargs)

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


def delete_prefix(entity, conf, sdata, **kwargs):
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
    prefix_list_name = inputdict['prefix_list_name']
    rule_num = inputdict['rule_num']

    url_device_prefix = '/controller:devices/device=%s/l3features:ip-prefixlist-list' %(device.device.id)
    device_prefix = yang.Sdk.getData(url_device_prefix, '', sdata.getTaskId())
    conf_prefix = util.parseXmlString(device_prefix)

    device_pre = []
    if hasattr(conf_prefix.ip_prefixlist_list, 'ip_prefixlist'):
        conf_prefix.ip_prefixlist_list.ip_prefixlist = util.convert_to_list(conf_prefix.ip_prefixlist_list.ip_prefixlist)
        for pre in conf_prefix.ip_prefixlist_list.ip_prefixlist:
            device_pre.append(pre.name)

    if prefix_list_name in device_pre:
        url_device_prefix_entry = '/controller:devices/device=%s/l3features:ip-prefixlist-list/ip-prefixlist=%s' %(device.device.id, prefix_list_name)
        device_prefix_entry = yang.Sdk.getData(url_device_prefix_entry, '', sdata.getTaskId())
        conf_prefix_entry = util.parseXmlString(device_prefix_entry)
        device_pre_entry = []
        if hasattr(conf_prefix_entry.ip_prefixlist, 'ip_prefixlist_entries'):
            if hasattr(conf_prefix_entry.ip_prefixlist.ip_prefixlist_entries, 'ip_prefixlist_entry'):
                conf_prefix_entry.ip_prefixlist.ip_prefixlist_entries.ip_prefixlist_entry = util.convert_to_list(conf_prefix_entry.ip_prefixlist.ip_prefixlist_entries.ip_prefixlist_entry)
                for entry in conf_prefix_entry.ip_prefixlist.ip_prefixlist_entries.ip_prefixlist_entry:
                    device_pre_entry.append(entry.rule_num)

        if rule_num in device_pre_entry:
            prefix_obj = devices.device.ip_prefixlist_list.ip_prefixlist.ip_prefixlist_entries.ip_prefixlist_entry.ip_prefixlist_entry()
            prefix_obj.rule_num = rule_num
            prefix_list_url = '/controller:devices/device=%s/l3features:ip-prefixlist-list/ip-prefixlist=%s/ip-prefixlist-entries/ip-prefixlist-entry=%s' % (device.device.id, prefix_list_name, rule_num)
            output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+prefix_list_url+'</rc-path></input>')
            ref = util.parseXmlString(output)
            log("xml_op:%s" %(ref))
            if hasattr(ref.output, 'references'):
                if hasattr(ref.output.references, 'reference'):
                    if hasattr(ref.output.references.reference, 'src_node'):
                        for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                            yang.Sdk.removeReference(each_ref, prefix_list_url)

            yang.Sdk.deleteData(prefix_list_url, prefix_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
        else:
            print "Prefix list with seq num is not in device: ", device
    else:
        print "Prefix list is not in device: ", device


def create_prefix(entity, conf, sdata, **kwargs):
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
    prefix_list_name = inputdict['prefix_list_name']
    rule_num = inputdict['rule_num']
    ipv4_prefix = inputdict['ipv4_prefix']
    prefix_name = inputdict['prefix_name']
    condition = inputdict['condition']
    exact_matching_prefix_length = inputdict['exact_matching_prefix_length']
    minimum_matching_prefix_length = inputdict['minimum_matching_prefix_length']
    maximum_matching_prefix_length = inputdict['maximum_matching_prefix_length']

    url_device_prefix = '/controller:devices/device=%s/l3features:ip-prefixlist-list' %(device.device.id)
    device_prefix = yang.Sdk.getData(url_device_prefix, '', sdata.getTaskId())
    conf_prefix = util.parseXmlString(device_prefix)

    device_pre = []
    if hasattr(conf_prefix.ip_prefixlist_list, 'ip_prefixlist'):
        conf_prefix.ip_prefixlist_list.ip_prefixlist = util.convert_to_list(conf_prefix.ip_prefixlist_list.ip_prefixlist)
        for pre in conf_prefix.ip_prefixlist_list.ip_prefixlist:
            device_pre.append(pre.name)

    if prefix_list_name in device_pre:
        prefix_obj = devices.device.ip_prefixlist_list.ip_prefixlist.ip_prefixlist_entries.ip_prefixlist_entry.ip_prefixlist_entry()
        if util.isNotEmpty(prefix_name):
            prefix_obj.prefix_name = prefix_name
        if util.isNotEmpty(rule_num):
            prefix_obj.rule_num = rule_num
        if util.isNotEmpty(ipv4_prefix):
            prefix_obj.subnet = ipv4_prefix
        if util.isNotEmpty(condition):
            prefix_obj.condition = condition
        if util.isNotEmpty(exact_matching_prefix_length):
            prefix_obj.num = exact_matching_prefix_length
        if util.isNotEmpty(minimum_matching_prefix_length):
            prefix_obj.num = minimum_matching_prefix_length
            prefix_obj.compare = 'ge'
        if util.isNotEmpty(maximum_matching_prefix_length):
            prefix_obj.num = maximum_matching_prefix_length
            prefix_obj.compare = 'le'
        device.addIpPrefixListEntriesContainer(prefix_list_name, sdata.getSession())

        prefix_list_url = device.url + '/ip-prefixlist-list/ip-prefixlist=%s/ip-prefixlist-entries' % (prefix_list_name)
        yang.Sdk.createData(prefix_list_url, prefix_obj.getxml(filter=True), sdata.getSession(), False)
    else:
        print "Prefix list is not in device: ", device


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
