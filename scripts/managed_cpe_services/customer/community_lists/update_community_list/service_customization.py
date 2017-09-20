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
                                    community-lists
                                                   |
                                                   update-community-list
                                                                        
Schema Representation:

/services/managed-cpe-services/customer/community-lists/update-community-list
"""
"""
Names of Leafs for this Yang Entity
                  id
 community-list-name
           operation
community-list-entry
           condition
               value
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
from servicemodel.controller.devices.device import extcommunity_lists
from servicemodel.controller.devices.device import community_lists

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log
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
                                delete_community(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_community(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        if inputdict['operation'] == 'DELETE':
                            delete_community(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_community(entity, conf, sdata, **kwargs)

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
                                delete_community(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_community(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary'
                            if inputdict['operation'] == 'DELETE':
                                delete_community(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_community(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary'
                        if inputdict['operation'] == 'DELETE':
                            delete_community(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_community(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary'
                        if inputdict['operation'] == 'DELETE':
                            delete_community(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_community(entity, conf, sdata, **kwargs)

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
                                delete_community(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_community(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        if inputdict['operation'] == 'DELETE':
                            delete_community(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_community(entity, conf, sdata, **kwargs)

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
                                delete_community(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_community(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_triple'
                            if inputdict['operation'] == 'DELETE':
                                delete_community(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_community(entity, conf, sdata, **kwargs)
                            entity = 'cpe_tertiary_triple'
                            if inputdict['operation'] == 'DELETE':
                                delete_community(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_community(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['triple_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_triple'
                        if inputdict['operation'] == 'DELETE':
                            delete_community(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_community(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_triple'
                        if inputdict['operation'] == 'DELETE':
                            delete_community(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_community(entity, conf, sdata, **kwargs)
                        entity = 'cpe_tertiary_triple'
                        if inputdict['operation'] == 'DELETE':
                            delete_community(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_community(entity, conf, sdata, **kwargs)

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
                                delete_community(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_community(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_dual'
                            if inputdict['operation'] == 'DELETE':
                                delete_community(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_community(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_dual'
                        if inputdict['operation'] == 'DELETE':
                            delete_community(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_community(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_dual'
                        if inputdict['operation'] == 'DELETE':
                            delete_community(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_community(entity, conf, sdata, **kwargs)

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


def delete_community(entity, conf, sdata, **kwargs):
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
    community_list_name = inputdict['community_list_name']
    value = inputdict['value']
    extcommunity = inputdict['extcommunity']
    if extcommunity == 'true':
        url_device_community = '/controller:devices/device=%s/l3features:extcommunity-lists' %(device.device.id)
        try:
            device_community = yang.Sdk.getData(url_device_community, '', sdata.getTaskId())
            conf_community = util.parseXmlString(device_community)

            device_com = []
            if hasattr(conf_community.extcommunity_lists, 'extcommunity_list'):
                conf_community.extcommunity_lists.extcommunity_list = util.convert_to_list(conf_community.extcommunity_lists.extcommunity_list)
                for com in conf_community.extcommunity_lists.extcommunity_list:
                    if com.extcommunity_list_name == community_list_name and com.value == value:
                        device_com.append(com.extcommunity_list_name)

            if community_list_name in device_com:
                community_obj = extcommunity_lists.extcommunity_list.extcommunity_list()
                community_obj.extcommunity_list_name = community_list_name
                community_obj.value = value
                value = value.replace(':', '%3A')
                com_url = "/controller:devices/device=%s/l3features:extcommunity-lists/extcommunity-list=%s,%s" %(device.device.id, community_list_name, value)
                output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+com_url+'</rc-path></input>')
                ref = util.parseXmlString(output)
                log("xml_op:%s" %(ref))
                if hasattr(ref.output, 'references'):
                    if hasattr(ref.output.references, 'reference'):
                        if hasattr(ref.output.references.reference, 'src_node'):
                            for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                                yang.Sdk.removeReference(each_ref, com_url)

                yang.Sdk.deleteData(device.url+"/l3features:extcommunity-lists/extcommunity-list=%s,%s" %(community_list_name, value), community_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
            else:
                print "Extcommunity list or with specified value is not in device: ", device
        except DataNodeNotFoundException:
            print "Extcommunity lists container is not in device: ", device
    else:
        url_device_community = '/controller:devices/device=%s/l3features:community-lists' %(device.device.id)
        try:
            device_community = yang.Sdk.getData(url_device_community, '', sdata.getTaskId())
            conf_community = util.parseXmlString(device_community)

            device_com = []
            if hasattr(conf_community.community_lists, 'community_list'):
                conf_community.community_lists.community_list = util.convert_to_list(conf_community.community_lists.community_list)
                for com in conf_community.community_lists.community_list:
                    if com.community_list_name == community_list_name and com.value == value:
                        device_com.append(com.community_list_name)

            if community_list_name in device_com:
                community_obj = community_lists.community_list.community_list()
                community_obj.community_list_name = community_list_name
                community_obj.value = value
                value = value.replace(':', '%3A')
                com_url = "/controller:devices/device=%s/l3features:community-lists/community-list=%s,%s" %(device.device.id, community_list_name, value)
                output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+com_url+'</rc-path></input>')
                ref = util.parseXmlString(output)
                log("xml_op:%s" %(ref))
                if hasattr(ref.output, 'references'):
                    if hasattr(ref.output.references, 'reference'):
                        if hasattr(ref.output.references.reference, 'src_node'):
                            for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                                yang.Sdk.removeReference(each_ref, com_url)

                yang.Sdk.deleteData(device.url+"/l3features:community-lists/community-list=%s,%s" %(community_list_name, value), community_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
            else:
                print "Community list or with specified value is not in device: ", device
        except DataNodeNotFoundException:
            print "community lists container is not in device: ", device


def create_community(entity, conf, sdata, **kwargs):
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
    community_list_name = inputdict['community_list_name']
    value = inputdict['value']
    community_list_entry = inputdict['community_list_entry']
    condition = inputdict['condition']

    extcommunity = inputdict['extcommunity']
    extcomm = inputdict['extcomm']
    if extcommunity == 'true':
        url_device_community = '/controller:devices/device=%s/l3features:extcommunity-lists' %(device.device.id)
        try:
            device_community = yang.Sdk.getData(url_device_community, '', sdata.getTaskId())
            conf_community = util.parseXmlString(device_community)
            device_com = []
            if hasattr(conf_community.extcommunity_lists, 'extcommunity_list'):
                conf_community.extcommunity_lists.extcommunity_list = util.convert_to_list(conf_community.extcommunity_lists.extcommunity_list)
                for com in conf_community.extcommunity_lists.extcommunity_list:
                    device_com.append(com.extcommunity_list_name)

            if community_list_name in device_com:
                community_list_obj = extcommunity_lists.extcommunity_list.extcommunity_list()
                if util.isNotEmpty(community_list_entry):
                    community_list_obj.extcommunity_list_entry = community_list_entry
                if util.isNotEmpty(community_list_name):
                    community_list_obj.extcommunity_list_name = community_list_name
                if util.isNotEmpty(condition):
                    community_list_obj.condition = condition
                if util.isNotEmpty(extcomm):
                    community_list_obj.extcomm = extcomm
                if util.isNotEmpty(value):
                    community_list_obj.value = value
                community_list_url = device.url + '/extcommunity-lists'
                yang.Sdk.createData(community_list_url, community_list_obj.getxml(filter=True), sdata.getSession(), False)
            else:
                print "Extcommunity list is not in device: ", device
        except DataNodeNotFoundException:
            print "Extcommunity lists container is not in device: ", device
    else:
        url_device_community = '/controller:devices/device=%s/l3features:community-lists' %(device.device.id)
        try:
            device_community = yang.Sdk.getData(url_device_community, '', sdata.getTaskId())
            conf_community = util.parseXmlString(device_community)
            device_com = []
            if hasattr(conf_community.community_lists, 'community_list'):
                conf_community.community_lists.community_list = util.convert_to_list(conf_community.community_lists.community_list)
                for com in conf_community.community_lists.community_list:
                    device_com.append(com.community_list_name)

            if community_list_name in device_com:
                community_list_obj = community_lists.community_list.community_list()
                if util.isNotEmpty(community_list_entry):
                    community_list_obj.community_list_entry = community_list_entry
                if util.isNotEmpty(community_list_name):
                    community_list_obj.community_list_name = community_list_name
                if util.isNotEmpty(condition):
                    community_list_obj.condition = condition
                if util.isNotEmpty(value):
                    community_list_obj.value = value
                community_list_url = device.url + '/community-lists'
                yang.Sdk.createData(community_list_url, community_list_obj.getxml(filter=True), sdata.getSession(), False)
            else:
                print "Community list is not in device: ", device
        except DataNodeNotFoundException:
            print "community lists container is not in device: ", device


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
