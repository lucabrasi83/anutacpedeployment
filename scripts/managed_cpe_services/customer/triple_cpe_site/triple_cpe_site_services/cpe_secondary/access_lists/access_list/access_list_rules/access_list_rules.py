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
                                    triple-cpe-site
                                                   |
                                                   triple-cpe-site-services
                                                                           |
                                                                           cpe-secondary
                                                                                        |
                                                                                        access-lists
                                                                                                    |
                                                                                                    access-list
                                                                                                               |
                                                                                                               access-list-rules
                                                                                                                                
Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-secondary/access-lists/access-list/access-list-rules
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


class AccessListRules(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'access_list_rules')

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
        inputdict['name'] = config.get_field_value('name')
        inputdict['action'] = config.get_field_value('action')
        inputdict['acl_sequence_num'] = config.get_field_value('acl_sequence_num')
        inputdict['protocol'] = config.get_field_value('protocol')
        inputdict['service_obj_name'] = config.get_field_value('service_obj_name')
        inputdict['source_condition'] = config.get_field_value('source_condition')
        inputdict['source_object'] = config.get_field_value('source_object')
        inputdict['source_object_group'] = config.get_field_value('source_object_group')
        inputdict['source_port'] = config.get_field_value('source_port')
        inputdict['destination_condition'] = config.get_field_value('destination_condition')
        inputdict['destination_object'] = config.get_field_value('destination_object')
        inputdict['destination_object_group'] = config.get_field_value('destination_object_group')
        inputdict['port_number'] = config.get_field_value('port_number')
        inputdict['match_packets'] = config.get_field_value('match_packets')
        inputdict['precedence'] = config.get_field_value('precedence')
        inputdict['dscp'] = config.get_field_value('dscp')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'cpe-secondary')
        device_mgmt_ip_address = _Gen_obj.cpe_secondary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        #inputkeydict['managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_secondary_access_lists_access_list_name'] = sdata.getRcPath().split('/')[-2].split('=')[1]
        #inputkeydict['managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_site_name'] = sdata.getRcPath().split('/')[-5].split('=')[1]
        #inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-7].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)

        #Start of Device binding with python bindings
        #End of Device binding
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'access_list_rules')
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
        inputdict['name'] = config.get_field_value('name')
        inputdict['action'] = config.get_field_value('action')
        inputdict['protocol'] = config.get_field_value('protocol')
        inputdict['service_obj_name'] = config.get_field_value('service_obj_name')
        inputdict['source_condition'] = config.get_field_value('source_condition')
        inputdict['source_object'] = config.get_field_value('source_object')
        inputdict['source_object_group'] = config.get_field_value('source_object_group')
        inputdict['source_port'] = config.get_field_value('source_port')
        inputdict['destination_condition'] = config.get_field_value('destination_condition')
        inputdict['destination_object'] = config.get_field_value('destination_object')
        inputdict['destination_object_group'] = config.get_field_value('destination_object_group')
        inputdict['port_number'] = config.get_field_value('port_number')
        inputdict['match_packets'] = config.get_field_value('match_packets')
        inputdict['precedence'] = config.get_field_value('precedence')
        inputdict['dscp'] = config.get_field_value('dscp')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'cpe-secondary')
        device_mgmt_ip_address = _Gen_obj.cpe_secondary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'access_list_rules')
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
        inputdict['name'] = config.get_field_value('name')
        inputdict['action'] = config.get_field_value('action')
        inputdict['protocol'] = config.get_field_value('protocol')
        inputdict['service_obj_name'] = config.get_field_value('service_obj_name')
        inputdict['source_condition'] = config.get_field_value('source_condition')
        inputdict['source_object'] = config.get_field_value('source_object')
        inputdict['source_object_group'] = config.get_field_value('source_object_group')
        inputdict['source_port'] = config.get_field_value('source_port')
        inputdict['destination_condition'] = config.get_field_value('destination_condition')
        inputdict['destination_object'] = config.get_field_value('destination_object')
        inputdict['destination_object_group'] = config.get_field_value('destination_object_group')
        inputdict['port_number'] = config.get_field_value('port_number')
        inputdict['match_packets'] = config.get_field_value('match_packets')
        inputdict['precedence'] = config.get_field_value('precedence')
        inputdict['dscp'] = config.get_field_value('dscp')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'cpe-secondary')
        device_mgmt_ip_address = _Gen_obj.cpe_secondary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(AccessListRules._instance == None):
            AccessListRules._instance = AccessListRules()
        return AccessListRules._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)

if __name__ == 'access_list_rules':
  from servicemodel.yang import YangServiceData
  sdata = YangServiceData()
  instance = AccessListRules().getInstance()
  instance.create(None, sdata)
  instance.delete(None, sdata)
  instance.update(None, sdata)
