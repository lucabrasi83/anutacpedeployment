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
                                    dps
                                       |
                                       dps-services
                                                   |
                                                   cpe-name
                                                           
Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name
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

class CpeName(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'cpe_name')

        #Fetch Service Model Context Object
        smodelctx = ServiceModelContext(id, sdata)

        #Fetch Parent Object
        parentobj = getParentObject(sdata)

        dev = []
        devbindobjs={}
        inputdict = {}

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['cpe'] = config.get_field_value('cpe')
        inputdict['vrf'] = config.get_field_value('vrf')
        inputdict['rd'] = config.get_field_value('rd')
        inputdict['rt_import'] = config.get_field_value('rt_import')
        inputdict['rt_export'] = config.get_field_value('rt_export')
        inputdict['lan_interface'] = config.get_field_value('lan_interface')
        inputdict['inbound_policy'] = config.get_field_value('inbound_policy')
        inputdict['hierarchical_inbound_policy'] = config.get_field_value('hierarchical_inbound_policy')
        inputdict['hierarchical_policy'] = config.get_field_value('hierarchical_policy')
        inputdict['pbr_policy'] = config.get_field_value('pbr_policy')
        inputdict['next_hop_ip'] = config.get_field_value('next_hop_ip')
        inputdict['vrf_receive'] = config.get_field_value('vrf_receive')
        inputdict['bgp_policy'] = config.get_field_value('bgp_policy')
        inputdict['bgp_policy_qos'] = config.get_field_value('bgp_policy_qos')
        inputdict['b2b_interface'] = config.get_field_value('b2b_interface')
        inputdict['vlan_id'] = config.get_field_value('vlan_id')
        inputdict['cidr'] = config.get_field_value('cidr')
        inputdict['interface_ip'] = config.get_field_value('interface_ip')
        inputdict['b2b_description'] = config.get_field_value('b2b_description')
        inputdict['loopback'] = config.get_field_value('loopback')
        inputdict['loopback_interface_id'] = config.get_field_value('loopback_interface_id')
        inputdict['description'] = config.get_field_value('description')
        inputdict['cidr_loopback'] = config.get_field_value('cidr_loopback')
        inputdict['loopback_ip'] = config.get_field_value('loopback_ip')
        inputdict['ospf'] = config.get_field_value('ospf')
        inputdict['ospf_id'] = config.get_field_value('ospf_id')
        inputdict['router_id'] = config.get_field_value('router_id')
        inputdict['static_route_map'] = config.get_field_value('static_route_map')
        inputdict['connected_route_map'] = config.get_field_value('connected_route_map')
        inputdict['lan_ospf_redistribution'] = config.get_field_value('lan_ospf_redistribution')
        inputdict['ospf_route_map'] = config.get_field_value('ospf_route_map')
        inputdict['ospf_redistribution_id'] = config.get_field_value('ospf_redistribution_id')
        inputdict['ospf_key1'] = config.get_field_value('ospf_key1')
        inputdict['ospf_key2'] = config.get_field_value('ospf_key2')
        inputdict['ospf_metric'] = config.get_field_value('ospf_metric')
        inputdict['ospf_metric_type'] = config.get_field_value('ospf_metric_type')
        inputdict['ospf_tag'] = config.get_field_value('ospf_tag')
        inputdict['lan_ebgp_redistribution'] = config.get_field_value('lan_ebgp_redistribution')
        inputdict['bgp_route_map'] = config.get_field_value('bgp_route_map')
        inputdict['bgp_key1'] = config.get_field_value('bgp_key1')
        inputdict['bgp_key2'] = config.get_field_value('bgp_key2')
        inputdict['bgp_metric'] = config.get_field_value('bgp_metric')
        inputdict['bgp_metric_type'] = config.get_field_value('bgp_metric_type')
        inputdict['bgp_tag'] = config.get_field_value('bgp_tag')
        inputdict['vrf_lite'] = config.get_field_value('vrf_lite')
        inputdict['bgp'] = config.get_field_value('bgp')
        inputdict['bgp_vrf'] = config.get_field_value('bgp_vrf')
        inputdict['qppb_policy'] = config.get_field_value('qppb_policy')
        inputdict['redistribute_connected'] = config.get_field_value('redistribute_connected')
        inputdict['redistribute_static'] = config.get_field_value('redistribute_static')
        inputdict['import_route_map'] = config.get_field_value('import_route_map')
        inputdict['tunnel'] = config.get_field_value('tunnel')
        inputdict['hub'] = config.get_field_value('hub')
        inputdict['dmvpn_profile'] = config.get_field_value('dmvpn_profile')
        inputdict['tunnel_interface_ip_address'] = config.get_field_value('tunnel_interface_ip_address')
        inputdict['tunnel_interface_description'] = config.get_field_value('tunnel_interface_description')
        inputdict['tunnel_bandwidth'] = config.get_field_value('tunnel_bandwidth')
        # END OF FETCHING THE LEAF PARAMETERS

        inputkeydict = {}
        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_dps_dps_services_name'] = sdata.getRcPath().split('/')[-2].split('=')[1]
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, device=dev, parentobj=parentobj, inputdict=inputdict, config=config)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'cpe_name')

        #Fetch Service Model Context Object
        smodelctx = ServiceModelContext(id, sdata)

        #Fetch Parent Object
        parentobj = getParentObject(sdata)
        dev = []
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, dev=dev, parentobj=parentobj, config=config)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'cpe_name')

        #Fetch Service Model Context Object
        smodelctx = ServiceModelContext(id, sdata)

        #Fetch Parent Object
        parentobj = getParentObject(sdata)
        dev = []

        inputdict = {}

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['cpe'] = config.get_field_value('cpe')
        inputdict['vrf'] = config.get_field_value('vrf')
        inputdict['rd'] = config.get_field_value('rd')
        inputdict['rt_import'] = config.get_field_value('rt_import')
        inputdict['rt_export'] = config.get_field_value('rt_export')
        inputdict['lan_interface'] = config.get_field_value('lan_interface')
        inputdict['inbound_policy'] = config.get_field_value('inbound_policy')
        inputdict['hierarchical_inbound_policy'] = config.get_field_value('hierarchical_inbound_policy')
        inputdict['hierarchical_policy'] = config.get_field_value('hierarchical_policy')
        inputdict['pbr_policy'] = config.get_field_value('pbr_policy')
        inputdict['next_hop_ip'] = config.get_field_value('next_hop_ip')
        inputdict['vrf_receive'] = config.get_field_value('vrf_receive')
        inputdict['bgp_policy'] = config.get_field_value('bgp_policy')
        inputdict['b2b_interface'] = config.get_field_value('b2b_interface')
        inputdict['vlan_id'] = config.get_field_value('vlan_id')
        inputdict['cidr'] = config.get_field_value('cidr')
        inputdict['interface_ip'] = config.get_field_value('interface_ip')
        inputdict['b2b_description'] = config.get_field_value('b2b_description')
        inputdict['loopback'] = config.get_field_value('loopback')
        inputdict['loopback_interface_id'] = config.get_field_value('loopback_interface_id')
        inputdict['description'] = config.get_field_value('description')
        inputdict['cidr_loopback'] = config.get_field_value('cidr_loopback')
        inputdict['loopback_ip'] = config.get_field_value('loopback_ip')
        inputdict['ospf'] = config.get_field_value('ospf')
        inputdict['ospf_id'] = config.get_field_value('ospf_id')
        inputdict['router_id'] = config.get_field_value('router_id')
        inputdict['static_route_map'] = config.get_field_value('static_route_map')
        inputdict['connected_route_map'] = config.get_field_value('connected_route_map')
        inputdict['vrf_lite'] = config.get_field_value('vrf_lite')
        inputdict['bgp'] = config.get_field_value('bgp')
        inputdict['bgp_vrf'] = config.get_field_value('bgp_vrf')
        inputdict['qppb_policy'] = config.get_field_value('qppb_policy')
        inputdict['redistribute_connected'] = config.get_field_value('redistribute_connected')
        inputdict['redistribute_static'] = config.get_field_value('redistribute_static')
        inputdict['import_route_map'] = config.get_field_value('import_route_map')
        inputdict['tunnel'] = config.get_field_value('tunnel')
        inputdict['hub'] = config.get_field_value('hub')
        inputdict['dmvpn_profile'] = config.get_field_value('dmvpn_profile')
        inputdict['tunnel_interface_ip_address'] = config.get_field_value('tunnel_interface_ip_address')
        inputdict['tunnel_interface_description'] = config.get_field_value('tunnel_interface_description')
        inputdict['tunnel_bandwidth'] = config.get_field_value('tunnel_bandwidth')
        # END OF FETCHING THE LEAF PARAMETERS

        inputkeydict = {}
        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_dps_dps_services_name'] = sdata.getRcPath().split('/')[-2].split('=')[1]
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS
        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, dev=dev, parentobj=parentobj, inputdict=inputdict, config=config)

    @staticmethod
    def getInstance():
        if(CpeName._instance == None):
            CpeName._instance = CpeName()
        return CpeName._instance

    #def rollbackCreate(self, id, sdata):
        #        log('rollback: id = %s, sdata = %s' % (id, sdata))
        #        self.delete(id,sdata)
