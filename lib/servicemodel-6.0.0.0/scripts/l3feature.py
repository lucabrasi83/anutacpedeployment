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

class IpPrefixList(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'ip-prefixlist')

    def setName(self, name):
        self.root.set_field_value('name', name)

    def setVdomName(self, value):
        self.root.set_field_value('vdom-name', value)


class IpPrefixListEntry(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'ip-prefixlist-entry')

    def setPrefixName(self, name):
        self.root.set_field_value('prefix-name', name)

    def setRuleNum(self, name):
        self.root.set_field_value('rule-num', name)

    def setSubnet(self, value):
        self.root.set_field_value('subnet', value)

    def setCompare(self, value):
        self.root.set_field_value('compare', value)

    def setNum(self, value):
        self.root.set_field_value('num', value)

    def setCondition(self, value):
        self.root.set_field_value('condition', value)


class RedistributeCommon(util.BaseObject):

    def __init__(self, name):
        util.BaseObject.__init__(self, name)

    def setProtocol(self, value):
        self.root.set_field_value('protocol', value)


class NeighborCommon(util.BaseObject):

    def __init__(self, name):
        util.BaseObject.__init__(self, name)

    def setIpAddress(self, value):
        self.root.set_field_value('ip-address', value)

    def setNetmask(self, value):
        self.root.set_field_value('netmask', value)

    def setLocalInterface(self, value):
        self.root.set_field_value('local-interface', value)

class Network(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'network')

    def setIpAddress(self, value):
        self.root.set_field_value('ip-address', value)

    def setNetmask(self, value):
        self.root.set_field_value('netmask', value)


class Vrf(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'vrf')

    def setRd(self, rd):
        self.root.set_field_value('rd', rd)

    def setName(self, name):
        self.root.set_field_value('name', name)

    def setDescription(self, description):
        self.root.set_field_value('description', description)

    def setMaximumPrefixipv4(self, maximumprefixipv4):
        self.root.set_field_value('maximum-prefixes-ipv4', maximumprefixipv4)

    def setMaximumPrefixipv6(self, maximumprefixipv6):
        self.root.set_field_value('maximum-prefixes-ipv6', maximumprefixipv6)

    def setImportRoutePolicy(self, value):
        self.root.set_field_value('import-route-policy', value)

    def setExportRoutePolicy(self, value):
        self.root.set_field_value('export-route-policy', value)

    def setRtImport(self, value):
        self.root.set_field_value('rt-import', value)

    def setRtExport(self, value):
        self.root.set_field_value('rt-export', value)

    def setVrfImport(self, value):
        self.root.set_field_value('vrf-import', value)

    def setVrfExport(self, value):
        self.root.set_field_value('vrf-export', value)

    def setRouterBGP(self, value):
        self.root.set_field_value('router-bgp', value)

    def setRouterOSPF(self, value):
        self.root.set_field_value('router-ospf', value)

    def setMpls(self, value):
        self.root.set_field_value('mpls', value)

    def setStaticRoutes(self, value):
        self.root.set_field_value('static-routes', value)

    def setPrefixSets(self, value):
        self.root.set_field_value('prefix-sets', value)

    def setForwardingOptions(self, value):
        self.root.set_field_value('forwarding-options', value)

    def setClusterId(self, value):
        self.root.set_field_value('cluster-id', value)

class ForwardingOptions(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'forwarding-options')

    def setUnicastRpf(self, value):
        self.root.set_field_value('unicast-rpf', value)

    def setRpfLooseModeDiscard(self, value):
        self.root.set_field_value('rpf-loose-mode-discard', value)

    class RpfLooseModeDiscard(util.BaseObject):

        def __init__(self):
            util.BaseObject.__init__(self, 'rpf-loose-mode-discard')

        def setFamily(self, value):
            self.root.set_field_value('family', value)


class PrefixSet(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'prefix-set')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setMatchConditions(self, value):
        self.root.set_field_value('match-conditions', value)

    def setCustomPrefixSet(self, value):
        self.root.set_field_value('custom-prefix-set', value)


