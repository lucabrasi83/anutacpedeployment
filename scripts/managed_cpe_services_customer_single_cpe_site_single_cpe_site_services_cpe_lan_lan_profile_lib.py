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
                                    single-cpe-site
                                                   |
                                                   single-cpe-site-services
                                                                           |
                                                                           cpe-lan
                                                                                  |
                                                                                  lan-profile
                                                                                             
Schema Representation:

/services/managed-cpe-services/customer/single-cpe-site/single-cpe-site-services/cpe-lan/lan-profile
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

def set_specific_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_cpe_lan_lan_profile(input_val, dev, sdata, id, **opaque_args):
  inputdict={}
  inputparent_key_dict={}
  obj = getLocalObject(sdata, 'single-cpe-site-services')
  if obj is None:
    sctx = ServiceModelContext(id, sdata)
    sobj = sctx.service_obj
    obj = sobj.managed_cpe_services.customer.single_cpe_site
  log("single-cpe-site-services obj is:%s"%(obj.single_cpe_site_services.cpe_lan))
  if hasattr(obj.single_cpe_site_services.cpe_lan, 'lan_profile'):
    obj.single_cpe_site_services.cpe_lan.lan_profile = util.convert_to_list(obj.single_cpe_site_services.cpe_lan.lan_profile)
    log("lan_profile obj is:%s"%(obj.single_cpe_site_services.cpe_lan.lan_profile))
    for lan_profile_obj in obj.single_cpe_site_services.cpe_lan.lan_profile:
      key_val = lan_profile_obj.get_field_value('profile_name')
      if input_val == key_val or opaque_args.get('custom_flag_set_all') == True:
        log("input_val is:%s key_val is %s"%(input_val, key_val))
        top_obj = lan_profile_obj
        inputdict['profile_name'] = lan_profile_obj.get_field_value('profile_name')
        inputdict['cidr'] = lan_profile_obj.get_field_value('cidr')
        inputdict['inbound_policy'] = lan_profile_obj.get_field_value('inbound_policy')
        inputdict['hierarchical_inbound_policy'] = lan_profile_obj.get_field_value('hierarchical_inbound_policy')
        inputdict['hierarchical_policy'] = lan_profile_obj.get_field_value('hierarchical_policy')
        inputdict['auto_negotiation'] = lan_profile_obj.get_field_value('auto_negotiation')
        if inputdict['auto_negotiation'] is None:
          inputdict['auto_negotiation'] = 'False'
        inputdict['speed'] = lan_profile_obj.get_field_value('speed')
        inputdict['duplex'] = lan_profile_obj.get_field_value('duplex')
        inputdict['load_interval'] = lan_profile_obj.get_field_value('load_interval')
        inputdict['load_interval_delay'] = lan_profile_obj.get_field_value('load_interval_delay')
        inputdict['hold_queue_in'] = lan_profile_obj.get_field_value('hold_queue_in')
        inputdict['in_queue_length'] = lan_profile_obj.get_field_value('in_queue_length')
        inputdict['hold_queue_out'] = lan_profile_obj.get_field_value('hold_queue_out')
        inputdict['out_queue_length'] = lan_profile_obj.get_field_value('out_queue_length')
        inputparent_key_dict['managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_cpe_lan_lan_profile_profile_name'] = inputdict.get('profile_name')
        #Fetch Local Config Object
        config = {}
        config['wanop_endpoint'] = getCurrentObjectConfig(id, sdata, 'wanop_endpoint')

        cpedeployment_lib_customization.custom_input_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_cpe_lan_lan_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args)
        devmapping_dict={}

        cpedeployment_lib_customization.custom_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_cpe_lan_lan_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devmapping_dict, id, **opaque_args)

        if inputdict.get('inbound_policy') is not None:
          from managed_cpe_services_customer_qos_service_policies_policy_lib import set_specific_managed_cpe_services_customer_qos_service_policies_policy
          set_specific_managed_cpe_services_customer_qos_service_policies_policy(inputdict.get('inbound_policy'), dev, sdata, id, **opaque_args)

        if inputdict.get('hierarchical_policy') is not None:
          from managed_cpe_services_customer_qos_service_hierarchical_policy_policy_lib import set_specific_managed_cpe_services_customer_qos_service_hierarchical_policy_policy
          set_specific_managed_cpe_services_customer_qos_service_hierarchical_policy_policy(inputdict.get('hierarchical_policy'), dev, sdata, id, **opaque_args)