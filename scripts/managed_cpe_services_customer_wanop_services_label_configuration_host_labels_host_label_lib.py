#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2016-2017 Anuta Networks, Inc. All Rights Reserved.
#
"""
Tree Structure of Handled XPATH:

services
        |
        managed-cpe-services
                            |
                            customer
                                    |
                                    wanop-services
                                                  |
                                                  label-configuration
                                                                     |
                                                                     host-labels
                                                                                |
                                                                                host-label
                                                                                          
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/host-label
"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr


import copy

from cpedeployment_lib import getLocalObject
from cpedeployment_lib import getDeviceObject
from cpedeployment_lib import getCurrentObjectConfig
from cpedeployment_lib import getPreviousObjectConfig
from cpedeployment_lib import ServiceModelContext
from cpedeployment_lib import getParentObject
from cpedeployment_lib import log
import cpedeployment_lib_customization

def set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label(input_val, dev, sdata, id, **opaque_args):
  inputdict={}
  inputparent_key_dict={}
  obj = getLocalObject(sdata, 'customer')
  if obj is None:
    sctx = ServiceModelContext(id, sdata)
    sobj = sctx.service_obj
    obj = sobj.managed_cpe_services
  if hasattr(obj.customer.wanop_services, "label_configuration") and hasattr(obj.customer.wanop_services.label_configuration, "host_labels"):

      log("customer obj is:%s"%(obj.customer.wanop_services.label_configuration.host_labels))
      if hasattr(obj.customer.wanop_services.label_configuration.host_labels, 'host_label'):
        obj.customer.wanop_services.label_configuration.host_labels.host_label = util.convert_to_list(obj.customer.wanop_services.label_configuration.host_labels.host_label)
        log("host_label obj is:%s"%(obj.customer.wanop_services.label_configuration.host_labels.host_label))
        for host_label_obj in obj.customer.wanop_services.label_configuration.host_labels.host_label:
          key_val = host_label_obj.get_field_value('host_label_name')
          if input_val == key_val or opaque_args.get('custom_flag_set_all') == True:
            log("input_val is:%s key_val is %s"%(input_val, key_val))
            top_obj = host_label_obj
            inputdict['host_label_name'] = host_label_obj.get_field_value('host_label_name')
            inputparent_key_dict['managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_host_label_name'] = inputdict.get('host_label_name')
            #Fetch Local Config Object
            config = {}
            config['inpath_rules'] = getCurrentObjectConfig(id, sdata, 'inpath_rules')
            config['inpath_rules'] = getCurrentObjectConfig(id, sdata, 'inpath_rules')
            config['inpath_rules'] = getCurrentObjectConfig(id, sdata, 'inpath_rules')

            cpedeployment_lib_customization.custom_input_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args)
            devmapping_dict={}
            mapping_dict_devices_device_label_configuration_host_label = {}
            mapping_dict_devices_device_label_configuration_host_label['host_label_name'] = inputdict['host_label_name']
            devmapping_dict['mapping_dict_devices_device_label_configuration_host_label'] = mapping_dict_devices_device_label_configuration_host_label

            cpedeployment_lib_customization.custom_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devmapping_dict, id, **opaque_args)
            from servicemodel.device_abs_lib import device_label_configuration
            if inputdict['host_label_name'] is not None:
                    device_label_configuration.label_configuration.host_label().create(sdata, dev, mapping_dict_devices_device_label_configuration_host_label, addref=True)

            if hasattr(host_label_obj,'hostname'):
              if cpedeployment_lib_customization.check_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_hostname_1(dev, sdata, inputdict, host_label_obj, top_obj, config, devmapping_dict, id, **opaque_args):
                managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_hostname_1(dev, sdata, inputparent_key_dict, host_label_obj, top_obj, id, config, **opaque_args)

            if hasattr(host_label_obj,'subnet'):
              if cpedeployment_lib_customization.check_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_subnet_1(dev, sdata, inputdict, host_label_obj, top_obj, config, devmapping_dict, id, **opaque_args):
                managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_subnet_1(dev, sdata, inputparent_key_dict, host_label_obj, top_obj, id, config, **opaque_args)

def managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_hostname_1(dev, sdata, inputparent_key_dict, obj, top_obj, id, config, **opaque_args):
    inputdict=copy.deepcopy(inputparent_key_dict)
    log("hostname obj is:%s"%(obj.hostname))
    hostname_obj = obj.hostname
    inputdict['hostname'] = hostname_obj.get_field_value('hostname')

    cpedeployment_lib_customization.custom_input_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_hostname_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args)

    devmapping_dict={}
    mapping_dict_devices_device_label_configuration_host_label_hostname = {}
    mapping_dict_devices_device_label_configuration_host_label_hostname['hostname'] = inputdict['hostname']
    devmapping_dict['mapping_dict_devices_device_label_configuration_host_label_hostname'] = mapping_dict_devices_device_label_configuration_host_label_hostname

    cpedeployment_lib_customization.custom_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_hostname_1(dev, sdata, inputdict, top_obj, config, devmapping_dict, id, **opaque_args)
    from servicemodel.device_abs_lib import device_label_configuration
    if inputdict['managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_host_label_name'] is not None:
        device_label_configuration.label_configuration.host_label.hostname().create(sdata, dev, inputdict['managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_host_label_name'], mapping_dict_devices_device_label_configuration_host_label_hostname, addref=True)

def managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_subnet_1(dev, sdata, inputparent_key_dict, obj, top_obj, id, config, **opaque_args):
    inputdict=copy.deepcopy(inputparent_key_dict)
    log("subnet obj is:%s"%(obj.subnet))
    subnet_obj = obj.subnet
    inputdict['subnet'] = subnet_obj.get_field_value('subnet')

    cpedeployment_lib_customization.custom_input_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_subnet_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args)

    devmapping_dict={}
    mapping_dict_devices_device_label_configuration_host_label_subnet = {}
    mapping_dict_devices_device_label_configuration_host_label_subnet['subnet'] = inputdict['subnet']
    devmapping_dict['mapping_dict_devices_device_label_configuration_host_label_subnet'] = mapping_dict_devices_device_label_configuration_host_label_subnet

    cpedeployment_lib_customization.custom_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_subnet_1(dev, sdata, inputdict, top_obj, config, devmapping_dict, id, **opaque_args)
    from servicemodel.device_abs_lib import device_label_configuration
    if inputdict['managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_host_label_name'] is not None:
        device_label_configuration.label_configuration.host_label.subnet().create(sdata, dev, inputdict['managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_host_label_name'], mapping_dict_devices_device_label_configuration_host_label_subnet, addref=True)
