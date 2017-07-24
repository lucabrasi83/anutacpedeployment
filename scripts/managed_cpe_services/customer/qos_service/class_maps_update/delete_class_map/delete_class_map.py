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
                                               class-maps-update
                                                                |
                                                                delete-class-map
                                                                                
Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps-update/delete-class-map
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

class DeleteClassMap(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'delete_class_map')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        dev = []
        devbindobjs={}
        inputdict = {}

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['id'] = config.get_field_value('id')
        inputdict['name'] = config.get_field_value('name')
        inputdict['dscp'] = config.get_field_value('dscp')
        if inputdict['dscp'] is None:
          inputdict['dscp'] = []
        inputdict['access_group'] = config.get_field_value('access_group')
        inputdict['qos_group'] = config.get_field_value('qos_group')
        inputdict['protocol'] = config.get_field_value('protocol')
        if inputdict['protocol'] is None:
          inputdict['protocol'] = []
        inputdict['traffic_class'] = config.get_field_value('traffic_class')
        inputdict['protocol_attribute'] = config.get_field_value('protocol_attribute')
        inputdict['business_relevance'] = config.get_field_value('business_relevance')
        if inputdict['business_relevance'] is None:
          inputdict['business_relevance'] = 'True'
        inputdict['pre_configured'] = config.get_field_value('pre_configured')
        inputdict['single_cpe_site'] = config.get_field_value('single_cpe_site')
        inputdict['single_cpe_sites'] = config.get_field_value('single_cpe_sites')
        if inputdict['single_cpe_sites'] is None:
          inputdict['single_cpe_sites'] = '[]'
        inputdict['dual_cpe_site'] = config.get_field_value('dual_cpe_site')
        inputdict['dual_cpe_sites'] = config.get_field_value('dual_cpe_sites')
        if inputdict['dual_cpe_sites'] is None:
          inputdict['dual_cpe_sites'] = '[]'
        inputdict['single_cpe_dual_wan_site'] = config.get_field_value('single_cpe_dual_wan_site')
        inputdict['single_cpe_dual_wan_sites'] = config.get_field_value('single_cpe_dual_wan_sites')
        if inputdict['single_cpe_dual_wan_sites'] is None:
          inputdict['single_cpe_dual_wan_sites'] = '[]'
        inputdict['triple_cpe_site'] = config.get_field_value('triple_cpe_site')
        inputdict['triple_cpe_sites'] = config.get_field_value('triple_cpe_sites')
        if inputdict.get('triple_cpe_sites') is None:
            inputdict['triple_cpe_sites'] = '[]'
        inputdict['dual_cpe_dual_wan_site'] = config.get_field_value('dual_cpe_dual_wan_site')
        inputdict['dual_cpe_dual_wan_sites'] = config.get_field_value('dual_cpe_dual_wan_sites')
        if inputdict.get('dual_cpe_dual_wan_sites') is None:
            inputdict['dual_cpe_dual_wan_sites'] = '[]'
        # END OF FETCHING THE LEAF PARAMETERS

        inputkeydict = {}
        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        #inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, device=dev, parentobj=parentobj, inputdict=inputdict, config=config)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'delete_class_map')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = getParentObject(sdata)
        dev = []
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'delete_class_map')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = getParentObject(sdata)
        dev = []
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    @staticmethod
    def getInstance():
        if(DeleteClassMap._instance == None):
            DeleteClassMap._instance = DeleteClassMap()
        return DeleteClassMap._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)
