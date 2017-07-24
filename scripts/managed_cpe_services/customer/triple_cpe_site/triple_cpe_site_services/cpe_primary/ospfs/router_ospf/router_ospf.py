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
                                                                           cpe-primary
                                                                                      |
                                                                                      ospfs
                                                                                           |
                                                                                           router-ospf
                                                                                                      
Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-primary/ospfs/router-ospf
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


class RouterOspf(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'router_ospf')

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
        inputdict['process_id'] = config.get_field_value('process_id')
        inputdict['vrf_name'] = config.get_field_value('vrf_name')
        inputdict['router_id'] = config.get_field_value('router_id')
        inputdict['reference_bandwidth'] = config.get_field_value('reference_bandwidth')
        if inputdict.get('reference_bandwidth') is None:
          inputdict['reference_bandwidth'] = '1000'
        inputdict['snmp'] = config.get_field_value('snmp')
        inputdict['context'] = config.get_field_value('context')
        inputdict['community'] = config.get_field_value('community')
        inputdict['access'] = config.get_field_value('access')
        inputdict['global_acl_name'] = config.get_field_value('global_acl_name')
        inputdict['site_acl_name'] = config.get_field_value('site_acl_name')
        inputdict['maximum_paths'] = config.get_field_value('maximum_paths')
        if inputdict.get('maximum_paths') is None:
          inputdict['maximum_paths'] = '1'
        inputdict['default_information'] = config.get_field_value('default_information')
        inputdict['default_inf_metric'] = config.get_field_value('default_inf_metric')
        if inputdict.get('default_inf_metric') is None:
          inputdict['default_inf_metric'] = '500'
        inputdict['default_inf_metric_type'] = config.get_field_value('default_inf_metric_type')
        if inputdict.get('default_inf_metric_type') is None:
          inputdict['default_inf_metric_type'] = '1'
        inputdict['default_inf_route_map'] = config.get_field_value('default_inf_route_map')
        inputdict['distribute_list'] = config.get_field_value('distribute_list')
        inputdict['dis_list_route_map'] = config.get_field_value('dis_list_route_map')
        inputdict['dis_list_route_update'] = config.get_field_value('dis_list_route_update')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'cpe-primary')
        device_mgmt_ip_address = _Gen_obj.cpe_primary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        #inputkeydict['managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_site_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        #inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-6].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)

        #Start of Device binding with python bindings
        #End of Device binding
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'router_ospf')
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
        inputdict['process_id'] = config.get_field_value('process_id')
        inputdict['vrf_name'] = config.get_field_value('vrf_name')
        inputdict['router_id'] = config.get_field_value('router_id')
        inputdict['reference_bandwidth'] = config.get_field_value('reference_bandwidth')
        if inputdict.get('reference_bandwidth') is None:
          inputdict['reference_bandwidth'] = '1000'
        inputdict['snmp'] = config.get_field_value('snmp')
        inputdict['context'] = config.get_field_value('context')
        inputdict['community'] = config.get_field_value('community')
        inputdict['access'] = config.get_field_value('access')
        inputdict['global_acl_name'] = config.get_field_value('global_acl_name')
        inputdict['site_acl_name'] = config.get_field_value('site_acl_name')
        inputdict['maximum_paths'] = config.get_field_value('maximum_paths')
        if inputdict.get('maximum_paths') is None:
          inputdict['maximum_paths'] = '1'
        inputdict['default_information'] = config.get_field_value('default_information')
        inputdict['default_inf_metric'] = config.get_field_value('default_inf_metric')
        if inputdict.get('default_inf_metric') is None:
          inputdict['default_inf_metric'] = '500'
        inputdict['default_inf_metric_type'] = config.get_field_value('default_inf_metric_type')
        if inputdict.get('default_inf_metric_type') is None:
          inputdict['default_inf_metric_type'] = '1'
        inputdict['default_inf_route_map'] = config.get_field_value('default_inf_route_map')
        inputdict['distribute_list'] = config.get_field_value('distribute_list')
        inputdict['dis_list_route_map'] = config.get_field_value('dis_list_route_map')
        inputdict['dis_list_route_update'] = config.get_field_value('dis_list_route_update')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'cpe-primary')
        device_mgmt_ip_address = _Gen_obj.cpe_primary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'router_ospf')
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
        inputdict['process_id'] = config.get_field_value('process_id')
        inputdict['vrf_name'] = config.get_field_value('vrf_name')
        inputdict['router_id'] = config.get_field_value('router_id')
        inputdict['reference_bandwidth'] = config.get_field_value('reference_bandwidth')
        if inputdict.get('reference_bandwidth') is None:
          inputdict['reference_bandwidth'] = '1000'
        inputdict['snmp'] = config.get_field_value('snmp')
        inputdict['context'] = config.get_field_value('context')
        inputdict['community'] = config.get_field_value('community')
        inputdict['access'] = config.get_field_value('access')
        inputdict['global_acl_name'] = config.get_field_value('global_acl_name')
        inputdict['site_acl_name'] = config.get_field_value('site_acl_name')
        inputdict['maximum_paths'] = config.get_field_value('maximum_paths')
        if inputdict.get('maximum_paths') is None:
          inputdict['maximum_paths'] = '1'
        inputdict['default_information'] = config.get_field_value('default_information')
        inputdict['default_inf_metric'] = config.get_field_value('default_inf_metric')
        if inputdict.get('default_inf_metric') is None:
          inputdict['default_inf_metric'] = '500'
        inputdict['default_inf_metric_type'] = config.get_field_value('default_inf_metric_type')
        if inputdict.get('default_inf_metric_type') is None:
          inputdict['default_inf_metric_type'] = '1'
        inputdict['default_inf_route_map'] = config.get_field_value('default_inf_route_map')
        inputdict['distribute_list'] = config.get_field_value('distribute_list')
        inputdict['dis_list_route_map'] = config.get_field_value('dis_list_route_map')
        inputdict['dis_list_route_update'] = config.get_field_value('dis_list_route_update')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'cpe-primary')
        device_mgmt_ip_address = _Gen_obj.cpe_primary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(RouterOspf._instance == None):
            RouterOspf._instance = RouterOspf()
        return RouterOspf._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)

if __name__ == 'router_ospf':
  from servicemodel.yang import YangServiceData
  sdata = YangServiceData()
  instance = RouterOspf().getInstance()
  instance.create(None, sdata)
  instance.delete(None, sdata)
  instance.update(None, sdata)
