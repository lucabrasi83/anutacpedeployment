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
                                    single-cpe-dual-wan-site
                                                            |
                                                            single-cpe-dual-wan-site-services
                                                                                             |
                                                                                             cpe-lan
                                                                                                    |
                                                                                                    end-points
                                                                                                              |
                                                                                                              eigrp
                                                                                                                   
Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/cpe-lan/end-points/eigrp
"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import getPreviousObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject
from cpedeployment.cpedeployment_lib import log


import service_customization


class Eigrp(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'eigrp', False)

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['name'] = config.get_field_value('name')
        inputdict['as_number'] = config.get_field_value('as_number')
        inputdict['in_route_map'] = config.get_field_value('in_route_map')
        inputdict['out_route_map'] = config.get_field_value('out_route_map')
        inputdict['passive_interface'] = config.get_field_value('passive_interface')
        inputdict['key_chain'] = config.get_field_value('key_chain')
        inputdict['hello_interval'] = config.get_field_value('hello_interval')
        inputdict['hold_time'] = config.get_field_value('hold_time')
        inputdict['split_horizon'] = config.get_field_value('split_horizon')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'end-points')
        device_mgmt_ip_address = _Gen_obj.end_points.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_cpe_lan_end_points_endpoint_name'] = sdata.getRcPath().split('/')[-2].split('=')[1]
        inputkeydict['managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_site_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-6].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'eigrp', False)
        pconfig = getPreviousObjectConfig(id, sdata, 'eigrp')
        opaque_args = self.opaque_args

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['name'] = config.get_field_value('name')
        inputdict['as_number'] = config.get_field_value('as_number')
        inputdict['in_route_map'] = config.get_field_value('in_route_map')
        inputdict['out_route_map'] = config.get_field_value('out_route_map')
        inputdict['passive_interface'] = config.get_field_value('passive_interface')
        inputdict['key_chain'] = config.get_field_value('key_chain')
        inputdict['hello_interval'] = config.get_field_value('hello_interval')
        inputdict['hold_time'] = config.get_field_value('hold_time')
        inputdict['split_horizon'] = config.get_field_value('split_horizon')
        # END OF FETCHING THE LEAF PARAMETERS

        pinputdict = {}

        # START OF FETCHING THE PREVIOUS LEAF PARAMETERS
        pinputdict['name'] = pconfig.get_field_value('name')
        pinputdict['as_number'] = pconfig.get_field_value('as_number')
        pinputdict['in_route_map'] = pconfig.get_field_value('in_route_map')
        pinputdict['out_route_map'] = pconfig.get_field_value('out_route_map')
        pinputdict['passive_interface'] = pconfig.get_field_value('passive_interface')
        pinputdict['key_chain'] = pconfig.get_field_value('key_chain')
        pinputdict['hello_interval'] = pconfig.get_field_value('hello_interval')
        pinputdict['hold_time'] = pconfig.get_field_value('hold_time')
        pinputdict['split_horizon'] = pconfig.get_field_value('split_horizon')
        _Gen_obj = getLocalObject(sdata, 'end-points')
        device_mgmt_ip_address = _Gen_obj.end_points.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, pconfig=pconfig, hopaque=opaque_args, inputdict=inputdict, pinputdict=pinputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'eigrp', False)
        opaque_args = self.opaque_args

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['name'] = config.get_field_value('name')
        inputdict['as_number'] = config.get_field_value('as_number')
        inputdict['in_route_map'] = config.get_field_value('in_route_map')
        inputdict['out_route_map'] = config.get_field_value('out_route_map')
        inputdict['passive_interface'] = config.get_field_value('passive_interface')
        inputdict['key_chain'] = config.get_field_value('key_chain')
        inputdict['hello_interval'] = config.get_field_value('hello_interval')
        inputdict['hold_time'] = config.get_field_value('hold_time')
        inputdict['split_horizon'] = config.get_field_value('split_horizon')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'end-points')
        device_mgmt_ip_address = _Gen_obj.end_points.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(Eigrp._instance == None):
            Eigrp._instance = Eigrp()
        return Eigrp._instance
