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

#XPATH devices/device/error-disable-recovery
class error_disable_recovery(AbstractDeviceMgr):
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
    error_disable_recovery_object_list = self.validate_inputs_form_payload(mapping_dict)

    for error_disable_recovery_object in error_disable_recovery_object_list:
      #fetch payload
      error_disable_recovery_payload = error_disable_recovery_object.getxml(filter=True)
      util.log_debug('error_disable_recovery_payload %s'%error_disable_recovery_payload)
      payload_list.append(error_disable_recovery_payload)

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
    error_disable_recovery_object_list = self.validate_inputs_form_payload(mapping_dict)

    for error_disable_recovery_object in error_disable_recovery_object_list:
      #fetch payload
      error_disable_recovery_payload = error_disable_recovery_object.getxml(filter=True)

      util.log_debug('error_disable_recovery_payload %s'%error_disable_recovery_payload)

      #call the base abstract class for createData
      super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=error_disable_recovery_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

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
    error_disable_recovery_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

    #convert keys to list

    #prepare rcpath
    rcpath = kwargs.get('rcpath')
    rcpath_list = []
    rcpath_tmp =  rcpath+"/error-disable-recovery"
    rcpath_list.append(rcpath_tmp)
    for rc_counter, error_disable_recovery_object in enumerate(error_disable_recovery_object_list):
      #fetch payload
      error_disable_recovery_payload = error_disable_recovery_object.getxml(filter=True)

      util.log_debug('update error_disable_recovery_payload %s'%error_disable_recovery_payload)

      rcpath = rcpath_list[rc_counter]
      #call the base abstract class for createData
      super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=error_disable_recovery_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

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
    rcpath_tmp =  rcpath+"/error-disable-recovery"
    rcpath_list.append(rcpath_tmp)
    payload = ''

    for rcpath in rcpath_list:
      #call the base abstract class for deleteData
      super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

  def validate_inputs_form_payload(self, mapping_dict, update=False):
    #validating inputs

    #convert keys to list

    #prepare payload
    error_disable_recovery_object_list = []
    from servicemodel.controller.devices import device
    error_disable_recovery_object = device.error_disable_recovery.error_disable_recovery()
    try:
      if (update == False) or (update == True and str(mapping_dict.get('err_disable_recovery_interval', None)) != ''):
        error_disable_recovery_object.err_disable_recovery_interval = mapping_dict.get('err_disable_recovery_interval', None)
      else:
        error_disable_recovery_object.err_disable_recovery_interval._empty_tag = True
    except TypeError:
      pass
    error_disable_recovery_object_list.append(error_disable_recovery_object)

    return error_disable_recovery_object_list

  #XPATH devices/device/error-disable-recovery/error-recoverycause
  class error_recoverycause(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "basicDeviceConfigs:error-disable-recovery"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      error_recoverycause_object_list = self.validate_inputs_form_payload(mapping_dict)

      for error_recoverycause_object in error_recoverycause_object_list:
        #fetch payload
        error_recoverycause_payload = error_recoverycause_object.getxml(filter=True)
        util.log_debug('error_recoverycause_payload %s'%error_recoverycause_payload)
        payload_list.append(error_recoverycause_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "basicDeviceConfigs:error-disable-recovery"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      error_recoverycause_object_list = self.validate_inputs_form_payload(mapping_dict)

      for error_recoverycause_object in error_recoverycause_object_list:
        #fetch payload
        error_recoverycause_payload = error_recoverycause_object.getxml(filter=True)

        util.log_debug('error_recoverycause_payload %s'%error_recoverycause_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=error_recoverycause_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "basicDeviceConfigs:error-disable-recovery"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      error_recoverycause_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      error_recovery_cause = mapping_dict.get('error_recovery_cause')
      if not isinstance(error_recovery_cause, list):
        error_recovery_cause = [error_recovery_cause]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for error_recovery_cause_iterator in error_recovery_cause:
        rcpath_tmp =  rcpath+"/error-recoverycause=%s"%(util.make_interfacename(error_recovery_cause_iterator))
        rcpath_list.append(rcpath_tmp)
      for rc_counter, error_recoverycause_object in enumerate(error_recoverycause_object_list):
        #fetch payload
        error_recoverycause_payload = error_recoverycause_object.getxml(filter=True)

        util.log_debug('update error_recoverycause_payload %s'%error_recoverycause_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=error_recoverycause_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "basicDeviceConfigs:error-disable-recovery"
      self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

    def delete_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs
      if util.isEmpty(mapping_dict.get('error_recovery_cause')):
        raise Exception("'error_recovery_cause' cannot be empty")

      #convert keys to list
      error_recovery_cause = mapping_dict.get('error_recovery_cause')
      if not isinstance(error_recovery_cause, list):
        error_recovery_cause = [error_recovery_cause]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for error_recovery_cause_iterator in error_recovery_cause:
        rcpath_tmp =  rcpath+"/error-recoverycause=%s"%(util.make_interfacename(error_recovery_cause_iterator))
        rcpath_list.append(rcpath_tmp)
      payload = ''

      for rcpath in rcpath_list:
        #call the base abstract class for deleteData
        super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

    def validate_inputs_form_payload(self, mapping_dict, update=False):
      #validating inputs
      if util.isEmpty(mapping_dict.get('error_recovery_cause')):
        raise Exception("'error_recovery_cause' cannot be empty")

      #convert keys to list
      error_recovery_cause = mapping_dict.get('error_recovery_cause')
      if not isinstance(error_recovery_cause, list):
        error_recovery_cause = [error_recovery_cause]

      #prepare payload
      error_recoverycause_object_list = []
      for error_recovery_cause_iterator in error_recovery_cause:
        from servicemodel.controller.devices.device import error_disable_recovery
        error_recoverycause_object = error_disable_recovery.error_recoverycause.error_recoverycause()
        error_recoverycause_object.error_recovery_cause = error_recovery_cause_iterator
        error_recoverycause_object_list.append(error_recoverycause_object)

      return error_recoverycause_object_list

