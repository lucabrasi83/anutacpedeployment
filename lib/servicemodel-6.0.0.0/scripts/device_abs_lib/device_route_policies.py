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

class route_policies(object):
  #XPATH devices/device/route-policies/route-policy
  class route_policy(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "l3features:route-policies"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      route_policy_object_list = self.validate_inputs_form_payload(mapping_dict)

      for route_policy_object in route_policy_object_list:
        #fetch payload
        route_policy_payload = route_policy_object.getxml(filter=True)
        util.log_debug('route_policy_payload %s'%route_policy_payload)
        payload_list.append(route_policy_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "l3features:route-policies"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      route_policy_object_list = self.validate_inputs_form_payload(mapping_dict)

      for route_policy_object in route_policy_object_list:
        #fetch payload
        route_policy_payload = route_policy_object.getxml(filter=True)

        util.log_debug('route_policy_payload %s'%route_policy_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=route_policy_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "l3features:route-policies"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      route_policy_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      name = mapping_dict.get('name')
      if not isinstance(name, list):
        name = [name]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for name_iterator in name:
        rcpath_tmp =  rcpath+"/route-policy=%s"%(util.make_interfacename(name_iterator))
        rcpath_list.append(rcpath_tmp)
      for rc_counter, route_policy_object in enumerate(route_policy_object_list):
        #fetch payload
        route_policy_payload = route_policy_object.getxml(filter=True)

        util.log_debug('update route_policy_payload %s'%route_policy_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=route_policy_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "l3features:route-policies"
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
        rcpath_tmp =  rcpath+"/route-policy=%s"%(util.make_interfacename(name_iterator))
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
      route_policy_object_list = []
      for name_iterator in name:
        from servicemodel.controller.devices.device import route_policies
        route_policy_object = route_policies.route_policy.route_policy()
        route_policy_object.name = name_iterator
        try:
          if (update == False) or (update == True and str(mapping_dict.get('cpl_string', None)) != ''):
            route_policy_object.cpl_string = mapping_dict.get('cpl_string', None)
          else:
            route_policy_object.cpl_string._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('skip_cpl_string', None)) != ''):
            route_policy_object.skip_cpl_string = mapping_dict.get('skip_cpl_string', None)
          else:
            route_policy_object.skip_cpl_string._empty_tag = True
        except TypeError:
          pass
        route_policy_object_list.append(route_policy_object)

      return route_policy_object_list

    #XPATH devices/device/route-policies/route-policy/route-policy-entries
    class route_policy_entries(AbstractDeviceMgr):
      key_hints = [['name']]
      def getRcpathPayload(self, sdata, dev, route_policy_name, mapping_dict):
        dev = get_valid_devices(dev)
        if len(dev) == 0:
          return
        #Input Key Validations
        self.validate_parent_keys( route_policy_name)

        #convert parent keys to list
        rcpath_list = []
        payload_list = []
        if not isinstance(route_policy_name, list):
          route_policy_name_list = [route_policy_name]
        else:
          route_policy_name_list = route_policy_name

        for route_policy_name in route_policy_name_list:
          ##prepare rcpath
          rcpath = "l3features:route-policies/route-policy=%s"%(util.make_interfacename(route_policy_name))
          rcpath_list.append(rcpath)
        mapping_dict = kwargs.get('mapping_dict')

        #validating inputs and get payload object
        route_policy_entries_object_list = self.validate_inputs_form_payload(mapping_dict)

        for route_policy_entries_object in route_policy_entries_object_list:
          #fetch payload
          route_policy_entries_payload = route_policy_entries_object.getxml(filter=True)
          util.log_debug('route_policy_entries_payload %s'%route_policy_entries_payload)
          payload_list.append(route_policy_entries_payload)

        return rcpath_list, payload_list

      def create(self, sdata, dev, route_policy_name, mapping_dict, addref=True, autocommit=True):
        dev = get_valid_devices(dev)
        if len(dev) == 0:
          return
        #Input Key Validations
        self.validate_parent_keys( route_policy_name)

        #convert parent keys to list
        if not isinstance(route_policy_name, list):
          route_policy_name_list = [route_policy_name]
        else:
          route_policy_name_list = route_policy_name

        for route_policy_name in route_policy_name_list:
          ##prepare rcpath
          rcpath = "l3features:route-policies/route-policy=%s"%(util.make_interfacename(route_policy_name))
          self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

      def create_(self, sdata, dev, **kwargs):
        mapping_dict = kwargs.get('mapping_dict')

        #validating inputs and get payload object
        route_policy_entries_object_list = self.validate_inputs_form_payload(mapping_dict)

        for route_policy_entries_object in route_policy_entries_object_list:
          #fetch payload
          route_policy_entries_payload = route_policy_entries_object.getxml(filter=True)

          util.log_debug('route_policy_entries_payload %s'%route_policy_entries_payload)

          #call the base abstract class for createData
          super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=route_policy_entries_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

      def update(self, sdata, dev, route_policy_name, mapping_dict, addref=True, autocommit=True):
        dev = get_valid_devices(dev)
        if len(dev) == 0:
          return
        #Input Key Validations
        self.validate_parent_keys( route_policy_name)


        ##prepare rcpath
        rcpath = "l3features:route-policies/route-policy=%s"%(util.make_interfacename(route_policy_name))
        self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

      def update_(self, sdata, dev, **kwargs):
        mapping_dict = kwargs.get('mapping_dict')

        #validating inputs and get payload object
        route_policy_entries_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

        #convert keys to list
        med = mapping_dict.get('med')
        if not isinstance(med, list):
          med = [med]

        #prepare rcpath
        rcpath = kwargs.get('rcpath')
        rcpath_list = []
        for med_iterator in med:
          rcpath_tmp =  rcpath+"/route-policy-entries=%s"%(util.make_interfacename(med_iterator))
          rcpath_list.append(rcpath_tmp)
        for rc_counter, route_policy_entries_object in enumerate(route_policy_entries_object_list):
          #fetch payload
          route_policy_entries_payload = route_policy_entries_object.getxml(filter=True)

          util.log_debug('update route_policy_entries_payload %s'%route_policy_entries_payload)

          rcpath = rcpath_list[rc_counter]
          #call the base abstract class for createData
          super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=route_policy_entries_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

      def delete(self, sdata, dev, route_policy_name, mapping_dict, fail_silently=False, remove_reference=False):
        dev = get_valid_devices(dev)
        if len(dev) == 0:
          return
        #Input Key Validations
        self.validate_parent_keys( route_policy_name)


        if not isinstance(route_policy_name, list):
          route_policy_name_list = [route_policy_name]
        else:
          route_policy_name_list = route_policy_name

        for route_policy_name in route_policy_name_list:
          ##prepare rcpath
          rcpath = "l3features:route-policies/route-policy=%s"%(util.make_interfacename(route_policy_name))
          self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

      def delete_(self, sdata, dev, **kwargs):
        mapping_dict = kwargs.get('mapping_dict')

        #validating inputs
        if util.isEmpty(mapping_dict.get('med')):
          raise Exception("'med' cannot be empty")

        #convert keys to list
        med = mapping_dict.get('med')
        if not isinstance(med, list):
          med = [med]

        #prepare rcpath
        rcpath = kwargs.get('rcpath')
        rcpath_list = []
        for med_iterator in med:
          rcpath_tmp =  rcpath+"/route-policy-entries=%s"%(util.make_interfacename(med_iterator))
          rcpath_list.append(rcpath_tmp)
        payload = ''

        for rcpath in rcpath_list:
          #call the base abstract class for deleteData
          super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

      def validate_parent_keys(self, route_policy_name):
        #Parent Key Validations
        if util.isEmpty(route_policy_name):
          raise Exception("'route_policy_name' cannot be empty")

      def validate_inputs_form_payload(self, mapping_dict, update=False):
        #validating inputs
        if util.isEmpty(mapping_dict.get('med')):
          raise Exception("'med' cannot be empty")

        #convert keys to list
        med = mapping_dict.get('med')
        if not isinstance(med, list):
          med = [med]

        #prepare payload
        route_policy_entries_object_list = []
        for med_iterator in med:
          from servicemodel.controller.devices.device.route_policies import route_policy
          route_policy_entries_object = route_policy.route_policy_entries.route_policy_entries()
          route_policy_entries_object.med = med_iterator
          try:
            if (update == False) or (update == True and str(mapping_dict.get('prefix_set', None)) != ''):
              route_policy_entries_object.prefix_set = mapping_dict.get('prefix_set', None)
            else:
              route_policy_entries_object.prefix_set._empty_tag = True
          except TypeError:
            pass
          route_policy_entries_object_list.append(route_policy_entries_object)

        return route_policy_entries_object_list

