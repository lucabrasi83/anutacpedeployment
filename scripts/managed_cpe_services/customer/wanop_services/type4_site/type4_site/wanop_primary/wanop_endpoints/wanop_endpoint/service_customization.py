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
#ALL THE CUSTOMIZATIONS REGARDING DATAPROCESSING SHOULD BE WRITTEN INTO THIS FILE
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
                                                  type4-site
                                                            |
                                                            type4-site
                                                                      |
                                                                      wanop-primary
                                                                                   |
                                                                                   wanop-endpoints
                                                                                                  |
                                                                                                  wanop-endpoint
                                                                                                                
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/type4-site/type4-site/wanop-primary/wanop-endpoints/wanop-endpoint
"""
"""
Names of Leafs for this Yang Entity
      interface-name            maps-to  /ac:devices/ac:device/if:interfaces/interface/name /ac:devices/ac:device/if:interfaces/interface/long-name
        profile-name
                cidr
        interface-ip            maps-to  /ac:devices/ac:device/if:interfaces/interface/ip-address
interface-description            maps-to  /ac:devices/ac:device/if:interfaces/interface/description
          gateway-ip            maps-to  /ac:devices/ac:device/if:interfaces/interface/gateway
               speed            maps-to  /ac:devices/ac:device/if:interfaces/interface/link-speed
              duplex            maps-to  /ac:devices/ac:device/if:interfaces/interface/duplex
                 mtu            maps-to  /ac:devices/ac:device/if:interfaces/interface/mtu
                 vrf
             vlan-id

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