class CustomPrefixSet(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'custom-prefix-set')

    def setPrefixSetBuf(self, value):
        self.root.set_field_value('prefix-set-buf', value)


class MatchCondition(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'match-condition')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setIpAddress(self, value):
        self.root.set_field_value('ip-address', value)

    def setMaskLength(self, value):
        self.root.set_field_value('mask-length', value)

    def setMinMatchLength(self, value):
        self.root.set_field_value('min-match-length', value)

    def setMaxMatchLength(self, value):
        self.root.set_field_value('max-match-length', value)

class RibGroup(util.BaseObject):
    def __init__(self):
        util.BaseObject.__init__(self, 'rib-group')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setImportRib(self, value):
        self.root.set_field_value('import-rib', value)

class RouterBgp(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'router-bgp')

    def setAsNumber(self, value):
        self.root.set_field_value('as-number', value)

    def setRouterId(self, value):
        self.root.set_field_value('router-id', value)

    def setAddressFamily(self, value):
        self.root.set_field_value('address-family', value)

    def setNeighbor(self, value):
        self.root.set_field_value('neighbor', value)

    def setRedistribute(self, value):
        self.root.set_field_value('redistribute', value)

    def setNetwork(self, value):
        self.root.set_field_value('network', value)

    def setGroup(self, value):
        self.root.set_field_value('group', value)

    def setLogNeighborChanges(self, value):
        self.root.set_field_value('log-neighbor-changes', value)

    class Redistribute(RedistributeCommon):

        def __init__(self):
            RedistributeCommon.__init__(self, 'redistribute')

        def setProtocol(self, value):
            self.root.set_field_value('protocol', value)

        def setOspfProcessId(self, value):
            self.root.set_field_value('ospf-process-id', value)

        def setRoutePolicyStatic(self, value):
            self.root.set_field_value('route-policy-static', value)

        def setRoutePolicyConnected(self, value):
            self.root.set_field_value('route-policy-connected', value)

    class Neighbor(NeighborCommon):

        def __init__(self):
            NeighborCommon.__init__(self, 'neighbor')

        def setAsNumber(self, value):
            self.root.set_field_value('as-number', value)

        def setDescription(self, value):
            self.root.set_field_value('description', value)

        def setRouteLimit(self, value):
            self.root.set_field_value('route-limit', value)

        def setAdvComm(self, value):
            self.root.set_field_value('advertise-community', value)

        def setAdvExtComm(self, value):
            self.root.set_field_value('advertise-ext-community', value)

        def setBfd(self, value):
            self.root.set_field_value('bfd', value)

        def setIpAddress(self, value):
            self.root.set_field_value('ip-address', value)

        def setPeerGroup(self, value):
            self.root.set_field_value('peer-group', value)

        def setLocalAsNumber(self, value):
            self.root.set_field_value('local-as-number', value)

        def setAsOverride(self, value):
            self.root.set_field_value('as-override', value)

        def setNextHopSelf(self, value):
            self.root.set_field_value('next-hop-self', value)

        def setSoftReconfiguration(self, value):
            self.root.set_field_value('soft-reconfiguration', value)

        def setEncryption(self, value):
            self.root.set_field_value('encryption', value)

        def setPassword(self, value):
            self.root.set_field_value('password', value)

        def setInboundRoutepolicy(self, value):
            self.root.set_field_value('inbound-routepolicy', value)

        def setOutboundRoutepolicy(self, value):
            self.root.set_field_value('outbound-routepolicy', value)

        def setGroup(self, value):
            self.root.set_field_value('group', value)

        def setAuthKey(self, value):
            self.root.set_field_value('auth-key', value)

        def setType(self, value):
            self.root.set_field_value('type', value)

        def setSendCommunity(self, value):
            self.root.set_field_value('send-community', value)

        def setInRouteMap(self, value):
            self.root.set_field_value('in-route-map', value)

        def setOutRouteMap(self, value):
            self.root.set_field_value('out-route-map', value)

        def setRemoteAs(self, value):
            self.root.set_field_value('remote-as', value)

        def setDefOriginateRouteMap(self, value):
            self.root.set_field_value('def-originate-route-map', value)

        def setDefOriginate(self, value):
            self.root.set_field_value('default-originate', value)

        def setAllowasin(self, value):
            self.root.set_field_value('allowas-in', value)

        def setAllowasinValue(self, value):
            self.root.set_field_value('allowas_in_value', value)

    class PeerGroup(util.BaseObject):

        def __init__(self):
            util.BaseObject.__init__(self, 'peer-group')

        def setName(self, value):
            self.root.set_field_value('name', value)

        def setDescription(self, value):
            self.root.set_field_value('description', value)

        def setRemoteAs(self, value):
            self.root.set_field_value('remote-as', value)

        def setTimers(self, value):
            self.root.set_field_value('timers', value)

        def setKeepaliveInterval(self, value):
            self.root.set_field_value('keepalive-interval', value)

        def setHoldtime(self, value):
            self.root.set_field_value('holdtime', value)

        def setNextHopSelf(self, value):
            self.root.set_field_value('next-hop-self', value)

        def setSendCommunity(self, value):
            self.root.set_field_value('send-community', value)

        def setInRouteMap(self, value):
            self.root.set_field_value('in-route-map', value)

        def setOutRouteMap(self, value):
            self.root.set_field_value('out-route-map', value)

        def setDefOriginateRouteMap(self, value):
            self.root.set_field_value('def-originate-route-map', value)

        def setDefOriginate(self, value):
            self.root.set_field_value('default-originate', value)

        def setCidr(self, value):
            self.root.set_field_value('cidr', value)

    class RouterBgpListen(util.BaseObject):

        def __init__(self):
            util.BaseObject.__init__(self, 'listen')

        def setType(self, value):
            self.root.set_field_value('type', value)

        def setLimitVal(self, value):
            self.root.set_field_value('limitval', value)

        def setCidr(self, value):
            self.root.set_field_value('cidr', value)

        def setPeerGroup(self, value):
            self.root.set_field_value('peer-group', value)

    class RouterBgpAggregateSummaryNetwork(util.BaseObject):

        def __init__(self):
            util.BaseObject.__init__(self, 'aggregate-summary-network')

        def setNetwork(self, value):
            self.root.set_field_value('network', value)

        def setSummaryOnly(self, value):
            self.root.set_field_value('aggregate-summary-only', value)

    class Group(util.BaseObject):
        def __init__(self):
            util.BaseObject.__init__(self, 'group')

        def setName(self, value):
            self.root.set_field_value('name', value)

        def setMetricOut(self, value):
            self.root.set_field_value('metric-out', value)

        def setHoldTime(self, value):
            self.root.set_field_value('hold-time', value)

        def setPrefixLimitMax(self, value):
            self.root.set_field_value('prefix-limit-max', value)

        def setTearDown(self, value):
            self.root.set_field_value('tear-down', value)

        def setIdleTimeout(self, value):
            self.root.set_field_value('idle-timeout', value)

        def setAdvertiseInactive(self, value):
            self.root.set_field_value('advertise-inactive', value)

        def setRemovePrivate(self, value):
            self.root.set_field_value('remove-private', value)

        def setGracefulRestart(self, value):
            self.root.set_field_value('graceful-restart', value)

        def setLogUpdown(self, value):
            self.root.set_field_value('log-updown', value)

        def setImport(self, value):
            self.root.set_field_value('import', value)

        def setExport(self, value):
            self.root.set_field_value('export', value)

        def setRibGroup(self, value):
            self.root.set_field_value('rib-group', value)

        class Import(util.BaseObject):
            def __init__(self):
                util.BaseObject.__init__(self, 'import')

            def setName(self, value):
                self.root.set_field_value('name', value)

        class Export(util.BaseObject):
            def __init__(self):
                util.BaseObject.__init__(self, 'export')

            def setName(self, value):
                self.root.set_field_value('name', value)

