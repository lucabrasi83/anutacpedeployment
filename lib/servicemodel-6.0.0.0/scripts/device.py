#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2014-2015 Anuta Networks, Inc. All Rights Reserved.

from servicemodel import util

class CommonRecordClass(util.BaseObject):
    def __init__(self, name):
        util.BaseObject.__init__(self, name)

    def setFqdn(self, value):
        self.root.set_field_value('fqdn', value)

    def setIpAddress(self, value):
        self.root.set_field_value('ip-address', value)

    def setView(self, value):
        self.root.set_field_value('view', value)

class Device(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'device')
    
    def setId(self, value):
        self.root.set_field_value('id', value)

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setCredentialSet(self, value):
        self.root.set_field_value('credential-set', value)

    def setStatus(self, value):
        self.root.set_field_value('status', value)

    def setMgmtIpAddress(self, value):
        self.root.set_field_value('mgmt-ip-address', value)

class CredentialSet(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'credential-set')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setUsername(self, value):
        self.root.set_field_value('username', value)

    def setPassword(self, value):
        self.root.set_field_value('password', value)

    def setEnablePassword(self, value):
        self.root.set_field_value('enable-password', value)

    def setSNMPRCString(self, value):
        self.root.set_field_value('read-community-str', value)

    def setTransportType(self, value):
        self.root.set_field_value('transport-type', value)

    def setPort(self, value):
        self.root.set_field_value('port-no', value)
   

class LbDomain(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'lb-domain')
    
    def setDomainNumber(self, value):
        self.root.set_field_value('domain-number', value)

    def setDomainName(self, value):
        self.root.set_field_value('domain-name', value)

    def setPartition(self, value):
        self.root.set_field_value('partition', value)


class SelfIp(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'self-ip')

    def setVlanNumber(self, value):
        self.root.set_field_value('vlan-number', value)
    
    def setName(self, value):
        self.root.set_field_value('name', value)

    def setVlanName(self, value):
        self.root.set_field_value('vlan-name', value)

    def setDomainNumber(self, value):
        self.root.set_field_value('domain-number', value)        

    def setNetmask(self, value):
        self.root.set_field_value('netmask', value)

    def setFloatingIp(self, value):
        self.root.set_field_value('floating-ip', value)

    def setIpAddress(self, value):
        self.root.set_field_value('ip-address', value)                

    def setInterfaceName(self, value):
        self.root.set_field_value('interface-name', value)

    def setTrafficGroup(self, value):
        self.root.set_field_value('traffic-group', value)                

    def setPartition(self, value):
        self.root.set_field_value('partition', value)
        
    def setPortLockdown(self, value):
        self.root.set_field_value('port-lockdown', value)

class HaSelfIp(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'ha-self-ip')

    def setVlanNumber(self, value):
        self.root.set_field_value('vlan-number', value)
    
    def setName(self, value):
        self.root.set_field_value('name', value)

    def setVlanName(self, value):
        self.root.set_field_value('vlan-name', value)

    def setDomainNumber(self, value):
        self.root.set_field_value('domain-number', value)        

    def setNetmask(self, value):
        self.root.set_field_value('netmask', value)

    def setFloatingIp(self, value):
        self.root.set_field_value('floating-ip', value)

    def setIpAddress(self, value):
        self.root.set_field_value('ip-address', value)                

    def setInterfaceName(self, value):
        self.root.set_field_value('interface-name', value)

    def setTrafficGroup(self, value):
        self.root.set_field_value('traffic-group', value)                

    def setPartition(self, value):
        self.root.set_field_value('partition', value)
        
    def setPortLockdown(self, value):
        self.root.set_field_value('port-lockdown', value)

class FloatingSelfIp(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'floating-self-ip')

    def setVlanNumber(self, value):
        self.root.set_field_value('vlan-number', value)
    
    def setName(self, value):
        self.root.set_field_value('name', value)

    def setVlanName(self, value):
        self.root.set_field_value('vlan-name', value)

    def setDomainNumber(self, value):
        self.root.set_field_value('domain-number', value)        

    def setNetmask(self, value):
        self.root.set_field_value('netmask', value)

    def setFloatingIp(self, value):
        self.root.set_field_value('floating-ip', value)

    def setIpAddress(self, value):
        self.root.set_field_value('ip-address', value)                

    def setInterfaceName(self, value):
        self.root.set_field_value('interface-name', value)

    def setTrafficGroup(self, value):
        self.root.set_field_value('traffic-group', value)                

    def setPartition(self, value):
        self.root.set_field_value('partition', value)
        
    def setPortLockdown(self, value):
        self.root.set_field_value('port-lockdown', value)

class StaticRoute(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'static-route')

    def setDestIpAddress(self, value):
        self.root.set_field_value('dest-ip-address', value)

    def setDestMask(self, value):
        self.root.set_field_value('dest-mask', value)

    def setNextHopIp(self, value):
        self.root.set_field_value('next-hop-ip', value)

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setDescription(self, value):
        self.root.set_field_value('description', value)


class TrafficGroup(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'traffic-group')

    def setName(self, value):
        self.root.set_field_value('name', value)



class ARecordClass(CommonRecordClass):
    def __init__(self):
        util.BaseObject.__init__(self, 'a-record')


class HostRecordClass(CommonRecordClass):
    def __init__(self):
        util.BaseObject.__init__(self, 'host-record')
