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

class InterfaceMember(util.BaseObject):

    def __init__(self):
      util.BaseObject.__init__(self, 'interface-member')

    def setInterfaceName(self, value):
        self.root.set_field_value('interface-name', value)

    def setTagging(self, value):
        self.root.set_field_value('tagging', value)

class Vlan(util.BaseObject):

    def __init__(self):
      util.BaseObject.__init__(self, 'vlan')

    def setId(self, value):
        self.root.set_field_value('id', value)

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setMode(self, value):
        self.root.set_field_value('mode', value)

    def setMtu(self, value):
        self.root.set_field_value('mtu', value)

class Vxlan(util.BaseObject):

    def __init__(self, name):
        util.BaseObject.__init__(self, name)

    def setId(self, value):
        self.root.set_field_value('id', value)

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setMcgroup(self, value):
        self.root.set_field_value('mcgroup', value)

class FirewallVlanGroup(util.BaseObject):

    def __init__(self, name):
        util.BaseObject.__init__(self, name)

    def setVlanId(self, value):
        self.root.set_field_value('vlanId', value)

    def setGroupnumber(self, value):
        self.root.set_field_value('groupnumber', value)

class VlanGroup(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'vlan-group')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setVlanId(self, value):
        self.root.set_field_value('vlan-id', value)

    def setVlans(self, value):
        self.root.set_field_value('vlans', value)

    def setGroupNumber(self, value):
        self.root.set_field_value('group-number', value)


class PortGroup(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'port-group')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setVlanType(self, value):
        self.root.set_field_value('vlan-type', value)

    def setVlanId(self, value):
        self.root.set_field_value('vlan-id', value)

    def setVlanName(self, value):
        self.root.set_field_value('vlan-name', value)

    def setPortCount(self, value):
        self.root.set_field_value('port-count', value)

    def setMode(self, value):
        self.root.set_field_value('mode', value)

    def setPromiscuousMode(self, value):
        self.root.set_field_value('promiscuous-mode', value)


class VirtualMachine(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'virtual-machine')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setUniqueName(self, value):
        self.root.set_field_value('unique-name', value)

    def setGuestHostName(self, value):
        self.root.set_field_value('guest-host-name', value)

    def setGuestIp(self, value):
        self.root.set_field_value('guest-ip-address', value)

    def setMacAddress(self, value):
        self.root.set_field_value('mac-address', value)

    def setStatus(self, value):
        self.root.set_field_value('status', value)

    def setHostDeviceDo(self, value):
        self.root.set_field_value('host-device-do', value)

    def setMgmtStation(self, value):
        self.root.set_field_value('mgmt-Station', value)

    def setVMDevice(self, value):
        self.root.set_field_value('vm-device', value)

    def setPortProfiles(self, value):
        self.root.set_field_value('port-profiles', value)

    def setInventoriedPortPorfiles(self, value):
        self.root.set_field_value('inventoried-port-profiles', value)

class AssignPortGroup(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'assigned-vm')

    def setVMName(self, value):
        self.root.set_field_value('vm-name', value)
    
    def setInterfaceName(self, value):
        self.root.set_field_value('interface-name', value)

