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
                                                                                   routes
                                                                                         |
                                                                                         route
                                                                                              |
                                                                                              options
                                                                                                     
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/type4-site/type4-site/wanop-primary/routes/route/options
"""
"""
Names of Leafs for this Yang Entity
                  id            maps-to  /ac:devices/ac:device/wanop-device:routes/route/options/id
         next-hop-ip            maps-to  /ac:devices/ac:device/wanop-device:routes/route/options/next-hop-ip
      interface-name            maps-to  /ac:devices/ac:device/wanop-device:routes/route/options/interface-name

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
        import cpedeployment.cpedeployment_grouping_lib.routes_customization
        cpedeployment.cpedeployment_grouping_lib.routes_customization.grouping_create_routes_route_options(smodelctx, sdata, dev, **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

        _route_obj = getLocalObject(sdata, 'route')
        inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_ip_address'] = _route_obj.route.dest_ip_address
        inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_mask'] = _route_obj.route.dest_mask
        from servicemodel.device_abs_lib import device_routes
        if inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_ip_address'] is not None and inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_mask'] is not None and inputdict['id'] is not None:
          device_routes.routes.route.options().create(sdata, dev, inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_ip_address'], inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_mask'], fill_map_devices_device_routes_route_options(inputdict), addref=True)

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
        import cpedeployment.cpedeployment_grouping_lib.routes_customization
        cpedeployment.cpedeployment_grouping_lib.routes_customization.grouping_update_routes_route_options(smodelctx, sdata, **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return
        _route_obj = getLocalObject(sdata, 'route')
        inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_ip_address'] = _route_obj.route.dest_ip_address
        inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_mask'] = _route_obj.route.dest_mask
        from servicemodel.device_abs_lib import device_routes
        up_map_devices_device_routes_route_options = fill_up_map_devices_device_routes_route_options(inputdict, pinputdict)
        if up_map_devices_device_routes_route_options[1] == 'key-delete-create' or up_map_devices_device_routes_route_options[1] == 'key-delete':
          device_routes.routes.route.options().delete(sdata, dev, inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_ip_address'], inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_mask'], pinputdict)
        if up_map_devices_device_routes_route_options[1] == 'key-delete-create' or up_map_devices_device_routes_route_options[1] == 'key-create':
          device_routes.routes.route.options().create(sdata, dev, inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_ip_address'], inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_mask'], up_map_devices_device_routes_route_options[0], addref=up_map_devices_device_routes_route_options)
        if up_map_devices_device_routes_route_options[1] == 'key-unchanged':
          device_routes.routes.route.options().update(sdata, dev, inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_ip_address'], inputdict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_wanop_primary_routes_route_dest_mask'], fill_map_devices_device_routes_route_options(inputdict, pinputdict, update=True))

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

        import cpedeployment.cpedeployment_grouping_lib.routes_customization
        cpedeployment.cpedeployment_grouping_lib.routes_customization.grouping_delete_routes_route_options(smodelctx, sdata, **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

def fill_map_devices_device_routes_route_options(inputdict, pinputdict={}, delete=False, update=False):
  mapping_dict_devices_device_routes_route_options = {}
  mapping_dict_devices_device_routes_route_options['id'] = inputdict['id'] if not update else inputdict['id'] if inputdict['id'] is not None else pinputdict['id'] 
  mapping_dict_devices_device_routes_route_options['next_hop_ip'] = inputdict['next_hop_ip'] if not delete else ''
  mapping_dict_devices_device_routes_route_options['interface_name'] = inputdict['interface_name'] if not delete else ''
  mapping_dict_devices_device_routes_route_options['inpath_route'] = inputdict['inpath_route'] if not delete else ''

  #Below are Helper mapping_dict device leafs which are not mapped in service yang
  mapping_dict_devices_device_routes_route_options['description'] = None
  mapping_dict_devices_device_routes_route_options['metric'] = None
  mapping_dict_devices_device_routes_route_options['name'] = None
  mapping_dict_devices_device_routes_route_options['user_id_grp_name'] = None
  mapping_dict_devices_device_routes_route_options['next_routing_table'] = None
  mapping_dict_devices_device_routes_route_options['vlan_number'] = None
  mapping_dict_devices_device_routes_route_options['tag'] = None
  mapping_dict_devices_device_routes_route_options['track'] = None
  return mapping_dict_devices_device_routes_route_options


def fill_up_map_devices_device_routes_route_options(inputdict, pinputdict):
  up_mapping_dict_devices_device_routes_route_options = {}
  up_mapping_dict_devices_device_routes_route_options['id'] = inputdict['id'] if inputdict['id'] is not None and inputdict['id'] != '' else pinputdict['id']
  up_mapping_dict_devices_device_routes_route_options['next_hop_ip'] = inputdict['next_hop_ip']
  up_mapping_dict_devices_device_routes_route_options['interface_name'] = inputdict['interface_name']
  up_mapping_dict_devices_device_routes_route_options['inpath_route'] = inputdict['inpath_route']
  if inputdict['id'] is None and inputdict['next_hop_ip'] is None and inputdict['interface_name'] is None:
    return [up_mapping_dict_devices_device_routes_route_options, 'no-change']
  up_schema = 'key-unchanged'
  del_mandatory = False
  if inputdict['id'] is not None and pinputdict['id'] is not None:
    up_schema = 'key-delete-create'
    return [up_mapping_dict_devices_device_routes_route_options, up_schema]
  elif inputdict['id'] == '':
    up_schema = 'key-delete'
    del_mandatory = True
  elif inputdict['id'] is not None:
    up_schema = 'key-create'
  else:
    up_schema = 'key-unchanged'
  if del_mandatory and up_schema != 'key-create':
    up_schema = 'key-delete'
  elif del_mandatory and up_schema == 'key-create':
    up_schema = 'key-delete-create'
  return [up_mapping_dict_devices_device_routes_route_options, up_schema]


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
