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

class ip_prefixlist_list(object):
  #XPATH devices/device/ip-prefixlist-list/ip-prefixlist
  class ip_prefixlist(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "l3features:ip-prefixlist-list"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      ip_prefixlist_object_list = self.validate_inputs_form_payload(mapping_dict)

      for ip_prefixlist_object in ip_prefixlist_object_list:
        #fetch payload
        ip_prefixlist_payload = ip_prefixlist_object.getxml(filter=True)
        util.log_debug('ip_prefixlist_payload %s'%ip_prefixlist_payload)
        payload_list.append(ip_prefixlist_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "l3features:ip-prefixlist-list"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      ip_prefixlist_object_list = self.validate_inputs_form_payload(mapping_dict)

      for ip_prefixlist_object in ip_prefixlist_object_list:
        #fetch payload
        ip_prefixlist_payload = ip_prefixlist_object.getxml(filter=True)

        util.log_debug('ip_prefixlist_payload %s'%ip_prefixlist_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=ip_prefixlist_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "l3features:ip-prefixlist-list"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      ip_prefixlist_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      name = mapping_dict.get('name')
      if not isinstance(name, list):
        name = [name]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for name_iterator in name:
        rcpath_tmp =  rcpath+"/ip-prefixlist=%s"%(util.make_interfacename(name_iterator))
        rcpath_list.append(rcpath_tmp)
      for rc_counter, ip_prefixlist_object in enumerate(ip_prefixlist_object_list):
        #fetch payload
        ip_prefixlist_payload = ip_prefixlist_object.getxml(filter=True)

        util.log_debug('update ip_prefixlist_payload %s'%ip_prefixlist_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=ip_prefixlist_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "l3features:ip-prefixlist-list"
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
        rcpath_tmp =  rcpath+"/ip-prefixlist=%s"%(util.make_interfacename(name_iterator))
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
      ip_prefixlist_object_list = []
      for name_iterator in name:
        from servicemodel.controller.devices.device import ip_prefixlist_list
        ip_prefixlist_object = ip_prefixlist_list.ip_prefixlist.ip_prefixlist()
        ip_prefixlist_object.name = name_iterator
        ip_prefixlist_object_list.append(ip_prefixlist_object)

      return ip_prefixlist_object_list

    class ip_prefixlist_entries(object):
      #XPATH devices/device/ip-prefixlist-list/ip-prefixlist/ip-prefixlist-entries/ip-prefixlist-entry
      class ip_prefixlist_entry(AbstractDeviceMgr):
        key_hints = [['name']]
        def getRcpathPayload(self, sdata, dev, ip_prefixlist_name, mapping_dict):
          dev = get_valid_devices(dev)
          if len(dev) == 0:
            return
          #Input Key Validations
          self.validate_parent_keys( ip_prefixlist_name)

          #convert parent keys to list
          rcpath_list = []
          payload_list = []
          if not isinstance(ip_prefixlist_name, list):
            ip_prefixlist_name_list = [ip_prefixlist_name]
          else:
            ip_prefixlist_name_list = ip_prefixlist_name

          for ip_prefixlist_name in ip_prefixlist_name_list:
            ##prepare rcpath
            rcpath = "l3features:ip-prefixlist-list/ip-prefixlist=%s/ip-prefixlist-entries"%(util.make_interfacename(ip_prefixlist_name))
            rcpath_list.append(rcpath)
          mapping_dict = kwargs.get('mapping_dict')

          #validating inputs and get payload object
          ip_prefixlist_entry_object_list = self.validate_inputs_form_payload(mapping_dict)

          for ip_prefixlist_entry_object in ip_prefixlist_entry_object_list:
            #fetch payload
            ip_prefixlist_entry_payload = ip_prefixlist_entry_object.getxml(filter=True)
            util.log_debug('ip_prefixlist_entry_payload %s'%ip_prefixlist_entry_payload)
            payload_list.append(ip_prefixlist_entry_payload)

          return rcpath_list, payload_list

        def create(self, sdata, dev, ip_prefixlist_name, mapping_dict, addref=True, autocommit=True):
          dev = get_valid_devices(dev)
          if len(dev) == 0:
            return
          #Input Key Validations
          self.validate_parent_keys( ip_prefixlist_name)

          #convert parent keys to list
          if not isinstance(ip_prefixlist_name, list):
            ip_prefixlist_name_list = [ip_prefixlist_name]
          else:
            ip_prefixlist_name_list = ip_prefixlist_name

          for ip_prefixlist_name in ip_prefixlist_name_list:
            ##prepare rcpath
            rcpath = "l3features:ip-prefixlist-list/ip-prefixlist=%s/ip-prefixlist-entries"%(util.make_interfacename(ip_prefixlist_name))
            self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

        def create_(self, sdata, dev, **kwargs):
          mapping_dict = kwargs.get('mapping_dict')

          #validating inputs and get payload object
          ip_prefixlist_entry_object_list = self.validate_inputs_form_payload(mapping_dict)

          for ip_prefixlist_entry_object in ip_prefixlist_entry_object_list:
            #fetch payload
            ip_prefixlist_entry_payload = ip_prefixlist_entry_object.getxml(filter=True)

            util.log_debug('ip_prefixlist_entry_payload %s'%ip_prefixlist_entry_payload)

            #call the base abstract class for createData
            super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=ip_prefixlist_entry_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

        def update(self, sdata, dev, ip_prefixlist_name, mapping_dict, addref=True, autocommit=True):
          dev = get_valid_devices(dev)
          if len(dev) == 0:
            return
          #Input Key Validations
          self.validate_parent_keys( ip_prefixlist_name)


          ##prepare rcpath
          rcpath = "l3features:ip-prefixlist-list/ip-prefixlist=%s/ip-prefixlist-entries"%(util.make_interfacename(ip_prefixlist_name))
          self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

        def update_(self, sdata, dev, **kwargs):
          mapping_dict = kwargs.get('mapping_dict')

          #validating inputs and get payload object
          ip_prefixlist_entry_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

          #convert keys to list
          rule_num = mapping_dict.get('rule_num')
          if not isinstance(rule_num, list):
            rule_num = [rule_num]

          #prepare rcpath
          rcpath = kwargs.get('rcpath')
          rcpath_list = []
          for rule_num_iterator in rule_num:
            rcpath_tmp =  rcpath+"/ip-prefixlist-entry=%s"%(util.make_interfacename(rule_num_iterator))
            rcpath_list.append(rcpath_tmp)
          for rc_counter, ip_prefixlist_entry_object in enumerate(ip_prefixlist_entry_object_list):
            #fetch payload
            ip_prefixlist_entry_payload = ip_prefixlist_entry_object.getxml(filter=True)

            util.log_debug('update ip_prefixlist_entry_payload %s'%ip_prefixlist_entry_payload)

            rcpath = rcpath_list[rc_counter]
            #call the base abstract class for createData
            super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=ip_prefixlist_entry_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

        def delete(self, sdata, dev, ip_prefixlist_name, mapping_dict, fail_silently=False, remove_reference=False):
          dev = get_valid_devices(dev)
          if len(dev) == 0:
            return
          #Input Key Validations
          self.validate_parent_keys( ip_prefixlist_name)


          if not isinstance(ip_prefixlist_name, list):
            ip_prefixlist_name_list = [ip_prefixlist_name]
          else:
            ip_prefixlist_name_list = ip_prefixlist_name

          for ip_prefixlist_name in ip_prefixlist_name_list:
            ##prepare rcpath
            rcpath = "l3features:ip-prefixlist-list/ip-prefixlist=%s/ip-prefixlist-entries"%(util.make_interfacename(ip_prefixlist_name))
            self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

        def delete_(self, sdata, dev, **kwargs):
          mapping_dict = kwargs.get('mapping_dict')

          #validating inputs
          if util.isEmpty(mapping_dict.get('rule_num')):
            raise Exception("'rule_num' cannot be empty")

          #convert keys to list
          rule_num = mapping_dict.get('rule_num')
          if not isinstance(rule_num, list):
            rule_num = [rule_num]

          #prepare rcpath
          rcpath = kwargs.get('rcpath')
          rcpath_list = []
          for rule_num_iterator in rule_num:
            rcpath_tmp =  rcpath+"/ip-prefixlist-entry=%s"%(util.make_interfacename(rule_num_iterator))
            rcpath_list.append(rcpath_tmp)
          payload = ''

          for rcpath in rcpath_list:
            #call the base abstract class for deleteData
            super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

        def validate_parent_keys(self, ip_prefixlist_name):
          #Parent Key Validations
          if util.isEmpty(ip_prefixlist_name):
            raise Exception("'ip_prefixlist_name' cannot be empty")

        def validate_inputs_form_payload(self, mapping_dict, update=False):
          #validating inputs
          if util.isEmpty(mapping_dict.get('rule_num')):
            raise Exception("'rule_num' cannot be empty")

          #convert keys to list
          rule_num = mapping_dict.get('rule_num')
          if not isinstance(rule_num, list):
            rule_num = [rule_num]

          #prepare payload
          ip_prefixlist_entry_object_list = []
          for rule_num_iterator in rule_num:
            from servicemodel.controller.devices.device.ip_prefixlist_list.ip_prefixlist import ip_prefixlist_entries
            ip_prefixlist_entry_object = ip_prefixlist_entries.ip_prefixlist_entry.ip_prefixlist_entry()
            try:
              if (update == False) or (update == True and str(mapping_dict.get('prefix_name', None)) != ''):
                ip_prefixlist_entry_object.prefix_name = mapping_dict.get('prefix_name', None)
              else:
                ip_prefixlist_entry_object.prefix_name._empty_tag = True
            except TypeError:
              pass
            ip_prefixlist_entry_object.rule_num = rule_num_iterator
            try:
              if (update == False) or (update == True and str(mapping_dict.get('subnet', None)) != ''):
                ip_prefixlist_entry_object.subnet = mapping_dict.get('subnet', None)
              else:
                ip_prefixlist_entry_object.subnet._empty_tag = True
            except TypeError:
              pass
            try:
              if (update == False) or (update == True and str(mapping_dict.get('compare', None)) != ''):
                ip_prefixlist_entry_object.compare = mapping_dict.get('compare', None)
              else:
                ip_prefixlist_entry_object.compare._empty_tag = True
            except TypeError:
              pass
            try:
              if (update == False) or (update == True and str(mapping_dict.get('num', None)) != ''):
                ip_prefixlist_entry_object.num = mapping_dict.get('num', None)
              else:
                ip_prefixlist_entry_object.num._empty_tag = True
            except TypeError:
              pass
            try:
              if (update == False) or (update == True and str(mapping_dict.get('condition', None)) != ''):
                ip_prefixlist_entry_object.condition = mapping_dict.get('condition', None)
              else:
                ip_prefixlist_entry_object.condition._empty_tag = True
            except TypeError:
              pass
            ip_prefixlist_entry_object_list.append(ip_prefixlist_entry_object)

          return ip_prefixlist_entry_object_list

