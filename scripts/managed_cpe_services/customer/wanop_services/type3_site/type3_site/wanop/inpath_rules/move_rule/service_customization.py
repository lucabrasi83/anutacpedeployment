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
                                                  type3-site
                                                            |
                                                            type3-site
                                                                      |
                                                                      wanop
                                                                           |
                                                                           inpath-rules
                                                                                       |
                                                                                       move-rule
                                                                                                
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/type3-site/type3-site/wanop/inpath-rules/move-rule
"""
"""
Names of Leafs for this Yang Entity
       from-rule-num            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/move-rule/from-rule-num
         to-rule-num            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/move-rule/to-rule-num

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
        import cpedeployment.cpedeployment_grouping_lib.inpath_rules_def_customization
        cpedeployment.cpedeployment_grouping_lib.inpath_rules_def_customization.grouping_create_inpath_rules_def_move_rule(smodelctx, sdata, dev, **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

        from servicemodel.device_abs_lib import device_inpath_rules
        if inputdict['from_rule_num'] is not None and inputdict['to_rule_num'] is not None:
          device_inpath_rules.inpath_rules.move_rule().create(sdata, dev, fill_map_devices_device_inpath_rules_move_rule(inputdict), addref=True)

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
        import cpedeployment.cpedeployment_grouping_lib.inpath_rules_def_customization
        cpedeployment.cpedeployment_grouping_lib.inpath_rules_def_customization.grouping_update_inpath_rules_def_move_rule(smodelctx, sdata, **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return
        from servicemodel.device_abs_lib import device_inpath_rules
        up_map_devices_device_inpath_rules_move_rule = fill_up_map_devices_device_inpath_rules_move_rule(inputdict, pinputdict)
        if up_map_devices_device_inpath_rules_move_rule[1] == 'key-delete-create' or up_map_devices_device_inpath_rules_move_rule[1] == 'key-delete':
          device_inpath_rules.inpath_rules.move_rule().delete(sdata, dev, pinputdict)
        if up_map_devices_device_inpath_rules_move_rule[1] == 'key-delete-create' or up_map_devices_device_inpath_rules_move_rule[1] == 'key-create':
          device_inpath_rules.inpath_rules.move_rule().create(sdata, dev, up_map_devices_device_inpath_rules_move_rule[0], addref=up_map_devices_device_inpath_rules_move_rule)
        if up_map_devices_device_inpath_rules_move_rule[1] == 'key-unchanged':
          device_inpath_rules.inpath_rules.move_rule().update(sdata, dev, fill_map_devices_device_inpath_rules_move_rule(inputdict, pinputdict, update=True))

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

        import cpedeployment.cpedeployment_grouping_lib.inpath_rules_def_customization
        cpedeployment.cpedeployment_grouping_lib.inpath_rules_def_customization.grouping_delete_inpath_rules_def_move_rule(smodelctx, sdata, **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

def fill_map_devices_device_inpath_rules_move_rule(inputdict, delete=False):
  mapping_dict_devices_device_inpath_rules_move_rule = {}
  mapping_dict_devices_device_inpath_rules_move_rule['from_rule_num'] = inputdict['from_rule_num']
  mapping_dict_devices_device_inpath_rules_move_rule['to_rule_num'] = inputdict['to_rule_num']
  mapping_dict_devices_device_inpath_rules_move_rule['id'] = inputdict['id']
  return mapping_dict_devices_device_inpath_rules_move_rule


def fill_up_map_devices_device_inpath_rules_move_rule(inputdict, pinputdict):
  up_mapping_dict_devices_device_inpath_rules_move_rule = {}
  up_mapping_dict_devices_device_inpath_rules_move_rule['from_rule_num'] = inputdict['from_rule_num'] if inputdict['from_rule_num'] is not None and inputdict['from_rule_num'] != '' else pinputdict['from_rule_num']
  up_mapping_dict_devices_device_inpath_rules_move_rule['to_rule_num'] = inputdict['to_rule_num'] if inputdict['to_rule_num'] is not None and inputdict['to_rule_num'] != '' else pinputdict['to_rule_num']
  up_mapping_dict_devices_device_inpath_rules_move_rule['id'] = inputdict['id'] if inputdict['id'] is not None and inputdict['id'] != '' else pinputdict['id']
  up_schema = 'key-unchanged'
  del_mandatory = False
  if inputdict['from_rule_num'] is not None and pinputdict['from_rule_num'] is not None:
    up_schema = 'key-delete-create'
    return [up_mapping_dict_devices_device_inpath_rules_move_rule, up_schema]
  elif inputdict['from_rule_num'] == '':
    up_schema = 'key-delete'
    del_mandatory = True
  elif inputdict['from_rule_num'] is not None:
    up_schema = 'key-create'
  else:
    up_schema = 'key-unchanged'
  if del_mandatory and up_schema != 'key-create':
    up_schema = 'key-delete'
  elif del_mandatory and up_schema == 'key-create':
    up_schema = 'key-delete-create'
  return [up_mapping_dict_devices_device_inpath_rules_move_rule, up_schema]


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
