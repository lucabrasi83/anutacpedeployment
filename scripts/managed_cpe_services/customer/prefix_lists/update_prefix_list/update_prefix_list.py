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
#DO NOT EDIT THIS FILE ITS AUTOGENERATED ONE
#ALL THE CUSTOMIZATIONS REGARDING DATAPROCESSING SHOULD BE WRITTEN INTO service_customization.py FILE
#
"""
Tree Structure of Handled XPATH:

services
        |
        managed-cpe-services
                            |
                            customer
                                    |
                                    prefix-lists
                                                |
                                                update-prefix-list
                                                                  
Schema Representation:

/services/managed-cpe-services/customer/prefix-lists/update-prefix-list
"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject
from cpedeployment.cpedeployment_lib import log

from servicemodel.controller import devices
import service_customization


class UpdatePrefixList(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'update_prefix_list')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['id'] = config.get_field_value('id')
        inputdict['prefix_list_name'] = config.get_field_value('prefix_list_name')
        inputdict['operation'] = config.get_field_value('operation')
        inputdict['prefix_name'] = config.get_field_value('prefix_name')
        inputdict['rule_num'] = config.get_field_value('rule_num')
        inputdict['ipv4_prefix'] = config.get_field_value('ipv4_prefix')
        inputdict['condition'] = config.get_field_value('condition')
        inputdict['exact_matching_prefix_length'] = config.get_field_value('exact_matching_prefix_length')
        inputdict['minimum_matching_prefix_length'] = config.get_field_value('minimum_matching_prefix_length')
        inputdict['maximum_matching_prefix_length'] = config.get_field_value('maximum_matching_prefix_length')
        inputdict['single_cpe_site'] = config.get_field_value('single_cpe_site')
        inputdict['single_cpe_sites'] = config.get_field_value('single_cpe_sites')
        if inputdict.get('single_cpe_sites') is None:
          inputdict['single_cpe_sites'] = '[]'
        inputdict['dual_cpe_site'] = config.get_field_value('dual_cpe_site')
        inputdict['dual_cpe_sites'] = config.get_field_value('dual_cpe_sites')
        if inputdict.get('dual_cpe_sites') is None:
          inputdict['dual_cpe_sites'] = '[]'
        inputdict['single_cpe_dual_wan_site'] = config.get_field_value('single_cpe_dual_wan_site')
        inputdict['single_cpe_dual_wan_sites'] = config.get_field_value('single_cpe_dual_wan_sites')
        if inputdict.get('single_cpe_dual_wan_sites') is None:
          inputdict['single_cpe_dual_wan_sites'] = '[]'
        inputdict['triple_cpe_site'] = config.get_field_value('triple_cpe_site')
        inputdict['triple_cpe_sites'] = config.get_field_value('triple_cpe_sites')
        if inputdict.get('triple_cpe_sites') is None:
            inputdict['triple_cpe_sites'] = '[]'
        inputdict['dual_cpe_dual_wan_site'] = config.get_field_value('dual_cpe_dual_wan_site')
        inputdict['dual_cpe_dual_wan_sites'] = config.get_field_value('dual_cpe_dual_wan_sites')
        if inputdict.get('dual_cpe_dual_wan_sites') is None:
            inputdict['dual_cpe_dual_wan_sites'] = '[]'
        # END OF FETCHING THE LEAF PARAMETERS

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        #inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-3].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)

        #Start of Device binding with python bindings
        #End of Device binding
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'update_prefix_list')
        opaque_args = self.opaque_args

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['id'] = config.get_field_value('id')
        inputdict['prefix_list_name'] = config.get_field_value('prefix_list_name')
        inputdict['operation'] = config.get_field_value('operation')
        inputdict['prefix_name'] = config.get_field_value('prefix_name')
        inputdict['rule_num'] = config.get_field_value('rule_num')
        inputdict['ipv4_prefix'] = config.get_field_value('ipv4_prefix')
        inputdict['condition'] = config.get_field_value('condition')
        inputdict['exact_matching_prefix_length'] = config.get_field_value('exact_matching_prefix_length')
        inputdict['minimum_matching_prefix_length'] = config.get_field_value('minimum_matching_prefix_length')
        inputdict['maximum_matching_prefix_length'] = config.get_field_value('maximum_matching_prefix_length')
        inputdict['single_cpe_site'] = config.get_field_value('single_cpe_site')
        inputdict['single_cpe_sites'] = config.get_field_value('single_cpe_sites')
        if inputdict.get('single_cpe_sites') is None:
          inputdict['single_cpe_sites'] = '[]'
        inputdict['dual_cpe_site'] = config.get_field_value('dual_cpe_site')
        inputdict['dual_cpe_sites'] = config.get_field_value('dual_cpe_sites')
        if inputdict.get('dual_cpe_sites') is None:
          inputdict['dual_cpe_sites'] = '[]'
        inputdict['single_cpe_dual_wan_site'] = config.get_field_value('single_cpe_dual_wan_site')
        inputdict['single_cpe_dual_wan_sites'] = config.get_field_value('single_cpe_dual_wan_sites')
        if inputdict.get('single_cpe_dual_wan_sites') is None:
          inputdict['single_cpe_dual_wan_sites'] = '[]'
        inputdict['triple_cpe_site'] = config.get_field_value('triple_cpe_site')
        inputdict['triple_cpe_sites'] = config.get_field_value('triple_cpe_sites')
        if inputdict.get('triple_cpe_sites') is None:
            inputdict['triple_cpe_sites'] = '[]'
        inputdict['dual_cpe_dual_wan_site'] = config.get_field_value('dual_cpe_dual_wan_site')
        inputdict['dual_cpe_dual_wan_sites'] = config.get_field_value('dual_cpe_dual_wan_sites')
        if inputdict.get('dual_cpe_dual_wan_sites') is None:
            inputdict['dual_cpe_dual_wan_sites'] = '[]'
        # END OF FETCHING THE LEAF PARAMETERS
        dev = []
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'update_prefix_list')
        opaque_args = self.opaque_args

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['id'] = config.get_field_value('id')
        inputdict['prefix_list_name'] = config.get_field_value('prefix_list_name')
        inputdict['operation'] = config.get_field_value('operation')
        inputdict['prefix_name'] = config.get_field_value('prefix_name')
        inputdict['rule_num'] = config.get_field_value('rule_num')
        inputdict['ipv4_prefix'] = config.get_field_value('ipv4_prefix')
        inputdict['condition'] = config.get_field_value('condition')
        inputdict['exact_matching_prefix_length'] = config.get_field_value('exact_matching_prefix_length')
        inputdict['minimum_matching_prefix_length'] = config.get_field_value('minimum_matching_prefix_length')
        inputdict['maximum_matching_prefix_length'] = config.get_field_value('maximum_matching_prefix_length')
        inputdict['single_cpe_site'] = config.get_field_value('single_cpe_site')
        inputdict['single_cpe_sites'] = config.get_field_value('single_cpe_sites')
        if inputdict.get('single_cpe_sites') is None:
          inputdict['single_cpe_sites'] = '[]'
        inputdict['dual_cpe_site'] = config.get_field_value('dual_cpe_site')
        inputdict['dual_cpe_sites'] = config.get_field_value('dual_cpe_sites')
        if inputdict.get('dual_cpe_sites') is None:
          inputdict['dual_cpe_sites'] = '[]'
        inputdict['single_cpe_dual_wan_site'] = config.get_field_value('single_cpe_dual_wan_site')
        inputdict['single_cpe_dual_wan_sites'] = config.get_field_value('single_cpe_dual_wan_sites')
        if inputdict.get('single_cpe_dual_wan_sites') is None:
          inputdict['single_cpe_dual_wan_sites'] = '[]'
        inputdict['triple_cpe_site'] = config.get_field_value('triple_cpe_site')
        inputdict['triple_cpe_sites'] = config.get_field_value('triple_cpe_sites')
        if inputdict.get('triple_cpe_sites') is None:
            inputdict['triple_cpe_sites'] = '[]'
        inputdict['dual_cpe_dual_wan_site'] = config.get_field_value('dual_cpe_dual_wan_site')
        inputdict['dual_cpe_dual_wan_sites'] = config.get_field_value('dual_cpe_dual_wan_sites')
        if inputdict.get('dual_cpe_dual_wan_sites') is None:
            inputdict['dual_cpe_dual_wan_sites'] = '[]'
        # END OF FETCHING THE LEAF PARAMETERS
        dev = []
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(UpdatePrefixList._instance == None):
            UpdatePrefixList._instance = UpdatePrefixList()
        return UpdatePrefixList._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)

if __name__ == 'update_prefix_list':
  from servicemodel.yang import YangServiceData
  sdata = YangServiceData()
  instance = UpdatePrefixList().getInstance()
  instance.create(None, sdata)
  instance.delete(None, sdata)
  instance.update(None, sdata)
