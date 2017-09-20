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
                                                                       cpe-primary
                                                                                  |
                                                                                  ip-sla
                                                                                        |
                                                                                        sla
                                                                                           
Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/cpe-primary/ip-sla/sla
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

class Sla(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'sla')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        dev = None
        devbindobjs={}
        inputdict = {}

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['vrf_name'] = config.get_field_value('vrf_name')
        inputdict['entry_number'] = config.get_field_value('entry_number')
        inputdict['operation_type'] = config.get_field_value('operation_type')
        inputdict['destination'] = config.get_field_value('destination')
        inputdict['source'] = config.get_field_value('source')
        inputdict['source_interface_name'] = config.get_field_value('source_interface_name')
        inputdict['source_interface_ip'] = config.get_field_value('source_interface_ip')
        inputdict['data_size'] = config.get_field_value('data_size')
        # if inputdict['data_size'] is None:
        #   inputdict['data_size'] = '500'
        inputdict['frequency'] = config.get_field_value('frequency')
        # if inputdict['frequency'] is None:
        #   inputdict['frequency'] = '3'
        inputdict['timeout'] = config.get_field_value('timeout')
        # if inputdict['timeout'] is None:
        #   inputdict['timeout'] = '2500'
        inputdict['threshold'] = config.get_field_value('threshold')
        # if inputdict['threshold'] is None:
        #   inputdict['threshold'] = '2500'
        inputdict['track_number'] = config.get_field_value('track_number')
        inputdict['response_data_size'] = config.get_field_value('response_data_size')
        inputdict['destination_port'] = config.get_field_value('destination_port')
        inputdict['source_port'] = config.get_field_value('source_port')
        inputdict['interval'] = config.get_field_value('interval')
        inputdict['tos'] = config.get_field_value('tos')
        inputdict['tag'] = config.get_field_value('tag')
        inputdict['history_interval'] = config.get_field_value('history_interval')
        inputdict['buckets_size'] = config.get_field_value('buckets_size')
        inputdict['http_request_type'] = config.get_field_value('http_request_type')
        inputdict['http_url'] = config.get_field_value('http_url')
        inputdict['http_raw_request'] = config.get_field_value('http_raw_request')
        inputdict['num_packets'] = config.get_field_value('num_packets')
        inputdict['delay_down_time'] = config.get_field_value('delay_down_time')
        inputdict['delay_up_time'] = config.get_field_value('delay_up_time')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'cpe-primary')
        device_mgmt_ip_address = _Gen_obj.cpe_primary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        inputkeydict = {}
        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_site_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-6].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, parentobj=parentobj, inputdict=inputdict, config=config)

        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, inputdict=inputdict, parentobj=parentobj, config=config, devbindobjs=devbindobjs)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'sla')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        _Gen_obj = getLocalObject(sdata, 'cpe-primary')
        device_mgmt_ip_address = _Gen_obj.cpe_primary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'sla')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        _Gen_obj = getLocalObject(sdata, 'cpe-primary')
        device_mgmt_ip_address = _Gen_obj.cpe_primary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    @staticmethod
    def getInstance():
        if(Sla._instance == None):
            Sla._instance = Sla()
        return Sla._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)
