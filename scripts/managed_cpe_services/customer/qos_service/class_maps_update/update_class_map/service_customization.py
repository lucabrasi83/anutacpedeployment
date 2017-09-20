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
                                               class-maps-update
                                                                |
                                                                update-class-map
                                                                                
Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps-update/update-class-map
"""
"""
Names of Leafs for this Yang Entity
                name
         description
          match-type
                dscp
        access-group
           qos-group
            protocol
       traffic-class
  protocol-attribute
  business-relevance
      pre-configured
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
from servicemodel.controller.devices.device import class_maps

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log
from cpedeployment.endpoint_lib import access_group_def


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
            #match_type = inputdict['match_type']
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
                            #delete_match_condition(entity, conf, sdata, **kwargs)
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        #delete_match_condition(entity, conf, sdata, **kwargs)
                        create_match_condition(entity, conf, sdata, **kwargs)

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
                            #delete_match_condition(entity, conf, sdata, **kwargs)
                            create_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary'
                            #delete_match_condition(entity, conf, sdata, **kwargs)
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary'
                        #delete_match_condition(entity, conf, sdata, **kwargs)
                        create_match_condition(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary'
                        #delete_match_condition(entity, conf, sdata, **kwargs)
                        create_match_condition(entity, conf, sdata, **kwargs)

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
                            #delete_match_condition(entity, conf, sdata, **kwargs)
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        #delete_match_condition(entity, conf, sdata, **kwargs)
                        create_match_condition(entity, conf, sdata, **kwargs)

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
                            create_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_triple'
                            create_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_tertiary_triple'
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['triple_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_triple'
                        create_match_condition(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_triple'
                        create_match_condition(entity, conf, sdata, **kwargs)
                        entity = 'cpe_tertiary_triple'
                        create_match_condition(entity, conf, sdata, **kwargs)

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
                            create_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_dual'
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_dual'
                        create_match_condition(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_dual'
                        create_match_condition(entity, conf, sdata, **kwargs)

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
      raise Exception('Update forbidden for node update-class-map at path managed-cpe-services/customer/qos-service/class-maps-update/update-class-map')
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


def delete_match_condition(entity, conf, sdata, **kwargs):
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
    cls_name = inputdict['name']
    dscp = inputdict['dscp']
    access_group = inputdict['access_group']
    qos_group = inputdict['qos_group']
    protocol = inputdict['protocol']

    url_device_class_map = '/controller:devices/device=%s/qos:class-maps/class-map=%s' %(device.device.id, cls_name)
    device_class_map = yang.Sdk.getData(url_device_class_map, '', sdata.getTaskId())
    conf_class = util.parseXmlString(device_class_map)

    cls_map_obj = class_maps.class_map.class_map()
    cls_map_obj.name = cls_name
    device_dscp = []
    if hasattr(conf_class.class_map, 'class_match_condition'):
        conf_class.class_map.class_match_condition = util.convert_to_list(conf_class.class_map.class_match_condition)
        for dscp_dyn in conf_class.class_map.class_match_condition:
            if dscp_dyn.condition_type == 'ip-dscp':
                device_dscp.append(dscp_dyn.match_value)
    if len(inputdict['dscp']) > 0:
        for ds in device_dscp:
            if ds not in dscp:
                match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                match_obj.condition_type = "ip-dscp"
                match_obj.match_value = ds
                yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name, 'ip-dscp', ds), match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())

    device_protocol = []
    if hasattr(conf_class.class_map, 'class_match_condition'):
        conf_class.class_map.class_match_condition = util.convert_to_list(conf_class.class_map.class_match_condition)
        for protocol_dyn in conf_class.class_map.class_match_condition:
            if protocol_dyn.condition_type == 'protocol':
                device_protocol.append(protocol_dyn.match_value)
    if len(inputdict['protocol']) > 0:
        for pr in device_protocol:
            if pr not in protocol:
                match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                match_obj.condition_type = "protocol"
                match_obj.match_value = pr
                yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name, 'protocol', pr), match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())

    device_access_group = []
    if hasattr(conf_class.class_map, 'class_match_condition'):
        conf_class.class_map.class_match_condition = util.convert_to_list(conf_class.class_map.class_match_condition)
        for access_dyn in conf_class.class_map.class_match_condition:
            if access_dyn.condition_type == 'access-group':
                device_access_group.append(access_dyn.match_value)
    if util.isNotEmpty(access_group):
        for access in device_access_group:
            if access != access_group:
                match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                match_obj.condition_type = "access-group"
                match_obj.match_value = access
                yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name, 'access-group', access), match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())

    device_qos_group = []
    if hasattr(conf_class.class_map, 'class_match_condition'):
        conf_class.class_map.class_match_condition = util.convert_to_list(conf_class.class_map.class_match_condition)
        for qos_dyn in conf_class.class_map.class_match_condition:
            if qos_dyn.condition_type == 'qos-group':
                device_qos_group.append(qos_dyn.match_value)
    if util.isNotEmpty(qos_group):
        for qos in device_qos_group:
            if qos != qos_group:
                match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                match_obj.condition_type = "qos-group"
                match_obj.match_value = qos
                yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name, 'qos-group', qos), match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())


