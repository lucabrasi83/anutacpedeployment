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
                                                                                         cpe-secondary-inet-wan
                                                                                                               |
                                                                                                               end-points
                                                                                                                         
Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/cpe-secondary-inet-wan/end-points
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


class EndPoints(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'end_points')

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
        inputdict['endpoint_name'] = config.get_field_value('endpoint_name')
        inputdict['device_ip'] = config.get_field_value('device_ip')
        inputdict['fvrf'] = config.get_field_value('fvrf')
        inputdict['ivrf'] = config.get_field_value('ivrf')
        inputdict['vrf'] = config.get_field_value('vrf')
        inputdict['interface_type'] = config.get_field_value('interface_type')
        inputdict['interface_name'] = config.get_field_value('interface_name')
        inputdict['vlan_id'] = config.get_field_value('vlan_id')
        inputdict['interface_description'] = config.get_field_value('interface_description')
        inputdict['inbound_acl'] = config.get_field_value('inbound_acl')
        inputdict['global_inbound_acl'] = config.get_field_value('global_inbound_acl')
        inputdict['site_inbound_acl'] = config.get_field_value('site_inbound_acl')
        inputdict['outbound_acl'] = config.get_field_value('outbound_acl')
        inputdict['global_outbound_acl'] = config.get_field_value('global_outbound_acl')
        inputdict['site_outbound_acl'] = config.get_field_value('site_outbound_acl')
        inputdict['dmvpn_profile'] = config.get_field_value('dmvpn_profile')
        inputdict['p2p'] = config.get_field_value('p2p')
        inputdict['tunnel_interface_ip_address'] = config.get_field_value('tunnel_interface_ip_address')
        inputdict['tunnel_interface_mask'] = config.get_field_value('tunnel_interface_mask')
        inputdict['tunnel_interface_id'] = config.get_field_value('tunnel_interface_id')
        inputdict['tunnel_interface_destination'] = config.get_field_value('tunnel_interface_destination')
        inputdict['tunnel_source'] = config.get_field_value('tunnel_source')
        inputdict['tunnel_bandwidth'] = config.get_field_value('tunnel_bandwidth')
        inputdict['nat_outside'] = config.get_field_value('nat_outside')
        inputdict['nat_inside'] = config.get_field_value('nat_inside')
        inputdict['tunnel_mss'] = config.get_field_value('tunnel_mss')
        # END OF FETCHING THE LEAF PARAMETERS

        #Fetch Device Object
        dev = getDeviceObject(config.get_field_value('device_ip'), sdata)
        self.opaque_args['hireachy_device'] = dev

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        #inputkeydict['managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_site_name'] = sdata.getRcPath().split('/')[-3].split('=')[1]
        #inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-5].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)

        #Start of Device binding with python bindings
        #End of Device binding
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'end_points')
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
        inputdict['endpoint_name'] = config.get_field_value('endpoint_name')
        inputdict['device_ip'] = config.get_field_value('device_ip')
        inputdict['fvrf'] = config.get_field_value('fvrf')
        inputdict['ivrf'] = config.get_field_value('ivrf')
        inputdict['vrf'] = config.get_field_value('vrf')
        inputdict['interface_type'] = config.get_field_value('interface_type')
        inputdict['interface_name'] = config.get_field_value('interface_name')
        inputdict['vlan_id'] = config.get_field_value('vlan_id')
        inputdict['interface_description'] = config.get_field_value('interface_description')
        inputdict['inbound_acl'] = config.get_field_value('inbound_acl')
        inputdict['global_inbound_acl'] = config.get_field_value('global_inbound_acl')
        inputdict['site_inbound_acl'] = config.get_field_value('site_inbound_acl')
        inputdict['outbound_acl'] = config.get_field_value('outbound_acl')
        inputdict['global_outbound_acl'] = config.get_field_value('global_outbound_acl')
        inputdict['site_outbound_acl'] = config.get_field_value('site_outbound_acl')
        inputdict['dmvpn_profile'] = config.get_field_value('dmvpn_profile')
        inputdict['p2p'] = config.get_field_value('p2p')
        inputdict['tunnel_interface_ip_address'] = config.get_field_value('tunnel_interface_ip_address')
        inputdict['tunnel_interface_mask'] = config.get_field_value('tunnel_interface_mask')
        inputdict['tunnel_interface_id'] = config.get_field_value('tunnel_interface_id')
        inputdict['tunnel_interface_destination'] = config.get_field_value('tunnel_interface_destination')
        inputdict['tunnel_source'] = config.get_field_value('tunnel_source')
        inputdict['tunnel_bandwidth'] = config.get_field_value('tunnel_bandwidth')
        inputdict['nat_outside'] = config.get_field_value('nat_outside')
        inputdict['nat_inside'] = config.get_field_value('nat_inside')
        inputdict['tunnel_mss'] = config.get_field_value('tunnel_mss')
        # END OF FETCHING THE LEAF PARAMETERS

        #Fetch Device Object
        dev = getDeviceObject(config.get_field_value('device_ip'), sdata)
        self.opaque_args['hireachy_device'] = dev

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'end_points')
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
        inputdict['endpoint_name'] = config.get_field_value('endpoint_name')
        inputdict['device_ip'] = config.get_field_value('device_ip')
        inputdict['fvrf'] = config.get_field_value('fvrf')
        inputdict['ivrf'] = config.get_field_value('ivrf')
        inputdict['vrf'] = config.get_field_value('vrf')
        inputdict['interface_type'] = config.get_field_value('interface_type')
        inputdict['interface_name'] = config.get_field_value('interface_name')
        inputdict['vlan_id'] = config.get_field_value('vlan_id')
        inputdict['interface_description'] = config.get_field_value('interface_description')
        inputdict['inbound_acl'] = config.get_field_value('inbound_acl')
        inputdict['global_inbound_acl'] = config.get_field_value('global_inbound_acl')
        inputdict['site_inbound_acl'] = config.get_field_value('site_inbound_acl')
        inputdict['outbound_acl'] = config.get_field_value('outbound_acl')
        inputdict['global_outbound_acl'] = config.get_field_value('global_outbound_acl')
        inputdict['site_outbound_acl'] = config.get_field_value('site_outbound_acl')
        inputdict['dmvpn_profile'] = config.get_field_value('dmvpn_profile')
        inputdict['p2p'] = config.get_field_value('p2p')
        inputdict['tunnel_interface_ip_address'] = config.get_field_value('tunnel_interface_ip_address')
        inputdict['tunnel_interface_mask'] = config.get_field_value('tunnel_interface_mask')
        inputdict['tunnel_interface_id'] = config.get_field_value('tunnel_interface_id')
        inputdict['tunnel_interface_destination'] = config.get_field_value('tunnel_interface_destination')
        inputdict['tunnel_source'] = config.get_field_value('tunnel_source')
        inputdict['tunnel_bandwidth'] = config.get_field_value('tunnel_bandwidth')
        inputdict['nat_outside'] = config.get_field_value('nat_outside')
        inputdict['nat_inside'] = config.get_field_value('nat_inside')
        inputdict['tunnel_mss'] = config.get_field_value('tunnel_mss')
        # END OF FETCHING THE LEAF PARAMETERS

        #Fetch Device Object
        dev = getDeviceObject(config.get_field_value('device_ip'), sdata)
        self.opaque_args['hireachy_device'] = dev

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(EndPoints._instance == None):
            EndPoints._instance = EndPoints()
        return EndPoints._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)

if __name__ == 'end_points':
  from servicemodel.yang import YangServiceData
  sdata = YangServiceData()
  instance = EndPoints().getInstance()
  instance.create(None, sdata)
  instance.delete(None, sdata)
  instance.update(None, sdata)
