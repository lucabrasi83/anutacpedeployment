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

class service_groups(object):
  #XPATH devices/device/service-groups/service-group
  class service_group(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "firewall:service-groups"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      service_group_object_list = self.validate_inputs_form_payload(mapping_dict)

      for service_group_object in service_group_object_list:
        #fetch payload
        service_group_payload = service_group_object.getxml(filter=True)
        util.log_debug('service_group_payload %s'%service_group_payload)
        payload_list.append(service_group_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "firewall:service-groups"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      service_group_object_list = self.validate_inputs_form_payload(mapping_dict)

      for service_group_object in service_group_object_list:
        #fetch payload
        service_group_payload = service_group_object.getxml(filter=True)

        util.log_debug('service_group_payload %s'%service_group_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=service_group_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "firewall:service-groups"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      service_group_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      name = mapping_dict.get('name')
      if not isinstance(name, list):
        name = [name]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for name_iterator in name:
        rcpath_tmp =  rcpath+"/service-group=%s"%(util.make_interfacename(name_iterator))
        rcpath_list.append(rcpath_tmp)
      for rc_counter, service_group_object in enumerate(service_group_object_list):
        #fetch payload
        service_group_payload = service_group_object.getxml(filter=True)

        util.log_debug('update service_group_payload %s'%service_group_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=service_group_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "firewall:service-groups"
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
        rcpath_tmp =  rcpath+"/service-group=%s"%(util.make_interfacename(name_iterator))
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
      service_group_object_list = []
      for name_iterator in name:
        from servicemodel.controller.devices.device import service_groups
        service_group_object = service_groups.service_group.service_group()
        service_group_object.name = name_iterator
        try:
          if (update == False) or (update == True and str(mapping_dict.get('device_group', None)) != ''):
            service_group_object.device_group = mapping_dict.get('device_group', None)
          else:
            service_group_object.device_group._empty_tag = True
        except TypeError:
          pass
        service_group_object_list.append(service_group_object)

      return service_group_object_list

    #XPATH devices/device/service-groups/service-group/member
    class member(AbstractDeviceMgr):
      key_hints = [['name']]
      def getRcpathPayload(self, sdata, dev, service_group_name, mapping_dict):
        dev = get_valid_devices(dev)
        if len(dev) == 0:
          return
        #Input Key Validations
        self.validate_parent_keys( service_group_name)

        #convert parent keys to list
        rcpath_list = []
        payload_list = []
        if not isinstance(service_group_name, list):
          service_group_name_list = [service_group_name]
        else:
          service_group_name_list = service_group_name

        for service_group_name in service_group_name_list:
          ##prepare rcpath
          rcpath = "firewall:service-groups/service-group=%s"%(util.make_interfacename(service_group_name))
          rcpath_list.append(rcpath)
        mapping_dict = kwargs.get('mapping_dict')

        #validating inputs and get payload object
        member_object_list = self.validate_inputs_form_payload(mapping_dict)

        for member_object in member_object_list:
          #fetch payload
          member_payload = member_object.getxml(filter=True)
          util.log_debug('member_payload %s'%member_payload)
          payload_list.append(member_payload)

        return rcpath_list, payload_list

      def create(self, sdata, dev, service_group_name, mapping_dict, addref=True, autocommit=True):
        dev = get_valid_devices(dev)
        if len(dev) == 0:
          return
        #Input Key Validations
        self.validate_parent_keys( service_group_name)

        #convert parent keys to list
        if not isinstance(service_group_name, list):
          service_group_name_list = [service_group_name]
        else:
          service_group_name_list = service_group_name

        for service_group_name in service_group_name_list:
          ##prepare rcpath
          rcpath = "firewall:service-groups/service-group=%s"%(util.make_interfacename(service_group_name))
          self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

      def create_(self, sdata, dev, **kwargs):
        mapping_dict = kwargs.get('mapping_dict')

        #validating inputs and get payload object
        member_object_list = self.validate_inputs_form_payload(mapping_dict)

        for member_object in member_object_list:
          #fetch payload
          member_payload = member_object.getxml(filter=True)

          util.log_debug('member_payload %s'%member_payload)

          #call the base abstract class for createData
          super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=member_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

      def update(self, sdata, dev, service_group_name, mapping_dict, addref=True, autocommit=True):
        dev = get_valid_devices(dev)
        if len(dev) == 0:
          return
        #Input Key Validations
        self.validate_parent_keys( service_group_name)


        ##prepare rcpath
        rcpath = "firewall:service-groups/service-group=%s"%(util.make_interfacename(service_group_name))
        self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

      def update_(self, sdata, dev, **kwargs):
        mapping_dict = kwargs.get('mapping_dict')

        #validating inputs and get payload object
        member_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

        #convert keys to list
        value = mapping_dict.get('value')
        if not isinstance(value, list):
          value = [value]

        #prepare rcpath
        rcpath = kwargs.get('rcpath')
        rcpath_list = []
        for value_iterator in value:
          rcpath_tmp =  rcpath+"/member=%s"%(util.make_interfacename(value_iterator))
          rcpath_list.append(rcpath_tmp)
        for rc_counter, member_object in enumerate(member_object_list):
          #fetch payload
          member_payload = member_object.getxml(filter=True)

          util.log_debug('update member_payload %s'%member_payload)

          rcpath = rcpath_list[rc_counter]
          #call the base abstract class for createData
          super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=member_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

      def delete(self, sdata, dev, service_group_name, mapping_dict, fail_silently=False, remove_reference=False):
        dev = get_valid_devices(dev)
        if len(dev) == 0:
          return
        #Input Key Validations
        self.validate_parent_keys( service_group_name)


        if not isinstance(service_group_name, list):
          service_group_name_list = [service_group_name]
        else:
          service_group_name_list = service_group_name

        for service_group_name in service_group_name_list:
          ##prepare rcpath
          rcpath = "firewall:service-groups/service-group=%s"%(util.make_interfacename(service_group_name))
          self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

      def delete_(self, sdata, dev, **kwargs):
        mapping_dict = kwargs.get('mapping_dict')

        #validating inputs
        if util.isEmpty(mapping_dict.get('value')):
          raise Exception("'value' cannot be empty")

        #convert keys to list
        value = mapping_dict.get('value')
        if not isinstance(value, list):
          value = [value]

        #prepare rcpath
        rcpath = kwargs.get('rcpath')
        rcpath_list = []
        for value_iterator in value:
          rcpath_tmp =  rcpath+"/member=%s"%(util.make_interfacename(value_iterator))
          rcpath_list.append(rcpath_tmp)
        payload = ''

        for rcpath in rcpath_list:
          #call the base abstract class for deleteData
          super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

      def validate_parent_keys(self, service_group_name):
        #Parent Key Validations
        if util.isEmpty(service_group_name):
          raise Exception("'service_group_name' cannot be empty")

      def validate_inputs_form_payload(self, mapping_dict, update=False):
        #validating inputs
        if util.isEmpty(mapping_dict.get('value')):
          raise Exception("'value' cannot be empty")

        #convert keys to list
        value = mapping_dict.get('value')
        if not isinstance(value, list):
          value = [value]

        #prepare payload
        member_object_list = []
        for value_iterator in value:
          from servicemodel.controller.devices.device.service_groups import service_group
          member_object = service_group.member.member()
          member_object.value = value_iterator
          member_object_list.append(member_object)

        return member_object_list

