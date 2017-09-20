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
                                    wanop-services
                                                  |
                                                  label-configuration
                                                                     |
                                                                     port-labels
                                                                                |
                                                                                update-port-label
                                                                                                 
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/port-labels/update-port-label
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


class UpdatePortLabel(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'update_port_label')

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
        inputdict['port_label_name'] = config.get_field_value('port_label_name')#leaf port-label-name type False
        inputdict['port'] = config.get_field_value('port')#leaf port type False
        inputdict['operation'] = config.get_field_value('operation')#leaf operation type False
        inputdict['type1_site'] = config.get_field_value('type1_site')#leaf type1-site type False
        inputdict['type1_sites'] = config.get_field_value('type1_sites')#leaf type1-sites type True
        inputdict['type2_site'] = config.get_field_value('type2_site')#leaf type2-site type False
        inputdict['type2_sites'] = config.get_field_value('type2_sites')#leaf type2-sites type True
        inputdict['type3_site'] = config.get_field_value('type3_site')#leaf type3-site type False
        inputdict['type3_sites'] = config.get_field_value('type3_sites')#leaf type3-sites type True
        inputdict['type4_site'] = config.get_field_value('type4_site')#leaf type4-site type False
        inputdict['type4_sites'] = config.get_field_value('type4_sites')#leaf type4-sites type True
        # END OF FETCHING THE LEAF PARAMETERS

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-5].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'update_port_label')
        pconfig = getPreviousObjectConfig(id, sdata, 'update_port_label')
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
        inputdict['port_label_name'] = config.get_field_value('port_label_name')#leaf port-label-name type False
        inputdict['port'] = config.get_field_value('port')#leaf port type False
        inputdict['operation'] = config.get_field_value('operation')#leaf operation type False
        inputdict['type1_site'] = config.get_field_value('type1_site')#leaf type1-site type False
        inputdict['type1_sites'] = config.get_field_value('type1_sites')#leaf type1-sites type True
        inputdict['type2_site'] = config.get_field_value('type2_site')#leaf type2-site type False
        inputdict['type2_sites'] = config.get_field_value('type2_sites')#leaf type2-sites type True
        inputdict['type3_site'] = config.get_field_value('type3_site')#leaf type3-site type False
        inputdict['type3_sites'] = config.get_field_value('type3_sites')#leaf type3-sites type True
        inputdict['type4_site'] = config.get_field_value('type4_site')#leaf type4-site type False
        inputdict['type4_sites'] = config.get_field_value('type4_sites')#leaf type4-sites type True
        # END OF FETCHING THE LEAF PARAMETERS

        pinputdict = {}

        # START OF FETCHING THE PREVIOUS LEAF PARAMETERS
        pinputdict['port_label_name'] = pconfig.get_field_value('port_label_name')
        pinputdict['port'] = pconfig.get_field_value('port')
        pinputdict['operation'] = pconfig.get_field_value('operation')
        pinputdict['type1_site'] = pconfig.get_field_value('type1_site')
        pinputdict['type1_sites'] = pconfig.get_field_value('type1_sites')
        pinputdict['type2_site'] = pconfig.get_field_value('type2_site')
        pinputdict['type2_sites'] = pconfig.get_field_value('type2_sites')
        pinputdict['type3_site'] = pconfig.get_field_value('type3_site')#leaf type3-site type False
        pinputdict['type3_sites'] = pconfig.get_field_value('type3_sites')#leaf type3-sites type True
        pinputdict['type4_site'] = pconfig.get_field_value('type4_site')#leaf type4-site type False
        pinputdict['type4_sites'] = pconfig.get_field_value('type4_sites')#leaf type4-sites type True
        dev = []
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, pconfig=pconfig, hopaque=opaque_args, inputdict=inputdict, pinputdict=pinputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'update_port_label')
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
        inputdict['port_label_name'] = config.get_field_value('port_label_name')#leaf port-label-name type False
        inputdict['port'] = config.get_field_value('port')#leaf port type False
        inputdict['operation'] = config.get_field_value('operation')#leaf operation type False
        inputdict['type1_site'] = config.get_field_value('type1_site')#leaf type1-site type False
        inputdict['type1_sites'] = config.get_field_value('type1_sites')#leaf type1-sites type True
        inputdict['type2_site'] = config.get_field_value('type2_site')#leaf type2-site type False
        inputdict['type2_sites'] = config.get_field_value('type2_sites')#leaf type2-sites type True
        inputdict['type3_site'] = config.get_field_value('type3_site')#leaf type3-site type False
        inputdict['type3_sites'] = config.get_field_value('type3_sites')#leaf type3-sites type True
        inputdict['type4_site'] = config.get_field_value('type4_site')#leaf type4-site type False
        inputdict['type4_sites'] = config.get_field_value('type4_sites')#leaf type4-sites type True
        # END OF FETCHING THE LEAF PARAMETERS

        dev = []
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(UpdatePortLabel._instance == None):
            UpdatePortLabel._instance = UpdatePortLabel()
        return UpdatePortLabel._instance
