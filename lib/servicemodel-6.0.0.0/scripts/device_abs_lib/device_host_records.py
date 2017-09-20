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

class host_records(object):
  #XPATH devices/device/host-records/host-record
  class host_record(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "dns:host-records"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      host_record_object_list = self.validate_inputs_form_payload(mapping_dict)

      for host_record_object in host_record_object_list:
        #fetch payload
        host_record_payload = host_record_object.getxml(filter=True)
        util.log_debug('host_record_payload %s'%host_record_payload)
        payload_list.append(host_record_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "dns:host-records"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      host_record_object_list = self.validate_inputs_form_payload(mapping_dict)

      for host_record_object in host_record_object_list:
        #fetch payload
        host_record_payload = host_record_object.getxml(filter=True)

        util.log_debug('host_record_payload %s'%host_record_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=host_record_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "dns:host-records"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      host_record_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      fqdn = mapping_dict.get('fqdn')
      if not isinstance(fqdn, list):
        fqdn = [fqdn]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for fqdn_iterator in fqdn:
        rcpath_tmp =  rcpath+"/host-record=%s"%(util.make_interfacename(fqdn_iterator))
        rcpath_list.append(rcpath_tmp)
      for rc_counter, host_record_object in enumerate(host_record_object_list):
        #fetch payload
        host_record_payload = host_record_object.getxml(filter=True)

        util.log_debug('update host_record_payload %s'%host_record_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=host_record_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "dns:host-records"
      self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

    def delete_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs
      if util.isEmpty(mapping_dict.get('fqdn')):
        raise Exception("'fqdn' cannot be empty")

      #convert keys to list
      fqdn = mapping_dict.get('fqdn')
      if not isinstance(fqdn, list):
        fqdn = [fqdn]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for fqdn_iterator in fqdn:
        rcpath_tmp =  rcpath+"/host-record=%s"%(util.make_interfacename(fqdn_iterator))
        rcpath_list.append(rcpath_tmp)
      payload = ''

      for rcpath in rcpath_list:
        #call the base abstract class for deleteData
        super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

    def validate_inputs_form_payload(self, mapping_dict, update=False):
      #validating inputs
      if util.isEmpty(mapping_dict.get('fqdn')):
        raise Exception("'fqdn' cannot be empty")
      if util.isEmpty(mapping_dict.get('ip_address')):
        raise Exception("'ip_address' cannot be empty")
      if util.isEmpty(mapping_dict.get('view')):
        raise Exception("'view' cannot be empty")

      #convert keys to list
      fqdn = mapping_dict.get('fqdn')
      if not isinstance(fqdn, list):
        fqdn = [fqdn]

      #prepare payload
      host_record_object_list = []
      for fqdn_iterator in fqdn:
        from servicemodel.controller.devices.device import host_records
        host_record_object = host_records.host_record.host_record()
        host_record_object.fqdn = fqdn_iterator
        try:
          if (update == False) or (update == True and str(mapping_dict.get('ip_address', None)) != ''):
            host_record_object.ip_address = mapping_dict.get('ip_address', None)
          else:
            host_record_object.ip_address._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('view', None)) != ''):
            host_record_object.view = mapping_dict.get('view', None)
          else:
            host_record_object.view._empty_tag = True
        except TypeError:
          pass
        host_record_object_list.append(host_record_object)

      return host_record_object_list

