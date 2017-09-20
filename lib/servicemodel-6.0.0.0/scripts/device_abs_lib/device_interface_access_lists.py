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

class interface_access_lists(object):
  #XPATH devices/device/interface-access-lists/interface-access-list
  class interface_access_list(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "acl:interface-access-lists"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      interface_access_list_object_list = self.validate_inputs_form_payload(mapping_dict)

      for interface_access_list_object in interface_access_list_object_list:
        #fetch payload
        interface_access_list_payload = interface_access_list_object.getxml(filter=True)
        util.log_debug('interface_access_list_payload %s'%interface_access_list_payload)
        payload_list.append(interface_access_list_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "acl:interface-access-lists"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      interface_access_list_object_list = self.validate_inputs_form_payload(mapping_dict)

      for interface_access_list_object in interface_access_list_object_list:
        #fetch payload
        interface_access_list_payload = interface_access_list_object.getxml(filter=True)

        util.log_debug('interface_access_list_payload %s'%interface_access_list_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=interface_access_list_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "acl:interface-access-lists"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      interface_access_list_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      name = mapping_dict.get('name')
      if not isinstance(name, list):
        name = [name]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for name_iterator in name:
        rcpath_tmp =  rcpath+"/interface-access-list=%s"%(util.make_interfacename(name_iterator))
        rcpath_list.append(rcpath_tmp)
      for rc_counter, interface_access_list_object in enumerate(interface_access_list_object_list):
        #fetch payload
        interface_access_list_payload = interface_access_list_object.getxml(filter=True)

        util.log_debug('update interface_access_list_payload %s'%interface_access_list_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=interface_access_list_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "acl:interface-access-lists"
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
        rcpath_tmp =  rcpath+"/interface-access-list=%s"%(util.make_interfacename(name_iterator))
        rcpath_list.append(rcpath_tmp)
      payload = ''

      for rcpath in rcpath_list:
        #call the base abstract class for deleteData
        super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

    def validate_inputs_form_payload(self, mapping_dict, update=False):
      #validating inputs
      if util.isEmpty(mapping_dict.get('name')):
        raise Exception("'name' cannot be empty")
      if util.isEmpty(mapping_dict.get('acl_name')):
        raise Exception("'acl_name' cannot be empty")
      if util.isEmpty(mapping_dict.get('interface_name')):
        raise Exception("'interface_name' cannot be empty")
      if util.isEmpty(mapping_dict.get('context_name')):
        raise Exception("'context_name' cannot be empty")
      if util.isEmpty(mapping_dict.get('direction')):
        raise Exception("'direction' cannot be empty")

      #convert keys to list
      name = mapping_dict.get('name')
      if not isinstance(name, list):
        name = [name]

      #prepare payload
      interface_access_list_object_list = []
      for name_iterator in name:
        from servicemodel.controller.devices.device import interface_access_lists
        interface_access_list_object = interface_access_lists.interface_access_list.interface_access_list()
        interface_access_list_object.name = name_iterator
        try:
          if (update == False) or (update == True and str(mapping_dict.get('acl_name', None)) != ''):
            interface_access_list_object.acl_name = mapping_dict.get('acl_name', None)
          else:
            interface_access_list_object.acl_name._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('interface_name', None)) != ''):
            interface_access_list_object.interface_name = mapping_dict.get('interface_name', None)
          else:
            interface_access_list_object.interface_name._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('context_name', None)) != ''):
            interface_access_list_object.context_name = mapping_dict.get('context_name', None)
          else:
            interface_access_list_object.context_name._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('direction', None)) != ''):
            interface_access_list_object.direction = mapping_dict.get('direction', None)
          else:
            interface_access_list_object.direction._empty_tag = True
        except TypeError:
          pass
        interface_access_list_object_list.append(interface_access_list_object)

      return interface_access_list_object_list

