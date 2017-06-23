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
                                    access-lists
                                                |
                                                update-access-list
                                                                  
Schema Representation:

/services/managed-cpe-services/customer/access-lists/update-access-list
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


class UpdateAccessList(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'update_access_list')

        #Fetch Service Model Context Object
        smodelctx = ServiceModelContext(id, sdata)

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['id'] = config.get_field_value('id')
        inputdict['access_list_name'] = config.get_field_value('access_list_name')
        inputdict['access_list_entry'] = config.get_field_value('access_list_entry')
        inputdict['operation'] = config.get_field_value('operation')
        inputdict['acl_name'] = config.get_field_value('acl_name')
        inputdict['action'] = config.get_field_value('action')
        inputdict['protocol'] = config.get_field_value('protocol')
        inputdict['service_obj_name'] = config.get_field_value('service_obj_name')
        inputdict['source_condition'] = config.get_field_value('source_condition')
        inputdict['source_object'] = config.get_field_value('source_object')
        inputdict['source_object_group'] = config.get_field_value('source_object_group')
        inputdict['destination_condition'] = config.get_field_value('destination_condition')
        inputdict['destination_object'] = config.get_field_value('destination_object')
        inputdict['destination_object_group'] = config.get_field_value('destination_object_group')
        inputdict['port_number'] = config.get_field_value('port_number')
        inputdict['match_packets'] = config.get_field_value('match_packets')
        inputdict['precedence'] = config.get_field_value('precedence')
        inputdict['dscp'] = config.get_field_value('dscp')
        inputdict['source_port'] = config.get_field_value('source_port')
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
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-3].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)

        #Start of Device binding with python bindings
        #End of Device binding
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'update_access_list')
        opaque_args = self.opaque_args

        #Fetch Service Model Context Object
        smodelctx = ServiceModelContext(id, sdata)

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['id'] = config.get_field_value('id')
        inputdict['access_list_name'] = config.get_field_value('access_list_name')
        inputdict['access_list_entry'] = config.get_field_value('access_list_entry')
        inputdict['operation'] = config.get_field_value('operation')
        inputdict['acl_name'] = config.get_field_value('acl_name')
        inputdict['action'] = config.get_field_value('action')
        inputdict['protocol'] = config.get_field_value('protocol')
        inputdict['service_obj_name'] = config.get_field_value('service_obj_name')
        inputdict['source_condition'] = config.get_field_value('source_condition')
        inputdict['source_object'] = config.get_field_value('source_object')
        inputdict['source_object_group'] = config.get_field_value('source_object_group')
        inputdict['destination_condition'] = config.get_field_value('destination_condition')
        inputdict['destination_object'] = config.get_field_value('destination_object')
        inputdict['destination_object_group'] = config.get_field_value('destination_object_group')
        inputdict['port_number'] = config.get_field_value('port_number')
        inputdict['match_packets'] = config.get_field_value('match_packets')
        inputdict['precedence'] = config.get_field_value('precedence')
        inputdict['dscp'] = config.get_field_value('dscp')
        inputdict['source_port'] = config.get_field_value('source_port')
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
        config = getCurrentObjectConfig(id, sdata, 'update_access_list')
        opaque_args = self.opaque_args

        #Fetch Service Model Context Object
        smodelctx = ServiceModelContext(id, sdata)

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['id'] = config.get_field_value('id')
        inputdict['access_list_name'] = config.get_field_value('access_list_name')
        inputdict['access_list_entry'] = config.get_field_value('access_list_entry')
        inputdict['operation'] = config.get_field_value('operation')
        inputdict['acl_name'] = config.get_field_value('acl_name')
        inputdict['action'] = config.get_field_value('action')
        inputdict['protocol'] = config.get_field_value('protocol')
        inputdict['service_obj_name'] = config.get_field_value('service_obj_name')
        inputdict['source_condition'] = config.get_field_value('source_condition')
        inputdict['source_object'] = config.get_field_value('source_object')
        inputdict['source_object_group'] = config.get_field_value('source_object_group')
        inputdict['destination_condition'] = config.get_field_value('destination_condition')
        inputdict['destination_object'] = config.get_field_value('destination_object')
        inputdict['destination_object_group'] = config.get_field_value('destination_object_group')
        inputdict['port_number'] = config.get_field_value('port_number')
        inputdict['match_packets'] = config.get_field_value('match_packets')
        inputdict['precedence'] = config.get_field_value('precedence')
        inputdict['dscp'] = config.get_field_value('dscp')
        inputdict['source_port'] = config.get_field_value('source_port')
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
        if(UpdateAccessList._instance == None):
            UpdateAccessList._instance = UpdateAccessList()
        return UpdateAccessList._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)

if __name__ == 'update_access_list':
  from servicemodel.yang import YangServiceData
  sdata = YangServiceData()
  instance = UpdateAccessList().getInstance()
  instance.create(None, sdata)
  instance.delete(None, sdata)
  instance.update(None, sdata)
