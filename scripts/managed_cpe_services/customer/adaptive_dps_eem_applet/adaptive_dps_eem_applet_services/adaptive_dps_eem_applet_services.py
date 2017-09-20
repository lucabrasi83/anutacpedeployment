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
                                    adaptive-dps
                                                |
                                                adaptive-dps
                                                            
Schema Representation:

/services/managed-cpe-services/customer/adaptive-dps/adaptive-dps
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


class AdaptiveDps(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'adaptive_dps_eem_applet_services')

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
        inputdict['applet_name'] = config.get_field_value('applet_name')
#        inputdict['device_ip'] = config.get_field_value('device_ip')
        # END OF FETCHING THE LEAF PARAMETERS

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-3].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'adaptive_dps_eem_applet_services')
        #pconfig = getPreviousObjectConfig(id, sdata, 'adaptive_dps')
        pconfig = config
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
        inputdict['applet_name'] = config.get_field_value('applet_name')
        # END OF FETCHING THE LEAF PARAMETERS

        pinputdict = {}

        # START OF FETCHING THE PREVIOUS LEAF PARAMETERS
        pinputdict['applet_name'] = pconfig.get_field_value('applet_name')
        dev = []
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, parentobj=parentobj, config=config, pconfig=pconfig, hopaque=opaque_args, inputdict=inputdict, pinputdict=pinputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'adaptive_dps_eem_applet_services')
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
        inputdict['applet_name'] = config.get_field_value('applet_name')
        # END OF FETCHING THE LEAF PARAMETERS

        dev = []
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(AdaptiveDps._instance == None):
            AdaptiveDps._instance = AdaptiveDps()
        return AdaptiveDps._instance