class RouterOSPF(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'router-ospf')

    def setProcessId(self, value):
        self.root.set_field_value('process-id', value)

    def setRouterId(self, value):
        self.root.set_field_value('router-id', value)

    def setNeighbor(self, value):
        self.root.set_field_value('neighbor', value)

    def setInterface(self, value):
        self.root.set_field_value('interface', value)

    class Interface(util.BaseObject):

        def __init__(self):
            util.BaseObject.__init__(self, 'interface')

        def setInterfaceName(self, value):
            self.root.set_field_value('interface-name', value)

        def setZoneName(self, value):
            self.root.set_field_value('zone-name', value)

        def setArea(self, value):
            self.root.set_field_value('area', value)

        def setCost(self, value):
            self.root.set_field_value('cost', value)

        def setMtu(self, value):
            self.root.set_field_value('mtu', value)

        def setMinLink(self, value):
            self.root.set_field_value('minimum-links', value)

        def setPriority(self, value):
            self.root.set_field_value('priority', value)

        def setNetworkType(self, value):
            self.root.set_field_value('network-type', value)

        def setNeighbor(self, value):
            self.root.set_field_value('neighbor', value)

        def setAuthType(self, value):
            self.root.set_field_value('auth-type', value)

        def setMd5Key(self, value):
            self.root.set_field_value('md5-key', value)

        def setKeyId(self, value):
            self.root.set_field_value('key-id', value)

    class Neighbor(NeighborCommon):

        def __init__(self):
            NeighborCommon.__init__(self, 'neighbor')

        def setArea(self, value):
            self.root.set_field_value('area', value)

    def setRedistribute(self, value):
        self.root.set_field_value('redistribute', value)

    class Redistribute(RedistributeCommon):

        def __init__(self):
            RedistributeCommon.__init__(self, 'redistribute')

        def setBgpAsNumber(self, value):
            self.root.set_field_value('bgp-as-number', value)

        def setMetric(self, value):
            self.root.set_field_value('metric', value)

        def setRoutemapName(self, value):
            self.root.set_field_value('routemap-name', value)

