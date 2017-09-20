#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2014-2015 Anuta Networks, Inc. All Rights Reserved.

from servicemodel import devicemgr
from servicemodel import util

class VirtualDevice(util.BaseObject):

  def __init__(self):
      util.BaseObject.__init__(self, 'virtual-device')

  def setName(self, name):
      self.root.set_field_value('name', name)        

  def setFileStore(self, value):
      self.root.set_field_value('file-store', value)

  def setFailovergroup(self, value):
      self.root.set_field_value('failovergroup', value)

  def setHostname(self, value):
      self.root.set_field_value('hostname', value)

  def setIsCommit(self, value):
      self.root.set_field_value('is-commit', value)        

  def setInterface(self, value):
      self.root.set_field_value('interface', value) 

  def setUser(self, value):
      self.root.set_field_value('user', value)        

  class Interface(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'interface')

    def setInterfaceName(self, name):
        self.root.set_field_value('interface-name', name)        

    def setInsideName(self, name):
        self.root.set_field_value('inside-name', name)   

    def setTransitVlanId(self, name):
        self.root.set_field_value('transit-vlanId', name)

    def setDescription(self, value):
        self.root.set_field_value('description', value)

    def setShutdown(self, value):
        self.root.set_field_value('shutdown', value)

  class User(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'user')

    def setUsername(self, name):
        self.root.set_field_value('username', name)        

    def setPassword(self, name):
        self.root.set_field_value('password', name)   

    def setPrivilege(self, name):
        self.root.set_field_value('privilege', name)


class NatObjectGroup(util.BaseObject):

  def __init__(self):
      util.BaseObject.__init__(self, 'nat-object-group')

  def setName(self, name):
      self.root.set_field_value('name', name)

  def setNatOutsideIp(self, value):
      self.root.set_field_value('nat-outside-ip', value)

  def setHostIp(self, value):
      self.root.set_field_value('host-ip', value)

  def setNatOutsideInterface(self, value):
      self.root.set_field_value('nat-outside-interface', value)

  def setNatInsideInterface(self, value):
      self.root.set_field_value('nat-inside-interface', value)
                  
  def setContextName(self, value):
      self.root.set_field_value('context-name', value)

class ObjectGroup(util.BaseObject):

  def __init__(self):
      util.BaseObject.__init__(self, 'object-group')

  def setName(self, name):
      self.root.set_field_value('name', name)

  def setDescription(self, value):
      self.root.set_field_value('description', value)

  def setType(self, value):
      self.root.set_field_value('type', value)

  def setServiceType(self, value):
      self.root.set_field_value('service-type', value)

  def setContextName(self, value):
      self.root.set_field_value('context-name', value)      
  
  def setNetworkObject(self, value):
      self.root.set_field_value('network-object', value)

  def setSubObjectGroup(self, value):
      self.root.set_field_value('sub-object-group', value)

  def setServiceObject(self, value):
      self.root.set_field_value('service-object', value)            

  class NetworkObject(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'network-object')

    def setNetworkObjectName(self, value):
        self.root.set_field_value('network-object-name', value)

  class SubObjectGroup(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'sub-object-group')

    def setObjectGroupName(self, value):
        self.root.set_field_value('object-group-name', value)

  class ServiceObject(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'service-object')

    def setServiceObjectValue(self, value):
        self.root.set_field_value('service-object-value', value)            
     
    def setServiceObjectType(self, value):
        self.root.set_field_value('service-object-type', value)   


class NetworkObject(util.BaseObject):

  def __init__(self):
      util.BaseObject.__init__(self, 'network-object')

  def setName(self, name):
      self.root.set_field_value('name', name)

  def setDescription(self, value):
      self.root.set_field_value('description', value)

  def setVrfName(self, value):
      self.root.set_field_value('vrf-name', value)

  def setObjectGroupName(self, value):
      self.root.set_field_value('object-group-name', value)

  def setType(self, value):
      self.root.set_field_value('type', value)

  def setIpAddress(self, value):
      self.root.set_field_value('ip-address', value)

  def setNetmask(self, value):
      self.root.set_field_value('netmask', value)

  def setTag(self, value):
      self.root.set_field_value('tag', value)


