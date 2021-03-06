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
                                                                create-class-map
                                                                                
Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps-update/create-class-map
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
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        create_match_condition(entity, conf, sdata, **kwargs)

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
                            create_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary'
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary'
                        create_match_condition(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary'
                        create_match_condition(entity, conf, sdata, **kwargs)

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
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        create_match_condition(entity, conf, sdata, **kwargs)

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
                            create_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_triple'
                            create_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_tertiary_triple'
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['triple_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
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
                            #uri = sdata.getRcPath()
                            #uri_list = uri.split('/',5)
                            #url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary_dual'
                            create_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_dual'
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_dual'
                        create_match_condition(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_dual'
                        create_match_condition(entity, conf, sdata, **kwargs)
                        
            if util.isNotEmpty(inputdict['device_group']):
                dev_group_output = yang.Sdk.invokeRpc('controller:apply-data-grouping', '''<input><group-name>'''+ inputdict['device_group'] + '''</group-name></input>''')
                dev_group_obj = util.parseXmlString(dev_group_output)
                if hasattr(dev_group_obj, 'output'):
                    if hasattr(dev_group_obj.output, 'result'):
                        for each_dev in util.convert_to_list(dev_group_obj.output.result):
                            if hasattr(each_dev, 'device'):
                                if hasattr(each_dev.device, 'id'):
                                    create_match_condition(each_dev.device.id, None, sdata, **kwargs)
            modify_class(sdata, **kwargs)
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
      #raise Exception('Update forbidden for node create-class-map at path managed-cpe-services/customer/qos-service/class-maps-update/create-class-map')
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

def modify_class(sdata, **kwargs):
    uri = sdata.getRcPath()
    uri_list = uri.split('/', 5)
    url = '/'.join(uri_list[0:4])
    inputdict = kwargs['inputdict']
    name = inputdict['name']
    if inputdict['update_profile'] == 'true':
        url = url + "/qos-service/class-maps"
        description = '' if util.isEmpty(inputdict['description']) else inputdict['description']
        match_type = '' if util.isEmpty(inputdict['match_type']) else inputdict['match_type']
        dscp = '' if util.isEmpty(inputdict['dscp']) else inputdict['dscp']
        access_group = '' if util.isEmpty(inputdict['access_group']) else inputdict['access_group']
        qos_group = '' if util.isEmpty(inputdict['qos_group']) else inputdict['qos_group']
        protocol = '' if util.isEmpty(inputdict['protocol']) else inputdict['protocol']
        http_url = '' if util.isEmpty(inputdict['http_url']) else inputdict['http_url']

        payload = '''
                    <class-map>
                        <description>'''+description+'''</description>
                        <qos-group>'''+qos_group+'''</qos-group>'''
        if len(dscp) > 0:
            if isinstance(dscp, list) is True:
                for ds in dscp:
                    payload = payload + '''<dscp>'''+ds+'''</dscp>'''
            else:
                payload = payload + '''<dscp>'''+dscp+'''</dscp>'''

        if len(protocol) > 0:
            if isinstance(protocol, list) is True:
                for pr in protocol:
                    payload = payload + '''<protocol>'''+pr+'''</protocol>'''
            else:
                payload = payload + '''<protocol>'''+protocol+'''</protocol>'''

        if len(http_url) > 0:
            if isinstance(http_url, list) is True:
                for hu in http_url:
                    payload = payload + '''<http-url>'''+hu+'''</http-url>'''
            else:
                payload = payload + '''<http-url>'''+http_url+'''</http-url>'''

        if len(access_group) > 0:
            if isinstance(access_group, list) is True:
                for ag in access_group:
                    payload = payload + '''<access-group>'''+ag+'''</access-group>'''
            else:
                payload = payload + '''<access-group>'''+access_group+'''</access-group>'''

        payload = payload + '''   <name>'''+name+'''</name>
                        <match-type>'''+match_type+'''</match-type>
                    </class-map>
                  '''
        yang.Sdk.createData(url, payload, sdata.getSession(), False)


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
    else:
        device = devicemgr.getDeviceById(entity)

    inputdict = kwargs['inputdict']
    cls_name = inputdict['name']
    access_group = inputdict['access_group']
    qos_group = inputdict['qos_group']
    match_type = inputdict['match_type']
    description = inputdict['description']

    device.addQOSClassMapsContainer(sdata.getSession())
    cls_map_obj = class_maps.class_map.class_map()
    cls_map_obj.name = cls_name
    if util.isNotEmpty(description):
        cls_map_obj.description = description
    if util.isNotEmpty(match_type):
        cls_map_obj.match_type = match_type
    yang.Sdk.createData(device.url+"/qos:class-maps", cls_map_obj.getxml(filter=True), sdata.getSession())

    if len(inputdict['dscp']) > 0:
        if isinstance(inputdict['dscp'], list) is True:
            for ds in inputdict['dscp']:
                match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                match_obj.condition_type = "ip dscp"
                match_obj.match_value = ds
                yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)
        else:
            match_obj = class_maps.class_map.class_match_condition.class_match_condition()
            match_obj.condition_type = "ip dscp"
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
                            yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name,'protocol','http'), match_object.getxml(filter=True), sdata.getSession(), False)
                    else:
                        match_obj.only_http = 'true'
                        yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)
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
                        yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name,'protocol','http'), match_object.getxml(filter=True), sdata.getSession(), False)
                else:
                    match_obj.only_http = 'true'
                    yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)

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
            #for access_dyn in conf_acl.device.access_lists.access_list:
                #device_access_group.append(access_dyn.name)
            device_access_group = [access_dyn.name for access_dyn in conf_acl.device.access_lists.access_list]
    if util.isNotEmpty(access_group):

            if len(inputdict['access_group']) > 0:
                if isinstance(inputdict['access_group'], list) is True:
                    for eachacl in inputdict['access_group']:
                        if eachacl not in device_access_group:
                            access_group_def(url, eachacl, device, sdata)

                        match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                        match_obj.condition_type = "access-group"
                        match_obj.match_value = eachacl
                        yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    if access_group not in device_access_group:
                            access_group_def(url, access_group, device, sdata)

                    match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                    match_obj.condition_type = "access-group"
                    match_obj.match_value = access_group
                    yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)

    if util.isNotEmpty(qos_group):
            if len(inputdict['qos_group']) > 0:
                if isinstance(inputdict['qos_group'], list) is True:
                    for eachqosg in inputdict['qos_group']:
                        match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                        match_obj.condition_type = "qos-group"
                        match_obj.match_value = eachqosg
                        yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                    match_obj.condition_type = "qos-group"
                    match_obj.match_value = qos_group
                    yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)


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
