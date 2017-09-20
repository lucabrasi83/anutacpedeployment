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
                                                  type1-site
                                                            |
                                                            type1-site
                                                                      |
                                                                      wanop
                                                                           |
                                                                           inpath-rules
                                                                                       |
                                                                                       inpath-rules
                                                                                                   
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/type1-site/type1-site/wanop/inpath-rules/inpath-rules
"""
"""
Names of Leafs for this Yang Entity
           rule-type            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/rule-type
     packet-mode-uni            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/packet-mode-uni
             srcaddr            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/srcaddr
             srcport            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/srcport
             dstaddr            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/dstaddr
             dstport            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/dstport
          dst-domain            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/dst-domain
            dst-host            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/dst-host
        optimization            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/optimization
     preoptimization            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/preoptimization
         latency-opt            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/latency-opt
                vlan            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/vlan
         neural-mode            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/neural-mode
         cloud-accel            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/cloud-accel
           web-proxy            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/web-proxy
      wan-visibility            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/wan-visibility
         description            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/description
        auto-kickoff            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/auto-kickoff
         rule-enable            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/rule-enable
             rulenum            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/rulenum
            protocol            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/protocol
         target-addr            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/target-addr
         target-port            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/target-port
         backup-addr            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/backup-addr
         backup-port            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/backup-port

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
      if dev is None or (isinstance(dev, list) and len(dev) == 0):
        return
      if inputdict.get('srcport') is not None:
        from cpedeployment.managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label
        set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label(inputdict.get('srcport'), dev, sdata, id, **opaque_args)

      if inputdict.get('dstport') is not None:
        from cpedeployment.managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label
        set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label(inputdict.get('dstport'), dev, sdata, id, **opaque_args)

      if inputdict.get('dst_domain') is not None:
        from cpedeployment.managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_domain_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_domain_label
        set_specific_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_domain_label(inputdict.get('dst_domain'), dev, sdata, id, **opaque_args)

      if inputdict.get('dst_host') is not None:
        from cpedeployment.managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label
        set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label(inputdict.get('dst_host'), dev, sdata, id, **opaque_args)

      if inputdict.get('target_port') is not None:
        from cpedeployment.managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label
        set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label(inputdict.get('target_port'), dev, sdata, id, **opaque_args)

      if inputdict.get('backup_port') is not None:
        from cpedeployment.managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label
        set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label(inputdict.get('backup_port'), dev, sdata, id, **opaque_args)

      import cpedeployment.cpedeployment_grouping_lib.inpath_rules_def_customization
      cpedeployment.cpedeployment_grouping_lib.inpath_rules_def_customization.grouping_create_inpath_rules_def_inpath_rules(smodelctx, sdata, dev, **kwargs)

      from servicemodel.device_abs_lib import device_inpath_rules
      if inputdict['rulenum'] is not None:
        device_inpath_rules.inpath_rules.inpath_rules_def().create(sdata, dev, fill_map_devices_device_inpath_rules_inpath_rules_def(inputdict), addref=True)

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

      #Previous config and previous inputdict
      pconfig = kwargs['pconfig']
      pinputdict = kwargs['pinputdict']

      dev = kwargs['dev']
      if dev is None or (isinstance(dev, list) and len(dev) == 0):
        return
      from servicemodel.device_abs_lib import device_inpath_rules
      up_map_devices_device_inpath_rules_inpath_rules_def = fill_up_map_devices_device_inpath_rules_inpath_rules_def(inputdict, pinputdict)
      if up_map_devices_device_inpath_rules_inpath_rules_def[1] == 'key-delete-create' or up_map_devices_device_inpath_rules_inpath_rules_def[1] == 'key-delete':
        device_inpath_rules.inpath_rules.inpath_rules_def().delete(sdata, dev, pinputdict)
      if up_map_devices_device_inpath_rules_inpath_rules_def[1] == 'key-delete-create' or up_map_devices_device_inpath_rules_inpath_rules_def[1] == 'key-create':
        device_inpath_rules.inpath_rules.inpath_rules_def().create(sdata, dev, up_map_devices_device_inpath_rules_inpath_rules_def[0], addref=up_map_devices_device_inpath_rules_inpath_rules_def)
      if up_map_devices_device_inpath_rules_inpath_rules_def[1] == 'key-unchanged':
        device_inpath_rules.inpath_rules.inpath_rules_def().update(sdata, dev, fill_map_devices_device_inpath_rules_inpath_rules_def(inputdict, pinputdict, update=True))

      if inputdict.get('srcport') is not None:
        from cpedeployment.managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label
        set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label(inputdict.get('srcport'), dev, sdata, id, **opaque_args)

      if inputdict.get('dstport') is not None:
        from cpedeployment.managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label
        set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label(inputdict.get('dstport'), dev, sdata, id, **opaque_args)

      if inputdict.get('dst_domain') is not None:
        from cpedeployment.managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_domain_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_domain_label
        set_specific_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_domain_label(inputdict.get('dst_domain'), dev, sdata, id, **opaque_args)

      if inputdict.get('dst_host') is not None:
        from cpedeployment.managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label
        set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label(inputdict.get('dst_host'), dev, sdata, id, **opaque_args)

      if inputdict.get('target_port') is not None:
        from cpedeployment.managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label
        set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label(inputdict.get('target_port'), dev, sdata, id, **opaque_args)

      if inputdict.get('backup_port') is not None:
        from cpedeployment.managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label_lib import set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label
        set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label(inputdict.get('backup_port'), dev, sdata, id, **opaque_args)
      import cpedeployment.cpedeployment_grouping_lib.inpath_rules_def_customization
      cpedeployment.cpedeployment_grouping_lib.inpath_rules_def_customization.grouping_update_inpath_rules_def_inpath_rules(smodelctx, sdata, **kwargs)

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
      if dev is None or (isinstance(dev, list) and len(dev) == 0):
        return
      import cpedeployment.cpedeployment_grouping_lib.inpath_rules_def_customization
      cpedeployment.cpedeployment_grouping_lib.inpath_rules_def_customization.grouping_delete_inpath_rules_def_inpath_rules(smodelctx, sdata, **kwargs)

