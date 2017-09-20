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

class static_routes(object):
  #XPATH devices/device/static-routes/static-route
  class static_route(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "l3features:static-routes"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      static_route_object_list = self.validate_inputs_form_payload(mapping_dict)

      for static_route_object in static_route_object_list:
        #fetch payload
        static_route_payload = static_route_object.getxml(filter=True)
        util.log_debug('static_route_payload %s'%static_route_payload)
        payload_list.append(static_route_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "l3features:static-routes"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      static_route_object_list = self.validate_inputs_form_payload(mapping_dict)

      for static_route_object in static_route_object_list:
        #fetch payload
        static_route_payload = static_route_object.getxml(filter=True)

        util.log_debug('static_route_payload %s'%static_route_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=static_route_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "l3features:static-routes"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      static_route_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      dest_ip_address = mapping_dict.get('dest_ip_address')
      if not isinstance(dest_ip_address, list):
        dest_ip_address = [dest_ip_address]
      dest_mask = mapping_dict.get('dest_mask')
      if not isinstance(dest_mask, list):
        dest_mask = [dest_mask]
      next_hop_ip = mapping_dict.get('next_hop_ip')
      if not isinstance(next_hop_ip, list):
        next_hop_ip = [next_hop_ip]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for dest_ip_address_iterator in dest_ip_address:
        for dest_mask_iterator in dest_mask:
          for next_hop_ip_iterator in next_hop_ip:
            rcpath_tmp =  rcpath+"/static-route=%s,%s,%s"%(util.make_interfacename(dest_ip_address_iterator),util.make_interfacename(dest_mask_iterator),util.make_interfacename(next_hop_ip_iterator))
            rcpath_list.append(rcpath_tmp)
      for rc_counter, static_route_object in enumerate(static_route_object_list):
        #fetch payload
        static_route_payload = static_route_object.getxml(filter=True)

        util.log_debug('update static_route_payload %s'%static_route_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=static_route_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "l3features:static-routes"
      self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

    def delete_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs
      if util.isEmpty(mapping_dict.get('dest_ip_address')):
        raise Exception("'dest_ip_address' cannot be empty")
      if util.isEmpty(mapping_dict.get('dest_mask')):
        raise Exception("'dest_mask' cannot be empty")
      if util.isEmpty(mapping_dict.get('next_hop_ip')):
        raise Exception("'next_hop_ip' cannot be empty")

      #convert keys to list
      dest_ip_address = mapping_dict.get('dest_ip_address')
      if not isinstance(dest_ip_address, list):
        dest_ip_address = [dest_ip_address]
      dest_mask = mapping_dict.get('dest_mask')
      if not isinstance(dest_mask, list):
        dest_mask = [dest_mask]
      next_hop_ip = mapping_dict.get('next_hop_ip')
      if not isinstance(next_hop_ip, list):
        next_hop_ip = [next_hop_ip]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for dest_ip_address_iterator in dest_ip_address:
        for dest_mask_iterator in dest_mask:
          for next_hop_ip_iterator in next_hop_ip:
            rcpath_tmp =  rcpath+"/static-route=%s,%s,%s"%(util.make_interfacename(dest_ip_address_iterator),util.make_interfacename(dest_mask_iterator),util.make_interfacename(next_hop_ip_iterator))
            rcpath_list.append(rcpath_tmp)
      payload = ''

      for rcpath in rcpath_list:
        #call the base abstract class for deleteData
        super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

    def validate_inputs_form_payload(self, mapping_dict, update=False):
      #validating inputs
      if util.isEmpty(mapping_dict.get('dest_ip_address')):
        raise Exception("'dest_ip_address' cannot be empty")
      if util.isEmpty(mapping_dict.get('dest_mask')):
        raise Exception("'dest_mask' cannot be empty")
      if util.isEmpty(mapping_dict.get('next_hop_ip')):
        raise Exception("'next_hop_ip' cannot be empty")

      #convert keys to list
      dest_ip_address = mapping_dict.get('dest_ip_address')
      if not isinstance(dest_ip_address, list):
        dest_ip_address = [dest_ip_address]
      dest_mask = mapping_dict.get('dest_mask')
      if not isinstance(dest_mask, list):
        dest_mask = [dest_mask]
      next_hop_ip = mapping_dict.get('next_hop_ip')
      if not isinstance(next_hop_ip, list):
        next_hop_ip = [next_hop_ip]

      #prepare payload
      static_route_object_list = []
      for dest_ip_address_iterator in dest_ip_address:
        for dest_mask_iterator in dest_mask:
          for next_hop_ip_iterator in next_hop_ip:
            from servicemodel.controller.devices.device import static_routes
            static_route_object = static_routes.static_route.static_route()
            static_route_object.dest_ip_address = dest_ip_address_iterator
            static_route_object.dest_mask = dest_mask_iterator
            try:
              if (update == False) or (update == True and str(mapping_dict.get('description', None)) != ''):
                static_route_object._set_description(mapping_dict.get('description', None))
              else:
                static_route_object._unset_description()
            except TypeError:
              pass
            try:
              if (update == False) or (update == True and str(mapping_dict.get('metric', None)) != ''):
                static_route_object._set_metric(mapping_dict.get('metric', None))
              else:
                static_route_object._unset_metric()
            except TypeError:
              pass
            static_route_object.next_hop_ip = next_hop_ip_iterator
            try:
              if (update == False) or (update == True and str(mapping_dict.get('name', None)) != ''):
                static_route_object._set_name(mapping_dict.get('name', None))
              else:
                static_route_object._unset_name()
            except TypeError:
              pass
            try:
              if (update == False) or (update == True and str(mapping_dict.get('user_id_grp_name', None)) != ''):
                static_route_object._set_user_id_grp_name(mapping_dict.get('user_id_grp_name', None))
              else:
                static_route_object._unset_user_id_grp_name()
            except TypeError:
              pass
            try:
              if (update == False) or (update == True and str(mapping_dict.get('interface_name', None)) != ''):
                static_route_object._set_interface_name(mapping_dict.get('interface_name', None))
              else:
                static_route_object._unset_interface_name()
            except TypeError:
              pass
            try:
              if (update == False) or (update == True and str(mapping_dict.get('next_routing_table', None)) != ''):
                static_route_object._set_next_routing_table(mapping_dict.get('next_routing_table', None))
              else:
                static_route_object._unset_next_routing_table()
            except TypeError:
              pass
            try:
              if (update == False) or (update == True and str(mapping_dict.get('vlan_number', None)) != ''):
                static_route_object._set_vlan_number(mapping_dict.get('vlan_number', None))
              else:
                static_route_object._unset_vlan_number()
            except TypeError:
              pass
            try:
              if (update == False) or (update == True and str(mapping_dict.get('tag', None)) != ''):
                static_route_object._set_tag(mapping_dict.get('tag', None))
              else:
                static_route_object._unset_tag()
            except TypeError:
              pass
            static_route_object_list.append(static_route_object)

      return static_route_object_list

