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
#

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr
from servicemodel.abstract_dev_mgr import AbstractDeviceMgr

def get_valid_devices(devs):
  vdevs = []
  if isinstance(devs, list):
    for dev in devs:
      drivername = dev.device.get_field_value('driver_name')
      if util.isEmpty(drivername):
        vdevs.append(dev)
  else:
    drivername = devs.device.get_field_value('driver_name')
    if util.isEmpty(drivername):
      vdevs.append(devs)

  return vdevs

class vty_configs(object):
  #XPATH devices/device/vty-configs/vty-config
  class vty_config(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "basicDeviceConfigs:vty-configs"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      vty_config_object_list = self.validate_inputs_form_payload(mapping_dict)

      for vty_config_object in vty_config_object_list:
        #fetch payload
        vty_config_payload = vty_config_object.getxml(filter=True)
        util.log_debug('vty_config_payload %s'%vty_config_payload)
        payload_list.append(vty_config_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "basicDeviceConfigs:vty-configs"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      vty_config_object_list = self.validate_inputs_form_payload(mapping_dict)

      for vty_config_object in vty_config_object_list:
        #fetch payload
        vty_config_payload = vty_config_object.getxml(filter=True)

        util.log_debug('vty_config_payload %s'%vty_config_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=vty_config_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "basicDeviceConfigs:vty-configs"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      vty_config_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      name = mapping_dict.get('name')
      if not isinstance(name, list):
        name = [name]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for name_iterator in name:
        rcpath_tmp =  rcpath+"/vty-config=%s"%(util.make_interfacename(name_iterator))
        rcpath_list.append(rcpath_tmp)
      for rc_counter, vty_config_object in enumerate(vty_config_object_list):
        #fetch payload
        vty_config_payload = vty_config_object.getxml(filter=True)

        util.log_debug('update vty_config_payload %s'%vty_config_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=vty_config_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "basicDeviceConfigs:vty-configs"
      self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

    def delete_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs
      if util.isEmpty(mapping_dict.get('name')):
        raise Exception("'name' cannot be empty")

      #convert keys to list
      name = mapping_dict.get('name')
      if not isinstance(name, list):
        name = [name]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for name_iterator in name:
        rcpath_tmp =  rcpath+"/vty-config=%s"%(util.make_interfacename(name_iterator))
        rcpath_list.append(rcpath_tmp)
      payload = ''

      for rcpath in rcpath_list:
        #call the base abstract class for deleteData
        super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

    def validate_inputs_form_payload(self, mapping_dict, update=False):
      #validating inputs
      if util.isEmpty(mapping_dict.get('name')):
        raise Exception("'name' cannot be empty")

      #convert keys to list
      name = mapping_dict.get('name')
      if not isinstance(name, list):
        name = [name]

      #prepare payload
      vty_config_object_list = []
      for name_iterator in name:
        from servicemodel.controller.devices.device import vty_configs
        vty_config_object = vty_configs.vty_config.vty_config()
        vty_config_object.name = name_iterator
        try:
          if (update == False) or (update == True and str(mapping_dict.get('protocol', None)) != ''):
            vty_config_object.protocol = mapping_dict.get('protocol', None)
          else:
            vty_config_object.protocol._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('network_mask', None)) != ''):
            vty_config_object.network_mask = mapping_dict.get('network_mask', None)
          else:
            vty_config_object.network_mask._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('min_vty', None)) != ''):
            vty_config_object.min_vty = mapping_dict.get('min_vty', None)
          else:
            vty_config_object.min_vty._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('max_vty', None)) != ''):
            vty_config_object.max_vty = mapping_dict.get('max_vty', None)
          else:
            vty_config_object.max_vty._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('acl_rule_number', None)) != ''):
            vty_config_object.acl_rule_number = mapping_dict.get('acl_rule_number', None)
          else:
            vty_config_object.acl_rule_number._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('vrf', None)) != ''):
            vty_config_object.vrf = mapping_dict.get('vrf', None)
          else:
            vty_config_object.vrf._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('auth_type', None)) != ''):
            vty_config_object.auth_type = mapping_dict.get('auth_type', None)
          else:
            vty_config_object.auth_type._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('timeout', None)) != ''):
            vty_config_object.timeout = mapping_dict.get('timeout', None)
          else:
            vty_config_object.timeout._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('transport_types_in', None)) != ''):
            vty_config_object.transport_types_in = mapping_dict.get('transport_types_in', None)
          else:
            vty_config_object.transport_types_in._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('transport_types_out', None)) != ''):
            vty_config_object.transport_types_out = mapping_dict.get('transport_types_out', None)
          else:
            vty_config_object.transport_types_out._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('logging_synchronous', None)) != ''):
            vty_config_object.logging_synchronous = mapping_dict.get('logging_synchronous', None)
          else:
            vty_config_object.logging_synchronous._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('privilege_level', None)) != ''):
            vty_config_object.privilege_level = mapping_dict.get('privilege_level', None)
          else:
            vty_config_object.privilege_level._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('history_size', None)) != ''):
            vty_config_object.history_size = mapping_dict.get('history_size', None)
          else:
            vty_config_object.history_size._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('login_local', None)) != ''):
            vty_config_object.login_local = mapping_dict.get('login_local', None)
          else:
            vty_config_object.login_local._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('no_privilege_level', None)) != ''):
            vty_config_object.no_privilege_level = mapping_dict.get('no_privilege_level', None)
          else:
            vty_config_object.no_privilege_level._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('no_password', None)) != ''):
            vty_config_object.no_password = mapping_dict.get('no_password', None)
          else:
            vty_config_object.no_password._empty_tag = True
        except TypeError:
          pass
        vty_config_object_list.append(vty_config_object)

      return vty_config_object_list

