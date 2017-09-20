#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2014-2015 Anuta Networks, Inc. All Rights Reserved.

from servicemodel import yang
from servicemodel import util

class AclRule(util.BaseObject):
    def __init__(self):
       util.BaseObject.__init__(self, 'acl-rule')
       
    def setName(self, value):
        self.root.set_field_value('name', value)
    
    def setDescription(self, value):
        self.root.set_field_value('description', value)
    
    def setLinenumber(self, value):
        self.root.set_field_value('linenumber', value)
        
    def setAction(self, value):
        self.root.set_field_value('action', value)
        
    def setLayer4protocol(self, value):
        self.root.set_field_value('layer4protocol', value)
        
    def setSourceZone(self, value):
        self.root.set_field_value('source-zone', value)
        
    def setDestZone(self, value):
        self.root.set_field_value('dest-zone', value)
        
    def setApplication(self, value):
        self.root.set_field_value('application', value)
        
    def setSourceConditionType(self, value):
        self.root.set_field_value('source-condition-type', value)
        
    def setSourceIp(self, value):
        self.root.set_field_value('source-ip', value)
        
    def setSourceMask(self, value):
        self.root.set_field_value('source-mask', value)
        
    def setSourceObjName(self, value):
        self.root.set_field_value('source-obj-name', value)
        
    def setSourcePortOperator(self, value):
        self.root.set_field_value('source-port-operator', value)
        
    def setSourcePort(self, value):
        self.root.set_field_value('source-port', value)
        
    def setDestConditionType(self, value):
        self.root.set_field_value('dest-condition-type', value)
        
    def setDestIp(self, value):
        self.root.set_field_value('dest-ip', value)
        
    def setDestMask(self, value):
        self.root.set_field_value('dest-mask', value)
        
    def setDestObjName(self, value):
        self.root.set_field_value('dest-obj-name', value)
        
    def setDestPortOperator(self, value):
        self.root.set_field_value('dest-port-operator', value)
        
    def setDestPort(self, value):
        self.root.set_field_value('dest-port', value)
        
    def setNextAclruleName(self, value):
        self.root.set_field_value('next-acl-rule-name', value)
        
    def setPrevAclruleName(self, value):
        self.root.set_field_value('prev-acl-rule-name', value)
        
    def setLogAction(self, value):
        self.root.set_field_value('log-action', value)
        
    def setRuleNat(self, value):
        self.root.set_field_value('rule-nat', value)
        
    def setTag(self, value):
        self.root.set_field_value('tag', value)
        
    def setService(self, value):
        self.root.set_field_value('service', value)

    def setSample(self, value):
        self.root.set_field_value('sample', value)

    def setCounter(self, value):
        self.root.set_field_value('counter', value)

class AccessList(util.BaseObject):
    def __init__(self):
       util.BaseObject.__init__(self, 'access-list')
       
    def setName(self, value):
        self.root.set_field_value('name', value)

    def setMode(self, value):
        self.root.set_field_value('mode', value)
        
    def setSourceZone(self, value):
        self.root.set_field_value('source-zone', value)

    def setDestZone(self, value):
        self.root.set_field_value('dest-zone', value)

    def setVirtualDeviceName(self, value):
        self.root.set_field_value('virtual-device-name', value)

    def setAclRules(self, value):
        self.root.set_field_value('acl-rules', value)

    def setStartRemark(self, value):
        self.root.set_field_value('start-remark', value)

    def setEndRemark(self, value):
        self.root.set_field_value('end-remark', value)

    def setOutInterfaceName(self, value):
        self.root.set_field_value('out-interface-name', value)

    def setInInterfaceName(self, value):
        self.root.set_field_value('in-interface-name', value)

class InterfaceAccessList(util.BaseObject):
    def __init__(self):
       util.BaseObject.__init__(self, 'interface-access-list')
       
    def setName(self, value):
        self.root.set_field_value('name', value)

    def setAclName(self, value):
        self.root.set_field_value('acl-name', value)

    def setInterfaceName(self, value):
        self.root.set_field_value('interface-name', value)

    def setContextName(self, value):
        self.root.set_field_value('context-name', value)

    def setDirection(self, value):
        self.root.set_field_value('direction', value)                        

class Address(util.BaseObject):
    def __init__(self):
       util.BaseObject.__init__(self, 'address')
       
    def setName(self, value):
        self.root.set_field_value('name', value)
        
    def setVirtualDeviceName(self, value):
        self.root.set_field_value('virtual-device-name', value)
        
    def setAddressType(self, value):
        self.root.set_field_value('address-type', value)
        
    def setIpAddress(self, value):
        self.root.set_field_value('ip-address', value)
    
    def setNetmask(self, value):
        self.root.set_field_value('netmask', value)