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
                                                  applications
                                                              |
                                                              application
                                                                         
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/applications/application
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

def set_specific_managed_cpe_services_customer_wanop_services_applications_application(input_val, dev, sdata, id, **opaque_args):
  inputdict={}
  inputparent_key_dict={}
  obj = getLocalObject(sdata, 'customer')
  if obj is None:
    sctx = ServiceModelContext(id, sdata)
    sobj = sctx.service_obj
    obj = sobj.managed_cpe_services
  log("customer obj is:%s"%(obj.customer.wanop_services.applications))
  if hasattr(obj.customer.wanop_services.applications, 'application'):
    obj.customer.wanop_services.applications.application = util.convert_to_list(obj.customer.wanop_services.applications.application)
    log("application obj is:%s"%(obj.customer.wanop_services.applications.application))
    for application_obj in obj.customer.wanop_services.applications.application:
      key_val = application_obj.get_field_value('application_name')
      if input_val == key_val or opaque_args.get('custom_flag_set_all') == True: 
        log("input_val is:%s key_val is %s"%(input_val, key_val))
        top_obj = application_obj
        inputdict['application_name'] = application_obj.get_field_value('application_name')
        inputdict['group'] = application_obj.get_field_value('group')
        inputdict['business_crit'] = application_obj.get_field_value('business_crit')
        inputdict['category'] = application_obj.get_field_value('category')
        inputdict['description'] = application_obj.get_field_value('description')
        inputdict['traffic_type'] = application_obj.get_field_value('traffic_type')
        inputdict['transport_prot'] = application_obj.get_field_value('transport_prot')
        inputdict['dscp'] = application_obj.get_field_value('dscp')
        inputdict['vlan'] = application_obj.get_field_value('vlan')
        inputdict['local_port'] = application_obj.get_field_value('local_port')
        inputdict['remote_port'] = application_obj.get_field_value('remote_port')
        inputdict['local_net'] = application_obj.get_field_value('local_net')
        inputdict['remote_net'] = application_obj.get_field_value('remote_net')
        inputdict['app_prot'] = application_obj.get_field_value('app_prot')
        inputparent_key_dict['managed_cpe_services_customer_wanop_services_applications_application_application_name'] = inputdict.get('application_name')
        #Fetch Local Config Object
        config = {}
        config['applications'] = getCurrentObjectConfig(id, sdata, 'applications')
        config['applications'] = getCurrentObjectConfig(id, sdata, 'applications')
        config['applications'] = getCurrentObjectConfig(id, sdata, 'applications')

        cpedeployment_lib_customization.custom_input_managed_cpe_services_customer_wanop_services_applications_application(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args)
        devmapping_dict={}
        mapping_dict_devices_device_wanop_applications_wanop_application = {}
        mapping_dict_devices_device_wanop_applications_wanop_application['traffic_type'] = inputdict['traffic_type']
        mapping_dict_devices_device_wanop_applications_wanop_application['business_crit'] = inputdict['business_crit']
        mapping_dict_devices_device_wanop_applications_wanop_application['dscp'] = inputdict['dscp']
        mapping_dict_devices_device_wanop_applications_wanop_application['remote_net'] = inputdict['remote_net']
        mapping_dict_devices_device_wanop_applications_wanop_application['name'] = inputdict['application_name']
        mapping_dict_devices_device_wanop_applications_wanop_application['remote_port'] = inputdict['remote_port']
        mapping_dict_devices_device_wanop_applications_wanop_application['group'] = inputdict['group']
        mapping_dict_devices_device_wanop_applications_wanop_application['transport_prot'] = inputdict['transport_prot']
        mapping_dict_devices_device_wanop_applications_wanop_application['description'] = inputdict['description']
        mapping_dict_devices_device_wanop_applications_wanop_application['local_port'] = inputdict['local_port']
        mapping_dict_devices_device_wanop_applications_wanop_application['vlan'] = inputdict['vlan']
        mapping_dict_devices_device_wanop_applications_wanop_application['local_net'] = inputdict['local_net']
        mapping_dict_devices_device_wanop_applications_wanop_application['app_prot'] = inputdict['app_prot']
        mapping_dict_devices_device_wanop_applications_wanop_application['category'] = inputdict['category']
        devmapping_dict['mapping_dict_devices_device_wanop_applications_wanop_application'] = mapping_dict_devices_device_wanop_applications_wanop_application

        cpedeployment_lib_customization.custom_managed_cpe_services_customer_wanop_services_applications_application(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devmapping_dict, id, **opaque_args)
        from servicemodel.device_abs_lib import device_wanop_applications
        if inputdict['application_name'] is not None:
          if inputdict.get('local_port') is not None:
            from managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label
            set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label(inputdict.get('local_port'), dev, sdata, id, **opaque_args)

          if inputdict.get('remote_port') is not None:
            from managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label
            set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label(inputdict.get('remote_port'), dev, sdata, id, **opaque_args)

          if inputdict.get('local_net') is not None:
            from managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label
            set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label(inputdict.get('local_net'), dev, sdata, id, **opaque_args)

          if inputdict.get('remote_net') is not None:
            from managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label
            set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label(inputdict.get('remote_net'), dev, sdata, id, **opaque_args)

          device_wanop_applications.wanop_applications.wanop_application().create(sdata, dev, mapping_dict_devices_device_wanop_applications_wanop_application, addref=True)
