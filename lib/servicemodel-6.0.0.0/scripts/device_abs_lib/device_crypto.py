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

class crypto(object):
  #XPATH devices/device/crypto/crypto-profile
  class crypto_profile(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "dmvpn:crypto"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      crypto_profile_object_list = self.validate_inputs_form_payload(mapping_dict)

      for crypto_profile_object in crypto_profile_object_list:
        #fetch payload
        crypto_profile_payload = crypto_profile_object.getxml(filter=True)
        util.log_debug('crypto_profile_payload %s'%crypto_profile_payload)
        payload_list.append(crypto_profile_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "dmvpn:crypto"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      crypto_profile_object_list = self.validate_inputs_form_payload(mapping_dict)

      for crypto_profile_object in crypto_profile_object_list:
        #fetch payload
        crypto_profile_payload = crypto_profile_object.getxml(filter=True)

        util.log_debug('crypto_profile_payload %s'%crypto_profile_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=crypto_profile_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "dmvpn:crypto"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      crypto_profile_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      ike_profile_name = mapping_dict.get('ike_profile_name')
      if not isinstance(ike_profile_name, list):
        ike_profile_name = [ike_profile_name]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for ike_profile_name_iterator in ike_profile_name:
        rcpath_tmp =  rcpath+"/crypto-profile=%s"%(util.make_interfacename(ike_profile_name_iterator))
        rcpath_list.append(rcpath_tmp)
      for rc_counter, crypto_profile_object in enumerate(crypto_profile_object_list):
        #fetch payload
        crypto_profile_payload = crypto_profile_object.getxml(filter=True)

        util.log_debug('update crypto_profile_payload %s'%crypto_profile_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=crypto_profile_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "dmvpn:crypto"
      self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

    def delete_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs
      if util.isEmpty(mapping_dict.get('ike_profile_name')):
        raise Exception("'ike_profile_name' cannot be empty")

      #convert keys to list
      ike_profile_name = mapping_dict.get('ike_profile_name')
      if not isinstance(ike_profile_name, list):
        ike_profile_name = [ike_profile_name]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for ike_profile_name_iterator in ike_profile_name:
        rcpath_tmp =  rcpath+"/crypto-profile=%s"%(util.make_interfacename(ike_profile_name_iterator))
        rcpath_list.append(rcpath_tmp)
      payload = ''

      for rcpath in rcpath_list:
        #call the base abstract class for deleteData
        super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

    def validate_inputs_form_payload(self, mapping_dict, update=False):
      #validating inputs
      if util.isEmpty(mapping_dict.get('ike_profile_name')):
        raise Exception("'ike_profile_name' cannot be empty")

      #convert keys to list
      ike_profile_name = mapping_dict.get('ike_profile_name')
      if not isinstance(ike_profile_name, list):
        ike_profile_name = [ike_profile_name]

      #prepare payload
      crypto_profile_object_list = []
      for ike_profile_name_iterator in ike_profile_name:
        from servicemodel.controller.devices.device import crypto
        crypto_profile_object = crypto.crypto_profile.crypto_profile()
        crypto_profile_object.ike_profile_name = ike_profile_name_iterator
        try:
          if (update == False) or (update == True and str(mapping_dict.get('life_time', None)) != ''):
            crypto_profile_object.life_time = mapping_dict.get('life_time', None)
          else:
            crypto_profile_object.life_time._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('ike_version', None)) != ''):
            crypto_profile_object.ike_version = mapping_dict.get('ike_version', None)
          else:
            crypto_profile_object.ike_version._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('description', None)) != ''):
            crypto_profile_object.description = mapping_dict.get('description', None)
          else:
            crypto_profile_object.description._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('key_ring_name', None)) != ''):
            crypto_profile_object.key_ring_name = mapping_dict.get('key_ring_name', None)
          else:
            crypto_profile_object.key_ring_name._empty_tag = True
        except TypeError:
          pass
        try:
          if (update == False) or (update == True and str(mapping_dict.get('auth_type', None)) != ''):
            crypto_profile_object.auth_type = mapping_dict.get('auth_type', None)
          else:
            crypto_profile_object.auth_type._empty_tag = True
        except TypeError:
          pass
        crypto_profile_object_list.append(crypto_profile_object)

      return crypto_profile_object_list

    #XPATH devices/device/crypto/crypto-profile/match
    class match(AbstractDeviceMgr):
      key_hints = [['ike_profile_name']]
      def getRcpathPayload(self, sdata, dev, crypto_profile_ike_profile_name, mapping_dict):
        dev = get_valid_devices(dev)
        if len(dev) == 0:
          return
        #Input Key Validations
        self.validate_parent_keys( crypto_profile_ike_profile_name)

        #convert parent keys to list
        rcpath_list = []
        payload_list = []
        if not isinstance(crypto_profile_ike_profile_name, list):
          crypto_profile_ike_profile_name_list = [crypto_profile_ike_profile_name]
        else:
          crypto_profile_ike_profile_name_list = crypto_profile_ike_profile_name

        for crypto_profile_ike_profile_name in crypto_profile_ike_profile_name_list:
          ##prepare rcpath
          rcpath = "dmvpn:crypto/crypto-profile=%s"%(util.make_interfacename(crypto_profile_ike_profile_name))
          rcpath_list.append(rcpath)
        mapping_dict = kwargs.get('mapping_dict')

        #validating inputs and get payload object
        match_object_list = self.validate_inputs_form_payload(mapping_dict)

        for match_object in match_object_list:
          #fetch payload
          match_payload = match_object.getxml(filter=True)
          util.log_debug('match_payload %s'%match_payload)
          payload_list.append(match_payload)

        return rcpath_list, payload_list

      def create(self, sdata, dev, crypto_profile_ike_profile_name, mapping_dict, addref=True, autocommit=True):
        dev = get_valid_devices(dev)
        if len(dev) == 0:
          return
        #Input Key Validations
        self.validate_parent_keys( crypto_profile_ike_profile_name)

        #convert parent keys to list
        if not isinstance(crypto_profile_ike_profile_name, list):
          crypto_profile_ike_profile_name_list = [crypto_profile_ike_profile_name]
        else:
          crypto_profile_ike_profile_name_list = crypto_profile_ike_profile_name

        for crypto_profile_ike_profile_name in crypto_profile_ike_profile_name_list:
          ##prepare rcpath
          rcpath = "dmvpn:crypto/crypto-profile=%s"%(util.make_interfacename(crypto_profile_ike_profile_name))
          self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

      def create_(self, sdata, dev, **kwargs):
        mapping_dict = kwargs.get('mapping_dict')

        #validating inputs and get payload object
        match_object_list = self.validate_inputs_form_payload(mapping_dict)

        for match_object in match_object_list:
          #fetch payload
          match_payload = match_object.getxml(filter=True)

          util.log_debug('match_payload %s'%match_payload)

          #call the base abstract class for createData
          super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=match_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

      def update(self, sdata, dev, crypto_profile_ike_profile_name, mapping_dict, addref=True, autocommit=True):
        dev = get_valid_devices(dev)
        if len(dev) == 0:
          return
        #Input Key Validations
        self.validate_parent_keys( crypto_profile_ike_profile_name)


        ##prepare rcpath
        rcpath = "dmvpn:crypto/crypto-profile=%s"%(util.make_interfacename(crypto_profile_ike_profile_name))
        self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

      def update_(self, sdata, dev, **kwargs):
        mapping_dict = kwargs.get('mapping_dict')

        #validating inputs and get payload object
        match_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

        #convert keys to list
        ip_address = mapping_dict.get('ip_address')
        if not isinstance(ip_address, list):
          ip_address = [ip_address]

        #prepare rcpath
        rcpath = kwargs.get('rcpath')
        rcpath_list = []
        for ip_address_iterator in ip_address:
          rcpath_tmp =  rcpath+"/match=%s"%(util.make_interfacename(ip_address_iterator))
          rcpath_list.append(rcpath_tmp)
        for rc_counter, match_object in enumerate(match_object_list):
          #fetch payload
          match_payload = match_object.getxml(filter=True)

          util.log_debug('update match_payload %s'%match_payload)

          rcpath = rcpath_list[rc_counter]
          #call the base abstract class for createData
          super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=match_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

      def delete(self, sdata, dev, crypto_profile_ike_profile_name, mapping_dict, fail_silently=False, remove_reference=False):
        dev = get_valid_devices(dev)
        if len(dev) == 0:
          return
        #Input Key Validations
        self.validate_parent_keys( crypto_profile_ike_profile_name)


        if not isinstance(crypto_profile_ike_profile_name, list):
          crypto_profile_ike_profile_name_list = [crypto_profile_ike_profile_name]
        else:
          crypto_profile_ike_profile_name_list = crypto_profile_ike_profile_name

        for crypto_profile_ike_profile_name in crypto_profile_ike_profile_name_list:
          ##prepare rcpath
          rcpath = "dmvpn:crypto/crypto-profile=%s"%(util.make_interfacename(crypto_profile_ike_profile_name))
          self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

      def delete_(self, sdata, dev, **kwargs):
        mapping_dict = kwargs.get('mapping_dict')

        #validating inputs
        if util.isEmpty(mapping_dict.get('ip_address')):
          raise Exception("'ip_address' cannot be empty")

        #convert keys to list
        ip_address = mapping_dict.get('ip_address')
        if not isinstance(ip_address, list):
          ip_address = [ip_address]

        #prepare rcpath
        rcpath = kwargs.get('rcpath')
        rcpath_list = []
        for ip_address_iterator in ip_address:
          rcpath_tmp =  rcpath+"/match=%s"%(util.make_interfacename(ip_address_iterator))
          rcpath_list.append(rcpath_tmp)
        payload = ''

        for rcpath in rcpath_list:
          #call the base abstract class for deleteData
          super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

      def validate_parent_keys(self, crypto_profile_ike_profile_name):
        #Parent Key Validations
        if util.isEmpty(crypto_profile_ike_profile_name):
          raise Exception("'crypto_profile_ike_profile_name' cannot be empty")

      def validate_inputs_form_payload(self, mapping_dict, update=False):
        #validating inputs
        if util.isEmpty(mapping_dict.get('ip_address')):
          raise Exception("'ip_address' cannot be empty")

        #convert keys to list
        ip_address = mapping_dict.get('ip_address')
        if not isinstance(ip_address, list):
          ip_address = [ip_address]

        #prepare payload
        match_object_list = []
        for ip_address_iterator in ip_address:
          from servicemodel.controller.devices.device.crypto import crypto_profile
          match_object = crypto_profile.match.match()
          try:
            if (update == False) or (update == True and str(mapping_dict.get('vrf_name', None)) != ''):
              match_object.vrf_name = mapping_dict.get('vrf_name', None)
            else:
              match_object.vrf_name._empty_tag = True
          except TypeError:
            pass
          match_object.ip_address = ip_address_iterator
          try:
            if (update == False) or (update == True and str(mapping_dict.get('netmask', None)) != ''):
              match_object.netmask = mapping_dict.get('netmask', None)
            else:
              match_object.netmask._empty_tag = True
          except TypeError:
            pass
          try:
            if (update == False) or (update == True and str(mapping_dict.get('identity_local_address', None)) != ''):
              match_object.identity_local_address = mapping_dict.get('identity_local_address', None)
            else:
              match_object.identity_local_address._empty_tag = True
          except TypeError:
            pass
          match_object_list.append(match_object)

        return match_object_list

