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
                                    single-cpe-site
                                                   |
                                                   single-cpe-site-services
                                                                           |
                                                                           cpe-lan
                                                                                  |
                                                                                  end-points
                                                                                            |
                                                                                            eigrp
                                                                                                 |
                                                                                                 summary-network
                                                                                                                
Schema Representation:

/services/managed-cpe-services/customer/single-cpe-site/single-cpe-site-services/cpe-lan/end-points/eigrp/summary-network
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


class SummaryNetwork(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'summary_network', False)

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
        inputdict['prefix'] = config.get_field_value('prefix')
        inputdict['summary_metric'] = config.get_field_value('summary_metric')
        inputdict['bandwidth_metric'] = config.get_field_value('bandwidth_metric')
        inputdict['delay_metric'] = config.get_field_value('delay_metric')
        inputdict['reliability_metric'] = config.get_field_value('reliability_metric')
        inputdict['load_metric'] = config.get_field_value('load_metric')
        inputdict['mtu'] = config.get_field_value('mtu')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'end-points')
        device_mgmt_ip_address = _Gen_obj.end_points.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_cpe_lan_end_points_eigrp_name'] = sdata.getRcPath().split('/')[-2].split('=')[1]
        inputkeydict['managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_cpe_lan_end_points_endpoint_name'] = sdata.getRcPath().split('/')[-3].split('=')[1]
        inputkeydict['managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_site_name'] = sdata.getRcPath().split('/')[-5].split('=')[1]
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-7].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'summary_network', False)
        pconfig = getPreviousObjectConfig(id, sdata, 'summary_network')
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
        inputdict['prefix'] = config.get_field_value('prefix')
        inputdict['summary_metric'] = config.get_field_value('summary_metric')
        inputdict['bandwidth_metric'] = config.get_field_value('bandwidth_metric')
        inputdict['delay_metric'] = config.get_field_value('delay_metric')
        inputdict['reliability_metric'] = config.get_field_value('reliability_metric')
        inputdict['load_metric'] = config.get_field_value('load_metric')
        inputdict['mtu'] = config.get_field_value('mtu')
        # END OF FETCHING THE LEAF PARAMETERS

        pinputdict = {}

        # START OF FETCHING THE PREVIOUS LEAF PARAMETERS
        pinputdict['prefix'] = pconfig.get_field_value('prefix')
        pinputdict['summary_metric'] = pconfig.get_field_value('summary_metric')
        pinputdict['bandwidth_metric'] = pconfig.get_field_value('bandwidth_metric')
        pinputdict['delay_metric'] = pconfig.get_field_value('delay_metric')
        pinputdict['reliability_metric'] = pconfig.get_field_value('reliability_metric')
        pinputdict['load_metric'] = pconfig.get_field_value('load_metric')
        pinputdict['mtu'] = pconfig.get_field_value('mtu')
        _Gen_obj = getLocalObject(sdata, 'end-points')
        device_mgmt_ip_address = _Gen_obj.end_points.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, pconfig=pconfig, hopaque=opaque_args, inputdict=inputdict, pinputdict=pinputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'summary_network', False)
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
        inputdict['prefix'] = config.get_field_value('prefix')
        inputdict['summary_metric'] = config.get_field_value('summary_metric')
        inputdict['bandwidth_metric'] = config.get_field_value('bandwidth_metric')
        inputdict['delay_metric'] = config.get_field_value('delay_metric')
        inputdict['reliability_metric'] = config.get_field_value('reliability_metric')
        inputdict['load_metric'] = config.get_field_value('load_metric')
        inputdict['mtu'] = config.get_field_value('mtu')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'end-points')
        device_mgmt_ip_address = _Gen_obj.end_points.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(SummaryNetwork._instance == None):
            SummaryNetwork._instance = SummaryNetwork()
        return SummaryNetwork._instance
