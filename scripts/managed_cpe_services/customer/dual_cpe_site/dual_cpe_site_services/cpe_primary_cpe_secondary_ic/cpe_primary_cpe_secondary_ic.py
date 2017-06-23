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
                                                                       cpe-primary-cpe-secondary-ic
                                                                                                   
Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/cpe-primary-cpe-secondary-ic
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

class CpePrimaryCpeSecondaryIc(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'cpe_primary_cpe_secondary_ic')

        #Fetch Service Model Context Object
        smodelctx = ServiceModelContext(id, sdata)

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        dev = None
        devbindobjs={}
        inputdict = {}

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['interconnect_name'] = config.get_field_value('interconnect_name')
        if inputdict['interconnect_name'] is None:
          inputdict['interconnect_name'] = 'cpe-primary-cpe-secondary-ic'
        inputdict['cidr'] = config.get_field_value('cidr')
        inputdict['auto_negotiation'] = config.get_field_value('auto_negotiation')
        if inputdict['auto_negotiation'] is None:
          inputdict['auto_negotiation'] = 'False'
        inputdict['speed'] = config.get_field_value('speed')
        inputdict['duplex'] = config.get_field_value('duplex')
        inputdict['load_interval'] = config.get_field_value('load_interval')
        inputdict['load_interval_delay'] = config.get_field_value('load_interval_delay')
        inputdict['hold_queue_in'] = config.get_field_value('hold_queue_in')
        inputdict['in_queue_length'] = config.get_field_value('in_queue_length')
        inputdict['hold_queue_out'] = config.get_field_value('hold_queue_out')
        inputdict['out_queue_length'] = config.get_field_value('out_queue_length')
        # END OF FETCHING THE LEAF PARAMETERS

        inputkeydict = {}
        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_site_name'] = sdata.getRcPath().split('/')[-2].split('=')[1]
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, parentobj=parentobj, inputdict=inputdict, config=config)

        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, inputdict=inputdict, parentobj=parentobj, config=config, devbindobjs=devbindobjs)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'cpe_primary_cpe_secondary_ic')

        #Fetch Service Model Context Object
        smodelctx = ServiceModelContext(id, sdata)

        #Fetch Parent Object
        parentobj = getParentObject(sdata)
        dev = None
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'cpe_primary_cpe_secondary_ic')

        #Fetch Service Model Context Object
        smodelctx = ServiceModelContext(id, sdata)

        #Fetch Parent Object
        parentobj = getParentObject(sdata)
        dev = None
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    @staticmethod
    def getInstance():
        if(CpePrimaryCpeSecondaryIc._instance == None):
            CpePrimaryCpeSecondaryIc._instance = CpePrimaryCpeSecondaryIc()
        return CpePrimaryCpeSecondaryIc._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)