class Mpls(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'mpls')

    def setLoopbackInterface(self, value):
        self.root.set_field_value('loopback-interface', value)

class StaticRoute(util.BaseObject):
    class NextHopIp(util.BaseObject):
        def __init__(self):
            util.BaseObject.__init__(self, 'next-hop-ip')

        def setNextHopIp(self, value):
            self.root.set_field_value('next-hop-ip', value)

    def __init__(self):
        util.BaseObject.__init__(self, 'static-route')

    def setDestIpAddress(self, value):
        self.root.set_field_value('dest-ip-address', value)

    def setDestMask(self, value):
        self.root.set_field_value('dest-mask', value)
    
    def setDescription(self, vlaue):
        self.root.set_field_value('description', vlaue)

    def setNextHopIp(self, value):
        self.root.set_field_value('next-hop-ip', value)

    def setNextRoutingTable(self, value):
        self.root.set_field_value('next-routing-table', value)

    def setInterfaceName(self, value):
        self.root.set_field_value('interface-name', value)

    def setDomainNumber(self, value):
        self.root.set_field_value('domain-number', value)

    def setMetric(self, value):
        self.root.set_field_value('metric', value)

    def setSeqNum(self, value):
        self.root.set_field_value('seq-num', value)

    def setName(self, value):
        self.root.set_field_value('name', value)

class LbRoute(util.BaseObject):
    def __init__(self):
        util.BaseObject.__init__(self, 'lb-route')

    def setDestIpAddress(self, value):
        self.root.set_field_value('dest-ip-address', value)

    def setDestMask(self, value):
        self.root.set_field_value('dest-mask', value)

    def setNextHopIp(self, value):
        self.root.set_field_value('next-hop-ip', value)

    def setNextRoutingTable(self, value):
        self.root.set_field_value('next-routing-table', value)

    def setInterfaceName(self, value):
        self.root.set_field_value('interface-name', value)

    def setDomainNumber(self, value):
        self.root.set_field_value('domain-number', value)

