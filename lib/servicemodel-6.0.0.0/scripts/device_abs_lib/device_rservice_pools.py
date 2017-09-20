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

class rservice_pools(object):
  #XPATH devices/device/rservice-pools/rservice-pool
  class rservice_pool(AbstractDeviceMgr):
    key_hints = [[]]
    def getRcpathPayload(self, sdata, dev, mapping_dict):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      rcpath_list = []
      payload_list = []
      ##prepare rcpath
      rcpath = "loadbalancer:rservice-pools"
      rcpath_list.append(rcpath)
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      rservice_pool_object_list = self.validate_inputs_form_payload(mapping_dict)

      for rservice_pool_object in rservice_pool_object_list:
        #fetch payload
        rservice_pool_payload = rservice_pool_object.getxml(filter=True)
        util.log_debug('rservice_pool_payload %s'%rservice_pool_payload)
        payload_list.append(rservice_pool_payload)

      return rcpath_list, payload_list

    def create(self, sdata, dev, mapping_dict, addref=True, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return
      #convert parent keys to list
      ##prepare rcpath
      rcpath = "loadbalancer:rservice-pools"
      self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def create_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      rservice_pool_object_list = self.validate_inputs_form_payload(mapping_dict)

      for rservice_pool_object in rservice_pool_object_list:
        #fetch payload
        rservice_pool_payload = rservice_pool_object.getxml(filter=True)

        util.log_debug('rservice_pool_payload %s'%rservice_pool_payload)

        #call the base abstract class for createData
        super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=rservice_pool_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def update(self, sdata, dev, mapping_dict, addref=False, autocommit=True):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "loadbalancer:rservice-pools"
      self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

    def update_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs and get payload object
      rservice_pool_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

      #convert keys to list
      name = mapping_dict.get('name')
      if not isinstance(name, list):
        name = [name]
      domain_number = mapping_dict.get('domain_number')
      if not isinstance(domain_number, list):
        domain_number = [domain_number]
      partition = mapping_dict.get('partition')
      if not isinstance(partition, list):
        partition = [partition]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for name_iterator in name:
        for domain_number_iterator in domain_number:
          for partition_iterator in partition:
            rcpath_tmp =  rcpath+"/rservice-pool=%s,%s,%s"%(util.make_interfacename(name_iterator),util.make_interfacename(domain_number_iterator),util.make_interfacename(partition_iterator))
            rcpath_list.append(rcpath_tmp)
      for rc_counter, rservice_pool_object in enumerate(rservice_pool_object_list):
        #fetch payload
        rservice_pool_payload = rservice_pool_object.getxml(filter=True)

        util.log_debug('update rservice_pool_payload %s'%rservice_pool_payload)

        rcpath = rcpath_list[rc_counter]
        #call the base abstract class for createData
        super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=rservice_pool_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

    def delete(self, sdata, dev, mapping_dict, fail_silently=False, remove_reference=False):
      dev = get_valid_devices(dev)
      if len(dev) == 0:
        return

      ##prepare rcpath
      rcpath = "loadbalancer:rservice-pools"
      self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

    def delete_(self, sdata, dev, **kwargs):
      mapping_dict = kwargs.get('mapping_dict')

      #validating inputs
      if util.isEmpty(mapping_dict.get('name')):
        raise Exception("'name' cannot be empty")
      if util.isEmpty(mapping_dict.get('domain_number')):
        raise Exception("'domain_number' cannot be empty")
      if util.isEmpty(mapping_dict.get('partition')):
        raise Exception("'partition' cannot be empty")

      #convert keys to list
      name = mapping_dict.get('name')
      if not isinstance(name, list):
        name = [name]
      domain_number = mapping_dict.get('domain_number')
      if not isinstance(domain_number, list):
        domain_number = [domain_number]
      partition = mapping_dict.get('partition')
      if not isinstance(partition, list):
        partition = [partition]

      #prepare rcpath
      rcpath = kwargs.get('rcpath')
      rcpath_list = []
      for name_iterator in name:
        for domain_number_iterator in domain_number:
          for partition_iterator in partition:
            rcpath_tmp =  rcpath+"/rservice-pool=%s,%s,%s"%(util.make_interfacename(name_iterator),util.make_interfacename(domain_number_iterator),util.make_interfacename(partition_iterator))
            rcpath_list.append(rcpath_tmp)
      payload = ''

      for rcpath in rcpath_list:
        #call the base abstract class for deleteData
        super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

    def validate_inputs_form_payload(self, mapping_dict, update=False):
      #validating inputs
      if util.isEmpty(mapping_dict.get('name')):
        raise Exception("'name' cannot be empty")
      if util.isEmpty(mapping_dict.get('domain_number')):
        raise Exception("'domain_number' cannot be empty")
      if util.isEmpty(mapping_dict.get('partition')):
        raise Exception("'partition' cannot be empty")

      #convert keys to list
      name = mapping_dict.get('name')
      if not isinstance(name, list):
        name = [name]
      domain_number = mapping_dict.get('domain_number')
      if not isinstance(domain_number, list):
        domain_number = [domain_number]
      partition = mapping_dict.get('partition')
      if not isinstance(partition, list):
        partition = [partition]

      #prepare payload
      rservice_pool_object_list = []
      for name_iterator in name:
        for domain_number_iterator in domain_number:
          for partition_iterator in partition:
            from servicemodel.controller.devices.device import rservice_pools
            rservice_pool_object = rservice_pools.rservice_pool.rservice_pool()
            rservice_pool_object.name = name_iterator
            try:
              if (update == False) or (update == True and str(mapping_dict.get('priority_group_activation', None)) != ''):
                rservice_pool_object.priority_group_activation = mapping_dict.get('priority_group_activation', None)
              else:
                rservice_pool_object.priority_group_activation._empty_tag = True
            except TypeError:
              pass
            try:
              if (update == False) or (update == True and str(mapping_dict.get('load_balancing_method', None)) != ''):
                rservice_pool_object.load_balancing_method = mapping_dict.get('load_balancing_method', None)
              else:
                rservice_pool_object.load_balancing_method._empty_tag = True
            except TypeError:
              pass
            rservice_pool_object.domain_number = domain_number_iterator
            try:
              if (update == False) or (update == True and str(mapping_dict.get('protocol', None)) != ''):
                rservice_pool_object.protocol = mapping_dict.get('protocol', None)
              else:
                rservice_pool_object.protocol._empty_tag = True
            except TypeError:
              pass
            rservice_pool_object.partition = partition_iterator
            rservice_pool_object_list.append(rservice_pool_object)

      return rservice_pool_object_list

    class pool_members(object):
      #XPATH devices/device/rservice-pools/rservice-pool/pool-members/pool-member
      class pool_member(AbstractDeviceMgr):
        key_hints = [['name','domain_number','partition']]
        def getRcpathPayload(self, sdata, dev, rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition, mapping_dict):
          dev = get_valid_devices(dev)
          if len(dev) == 0:
            return
          #Input Key Validations
          self.validate_parent_keys( rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition)

          #convert parent keys to list
          rcpath_list = []
          payload_list = []
          if not isinstance(rservice_pool_name, list):
            rservice_pool_name_list = [rservice_pool_name]
          else:
            rservice_pool_name_list = rservice_pool_name
          if not isinstance(rservice_pool_domain_number, list):
            rservice_pool_domain_number_list = [rservice_pool_domain_number]
          else:
            rservice_pool_domain_number_list = rservice_pool_domain_number
          if not isinstance(rservice_pool_partition, list):
            rservice_pool_partition_list = [rservice_pool_partition]
          else:
            rservice_pool_partition_list = rservice_pool_partition

          for rservice_pool_name in rservice_pool_name_list:
            for rservice_pool_domain_number in rservice_pool_domain_number_list:
              for rservice_pool_partition in rservice_pool_partition_list:
                ##prepare rcpath
                rcpath = "loadbalancer:rservice-pools/rservice-pool=%s,%s,%s/pool-members"%(util.make_interfacename(rservice_pool_name),util.make_interfacename(rservice_pool_domain_number),util.make_interfacename(rservice_pool_partition))
                rcpath_list.append(rcpath)
          mapping_dict = kwargs.get('mapping_dict')

          #validating inputs and get payload object
          pool_member_object_list = self.validate_inputs_form_payload(mapping_dict)

          for pool_member_object in pool_member_object_list:
            #fetch payload
            pool_member_payload = pool_member_object.getxml(filter=True)
            util.log_debug('pool_member_payload %s'%pool_member_payload)
            payload_list.append(pool_member_payload)

          return rcpath_list, payload_list

        def create(self, sdata, dev, rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition, mapping_dict, addref=True, autocommit=True):
          dev = get_valid_devices(dev)
          if len(dev) == 0:
            return
          #Input Key Validations
          self.validate_parent_keys( rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition)

          #convert parent keys to list
          if not isinstance(rservice_pool_name, list):
            rservice_pool_name_list = [rservice_pool_name]
          else:
            rservice_pool_name_list = rservice_pool_name
          if not isinstance(rservice_pool_domain_number, list):
            rservice_pool_domain_number_list = [rservice_pool_domain_number]
          else:
            rservice_pool_domain_number_list = rservice_pool_domain_number
          if not isinstance(rservice_pool_partition, list):
            rservice_pool_partition_list = [rservice_pool_partition]
          else:
            rservice_pool_partition_list = rservice_pool_partition

          for rservice_pool_name in rservice_pool_name_list:
            for rservice_pool_domain_number in rservice_pool_domain_number_list:
              for rservice_pool_partition in rservice_pool_partition_list:
                ##prepare rcpath
                rcpath = "loadbalancer:rservice-pools/rservice-pool=%s,%s,%s/pool-members"%(util.make_interfacename(rservice_pool_name),util.make_interfacename(rservice_pool_domain_number),util.make_interfacename(rservice_pool_partition))
                self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

        def create_(self, sdata, dev, **kwargs):
          mapping_dict = kwargs.get('mapping_dict')

          #validating inputs and get payload object
          pool_member_object_list = self.validate_inputs_form_payload(mapping_dict)

          for pool_member_object in pool_member_object_list:
            #fetch payload
            pool_member_payload = pool_member_object.getxml(filter=True)

            util.log_debug('pool_member_payload %s'%pool_member_payload)

            #call the base abstract class for createData
            super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=pool_member_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

        def update(self, sdata, dev, rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition, mapping_dict, addref=True, autocommit=True):
          dev = get_valid_devices(dev)
          if len(dev) == 0:
            return
          #Input Key Validations
          self.validate_parent_keys( rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition)


          ##prepare rcpath
          rcpath = "loadbalancer:rservice-pools/rservice-pool=%s,%s,%s/pool-members"%(util.make_interfacename(rservice_pool_name),util.make_interfacename(rservice_pool_domain_number),util.make_interfacename(rservice_pool_partition))
          self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

        def update_(self, sdata, dev, **kwargs):
          mapping_dict = kwargs.get('mapping_dict')

          #validating inputs and get payload object
          pool_member_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

          #convert keys to list
          real_server_ip = mapping_dict.get('real_server_ip')
          if not isinstance(real_server_ip, list):
            real_server_ip = [real_server_ip]
          service_port = mapping_dict.get('service_port')
          if not isinstance(service_port, list):
            service_port = [service_port]

          #prepare rcpath
          rcpath = kwargs.get('rcpath')
          rcpath_list = []
          for real_server_ip_iterator in real_server_ip:
            for service_port_iterator in service_port:
              rcpath_tmp =  rcpath+"/pool-member=%s,%s"%(util.make_interfacename(real_server_ip_iterator),util.make_interfacename(service_port_iterator))
              rcpath_list.append(rcpath_tmp)
          for rc_counter, pool_member_object in enumerate(pool_member_object_list):
            #fetch payload
            pool_member_payload = pool_member_object.getxml(filter=True)

            util.log_debug('update pool_member_payload %s'%pool_member_payload)

            rcpath = rcpath_list[rc_counter]
            #call the base abstract class for createData
            super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=pool_member_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

        def delete(self, sdata, dev, rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition, mapping_dict, fail_silently=False, remove_reference=False):
          dev = get_valid_devices(dev)
          if len(dev) == 0:
            return
          #Input Key Validations
          self.validate_parent_keys( rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition)


          if not isinstance(rservice_pool_name, list):
            rservice_pool_name_list = [rservice_pool_name]
          else:
            rservice_pool_name_list = rservice_pool_name
          if not isinstance(rservice_pool_domain_number, list):
            rservice_pool_domain_number_list = [rservice_pool_domain_number]
          else:
            rservice_pool_domain_number_list = rservice_pool_domain_number
          if not isinstance(rservice_pool_partition, list):
            rservice_pool_partition_list = [rservice_pool_partition]
          else:
            rservice_pool_partition_list = rservice_pool_partition

          for rservice_pool_name in rservice_pool_name_list:
            for rservice_pool_domain_number in rservice_pool_domain_number_list:
              for rservice_pool_partition in rservice_pool_partition_list:
                ##prepare rcpath
                rcpath = "loadbalancer:rservice-pools/rservice-pool=%s,%s,%s/pool-members"%(util.make_interfacename(rservice_pool_name),util.make_interfacename(rservice_pool_domain_number),util.make_interfacename(rservice_pool_partition))
                self.delete_(sdata, dev, mapping_dict=mapping_dict, fail_silently=fail_silently, remove_reference=remove_reference, rcpath=rcpath)

        def delete_(self, sdata, dev, **kwargs):
          mapping_dict = kwargs.get('mapping_dict')

          #validating inputs
          if util.isEmpty(mapping_dict.get('real_server_ip')):
            raise Exception("'real_server_ip' cannot be empty")
          if util.isEmpty(mapping_dict.get('service_port')):
            raise Exception("'service_port' cannot be empty")

          #convert keys to list
          real_server_ip = mapping_dict.get('real_server_ip')
          if not isinstance(real_server_ip, list):
            real_server_ip = [real_server_ip]
          service_port = mapping_dict.get('service_port')
          if not isinstance(service_port, list):
            service_port = [service_port]

          #prepare rcpath
          rcpath = kwargs.get('rcpath')
          rcpath_list = []
          for real_server_ip_iterator in real_server_ip:
            for service_port_iterator in service_port:
              rcpath_tmp =  rcpath+"/pool-member=%s,%s"%(util.make_interfacename(real_server_ip_iterator),util.make_interfacename(service_port_iterator))
              rcpath_list.append(rcpath_tmp)
          payload = ''

          for rcpath in rcpath_list:
            #call the base abstract class for deleteData
            super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

        def validate_parent_keys(self, rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition):
          #Parent Key Validations
          if util.isEmpty(rservice_pool_name):
            raise Exception("'rservice_pool_name' cannot be empty")
          if util.isEmpty(rservice_pool_domain_number):
            raise Exception("'rservice_pool_domain_number' cannot be empty")
          if util.isEmpty(rservice_pool_partition):
            raise Exception("'rservice_pool_partition' cannot be empty")

        def validate_inputs_form_payload(self, mapping_dict, update=False):
          #validating inputs
          if util.isEmpty(mapping_dict.get('real_server_ip')):
            raise Exception("'real_server_ip' cannot be empty")
          if util.isEmpty(mapping_dict.get('service_port')):
            raise Exception("'service_port' cannot be empty")

          #convert keys to list
          real_server_ip = mapping_dict.get('real_server_ip')
          if not isinstance(real_server_ip, list):
            real_server_ip = [real_server_ip]
          service_port = mapping_dict.get('service_port')
          if not isinstance(service_port, list):
            service_port = [service_port]

          #prepare payload
          pool_member_object_list = []
          for real_server_ip_iterator in real_server_ip:
            for service_port_iterator in service_port:
              from servicemodel.controller.devices.device.rservice_pools.rservice_pool import pool_members
              pool_member_object = pool_members.pool_member.pool_member()
              pool_member_object.real_server_ip = real_server_ip_iterator
              pool_member_object.service_port = service_port_iterator
              pool_member_object_list.append(pool_member_object)

          return pool_member_object_list

    class health_monitors(object):
      #XPATH devices/device/rservice-pools/rservice-pool/health-monitors/health-monitor
      class health_monitor(AbstractDeviceMgr):
        key_hints = [['name','domain_number','partition']]
        def getRcpathPayload(self, sdata, dev, rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition, mapping_dict):
          dev = get_valid_devices(dev)
          if len(dev) == 0:
            return
          #Input Key Validations
          self.validate_parent_keys( rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition)

          #convert parent keys to list
          rcpath_list = []
          payload_list = []
          if not isinstance(rservice_pool_name, list):
            rservice_pool_name_list = [rservice_pool_name]
          else:
            rservice_pool_name_list = rservice_pool_name
          if not isinstance(rservice_pool_domain_number, list):
            rservice_pool_domain_number_list = [rservice_pool_domain_number]
          else:
            rservice_pool_domain_number_list = rservice_pool_domain_number
          if not isinstance(rservice_pool_partition, list):
            rservice_pool_partition_list = [rservice_pool_partition]
          else:
            rservice_pool_partition_list = rservice_pool_partition

          for rservice_pool_name in rservice_pool_name_list:
            for rservice_pool_domain_number in rservice_pool_domain_number_list:
              for rservice_pool_partition in rservice_pool_partition_list:
                ##prepare rcpath
                rcpath = "loadbalancer:rservice-pools/rservice-pool=%s,%s,%s/health-monitors"%(util.make_interfacename(rservice_pool_name),util.make_interfacename(rservice_pool_domain_number),util.make_interfacename(rservice_pool_partition))
                rcpath_list.append(rcpath)
          mapping_dict = kwargs.get('mapping_dict')

          #validating inputs and get payload object
          health_monitor_object_list = self.validate_inputs_form_payload(mapping_dict)

          for health_monitor_object in health_monitor_object_list:
            #fetch payload
            health_monitor_payload = health_monitor_object.getxml(filter=True)
            util.log_debug('health_monitor_payload %s'%health_monitor_payload)
            payload_list.append(health_monitor_payload)

          return rcpath_list, payload_list

        def create(self, sdata, dev, rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition, mapping_dict, addref=True, autocommit=True):
          dev = get_valid_devices(dev)
          if len(dev) == 0:
            return
          #Input Key Validations
          self.validate_parent_keys( rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition)

          #convert parent keys to list
          if not isinstance(rservice_pool_name, list):
            rservice_pool_name_list = [rservice_pool_name]
          else:
            rservice_pool_name_list = rservice_pool_name
          if not isinstance(rservice_pool_domain_number, list):
            rservice_pool_domain_number_list = [rservice_pool_domain_number]
          else:
            rservice_pool_domain_number_list = rservice_pool_domain_number
          if not isinstance(rservice_pool_partition, list):
            rservice_pool_partition_list = [rservice_pool_partition]
          else:
            rservice_pool_partition_list = rservice_pool_partition

          for rservice_pool_name in rservice_pool_name_list:
            for rservice_pool_domain_number in rservice_pool_domain_number_list:
              for rservice_pool_partition in rservice_pool_partition_list:
                ##prepare rcpath
                rcpath = "loadbalancer:rservice-pools/rservice-pool=%s,%s,%s/health-monitors"%(util.make_interfacename(rservice_pool_name),util.make_interfacename(rservice_pool_domain_number),util.make_interfacename(rservice_pool_partition))
                self.create_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

        def create_(self, sdata, dev, **kwargs):
          mapping_dict = kwargs.get('mapping_dict')

          #validating inputs and get payload object
          health_monitor_object_list = self.validate_inputs_form_payload(mapping_dict)

          for health_monitor_object in health_monitor_object_list:
            #fetch payload
            health_monitor_payload = health_monitor_object.getxml(filter=True)

            util.log_debug('health_monitor_payload %s'%health_monitor_payload)

            #call the base abstract class for createData
            super(self.__class__, self).create_(sdata, dev, rcpath=kwargs.get('rcpath'), payload=health_monitor_payload, key_hints=self.key_hints, addref=kwargs.get('addref', True), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

        def update(self, sdata, dev, rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition, mapping_dict, addref=True, autocommit=True):
          dev = get_valid_devices(dev)
          if len(dev) == 0:
            return
          #Input Key Validations
          self.validate_parent_keys( rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition)


          ##prepare rcpath
          rcpath = "loadbalancer:rservice-pools/rservice-pool=%s,%s,%s/health-monitors"%(util.make_interfacename(rservice_pool_name),util.make_interfacename(rservice_pool_domain_number),util.make_interfacename(rservice_pool_partition))
          self.update_(sdata, dev, mapping_dict=mapping_dict, addref=addref, autocommit=autocommit, rcpath=rcpath)

        def update_(self, sdata, dev, **kwargs):
          mapping_dict = kwargs.get('mapping_dict')

          #validating inputs and get payload object
          health_monitor_object_list = self.validate_inputs_form_payload(mapping_dict, update=True)

          #convert keys to list
          name = mapping_dict.get('name')
          if not isinstance(name, list):
            name = [name]

          #prepare rcpath
          rcpath = kwargs.get('rcpath')
          rcpath_list = []
          for name_iterator in name:
            rcpath_tmp =  rcpath+"/health-monitor=%s"%(util.make_interfacename(name_iterator))
            rcpath_list.append(rcpath_tmp)
          for rc_counter, health_monitor_object in enumerate(health_monitor_object_list):
            #fetch payload
            health_monitor_payload = health_monitor_object.getxml(filter=True)

            util.log_debug('update health_monitor_payload %s'%health_monitor_payload)

            rcpath = rcpath_list[rc_counter]
            #call the base abstract class for createData
            super(self.__class__, self).update_(sdata, dev, rcpath=rcpath, payload=health_monitor_payload, key_hints=self.key_hints, addref=kwargs.get('addref', False), autocommit=kwargs.get('autocommit', True), mapping_dict=mapping_dict)

        def delete(self, sdata, dev, rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition, mapping_dict, fail_silently=False, remove_reference=False):
          dev = get_valid_devices(dev)
          if len(dev) == 0:
            return
          #Input Key Validations
          self.validate_parent_keys( rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition)


          if not isinstance(rservice_pool_name, list):
            rservice_pool_name_list = [rservice_pool_name]
          else:
            rservice_pool_name_list = rservice_pool_name
          if not isinstance(rservice_pool_domain_number, list):
            rservice_pool_domain_number_list = [rservice_pool_domain_number]
          else:
            rservice_pool_domain_number_list = rservice_pool_domain_number
          if not isinstance(rservice_pool_partition, list):
            rservice_pool_partition_list = [rservice_pool_partition]
          else:
            rservice_pool_partition_list = rservice_pool_partition

          for rservice_pool_name in rservice_pool_name_list:
            for rservice_pool_domain_number in rservice_pool_domain_number_list:
              for rservice_pool_partition in rservice_pool_partition_list:
                ##prepare rcpath
                rcpath = "loadbalancer:rservice-pools/rservice-pool=%s,%s,%s/health-monitors"%(util.make_interfacename(rservice_pool_name),util.make_interfacename(rservice_pool_domain_number),util.make_interfacename(rservice_pool_partition))
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
            rcpath_tmp =  rcpath+"/health-monitor=%s"%(util.make_interfacename(name_iterator))
            rcpath_list.append(rcpath_tmp)
          payload = ''

          for rcpath in rcpath_list:
            #call the base abstract class for deleteData
            super(self.__class__, self).delete_(sdata, dev, rcpath=rcpath, payload=payload, fail_silently=kwargs.get('fail_silently', False), remove_reference=kwargs.get('remove_reference', False))

        def validate_parent_keys(self, rservice_pool_name, rservice_pool_domain_number, rservice_pool_partition):
          #Parent Key Validations
          if util.isEmpty(rservice_pool_name):
            raise Exception("'rservice_pool_name' cannot be empty")
          if util.isEmpty(rservice_pool_domain_number):
            raise Exception("'rservice_pool_domain_number' cannot be empty")
          if util.isEmpty(rservice_pool_partition):
            raise Exception("'rservice_pool_partition' cannot be empty")

        def validate_inputs_form_payload(self, mapping_dict, update=False):
          #validating inputs
          if util.isEmpty(mapping_dict.get('name')):
            raise Exception("'name' cannot be empty")

          #convert keys to list
          name = mapping_dict.get('name')
          if not isinstance(name, list):
            name = [name]

          #prepare payload
          health_monitor_object_list = []
          for name_iterator in name:
            from servicemodel.controller.devices.device.rservice_pools.rservice_pool import health_monitors
            health_monitor_object = health_monitors.health_monitor.health_monitor()
            health_monitor_object.name = name_iterator
            try:
              if (update == False) or (update == True and str(mapping_dict.get('weight', None)) != ''):
                health_monitor_object.weight = mapping_dict.get('weight', None)
              else:
                health_monitor_object.weight._empty_tag = True
            except TypeError:
              pass
            try:
              if (update == False) or (update == True and str(mapping_dict.get('state', None)) != ''):
                health_monitor_object.state = mapping_dict.get('state', None)
              else:
                health_monitor_object.state._empty_tag = True
            except TypeError:
              pass
            health_monitor_object_list.append(health_monitor_object)

          return health_monitor_object_list

