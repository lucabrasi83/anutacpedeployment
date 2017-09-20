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

class system_qos(object):
  #XPATH devices/device/system-qos/service-policy
  class service_policy(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "qos:system-qos"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      service_policy_object_list = self.validate_inputs_form_payload(mapping_dict)

      for service_policy_object in service_policy_object_list:
        #fetch payload
        service_policy_payload = service_policy_object.getxml(filter=True)
        util.log_debug('service_policy_payload %s'%service_policy_payload)
        payload_list.append(service_policy_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "qos:system-qos"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      service_policy_object_list = self.validate_inputs_form_payload(mapping_dict)

      for service_policy_object in service_policy_object_list:
        #fetch payload
        service_policy_payload = service_policy_object.getxml(filter=True)

        util.log_debug('service_policy_payload %s'%service_policy_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=service_policy_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "qos:system-qos"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      service_policy_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      policy_map = mapping_dict.get('policy_map')
      if not isinstance(policy_map, list):
        policy_map = [policy_map]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for policy_map_iterator in policy_map:
        rcpath_tmp =  rcpath+"/service-policy=%s"%(util.make_interfacename(policy_map_iterator))
        rcpath_list.append(rcpath_tmp)
      for rc_counter, service_policy_object in enumerate(service_policy_object_list):
        #fetch payload
        service_policy_payload = service_policy_object.getxml(filter=True)

        util.log_debug('update service_policy_payload %s'%service_policy_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=service_policy_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "qos:system-qos"
      self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

    def delete_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs
      if util.isEmpty(mapping_dict.get('policy_map')):
        raise Exception("'policy_map' cannot be empty")

      #convert keys to list
      policy_map = mapping_dict.get('policy_map')
      if not isinstance(policy_map, list):
        policy_map = [policy_map]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for policy_map_iterator in policy_map:
        rcpath_tmp =  rcpath+"/service-policy=%s"%(util.make_interfacename(policy_map_iterator))
        rcpath_list.append(rcpath_tmp)
      payload = ''

      for rcpath in rcpath_list:
        #call the base abstract class for deleteData
        super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

    def validate_inputs_form_payload(self, mapping_dict, update=False):
      #validating inputs
      if util.isEmpty(mapping_dict.get('policy_map')):
        raise Exception("'policy_map' cannot be empty")

      #convert keys to list
      policy_map = mapping_dict.get('policy_map')
      if not isinstance(policy_map, list):
        policy_map = [policy_map]

      #prepare payload
      service_policy_object_list = []
      for policy_map_iterator in policy_map:
        from servicemodel.controller.devices.device import system_qos
        service_policy_object = system_qos.service_policy.service_policy()
        try:
          if (update == False) or (update == True and str(mapping_dict.get('type', None)) != ''):
            service_policy_object.type = mapping_dict.get('type', None)
          else:
            service_policy_object.type._empty_tag = True
        except TypeError:
          pass
        service_policy_object.policy_map = policy_map_iterator
        service_policy_object_list.append(service_policy_object)

      return service_policy_object_list

