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
                                                                   actions
                                                                          |
                                                                          action
                                                                                
Schema Representation:

/services/managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action
"""
"""
Names of Leafs for this Yang Entity
               label            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/label
    action-statement            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/action-statement
            cli-type            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/cli-type
          cli-string            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/cli-string
       regex-pattern            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/regex-pattern
        input-string            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/input-string
     syslog-priority            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/syslog-priority
          syslog-msg            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/syslog-msg
       first-operand            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/first-operand
             compare            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/compare
      second-operand            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/second-operand
         exit-result            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/exit-result
      comment-string            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/comment-string
   handle-error-type            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/handle-error-type

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
        cpedeployment.cpedeployment_grouping_lib.eem_applet_customization.grouping_create_eem_applet_event_manager_applet_actions_action(smodelctx, sdata, dev, xpath='managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action', **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

        _event_manager_applet_obj = getLocalObject(sdata, 'event-manager-applet')
        inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'] = _event_manager_applet_obj.event_manager_applet.applet_name
        

        from servicemodel.device_abs_lib import device_eem_applets
        

        if inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'] is not None and inputdict['label'] is not None:
          device_eem_applets.eem_applets.event_manager_applet.actions.action().create(sdata, dev, inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'], fill_map_devices_device_eem_applets_event_manager_applet_actions_action(inputdict, sdata=sdata), addref=True)


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
        cpedeployment.cpedeployment_grouping_lib.eem_applet_customization.grouping_update_eem_applet_event_manager_applet_actions_action(smodelctx, sdata, xpath='managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action', **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return
        _event_manager_applet_obj = getLocalObject(sdata, 'event-manager-applet')
        inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'] = _event_manager_applet_obj.event_manager_applet.applet_name
        

        from servicemodel.device_abs_lib import device_eem_applets
        

        up_map_devices_device_eem_applets_event_manager_applet_actions_action = fill_up_map_devices_device_eem_applets_event_manager_applet_actions_action(inputdict, pinputdict, sdata=sdata)
        if up_map_devices_device_eem_applets_event_manager_applet_actions_action[1] == 'key-delete-create' or up_map_devices_device_eem_applets_event_manager_applet_actions_action[1] == 'key-delete':
          device_eem_applets.eem_applets.event_manager_applet.actions.action().delete(sdata, dev, inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'], fill_map_devices_device_eem_applets_event_manager_applet_actions_action(pinputdict), remove_reference=True)

        if up_map_devices_device_eem_applets_event_manager_applet_actions_action[1] == 'key-delete-create' or up_map_devices_device_eem_applets_event_manager_applet_actions_action[1] == 'key-create':
          device_eem_applets.eem_applets.event_manager_applet.actions.action().create(sdata, dev, inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'], up_map_devices_device_eem_applets_event_manager_applet_actions_action[0], addref=True)

        if up_map_devices_device_eem_applets_event_manager_applet_actions_action[1] == 'key-unchanged':
          device_eem_applets.eem_applets.event_manager_applet.actions.action().update(sdata, dev, inputdict['managed_cpe_services_customer_eem_applets_event_manager_applet_applet_name'], fill_map_devices_device_eem_applets_event_manager_applet_actions_action(inputdict, pinputdict=pinputdict, sdata=sdata, update=True))


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
        cpedeployment.cpedeployment_grouping_lib.eem_applet_customization.grouping_delete_eem_applet_event_manager_applet_actions_action(smodelctx, sdata, xpath='managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action', **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

def fill_map_devices_device_eem_applets_event_manager_applet_actions_action(inputdict, sdata=None, pinputdict={}, delete=False, update=False):
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action = {}
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['first_operand'] = inputdict['first_operand'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['cli_string'] = inputdict['cli_string'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['syslog_priority'] = inputdict['syslog_priority'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['syslog_msg'] = inputdict['syslog_msg'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['action_statement'] = inputdict['action_statement'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['label'] = inputdict['label'] if not update else inputdict['label'] if inputdict['label'] is not None else pinputdict['label'] 
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['second_operand'] = inputdict['second_operand'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['comment_string'] = inputdict['comment_string'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['cli_type'] = inputdict['cli_type'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['exit_result'] = inputdict['exit_result'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['handle_error_type'] = inputdict['handle_error_type'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['input_string'] = inputdict['input_string'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['regex_pattern'] = inputdict['regex_pattern'] if not delete else ''
  mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['compare'] = inputdict['compare'] if not delete else ''
  return mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action


def fill_up_map_devices_device_eem_applets_event_manager_applet_actions_action(inputdict, pinputdict, sdata=None):
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action = {}
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['first_operand'] = inputdict['first_operand']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['cli_string'] = inputdict['cli_string']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['syslog_priority'] = inputdict['syslog_priority']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['syslog_msg'] = inputdict['syslog_msg']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['action_statement'] = inputdict['action_statement']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['label'] = inputdict['label'] if inputdict['label'] is not None and inputdict['label'] != '' else pinputdict['label']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['second_operand'] = inputdict['second_operand']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['comment_string'] = inputdict['comment_string']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['cli_type'] = inputdict['cli_type']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['exit_result'] = inputdict['exit_result']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['handle_error_type'] = inputdict['handle_error_type']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['input_string'] = inputdict['input_string']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['regex_pattern'] = inputdict['regex_pattern']
  up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['compare'] = inputdict['compare']
  if up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action.get('label') is None:
    up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action['label'] = pinputdict['label']
  if inputdict['first_operand'] is None and inputdict['cli_string'] is None and inputdict['syslog_priority'] is None and inputdict['syslog_msg'] is None and inputdict['action_statement'] is None and inputdict['label'] is None and inputdict['second_operand'] is None and inputdict['comment_string'] is None and inputdict['cli_type'] is None and inputdict['exit_result'] is None and inputdict['handle_error_type'] is None and inputdict['input_string'] is None and inputdict['regex_pattern'] is None and inputdict['compare'] is None:
    return [up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action, 'no-change']
  up_schema = 'key-unchanged'
  del_mandatory = False
  if inputdict['label'] is not None and pinputdict['label'] is not None:
    up_schema = 'key-delete-create'
    return [up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action, up_schema]
  elif inputdict['label'] == '':
    up_schema = 'key-delete'
    del_mandatory = True
  elif inputdict['label'] is None and pinputdict['label'] is None:
    up_schema = 'no-change'
  elif inputdict['label'] is not None:
    up_schema = 'key-create'
  else:
    up_schema = 'key-unchanged'
  if del_mandatory and up_schema != 'key-create':
    up_schema = 'key-delete'
  elif del_mandatory and up_schema == 'key-create':
    up_schema = 'key-delete-create'
  return [up_mapping_dict_devices_device_eem_applets_event_manager_applet_actions_action, up_schema]


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
