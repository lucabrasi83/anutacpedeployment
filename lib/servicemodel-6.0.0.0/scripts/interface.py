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


class Interface(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'interface')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setLongName(self, value):
        self.root.set_field_value('long-name', value)

    def setRncName(self, value):
        self.root.set_field_value('rnc-name', value)

    def setCos(self, value):
        self.root.set_field_value('cos', value)

    def setPos(self, value):
        self.root.set_field_value('pos', value)

    def setVRRPType(self, value):
        self.root.set_field_value('vrrp-type', value)

    def setVpnInstanceName(self, value):
        self.root.set_field_value('vpn-instance-name', value)

    def setVplsName(self, value):
        self.root.set_field_value('vpls-name', value)

    def setBfd(self, value):
        #TODO- temperorly changing this from
        # self.root.set_field_value('l3features:bfd-name', value) to self.root.set_field_value('bfd-name', value)
        self.root.set_field_value('bfd-name', value)

    def setPortNumberVpls(self, value):
        self.root.set_field_value('port-number-vpls', value)

    def setPortNumberVlan(self, value):
        self.root.set_field_value('port-number-vlan', value)

    def setPortType(self, value):
        self.root.set_field_value('port-type', value)

    def setVirtualEthernetNumber(self, value):
        self.root.set_field_value('virtual-ethernet-number', value)

    def setBandwidth(self, value):
        self.root.set_field_value('bandwidth', value)

    def setEthernetNumberVpls(self, value):
        self.root.set_field_value('ethernet-number-vpls', value)

    def setInterfaceMode(self, value):
        self.root.set_field_value('interface-mode', value)

    def setInsideName(self, value):
        self.root.set_field_value('inside-name', value)

    def setSecurityLevelInside(self, value):
        self.root.set_field_value('security-level-inside', value)

    def setSlotNumber(self, value):
        self.root.set_field_value('slot-number', value)

    def setPort(self, value):
        self.root.set_field_value('port', value)

    def setPortNumber(self, value):
        self.root.set_field_value('port-number', value)

    def setDescription(self, value):
        self.root.set_field_value('description', value)

    def setMode(self, value):
        self.root.set_field_value('mode', value)

    def setIpAddress(self, value):
        self.root.set_field_value('ip-address', value)

    def setNetmask(self, value):
        self.root.set_field_value('netmask', value)

    def setSecondaryip(self, value):
        self.root.set_field_value('secondaryip', value)

    def setMtu(self, value):
        self.root.set_field_value('mtu', value)

    def setAllowedVlans(self, value):
        if value == None or not isinstance(value, list):
            value = []
        self.root.set_field_value('allowed-vlans', value)

    def setAdminState(self, value):
        self.root.set_field_value('admin-state', value)

    def setVlan(self, value):
        self.root.set_field_value('vlan', value)

    def setDhcp(self, value):
        self.root.set_field_value('dhcp', value)

    def setMinLink(self, value):
        self.root.set_field_value('minimum-links', value)

    def setVisibleInterface(self, value):
        self.root.set_field_value('visible-interface', value)

    def setUnit(self, value):
        self.root.set_field_value('unit', value)

    def setVrf(self, value):
        #TODO- temperorly changing this from
        # self.root.set_field_value('l3features:vrf', value) to self.root.set_field_value('vrf', value)
        self.root.set_field_value('vrf', value)

    def setContextName(self, value):
        self.root.set_field_value('context-name', value)

    def setHsrp(self, value):
        self.root.set_field_value('hsrp', value)

    def setVrrp(self, value):
        self.root.set_field_value('vrrp', value)

    def setInterfaceState(self, value):
        # FIXME: temporary hack
        state = util.BaseObj()
        state.set_field_value('operationalstate', value)
        # value = '<operationalstate>%s</operationalstate>' % (value)
        # print 'setting value=%s' % (value)
        self.root.set_field_value('interface-state', state)

    def setMplsDeviceRole(self, value):
        self.root.set_field_value('mpls-device-role', value)

    def setInnerVlan(self, value):
        self.root.set_field_value('inner-vlan', value)

    def setOutboundQos(self, value):
        self.root.set_field_value('outbound-qos', value)

    def setInboundQos(self, value):
        self.root.set_field_value('inbound-qos', value)

    def setLinkNegotiation(self, value):
        self.root.set_field_value('link-negotiation', value)

    def setAclInboundName(self, value):
        self.root.set_field_value('acl-inbound-name', value)

    def setAclOutboundName(self, value):
        self.root.set_field_value('acl-outbound-name', value)

    def setEncapMode(self, value):
        self.root.set_field_value('encap-mode', value)

    def setMgmtProfile(self, value):
        self.root.set_field_value('mgmt-profile', value)

    def setIpAddress2(self, value):
        self.root.set_field_value('ip-address2', value)

    def setNetmask2(self, value):
        self.root.set_field_value('netmask2', value)

    def setAddress1Comment(self, value):
        self.root.set_field_value('address1-comment', value)

    def setAddress2Comment(self, value):
        self.root.set_field_value('address2-comment', value)

    def setRpfCheck(self, value):
        self.root.set_field_value('rpf-check', value)

    def setPostscrubUnit(self, value):
        self.root.set_field_value('postscrub-unit', value)

    def setTunnelSourceIP(self, value):
        self.root.set_field_value('gre-tunnel:source-ip', value)

    def setTunnelDestinationIP(self, value):
        self.root.set_field_value('gre-tunnel:destination-ip', value)

    def setKeepaliveTime(self, value):
        self.root.set_field_value('keepalive-time', value)

    def setHoldTime(self, value):
        self.root.set_field_value('hold-time-up', value)

    def setHoldTimeDown(self, value):
        self.root.set_field_value('hold-time-down', value)

    def setTunnelDestinationVrf(self, value):
        self.root.set_field_value('gre-tunnel:destination-vrf', value)

    def setDefaultRoute(self, value):
        self.root.set_field_value('default-route', value)

    def setGateway(self, value):
        self.root.set_field_value('gateway', value)

    def setLACPActivePeroidicFast(self, value):
        self.root.set_field_value('lacp-active-periodic-fast', value)

    def setLACPActive(self, value):
        self.root.set_field_value('lacp-active-enable', value)

    def setLinkSpeed(self, value):
        self.root.set_field_value('link-speed', value)

    def setPortChannelName(self, value):
        self.root.set_field_value('port-channel-name', value)

    def setFcoe(self, value):
        self.root.set_field_value('fcoe-lag', value)