class ServiceDataCustomization:

    @staticmethod
    def process_service_create_data(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the inputs"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']

    @staticmethod
    def process_service_device_bindings(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the device bindings or Call the Business Login Handlers"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']
        devbindobjs = kwargs['devbindobjs']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']
        import cpedeployment.cpedeployment_grouping_lib.wanop_ic_local_props_type4_customization
        interface_ip,mask_length = cpedeployment.cpedeployment_grouping_lib.wanop_ic_local_props_type4_customization.grouping_create_wanop_ic_local_props_type4_wanop_endpoint(smodelctx, sdata, dev, **kwargs)
        inputdict["interface_ip"] = interface_ip
        inputdict["mask_length"] = mask_length

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

        from servicemodel.device_abs_lib import device_interfaces
        if inputdict['interface_name'] is not None:
          device_interfaces.interfaces.interface().create(sdata, dev, fill_map_devices_device_interfaces_interface(inputdict), addref=False)

    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']

        #Previous config and previous inputdict
        pconfig = kwargs['pconfig']
        pinputdict = kwargs['pinputdict']

        dev = kwargs['dev']
        import cpedeployment.cpedeployment_grouping_lib.wanop_ic_local_props_type4_customization
        cpedeployment.cpedeployment_grouping_lib.wanop_ic_local_props_type4_customization.grouping_update_wanop_ic_local_props_type4_wanop_endpoint(smodelctx, sdata, **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return
        from servicemodel.device_abs_lib import device_interfaces
        up_map_devices_device_interfaces_interface = fill_up_map_devices_device_interfaces_interface(inputdict, pinputdict)
        if up_map_devices_device_interfaces_interface[1] == 'key-delete-create' or up_map_devices_device_interfaces_interface[1] == 'key-create':
          device_interfaces.interfaces.interface().create(sdata, dev, up_map_devices_device_interfaces_interface[0], addref=up_map_devices_device_interfaces_interface)
        if up_map_devices_device_interfaces_interface[1] == 'key-unchanged':
          device_interfaces.interfaces.interface().update(sdata, dev, fill_map_devices_device_interfaces_interface(inputdict, pinputdict, update=True))

    @staticmethod
    def process_service_delete_data(smodelctx, sdata, **kwargs):
      """callback called for delete operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        dev = kwargs['dev']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']

        import cpedeployment.cpedeployment_grouping_lib.wanop_ic_local_props_type4_customization
        cpedeployment.cpedeployment_grouping_lib.wanop_ic_local_props_type4_customization.grouping_delete_wanop_ic_local_props_type4_wanop_endpoint(smodelctx, sdata, **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return
        from servicemodel.device_abs_lib import device_interfaces
        if inputdict['interface_name'] is not None:
          device_interfaces.interfaces.interface().update(sdata, dev, fill_map_devices_device_interfaces_interface(inputdict, delete=True))

def fill_map_devices_device_interfaces_interface(inputdict, delete=False):
  mapping_dict_devices_device_interfaces_interface = {}
  mapping_dict_devices_device_interfaces_interface['name'] = inputdict['interface_name']
  mapping_dict_devices_device_interfaces_interface['duplex'] = inputdict['duplex'] if not delete else ''
  mapping_dict_devices_device_interfaces_interface['long_name'] = inputdict['interface_name']
  mapping_dict_devices_device_interfaces_interface['ip_address'] = inputdict['interface_ip'] if not delete else ''
  mapping_dict_devices_device_interfaces_interface['ipv4_prefix_length'] = inputdict['mask_length'] if not delete else ''
  mapping_dict_devices_device_interfaces_interface['description'] = inputdict['interface_description'] if not delete else ''
  mapping_dict_devices_device_interfaces_interface['mtu'] = inputdict['mtu'] if not delete else ''
  mapping_dict_devices_device_interfaces_interface['link_speed'] = inputdict['speed'] if not delete else ''
  mapping_dict_devices_device_interfaces_interface['inpath_gateway'] = inputdict['gateway_ip'] if not delete else ''
  mapping_dict_devices_device_interfaces_interface['port_number_vlan'] = inputdict['vlan_id'] if not delete else ''
  mapping_dict_devices_device_interfaces_interface['inpath_optimisation'] = inputdict['enable_optimization'] if not delete else ''
  mapping_dict_devices_device_interfaces_interface['admin_state'] = "UP"


  #Below are Helper mapping_dict device leafs which are not mapped in service yang
  mapping_dict_devices_device_interfaces_interface['if_index'] = None
  mapping_dict_devices_device_interfaces_interface['mode'] = None
  mapping_dict_devices_device_interfaces_interface['hold_time_up'] = None
  mapping_dict_devices_device_interfaces_interface['hold_time_down'] = None
  mapping_dict_devices_device_interfaces_interface['physical_address'] = None
  mapping_dict_devices_device_interfaces_interface['rnc_name'] = None
  mapping_dict_devices_device_interfaces_interface['port'] = None
  mapping_dict_devices_device_interfaces_interface['dhcp'] = None
  mapping_dict_devices_device_interfaces_interface['netmask'] = None
  mapping_dict_devices_device_interfaces_interface['ipv6_address'] = None
  mapping_dict_devices_device_interfaces_interface['ipv6_prefix_length'] = None
  mapping_dict_devices_device_interfaces_interface['alias_address'] = None
  mapping_dict_devices_device_interfaces_interface['gateway'] = None
  mapping_dict_devices_device_interfaces_interface['primaryip'] = None
  mapping_dict_devices_device_interfaces_interface['secondaryip'] = None
  mapping_dict_devices_device_interfaces_interface['out_bandwidth'] = None
  mapping_dict_devices_device_interfaces_interface['in_bandwidth'] = None
  mapping_dict_devices_device_interfaces_interface['native_vlan'] = None
  mapping_dict_devices_device_interfaces_interface['portfast'] = None
  mapping_dict_devices_device_interfaces_interface['service'] = None
  mapping_dict_devices_device_interfaces_interface['cdp'] = None
  mapping_dict_devices_device_interfaces_interface['bpduguard'] = None
  mapping_dict_devices_device_interfaces_interface['broadcast'] = None
  mapping_dict_devices_device_interfaces_interface['nonegotiate'] = None
  mapping_dict_devices_device_interfaces_interface['power_inline'] = None
  mapping_dict_devices_device_interfaces_interface['value'] = None
  mapping_dict_devices_device_interfaces_interface['priority_queue'] = None
  mapping_dict_devices_device_interfaces_interface['voice_vlan'] = None
  mapping_dict_devices_device_interfaces_interface['level'] = None
  mapping_dict_devices_device_interfaces_interface['speed_unit'] = None
  mapping_dict_devices_device_interfaces_interface['policer_name'] = None
  mapping_dict_devices_device_interfaces_interface['unit'] = None
  mapping_dict_devices_device_interfaces_interface['context_name'] = None
  mapping_dict_devices_device_interfaces_interface['visible_interface'] = None
  mapping_dict_devices_device_interfaces_interface['inside_name'] = None
  mapping_dict_devices_device_interfaces_interface['security_level_inside'] = None
  mapping_dict_devices_device_interfaces_interface['mpls_device_role'] = None
  mapping_dict_devices_device_interfaces_interface['inner_vlan'] = None
  mapping_dict_devices_device_interfaces_interface['outbound_qos'] = None
  mapping_dict_devices_device_interfaces_interface['inbound_qos'] = None
  mapping_dict_devices_device_interfaces_interface['load_interval_delay'] = None
  mapping_dict_devices_device_interfaces_interface['in_queue_length'] = None
  mapping_dict_devices_device_interfaces_interface['out_queue_length'] = None
  mapping_dict_devices_device_interfaces_interface['link_negotiation'] = None
  mapping_dict_devices_device_interfaces_interface['vrf_receive'] = None
  mapping_dict_devices_device_interfaces_interface['bgp_policy'] = None
  mapping_dict_devices_device_interfaces_interface['bgp_policy_qos'] = None
  mapping_dict_devices_device_interfaces_interface['pbr_policy'] = None
  mapping_dict_devices_device_interfaces_interface['vrf_definition_mode'] = None
  mapping_dict_devices_device_interfaces_interface['encap_mode'] = None
  mapping_dict_devices_device_interfaces_interface['port_number'] = None
  mapping_dict_devices_device_interfaces_interface['mgmt_profile'] = None
  mapping_dict_devices_device_interfaces_interface['address1_comment'] = None
  mapping_dict_devices_device_interfaces_interface['address2_comment'] = None
  mapping_dict_devices_device_interfaces_interface['rpf_check'] = None
  mapping_dict_devices_device_interfaces_interface['postscrub_unit'] = None
  mapping_dict_devices_device_interfaces_interface['keepalive_time'] = None
  mapping_dict_devices_device_interfaces_interface['virtual_ethernet_number'] = None
  mapping_dict_devices_device_interfaces_interface['ethernet_number_vpls'] = None
  mapping_dict_devices_device_interfaces_interface['cos'] = None
  mapping_dict_devices_device_interfaces_interface['port_number_vpls'] = None
  mapping_dict_devices_device_interfaces_interface['slot_number'] = None
  mapping_dict_devices_device_interfaces_interface['full_slot_number'] = None
  mapping_dict_devices_device_interfaces_interface['slot_module_number'] = None
  mapping_dict_devices_device_interfaces_interface['vpn_instance_name'] = None
  mapping_dict_devices_device_interfaces_interface['vsi_vlan_name'] = None
  mapping_dict_devices_device_interfaces_interface['port_type'] = None
  mapping_dict_devices_device_interfaces_interface['if_type'] = None
  mapping_dict_devices_device_interfaces_interface['arp_timeout'] = None
  mapping_dict_devices_device_interfaces_interface['vpls_name'] = None
  mapping_dict_devices_device_interfaces_interface['bandwidth'] = None
  mapping_dict_devices_device_interfaces_interface['maximum_segment_size'] = None
  mapping_dict_devices_device_interfaces_interface['nat_name'] = None
  mapping_dict_devices_device_interfaces_interface['minimum_links'] = None
  mapping_dict_devices_device_interfaces_interface['speed'] = None
  mapping_dict_devices_device_interfaces_interface['fcoe_lag'] = None
  mapping_dict_devices_device_interfaces_interface['lacp_active_enable'] = None
  mapping_dict_devices_device_interfaces_interface['lacp_active_periodic_fast'] = None
  mapping_dict_devices_device_interfaces_interface['vlan'] = None
  mapping_dict_devices_device_interfaces_interface['port_channel_name'] = None
  mapping_dict_devices_device_interfaces_interface['channel_group_mode'] = None
  mapping_dict_devices_device_interfaces_interface['channel_protocol'] = None
  mapping_dict_devices_device_interfaces_interface['vrf'] = None
  mapping_dict_devices_device_interfaces_interface['bfd_name'] = None
  mapping_dict_devices_device_interfaces_interface['port_qos_group_template'] = None
  mapping_dict_devices_device_interfaces_interface['port_qos_scheduler_policy'] = None
  mapping_dict_devices_device_interfaces_interface['rate_limit'] = None
  return mapping_dict_devices_device_interfaces_interface


def fill_up_map_devices_device_interfaces_interface(inputdict, pinputdict):
  up_mapping_dict_devices_device_interfaces_interface = {}
  up_mapping_dict_devices_device_interfaces_interface['name'] = inputdict['interface_name'] if inputdict['interface_name'] is not None and inputdict['interface_name'] != '' else pinputdict['interface_name']
  up_mapping_dict_devices_device_interfaces_interface['duplex'] = inputdict['duplex']
  up_mapping_dict_devices_device_interfaces_interface['long_name'] = inputdict['interface_name'] if inputdict['interface_name'] is not None and inputdict['interface_name'] != '' else pinputdict['interface_name']
  up_mapping_dict_devices_device_interfaces_interface['ip_address'] = inputdict['interface_ip']
  up_mapping_dict_devices_device_interfaces_interface['ipv4_prefix_length'] = inputdict['mask_length']
  up_mapping_dict_devices_device_interfaces_interface['description'] = inputdict['interface_description']
  up_mapping_dict_devices_device_interfaces_interface['mtu'] = inputdict['mtu']
  up_mapping_dict_devices_device_interfaces_interface['link_speed'] = inputdict['speed']
  up_mapping_dict_devices_device_interfaces_interface['inpath_gateway'] = inputdict['gateway_ip']
  up_mapping_dict_devices_device_interfaces_interface['port_number_vlan'] = inputdict['vlan_id']
  up_mapping_dict_devices_device_interfaces_interface['inpath_optimisation'] = inputdict['enable_optimization']
  up_mapping_dict_devices_device_interfaces_interface['admin_state'] = "UP"

  up_schema = 'key-unchanged'
  del_mandatory = False
  if inputdict['interface_name'] is not None and pinputdict['interface_name'] is not None:
    up_schema = 'key-delete-create'
    return [up_mapping_dict_devices_device_interfaces_interface, up_schema]
  elif inputdict['interface_name'] == '':
    up_schema = 'key-delete'
    del_mandatory = True
  elif inputdict['interface_name'] is not None:
    up_schema = 'key-create'
  else:
    up_schema = 'key-unchanged'
  if del_mandatory and up_schema != 'key-create':
    up_schema = 'key-delete'
  elif del_mandatory and up_schema == 'key-create':
    up_schema = 'key-delete-create'
  return [up_mapping_dict_devices_device_interfaces_interface, up_schema]


class DeletePreProcessor(yang.SessionPreProcessor):
  def processBeforeReserve(self, session):
    operations = session.getOperations()
    """Add any move operations for Deletion"""
    log('operations: %s' % (operations))

class CreatePreProcessor(yang.SessionPreProcessor):
  def processBeforeReserve(self, session):
    operations = session.getOperations()
    """Add any move operations for creation"""
    log('operations: %s' % (operations))
