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
                                    qos-service
                                               |
                                               class-maps
                                                         |
                                                         class-map
                                                                  
Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps/class-map
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


import service_customization

class ClassMap(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'class_map')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        dev = None
        devbindobjs={}
        inputdict = {}

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['name'] = config.get_field_value('name')
        inputdict['description'] = config.get_field_value('description')
        inputdict['match_type'] = config.get_field_value('match_type')
        if inputdict['match_type'] is None:
          inputdict['match_type'] = 'match-any'
        inputdict['dscp'] = config.get_field_value('dscp')
        if inputdict['dscp'] is None:
          inputdict['dscp'] = '[]'
        inputdict['access_group'] = config.get_field_value('access_group')
        if inputdict['access_group'] is None:
          inputdict['access_group'] = 'ACL'
        inputdict['qos_group'] = config.get_field_value('qos_group')
        inputdict['custom_nbar'] = config.get_field_value('custom_nbar')
        inputdict['protocol'] = config.get_field_value('protocol')
        if inputdict['protocol'] is None:
          inputdict['protocol'] = '[]'
        inputdict['traffic_class'] = config.get_field_value('traffic_class')
        inputdict['protocol_attribute'] = config.get_field_value('protocol_attribute')
        inputdict['business_relevance'] = config.get_field_value('business_relevance')
        if inputdict['business_relevance'] is None:
          inputdict['business_relevance'] = 'True'
        inputdict['pre_configured'] = config.get_field_value('pre_configured')
        # END OF FETCHING THE LEAF PARAMETERS

        inputkeydict = {}
        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, parentobj=parentobj, inputdict=inputdict, config=config)

        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, inputdict=inputdict, parentobj=parentobj, config=config, devbindobjs=devbindobjs)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'class_map')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None
        dev = None
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'class_map')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None
        dev = None
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    @staticmethod
    def getInstance():
        if(ClassMap._instance == None):
            ClassMap._instance = ClassMap()
        return ClassMap._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)
