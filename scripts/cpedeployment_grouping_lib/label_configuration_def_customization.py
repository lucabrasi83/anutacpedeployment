
from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr
from servicemodel.controller.devices.device import label_configuration

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

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_label_configuration_def_host_labels(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_label_configuration_def_host_labels(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_label_configuration_def_host_labels(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
     host-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/host-label-name

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_label_configuration_def_host_labels_host_label(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_label_configuration_def_host_labels_host_label(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_label_configuration_def_host_labels_host_label(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
            hostname            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/hostname/hostname

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_label_configuration_def_host_labels_host_label_hostname(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_label_configuration_def_host_labels_host_label_hostname(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_label_configuration_def_host_labels_host_label_hostname(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
              subnet            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/subnet/subnet

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_label_configuration_def_host_labels_host_label_subnet(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_label_configuration_def_host_labels_host_label_subnet(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_label_configuration_def_host_labels_host_label_subnet(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
     host-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/host-label-name
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
def grouping_create_label_configuration_def_host_labels_update_host_label(smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs["inputdict"]
    type1_site = inputdict['type1_site']
    type1_sites = inputdict['type1_sites']
    type2_site = inputdict['type2_site']
    type2_sites = inputdict['type2_sites']
    type3_site = inputdict['type3_site']
    type3_sites = inputdict['type3_sites']
    type4_site = inputdict['type4_site']
    type4_sites = inputdict['type4_sites']

    if type1_site and util.isNotEmpty(type1_sites):
        for site in util.convert_to_list(type1_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type1-site/type1-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_hostlabel("type1_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_hostlabel("type1_site", conf, sdata, cust_name, **kwargs)

    if type2_site and util.isNotEmpty(type2_sites):
        for site in util.convert_to_list(type2_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type2-site/type2-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_hostlabel("type2_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_hostlabel("type2_site", conf, sdata, cust_name, **kwargs)

    if type3_site and util.isNotEmpty(type3_sites):
        for site in util.convert_to_list(type3_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type3-site/type3-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_hostlabel("type3_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_hostlabel("type3_site", conf, sdata, cust_name, **kwargs)

    if type4_site and util.isNotEmpty(type4_sites):
        for site in util.convert_to_list(type4_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type4-site/type4-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_hostlabel("type4_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_hostlabel("type4_site", conf, sdata, cust_name, **kwargs)
    return dev_url

def create_hostlabel(entity, conf, sdata, **kwargs):
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
        url_device_prefix = '/controller:devices/device=%s/wanoptimizer:label-configuration' %(device.device.id)
        device_prefix = yang.Sdk.getData(url_device_prefix, '', sdata.getTaskId())
        conf_prefix = util.parseXmlString(device_prefix)
        log("conf_prefix: "+str(conf_prefix))

        device_pre = []
        if hasattr(conf_prefix.label_configuration, 'host_label'):
            conf_prefix.label_configuration.host_label = util.convert_to_list(conf_prefix.label_configuration.host_label)
            for pre in conf_prefix.label_configuration.host_label:
                device_pre.append(pre.host_label_name)
        if kwargs["inputdict"]["host_label_name"] in device_pre:
            log("found device:" + device.device.id)
            dev_url.append(device)
        else:
            print "Host-Label:%s is not in device:%s"%(kwargs["inputdict"]["host_label_name"],device.device.mgmt_ip_address)
    return dev_url

def delete_hostlabel(entity, conf, sdata, cust_name, **kwargs):
    dev_object_list = []
    if entity == "type1_site":
        device = devicemgr.getDeviceById(conf.type1_site.wanop.device_ip)
        log("device object:"+str(device))
        dev_object_list.append(device)
        if hasattr(device.device, "inpath_rules"):
            for rule in util.convert_to_list(device.device.inpath_rules.inpath_rules_def):
                dst_host = rule.get_field_value("dst_host")
                if util.isNotEmpty(dst_host) and dst_host == kwargs["inputdict"]["host_label_name"]:
                    raise Exception("Cannot delete Host-Label:"+dst_host+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(device.device, "wanop_applications"):
            for application in util.convert_to_list(device.device.wanop_applications.wanop_application):
                if hasattr(application, "local_net"):
                    local_net = application.local_net
                    log("In application = " + str(application.name) + " : local_net = " + local_net)
                    if util.isNotEmpty(local_net) and local_net == kwargs["inputdict"]["host_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+local_net+".Because it is being used in the application: "+application.name)
                if hasattr(application, "remote_net"):
                    remote_net = application.remote_net
                    log("In application = " + str(application.name) + " : remote_net = " + remote_net)
                    if util.isNotEmpty(remote_net) and remote_net == kwargs["inputdict"]["host_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+remote_net+".Because it is being used in the application: "+application.name)

    if entity == "type3_site":
        device = devicemgr.getDeviceById(conf.type3_site.wanop.device_ip)
        log("device object:"+str(device))
        dev_object_list.append(device)
        if hasattr(device.device, "inpath_rules"):
            for rule in util.convert_to_list(device.device.inpath_rules.inpath_rules_def):
                dst_host = rule.get_field_value("dst_host")
                if util.isNotEmpty(dst_host) and dst_host == kwargs["inputdict"]["host_label_name"]:
                    raise Exception("Cannot delete Host-Label:"+dst_host+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(device.device, "wanop_applications"):
            for application in util.convert_to_list(device.device.wanop_applications.wanop_application):
                if hasattr(application, "local_net"):
                    local_net = application.local_net
                    log("In application = " + str(application.name) + " : local_net = " + local_net)
                    if util.isNotEmpty(local_net) and local_net == kwargs["inputdict"]["host_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+local_net+".Because it is being used in the application: "+application.name)
                if hasattr(application, "remote_net"):
                    remote_net = application.remote_net
                    log("In application = " + str(application.name) + " : remote_net = " + remote_net)
                    if util.isNotEmpty(remote_net) and remote_net == kwargs["inputdict"]["host_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+remote_net+".Because it is being used in the application: "+application.name)

    if entity == "type2_site":
        primary_device = devicemgr.getDeviceById(conf.type2_site.wanop_primary.device_ip)
        sec_device = devicemgr.getDeviceById(conf.type2_site.wanop_secondary.device_ip)
        dev_object_list.append(primary_device)
        dev_object_list.append(sec_device)

        if hasattr(primary_device.device, "inpath_rules"):
            for rule in util.convert_to_list(primary_device.device.inpath_rules.inpath_rules_def):
                dst_host = rule.get_field_value("dst_host")
                if util.isNotEmpty(dst_host) and dst_host == kwargs["inputdict"]["host_label_name"]:
                    raise Exception("Cannot delete Host-Label:"+dst_host+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(sec_device.device, "inpath_rules"):
            for rule in util.convert_to_list(sec_device.device.inpath_rules.inpath_rules_def):
                dst_host = rule.get_field_value("dst_host")
                if util.isNotEmpty(dst_host):
                    raise Exception("Cannot delete Host-Label:"+dst_host+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(primary_device.device, "wanop_applications"):
            for application in util.convert_to_list(primary_device.device.wanop_applications.wanop_application):
                if hasattr(application, "local_net"):
                    local_net = application.local_net
                    log("In application = " + str(application.name) + " : local_net = " + local_net)
                    if util.isNotEmpty(local_net) and local_net == kwargs["inputdict"]["host_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+local_net+".Because it is being used in the application: "+application.name)
                if hasattr(application, "remote_net"):
                    remote_net = application.remote_net
                    log("In application = " + str(application.name) + " : remote_net = " + remote_net)
                    if util.isNotEmpty(remote_net) and remote_net == kwargs["inputdict"]["host_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+remote_net+".Because it is being used in the application: "+application.name)

        if hasattr(sec_device.device, "wanop_applications"):
            for application in util.convert_to_list(sec_device.device.wanop_applications.wanop_application):
                if hasattr(application, "local_net"):
                    local_net = application.local_net
                    log("In application = " + str(application.name) + " : local_net = " + local_net)
                    if util.isNotEmpty(local_net) and local_net == kwargs["inputdict"]["host_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+local_net+".Because it is being used in the application: "+application.name)
                if hasattr(application, "remote_net"):
                    remote_net = application.remote_net
                    log("In application = " + str(application.name) + " : remote_net = " + remote_net)
                    if util.isNotEmpty(remote_net) and remote_net == kwargs["inputdict"]["host_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+remote_net+".Because it is being used in the application: "+application.name)

    if entity == "type4_site":
        primary_device = devicemgr.getDeviceById(conf.type4_site.wanop_primary.device_ip)
        sec_device = devicemgr.getDeviceById(conf.type4_site.wanop_secondary.device_ip)
        dev_object_list.append(primary_device)
        dev_object_list.append(sec_device)

        if hasattr(primary_device.device, "inpath_rules"):
            for rule in util.convert_to_list(primary_device.device.inpath_rules.inpath_rules_def):
                dst_host = rule.get_field_value("dst_host")
                if util.isNotEmpty(dst_host) and dst_host == kwargs["inputdict"]["host_label_name"]:
                    raise Exception("Cannot delete Host-Label:"+dst_host+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(sec_device.device, "inpath_rules"):
            for rule in util.convert_to_list(conf.type4_site.wanop_secondary.inpath_rules.inpath_rules_def):
                dst_host = rule.get_field_value("dst_host")
                if util.isNotEmpty(dst_host):
                    raise Exception("Cannot delete Host-Label:"+dst_host+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(primary_device.device, "wanop_applications"):
            for application in util.convert_to_list(primary_device.device.wanop_applications.wanop_application):
                if hasattr(application, "local_net"):
                    local_net = application.local_net
                    log("In application = " + str(application.name) + " : local_net = " + local_net)
                    if util.isNotEmpty(local_net) and local_net == kwargs["inputdict"]["host_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+local_net+".Because it is being used in the application: "+application.name)
                if hasattr(application, "remote_net"):
                    remote_net = application.remote_net
                    log("In application = " + str(application.name) + " : remote_net = " + remote_net)
                    if util.isNotEmpty(remote_net) and remote_net == kwargs["inputdict"]["host_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+remote_net+".Because it is being used in the application: "+application.name)

        if hasattr(sec_device.device, "wanop_applications"):
            for application in util.convert_to_list(sec_device.device.wanop_applications.wanop_application):
                if hasattr(application, "local_net"):
                    local_net = application.local_net
                    log("In application = " + str(application.name) + " : local_net = " + local_net)
                    if util.isNotEmpty(local_net) and local_net == kwargs["inputdict"]["host_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+local_net+".Because it is being used in the application: "+application.name)
                if hasattr(application, "remote_net"):
                    remote_net = application.remote_net
                    log("In application = " + str(application.name) + " : remote_net = " + remote_net)
                    if util.isNotEmpty(remote_net) and remote_net == kwargs["inputdict"]["host_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+remote_net+".Because it is being used in the application: "+application.name)

    for device in set(dev_object_list):
        url_device_prefix = '/controller:devices/device=%s/wanoptimizer:label-configuration' %(device.device.id)
        device_prefix = yang.Sdk.getData(url_device_prefix, '', sdata.getTaskId())
        conf_prefix = util.parseXmlString(device_prefix)
        log("conf_prefix: "+str(conf_prefix))

        device_pre = []
        if hasattr(conf_prefix.label_configuration, 'host_label'):
            conf_prefix.label_configuration.host_label = util.convert_to_list(conf_prefix.label_configuration.host_label)
            for pre in conf_prefix.label_configuration.host_label:
                device_pre.append(pre.host_label_name)

        if kwargs["inputdict"]["host_label_name"] in device_pre:
            prefix_obj = label_configuration.host_label.host_label()
            prefix_obj.host_label_name = kwargs["inputdict"]["host_label_name"]

            app_url = '/controller:devices/device=%s/wanoptimizer:label-configuration/host-label=%s' %(device.device.id, kwargs["inputdict"]["host_label_name"])
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
            print "Host-Label:%s is not in device:%s"%(kwargs["inputdict"]["host_label_name"],device.device.mgmt_ip_address)


"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_label_configuration_def_host_labels_update_host_label(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_label_configuration_def_host_labels_update_host_label(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_label_configuration_def_domain_labels(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_label_configuration_def_domain_labels(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_label_configuration_def_domain_labels(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
   domain-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/domain-label/domain-label-name
              domain            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/domain-label/domain

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_label_configuration_def_domain_labels_domain_label(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_label_configuration_def_domain_labels_domain_label(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_label_configuration_def_domain_labels_domain_label(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
   domain-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/domain-label/domain-label-name
              domain            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/domain-label/domain
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
def grouping_create_label_configuration_def_domain_labels_update_domain_label(smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs["inputdict"]
    type1_site = inputdict['type1_site']
    type1_sites = inputdict['type1_sites']
    type2_site = inputdict['type2_site']
    type2_sites = inputdict['type2_sites']
    type3_site = inputdict['type3_site']
    type3_sites = inputdict['type3_sites']
    type4_site = inputdict['type4_site']
    type4_sites = inputdict['type4_sites']

    if type1_site and util.isNotEmpty(type1_sites):
        for site in util.convert_to_list(type1_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type1-site/type1-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_domainlabel("type1_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_domainlabel("type1_site", conf, sdata, **kwargs)

    if type2_site and util.isNotEmpty(type2_sites):
        for site in util.convert_to_list(type2_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type2-site/type2-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_domainlabel("type2_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_domainlabel("type2_site", conf, sdata, **kwargs)

    if type3_site and util.isNotEmpty(type3_sites):
        for site in util.convert_to_list(type3_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type3-site/type3-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_domainlabel("type3_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_domainlabel("type3_site", conf, sdata, **kwargs)

    if type4_site and util.isNotEmpty(type4_sites):
        for site in util.convert_to_list(type4_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type4-site/type4-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_domainlabel("type4_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_domainlabel("type4_site", conf, sdata, **kwargs)
    return dev_url
def create_domainlabel(entity, conf, sdata, **kwargs):
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
        sec_device = devicemgr.getDeviceById(sec_device.device.device_ip)
        dev_object_list.append(primary_device)
        dev_object_list.append(sec_device)

    dev_url = []
    for device in set(dev_object_list):
        url_device_prefix = '/controller:devices/device=%s/wanoptimizer:label-configuration' %(device.device.id)
        device_prefix = yang.Sdk.getData(url_device_prefix, '', sdata.getTaskId())
        conf_prefix = util.parseXmlString(device_prefix)
        log("conf_prefix: "+str(conf_prefix))

        device_pre = []
        if hasattr(conf_prefix.label_configuration, 'domain_label'):
            conf_prefix.label_configuration.domain_label = util.convert_to_list(conf_prefix.label_configuration.domain_label)
            for pre in conf_prefix.label_configuration.domain_label:
                device_pre.append(pre.domain_label_name)
        if kwargs["inputdict"]["domain_label_name"] in device_pre:
            dev_url.append(device)
        else:
            print "Domain-Label:%s is not in device:%s"%(kwargs["inputdict"]["domain_label_name"],device.device.mgmt_ip_address)
    return dev_url

def delete_domainlabel(entity, conf, sdata, **kwargs):
    dev_object_list = []
    if entity == "type1_site":
        device = devicemgr.getDeviceById(conf.type1_site.wanop.device_ip)
        log("device object:"+str(device))
        dev_object_list.append(device)
        if hasattr(device.device, "inpath_rules"):
            for rule in util.convert_to_list(device.device.inpath_rules.inpath_rules_def):
                dst_domain = rule.get_field_value("dst_domain")
                if util.isNotEmpty(dst_domain) and dst_domain == kwargs["inputdict"]["domain_label_name"]:
                    raise Exception("Cannot delete Domain-Label:"+dst_domain+".Because it is being used in the inpath-rules: "+rule.rulenum)
    if entity == "type3_site":
        device = devicemgr.getDeviceById(conf.type3_site.wanop.device_ip)
        log("device object:"+str(device))
        dev_object_list.append(device)
        if hasattr(device.device, "inpath_rules"):
            for rule in util.convert_to_list(device.device.inpath_rules.inpath_rules_def):
                dst_domain = rule.get_field_value("dst_domain")
                if util.isNotEmpty(dst_domain) and dst_domain == kwargs["inputdict"]["domain_label_name"]:
                    raise Exception("Cannot delete Domain-Label:"+dst_domain+".Because it is being used in the inpath-rules: "+rule.rulenum)
    if entity == "type2_site":
        primary_device = devicemgr.getDeviceById(conf.type2_site.wanop_primary.device_ip)
        sec_device = devicemgr.getDeviceById(conf.type2_site.wanop_secondary.device_ip)
        dev_object_list.append(primary_device)
        dev_object_list.append(sec_device)

        if hasattr(primary_device.device, "inpath_rules"):
            for rule in util.convert_to_list(primary_device.device.inpath_rules.inpath_rules_def):
                dst_domain = rule.get_field_value("dst_domain")
                if util.isNotEmpty(dst_domain) and dst_domain == kwargs["inputdict"]["domain_label_name"]:
                    raise Exception("Cannot delete Domain-Label:"+dst_domain+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(sec_device.device, "inpath_rules"):
            for rule in util.convert_to_list(sec_device.device.inpath_rules.inpath_rules_def):
                dst_domain = rule.get_field_value("dst_domain")
                if util.isNotEmpty(dst_domain):
                    raise Exception("Cannot delete Domain-Label:"+dst_domain+".Because it is being used in the inpath-rules: "+rule.rulenum)
    if entity == "type4_site":
        primary_device = devicemgr.getDeviceById(conf.type4_site.wanop_primary.device_ip)
        sec_device = devicemgr.getDeviceById(sec_device.device.device_ip)
        dev_object_list.append(primary_device)
        dev_object_list.append(sec_device)

        if hasattr(primary_device.device, "inpath_rules"):
            for rule in util.convert_to_list(primary_device.device.inpath_rules.inpath_rules_def):
                dst_domain = rule.get_field_value("dst_domain")
                if util.isNotEmpty(dst_domain) and dst_domain == kwargs["inputdict"]["domain_label_name"]:
                    raise Exception("Cannot delete Domain-Label:"+dst_domain+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(sec_device.device, "inpath_rules"):
            for rule in util.convert_to_list(sec_device.device.inpath_rules.inpath_rules_def):
                dst_domain = rule.get_field_value("dst_domain")
                if util.isNotEmpty(dst_domain):
                    raise Exception("Cannot delete Domain-Label:"+dst_domain+".Because it is being used in the inpath-rules: "+rule.rulenum)

    for device in set(dev_object_list):
        url_device_prefix = '/controller:devices/device=%s/wanoptimizer:label-configuration' %(device.device.id)
        device_prefix = yang.Sdk.getData(url_device_prefix, '', sdata.getTaskId())
        conf_prefix = util.parseXmlString(device_prefix)
        log("conf_prefix: "+str(conf_prefix))

        device_pre = []
        if hasattr(conf_prefix.label_configuration, 'domain_label'):
            conf_prefix.label_configuration.domain_label = util.convert_to_list(conf_prefix.label_configuration.domain_label)
            for pre in conf_prefix.label_configuration.domain_label:
                device_pre.append(pre.domain_label_name)

        if kwargs["inputdict"]["domain_label_name"] in device_pre:
            prefix_obj = label_configuration.domain_label.domain_label()
            prefix_obj.domain_label_name = kwargs["inputdict"]["domain_label_name"]

            app_url = '/controller:devices/device=%s/wanoptimizer:label-configuration/domain-label=%s' %(device.device.id, kwargs["inputdict"]["domain_label_name"])
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
            print "Domain-Label:%s is not in device:%s"%(kwargs["inputdict"]["domain_label_name"],device.device.mgmt_ip_address)



"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_label_configuration_def_domain_labels_update_domain_label(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_label_configuration_def_domain_labels_update_domain_label(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_label_configuration_def_port_labels(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_label_configuration_def_port_labels(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_label_configuration_def_port_labels(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
     port-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port-label-name
                port            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_label_configuration_def_port_labels_port_label(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_label_configuration_def_port_labels_port_label(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_label_configuration_def_port_labels_port_label(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
     port-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port-label-name
                port            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port
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
def grouping_create_label_configuration_def_port_labels_update_port_label(smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs["inputdict"]
    type1_site = inputdict['type1_site']
    type1_sites = inputdict['type1_sites']
    type2_site = inputdict['type2_site']
    type2_sites = inputdict['type2_sites']
    type3_site = inputdict['type3_site']
    type3_sites = inputdict['type3_sites']
    type4_site = inputdict['type4_site']
    type4_sites = inputdict['type4_sites']

    if type1_site and util.isNotEmpty(type1_sites):
        for site in util.convert_to_list(type1_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type1-site/type1-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_portlabel("type1_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_portlabel("type1_site", conf, sdata, cust_name, **kwargs)

    if type2_site and util.isNotEmpty(type2_sites):
        for site in util.convert_to_list(type2_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type2-site/type2-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_portlabel("type2_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_portlabel("type2_site", conf, sdata, cust_name, **kwargs)

    if type3_site and util.isNotEmpty(type3_sites):
        for site in util.convert_to_list(type3_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type3-site/type3-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_portlabel("type3_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_portlabel("type3_site", conf, sdata, cust_name, **kwargs)

    if type4_site and util.isNotEmpty(type4_sites):
        for site in util.convert_to_list(type4_sites):
            uri = sdata.getRcPath()
            cust_name = uri.split('/')[3].split("=")[1]
            url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/type4-site/type4-site="+str(site)
            site_output = yang.Sdk.getData(url, '', sdata.getTaskId())
            conf = util.parseXmlString(site_output)

            if inputdict['operation'] == 'CREATE':
                dev_url = create_portlabel("type4_site", conf, sdata, **kwargs)
            if inputdict["operation"] == "DELETE":
                dev_url = delete_portlabel("type4_site", conf, sdata, cust_name, **kwargs)
    return dev_url

def create_portlabel(entity, conf, sdata, **kwargs):
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
        url_device_prefix = '/controller:devices/device=%s/wanoptimizer:label-configuration' %(device.device.id)
        device_prefix = yang.Sdk.getData(url_device_prefix, '', sdata.getTaskId())
        conf_prefix = util.parseXmlString(device_prefix)
        log("conf_prefix: "+str(conf_prefix))

        device_pre = []
        if hasattr(conf_prefix.label_configuration, 'port_label'):
            conf_prefix.label_configuration.port_label = util.convert_to_list(conf_prefix.label_configuration.port_label)
            for pre in conf_prefix.label_configuration.port_label:
                device_pre.append(pre.port_label_name)
        if kwargs["inputdict"]["port_label_name"] in device_pre:
            dev_url.append(device)
        else:
            print "Port-Label:%s is not in device:%s"%(kwargs["inputdict"]["port_label_name"],device.device.mgmt_ip_address)
    return dev_url

def delete_portlabel(entity, conf, sdata, cust_name, **kwargs):
    dev_object_list = []
    if entity == "type1_site":
        device = devicemgr.getDeviceById(conf.type1_site.wanop.device_ip)
        log("device object:"+str(device))
        dev_object_list.append(device)
        if hasattr(device.device, "inpath_rules"):
            for rule in util.convert_to_list(device.device.inpath_rules.inpath_rules_def):
                dst_port = rule.get_field_value("dst_port")
                if util.isNotEmpty(dst_port) and dst_port == kwargs["inputdict"]["port_label_name"]:
                    raise Exception("Cannot delete Port-Label:"+dst_port+".Because it is being used in the inpath-rules: "+rule.rulenum)
        if hasattr(device.device, "wanop_applications"):
            for application in util.convert_to_list(device.device.wanop_applications.wanop_application):
                log("Application="+str(application))
                if hasattr(application, "local_port"):
                    local_port = application.local_port
                    log("In application = " + str(application.name) + " : local_port = " + local_port)
                    if util.isNotEmpty(local_port) and local_port == kwargs["inputdict"]["port_label_name"]:
                        raise Exception("Cannot delete port-label:"+local_port+".Because it is being used in the application: "+application.name)
                if hasattr(application, "remote_port"):
                    remote_port = application.remote_port
                    log("In application = " + str(application.name) + " : remote_port = " + remote_port)
                    if util.isNotEmpty(remote_port) and remote_port == kwargs["inputdict"]["port_label_name"]:
                        raise Exception("Cannot delete port-Label:"+remote_port+".Because it is being used in the application: "+application.name)

    if entity == "type3_site":
        device = devicemgr.getDeviceById(conf.type3_site.wanop.device_ip)
        log("device object:"+str(device))
        dev_object_list.append(device)
        if hasattr(device.device, "inpath_rules"):
            for rule in util.convert_to_list(device.device.inpath_rules.inpath_rules_def):
                dst_port = rule.get_field_value("dst_port")
                if util.isNotEmpty(dst_port) and dst_port == kwargs["inputdict"]["port_label_name"]:
                    raise Exception("Cannot delete Port-Label:"+dst_port+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(device.device, "wanop_applications"):
            for application in util.convert_to_list(device.device.wanop_applications.wanop_application):
                log("Application="+str(application))
                url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/applications/application="+str(application.name)
                application_detail = yang.Sdk.getData(url, '', sdata.getTaskId())
                application_parse = util.parseXmlString(application_detail)
                log("application_parse == " + str(application_parse))
                if hasattr(application, "local_port"):
                    local_port = application.local_port
                    log("In application = " + str(application.name) + " : local_port = " + local_port)
                    if util.isNotEmpty(local_port) and local_port == kwargs["inputdict"]["port_label_name"]:
                        raise Exception("Cannot delete Port-Label:"+local_port+".Because it is being used in the application: "+application.name)
                if hasattr(application, "remote_port"):
                    remote_port = application.remote_port
                    log("In application = " + str(application.name) + " : remote_port = " + remote_port)
                    if util.isNotEmpty(remote_port) and remote_port == kwargs["inputdict"]["port_label_name"]:
                        raise Exception("Cannot delete Port-Label:"+remote_port+".Because it is being used in the application: "+application.name)

    if entity == "type2_site":
        primary_device = devicemgr.getDeviceById(conf.type2_site.wanop_primary.device_ip)
        sec_device = devicemgr.getDeviceById(conf.type2_site.wanop_secondary.device_ip)
        dev_object_list.append(primary_device)
        dev_object_list.append(sec_device)

        if hasattr(primary_device.device, "inpath_rules"):
            for rule in util.convert_to_list(primary_device.device.inpath_rules.inpath_rules_def):
                dst_port = rule.get_field_value("dst_port")
                if util.isNotEmpty(dst_port) and dst_port == kwargs["inputdict"]["port_label_name"]:
                    raise Exception("Cannot delete Port-Label:"+dst_port+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(sec_device.device, "inpath_rules"):
            for rule in util.convert_to_list(sec_device.device.inpath_rules.inpath_rules_def):
                dst_port = rule.get_field_value("dst_port")
                if util.isNotEmpty(dst_port):
                    raise Exception("Cannot delete Port-Label:"+dst_port+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(primary_device.device, "wanop_applications"):
            for application in util.convert_to_list(primary_device.device.wanop_applications.wanop_application):
                url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/applications/application="+str(application.name)
                application_detail = yang.Sdk.getData(url, '', sdata.getTaskId())
                application_parse = util.parseXmlString(application_detail)
                log("application_parse == " + str(application_parse))
                if hasattr(application, "local_port"):
                    local_port = application.local_port
                    log("In application = " + str(application.name) + " : local_port = " + local_port)
                    if util.isNotEmpty(local_port) and local_port == kwargs["inputdict"]["port_label_name"]:
                        raise Exception("Cannot delete Port-Label:"+local_port+".Because it is being used in the application: "+application.name)
                if hasattr(application, "remote_port"):
                    remote_port = application.remote_port
                    log("In application = " + str(application.name) + " : remote_port = " + remote_port)
                    if util.isNotEmpty(remote_port) and remote_port == kwargs["inputdict"]["port_label_name"]:
                        raise Exception("Cannot delete Port-Label:"+remote_port+".Because it is being used in the application: "+application.name)


        if hasattr(sec_device.device, "wanop_applications"):
            for application in util.convert_to_list(sec_device.device.wanop_applications.wanop_application):
                url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/applications/application="+str(application.name)
                application_detail = yang.Sdk.getData(url, '', sdata.getTaskId())
                application_parse = util.parseXmlString(application_detail)
                log("application_parse == " + str(application_parse))
                if hasattr(application, "local_port"):
                    local_port = application.local_port
                    log("In application = " + str(application.name) + " : local_port = " + local_port)
                    if util.isNotEmpty(local_port) and local_port == kwargs["inputdict"]["port_label_name"]:
                        raise Exception("Cannot delete Port-Label:"+local_port+".Because it is being used in the application: "+application.name)
                if hasattr(application, "remote_port"):
                    remote_port = application.remote_port
                    log("In application = " + str(application.name) + " : remote_port = " + remote_port)
                    if util.isNotEmpty(remote_port) and remote_port == kwargs["inputdict"]["port_label_name"]:
                        raise Exception("Cannot delete Port-Label:"+remote_port+".Because it is being used in the application: "+application.name)

    if entity == "type4_site":
        primary_device = devicemgr.getDeviceById(conf.type4_site.wanop_primary.device_ip)
        sec_device = devicemgr.getDeviceById(conf.type4_site.wanop_secondary.device_ip)
        dev_object_list.append(primary_device)
        dev_object_list.append(sec_device)

        if hasattr(primary_device.device, "inpath_rules"):
            for rule in util.convert_to_list(primary_device.device.inpath_rules.inpath_rules_def):
                dst_port = rule.get_field_value("dst_port")
                if util.isNotEmpty(dst_port) and dst_port == kwargs["inputdict"]["port_label_name"]:
                    raise Exception("Cannot delete Port-Label:"+dst_port+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(sec_device.device, "inpath_rules"):
            for rule in util.convert_to_list(sec_device.device.inpath_rules.inpath_rules_def):
                dst_port = rule.get_field_value("dst_port")
                if util.isNotEmpty(dst_port):
                    raise Exception("Cannot delete Port-Label:"+dst_port+".Because it is being used in the inpath-rules: "+rule.rulenum)

        if hasattr(primary_device.device, "wanop_applications"):
            for application in util.convert_to_list(primary_device.device.wanop_applications.wanop_application):
                url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/wanop-services/applications/application="+str(application.name)
                application_detail = yang.Sdk.getData(url, '', sdata.getTaskId())
                application_parse = util.parseXmlString(application_detail)
                log("application_parse == " + str(application_parse))
                if hasattr(application, "local_port"):
                    local_port = application.local_port
                    log("In application = " + str(application.name) + " : local_port = " + local_port)
                    if util.isNotEmpty(local_port) and local_port == kwargs["inputdict"]["port_label_name"]:
                        raise Exception("Cannot delete Port-Label:"+local_port+".Because it is being used in the application: "+application.name)
                if hasattr(application, "remote_port"):
                    remote_port = application.remote_port
                    log("In application = " + str(application.name) + " : remote_port = " + remote_port)
                    if util.isNotEmpty(remote_port) and remote_port == kwargs["inputdict"]["port_label_name"]:
                        raise Exception("Cannot delete Port-Label:"+remote_port+".Because it is being used in the application: "+application.name)


        if hasattr(sec_device.device, "wanop_applications"):
            for application in util.convert_to_list(sec_device.device.wanop_applications.wanop_application):
                if hasattr(application, "local_port"):
                    local_port = application.local_port
                    log("In application = " + str(application.name) + " : local_port = " + local_port)
                    if util.isNotEmpty(local_port) and local_port == kwargs["inputdict"]["port_label_name"]:
                        raise Exception("Cannot delete Host-Label:"+local_port+".Because it is being used in the application: "+application.name)
                if hasattr(application, "remote_port"):
                    remote_port = application.remote_port
                    log("In application = " + str(application.name) + " : remote_port = " + remote_port)
                    if util.isNotEmpty(remote_port) and remote_port == kwargs["inputdict"]["port_label_name"]:
                        raise Exception("Cannot delete Port-Label:"+remote_port+".Because it is being used in the application: "+application.name)


    for device in set(dev_object_list):
        url_device_prefix = '/controller:devices/device=%s/wanoptimizer:label-configuration' %(device.device.id)
        device_prefix = yang.Sdk.getData(url_device_prefix, '', sdata.getTaskId())
        conf_prefix = util.parseXmlString(device_prefix)
        log("conf_prefix: "+str(conf_prefix))

        device_pre = []
        if hasattr(conf_prefix.label_configuration, 'port_label'):
            conf_prefix.label_configuration.port_label = util.convert_to_list(conf_prefix.label_configuration.port_label)
            for pre in conf_prefix.label_configuration.port_label:
                device_pre.append(pre.port_label_name)

        if kwargs["inputdict"]["port_label_name"] in device_pre:
            prefix_obj = label_configuration.port_label.port_label()
            prefix_obj.port_label_name = kwargs["inputdict"]["port_label_name"]

            app_url = '/controller:devices/device=%s/wanoptimizer:label-configuration/port-label=%s' %(device.device.id, kwargs["inputdict"]["port_label_name"])
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
            print "Port-Label:%s is not in device:%s"%(kwargs["inputdict"]["port_label_name"],device.device.mgmt_ip_address)


"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_label_configuration_def_port_labels_update_port_label(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_label_configuration_def_port_labels_update_port_label(smodelctx, sdata, **kwargs):
    pass