class TunnelInterface(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'dmvpntunnel')

    def setTunnelInterfaceName(self, value):
        self.root.set_field_value('name', value)

    def setDescription(self, value):
        self.root.set_field_value('description', value)

    def setType(self, value):
        self.root.set_field_value('type', value)

    def setIP(self, value):
        self.root.set_field_value('ipaddress', value)

    def setNetmask(self, value):
        self.root.set_field_value('netmask', value)

    def setTunnelSource(self, value):
        self.root.set_field_value('tunnel-source', value)

    def setTunnelMode(self, value):
        self.root.set_field_value('tunnel-mode', value)

    def setTunnelKey(self, value):
        self.root.set_field_value('tunnel-key', value)

    def setNhrpId(self, value):
        self.root.set_field_value('nhrp-network-id', value)

    def setNhrpKey(self, value):
        self.root.set_field_value('nhrp-auth-key', value)

    def setBandwidth(self, value):
        self.root.set_field_value('bandwidth', value)

    def setDelay(self, value):
        self.root.set_field_value('delay', value)

    def setAuthType(self, value):
        self.root.set_field_value('authentication-type', value)

    def setEigrpNum(self, value):
        self.root.set_field_value('eigrpProcessNumber', value)

    def setKeyChain(self, value):
        self.root.set_field_value('key-chain', value)

    def setVrf(self, value):
        self.root.set_field_value('vrf-name', value)

    def setFrontVrf(self, value):
        self.root.set_field_value('front-vrf-name', value)

    def setIpsecProfile(self, value):
        self.root.set_field_value('ipsec-profile-name', value)

    def setRoutingProtocol(self, value):
        self.root.set_field_value('routing-protocol', value)

    def setHubList(self, value):
        self.root.set_field_value('hub-list', value)

    def setNhrpQosMaps(self, value):
        self.root.set_field_value('nhrp-qos-maps', value)

    def setDomainName(self, value):
        self.root.set_field_value('domain-name', value)

    def setNhrpGrpName(self, value):
        self.root.set_field_value('nhrp-grp-name', value)

    class NhrpMap(util.BaseObject):

        def __init__(self):
            util.BaseObject.__init__(self, 'nhrp-maps')

        def setSourceIP(self, value):
            self.root.set_field_value('sourceip', value)

        def setDestIP(self, value):
            self.root.set_field_value('destip', value)

    class NhrpQosMap(util.BaseObject):

        def __init__(self):
            util.BaseObject.__init__(self, 'nhrp-qos-maps')

        def setName(self, value):
            self.root.set_field_value('name', value)

        def setPolicyMap(self, value):
            self.root.set_field_value('policy-map', value)

    class DomainPath(util.BaseObject):

        def __init__(self):
            util.BaseObject.__init__(self, 'domain-path')

        def setDomainName(self, value):
            self.root.set_field_value('domain-name', value)

        def setPathId(self, value):
            self.root.set_field_value('path-id', value)

class RoutePolicy(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'route-policy')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setCplString(self, value):
        self.root.set_field_value('cpl-string', value)

class RouteMap(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'route-map')

    def setName(self, value):
        self.root.set_field_value('name', value)

    class RouteMapEntries(util.BaseObject):
        def __init__(self):
            util.BaseObject.__init__(self, 'route-map-entries')

        def setAction(self, value):
            self.root.set_field_value('action', value)

        def setSequence(self, value):
            self.root.set_field_value('seq', value)

        def setPrefixList(self, value):
            self.root.set_field_value('prefix-list', value)

        def setNextHopValue(self, value):
            self.root.set_field_value('next-hop-value', value)

        def setLocalPreferenceValue(self, value):
            self.root.set_field_value('local-preference-value', value)

        def setCommunityAttribute(self, value):
            self.root.set_field_value('community-attribute', value)

        def setVdomName(self, value):
            self.root.set_field_value('vdom-name', value)

        class MatchCondition(util.BaseObject):

            def __init__(self):
                util.BaseObject.__init__(self, 'match-condition')

            def setConditionType(self, value):
                self.root.set_field_value('condition-type', value)

            def setValue(self, value):
                self.root.set_field_value('value', value)


        class SetAction(util.BaseObject):

            def __init__(self):
                util.BaseObject.__init__(self, 'set-action')

            def setSetType(self, value):
                self.root.set_field_value('set-type', value)

            def setValue(self, value):
                self.root.set_field_value('value', value)


