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

class RealServer(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'real-server')
    
    def setName(self, value):
        self.root.set_field_value('name', value)

    def setIpAddress(self, value):
        self.root.set_field_value('ip-address', value)

    def setConnectionLimit(self, value):
        self.root.set_field_value('connection-limit', value)

    def setState(self, value):
        self.root.set_field_value('state', value)

    def setDomainNumber(self, value):
        self.root.set_field_value('domain-number', value)

    def setPartition(self, value):
        self.root.set_field_value('partition', value)


class Pool(util.BaseObject):
    
    def __init__(self, name):
        util.BaseObject.__init__(self, name)
    
    def setName(self, value):
        self.root.set_field_value('name', value)

    def setPriorityGroupActivation(self, value):
        self.root.set_field_value('priority-group-activation', value)

    def setLoadBalancingMethod(self, value):
        self.root.set_field_value('load-balancing-method', value)

    def setDomainNumber(self, value):
        self.root.set_field_value('domain-number', value)

    def setPartition(self, value):
        self.root.set_field_value('partition', value)

    def setProtocol(self, value):
        self.root.set_field_value('protocol', value)            

    def setPoolMembers(self, value):
        self.root.set_field_value('pool-members', value)

    def setHealthMonitors(self, value):
        self.root.set_field_value('health-monitors', value) 

    class PoolMembers(util.BaseObject):
        
        def __init__(self):
            util.BaseObject.__init__(self, 'pool-members')

        def setPoolMember(self, value):
            self.root.set_field_value('pool-member', value)            

class HealthMonitor(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'health-monitor')
    
    def setName(self, value):
        self.root.set_field_value('name', value)

    def setWeight(self, value):
        self.root.set_field_value('weight', value)

    def setState(self, value):
        self.root.set_field_value('state', value)



class HealthMonitorInDevice(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'health-monitor')
    
    def setName(self, value):
        self.root.set_field_value('name', value)

    def setPartition(self, value):
        self.root.set_field_value('partition', value)

    def setType(self, value):
        self.root.set_field_value('type', value)

    def setHTTPRequest(self,value):
        self.root.set_field_value('http-request', value)

    def setResponseCode(self,value):
        self.root.set_field_value('response-codes', value)





class PoolMember(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'pool-member')
    
    def setRealServerIp(self, value):
        self.root.set_field_value('real-server-ip', value)

    def setServicePort(self, value):
        self.root.set_field_value('service-port', value)


class VirtualServer(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'virtual-server')
    
    def setName(self, value):
        self.root.set_field_value('name', value)

    def setVip(self, value):
        self.root.set_field_value('vip', value)

    def setPort(self, value):
        self.root.set_field_value('port', value)

    def setL4Protocol(self, value):
        self.root.set_field_value('l4-protocol', value)                

    def setState(self, value):
        self.root.set_field_value('state', value)

    def setPool(self, value):
        self.root.set_field_value('pool', value)

    def setDomainNumber(self, value):
        self.root.set_field_value('domain-number', value)

    def setLoadBalancingMethod(self, value):
        self.root.set_field_value('load-balancing-method', value)

    def setPartition(self, value):
        self.root.set_field_value('partition', value)

    def setPersistence(self, value):
        self.root.set_field_value('persistence', value)

    def setServerCertificate(self, value):
        self.root.set_field_value('server-certificate', value)

    def setProtection(self,value):
        self.root.set_field_value('protection', value)

    class ServerCertificate(util.BaseObject):
        
        def __init__(self):
            util.BaseObject.__init__(self, 'server-certificate')

        def setName(self, value):
            self.root.set_field_value('name', value)

        def setSni(self, value):
            self.root.set_field_value('sni', value)


    class Protection(util.BaseObject):
        
        def __init__(self):
            util.BaseObject.__init__(self, 'protection')

        def setRedirectionurl(self, value):
            self.root.set_field_value('redirect-url', value)

        def setBackupVirtualServer(self, value):
            self.root.set_field_value('backup-virtual-server', value)



class Persistence(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'persistence')

    def setType(self, value):
        self.root.set_field_value('type', value)
       
    def setTimeOut(self, value):
        self.root.set_field_value('time-out', value)

    def setCookieName(self, value):
        self.root.set_field_value('cookie-name', value)

    def setNetmask(self, value):
        self.root.set_field_value('netmask', value)                

    def setIpv6MaskLength(self, value):
        self.root.set_field_value('ipv6-mask-length', value)

    def setExpression(self, value):
        self.root.set_field_value('expression', value)

    def setResponseExpression(self, value):
        self.root.set_field_value('response-expression', value)


class Certificate(util.BaseObject):
    
    def __init__(self):
        util.BaseObject.__init__(self, 'certificate')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setFqdn(self, value):
        self.root.set_field_value('fqdn', value)

    def setCertData(self, value):
        self.root.set_field_value('cert-data', value)

    def setKeyData(self, value):
        self.root.set_field_value('key-data', value)

    def setPartition(self, value):
        self.root.set_field_value('partition', value)

class Peer(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'peer')

    def setIpAddress(self, value):
        self.root.set_field_value('ip-address', value)

    def setDeviceName(self, value):
        self.root.set_field_value('device-name', value)

    def setUsername(self, value):
        self.root.set_field_value('username', value)

    def setPassword(self, value):
        self.root.set_field_value('password', value)

class DeviceGroup(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'device-group')

    def setName(self, value):
        self.root.set_field_value('name', value)

    def setGroupType(self, value):
        self.root.set_field_value('group-type', value)

    def setIncludeSelf(self, value):
        self.root.set_field_value('include-self', value)

    def setNetworkFailover(self, value):
        self.root.set_field_value('network-failover', value)

    def setAutomaticSync(self, value):
        self.root.set_field_value('automatic-sync', value)

    def setFullSync(self, value):
        self.root.set_field_value('full-sync', value)

    def setMember(self, value):
        self.root.set_field_value('member', value)

    class Member(util.BaseObject):

        def __init__(self):
            util.BaseObject.__init__(self, 'member')

        def setDeviceName(self, value):
            self.root.set_field_value('device-name', value)


class ConfigSync(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'config-sync')

    def setLocalAddress(self, value):
        self.root.set_field_value('local-address', value)
        
class FailoverConfiguration(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'failover-configuration')

    def setAddress(self, value):
        self.root.set_field_value('address', value)

    def setPort(self, value):
        self.root.set_field_value('port', value)

class AddressRecord(util.BaseObject):

    def __init__(self):
        util.BaseObject.__init__(self, 'resource-record')

    def setFqdn(self, value):
        self.root.set_field_value('fqdn', value)

    def setAbsoluteName(self, value):
        self.root.set_field_value('absolute-name', value)

    def setType(self, value):
        self.root.set_field_value('type', value)

    def setRecordData(self, value):
        self.root.set_field_value('record-data', value)






