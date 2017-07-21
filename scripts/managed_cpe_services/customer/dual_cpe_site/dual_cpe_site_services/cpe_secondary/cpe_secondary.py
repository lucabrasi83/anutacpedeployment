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
                                    dual-cpe-site
                                                 |
                                                 dual-cpe-site-services
                                                                       |
                                                                       cpe-secondary
                                                                                    
Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/cpe-secondary
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

class CpeSecondary(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'cpe_secondary')

        #Fetch Service Model Context Object
        smodelctx = ServiceModelContext(id, sdata)

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        dev = None
        devbindobjs={}
        inputdict = {}

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['vrf_name'] = config.get_field_value('vrf_name')
        inputdict['name'] = config.get_field_value('name')
        if inputdict['name'] is None:
          inputdict['name'] = 'cpe-secondary'
        inputdict['rd'] = config.get_field_value('rd')
        inputdict['device_ip'] = config.get_field_value('device_ip')
        inputdict['bgp_router_id'] = config.get_field_value('bgp_router_id')
        inputdict['redistribute_connected'] = config.get_field_value('redistribute_connected')
        if inputdict['redistribute_connected'] is None:
          inputdict['redistribute_connected'] = 'True'
        inputdict['redistribute_connected_route_policy'] = config.get_field_value('redistribute_connected_route_policy')
        inputdict['interface_name'] = config.get_field_value('interface_name')
        inputdict['redistribute_static'] = config.get_field_value('redistribute_static')
        inputdict['redistribute_static_route_policy'] = config.get_field_value('redistribute_static_route_policy')
        inputdict['aggregate_summary_networks'] = config.get_field_value('aggregate_summary_networks')
        inputdict['summary_networks'] = config.get_field_value('summary_networks')
        # END OF FETCHING THE LEAF PARAMETERS

        #Fetch Device Object
        dev = getDeviceObject(config.get_field_value('device_ip'), sdata)

        inputkeydict = {}
        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        #inputkeydict['managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_site_name'] = sdata.getRcPath().split('/')[-2].split('=')[1]
        #inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, parentobj=parentobj, inputdict=inputdict, config=config)

        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, inputdict=inputdict, parentobj=parentobj, config=config, devbindobjs=devbindobjs)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'cpe_secondary')

        #Fetch Service Model Context Object
        smodelctx = ServiceModelContext(id, sdata)

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        #Fetch Device Object
        dev = getDeviceObject(config.get_field_value('device_ip'), sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'cpe_secondary')

        #Fetch Service Model Context Object
        smodelctx = ServiceModelContext(id, sdata)

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        #Fetch Device Object
        dev = getDeviceObject(config.get_field_value('device_ip'), sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    @staticmethod
    def getInstance():
        if(CpeSecondary._instance == None):
            CpeSecondary._instance = CpeSecondary()
        return CpeSecondary._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)
