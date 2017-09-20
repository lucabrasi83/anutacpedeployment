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

#XPATH devices/device/aaa-root
class aaa_root(AbstractDeviceMgr):
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
    aaa_root_object_list = self.validate_inputs_form_payload(mapping_dict)

    for aaa_root_object in aaa_root_object_list:
      #fetch payload
      aaa_root_payload = aaa_root_object.getxml(filter=True)
      util.log_debug('aaa_root_payload %s'%aaa_root_payload)
      payload_list.append(aaa_root_payload)

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
    aaa_root_object_list = self.validate_inputs_form_payload(mapping_dict)

    for aaa_root_object in aaa_root_object_list:
      #fetch payload
      aaa_root_payload = aaa_root_object.getxml(filter=True)

      util.log_debug('aaa_root_payload %s'%aaa_root_payload)

      #call the base abstract class for createData
      super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=aaa_root_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

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
    aaa_root_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

    #convert keys to list

    #prepare rcpath
    rcpath = kwargs.get('rcpath')
    rcpath_list = []
    rcpath_tmp =  rcpath+"/aaa-root"
    rcpath_list.append(rcpath_tmp)
    for rc_counter, aaa_root_object in enumerate(aaa_root_object_list):
      #fetch payload
      aaa_root_payload = aaa_root_object.getxml(filter=True)

      util.log_debug('update aaa_root_payload %s'%aaa_root_payload)

      rcpath = rcpath_list[rc_counter]
      #call the base abstract class for createData
      super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=aaa_root_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

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
    rcpath_tmp =  rcpath+"/aaa-root"
    rcpath_list.append(rcpath_tmp)
    payload = ''

    for rcpath in rcpath_list:
      #call the base abstract class for deleteData
      super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

  def validate_inputs_form_payload(self, mapping_dict, update=False):
    #validating inputs

    #convert keys to list

    #prepare payload
    aaa_root_object_list = []
    from servicemodel.controller.devices import device
    aaa_root_object = device.aaa_root.aaa_root()
    try:
      if (update == False) or (update == True and str(mapping_dict.get('root_disable', None)) != ''):
        aaa_root_object.root_disable = mapping_dict.get('root_disable', None)
      else:
        aaa_root_object.root_disable._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('password', None)) != ''):
        aaa_root_object.password = mapping_dict.get('password', None)
      else:
        aaa_root_object.password._empty_tag = True
    except TypeError:
      pass
    try:
      if (update == False) or (update == True and str(mapping_dict.get('secret_level', None)) != ''):
        aaa_root_object.secret_level = mapping_dict.get('secret_level', None)
      else:
        aaa_root_object.secret_level._empty_tag = True
    except TypeError:
      pass
    aaa_root_object_list.append(aaa_root_object)

    return aaa_root_object_list

