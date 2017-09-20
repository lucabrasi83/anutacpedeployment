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
                                                                   |
                                                                   events
                                                                         |
                                                                         tag
                                                                            
Schema Representation:

/services/managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag
"""
"""
Names of Leafs for this Yang Entity
          tag-number            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/events/tag/tag-number
      interface-name            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/events/tag/interface-name
           parameter            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/events/tag/parameter
       entry-compare            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/events/tag/entry-compare
   entry-counter-val            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/events/tag/entry-counter-val
       poll-interval            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/events/tag/poll-interval

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
        cpedeployment.cpedeployment_grouping_lib.eem_applet_customization.grouping_create_eem_applet_event_manager_applet_events_tag(smodelctx, sdata, dev, xpath='managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag', **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

        _event_manager_applet_obj = getLocalObject(sdata, 'event-manager-applet')
        inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'] = _event_manager_applet_obj.event_manager_applet.applet_name
        

        from servicemodel.device_abs_lib import device_eem_applets
        

        if inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'] is not None and inputdict['tag_number'] is not None:
          device_eem_applets.eem_applets.event_manager_applet.events.tag().create(sdata, dev, inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'], fill_map_devices_device_eem_applets_event_manager_applet_events_tag(inputdict, sdata=sdata), addref=True)


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
        cpedeployment.cpedeployment_grouping_lib.eem_applet_customization.grouping_update_eem_applet_event_manager_applet_events_tag(smodelctx, sdata, xpath='managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag', **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return
        _event_manager_applet_obj = getLocalObject(sdata, 'event-manager-applet')
        inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'] = _event_manager_applet_obj.event_manager_applet.applet_name
        

        from servicemodel.device_abs_lib import device_eem_applets
        

        up_map_devices_device_eem_applets_event_manager_applet_events_tag = fill_up_map_devices_device_eem_applets_event_manager_applet_events_tag(inputdict, pinputdict, sdata=sdata)
        if up_map_devices_device_eem_applets_event_manager_applet_events_tag[1] == 'key-delete-create' or up_map_devices_device_eem_applets_event_manager_applet_events_tag[1] == 'key-delete':
          device_eem_applets.eem_applets.event_manager_applet.events.tag().delete(sdata, dev, inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'], fill_map_devices_device_eem_applets_event_manager_applet_events_tag(pinputdict), remove_reference=True)

        if up_map_devices_device_eem_applets_event_manager_applet_events_tag[1] == 'key-delete-create' or up_map_devices_device_eem_applets_event_manager_applet_events_tag[1] == 'key-create':
          device_eem_applets.eem_applets.event_manager_applet.events.tag().create(sdata, dev, inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'], up_map_devices_device_eem_applets_event_manager_applet_events_tag[0], addref=True)

        if up_map_devices_device_eem_applets_event_manager_applet_events_tag[1] == 'key-unchanged':
          device_eem_applets.eem_applets.event_manager_applet.events.tag().update(sdata, dev, inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'], fill_map_devices_device_eem_applets_event_manager_applet_events_tag(inputdict, pinputdict=pinputdict, sdata=sdata, update=True))


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
        cpedeployment.cpedeployment_grouping_lib.eem_applet_customization.grouping_delete_eem_applet_event_manager_applet_events_tag(smodelctx, sdata, xpath='managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag', **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

def fill_map_devices_device_eem_applets_event_manager_applet_events_tag(inputdict, sdata=None, pinputdict={}, delete=False, update=False):
  mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag = {}
  mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['tag_number'] = inputdict['tag_number'] if not update else inputdict['tag_number'] if inputdict['tag_number'] is not None else pinputdict['tag_number'] 
  mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['parameter'] = inputdict['parameter'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['entry_counter_val'] = inputdict['entry_counter_val'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['poll_interval'] = inputdict['poll_interval'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['interface_name'] = inputdict['interface_name'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['entry_compare'] = inputdict['entry_compare'] if not delete else ''
  return mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag


def fill_up_map_devices_device_eem_applets_event_manager_applet_events_tag(inputdict, pinputdict, sdata=None):
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag = {}
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['tag_number'] = inputdict['tag_number'] if inputdict['tag_number'] is not None and inputdict['tag_number'] != '' else pinputdict['tag_number']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['parameter'] = inputdict['parameter']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['entry_counter_val'] = inputdict['entry_counter_val']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['poll_interval'] = inputdict['poll_interval']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['interface_name'] = inputdict['interface_name']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['entry_compare'] = inputdict['entry_compare']
  if up_mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag.get('tag_number') is None:
    up_mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag['tag_number'] = pinputdict['tag_number']
  if inputdict['tag_number'] is None and inputdict['parameter'] is None and inputdict['entry_counter_val'] is None and inputdict['poll_interval'] is None and inputdict['interface_name'] is None and inputdict['entry_compare'] is None:
    return [up_mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag, 'no-change']
  up_schema = 'key-unchanged'
  del_mandatory = False
  if inputdict['tag_number'] is not None and pinputdict['tag_number'] is not None:
    up_schema = 'key-delete-create'
    return [up_mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag, up_schema]
  elif inputdict['tag_number'] == '':
    up_schema = 'key-delete'
    del_mandatory = True
  elif inputdict['tag_number'] is None and pinputdict['tag_number'] is None:
    up_schema = 'no-change'
  elif inputdict['tag_number'] is not None:
    up_schema = 'key-create'
  else:
    up_schema = 'key-unchanged'
  if del_mandatory and up_schema != 'key-create':
    up_schema = 'key-delete'
  elif del_mandatory and up_schema == 'key-create':
    up_schema = 'key-delete-create'
  return [up_mapping_dict_devices_device_eem_applets_event_manager_applet_events_tag, up_schema]


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
