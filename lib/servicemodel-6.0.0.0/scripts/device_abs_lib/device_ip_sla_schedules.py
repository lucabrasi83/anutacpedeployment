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

class ip_sla_schedules(object):
  #XPATH devices/device/ip-sla-schedules/ip-sla-schedule
  class ip_sla_schedule(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "l3features:ip-sla-schedules"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      ip_sla_schedule_object_list = self.validate_inputs_form_payload(mapping_dict)

      for ip_sla_schedule_object in ip_sla_schedule_object_list:
        #fetch payload
        ip_sla_schedule_payload = ip_sla_schedule_object.getxml(filter=True)
        util.log_debug('ip_sla_schedule_payload %s'%ip_sla_schedule_payload)
        payload_list.append(ip_sla_schedule_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "l3features:ip-sla-schedules"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      ip_sla_schedule_object_list = self.validate_inputs_form_payload(mapping_dict)

      for ip_sla_schedule_object in ip_sla_schedule_object_list:
        #fetch payload
        ip_sla_schedule_payload = ip_sla_schedule_object.getxml(filter=True)

        util.log_debug('ip_sla_schedule_payload %s'%ip_sla_schedule_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=ip_sla_schedule_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "l3features:ip-sla-schedules"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      ip_sla_schedule_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      entry_number = mapping_dict.get('entry_number')
      if not isinstance(entry_number, list):
        entry_number = [entry_number]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for entry_number_iterator in entry_number:
        rcpath_tmp =  rcpath+"/ip-sla-schedule=%s"%(util.make_interfacename(entry_number_iterator))
        rcpath_list.append(rcpath_tmp)
      for rc_counter, ip_sla_schedule_object in enumerate(ip_sla_schedule_object_list):
        #fetch payload
        ip_sla_schedule_payload = ip_sla_schedule_object.getxml(filter=True)

        util.log_debug('update ip_sla_schedule_payload %s'%ip_sla_schedule_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=ip_sla_schedule_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "l3features:ip-sla-schedules"
      self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

    def delete_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs
      if util.isEmpty(mapping_dict.get('entry_number')):
        raise Exception("'entry_number' cannot be empty")

      #convert keys to list
      entry_number = mapping_dict.get('entry_number')
      if not isinstance(entry_number, list):
        entry_number = [entry_number]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for entry_number_iterator in entry_number:
        rcpath_tmp =  rcpath+"/ip-sla-schedule=%s"%(util.make_interfacename(entry_number_iterator))
        rcpath_list.append(rcpath_tmp)
      payload = ''

      for rcpath in rcpath_list:
        #call the base abstract class for deleteData
        super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

    def validate_inputs_form_payload(self, mapping_dict, update=False):
      #validating inputs
      if util.isEmpty(mapping_dict.get('entry_number')):
        raise Exception("'entry_number' cannot be empty")

      #convert keys to list
      entry_number = mapping_dict.get('entry_number')
      if not isinstance(entry_number, list):
        entry_number = [entry_number]

      #prepare payload
      ip_sla_schedule_object_list = []
      for entry_number_iterator in entry_number:
        from servicemodel.controller.devices.device import ip_sla_schedules
        ip_sla_schedule_object = ip_sla_schedules.ip_sla_schedule.ip_sla_schedule()
        ip_sla_schedule_object.entry_number = entry_number_iterator
        ip_sla_schedule_object_list.append(ip_sla_schedule_object)

      return ip_sla_schedule_object_list

