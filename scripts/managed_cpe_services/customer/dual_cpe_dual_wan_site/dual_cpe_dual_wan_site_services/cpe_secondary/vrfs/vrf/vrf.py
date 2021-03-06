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
                                    dual-cpe-dual-wan-site
                                                          |
                                                          dual-cpe-dual-wan-site-services
                                                                                         |
                                                                                         cpe-secondary
                                                                                                      |
                                                                                                      vrfs
                                                                                                          |
                                                                                                          vrf
                                                                                                             
Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/cpe-secondary/vrfs/vrf
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


class Vrf(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'vrf')

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
        inputdict['name'] = config.get_field_value('name')
        inputdict['vrf_name'] = config.get_field_value('vrf_name')
        inputdict['bgp_router_id'] = config.get_field_value('bgp_router_id')
        inputdict['bgp_distance'] = config.get_field_value('bgp_distance')
        inputdict['bgp_distance_external'] = config.get_field_value('bgp_distance_external')
        inputdict['bgp_distance_internal'] = config.get_field_value('bgp_distance_internal')
        inputdict['bgp_distance_local'] = config.get_field_value('bgp_distance_local')
        inputdict['bgp_address_family'] = config.get_field_value('bgp_address_family')
        inputdict['bgp_keepalive_timer'] = config.get_field_value('bgp_keepalive_timer')
        inputdict['bgp_holdtime_timer'] = config.get_field_value('bgp_holdtime_timer')
        inputdict['default_information_originate'] = config.get_field_value('default_information_originate')
        inputdict['bgp_community_new'] = config.get_field_value('bgp_community_new')
        inputdict['peer_groups'] = config.get_field_value('peer_group')
        inputdict['peer_group'] = config.get_field_value('peer_group')
        # inputdict['listen_cidr'] = config.get_field_value('listen_cidr')
        inputdict['redistribute_connected'] = config.get_field_value('redistribute_connected')
        if inputdict.get('redistribute_connected') is None:
          inputdict['redistribute_connected'] = 'True'
        inputdict['redistribute_connected_route_policy'] = config.get_field_value('redistribute_connected_route_policy')
        inputdict['redistribute_static'] = config.get_field_value('redistribute_static')
        inputdict['redistribute_static_route_policy'] = config.get_field_value('redistribute_static_route_policy')
        inputdict['aggregate_summary_networks'] = config.get_field_value('aggregate_summary_networks')
        inputdict['summary_networks'] = config.get_field_value('summary_networks')
        inputdict['bgp_settings'] = config.get_field_value('bgp_settings')
        inputdict['bgp_redis_internal'] = config.get_field_value('bgp_redis_internal')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'cpe-secondary')
        device_mgmt_ip_address = _Gen_obj.cpe_secondary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_site_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-6].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)

        #Start of Device binding with python bindings
        #End of Device binding
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'vrf')
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
        inputdict['name'] = config.get_field_value('name')
        inputdict['vrf_name'] = config.get_field_value('vrf_name')
        inputdict['bgp_router_id'] = config.get_field_value('bgp_router_id')
        inputdict['bgp_distance'] = config.get_field_value('bgp_distance')
        inputdict['bgp_distance_external'] = config.get_field_value('bgp_distance_external')
        inputdict['bgp_distance_internal'] = config.get_field_value('bgp_distance_internal')
        inputdict['bgp_distance_local'] = config.get_field_value('bgp_distance_local')
        inputdict['bgp_address_family'] = config.get_field_value('bgp_address_family')
        inputdict['bgp_keepalive_timer'] = config.get_field_value('bgp_keepalive_timer')
        inputdict['bgp_holdtime_timer'] = config.get_field_value('bgp_holdtime_timer')
        inputdict['default_information_originate'] = config.get_field_value('default_information_originate')
        inputdict['bgp_community_new'] = config.get_field_value('bgp_community_new')
        inputdict['peer_groups'] = config.get_field_value('peer_group')
        inputdict['peer_group'] = config.get_field_value('peer_group')
        # inputdict['listen_cidr'] = config.get_field_value('listen_cidr')
        inputdict['redistribute_connected'] = config.get_field_value('redistribute_connected')
        if inputdict.get('redistribute_connected') is None:
          inputdict['redistribute_connected'] = 'True'
        inputdict['redistribute_connected_route_policy'] = config.get_field_value('redistribute_connected_route_policy')
        inputdict['redistribute_static'] = config.get_field_value('redistribute_static')
        inputdict['redistribute_static_route_policy'] = config.get_field_value('redistribute_static_route_policy')
        inputdict['aggregate_summary_networks'] = config.get_field_value('aggregate_summary_networks')
        inputdict['summary_networks'] = config.get_field_value('summary_networks')
        inputdict['bgp_settings'] = config.get_field_value('bgp_settings')
        inputdict['bgp_redis_internal'] = config.get_field_value('bgp_redis_internal')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'cpe-secondary')
        device_mgmt_ip_address = _Gen_obj.cpe_secondary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'vrf')
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
        inputdict['name'] = config.get_field_value('name')
        inputdict['vrf_name'] = config.get_field_value('vrf_name')
        inputdict['bgp_router_id'] = config.get_field_value('bgp_router_id')
        inputdict['bgp_distance'] = config.get_field_value('bgp_distance')
        inputdict['bgp_distance_external'] = config.get_field_value('bgp_distance_external')
        inputdict['bgp_distance_internal'] = config.get_field_value('bgp_distance_internal')
        inputdict['bgp_distance_local'] = config.get_field_value('bgp_distance_local')
        inputdict['bgp_address_family'] = config.get_field_value('bgp_address_family')
        inputdict['bgp_keepalive_timer'] = config.get_field_value('bgp_keepalive_timer')
        inputdict['bgp_holdtime_timer'] = config.get_field_value('bgp_holdtime_timer')
        inputdict['default_information_originate'] = config.get_field_value('default_information_originate')
        inputdict['bgp_community_new'] = config.get_field_value('bgp_community_new')
        inputdict['peer_groups'] = config.get_field_value('peer_group')
        inputdict['peer_group'] = config.get_field_value('peer_group')
        # inputdict['listen_cidr'] = config.get_field_value('listen_cidr')
        inputdict['redistribute_connected'] = config.get_field_value('redistribute_connected')
        if inputdict.get('redistribute_connected') is None:
          inputdict['redistribute_connected'] = 'True'
        inputdict['redistribute_connected_route_policy'] = config.get_field_value('redistribute_connected_route_policy')
        inputdict['redistribute_static'] = config.get_field_value('redistribute_static')
        inputdict['redistribute_static_route_policy'] = config.get_field_value('redistribute_static_route_policy')
        inputdict['aggregate_summary_networks'] = config.get_field_value('aggregate_summary_networks')
        inputdict['summary_networks'] = config.get_field_value('summary_networks')
        inputdict['bgp_settings'] = config.get_field_value('bgp_settings')
        inputdict['bgp_redis_internal'] = config.get_field_value('bgp_redis_internal')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'cpe-secondary')
        device_mgmt_ip_address = _Gen_obj.cpe_secondary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(Vrf._instance == None):
            Vrf._instance = Vrf()
        return Vrf._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)

if __name__ == 'vrf':
  from servicemodel.yang import YangServiceData
  sdata = YangServiceData()
  instance = Vrf().getInstance()
  instance.create(None, sdata)
  instance.delete(None, sdata)
  instance.update(None, sdata)
