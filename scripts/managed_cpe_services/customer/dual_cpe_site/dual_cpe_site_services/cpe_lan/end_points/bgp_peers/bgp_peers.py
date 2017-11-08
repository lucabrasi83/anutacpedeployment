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
                                                                       cpe-lan
                                                                              |
                                                                              end-points
                                                                                        |
                                                                                        bgp-peers
                                                                                                 
Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/cpe-lan/end-points/bgp-peers
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

class BgpPeers(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'bgp_peers')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        dev = None
        devbindobjs={}
        inputdict = {}

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['BGP_peer_name'] = config.get_field_value('BGP_peer_name')
        #inputdict['peer'] = config.get_field_value('peer')
        inputdict['peer_ip'] = config.get_field_value('peer_ip')
        inputdict['peer_group'] = config.get_field_value('peer_group')
        #inputdict['listen_cidr'] = config.get_field_value('listen_cidr')
        inputdict['peer_description'] = config.get_field_value('peer_description')
        inputdict['remote_as'] = config.get_field_value('remote_as')
        inputdict['password'] = config.get_field_value('password')
        inputdict['import_route_map'] = config.get_field_value('import_route_map')
        inputdict['export_route_map'] = config.get_field_value('export_route_map')
        inputdict['next_hop_self'] = config.get_field_value('next_hop_self')
        inputdict['soft_reconfiguration'] = config.get_field_value('soft_reconfiguration')
        inputdict['default_originate'] = config.get_field_value('default_originate')
        inputdict['default_originate_route_map'] = config.get_field_value('default_originate_route_map')
        inputdict['send_community'] = config.get_field_value('send_community')
        inputdict['encrypted_password'] = config.get_field_value('encrypted_password')
        inputdict['advertisement_interval'] = config.get_field_value('advertisement_interval')
        inputdict['time_in_sec'] = config.get_field_value('time_in_sec')
        if inputdict['time_in_sec'] is None:
          inputdict['time_in_sec'] = '5'
        inputdict['timers'] = config.get_field_value('timers')
        inputdict['keepalive_interval'] = config.get_field_value('keepalive_interval')
        if inputdict['keepalive_interval'] is None:
          inputdict['keepalive_interval'] = '10'
        inputdict['holdtime'] = config.get_field_value('holdtime')
        if inputdict['holdtime'] is None:
          inputdict['holdtime'] = '30'
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'end-points')
        device_mgmt_ip_address = _Gen_obj.end_points.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        inputkeydict = {}
        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_cpe_lan_end_points_endpoint_name'] = sdata.getRcPath().split('/')[-2].split('=')[1]
        inputkeydict['managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_site_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-6].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, parentobj=parentobj, inputdict=inputdict, config=config)

        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, inputdict=inputdict, parentobj=parentobj, config=config, devbindobjs=devbindobjs)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'bgp_peers')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        _Gen_obj = getLocalObject(sdata, 'end-points')
        device_mgmt_ip_address = _Gen_obj.end_points.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'bgp_peers')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        _Gen_obj = getLocalObject(sdata, 'end-points')
        device_mgmt_ip_address = _Gen_obj.end_points.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    @staticmethod
    def getInstance():
        if(BgpPeers._instance == None):
            BgpPeers._instance = BgpPeers()
        return BgpPeers._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)