class FailoverGroup(util.BaseObject):

  def __init__(self):
      util.BaseObject.__init__(self, 'failover-group')

  def setGroupNumber(self, name):
      self.root.set_field_value('group-number', name)

  def setGroupMode(self, value):
      self.root.set_field_value('group-mode', value)

  def setPreempt(self, value):
      self.root.set_field_value('preempt', value)


class AddressBook(util.BaseObject):

  def __init__(self):
      util.BaseObject.__init__(self, 'address-book')

  def setName(self, name):
      self.root.set_field_value('name', name)

  def setZoneName(self, name):
      self.root.set_field_value('zone-name', name)

  def setAddresses(self, name):
      self.root.set_field_value('addresses', name)

  def setAddressSets(self, name):
      self.root.set_field_value('address-sets', name)      

  class ABAddress(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'ab-address')

    def setName(self, name):
        self.root.set_field_value('name', name)            

    def setDescription(self, name):
        self.root.set_field_value('description', name) 

    def setAddressType(self, name):
        self.root.set_field_value('address-type', name) 

    def setIpAddress(self, name):
        self.root.set_field_value('ip-address', name)                 

    def setNetmask(self, name):
        self.root.set_field_value('netmask', name) 

    def setDnsName(self, name):
        self.root.set_field_value('dns-name', name) 

    def setStartIp(self, name):
        self.root.set_field_value('start-ip', name) 

    def setEndIp(self, name):
        self.root.set_field_value('end-ip', name) 

    def setInterfaceName(self, name):
        self.root.set_field_value('interface-name', name) 

    def setVirtualDeviceName(self, name):
        self.root.set_field_value('virtual-device-name', name)         

  class ABAddressSet(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'ab-address-set')

    def setName(self, name):
        self.root.set_field_value('name', name)

class Address(util.BaseObject):

  def __init__(self):
      util.BaseObject.__init__(self, 'address')

  def setName(self, name):
      self.root.set_field_value('name', name)            

  def setDescription(self, name):
      self.root.set_field_value('description', name) 

  def setAddressType(self, name):
      self.root.set_field_value('address-type', name) 

  def setIpAddress(self, name):
      self.root.set_field_value('ip-address', name)                 

  def setNetmask(self, name):
      self.root.set_field_value('netmask', name) 

  def setDnsName(self, name):
      self.root.set_field_value('dns-name', name) 

  def setStartIp(self, name):
      self.root.set_field_value('start-ip', name) 

  def setEndIp(self, name):
      self.root.set_field_value('end-ip', name) 

  def setInterfaceName(self, name):
      self.root.set_field_value('interface-name', name) 

  def setVirtualDeviceName(self, name):
      self.root.set_field_value('virtual-device-name', name)

class AddressSet(util.BaseObject):

  def __init__(self):
      util.BaseObject.__init__(self, 'address-set')

  def setName(self, name):
      self.root.set_field_value('name', name)            

  def setDescription(self, name):
      self.root.set_field_value('description', name) 

  def setVirtualDeviceName(self, name):
      self.root.set_field_value('virtual-device-name', name)

  def setAddress(self, name):
      self.root.set_field_value('address', name)

  def setSubAddressSet(self, name):
      self.root.set_field_value('sub-address-set', name)

class Ha(util.BaseObject):

  def __init__(self):
      util.BaseObject.__init__(self, 'ha')

  def setGroupId(self, name):
      self.root.set_field_value('group-id', name) 

  def setGroupName(self, name):
      self.root.set_field_value('group-name', name) 

  def setPassword(self, name):
      self.root.set_field_value('password', name) 

  def setPort(self, name):
      self.root.set_field_value('port', name) 

  def setArps(self, name):
      self.root.set_field_value('arps', name) 

  def setArpsInterval(self, name):
      self.root.set_field_value('arps-interval', name) 

  def setPriority(self, name):
      self.root.set_field_value('priority', name) 

