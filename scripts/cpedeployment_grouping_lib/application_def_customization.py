
from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr
from servicemodel.controller.devices.device import wanop_applications

import copy

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import getPreviousObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject
from cpedeployment.cpedeployment_lib import log

"""
Names of Leafs for this Yang Entity
    application-name            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/name
               group            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/group
       business-crit            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/business-crit
            category            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/category
         description            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/description
        traffic-type            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/traffic-type
      transport-prot            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/transport-prot
                dscp            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/dscp
                vlan            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/vlan
          local-port            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/local-port
         remote-port            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/remote-port
           local-net            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/local-net
          remote-net            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/remote-net
            app-prot            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/app-prot

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_application_def_application(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_application_def_application(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_application_def_application(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
    application-name            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/name
               group            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/group
       business-crit            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/business-crit
            category            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/category
         description
        traffic-type            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/traffic-type
      transport-prot            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/transport-prot
                dscp            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/dscp
                vlan            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/vlan
          local-port            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/local-port
         remote-port            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/remote-port
           local-net            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/local-net
          remote-net            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/remote-net
            app-prot            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/app-prot
           operation
          type1-site
         type1-sites
          type2-site
         type2-sites

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_application_def_update_application(smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs["inputdict"]
    type1_site = inputdict['type1_site']
    type1_sites = inputdict['type1_sites']
    type2_site = inputdict['type2_site']
    type2_sites = inputdict['type2_sites']
    type3_site = inputdict['type3_site']
    type3_sites = inputdict['type3_sites']
    type4_site = inputdict['type4_site']
    type4_sites = inputdict['type4_sites']
    dev_url = []
    if type1_site and util.isNotEmpty(type1_sites):
        for site in util.convert_to_list(type1_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type1-site/type1-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_application("type1_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_application("type1_site", conf, sdata, **kwargs)

    if type2_site and util.isNotEmpty(type2_sites):
        for site in util.convert_to_list(type2_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type2-site/type2-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_application("type2_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_application("type2_site", conf, sdata, **kwargs)

    if type3_site and util.isNotEmpty(type3_sites):
        for site in util.convert_to_list(type3_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type3-site/type3-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_application("type3_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_application("type3_site", conf, sdata, **kwargs)

    if type4_site and util.isNotEmpty(type4_sites):
        for site in util.convert_to_list(type4_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type4-site/type4-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_application("type4_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_application("type4_site", conf, sdata, **kwargs)
    return dev_url

def create_application(entity, conf, sdata, **kwargs):
    dev_object_list = []
    if entity == "type1_site":
        device = devicemgr.getDeviceById(conf.type1_site.wanop.device_ip)
        log("device object:"+str(device))
        dev_object_list.append(device)
    if entity == "type3_site":
        device = devicemgr.getDeviceById(conf.type3_site.wanop.device_ip)
        log("device object:"+str(device))
        dev_object_list.append(device)
    if entity == "type2_site":
        primary_device = devicemgr.getDeviceById(conf.type2_site.wanop_primary.device_ip)
        sec_device = devicemgr.getDeviceById(conf.type2_site.wanop_secondary.device_ip)
        dev_object_list.append(primary_device)
        dev_object_list.append(sec_device)
    if entity == "type4_site":
        primary_device = devicemgr.getDeviceById(conf.type4_site.wanop_primary.device_ip)
        sec_device = devicemgr.getDeviceById(conf.type4_site.wanop_secondary.device_ip)
        dev_object_list.append(primary_device)
        dev_object_list.append(sec_device)

    dev_url = []
    for device in set(dev_object_list):
        url_device_prefix = '/controller:devices/device=%s/wanoptimizer:wanop-applications' %(device.device.id)
        device_prefix = yang.Sdk.getData(url_device_prefix, '', sdata.getTaskId())
        conf_prefix = util.parseXmlString(device_prefix)
        log("conf_prefix: "+str(conf_prefix))

        device_pre = []
        if hasattr(conf_prefix.wanop_applications, 'wanop_application'):
            conf_prefix.wanop_applications.wanop_application = util.convert_to_list(conf_prefix.wanop_applications.wanop_application)
            for pre in conf_prefix.wanop_applications.wanop_application:
                device_pre.append(pre.name)
        if kwargs["inputdict"]["application_name"] in device_pre:
            dev_url.append(device)
        else:
            print "Application:%s is not in device:%s"%(kwargs["inputdict"]["application_name"],device.device.mgmt_ip_address)
    return dev_url

def delete_application(entity, conf, sdata, **kwargs):
    dev_object_list = []
    if entity == "type1_site":
        device = devicemgr.getDeviceById(conf.type1_site.wanop.device_ip)
        log("device object:"+str(device))
        dev_object_list.append(device)
    if entity == "type3_site":
        device = devicemgr.getDeviceById(conf.type3_site.wanop.device_ip)
        log("device object:"+str(device))
        dev_object_list.append(device)
    if entity == "type2_site":
        primary_device = devicemgr.getDeviceById(conf.type2_site.wanop_primary.device_ip)
        sec_device = devicemgr.getDeviceById(conf.type2_site.wanop_secondary.device_ip)
        dev_object_list.append(primary_device)
        dev_object_list.append(sec_device)
    if entity == "type4_site":
        primary_device = devicemgr.getDeviceById(conf.type4_site.wanop_primary.device_ip)
        sec_device = devicemgr.getDeviceById(conf.type4_site.wanop_secondary.device_ip)
        dev_object_list.append(primary_device)
        dev_object_list.append(sec_device)

    for device in set(dev_object_list):
        url_device_prefix = '/controller:devices/device=%s/wanoptimizer:wanop-applications' %(device.device.id)
        device_prefix = yang.Sdk.getData(url_device_prefix, '', sdata.getTaskId())
        conf_prefix = util.parseXmlString(device_prefix)
        log("conf_prefix: "+str(conf_prefix))

        device_pre = []
        if hasattr(conf_prefix.wanop_applications, 'wanop_application'):
            conf_prefix.wanop_applications.wanop_application = util.convert_to_list(conf_prefix.wanop_applications.wanop_application)
            for pre in conf_prefix.wanop_applications.wanop_application:
                device_pre.append(pre.name)
        if kwargs["inputdict"]["application_name"] in device_pre:
            prefix_obj = wanop_applications.wanop_application.wanop_application()
            prefix_obj.name = kwargs["inputdict"]["application_name"]
            app_url = '/controller:devices/device=%s/wanoptimizer:wanop-applications/wanop-application=%s' %(device.device.id, kwargs["inputdict"]["application_name"])
            output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+app_url+'</rc-path></input>')
            ref = util.parseXmlString(output)
            log("xml_op:%s" %(ref))
            if hasattr(ref.output, 'references'):
                if hasattr(ref.output.references, 'reference'):
                    if hasattr(ref.output.references.reference, 'src_node'):
                        for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                            yang.Sdk.removeReference(each_ref, app_url)

            yang.Sdk.deleteData(app_url, prefix_obj.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
        else:
            print "Application:%s is not in device:%s"%(kwargs["inputdict"]["application_name"],device.device.mgmt_ip_address)

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_application_def_update_application(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_application_def_update_application(smodelctx, sdata, **kwargs):
    pass
