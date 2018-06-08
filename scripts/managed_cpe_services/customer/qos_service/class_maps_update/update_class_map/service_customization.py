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
from cpedeployment.endpoint_lib import access_group_def, cust_nbar


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
            #match_type = inputdict['match_type']
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
                            #delete_match_condition(entity, conf, sdata, **kwargs)
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        #delete_match_condition(entity, conf, sdata, **kwargs)
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
                            #delete_match_condition(entity, conf, sdata, **kwargs)
                            create_match_condition(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary'
                            #delete_match_condition(entity, conf, sdata, **kwargs)
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
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
                            #uri = sdata.getRcPath()
                            #uri_list = uri.split('/',5)
                            #url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_dual'
                            #delete_match_condition(entity, conf, sdata, **kwargs)
                            create_match_condition(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        #delete_match_condition(entity, conf, sdata, **kwargs)
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
      #raise Exception('Update forbidden for node update-class-map at path managed-cpe-services/customer/qos-service/class-maps-update/update-class-map')
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
    qos_group = '' if util.isEmpty(inputdict['qos_group']) else inputdict['qos_group']
    dscp = '' if util.isEmpty(inputdict['dscp']) else inputdict['dscp']
    access_group = '' if util.isEmpty(inputdict['access_group']) else inputdict['access_group']
    protocol = '' if util.isEmpty(inputdict['protocol']) else inputdict['protocol']
    http_url = '' if util.isEmpty(inputdict['http_url']) else inputdict['http_url']
    custom_nbar = '' if util.isEmpty(inputdict['custom_nbar']) else inputdict['custom_nbar']
    if inputdict['update_profile'] == 'true':
        url = url + "/qos-service/class-maps/class-map=" + str(name)
        
        service_class = yang.Sdk.getData(url, '', sdata.getTaskId())
        conf_cls = util.parseXmlString(service_class)

        service_qos_group = []
        if hasattr(conf_cls.class_map, 'qos_group'):
            conf_cls.class_map.qos_group = util.convert_to_list(conf_cls.class_map.qos_group)
            for qg in conf_cls.class_map.qos_group:
                service_qos_group.append(qg)

        if len(qos_group) > 0:
            if isinstance(qos_group, list) is True:
                for qg_bulk in qos_group:
                    if qg_bulk in service_qos_group:
                        service_qos_group.append(qg_bulk)
            else:
                if qos_group in service_qos_group:
                    service_qos_group.append(qos_group)

        if len(service_qos_group) > 0:
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>
                                <qos-group>'''+qos_group+'''</qos-group>
                            </class-map>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>'''
            for qg in service_qos_group:
                payload = payload + '''<qos-group>'''+qg+'''</qos-group>'''
            payload = payload + ''' </class-map>'''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)

        else:
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>
                                <qos-group></qos-group>
                            </class-map>
                      '''

            yang.Sdk.patchData(url, payload, sdata, add_reference=False)

        service_dscp = []
        if hasattr(conf_cls.class_map, 'dscp'):
            conf_cls.class_map.dscp = util.convert_to_list(conf_cls.class_map.dscp)
            for ds in conf_cls.class_map.dscp:
                service_dscp.append(ds)

        if len(dscp) > 0:
            if isinstance(dscp, list) is True:
                for ds_bulk in dscp:
                    if ds_bulk not in service_dscp:
                        service_dscp.append(ds_bulk)
            else:
                if dscp not in service_dscp:
                    service_dscp.append(dscp)
        if len(service_dscp) > 0:
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>
                                <dscp></dscp>
                            </class-map>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>'''
            for ds in service_dscp:
                payload = payload + '''<dscp>'''+ds+'''</dscp>'''
            payload = payload + ''' </class-map>'''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
        else:
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>
                                <dscp></dscp>
                            </class-map>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)

        service_access_group = []
        if hasattr(conf_cls.class_map, 'access_group'):
            conf_cls.class_map.access_group = util.convert_to_list(conf_cls.class_map.access_group)
            for ag in conf_cls.class_map.access_group:
                service_access_group.append(ag)

        if len(access_group) > 0:
            if isinstance(access_group, list) is True:
                for ag_bulk in access_group:
                    if ag_bulk not in service_access_group:
                        service_access_group.append(ag_bulk)
            else:
                if access_group not in service_access_group:
                    service_access_group.append(access_group)
        if len(service_access_group) > 0:
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>
                                <access-group></access-group>
                            </class-map>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>'''
            for ag in service_access_group:
                payload = payload + '''<access-group>'''+ag+'''</access-group>'''
            payload = payload + ''' </class-map>'''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
        else:
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>
                                <access-group></access-group>
                            </class-map>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)

        service_protocol = []
        if hasattr(conf_cls.class_map, 'protocol'):
            conf_cls.class_map.protocol = util.convert_to_list(conf_cls.class_map.protocol)
            for pr in conf_cls.class_map.protocol:
                service_protocol.append(pr)

        if len(protocol) > 0:
            if isinstance(protocol, list) is True:
                for pr_bulk in protocol:
                    if pr_bulk not in service_protocol:
                        service_protocol.append(pr_bulk)
            else:
                if protocol not in service_protocol:
                    service_protocol.append(protocol)
        if len(service_protocol) > 0:
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>
                                <protocol></protocol>
                            </class-map>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>'''
            for pr in service_protocol:
                payload = payload + '''<protocol>'''+pr+'''</protocol>'''
            payload = payload + ''' </class-map>'''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
        else:
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>
                                <protocol></protocol>
                            </class-map>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)

        service_cust_nbar = []
        if hasattr(conf_cls.class_map, 'custom_nbar'):
            conf_cls.class_map.custom_nbar = util.convert_to_list(conf_cls.class_map.custom_nbar)
            for nb in conf_cls.class_map.custom_nbar:
                service_cust_nbar.append(nb)

        if len(custom_nbar) > 0:
            if isinstance(custom_nbar, list) is True:
                for nbar_bulk in custom_nbar:
                    if nbar_bulk not in service_cust_nbar:
                        service_cust_nbar.append(nbar_bulk)
            else:
                if custom_nbar not in service_cust_nbar:
                    service_cust_nbar.append(custom_nbar)
        if len(service_cust_nbar) > 0:
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>
                                <custom-nbar></custom-nbar>
                            </class-map>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>'''
            for nbar in service_cust_nbar:
                payload = payload + '''<custom-nbar>'''+nbar+'''</custom-nbar>'''
            payload = payload + ''' </class-map>'''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
        else:
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>
                                <custom-nbar></custom-nbar>
                            </class-map>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)

        service_http_url = []
        if hasattr(conf_cls.class_map, 'http_url'):
            conf_cls.class_map.http_url = util.convert_to_list(conf_cls.class_map.http_url)
            for hu in conf_cls.class_map.http_url:
                service_http_url.append(hu)

        if len(http_url) > 0:
            if isinstance(http_url, list) is True:
                for hu_bulk in http_url:
                    if hu_bulk not in service_http_url:
                        service_http_url.append(hu_bulk)
            else:
                if http_url not in service_http_url:
                    service_http_url.append(http_url)
        if len(service_http_url) > 0:
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>
                                <http-url></http-url>
                            </class-map>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>'''
            for hu in service_http_url:
                payload = payload + '''<http-url>'''+hu+'''</http-url>'''
            payload = payload + ''' </class-map>'''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
        else:
            payload = '''
                            <class-map>
                                <name>'''+name+'''</name>
                                <http-url></http-url>
                            </class-map>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)


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
    else:
        device = devicemgr.getDeviceById(entity)

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
        #for dscp_dyn in conf_class.class_map.class_match_condition:
            #if dscp_dyn.condition_type == 'ip-dscp':
                #device_dscp.append(dscp_dyn.match_value)
        device_dscp = [dscp_dyn.match_value for dscp_dyn in conf_class.class_map.class_match_condition if dscp_dyn.condition_type == 'ip dscp']
    if len(inputdict['dscp']) > 0:
        for ds in device_dscp:
            if ds not in dscp:
                match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                match_obj.condition_type = "ip dscp"
                match_obj.match_value = ds
                yang.Sdk.deleteData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name, 'ip dscp', ds), match_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())

    device_protocol = []
    if hasattr(conf_class.class_map, 'class_match_condition'):
        conf_class.class_map.class_match_condition = util.convert_to_list(conf_class.class_map.class_match_condition)
        #for protocol_dyn in conf_class.class_map.class_match_condition:
            #if protocol_dyn.condition_type == 'protocol':
                #device_protocol.append(protocol_dyn.match_value)
        device_protocol = [protocol_dyn.match_value for protocol_dyn in conf_class.class_map.class_match_condition if protocol_dyn.condition_type == 'protocol']
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
        #for access_dyn in conf_class.class_map.class_match_condition:
            #if access_dyn.condition_type == 'access-group':
                #device_access_group.append(access_dyn.match_value)
        device_access_group = [access_dyn.match_value for access_dyn in conf_class.class_map.class_match_condition if access_dyn.condition_type == 'access-group']
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
        #for qos_dyn in conf_class.class_map.class_match_condition:
            #if qos_dyn.condition_type == 'qos-group':
                #device_qos_group.append(qos_dyn.match_value)
        device_qos_group = [qos_dyn.match_value for qos_dyn in conf_class.class_map.class_match_condition if qos_dyn.condition_type == 'qos-group']
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
    else:
        device = devicemgr.getDeviceById(entity)

    inputdict = kwargs['inputdict']
    cls_name = inputdict['name']
    access_group = inputdict['access_group']
    qos_group = inputdict['qos_group']
    custom_nbar = inputdict['custom_nbar']
    url_device_class = '/controller:devices/device=%s/qos:class-maps/class-map=%s' %(device.device.id, cls_name)

    '''
    device_class = yang.Sdk.getData(url_device_class, '', sdata.getTaskId())
    conf_cls = util.parseXmlString(device_class)

    device_cls = []
    if hasattr(conf_cls.class_maps, 'class_map'):
        conf_cls.class_maps.class_map = util.convert_to_list(conf_cls.class_maps.class_map)
        #for cls in conf_cls.class_maps.class_map:
            #device_cls.append(cls.name)
        device_cls = [cls.name for cls in conf_cls.class_maps.class_map]
    '''
    #if cls_name in device_cls:
    if yang.Sdk.dataExists(url_device_class):
        cls_map_obj = class_maps.class_map.class_map()
        cls_map_obj.name = cls_name
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
                        # print "http_url is:",http_url
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
                    # print "http_url is:",http_url
                    if util.isNotEmpty(http_url):
                        for url_http in util.convert_to_list(http_url):
                            match_object.url = url_http
                            yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name,'protocol','http'), match_object.getxml(filter=True), sdata.getSession(), False)
                    else:
                        match_obj.only_http = 'true'
                        yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)

        if len(inputdict['custom_nbar']) > 0:
            if isinstance(inputdict['custom_nbar'], list) is True:
                for nbar in inputdict['custom_nbar']:
                    cust_nbar(nbar, device, sdata)
                    match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                    match_obj.condition_type = "protocol"
                    match_obj.match_value = nbar
                    yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)
                   
            else:
                cust_nbar(inputdict['custom_nbar'], device, sdata)
                match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                match_obj.condition_type = "protocol"
                match_obj.match_value = inputdict['custom_nbar']
                yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)
                
        '''
        url_device_acl = '/controller:devices/device=%s/acl:access-lists' %(device.device.id)
        
        device_acl = yang.Sdk.getData(url_device_acl, '', sdata.getTaskId())
        conf_acl = util.parseXmlString(device_acl)
        device_access_group = []
        
        if hasattr(conf_acl.device, 'access_lists'):
            if hasattr(conf_acl.device, 'access_list'):
                conf_acl.device.access_lists.access_list = util.convert_to_list(conf_acl.device.access_lists.access_list)
                #for access_dyn in conf_acl.device.access_lists.access_list:
                    #device_access_group.append(access_dyn.name)
                device_access_group = [access_dyn.name for access_dyn in conf_acl.device.access_lists.access_list]
        '''
        uri = sdata.getRcPath()
        uri_list = uri.split('/',5)
        url = '/'.join(uri_list[0:4])
        if util.isNotEmpty(access_group):

            if len(inputdict['access_group']) > 0:
                if isinstance(inputdict['access_group'], list) is True:
                    for eachacl in inputdict['access_group']:
                        url_device_acl = '/controller:devices/device=%s/acl:access-lists/access-list=%s' %(device.device.id, eachacl)
                        #if eachacl not in device_access_group:
                        if not yang.Sdk.dataExists(url_device_acl):
                            access_group_def(url, eachacl, device, sdata)

                        match_obj = class_maps.class_map.class_match_condition.class_match_condition()
                        match_obj.condition_type = "access-group"
                        match_obj.match_value = eachacl
                        yang.Sdk.createData(device.url+"/qos:class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession(), False)
                else:
                    url_device_acl = '/controller:devices/device=%s/acl:access-lists/access-list=%s' %(device.device.id, access_group)
                    #if access_group not in device_access_group:
                    if not yang.Sdk.dataExists(url_device_acl):
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
    else:
        yang.Sdk.append_taskdetail(sdata.getTaskId(), "Class-Map " + str(cls_name) + " not found on device " + str(device.device.id) + ". Skipping this device")


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