def create_match_condition(entity, conf, sdata, **kwargs):
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
    cls_name = inputdict['name']
    access_group = inputdict['access_group']
    qos_group = inputdict['qos_group']

    url_device_class = '/controller:devices/device=%s/qos:class-maps' %(device.device.id)
    device_class = yang.Sdk.getData(url_device_class, '', sdata.getTaskId())
    conf_cls = util.parseXmlString(device_class)

    device_cls = []
    if hasattr(conf_cls.class_maps, 'class_map'):
        conf_cls.class_maps.class_map = util.convert_to_list(conf_cls.class_maps.class_map)
        for cls in conf_cls.class_maps.class_map:
            device_cls.append(cls.name)

    if cls_name in device_cls:
        cls_map_obj = class_maps.class_map.class_map()
        cls_map_obj.name = cls_name
        if len(inputdict['dscp']) > 0:
            if isinstance(inputdict['dscp'], list) is True:
                for ds in inputdict['dscp']:
                    match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                    match_obj.condition_type = "ip-dscp"
                    match_obj.match_value = ds
                    yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)
            else:
                match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                match_obj.condition_type = "ip-dscp"
                match_obj.match_value = inputdict['dscp']
                yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)

        if len(inputdict['protocol']) > 0:
            if isinstance(inputdict['protocol'], list) is True:
                for pr in inputdict['protocol']:
                    match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                    match_obj.condition_type = "protocol"
                    match_obj.match_value = pr
                    yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)
                    if pr == "http":
                        match_object = class_maps.class_map.class_match_condition.http_url.http_url()
                        http_url = inputdict['http_url']
                        print "http_url is:",http_url
                        if util.isNotEmpty(http_url):
                            for url_http in util.convert_to_list(http_url):
                                match_object.url = url_http
                                yang.Sdk.createData(device.url+"/class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name,'protocol','http'), match_object.getxml(filter=True), sdata.getSession(), False)
                        else:
                            match_obj.only_http = 'true'
                            yang.Sdk.createData(device.url+"/class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)
            else:
                match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                match_obj.condition_type = "protocol"
                match_obj.match_value = inputdict['protocol']
                yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)
                if inputdict['protocol'] == "http":
                    match_object = class_maps.class_map.class_match_condition.http_url.http_url()
                    http_url = inputdict['http_url']
                    print "http_url is:",http_url
                    if util.isNotEmpty(http_url):
                        for url_http in util.convert_to_list(http_url):
                            match_object.url = url_http
                            yang.Sdk.createData(device.url+"/class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name,'protocol','http'), match_object.getxml(filter=True), sdata.getSession(), False)
                    else:
                        match_obj.only_http = 'true'
                        yang.Sdk.createData(device.url+"/class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)

        url_device_acl = '/controller:devices/device=%s' %(device.device.id)
        device_acl = yang.Sdk.getData(url_device_acl, '', sdata.getTaskId())
        conf_acl = util.parseXmlString(device_acl)
        device_access_group = []
        uri = sdata.getRcPath()
        uri_list = uri.split('/',5)
        url = '/'.join(uri_list[0:4])
        if hasattr(conf_acl.device, 'access_lists'):
            if hasattr(conf_acl.device, 'access_list'):
                conf_acl.device.access_lists.access_list = util.convert_to_list(conf_acl.device.access_lists.access_list)
                for access_dyn in conf_acl.device.access_lists.access_list:
                    device_access_group.append(access_dyn.name)

        if util.isNotEmpty(access_group):
            if access_group not in device_access_group:
                access_group_def(url, access_group, device, sdata)

            match_obj = class_maps.class_map.class_match_condition.class_match_condition()
            match_obj.condition_type = "access-group"
            match_obj.match_value = access_group
            yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)

        if util.isNotEmpty(qos_group):
            match_obj = class_maps.class_map.class_match_condition.class_match_condition()
            match_obj.condition_type = "qos-group"
            match_obj.match_value = qos_group
            yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)
    else:
        print "Class is not in device: ", device


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
