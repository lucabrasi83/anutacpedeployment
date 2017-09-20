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
                                                                                             lan
                                                                                                |
                                                                                                switches
                                                                                                        |
                                                                                                        interface
                                                                                                                 
Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/lan/switches/interface
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


class Interface(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'interface', False)

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
        inputdict['sequence_number'] = config.get_field_value('sequence_number')
        if inputdict.get('sequence_number') is None:
          inputdict['sequence_number'] = '133'
        inputdict['name'] = config.get_field_value('name')
        inputdict['interface_type'] = config.get_field_value('interface_type')
        inputdict['interface_name'] = config.get_field_value('interface_name')
        inputdict['vlan_id'] = config.get_field_value('vlan_id')
        inputdict['cidr'] = config.get_field_value('cidr')
        inputdict['interface_ip'] = config.get_field_value('interface_ip')
        inputdict['interface_description'] = config.get_field_value('interface_description')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'switches')
        device_mgmt_ip_address = _Gen_obj.switches.device

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_lan_switches_device'] = sdata.getRcPath().split('/')[-2].split('=')[1]
        inputkeydict['managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_site_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-6].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'interface', False)
        pconfig = getPreviousObjectConfig(id, sdata, 'interface')
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
        inputdict['sequence_number'] = config.get_field_value('sequence_number')
        if inputdict.get('sequence_number') is None:
          inputdict['sequence_number'] = '133'
        inputdict['name'] = config.get_field_value('name')
        inputdict['interface_type'] = config.get_field_value('interface_type')
        inputdict['interface_name'] = config.get_field_value('interface_name')
        inputdict['vlan_id'] = config.get_field_value('vlan_id')
        inputdict['cidr'] = config.get_field_value('cidr')
        inputdict['interface_ip'] = config.get_field_value('interface_ip')
        inputdict['interface_description'] = config.get_field_value('interface_description')
        # END OF FETCHING THE LEAF PARAMETERS

        pinputdict = {}

        # START OF FETCHING THE PREVIOUS LEAF PARAMETERS
        pinputdict['sequence_number'] = pconfig.get_field_value('sequence_number')
        if pinputdict.get('sequence_number') is None:
          pinputdict['sequence_number'] = '133'
        pinputdict['name'] = pconfig.get_field_value('name')
        pinputdict['interface_type'] = pconfig.get_field_value('interface_type')
        pinputdict['interface_name'] = pconfig.get_field_value('interface_name')
        pinputdict['vlan_id'] = pconfig.get_field_value('vlan_id')
        pinputdict['cidr'] = pconfig.get_field_value('cidr')
        pinputdict['interface_ip'] = pconfig.get_field_value('interface_ip')
        pinputdict['interface_description'] = pconfig.get_field_value('interface_description')
        _Gen_obj = getLocalObject(sdata, 'switches')
        device_mgmt_ip_address = _Gen_obj.switches.device

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, pconfig=pconfig, hopaque=opaque_args, inputdict=inputdict, pinputdict=pinputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'interface', False)
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
        inputdict['sequence_number'] = config.get_field_value('sequence_number')
        if inputdict.get('sequence_number') is None:
          inputdict['sequence_number'] = '133'
        inputdict['name'] = config.get_field_value('name')
        inputdict['interface_type'] = config.get_field_value('interface_type')
        inputdict['interface_name'] = config.get_field_value('interface_name')
        inputdict['vlan_id'] = config.get_field_value('vlan_id')
        inputdict['cidr'] = config.get_field_value('cidr')
        inputdict['interface_ip'] = config.get_field_value('interface_ip')
        inputdict['interface_description'] = config.get_field_value('interface_description')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'switches')
        device_mgmt_ip_address = _Gen_obj.switches.device

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(Interface._instance == None):
            Interface._instance = Interface()
        return Interface._instance
