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
                                                                delete-class-map
                                                                                
Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps-update/delete-class-map
"""
"""
Names of Leafs for this Yang Entity
                  id
                name
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
                            delete_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        delete_match_condition(entity, conf, sdata, **kwargs)

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
                            delete_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary'
                            delete_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary'
                        delete_match_condition(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary'
                        delete_match_condition(entity, conf, sdata, **kwargs)

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
                            delete_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        delete_match_condition(entity, conf, sdata, **kwargs)

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
                            delete_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_triple'
                            delete_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_tertiary_triple'
                            delete_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['triple_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_triple'
                        delete_match_condition(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_triple'
                        delete_match_condition(entity, conf, sdata, **kwargs)
                        entity = 'cpe_tertiary_triple'
                        delete_match_condition(entity, conf, sdata, **kwargs)

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
                            delete_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_dual'
                            delete_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_dual'
                        delete_match_condition(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_dual'
                        delete_match_condition(entity, conf, sdata, **kwargs)

    @staticmethod
    def process_service_device_bindings(smodelctx, sdata, dev, **kwargs):
        """ Custom API to modify the inputs"""
        modify = True
        if modify and kwargs is not None:
            for key, value in kwargs.iteritems():
                log("%s == %s" %(key,value))

        if modify:
            config = kwargs['config']
            inputdict = kwargs['inputdict']

    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      raise Exception('Update forbidden for node delete-class-map at path managed-cpe-services/customer/qos-service/class-maps-update/delete-class-map')
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

    url_device_class = '/controller:devices/device=%s/qos:class-maps' %(device.device.id)
    device_class = yang.Sdk.getData(url_device_class, '', sdata.getTaskId())
    conf_cls = util.parseXmlString(device_class)

    device_cls = []
    if hasattr(conf_cls.class_maps, 'class_map'):
        conf_cls.class_maps.class_map = util.convert_to_list(conf_cls.class_maps.class_map)
        for cls in conf_cls.class_maps.class_map:
            device_cls.append(cls.name)

    if cls_name in device_cls:
        url_device_class_map = '/controller:devices/device=%s/qos:class-maps/class-map=%s' %(device.device.id, cls_name)
        device_class_map = yang.Sdk.getData(url_device_class_map, '', sdata.getTaskId())
        conf_class = util.parseXmlString(device_class_map)

        cls_map_obj = devices.device.class_maps.class_map.class_map()
        cls_map_obj.name = cls_name
        device_dscp = []
        if hasattr(conf_class.class_map, 'class_match_condition'):
            conf_class.class_map.class_match_condition = util.convert_to_list(conf_class.class_map.class_match_condition)
            for dscp_dyn in conf_class.class_map.class_match_condition:
                if dscp_dyn.condition_type == 'ip-dscp':
                    device_dscp.append(dscp_dyn.match_value)
        if len(inputdict['dscp']) > 0:
            if isinstance(inputdict['dscp'], list) is True:
                for ds in inputdict['dscp']:
                    if ds in device_dscp:
                        match_obj = devices.device.class_maps.class_map.class_match_condition.class_match_condition()
                        match_obj.condition_type = "ip-dscp"
                        match_obj.match_value = ds
                        yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name, 'ip-dscp', ds), match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
            else:
                if inputdict['dscp'] in device_dscp:
                    match_obj = devices.device.class_maps.class_map.class_match_condition.class_match_condition()
                    match_obj.condition_type = "ip-dscp"
                    match_obj.match_value = inputdict['dscp']
                    yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name, 'ip-dscp', inputdict['dscp']), match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())

        device_protocol = []
        if hasattr(conf_class.class_map, 'class_match_condition'):
            conf_class.class_map.class_match_condition = util.convert_to_list(conf_class.class_map.class_match_condition)
            for protocol_dyn in conf_class.class_map.class_match_condition:
                if protocol_dyn.condition_type == 'protocol':
                    device_protocol.append(protocol_dyn.match_value)
        if len(inputdict['protocol']) > 0:
            if isinstance(inputdict['protocol'], list) is True:
                for pr in inputdict['protocol']:
                    if pr in device_protocol:
                        cls_protocol_url = "/controller:devices/device=%s/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(device.device.id, cls_name, 'protocol', pr)
                        output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+cls_protocol_url+'</rc-path></input>')
                        ref = util.parseXmlString(output)
                        if hasattr(ref.output, 'references'):
                           if hasattr(ref.output.references, 'reference'):
                               if hasattr(ref.output.references.reference, 'src_node'):
                                  for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                                     yang.Sdk.removeReference(each_ref, cls_protocol_url)
                        match_obj = devices.device.class_maps.class_map.class_match_condition.class_match_condition()
                        match_obj.condition_type = "protocol"
                        match_obj.match_value = pr
                        yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name, 'protocol', pr), match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
                        if pr == "http":
                            # device_http_url = []
                            # if hasattr(conf_class.class_map.class_match_condition, 'http_url'):
                            #     conf_class.class_map.class_match_condition.http_url = util.convert_to_list(conf_class.class_map.class_match_condition.http_url)
                            #     for dev_http_url in conf_class.class_map.class_match_condition.http_url:
                            #         device_http_url.append(dev_http_url.url)
                            match_object = devices.device.class_maps.class_map.class_match_condition.http_url.http_url()
                            http_url = inputdict['http_url']
                            print "http_url is:",http_url

                            path = '/controller:devices/device=%s/qos:class-maps/class-map=%s/class-match-condition=%s,%s' %(device.device.id, cls_name, 'protocol', pr)
                            http = yang.Sdk.getData(path, '', sdata.getTaskId())
                            obj_http = util.parseXmlString(http)

                            if util.isNotEmpty(http_url):
                                for url_http in util.convert_to_list(http_url):
                                    if hasattr(obj_http.class_match_condition, 'http_url'):
                                        obj_http.class_match_condition.http_url = util.convert_to_list(obj_http.class_match_condition.http_url)
                                        for dev_http_url in obj_http.class_match_condition.http_url:
                                            if dev_http_url.url == url_http:
                                                match_object.url = url_http
                                                yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s/http-url=%s,%s" %(cls_name,'protocol','http',dev_http_url.url), match_object.getxml(filter=True), sdata.getSession())
                            else:
                                cls_protocol_url = "/controller:devices/device=%s/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(device.device.id, cls_name, 'protocol', pr)
                                output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+cls_protocol_url+'</rc-path></input>')
                                ref = util.parseXmlString(output)
                                if hasattr(ref.output, 'references'):
                                    if hasattr(ref.output.references, 'reference'):
                                        if hasattr(ref.output.references.reference, 'src_node'):
                                           for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                                                yang.Sdk.removeReference(each_ref, cls_protocol_url)
                                match_obj = devices.device.class_maps.class_map.class_match_condition.class_match_condition()
                                match_obj.condition_type = "protocol"
                                match_obj.match_value = pr
                                match_obj.only_http = 'true'
                                yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name, 'protocol', pr), match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
            else:
                if inputdict['protocol'] in device_protocol:
                    cls_protocol_url = "/controller:devices/device=%s/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(device.device.id, cls_name, 'protocol', inputdict['protocol'])
                    output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+cls_protocol_url+'</rc-path></input>')
                    ref = util.parseXmlString(output)
                    if hasattr(ref.output, 'references'):
                        if hasattr(ref.output.references, 'reference'):
                            if hasattr(ref.output.references.reference, 'src_node'):
                                for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                                    yang.Sdk.removeReference(each_ref, cls_protocol_url)
                    match_obj = devices.device.class_maps.class_map.class_match_condition.class_match_condition()
                    match_obj.condition_type = "protocol"
                    match_obj.match_value = inputdict['protocol']
                    yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name, 'protocol', inputdict['protocol']), match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
                    if inputdict['protocol'] == "http":
                        # device_http_url = []
                        # if hasattr(conf_class.class_map.class_match_condition, 'http_url'):
                        #     conf_class.class_map.class_match_condition.http_url = util.convert_to_list(conf_class.class_map.class_match_condition.http_url)
                        #     for dev_http_url in conf_class.class_map.class_match_condition.http_url:
                        #         device_http_url.append(dev_http_url.url)
                        match_object = devices.device.class_maps.class_map.class_match_condition.http_url.http_url()
                        http_url = inputdict['http_url']
                        print "http_url is:",http_url

                        path = '/controller:devices/device=%s/qos:class-maps/class-map=%s/class-match-condition=%s,%s' %(device.device.id, cls_name, 'protocol', inputdict['protocol'])
                        http = yang.Sdk.getData(path, '', sdata.getTaskId())
                        obj_http = util.parseXmlString(http)

                        if util.isNotEmpty(http_url):
                            for url_http in util.convert_to_list(http_url):
                                if hasattr(obj_http.class_match_condition, 'http_url'):
                                    obj_http.class_match_condition.http_url = util.convert_to_list(obj_http.class_match_condition.http_url)
                                    for dev_http_url in obj_http.class_match_condition.http_url:
                                        if dev_http_url.url == url_http:
                                            match_object.url = url_http
                                            yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s/http-url=%s" %(cls_name,'protocol','http',dev_http_url.url), match_object.getxml(filter=True), sdata.getSession())
                        else:
                            match_obj = devices.device.class_maps.class_map.class_match_condition.class_match_condition()
                            match_obj.condition_type = "protocol"
                            match_obj.match_value = inputdict['protocol']
                            match_obj.only_http = 'true'
                            yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name, 'protocol', inputdict['protocol']), match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())

        device_access_group = []
        if hasattr(conf_class.class_map, 'class_match_condition'):
            conf_class.class_map.class_match_condition = util.convert_to_list(conf_class.class_map.class_match_condition)
            for access_dyn in conf_class.class_map.class_match_condition:
                if access_dyn.condition_type == 'access-group':
                    device_access_group.append(access_dyn.match_value)
        if util.isNotEmpty(access_group):
            if access_group in device_access_group:
                #Test to remove existing references
                cls_acl_url = "/controller:devices/device=%s/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(device.device.id, cls_name, 'access-group', access_group)
                output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+cls_acl_url+'</rc-path></input>')
                ref = util.parseXmlString(output)
                if hasattr(ref.output, 'references'):
                    if hasattr(ref.output.references, 'reference'):
                        if hasattr(ref.output.references.reference, 'src_node'):
                            for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                                yang.Sdk.removeReference(each_ref, cls_acl_url)
                match_obj = devices.device.class_maps.class_map.class_match_condition.class_match_condition()
                match_obj.condition_type = "access-group"
                match_obj.match_value = access_group
                yang.Sdk.deleteData(cls_acl_url, match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())

        device_qos_group = []
        if hasattr(conf_class.class_map, 'class_match_condition'):
            conf_class.class_map.class_match_condition = util.convert_to_list(conf_class.class_map.class_match_condition)
            for qos_dyn in conf_class.class_map.class_match_condition:
                if qos_dyn.condition_type == 'qos-group':
                    device_qos_group.append(qos_dyn.match_value)
        if util.isNotEmpty(qos_group):
            if qos_group in device_qos_group:
                    match_obj = devices.device.class_maps.class_map.class_match_condition.class_match_condition()
                    match_obj.condition_type = "qos-group"
                    match_obj.match_value = qos_group
                    yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name, 'qos-group', qos_group), match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
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
