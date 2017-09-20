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
                                                                     domain-labels
                                                                                  |
                                                                                  update-domain-label
                                                                                                     
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/domain-labels/update-domain-label
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

def set_specific_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_update_domain_label(input_val, dev, sdata, id, **opaque_args):
  inputdict={}
  inputparent_key_dict={}
  obj = getLocalObject(sdata, 'customer')
  if obj is None:
    sctx = ServiceModelContext(id, sdata)
    sobj = sctx.service_obj
    obj = sobj.managed_cpe_services
  log("customer obj is:%s"%(obj.customer.wanop_services.label_configuration.domain_labels))
  if hasattr(obj.customer.wanop_services.label_configuration.domain_labels, 'update_domain_label'):
    obj.customer.wanop_services.label_configuration.domain_labels.update_domain_label = util.convert_to_list(obj.customer.wanop_services.label_configuration.domain_labels.update_domain_label)
    log("update_domain_label obj is:%s"%(obj.customer.wanop_services.label_configuration.domain_labels.update_domain_label))
    for update_domain_label_obj in obj.customer.wanop_services.label_configuration.domain_labels.update_domain_label:
      key_val = update_domain_label_obj.get_field_value('domain_label_name')
      if input_val == key_val or opaque_args.get('custom_flag_set_all') == True: 
        log("input_val is:%s key_val is %s"%(input_val, key_val))
        top_obj = update_domain_label_obj
        inputdict['domain_label_name'] = update_domain_label_obj.get_field_value('domain_label_name')
        inputdict['domain'] = update_domain_label_obj.get_field_value('domain')
        inputdict['operation'] = update_domain_label_obj.get_field_value('operation')
        inputdict['type1_site'] = update_domain_label_obj.get_field_value('type1_site')
        inputdict['type1_sites'] = update_domain_label_obj.get_field_value('type1_sites')
        inputdict['type2_site'] = update_domain_label_obj.get_field_value('type2_site')
        inputdict['type2_sites'] = update_domain_label_obj.get_field_value('type2_sites')
        inputparent_key_dict['managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_update_domain_label_domain_label_name'] = inputdict.get('domain_label_name')
        #Fetch Local Config Object
        config = {}

        cpedeployment_lib_customization.custom_input_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_update_domain_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args)
        devmapping_dict={}
        mapping_dict_devices_device_label_configuration_domain_label = {}
        mapping_dict_devices_device_label_configuration_domain_label['domain_label_name'] = inputdict['domain_label_name'] if not update else inputdict['domain_label_name'] if inputdict['domain_label_name'] is not None else pinputdict['domain_label_name'] 
        mapping_dict_devices_device_label_configuration_domain_label['domain'] = inputdict['domain'] if not update else inputdict['domain'] if inputdict['domain'] is not None else pinputdict['domain'] 
        devmapping_dict['mapping_dict_devices_device_label_configuration_domain_label'] = mapping_dict_devices_device_label_configuration_domain_label

        cpedeployment_lib_customization.custom_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_update_domain_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devmapping_dict, id, **opaque_args)
        from servicemodel.device_abs_lib import device_label_configuration
        if inputdict['domain_label_name'] is not None and inputdict['domain'] is not None:
                device_label_configuration.label_configuration.domain_label().create(sdata, dev, mapping_dict_devices_device_label_configuration_domain_label, addref=True)
