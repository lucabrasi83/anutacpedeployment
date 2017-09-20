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

class network_objects(object):
  #XPATH devices/device/network-objects/network-object
  class network_object(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "firewall:network-objects"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      network_object_object_list = self.validate_inputs_form_payload(mapping_dict)

      for network_object_object in network_object_object_list:
        #fetch payload
        network_object_payload = network_object_object.getxml(filter=True)
        util.log_debug('network_object_payload %s'%network_object_payload)
        payload_list.append(network_object_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "firewall:network-objects"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      network_object_object_list = self.validate_inputs_form_payload(mapping_dict)

      for network_object_object in network_object_object_list:
        #fetch payload
        network_object_payload = network_object_object.getxml(filter=True)

        util.log_debug('network_object_payload %s'%network_object_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=network_object_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "firewall:network-objects"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      network_object_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      name = mapping_dict.get('name')
      if not isinstance(name, list):
        name = [name]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for name_iterator in name:
        rcpath_tmp =  rcpath+"/network-object=%s"%(util.make_interfacename(name_iterator))
        rcpath_list.append(rcpath_tmp)
      for rc_counter, network_object_object in enumerate(network_object_object_list):
        #fetch payload
        network_object_payload = network_object_object.getxml(filter=True)

        util.log_debug('update network_object_payload %s'%network_object_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=network_object_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "firewall:network-objects"
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
        rcpath_tmp =  rcpath+"/network-object=%s"%(util.make_interfacename(name_iterator))
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
      network_object_object_list = []
      for name_iterator in name:
        from servicemodel.controller.devices.device import network_objects
        network_object_object = network_objects.network_object.network_object()
        network_object_object.name = name_iterator
        try:
          if (update == False) or (update == True and str(mapping_dict.get('description', None)) != ''):
            network_object_object.description = mapping_dict.get('description', None)
          else:
            network_object_object.description._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('vrf_name', None)) != ''):
            network_object_object.vrf_name = mapping_dict.get('vrf_name', None)
          else:
            network_object_object.vrf_name._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('object_group_name', None)) != ''):
            network_object_object.object_group_name = mapping_dict.get('object_group_name', None)
          else:
            network_object_object.object_group_name._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('type', None)) != ''):
            network_object_object.type = mapping_dict.get('type', None)
          else:
            network_object_object.type._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('ip_address', None)) != ''):
            network_object_object.ip_address = mapping_dict.get('ip_address', None)
          else:
            network_object_object.ip_address._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('netmask', None)) != ''):
            network_object_object.netmask = mapping_dict.get('netmask', None)
          else:
            network_object_object.netmask._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('tag', None)) != ''):
            network_object_object.tag = mapping_dict.get('tag', None)
          else:
            network_object_object.tag._empty_tag = True
        except TypeError:
          pass
        network_object_object_list.append(network_object_object)

      return network_object_object_list

