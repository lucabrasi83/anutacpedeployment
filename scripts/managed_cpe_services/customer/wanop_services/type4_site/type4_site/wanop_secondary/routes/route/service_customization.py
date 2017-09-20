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
                                                                      wanop-secondary
                                                                                     |
                                                                                     routes
                                                                                           |
                                                                                           route
                                                                                                
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/type4-site/type4-site/wanop-secondary/routes/route
"""
"""
Names of Leafs for this Yang Entity
     dest-ip-address            maps-to  /ac:devices/ac:device/wanop-device:routes/route/dest-ip-address
           dest-mask            maps-to  /ac:devices/ac:device/wanop-device:routes/route/dest-mask

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
        cpedeployment.cpedeployment_grouping_lib.routes_customization.grouping_create_routes_route(smodelctx, sdata, dev, **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

        from servicemodel.device_abs_lib import device_routes
        if inputdict['dest_ip_address'] is not None and inputdict['dest_mask'] is not None:
          device_routes.routes.route().create(sdata, dev, fill_map_devices_device_routes_route(inputdict), addref=True)

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
        cpedeployment.cpedeployment_grouping_lib.routes_customization.grouping_update_routes_route(smodelctx, sdata, **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return
        from servicemodel.device_abs_lib import device_routes
        up_map_devices_device_routes_route = fill_up_map_devices_device_routes_route(inputdict, pinputdict)
        if up_map_devices_device_routes_route[1] == 'key-delete-create' or up_map_devices_device_routes_route[1] == 'key-delete':
          device_routes.routes.route().delete(sdata, dev, pinputdict)
        if up_map_devices_device_routes_route[1] == 'key-delete-create' or up_map_devices_device_routes_route[1] == 'key-create':
          device_routes.routes.route().create(sdata, dev, up_map_devices_device_routes_route[0], addref=up_map_devices_device_routes_route)
        if up_map_devices_device_routes_route[1] == 'key-unchanged':
          device_routes.routes.route().update(sdata, dev, fill_map_devices_device_routes_route(inputdict, pinputdict, update=True))

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
        cpedeployment.cpedeployment_grouping_lib.routes_customization.grouping_delete_routes_route(smodelctx, sdata, **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

def fill_map_devices_device_routes_route(inputdict, pinputdict={}, delete=False, update=False):
  mapping_dict_devices_device_routes_route = {}
  mapping_dict_devices_device_routes_route['dest_ip_address'] = inputdict['dest_ip_address'] if not update else inputdict['dest_ip_address'] if inputdict['dest_ip_address'] is not None else pinputdict['dest_ip_address'] 
  mapping_dict_devices_device_routes_route['dest_mask'] = inputdict['dest_mask'] if not update else inputdict['dest_mask'] if inputdict['dest_mask'] is not None else pinputdict['dest_mask'] 
  return mapping_dict_devices_device_routes_route


def fill_up_map_devices_device_routes_route(inputdict, pinputdict):
  up_mapping_dict_devices_device_routes_route = {}
  up_mapping_dict_devices_device_routes_route['dest_ip_address'] = inputdict['dest_ip_address'] if inputdict['dest_ip_address'] is not None and inputdict['dest_ip_address'] != '' else pinputdict['dest_ip_address']
  up_mapping_dict_devices_device_routes_route['dest_mask'] = inputdict['dest_mask'] if inputdict['dest_mask'] is not None and inputdict['dest_mask'] != '' else pinputdict['dest_mask']
  if inputdict['dest_ip_address'] is None and inputdict['dest_mask'] is None:
    return [up_mapping_dict_devices_device_routes_route, 'no-change']
  up_schema = 'key-unchanged'
  del_mandatory = False
  if inputdict['dest_ip_address'] is not None and pinputdict['dest_ip_address'] is not None:
    up_schema = 'key-delete-create'
    return [up_mapping_dict_devices_device_routes_route, up_schema]
  elif inputdict['dest_ip_address'] == '':
    up_schema = 'key-delete'
    del_mandatory = True
  elif inputdict['dest_ip_address'] is not None:
    up_schema = 'key-create'
  else:
    up_schema = 'key-unchanged'
  if inputdict['dest_mask'] is not None and pinputdict['dest_mask'] is not None:
    up_schema = 'key-delete-create'
    return [up_mapping_dict_devices_device_routes_route, up_schema]
  elif inputdict['dest_mask'] == '':
    up_schema = 'key-delete'
    del_mandatory = True
  elif inputdict['dest_mask'] is not None:
    up_schema = 'key-create'
  if del_mandatory and up_schema != 'key-create':
    up_schema = 'key-delete'
  elif del_mandatory and up_schema == 'key-create':
    up_schema = 'key-delete-create'
  return [up_mapping_dict_devices_device_routes_route, up_schema]


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
