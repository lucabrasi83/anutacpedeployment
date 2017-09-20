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
                                                                                             failover-fallback-service
                                                                                                                      |
                                                                                                                      failover-fallback
                                                                                                                                       
Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/failover-fallback-service/failover-fallback
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


class FailoverFallback(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'failover_fallback', False)

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
          inputdict['sequence_number'] = '89'
        inputdict['name'] = config.get_field_value('name')
        inputdict['device'] = config.get_field_value('device')
        inputdict['cpe_primary_wan_neighbor'] = config.get_field_value('cpe_primary_wan_neighbor')
        inputdict['cpe_secondary_wan_neighbor'] = config.get_field_value('cpe_secondary_wan_neighbor')
        inputdict['failover_wan'] = config.get_field_value('failover_wan')
        inputdict['fallback_wan'] = config.get_field_value('fallback_wan')
        inputdict['failover_lan'] = config.get_field_value('failover_lan')
        inputdict['fallback_lan'] = config.get_field_value('fallback_lan')
        # END OF FETCHING THE LEAF PARAMETERS

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_site_name'] = sdata.getRcPath().split('/')[-3].split('=')[1]
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-5].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'failover_fallback', False)
        pconfig = getPreviousObjectConfig(id, sdata, 'failover_fallback')
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
          inputdict['sequence_number'] = '89'
        inputdict['name'] = config.get_field_value('name')
        inputdict['device'] = config.get_field_value('device')
        inputdict['cpe_primary_wan_neighbor'] = config.get_field_value('cpe_primary_wan_neighbor')
        inputdict['cpe_secondary_wan_neighbor'] = config.get_field_value('cpe_secondary_wan_neighbor')
        inputdict['failover_wan'] = config.get_field_value('failover_wan')
        inputdict['fallback_wan'] = config.get_field_value('fallback_wan')
        inputdict['failover_lan'] = config.get_field_value('failover_lan')
        inputdict['fallback_lan'] = config.get_field_value('fallback_lan')
        # END OF FETCHING THE LEAF PARAMETERS

        pinputdict = {}

        # START OF FETCHING THE PREVIOUS LEAF PARAMETERS
        pinputdict['sequence_number'] = pconfig.get_field_value('sequence_number')
        if pinputdict.get('sequence_number') is None:
          pinputdict['sequence_number'] = '89'
        pinputdict['name'] = pconfig.get_field_value('name')
        pinputdict['device'] = pconfig.get_field_value('device')
        pinputdict['cpe_primary_wan_neighbor'] = pconfig.get_field_value('cpe_primary_wan_neighbor')
        pinputdict['cpe_secondary_wan_neighbor'] = pconfig.get_field_value('cpe_secondary_wan_neighbor')
        pinputdict['failover_wan'] = pconfig.get_field_value('failover_wan')
        pinputdict['fallback_wan'] = pconfig.get_field_value('fallback_wan')
        pinputdict['failover_lan'] = pconfig.get_field_value('failover_lan')
        pinputdict['fallback_lan'] = pconfig.get_field_value('fallback_lan')
        dev = []
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, pconfig=pconfig, hopaque=opaque_args, inputdict=inputdict, pinputdict=pinputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'failover_fallback', False)
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
          inputdict['sequence_number'] = '89'
        inputdict['name'] = config.get_field_value('name')
        inputdict['device'] = config.get_field_value('device')
        inputdict['cpe_primary_wan_neighbor'] = config.get_field_value('cpe_primary_wan_neighbor')
        inputdict['cpe_secondary_wan_neighbor'] = config.get_field_value('cpe_secondary_wan_neighbor')
        inputdict['failover_wan'] = config.get_field_value('failover_wan')
        inputdict['fallback_wan'] = config.get_field_value('fallback_wan')
        inputdict['failover_lan'] = config.get_field_value('failover_lan')
        inputdict['fallback_lan'] = config.get_field_value('fallback_lan')
        # END OF FETCHING THE LEAF PARAMETERS

        dev = []
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(FailoverFallback._instance == None):
            FailoverFallback._instance = FailoverFallback()
        return FailoverFallback._instance