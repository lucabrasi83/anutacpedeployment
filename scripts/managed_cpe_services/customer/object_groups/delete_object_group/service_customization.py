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
                                    object-groups
                                                |
                                                delete-object-group
                                                                  
Schema Representation:

/services/managed-cpe-services/customer/object-groups/delete-object-group
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
        inputkeydict = kwargs['inputkeydict']

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
                            delete_object_group(entity, conf, sdata, **kwargs)
                            
                    else:
                        site = inputdict['single_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        delete_object_group(entity, conf, sdata, **kwargs)
                        

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
                            delete_object_group(entity, conf, sdata, **kwargs)
                            
                            entity = 'cpe_secondary'
                            delete_object_group(entity, conf, sdata, **kwargs)
                           
                    else:
                        site = inputdict['dual_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary'
                        delete_object_group(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary'
                        delete_object_group(entity, conf, sdata, **kwargs)
                        

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
                            delete_object_group(entity, conf, sdata, **kwargs)
                           
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        delete_object_group(entity, conf, sdata, **kwargs)
                        

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
                            delete_object_group(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_triple'
                            delete_object_group(entity, conf, sdata, **kwargs)
                            entity = 'cpe_tertiary_triple'
                            delete_object_group(entity, conf, sdata, **kwargs)
                            
                    else:
                        site = inputdict['triple_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_triple'
                        delete_object_group(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_triple'
                        delete_object_group(entity, conf, sdata, **kwargs)
                        entity = 'cpe_tertiary_triple'
                        delete_object_group(entity, conf, sdata, **kwargs)

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
                            delete_object_group(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_dual'
                            delete_object_group(entity, conf, sdata, **kwargs)
                           
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_dual'
                        delete_object_group(entity, conf, sdata, **kwargs)
                        
                        entity = 'cpe_secondary_dual'
                        delete_object_group(entity, conf, sdata, **kwargs)
                        

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

def delete_object_group(entity, conf, sdata, **kwargs):
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
    object_group_name = inputdict['object_group_name']
    

    url_objgroup = '/controller:devices/device=%s/acl:object-groups-acl/' %(device.device.id)
    try:
        dev_objgroup = yang.Sdk.getData(url_objgroup, '', sdata.getTaskId())
        conf_objgroup = util.parseXmlString(dev_objgroup)
    except DataNodeNotFoundException:
        yang.Sdk.createData(device.url, '<object-groups-acl/>', sdata.getSession(), False)

    device_object_group = []
    if hasattr(conf_objgroup.object_groups_acl, 'object_group'):
        conf_objgroup.object_groups_acl.object_group = util.convert_to_list(conf_objgroup.object_groups_acl.object_group)
        for objgroup in conf_objgroup.object_groups_acl.object_group:
            device_object_group.append(objgroup.name)
    
        if object_group_name in device_object_group:
            object_group_url = '/controller:devices/device=%s/acl:object-groups-acl/object-group=%s' % (device.device.id, object_group_name)
            output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+object_group_url+'</rc-path></input>')
            ref = util.parseXmlString(output)
            log("xml_op:%s" %(ref))
            if hasattr(ref.output, 'references'):
                if hasattr(ref.output.references, 'reference'):
                    for eachreference in util.convert_to_list(ref.output.references.reference):
                        if hasattr(eachreference, 'src_node'):
                            for each_ref in util.convert_to_list(eachreference.src_node):
                                yang.Sdk.removeReference(each_ref, eachreference.dest_node)
            yang.Sdk.deleteData(object_group_url, '', sdata.getTaskId(), sdata.getSession())
        else:
            log("Object-Group is not in device: " + str(device))
   


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
