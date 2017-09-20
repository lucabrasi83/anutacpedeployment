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
                                    eem-applets
                                               |
                                               event-manager-applet
                                                                   
Schema Representation:

/services/managed-cpe-services/customer/eem-applets/event-manager-applet
"""
"""
Names of Leafs for this Yang Entity
         applet-name            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/applet-name

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
        import cpedeployment.cpedeployment_grouping_lib.eem_applet_customization
        cpedeployment.cpedeployment_grouping_lib.eem_applet_customization.grouping_create_eem_applet_event_manager_applet(smodelctx, sdata, dev, xpath='managed-cpe-services/customer/eem-applets/event-manager-applet', **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

        from servicemodel.device_abs_lib import device_eem_applets
        

        if inputdict['applet_name'] is not None:
          device_eem_applets.eem_applets.event_manager_applet().create(sdata, dev, fill_map_devices_device_eem_applets_event_manager_applet(inputdict, sdata=sdata), addref=True)


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
        import cpedeployment.cpedeployment_grouping_lib.eem_applet_customization
        cpedeployment.cpedeployment_grouping_lib.eem_applet_customization.grouping_update_eem_applet_event_manager_applet(smodelctx, sdata, xpath='managed-cpe-services/customer/eem-applets/event-manager-applet', **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return
        from servicemodel.device_abs_lib import device_eem_applets
        

        up_map_devices_device_eem_applets_event_manager_applet = fill_up_map_devices_device_eem_applets_event_manager_applet(inputdict, pinputdict, sdata=sdata)
        if up_map_devices_device_eem_applets_event_manager_applet[1] == 'key-delete-create' or up_map_devices_device_eem_applets_event_manager_applet[1] == 'key-delete':
          device_eem_applets.eem_applets.event_manager_applet().delete(sdata, dev, fill_map_devices_device_eem_applets_event_manager_applet(pinputdict), remove_reference=True)

        if up_map_devices_device_eem_applets_event_manager_applet[1] == 'key-delete-create' or up_map_devices_device_eem_applets_event_manager_applet[1] == 'key-create':
          device_eem_applets.eem_applets.event_manager_applet().create(sdata, dev, up_map_devices_device_eem_applets_event_manager_applet[0], addref=True)

        if up_map_devices_device_eem_applets_event_manager_applet[1] == 'key-unchanged':
          device_eem_applets.eem_applets.event_manager_applet().update(sdata, dev, fill_map_devices_device_eem_applets_event_manager_applet(inputdict, pinputdict=pinputdict, sdata=sdata, update=True))


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

        import cpedeployment.cpedeployment_grouping_lib.eem_applet_customization
        cpedeployment.cpedeployment_grouping_lib.eem_applet_customization.grouping_delete_eem_applet_event_manager_applet(smodelctx, sdata, xpath='managed-cpe-services/customer/eem-applets/event-manager-applet', **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

def fill_map_devices_device_eem_applets_event_manager_applet(inputdict, sdata=None, pinputdict={}, delete=False, update=False):
  mapping_dict_devices_device_eem_applets_event_manager_applet = {}
  mapping_dict_devices_device_eem_applets_event_manager_applet['applet_name'] = inputdict['applet_name'] if not update else inputdict['applet_name'] if inputdict['applet_name'] is not None else pinputdict['applet_name'] 
  return mapping_dict_devices_device_eem_applets_event_manager_applet


def fill_up_map_devices_device_eem_applets_event_manager_applet(inputdict, pinputdict, sdata=None):
  up_mapping_dict_devices_device_eem_applets_event_manager_applet = {}
  up_mapping_dict_devices_device_eem_applets_event_manager_applet['applet_name'] = inputdict['applet_name'] if inputdict['applet_name'] is not None and inputdict['applet_name'] != '' else pinputdict['applet_name']
  if up_mapping_dict_devices_device_eem_applets_event_manager_applet.get('applet_name') is None:
    up_mapping_dict_devices_device_eem_applets_event_manager_applet['applet_name'] = pinputdict['applet_name']
  if inputdict['applet_name'] is None:
    return [up_mapping_dict_devices_device_eem_applets_event_manager_applet, 'no-change']
  up_schema = 'key-unchanged'
  del_mandatory = False
  if inputdict['applet_name'] is not None and pinputdict['applet_name'] is not None:
    up_schema = 'key-delete-create'
    return [up_mapping_dict_devices_device_eem_applets_event_manager_applet, up_schema]
  elif inputdict['applet_name'] == '':
    up_schema = 'key-delete'
    del_mandatory = True
  elif inputdict['applet_name'] is None and pinputdict['applet_name'] is None:
    up_schema = 'no-change'
  elif inputdict['applet_name'] is not None:
    up_schema = 'key-create'
  else:
    up_schema = 'key-unchanged'
  if del_mandatory and up_schema != 'key-create':
    up_schema = 'key-delete'
  elif del_mandatory and up_schema == 'key-create':
    up_schema = 'key-delete-create'
  return [up_mapping_dict_devices_device_eem_applets_event_manager_applet, up_schema]


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