class PrefixList(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'prefix-list')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setPrefixPolicy(self, value):
        self.root.set_field_value('prefix-policy', value)

    def setPrefix(self, value):
        self.root.set_field_value('prefix', value)

    class PrefixPolicy(util.BaseObject):
        def __init__(self):
            util.BaseObject.__init__(self, 'prefix-policy')

        def setName(self, value):
            self.root.set_field_value('name', value)

        def setAction(self, value):
            self.root.set_field_value('action', value)

    class Prefix(util.BaseObject):
        def __init__(self):
            util.BaseObject.__init__(self, 'prefix')

        def setIpAddress(self, value):
            self.root.set_field_value('ip-address', value)

        def setNetmask(self, value):
            self.root.set_field_value('netmask', value)

class Vpls(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'vpls')

    def setId(self, value):
        self.root.set_field_value('id', value)

    def setVplsName(self, value):
        self.root.set_field_value('vpls-name', value)

    def setServiceName(self, value):
        self.root.set_field_value('service-name', value)

    def setDevicePortNum(self, value):
        self.root.set_field_value('device-port-num', value)

    def setVplsMeshId(self, value):
        self.root.set_field_value('vpls-mesh-id', value)

class PolicyMap(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self,'policy-map')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setDescription(self, value):
        self.root.set_field_value('description', value)

    class ClassEntry(util.BaseObject):

        def __init__(self):
            util.BaseObject.__init__(self,'class-entry')

        def setClassName(self, value):
            self.root.set_field_value('class-name', value)

        def setShapeAverage(self, value):
            self.root.set_field_value('shape-average', value)

        def setBandwidthRemainingRatio(self, value):
            self.root.set_field_value('bandwidth-remaining-ratio', value)

        def setServicePolicy(self, value):
            self.root.set_field_value('service-policy', value)

        def setIsDscpTunnel(self, value):
            self.root.set_field_value('is-dscp-tunnel', value)

        def setDscpValue(self, value):
            self.root.set_field_value('dscp-value', value)

        def setBandwidthPercentage(self, value):
            self.root.set_field_value('bandwidth-percentage', value)

        def setBandwidthRemainingPercentage(self, value):
            self.root.set_field_value('bandwidth-remaining-percentage', value)

        def setPriorityValue(self, value):
            self.root.set_field_value('priority-value', value)

        def setPriorityPercentage(self, value):
            self.root.set_field_value('priority-percentage', value)

        def setRandomDetect(self, value):
            self.root.set_field_value('random-detect', value)

        def setPriorityLevel(self, value):
            self.root.set_field_value('priority-level', value)

class ClassMap(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self,'class-map')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setDescription(self, value):
        self.root.set_field_value('description', value)

    def setMatchType(self, value):
        self.root.set_field_value('match-type', value)

    class ClassMatchCondition(util.BaseObject):
        def __init__(self):
            util.BaseObject.__init__(self, 'class-match-condition')

        def setConditionType(self, value):
            self.root.set_field_value('condition-type', value)

        def setMatchValue(self, value):
            self.root.set_field_value('match-value', value)

class Domain(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self,'domain')

    def setRole(self, value):
        self.root.set_field_value('role', value)

    def setDomainName(self, value):
        self.root.set_field_value('domain-name', value)

    def setVrfName(self, value):
        self.root.set_field_value('vrf-name', value)

    def setTransitId(self, value):
        self.root.set_field_value('transit-id', value)

    def setSourceInterface(self, value):
        self.root.set_field_value('source-interface', value)

    def setSitePrefixList(self, value):
        self.root.set_field_value('site-prefix-list', value)

    def setLoadBalance(self, value):
        self.root.set_field_value('load-balance', value)

    def setEnterprisePrefixList(self, value):
        self.root.set_field_value('enterprise-prefix-list', value)

    def setHubIp(self, value):
        self.root.set_field_value('hub-ip', value)

    def setMasterIp(self, value):
        self.root.set_field_value('master-ip', value)

    def setPassword(self, value):
        self.root.set_field_value('password', value)