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

#XPATH devices/device/tacacs-conf
class tacacs_conf(AbstractDeviceMgr):
  key_hints = [[]]
  def getRcpathPayload(self, sdata, dev, mapping_dict):
    dev = get_valid_devices(dev)
    if len(dev) == 0:
      return
    #convert parent keys to list
    rcpath_list = []
    payload_list = []
    ##prepare rcpath
    rcpath = ""
    rcpath_list.append(rcpath)
    mapping_dict = kwargs.get('mapping_dict')

    #validating inputs and get payload object
    tacacs_conf_object_list = self.validate_inputs_form_payload(mapping_dict)

    for tacacs_conf_object in tacacs_conf_object_list:
      #fetch payload
      tacacs_conf_payload = tacacs_conf_object.getxml(filter=True)
      util.log_debug('tacacs_conf_payload %s'%tacacs_conf_payload)
      payload_list.append(tacacs_conf_payload)

    return rcpath_list, payload_list

  def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
    dev = get_valid_devices(dev)
    if len(dev) == 0:
      return
    #convert parent keys to list
    ##prepare rcpath
    rcpath = ""
    self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

  def create_(self, sdata, dev, **kwargs):
    mapping_dict = kwargs.get('mapping_dict')

    #validating inputs and get payload object
    tacacs_conf_object_list = self.validate_inputs_form_payload(mapping_dict)

    for tacacs_conf_object in tacacs_conf_object_list:
      #fetch payload
      tacacs_conf_payload = tacacs_conf_object.getxml(filter=True)

      util.log_debug('tacacs_conf_payload %s'%tacacs_conf_payload)

      #call the base abstract class for createData
      super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=tacacs_conf_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

  def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
    dev = get_valid_devices(dev)
    if len(dev) == 0:
      return

    ##prepare rcpath
    rcpath = ""
    self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

  def update_(self, sdata, dev, **kwargs):
    mapping_dict = kwargs.get('mapping_dict')

    #validating inputs and get payload object
    tacacs_conf_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

    #convert keys to list

    #prepare rcpath
    rcpath = kwargs.get('rcpath')
    rcpath_list = []
    rcpath_tmp =  rcpath+"/tacacs-conf"
    rcpath_list.append(rcpath_tmp)
    for rc_counter, tacacs_conf_object in enumerate(tacacs_conf_object_list):
      #fetch payload
      tacacs_conf_payload = tacacs_conf_object.getxml(filter=True)

      util.log_debug('update tacacs_conf_payload %s'%tacacs_conf_payload)

      rcpath = rcpath_list[rc_counter]
      #call the base abstract class for createData
      super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=tacacs_conf_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

  def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
    dev = get_valid_devices(dev)
    if len(dev) == 0:
      return

    ##prepare rcpath
    rcpath = ""
    self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

  def delete_(self, sdata, dev, **kwargs):
    mapping_dict = kwargs.get('mapping_dict')

    #validating inputs

    #convert keys to list

    #prepare rcpath
    rcpath = kwargs.get('rcpath')
    rcpath_list = []
    rcpath_tmp =  rcpath+"/tacacs-conf"
    rcpath_list.append(rcpath_tmp)
    payload = ''

    for rcpath in rcpath_list:
      #call the base abstract class for deleteData
      super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

  def validate_inputs_form_payload(self, mapping_dict, update=False):
    #validating inputs

    #convert keys to list

    #prepare payload
    tacacs_conf_object_list = []
    from servicemodel.controller.devices import device
    tacacs_conf_object = device.tacacs_conf.tacacs_conf()
    try:
      if (update == False) or (update == True and str(mapping_dict.get('tacacs_host_ip', None)) != ''):
        tacacs_conf_object.tacacs_host_ip = mapping_dict.get('tacacs_host_ip', None)
      else:
        tacacs_conf_object.tacacs_host_ip._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('timeout', None)) != ''):
        tacacs_conf_object.timeout = mapping_dict.get('timeout', None)
      else:
        tacacs_conf_object.timeout._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('tacacs_key', None)) != ''):
        tacacs_conf_object.tacacs_key = mapping_dict.get('tacacs_key', None)
      else:
        tacacs_conf_object.tacacs_key._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('enable_password', None)) != ''):
        tacacs_conf_object.enable_password = mapping_dict.get('enable_password', None)
      else:
        tacacs_conf_object.enable_password._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('secret_level', None)) != ''):
        tacacs_conf_object.secret_level = mapping_dict.get('secret_level', None)
      else:
        tacacs_conf_object.secret_level._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('tacacs_server_group', None)) != ''):
        tacacs_conf_object.tacacs_server_group = mapping_dict.get('tacacs_server_group', None)
      else:
        tacacs_conf_object.tacacs_server_group._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('tacacs_server_name', None)) != ''):
        tacacs_conf_object.tacacs_server_name = mapping_dict.get('tacacs_server_name', None)
      else:
        tacacs_conf_object.tacacs_server_name._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('tacacs_src_interface', None)) != ''):
        tacacs_conf_object.tacacs_src_interface = mapping_dict.get('tacacs_src_interface', None)
      else:
        tacacs_conf_object.tacacs_src_interface._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('context_name', None)) != ''):
        tacacs_conf_object.context_name = mapping_dict.get('context_name', None)
      else:
        tacacs_conf_object.context_name._empty_tag = True
    except TypeError:
      pass
    tacacs_conf_object_list.append(tacacs_conf_object)

    return tacacs_conf_object_list

  #XPATH devices/device/tacacs-conf/tacacs-servers
  class tacacs_servers(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "basicDeviceConfigs:tacacs-conf"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      tacacs_servers_object_list = self.validate_inputs_form_payload(mapping_dict)

      for tacacs_servers_object in tacacs_servers_object_list:
        #fetch payload
        tacacs_servers_payload = tacacs_servers_object.getxml(filter=True)
        util.log_debug('tacacs_servers_payload %s'%tacacs_servers_payload)
        payload_list.append(tacacs_servers_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "basicDeviceConfigs:tacacs-conf"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      tacacs_servers_object_list = self.validate_inputs_form_payload(mapping_dict)

      for tacacs_servers_object in tacacs_servers_object_list:
        #fetch payload
        tacacs_servers_payload = tacacs_servers_object.getxml(filter=True)

        util.log_debug('tacacs_servers_payload %s'%tacacs_servers_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=tacacs_servers_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "basicDeviceConfigs:tacacs-conf"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      tacacs_servers_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      tacacs_server = mapping_dict.get('tacacs_server')
      if not isinstance(tacacs_server, list):
        tacacs_server = [tacacs_server]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for tacacs_server_iterator in tacacs_server:
        rcpath_tmp =  rcpath+"/tacacs-servers=%s"%(util.make_interfacename(tacacs_server_iterator))
        rcpath_list.append(rcpath_tmp)
      for rc_counter, tacacs_servers_object in enumerate(tacacs_servers_object_list):
        #fetch payload
        tacacs_servers_payload = tacacs_servers_object.getxml(filter=True)

        util.log_debug('update tacacs_servers_payload %s'%tacacs_servers_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=tacacs_servers_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "basicDeviceConfigs:tacacs-conf"
      self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

    def delete_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs
      if util.isEmpty(mapping_dict.get('tacacs_server')):
        raise Exception("'tacacs_server' cannot be empty")

      #convert keys to list
      tacacs_server = mapping_dict.get('tacacs_server')
      if not isinstance(tacacs_server, list):
        tacacs_server = [tacacs_server]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for tacacs_server_iterator in tacacs_server:
        rcpath_tmp =  rcpath+"/tacacs-servers=%s"%(util.make_interfacename(tacacs_server_iterator))
        rcpath_list.append(rcpath_tmp)
      payload = ''

      for rcpath in rcpath_list:
        #call the base abstract class for deleteData
        super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

    def validate_inputs_form_payload(self, mapping_dict, update=False):
      #validating inputs
      if util.isEmpty(mapping_dict.get('tacacs_server')):
        raise Exception("'tacacs_server' cannot be empty")

      #convert keys to list
      tacacs_server = mapping_dict.get('tacacs_server')
      if not isinstance(tacacs_server, list):
        tacacs_server = [tacacs_server]

      #prepare payload
      tacacs_servers_object_list = []
      for tacacs_server_iterator in tacacs_server:
        from servicemodel.controller.devices.device import tacacs_conf
        tacacs_servers_object = tacacs_conf.tacacs_servers.tacacs_servers()
        tacacs_servers_object.tacacs_server = tacacs_server_iterator
        tacacs_servers_object_list.append(tacacs_servers_object)

      return tacacs_servers_object_list