def fill_map_devices_device_inpath_rules_inpath_rules_def(inputdict, pinputdict={}, delete=False, update=False):
  mapping_dict_devices_device_inpath_rules_inpath_rules_def = {}
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['auto_kickoff'] = inputdict['auto_kickoff'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['protocol'] = inputdict['protocol'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['backup_addr'] = inputdict['backup_addr'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['cloud_accel'] = inputdict['cloud_accel'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['preoptimization'] = inputdict['preoptimization'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['target_addr'] = inputdict['target_addr'] if not update else inputdict['target_addr'] if inputdict['target_addr'] is not None else pinputdict['target_addr']
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['packet_mode_uni'] = inputdict['packet_mode_uni'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['srcport'] = inputdict['srcport'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['wan_visibility'] = inputdict['wan_visibility'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['rule_enable'] = inputdict['rule_enable'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['dst_host'] = inputdict['dst_host'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['web_proxy'] = inputdict['web_proxy'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['dstaddr'] = inputdict['dstaddr'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['dst_domain'] = inputdict['dst_domain'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['latency_opt'] = inputdict['latency_opt'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['target_port'] = inputdict['target_port'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['neural_mode'] = inputdict['neural_mode'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['description'] = inputdict['description'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['optimization'] = inputdict['optimization'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['backup_port'] = inputdict['backup_port'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['dstport'] = inputdict['dstport'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['rulenum'] = inputdict['rulenum'] if not update else inputdict['rulenum'] if inputdict['rulenum'] is not None else pinputdict['rulenum']
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['vlan'] = inputdict['vlan'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['rule_type'] = inputdict['rule_type'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['srcaddr'] = inputdict['srcaddr'] if not delete else ''
  mapping_dict_devices_device_inpath_rules_inpath_rules_def['wan_vis_opt'] = inputdict['wan_vis_opt'] if not delete else ''
  return mapping_dict_devices_device_inpath_rules_inpath_rules_def


def fill_up_map_devices_device_inpath_rules_inpath_rules_def(inputdict, pinputdict):
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def = {}
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['auto_kickoff'] = inputdict['auto_kickoff']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['protocol'] = inputdict['protocol']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['backup_addr'] = inputdict['backup_addr']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['cloud_accel'] = inputdict['cloud_accel']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['preoptimization'] = inputdict['preoptimization']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['target_addr'] = inputdict['target_addr'] if inputdict['target_addr'] is not None and inputdict['target_addr'] != '' else pinputdict['target_addr']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['packet_mode_uni'] = inputdict['packet_mode_uni']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['srcport'] = inputdict['srcport']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['wan_visibility'] = inputdict['wan_visibility']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['rule_enable'] = inputdict['rule_enable']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['dst_host'] = inputdict['dst_host']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['web_proxy'] = inputdict['web_proxy']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['dstaddr'] = inputdict['dstaddr']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['dst_domain'] = inputdict['dst_domain']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['latency_opt'] = inputdict['latency_opt']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['target_port'] = inputdict['target_port']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['neural_mode'] = inputdict['neural_mode']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['description'] = inputdict['description']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['optimization'] = inputdict['optimization']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['backup_port'] = inputdict['backup_port']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['dstport'] = inputdict['dstport']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['rulenum'] = inputdict['rulenum'] if inputdict['rulenum'] is not None and inputdict['rulenum'] != '' else pinputdict['rulenum']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['vlan'] = inputdict['vlan']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['rule_type'] = inputdict['rule_type']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['srcaddr'] = inputdict['srcaddr']
  up_mapping_dict_devices_device_inpath_rules_inpath_rules_def['wan_vis_opt'] = inputdict['wan_vis_opt']

  if inputdict['auto_kickoff'] is None and inputdict['protocol'] is None and inputdict['backup_addr'] is None and inputdict['cloud_accel'] is None and inputdict['preoptimization'] is None and inputdict['target_addr'] is None and inputdict['packet_mode_uni'] is None and inputdict['srcport'] is None and inputdict['wan_visibility'] is None and inputdict['rule_enable'] is None and inputdict['dst_host'] is None and inputdict['web_proxy'] is None and inputdict['dstaddr'] is None and inputdict['dst_domain'] is None and inputdict['latency_opt'] is None and inputdict['target_port'] is None and inputdict['neural_mode'] is None and inputdict['description'] is None and inputdict['optimization'] is None and inputdict['backup_port'] is None and inputdict['dstport'] is None and inputdict['rulenum'] is None and inputdict['vlan'] is None and inputdict['rule_type'] is None and inputdict['srcaddr'] is None:
    return [up_mapping_dict_devices_device_inpath_rules_inpath_rules_def, 'no-change']
  up_schema = 'key-unchanged'
  del_mandatory = False
  if inputdict['rulenum'] is not None and pinputdict['rulenum'] is not None:
    up_schema = 'key-delete-create'
    return [up_mapping_dict_devices_device_inpath_rules_inpath_rules_def, up_schema]
  elif inputdict['rulenum'] == '':
    up_schema = 'key-delete'
    del_mandatory = True
  elif inputdict['rulenum'] is not None:
    up_schema = 'key-create'
  else:
    up_schema = 'key-unchanged'
  if del_mandatory and up_schema != 'key-create':
    up_schema = 'key-delete'
  elif del_mandatory and up_schema == 'key-create':
    up_schema = 'key-delete-create'
  return [up_mapping_dict_devices_device_inpath_rules_inpath_rules_def, up_schema]


class DeletePreProcessor(yang.SessionPreProcessor):
  def processBeforeReserve(self, session):
    operations = session.getOperations()
    """Add any move operations for Deletion"""
    yang.moveOperations(operations, ['DeleteHostLabel', 'DeletePortLabel', 'DeleteDomainLabel'], ['DeleteInpathRule', 'DeleteApplication'], True)
    log('operations: %s' % (operations))

class CreatePreProcessor(yang.SessionPreProcessor):
  def processBeforeReserve(self, session):
    operations = session.getOperations()
    """Add any move operations for creation"""
    log('operations: %s' % (operations))