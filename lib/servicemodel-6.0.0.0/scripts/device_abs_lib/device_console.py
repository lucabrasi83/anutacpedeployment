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

#XPATH devices/device/console
class console(AbstractDeviceMgr):
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
    console_object_list = self.validate_inputs_form_payload(mapping_dict)

    for console_object in console_object_list:
      #fetch payload
      console_payload = console_object.getxml(filter=True)
      util.log_debug('console_payload %s'%console_payload)
      payload_list.append(console_payload)

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
    console_object_list = self.validate_inputs_form_payload(mapping_dict)

    for console_object in console_object_list:
      #fetch payload
      console_payload = console_object.getxml(filter=True)

      util.log_debug('console_payload %s'%console_payload)

      #call the base abstract class for createData
      super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=console_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

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
    console_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

    #convert keys to list

    #prepare rcpath
    rcpath = kwargs.get('rcpath')
    rcpath_list = []
    rcpath_tmp =  rcpath+"/console"
    rcpath_list.append(rcpath_tmp)
    for rc_counter, console_object in enumerate(console_object_list):
      #fetch payload
      console_payload = console_object.getxml(filter=True)

      util.log_debug('update console_payload %s'%console_payload)

      rcpath = rcpath_list[rc_counter]
      #call the base abstract class for createData
      super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=console_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

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
    rcpath_tmp =  rcpath+"/console"
    rcpath_list.append(rcpath_tmp)
    payload = ''

    for rcpath in rcpath_list:
      #call the base abstract class for deleteData
      super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

  def validate_inputs_form_payload(self, mapping_dict, update=False):
    #validating inputs

    #convert keys to list

    #prepare payload
    console_object_list = []
    from servicemodel.controller.devices import device
    console_object = device.console.console()
    try:
      if (update == False) or (update == True and str(mapping_dict.get('console_line', None)) != ''):
        console_object.console_line = mapping_dict.get('console_line', None)
      else:
        console_object.console_line._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('exec_timeout', None)) != ''):
        console_object.exec_timeout = mapping_dict.get('exec_timeout', None)
      else:
        console_object.exec_timeout._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('privilege_level', None)) != ''):
        console_object.privilege_level = mapping_dict.get('privilege_level', None)
      else:
        console_object.privilege_level._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('logging_synchronous', None)) != ''):
        console_object.logging_synchronous = mapping_dict.get('logging_synchronous', None)
      else:
        console_object.logging_synchronous._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('no_password', None)) != ''):
        console_object.no_password = mapping_dict.get('no_password', None)
      else:
        console_object.no_password._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('auth_type', None)) != ''):
        console_object.auth_type = mapping_dict.get('auth_type', None)
      else:
        console_object.auth_type._empty_tag = True
    except TypeError:
      pass
    console_object_list.append(console_object)

    return console_object_list