class HSRP(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'hsrp')

    def setIpAddress(self, value):
        self.root.set_field_value('ip-address', value)

    def setGroup(self, value):
        self.root.set_field_value('group', value)

    def setGroupName(self, value):
        self.root.set_field_value('group-name', value)

    def setBfd(self, value):
        self.root.set_field_value('bfd', value)

    def setBfdInterval(self, value):
        self.root.set_field_value('bfd-interval', value)

    def setBfdMultiplier(self, value):
        self.root.set_field_value('bfd-multiplier', value)

    def setPriority(self, value):
        self.root.set_field_value('priority', value)

    def setHsrpPreempt(self, value):
        self.root.set_field_value('hsrp-preempt', value)

    def setPreemptReload(self, value):
        self.root.set_field_value('preempt-reload', value)

    def setAuthType(self, value):
        self.root.set_field_value('auth-type', value)

    def setAuthKey(self, value):
        self.root.set_field_value('auth-key', value)

    def setTimer1(self, value):
        self.root.set_field_value('timer1', value)

    def setTimer2(self, value):
        self.root.set_field_value('timer2', value)

    def setVersion(self, value):
        self.root.set_field_value('version', value)

    def setTrackInterface(self, value):
        self.root.set_field_value('track-interface', value)

class TrackInterface(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'track-interface')

    def setName(self, value):
        self.root.set_field_value('name', value)
    def setMgo(self, value):
        self.root.set_field_value('mgo', value)

class VRRP(util.BaseObject):

    class Bfd(util.BaseObject):
        def __init__(self):
            util.BaseObject.__init__(self, 'bfd')

        def setPeerIp(self, value):
            self.root.set_field_value('peer-ip', value)

        def setBfdVrrpId(self, value):
            self.root.set_field_value('bfd-vrrp-id', value)

        def setLocal(self, value):
            self.root.set_field_value('local', value)

        def setRemote(self, value):
            self.root.set_field_value('remote', value)

    def __init__(self):
        util.BaseObject.__init__(self, 'vrrp')

    def setBfd(self, value):
        self.root.set_field_value('bfd', value)

    def setVrid(self, value):
        self.root.set_field_value('vrid', value)

    def setVrrpInterfaceName(self, value):
        self.root.set_field_value('vrrp-interface-name', value)

    def setUnit(self, value):
        self.root.set_field_value('unit', value)

    def setInetAddress(self, value):
        self.root.set_field_value('inet-address', value)

    def setBackupAddress(self, value):
        self.root.set_field_value('backup-address', value)

    def setMask(self, value):
        self.root.set_field_value('mask', value)

    def setPriority(self, value):
        self.root.set_field_value('priority', value)

    def setVrrpGroup(self, value):
        self.root.set_field_value('vrrp-group', value)

    def setVirtualAddress(self, value):
        self.root.set_field_value('virtual-address', value)

    def setBackupAddress(self, value):
        self.root.set_field_value('backup-address', value)


    def setAdvertisementInterval(self, value):
        self.root.set_field_value('advertisement-interval', value)

    def setPreempt(self, value):
        self.root.set_field_value('preempt', value)

    def setAuthType(self, value):
        self.root.set_field_value('auth-type', value)

    def setAuthKey(self, value):
        self.root.set_field_value('auth-key', value)

    def setTrackInterface(self, value):
        self.root.set_field_value('track-interface', value)

    def setVrrpType(self, value):
        self.root.set_field_value('vrrp-interface-type', value)

    def setTrackInterface(self, value):
        self.root.set_field_value('track-interface', value)

    def setVrrpTrackGroup(self, value):
        self.root.set_field_value('vrrp-track-group', value)

    def setDelay(self, value):
        self.root.set_field_value('delay-interval', value)


class PortQoS(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'port-qos')

    def setPort(self, value):
        self.root.set_field_value('port', value)

    def setPortQosGroupTemplate(self, value):
        self.root.set_field_value('port-qos-group-template' , value)

    def setPortQosSchedulerPolicy(self, value):
        self.root.set_field_value('port-qos-scheduler-policy', value)

    def setRateLimit(self, value):
        self.root.set_field_value('rate-limit', value)
    

