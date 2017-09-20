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

class Device():

    class Vlan(util.BaseObject):
        """ Vlan object presenting the vlan object.

        setNumber(n) is used to set the vlan number to n.
        setName(name) is used to set the vlan name to name
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'vlan')

        def setNumber(self, number):
            self.root.set_field_value('id', number)

        def setName(self, name):
            self.root.set_field_value('name', name)

        def setVlanNumber(self, number):
            # used for route domain only
            self.root.set_field_value('vlan-number', number)

        def setPartition(self, partition):
            self.root.set_field_value('partition', partition)


    class Logging(util.BaseObject):
        """ Logging object presenting the logging object.

        setContextName is used to set the ContextName.
        setIpAddress is used to set the IpAddress
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'logging')

        def setContextName(self, value):
            self.root.set_field_value('context-name', value)

        def setIpAddress(self, value):
            self.root.set_field_value('ip-address', value)

        def setFacilityName(self, value):
            self.root.set_field_value('facility-name', value)

        def setInterfaceName(self, value):
            self.root.set_field_value('interface-name', value)

        def setLoggingTrap(self, value):
            self.root.set_field_value('logging-trap', value)

        def setNoLoggingConsole(self, value):
            self.root.set_field_value('no-logging-console', value)



    class LoggingHost(util.BaseObject):
        """ Logging object presenting the logging object.

        setContextName is used to set the ContextName.
        setIpAddress is used to set the IpAddress
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'logging-hosts')

        def setIpAddress(self, value):
            self.root.set_field_value('ip-address', value)



    class VTY(util.BaseObject):
        """ Logging object presenting the logging object.

        setContextName is used to set the ContextName.
        setIpAddress is used to set the IpAddress
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'vty-config')

        def setName(self, value):
            self.root.set_field_value('name', value)

        def setAuthType(self, value):
            self.root.set_field_value('auth-type', value)

        def setMinVty(self, value):
            self.root.set_field_value('min-vty', value)

        def setMaxVty(self, value):
            self.root.set_field_value('max-vty', value)

        def setTimeOut(self, value):
            self.root.set_field_value('timeout', value)

        def setTransportTypesIn(self, value):
            self.root.set_field_value('transport-types-in', value)


    class AllowPings(util.BaseObject):
        """ AllowPings object presenting the  managementaccess-interface object.

        setEchoType is used to set the echo-type.
        setIpAddress is used to set the IpAddress
        setNetmask is used to set the netmask
        setInterfaceNameIf is used to set the interface-nameif
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'managementaccess-interface')

        def setEchoType(self, value):
            self.root.set_field_value('echo-type', value)

        def setIpAddress(self, value):
            self.root.set_field_value('ip-address', value)

        def setNetmask(self, value):
            self.root.set_field_value('netmask', value)

        def setInterfaceNameIf(self, value):
            self.root.set_field_value('interface-nameif', value)

        def setContextName(self, value):
            self.root.set_field_value('context-name', value)


    class Aaa(util.BaseObject):
        """ Aaa object presenting the tacacs-conf object.

        setTacacsHostIp is used to set the tacacs-host-ip.
        setTacacsKey is used to set the tacacs-key
        setTimeout is used to set the timeout
        setContextName is used to set the context-name
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'tacacs-conf')

        def setTacacsHostIp(self, value):
            self.root.set_field_value('tacacs-host-ip', value)

        def setTacacsKey(self, value):
            self.root.set_field_value('tacacs-key', value)

        def setTimeout(self, value):
            self.root.set_field_value('timeout', value)

        def setContextName(self, value):
            self.root.set_field_value('context-name', value)

    class Snmp(util.BaseObject):
        """ Snmp object presenting the snmp object.

        setContextName is used to set the ContextName.
        setLocation is used to set the location
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'snmp')

        def setContextName(self, value):
            self.root.set_field_value('context-name', value)

        def setCommAuthType(self, value):
            self.root.set_field_value('comm-auth-type', value)

        def setCommunity(self, value):
            self.root.set_field_value('community', value)

        def setLocation(self, value):
            self.root.set_field_value('location', value)

        def setContact(self, value):
            self.root.set_field_value('contact', value)

        def setVersion(self, value):
            self.root.set_field_value('snmp-version', value)

        def setTrapSource(self,value):
            self.root.set_field_value('trap-source', value)

        def setSnmpIfMib(self,value):
            self.root.set_field_value('snmp-ifmib-ifindex-persist', value)


    class SnmpServer(util.BaseObject):
        """ SnmpServer object presenting the snmp-server object.

        setContextName is used to set the context-name.
        setSnmpServerIp is used to set the snmp-server-ip
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'snmp-server')

        def setContextName(self, value):
            self.root.set_field_value('context-name', value)

        def setSnmpServerIp(self, value):
            self.root.set_field_value('snmp-server-ip', value)

        def setVersion(self, value):
            self.root.set_field_value('snmp-version', value)

        def setCommunity(self, value):
            self.root.set_field_value('community', value)

    class SnmpTraps(util.BaseObject):
        """ SnmpTraps object presenting the snmp-trap object.

        setContextName is used to set the context-name.
        setSnmpServerIp is used to set the snmp-server-ip
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'snmp-traps')

        def setTrap(self, value):
            self.root.set_field_value('snmp-trap', value)

    class SnmpCommunity(util.BaseObject):
        """ SnmpTraps object presenting the snmp-trap object.

        setContextName is used to set the context-name.
        setSnmpServerIp is used to set the snmp-server-ip
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'snmp-community-list')

        def setString(self, value):
            self.root.set_field_value('snmp-string', value)

        def setPermission(self, value):
            self.root.set_field_value('permission-type', value)

    class Clock(util.BaseObject):
        """ SnmpTraps object presenting the snmp-trap object.

        setContextName is used to set the context-name.
        setSnmpServerIp is used to set the snmp-server-ip
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'clock')

        def setTimeZone(self, value):
            self.root.set_field_value('timezone', value)

        def setSummerTime(self, value):
            self.root.set_field_value('summer-time', value)


    class Ssh(util.BaseObject):
        """ Ssh object presenting the ssh object.

        setContextName is used to set the context-name.
        setTimeout is used to set the timeout
        setVersion is used to set the version
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'ssh')

        def setContextName(self, value):
            self.root.set_field_value('context-name', value)

        def setTimeout(self, value):
            self.root.set_field_value('timeout', value)

        def setVersion(self, value):
            self.root.set_field_value('version', value)

        def setSourceInterface(self,value):
            self.root.set_field_value('source-interface',value)

        def setScpEnable(self,value):
            self.root.set_field_value('scp-enable',value)


    class SshNetwork(util.BaseObject):
        """ SshNetwork object presenting the network object.

        setContextName is used to set the context-name.
        setTimeout is used to set the timeout
        setVersion is used to set the version
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'network')

        def setContextName(self, value):
            self.root.set_field_value('context-name', value)

        def setIpAddress(self, value):
            self.root.set_field_value('ip-address', value)

        def setNetmask(self, value):
            self.root.set_field_value('netmask', value)

    class ClassMap(util.BaseObject):
        """ ClassMap object presenting the class-map object.

        setContextName is used to set the context-name.
        setName is used to set the name.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'class-map')

        def setContextName(self, value):
            self.root.set_field_value('context-name', value)

        def setName(self, value):
            self.root.set_field_value('name', value)

    class ClassMapMatchCondition(util.BaseObject):
        """ ClassMapMatchCondition object presenting the match-condition object.

        setContextName is used to set the context-name.
        setMatchValue is used to set the match-value.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'match-condition')

        def setContextName(self, value):
            self.root.set_field_value('context-name', value)

        def setMatchValue(self, value):
            self.root.set_field_value('match-value', value)

    class PolicyMap(util.BaseObject):
        """ PolicyMap object presenting the policy-map object.

        setContextName is used to set the context-name.
        setName is used to set the name.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'policy-map')

        def setContextName(self, value):
            self.root.set_field_value('context-name', value)

        def setName(self, value):
            self.root.set_field_value('name', value)


    class PolicyMapClass(util.BaseObject):
        """ PolicyMapClass object presenting the class object.

        setClassMapName is used to set the class.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'class')


        def setClassMapName(self, value):
            self.root.set_field_value('class-map-name', value)


    class Http(util.BaseObject):
        """ HttpClassInspect object presenting the  object.

        NoIpHttpServer Value is used to enable or disable http server.
        NoIpHttpSecureServer Value is used to enable or disable http secure server.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'http')

        def SetNoIpHttpServer(self, value):
            self.root.set_field_value('no-ip-http-server', value)
        def SetNoIpHttpSecureServer(self, value):
            self.root.set_field_value('no-ip-http-secure-server', value)
    
    class CallHome(util.BaseObject):
        """ HttpClassInspect object presenting the  object.

        NoIpHttpServer Value is used to enable or disable http server.
        NoIpHttpSecureServer Value is used to enable or disable http secure server.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'call-home')

        def SetProfile(self, value):
            self.root.set_field_value('profile', value)
        def SetDestination(self, value):
            self.root.set_field_value('destination', value)
        def SetNoDestination(self, value):
            self.root.set_field_value('no-destination', value)

    class Banner(util.BaseObject):
        """ HttpClassInspect object presenting the  object.

        NoIpHttpServer Value is used to enable or disable http server.
        NoIpHttpSecureServer Value is used to enable or disable http secure server.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'banner')

        def SetDelimiter(self, value):
            self.root.set_field_value('delimiter', value)
        def SetMotdMessage(self, value):
            self.root.set_field_value('motd-message', value)


    class Ntp(util.BaseObject):
        """ Ntp object presenting the  object.

        setInspectValue is used to set the inspect-type.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'ntp')

        def SetNtpServer(self, value):
            self.root.set_field_value('ntp-server', value)
        def SetNtpServerAddress(self, value):
            self.root.set_field_value('ntp-server-address', value)
        def SetNtpServer2Address(self, value):
            self.root.set_field_value('ntp-server2-address', value)
        def SetVrf(self, value):
            self.root.set_field_value('vrf', value)

    class Dns(util.BaseObject):
        """ DNS object presenting the  object.

        setInspectValue is used to set the inspect-type.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'dns')

        def SetlookUPSourceInterface(self, value):
            self.root.set_field_value('lookup-source-interface', value)
        def SetDomainName(self, value):
            self.root.set_field_value('domain-name', value)


    class DnsNameServer(util.BaseObject):
        """ DNS object presenting the  object.

        setInspectValue is used to set the inspect-type.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'nameserver')

        def SetNameServer(self, value):
            self.root.set_field_value('nameserver', value)
        def SetVrfName(self, value):
            self.root.set_field_value('vrf-name', value)

    class ServiceTimeStamps(util.BaseObject):
        """ DNS object presenting the  object.

        setInspectValue is used to set the inspect-type.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'service-time-stamps')

        def SetServiceTimeStampsDebug(self, value):
            self.root.set_field_value('service-timestamps-debug', value)
        def SetServiceTimeStampsLog(self, value):
            self.root.set_field_value('service-timestamps-log', value)
        def SetServicePasswordEncryption(self, value):
            self.root.set_field_value('service-password-encryption', value)


    class License(util.BaseObject):
        """ License object presenting the  object.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'license')

        def setSourceInterface(self, value):
            self.root.set_field_value('source-interface', value)
        def SetLicenseToken(self, value):
            self.root.set_field_value('license-token', value)

    class RouteMap(util.BaseObject):
        """ License object presenting the  object.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'route-map')

        def setName(self, value):
            self.root.set_field_value('name', value)

    class RouteMapEntries(util.BaseObject):
        """ License object presenting the  object.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'route-map-entries')

        def setSeq(self, value):
            self.root.set_field_value('seq', value)
        def setAction(self, value):
            self.root.set_field_value('action', value)


    class PolicyMapClassInspect(util.BaseObject):
        """ PolicyMapClassInspect object presenting the  object.

        setInspectValue is used to set the inspect-type.
        """

        def __init__(self):
            util.BaseObject.__init__(self, 'inspect-type')

        def setInspectValue(self, value):
            self.root.set_field_value('inspect-value', value)


    def __init__(self, xmlObj):
        self.deviceXmlObj = xmlObj
        if xmlObj == None:
            self.device = None
            self.url = None
        else:
            self.device = xmlObj.device
            self.url = '/app/restconf/data/controller:devices/device=%s' % (
                self.device.id)

    def toXml(self):
        """
        converts device object to xml object
        Args: None
        Returns: xml object
        """
        return self.deviceXmlObj.toXml()

    def isInterfaceInDeviceExists(self, intfname):
        interfaces = self.device.get_field_value('interfaces')
        if interfaces == None:
            return False
        intflist = interfaces.get_field_value('interface', True)
        util.log_debug('intflist = %s' % (intflist))
        for intf in intflist:
            name = intf.get_field_value('name')
            util.log_debug('interface_name = %s, looking for %s' % (name, intfname))
            if intfname == name:
                return True
        return False

    def isAccessListInDeviceExists(self, accesslistname):
        accesslists = self.device.get_field_value('access-lists')
        if accesslists == None:
            return False
        accesslist = accesslists.get_field_value('access-list', True)
        util.log_debug('accesslist = %s' % (accesslist))
        for al in util.convert_to_list(accesslist):
            name = al.get_field_value('name')
            util.log_debug('accesslist_name = %s, looking for %s' % (name, accesslistname))
            if accesslistname == name:
                return True
        return False

    def addHostName(self, hostName, session, addReferences = True):
        """
        add HostName
        Args: host name and session.
        Return: None
        """
        url = util.get_parent_rcpath(self.url)
        util.log_debug("url: ",url)
        util.log_debug("selfurl: ",self.url)
        device_id = self.device.id
        payload = '<device><id>'+device_id+'</id><name>'+hostName+'</name></device>'
        util.log_debug("payload hostname ",payload)
        yang.Sdk.createData(url, payload, session, addReferences)

    def addHa(self, ha, session, addReferences = True):
        """
        add tunnel for the given device
        Args: tunnel object, session
        Return: None
        """
        uri = self.url
        payload = ha.toXml()
        util.log_debug('addha: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addReferences)

    def addHardwareThroughput(self, throughput_value, session, addReferences = True):
        '''

        :param throughput_value: Throughput Value
        :param session: session object
        :param addReferences: True or False
        :return:
        '''
        url = util.get_parent_rcpath(self.url)
        util.log_debug("url: ",url)
        util.log_debug("selfurl: ",self.url)
        device_id = self.device.id
        payload = '<device><id>'+device_id+'</id><hardware-throughput>'+throughput_value+'</hardware-throughput></device>'
        util.log_debug("payload ihardware throughput ",payload)
        yang.Sdk.createData(url, payload, session, addReferences)

    def addVlan(self, vlan, session, addReferences = True):
        """
        add vlan
        Args: vlan object and session.
        Return: None
        """
        if not hasattr(self.device, 'vlans'):
            payload = '<vlans/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.add_field_value('vlans', [])
        uri = '%s/vlans' % (self.url)
        payload = vlan if isinstance(vlan, unicode) or isinstance(vlan, str) else vlan.toXml()
        return yang.Sdk.createData(uri, payload, session, addReferences)

    def addVlanGroup(self, vlangroup, session, addReferences = True):
        """
        add vlangroup
        Args: vlan-group object and session.
        Return: None
        """
        if not hasattr(self.device, 'vlan_groups'):
            payload = '<vlan-groups/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.add_field_value('vlan_groups', [])
        uri = '%s/vlan-groups' % (self.url)
        payload = vlangroup.toXml()
        return yang.Sdk.createData(uri, payload, session, addReferences)

    def addRoutePolicy(self, routepolicy, session, addReferences=True):
        """
        add route policy
        Args: route policy object, session
        Return: None
        """
        if not hasattr(self.device, 'route_policies'):
            payload = '<route-policies/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.add_field_value('route_policies', [])
        uri = '%s/route-policies' % (self.url)
        payload = routepolicy.toXml()
        if isinstance(self.device.route_policies, list):
            self.device.route_policies.append(routepolicy)
        util.log_debug('uri = %s\npayload = %s' % (uri, payload))
        return yang.Sdk.createData(uri, payload, session, addReferences)

    def addAcl(self, acl, session, addReference = True):
        """
        Add access control list
        Args: acl object, session
        Return: None
        """
        if not hasattr(self.device, 'access_lists'):
            payload = '<access-lists/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.add_field_value('access_lists', [])
        uri = '%s/access-lists' % (self.url)
        payload = acl.toXml()
        util.log_debug('uri = %s\npayload = %s' % (uri, payload))
        return yang.Sdk.createData(uri, payload, session, addReference)

    def addAclRule(self, listname, aclrule, session, task_id, addReference = True):
        """
        Add access control list rule
        Args: acl rule object, session
        Return: None
        """
        acl_list = self.url+'/access-lists/access-list=%s' % listname
        xml_output = yang.Sdk.getData(acl_list, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.access_list, 'acl_rules'):
            payload = '<acl-rules/>'
            yang.Sdk.createData(acl_list, payload, session, False)
            self.device.add_field_value('acl_rules', [])
        uri = '%s/acl-rules' % (acl_list)
        payload = aclrule.toXml()
        util.log_debug('uri = %s\npayload = %s' % (uri, payload))
        return yang.Sdk.createData(uri, payload, session, addReference)

    def getVirtualDeviceAccessList(self, devicename, accesslistname, task_id):
        vd_uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        xml_output = yang.Sdk.getData(vd_uri, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.virtual_device, 'access_lists'):
            return None
        accesslists = obj.virtual_device.get_field_value('access-lists')
        if accesslists == None:
            return None
        accesslist = accesslists.get_field_value('access-list', True)
        util.log_debug('accesslist = %s' % (accesslist))
        for al in util.convert_to_list(accesslist):
            name = al.get_field_value('name')
            util.log_debug('accesslist_name = %s, looking for %s' % (name, accesslistname))
            if accesslistname == name:
                return al
        return None

    def getHealthMonitorByName(self, hm_name):
        hms = self.device.get_field_value('health_monitors')
        if hms == None:
            return None
        hmlist = hms.get_field_value('health_monitor', True)
        for hm in hmlist:
            name = hm.get_field_value('name')
            util.log_debug('hm_name = %s, looking for %s' % (name, hm_name))
            if hm_name == name:
                return hm
        return None

    def getCertificateByNamePartition(self, name, partition):
        certificates = self.device.get_field_value('certificates')
        if certificates == None:
            return None
        cert_list = certificates.get_field_value('certificate', True)
        for cert in cert_list:
            cert_name = cert.get_field_value('name')
            util.log_debug('cert_name = %s, looking for %s' % (cert_name, name))
            cert_partition = cert.get_field_value('partition')
            util.log_debug('cert_partition = %s, looking for %s' % (cert_partition, partition)            )
            if cert_name == name and cert_partition == partition:
                return cert
        return None

    def getCertificateByFqdnPartition(self, fqdn, partition):
        certificates = self.device.get_field_value('certificates')
        if certificates == None:
            return None
        cert_list = certificates.get_field_value('certificate', True)
        for cert in cert_list:
            cert_fqdn = cert.get_field_value('fqdn')
            util.log_debug('cert_fqdn = %s, looking for %s' % (cert_fqdn, fqdn))
            cert_partition = cert.get_field_value('partition')
            util.log_debug('cert_partition = %s, looking for %s' % (cert_partition, partition)            )
            if cert_fqdn == fqdn and cert_partition == partition:
                return cert
        return None        

    def getVirtualDeviceZone(self, devicename, zone_name, task_id):
        vd_uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        xml_output = yang.Sdk.getData(vd_uri, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.virtual_device, 'zones'):
            return None
        zones = obj.virtual_device.get_field_value('zones')
        if zones == None:
            return None
        zone = zones.get_field_value('zone', True)
        util.log_debug('zone = %s' % (zone))
        for al in util.convert_to_list(zone):
            name = al.get_field_value('name')
            util.log_debug('zone_name = %s, looking for %s' % (name, zone_name))
            if zone_name == name:
                return al
        return None

    def addVirtualDeviceInterface(self, devicename, interface, session, task_id, addReference = True):
        """
        Add Interface for virtual device (firewall)
        Args: interface object, session
        Return: None
        """
        vd_uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        xml_output = yang.Sdk.getData(vd_uri, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.virtual_device, 'interfaces'):
            payload = '<interfaces/>'
            yang.Sdk.createData(vd_uri, payload, session, False)
            self.device.add_field_value('interfaces', [])
        uri = '%s/interfaces' % (vd_uri)
        payload = interface.toXml()
        util.log_debug('uri = %s\npayload = %s' % (uri, payload))
        return yang.Sdk.createData(uri, payload, session, addReference)

    def addVirtualDeviceAcl(self, devicename, acl, session, task_id, addReference = True):
        """
        Add access control list for virtual device (firewall)
        Args: acl object, session
        Return: None
        """
        vd_uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        xml_output = yang.Sdk.getData(vd_uri, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.virtual_device, 'access_lists'):
            payload = '<access-lists/>'
            yang.Sdk.createData(vd_uri, payload, session, False)
            self.device.add_field_value('access_lists', [])
        uri = '%s/access-lists' % (vd_uri)
        payload = acl.toXml()
        util.log_debug('uri = %s\npayload = %s' % (uri, payload))
        return yang.Sdk.createData(uri, payload, session, addReference)

    def addVirtualDeviceAclRule(self, devicename, listname, aclrule, session, task_id, addReference = True):
        """
        Add access control list rule for virtual device (firewall)
        Args: acl rule object, session
        Return: None
        """
        vd_uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        acl_list = vd_uri +'/access-lists/access-list=%s' % listname
        xml_output = yang.Sdk.getData(acl_list, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.access_list, 'acl_rules'):
            payload = '<acl-rules/>'
            yang.Sdk.createData(acl_list, payload, session, False)
            self.device.add_field_value('acl_rules', [])
        uri = '%s/acl-rules' % (acl_list)
        payload = aclrule.toXml()
        util.log_debug('uri = %s\npayload = %s' % (uri, payload))
        return yang.Sdk.createData(uri, payload, session, addReference)

    def addVpls(self, vpls, session, addReference = True):
        """
        Add vpls
        Args: vpls object, session
        Return: None
        """
        if not hasattr(self.device, 'vpls_list'):
            payload = '<vpls-list/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.add_field_value('vpls_list', [])
        uri = '%s/vpls-list' % (self.url)
        payload = vpls.toXml()
        util.log_debug('uri = %s\npayload = %s' % (uri, payload))
        return yang.Sdk.createData(uri, payload, session, addReference)

    def addPrefixSet(self, obj, session, addReference = True):
        container = self.device.get_field_value('prefix_sets')
        if(container == None):
            yang.Sdk.createData(self.url, '<prefix-sets/>', session, False)
            self.device.set_field_value('prefix_sets', [])
        yang.Sdk.createData('%s/prefix-sets' % (self.url), obj.toXml(), session, addReference)

    def addInterfacesContainer(self, session, add_ref = False):
        interfaces = self.device.get_field_value('interfaces')
        if(interfaces == None):
            payload = '<interfaces/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('interfaces', [])

    def addPfrClassesContainer(self, session, add_ref = False):
        pfr_classes = self.device.get_field_value('pfr-classes')
        if(pfr_classes == None):
            payload = '<pfr-classes/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('pfr-classes', [])

    def addPrefixEntry(self,session,prefix_name,prefix_entity_object,ref=True):
        uri = self.url + '/ip-prefixlist-list/ip-prefixlist='+prefix_name+'/ip-prefixlist-entries'
        payload = prefix_entity_object.toXml()
        util.log_debug('addPrefixEntry: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, ref)

    def addInterface(self, intf, session, addreference=True):
        """
        add interface for the given device
        Args: interface object, session
        Return: None
        """
        self.addInterfacesContainer(session)
        uri = self.url + '/interfaces'
        payload = intf if isinstance(intf, unicode) or isinstance(intf, str) else intf.toXml()
        util.log_debug('addInterface: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addLbDomainsContainer(self, session, add_ref = False):
        lbdomains = self.device.get_field_value('lb_domains')
        if(lbdomains == None):
            payload = '<lb-domains/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('lb_domains', [])

    def addLbDomain(self, lb_domain, session, addreference=True):
        """
        add lb_domain for the given device
        Args: lb_domain object, session
        Return: None
        """
        self.addLbDomainsContainer(session)
        uri = self.url + '/lb-domains'
        payload = lb_domain.toXml()
        util.log_debug('addLbDomain: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addLBTrafficGroupsContainer(self, session, add_ref = False):
        selfips = self.device.get_field_value('traffic-groups')
        if(selfips == None):
            payload = '<traffic-groups/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('traffic-groups', [])

    def addLBTrafficGroup(self, traffic_group, session, addreference=True):
        """
        add self_ip for the given device
        Args: traffic_group object, session
        Return: None
        """
        self.addLBTrafficGroupsContainer(session)
        uri = self.url + '/traffic-groups'
        payload = traffic_group.toXml()
        util.log_debug('addLBTrafficGroup: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addSelfIpsContainer(self, session, add_ref = False):
        selfips = self.device.get_field_value('self_ips')
        if(selfips == None):
            payload = '<self-ips/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('self_ips', [])

    def addSelfIp(self, self_ip, session, addreference=True):
        """
        add self_ip for the given device
        Args: self_ip object, session
        Return: None
        """
        self.addSelfIpsContainer(session)
        uri = self.url + '/self-ips'
        payload = self_ip.toXml()
        util.log_debug('addSelfIp: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addPeersContainer(self, session, add_ref = False):
        peers = self.device.get_field_value('peers')
        if(peers == None):
            payload = '<peers/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('peers', [])

    def addPeer(self, peer, session, addreference=True):
        """
        add peer for the given device
        Args: peer object, session
        Return: None
        """
        self.addPeersContainer(session)
        uri = self.url + '/peers'
        payload = peer.toXml()
        util.log_debug('addPeer: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addHaSelfIpContainer(self, session, add_ref = False):
        peers = self.device.get_field_value('ha-self-ips')
        if(peers == None):
            payload = '<ha-self-ips/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('ha-self-ips', [])

    def addHaSelfIp(self, peer, session, addreference=True):
        """
        add ha-self-ip for the given device
        Args: ha-self-ip object, session
        Return: None
        """
        self.addHaSelfIpContainer(session)
        uri = self.url + '/ha-self-ips'
        payload = peer.toXml()
        util.log_debug('addHaSelfIp: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addFloatingSelfIpContainer(self, session, add_ref = False):
        peers = self.device.get_field_value('floating-self-ips')
        if(peers == None):
            payload = '<floating-self-ips/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('floating-self-ips', [])

    def addFloatingSelfIp(self, peer, session, addreference=True):
        """
        add ha-self-ip for the given device
        Args: ha-self-ip object, session
        Return: None
        """
        self.addFloatingSelfIpContainer(session)
        uri = self.url + '/floating-self-ips'
        payload = peer.toXml()
        util.log_debug('addHaSelfIp: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addDeviceGroupsContainer(self, session, add_ref = False):
        peers = self.device.get_field_value('device-groups')
        if(peers == None):
            payload = '<device-groups/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('device-groups', [])

    def addDeviceGroup(self, devicegroup, session, addreference=True):
        """
        add devicegroup for the given device
        Args: devicegroup object, session
        Return: None
        """
        self.addDeviceGroupsContainer(session)
        uri = self.url + '/device-groups'
        payload = devicegroup.toXml()
        util.log_debug('addDeviceGroup: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addConfigSync(self, configsync, session, addreference=True):
        '''

        :param configsync: 
        :param session: 
        :param addreference: 
        :return:
        '''
        uri = self.url
        payload = configsync.toXml()
        util.log_debug('addConfigSync: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addFailOverConfig(self, failoverconfig, session, addreference=True):
        '''

        :param failoverconfig:
        :param session:
        :param addreference:
        :return:
        '''
        uri = self.url
        payload = failoverconfig.toXml()
        util.log_debug('addFailOverConfig: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def deleteSelfIp(self, self_ip, self_ip_name, partition, task_id, session):
        """
        :param self_ip: self_ip payload for non-floating ip
        :param session: session object
        :param task_id: task id 
        :return:
        """
        
        uri = self.url + '/self-ips/self-ip=%s,%s' % (self_ip_name, partition)
        payload = self_ip.toXml()
        util.log_debug('addSelfIp: %s, payload = %s' % (uri, payload))
        yang.Sdk.deleteData(uri, payload, task_id, session)

    def addLbDomainVlan(self, lbdomain, vlan, session, task_id, addReference = True):
        """
        Add vlan for lb domain (loadbalancer)
        Args: vlan object, session
        Return: None
        """
        rd_uri = "%s/lb-domains/lb-domain=%s" % (self.url, lbdomain)
        xml_output = yang.Sdk.getData(rd_uri, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.lb_domain, 'vlans'):
            payload = '<vlans/>'
            yang.Sdk.createData(rd_uri, payload, session, False)
            self.device.add_field_value('vlans', [])
        uri = '%s/vlans' % (rd_uri)
        payload = vlan.toXml()
        util.log_debug('uri = %s\npayload = %s' % (uri, payload))
        return yang.Sdk.createData(uri, payload, session, addReference)

    def addAllowedVlanInInterface(self, intf_name, vlanobj, session, task_id, addReference = True):
        """
        Add allowed valn to given interface
        Args: vlanobj, session, taskid
        Return: None
        """
        intf = self.url+'/interfaces/interface=%s' % util.make_interfacename(intf_name)
        xml_output = yang.Sdk.getData(intf, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.interface, 'allowed_vlans'):
            payload = '<allowed-vlans/>'
            yang.Sdk.createData(intf, payload, session, False)
            self.device.add_field_value('allowed_vlans', [])
        uri = '%s/allowed-vlans' % (intf)
        payload = vlanobj.toXml()
        util.log_debug('uri = %s\npayload = %s' % (uri, payload))
        return yang.Sdk.createData(uri, payload, session, addReference)

    def addStaticRoutesContainer(self, session, add_ref = False):
        staticroutes = self.device.get_field_value('static_routes')
        if(staticroutes == None):
            payload = '<static-routes/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('static_routes', [])

    def addStaticRoute(self, staticroute, session, add_ref = True):
        """
        add staticroute for the given device
        Args: staticroute object, session
        Return: None
        """
        self.addStaticRoutesContainer(session)
        uri = self.url + '/static-routes'
        payload = staticroute.toXml()
        util.log_debug('addStaticRoute: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addLbRoutesContainer(self, session, add_ref = False):
        lbroutes = self.device.get_field_value('lb_routes')
        if(lbroutes == None):
            payload = '<lb-routes/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('lb_routes', [])

    def addLbRoute(self, lbroute, session, add_ref = True):
        """
        add lbroute for the given device
        Args: lbroute object, session
        Return: None
        """
        self.addLbRoutesContainer(session, add_ref)
        uri = self.url + '/lb-routes'
        payload = lbroute.toXml()
        util.log_debug('addlbRoute: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addSNMP(self, snmpobject, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = snmpobject.toXml()
        util.log_debug('addSNMP: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)

    def addNTPContainer(self,session,ref=False):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = "<ntp-servers/>"
        util.log_debug('addNTPContainers: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)

        

    def addSnmpCommunity(self, snmpobject, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = snmpobject.toXml()
        community_uri = self.url + '/snmp'
        util.log_debug('addSnmpCommunity: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(community_uri, payload, session,ref)

    def addSnmpTraps(self, snmpobject, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = snmpobject.toXml()
        trap_uri = self.url + '/snmp'
        util.log_debug('addSnmpTraps: %s, payload = %s' % (trap_uri, payload))
        yang.Sdk.createData(trap_uri, payload, session,ref)

    def addSNMPServer(self, snmpserverobj, session,ref=True):
        """
        add addSNMPServer for the given device
        Args: snmpserverobj object, session
        Return: None
        """
        uri = self.url + '/snmp'
        payload = snmpserverobj.toXml()
        util.log_debug('addSNMPServer: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session,ref)

    def addHTTP(self, httpobject, session,ref=True):
        """
        add addHTTP for the given device
        Args: Httpobject object, session
        Return: None
        """
        payload = httpobject.toXml()
        util.log_debug('addHTTP: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)

    def addNtp(self, ntpobject, session,ref=True):
        """
        add addHTTP for the given device
        Args: Httpobject object, session
        Return: None
        """
        payload = ntpobject.toXml()
        util.log_debug('addNtp: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)

    def addClock(self, clock_object, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = clock_object.toXml()
        util.log_debug('addClock: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)


    def addDNS(self, dnsobject, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = dnsobject.toXml()
        util.log_debug('addDNS: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)


    def addDNSNameServer(self, name_server_object, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = name_server_object.toXml()
        dns_name_server_url = self.url + '/dns'
        util.log_debug('addSNMP: %s, payload = %s' % (dns_name_server_url, payload))
        yang.Sdk.createData(dns_name_server_url, payload, session,ref)


    def addLogging(self, logging_object, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = logging_object.toXml()
        util.log_debug('addLogging: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)

    def addLoggingHost(self, logging_host_object, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """

        payload = logging_host_object.toXml()
        logging_host_url = self.url + '/logging'
        util.log_debug('addLogginghost: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(logging_host_url, payload, session,ref)

    def addCallHome(self, callhomeobject, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = callhomeobject.toXml()
        util.log_debug('addcallhome: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)

    def addBanner(self, bannerobject, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = bannerobject.toXml()
        util.log_debug('addBanner: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)

    def addServiceTimeStamps(self, timestamp_object, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = timestamp_object.toXml()
        util.log_debug('addTimestamps: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)

    def addVTY(self, vtyobject, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = vtyobject.toXml()
        vty_uri = self.url+'/vty-configs'
        util.log_debug('addVTY: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(vty_uri, payload, session,ref)

    def addVTYContainer(self, session,ref=False):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = "<vty-configs/>"
        util.log_debug('addVTY: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)


    def addLicense(self, license_object, session,ref=True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = license_object.toXml()
        util.log_debug('addLicenseObject: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)

    def addVirtualDeviceSNMPServer(self, devicename, snmpserverobj, session, add_ref = True):
        """
        add addSNMPServer for the given device
        Args: snmpserverobj object, session
        Return: None
        """
        uri = "%s/virtual-devices/virtual-device=%s/snmp" % (self.url, devicename)
        payload = snmpserverobj.toXml()
        util.log_debug('addSNMPServer: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addSSH(self, sshobject, session,ref=True):
        """
        add addSSH for the given device
        Args: sshobject object, session
        Return: None
        """
        payload = sshobject.toXml()
        util.log_debug('addSSH: %s, payload = %s' % (self.url, payload))
        yang.Sdk.createData(self.url, payload, session,ref)

    def addSSHNetwork(self, sshnetworkobj, session, add_ref = True):
        """
        add addSSHNetwork for the given device
        Args: sshnetworkobj object, session
        Return: None
        """
        uri = self.url + '/ssh'
        payload = sshnetworkobj.toXml()
        util.log_debug('addSSHNetwork: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addQosPolicyMapsContainer(self, session, add_ref = False):
        tipolicymaps = self.device.get_field_value('policy_maps')
        if(tipolicymaps == None):
            payload = '<policy-maps/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('policy-maps', [])

    def addQOSClassMapsContainer(self, session, add_ref = False):
        tipolicymaps = self.device.get_field_value('class_maps')
        if(tipolicymaps == None):
            payload = '<class-maps/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('class-maps', [])

    def addClassMapsContainer(self, session, add_ref = False):
        ticlassmaps = self.device.get_field_value('ti_class_maps')
        if(ticlassmaps == None):
            payload = '<ti-class-maps/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('ti-class-maps', [])

    def addTiClassMap(self, classmap, session, add_ref = True):
        """
        add TiClassMap for the given device
        Args: classmap object, session
        Return: None
        """
        self.addClassMapsContainer(session)
        uri = self.url + '/ti-class-maps'
        payload = classmap.toXml()
        util.log_debug('addTiClassMap: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addTiClassMapMatchCondition(self, classmapmatchcond, class_map_name, session, add_ref = True):
        """
        add addTiClassMapMatchCondition for the given device
        Args: classmapmatchcond object, session
        Return: None
        """
        uri = self.url + '/ti-class-maps/class-map=%s' % (class_map_name)
        payload = classmapmatchcond.toXml()
        util.log_debug('addTiClassMapMatchCondition: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addPolicyMapsContainer(self, session, add_ref = False):
        tipolicymaps = self.device.get_field_value('ti_policy_maps')
        if(tipolicymaps == None):
            payload = '<ti-policy-maps/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('ti-policy-maps', [])

    def addTiPolicyMap(self, policymap, session, add_ref = True):
        """
        add TiPolicyMap for the given device
        Args: policymap object, session
        Return: None
        """
        self.addPolicyMapsContainer(session, add_ref)
        uri = self.url + '/ti-policy-maps'
        payload = policymap.toXml()
        util.log_debug('addTiPolicyMap: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addTiPolicyMapClass(self, policymapclass, policy_map_name, session, add_ref = True):
        """
        add addTiPolicyMapClass for the given device
        Args: policymapclass object, session
        Return: None
        """
        uri = self.url + '/ti-policy-maps/policy-map=%s' % (policy_map_name)
        payload = policymapclass.toXml()
        util.log_debug('addTiPolicyMapClass: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addTiPolicyMapClassInspect(self, policymapclassinspect, policy_map_name, class_map_name, session, add_ref = True):
        """
        add addTiPolicyMapClassInspect for the given device
        Args: policymapclassinspect object, session
        Return: None
        """
        uri = self.url + '/ti-policy-maps/policy-map=%s/class=%s' % (policy_map_name, class_map_name)
        payload = policymapclassinspect.toXml()
        util.log_debug('addTiPolicyMapClassInspect: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addContainer(self, session, field, xml_tag, addReference=False):
        val = self.device.get_field_value(field)
        if val == None:
            payload = '<%s/>' % (xml_tag)
            yang.Sdk.createData(self.url, payload, session, addReference)
            self.device.set_field_value(field, [])

    def getOrCreateContainer(self, session, field, xml_tag, addReference=False):
        self.addContainer(session, field, xml_tag, addReference)
        return self.device.get_field_value(field)

    def addRouteMapsContainer(self, session,ref=False):
        routemaps = self.device.get_field_value('route_maps')
        if(routemaps == None):
            payload = '<route-maps/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('route_maps', [],ref)

    def addRouteMap(self, routemap, session,ref=True):
        """
        add routemap for the given device
        Args: routemap object, session
        Return: None
        """
        self.addRouteMapsContainer(session, ref)
        uri = self.url + '/route-maps'
        payload = routemap.toXml()
        util.log_debug('addRouteMap: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session,ref)

    def addRouteMapEntity(self,entity_object,mapname,session,ref=True):
        entity_url = self.url+'/route-maps/route-map='+mapname
        payload = entity_object.toXml()
        util.log_debug('addRouteMapEntity: %s, payload = %s' % (entity_url, payload))
        yang.Sdk.createData(entity_url, payload, session,ref)


    def addRouteMapMatchCondition(self, routemapmatch, session,map_name,seq_num,ref=True):
        """
        add routemap Match for the given device
        Args: routemap object, session
        Return: None
        """
        self.addRouteMapsContainer(session)
        uri = self.url + '/route-maps/route-map='+map_name+'/route-map-entries='+str(seq_num)
        payload = routemapmatch.toXml()
        util.log_debug('addRouteMapMatch: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session,ref)


    def addRouteMapSetAction(self, routemapa_action_object, session,map_name,seq_num,ref=True):
        """
        add routemap Match for the given device
        Args: routemap object, session
        Return: None
        """
        self.addRouteMapsContainer(session)
        uri = self.url + '/route-maps/route-map='+map_name+'/route-map-entries='+str(seq_num)
        payload = routemapa_action_object.toXml()
        util.log_debug('addRouteMapMatch: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session,ref)


    def addVrf(self, vrf, session, addReference=True):
        """
        add vrf
        Args: vrf object, session
        Return: None
        """
        vrfs = self.getOrCreateContainer(session, 'vrfs', 'vrfs')
        if not isinstance(vrfs, list) and util.isEmpty(vrfs.get_field_value('vrf')):
            vrfs.set_field_value('vrf', [])
        payload = vrf if isinstance(vrf, unicode) or isinstance(vrf, str) else vrf.toXml()
        url = '%s/vrfs' % (self.url)
        yang.Sdk.createData(url, payload, session, addReference)
        # vrfs.vrf.append(vrf)

    def getVrf(self, name):
        for vrf in self.device.get_field_value('vrf', True):
            if vrf.name == name:
                return vrf
        return None

    def getInterfaceByPort(self, port):
        interfaces = self.device.get_field_value('interfaces')
        if interfaces is None:
            return None
        for intf in interfaces.get_field_value('interface'):
            if intf.get_field_value('port') == port:
                return intf
        return None

    def getInterfaceByName(self, name):
        interfaces = self.device.get_field_value('interfaces')
        if interfaces is None:
            return None
        for intf in interfaces.get_field_value('interface'):
            if intf.get_field_value('name') == name:
                return intf
        return None

    def addDmvpnTunnelContainer(self, session, add_ref = False):
        dmvpntunnels = self.device.get_field_value('dmvpntunnels')
        if(dmvpntunnels == None):
            payload = '<dmvpntunnels/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('dmvpntunnels', [])

    def addDmvpnTunnel(self, intf, session, add_ref = True):
        """
        add tunnel for the given device
        Args: tunnel object, session
        Return: None
        """
        self.addDmvpnTunnelContainer(session)
        uri = self.url + '/dmvpntunnels'
        payload = intf.toXml()
        util.log_debug('addTunnel: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addIpPrefixListListsContainer(self, session, add_ref = False):
        ipprefixlistlists = self.device.get_field_value('ip_prefixlist_list')
        if(ipprefixlistlists == None):
            payload = '<ip-prefixlist-list/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('ip_prefixlist_list', [])

    def addPrefixSetsContainer(self, session, add_ref = False):
        prefixsets = self.device.get_field_value('prefix_sets')
        if(prefixsets == None):
            payload = '<prefix-sets/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('prefix_sets', [])

    def addMatchConditionsContainer(self,prefix_set_name,session,add_ref = False):

        uri = self.url + '/prefix-sets/prefix-set=%s' % (prefix_set_name)
        payload = '<match-conditions/>'
        yang.Sdk.createData(uri, payload, session, False)			
            
    def isInterfaceInDeviceExists(self, intfname):
        interfaces = self.device.get_field_value('interfaces')
        if interfaces == None:
            return False
        intflist = interfaces.get_field_value('interface', True)
        util.log_debug('intflist = %s' % (intflist))
        for intf in intflist:
            name = intf.get_field_value('name')
            util.log_debug('interface_name = %s, looking for %s' % (name, intfname))
            if intfname == name:
                return True
        return False

    def isVrfinDeviceExist(self, vrfname):
        vrfs = self.device.get_field_value('vrfs')
        if vrfs == None:
            return False
        vrflist = vrfs.get_field_value('vrf', True)
        util.log_debug('vrflist = %s' % (vrflist))
        for vrf in vrflist:
            name = vrf.get_field_value('name')
            util.log_debug('vrf_name = %s, looking for %s' % (name, vrfname))
            if vrfname == name:
                return True
        return False

    def isVlanIdInDeviceExist(self, vlanid):
        vlans = self.device.get_field_value('vlans')
        if vlans == None:
            return False
        vlanlist = vlans.get_field_value('vlan', True)
        util.log_debug('vlanlist = %s' % (vlanlist))
        for vlan in vlanlist:
            id = vlan.get_field_value('id')
            util.log_debug('vlan_id = %s, looking for %s' % (id, vlanid))
            if int(vlanid) == int(id):
                return True
        return False

    def isPortInDeviceExists(self, port):
        interfaces = self.device.get_field_value('interfaces')
        if interfaces == None:
            return False
        intflist = interfaces.get_field_value('interface', True)
        util.log_debug('intflist = %s' % (intflist))
        for intf in intflist:
            value = intf.get_field_value('port')
            util.log_debug('interface_port = %s, looking for %s' % (value, port))
            if value == port:
                return True
        return False

    def isVlanIdRangeInDeviceExist(self, begin, end):
        vlans = self.device.get_field_value('vlans')
        if vlans == None:
            return False
        vlanlist = vlans.get_field_value('vlan', True)
        util.log_debug('vlanlist is = %s' % (vlanlist))
        devicevlans = []
        for vlan in vlanlist:
            util.log_debug('')
            devicevlans.append(int(vlan.get_field_value('id', False)))
        util.log_debug('device vlans are %s' % (devicevlans))
        vlans = range(int(begin), int(end))
        util.log_debug('vlan range to check is %s' % (vlans))
        for vlan in vlans:
            if vlan not in devicevlans:
                return False
        return True

    def addIpPrefixList(self, ipprefixlist, session,ref=True):
        """
        add ipprefixlist for the given device
        Args: ipprefixlist object, session
        Return: None
        """
        self.addIpPrefixListListsContainer(session)
        uri = self.url + '/ip-prefixlist-list'
        payload = ipprefixlist.toXml()
        util.log_debug('addIpPrefixList: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session,ref)

    def addIpPrefixListEntriesContainer(self,prefix_name,session,ref=False):
        uri = self.url + '/ip-prefixlist-list/ip-prefixlist=' + prefix_name
        payload = "<ip-prefixlist-entries/>"
        util.log_debug('addIpPrefixListEntries: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session,ref)

    def addVirtualDevicesContainer(self, session, add_ref=False):
        virtualdevices = self.device.get_field_value('virtual_devices')
        if(virtualdevices == None):
            payload = '<virtual-devices/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('virtual-devices', [])


    def addVirtualDevice(self, virtualdevice, session, addreference=True):
        """
        add VirtualDevice for the given device
        Args: virtualdevice object, session
        Return: None
        """
        self.addVirtualDevicesContainer(session)
        uri = self.url + '/virtual-devices'
        payload = virtualdevice.toXml()
        util.log_debug('addVirtualDevice: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)



    def addObjectGroupsContainer(self, session, add_ref = False):
        objectgroups = self.device.get_field_value('object_groups')
        if(objectgroups == None):
            payload = '<object-groups/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('object-groups', [])

    def addObjectGroup(self, objectgroup, session, addreference=True):
        """
        add objectgroup for the given device
        Args: objectgroup object, session
        Return: None
        """
        self.addObjectGroupsContainer(session)
        uri = self.url + '/object-groups'
        payload = objectgroup.toXml()
        util.log_debug('addObjectGroup: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addNetworkObjectsContainer(self, session, add_ref = False):
        networkobjects = self.device.get_field_value('network_objects')
        if(networkobjects == None):
            payload = '<network-objects/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('network_objects', [])

    def addNetworkObject(self, networkobject, session, addreference=True):
        """
        add network-object for the given device
        Args: network-object object, session
        Return: None
        """
        self.addNetworkObjectsContainer(session)
        uri = self.url + '/network-objects'
        payload = networkobject.toXml()
        util.log_debug('addNetworkObject: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addVirtualDeviceNatObjectGroupsContainer(self, devicename, session, task_id, add_ref = False):
        vd_uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        xml_output = yang.Sdk.getData(vd_uri, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.virtual_device, 'nat_object_groups'):
            payload = '<nat-object-groups/>'
            yang.Sdk.createData(vd_uri, payload, session, False)
            self.device.set_field_value('nat_object_groups', [])

    def addVirtualDeviceNatObjectGroup(self, devicename, natobjectgroup, session, task_id, addreference=True):
        """
        add nat-object-group for the given virtual device
        Args: nat-object-group object, session
        Return: None
        """
        self.addVirtualDeviceNatObjectGroupsContainer(devicename, session, task_id)
        uri = "%s/virtual-devices/virtual-device=%s/nat-object-groups" % (self.url, devicename)
        payload = natobjectgroup.toXml()
        util.log_debug('addVirtualDeviceNatObjectGroup: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addInterfaceAccessListsContainer(self, session, add_ref = False):
        interfaceaccesslists = self.device.get_field_value('interface_access_lists')
        if(interfaceaccesslists == None):
            payload = '<interface-access-lists/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('interface_access_lists', [])

    def addInterfaceAccessList(self, interfaceaccesslist, session, addreference=True):
        """
        add interface-access-list for the given device
        Args: interface-access-list object, session
        Return: None
        """
        self.addInterfaceAccessListsContainer(session)
        uri = self.url + '/interface-access-lists'
        payload = interfaceaccesslist.toXml()
        util.log_debug('addInterfaceAccessList: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addFailoverGroupsContainer(self, session, add_ref = False):
        failovergroups = self.device.get_field_value('failover_groups')
        if(failovergroups == None):
            payload = '<failover-groups/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('failover-groups', [])

    def addFailoverGroup(self, failovergroup, session, addreference=True):
        """
        add failover-group for the given device
        Args: failover-group object, session
        Return: None
        """
        self.addFailoverGroupsContainer(session)
        uri = self.url + '/failover-groups'
        payload = failovergroup.toXml()
        util.log_debug('addNetworkObject: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addVirtualDeviceSNMP(self, devicename,  snmpobject, session, add_ref = True):
        """
        add addSNMP for the given device
        Args: snmpobject object, session
        Return: None
        """
        payload = snmpobject.toXml()
        url = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        util.log_debug('addSNMP: %s, payload = %s' % (url, payload))
        yang.Sdk.createData(url, payload, session, add_ref)

    def addVirtualDeviceSSH(self,  devicename, sshobject, session, add_ref = True):
        """
        add addSSH for the given device
        Args: sshobject object, session
        Return: None
        """
        payload = sshobject.toXml()
        url = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        util.log_debug('addSSH: %s, payload = %s' % (url, payload))
        yang.Sdk.createData(url, payload, session, add_ref)

    def addVirtualDeviceSSHNetwork(self, devicename, sshnetworkobj, session, add_ref = True):
        """
        add addVirtualDeviceSSHNetwork for the given device
        Args: sshnetworkobj object, session
        Return: None
        """
        uri = "%s/virtual-devices/virtual-device=%s/ssh" % (self.url, devicename)
        payload = sshnetworkobj.toXml()
        util.log_debug('addVirtualDeviceSSHNetwork: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addVirtualDeviceTiClassMapsContainer(self, devicename, session, task_id, add_ref = False):
        vd_uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        xml_output = yang.Sdk.getData(vd_uri, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.virtual_device, 'ti_class_maps'):
            payload = '<ti-class-maps/>'
            yang.Sdk.createData(vd_uri, payload, session, False)
            self.device.add_field_value('ti_class_maps', [])

    def addVirtualDeviceTiClassMap(self, devicename, ticlassmap, session, task_id, add_ref = True):
        """
        add addVirtualDeviceTiClassMap for the given device
        Args: ticlassmap object, session
        Return: None
        """
        self.addVirtualDeviceTiClassMapsContainer(devicename, session, task_id)
        uri = "%s/virtual-devices/virtual-device=%s/ti-class-maps" % (self.url, devicename)
        payload = ticlassmap.toXml()
        util.log_debug('addVirtualDeviceTiClassMap: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addVirtualDeviceTiClassMapMatchCondition(self, devicename, classmapmatchcond, class_map_name, session, add_ref = True):
        """
        add addVirtualDeviceTiClassMapMatchCondition for the given device
        Args: classmapmatchcond object, session
        Return: None
        """
        uri = self.url + '/virtual-devices/virtual-device=%s/ti-class-maps/class-map=%s' % (devicename, class_map_name)
        payload = classmapmatchcond.toXml()
        util.log_debug('addVirtualDeviceTiClassMapMatchCondition: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addVirtualDevicePolicyMapsContainer(self, devicename, session, task_id, add_ref = False):
        vd_uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        xml_output = yang.Sdk.getData(vd_uri, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.virtual_device, 'ti_policy_maps'):
            payload = '<ti-policy-maps/>'
            yang.Sdk.createData(vd_uri, payload, session, False)
            self.device.set_field_value('ti_policy_maps', [])

    def addVirtualDeviceTiPolicyMap(self, devicename, policymap, session, task_id, add_ref = True):
        """
        add addVirtualDeviceTiPolicyMap for the given device
        Args: policymap object, session
        Return: None
        """
        self.addVirtualDevicePolicyMapsContainer(devicename, session, task_id)
        uri = "%s/virtual-devices/virtual-device=%s/ti-policy-maps" % (self.url, devicename)
        payload = policymap.toXml()
        util.log_debug('addVirtualDeviceTiPolicyMap: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addVirtualDeviceNetworkObjectsContainer(self, devicename, session, task_id, add_ref = False):
        vd_uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        xml_output = yang.Sdk.getData(vd_uri, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.virtual_device, 'network_objects'):
            payload = '<network-objects/>'
            yang.Sdk.createData(vd_uri, payload, session, False)
            self.device.set_field_value('network_objects', [])

    def addVirtualDeviceNetworkObject(self, devicename, networkobject, session, task_id, addreference=True):
        """
        add network-object for the given device
        Args: network-object object, session
        Return: None
        """
        self.addVirtualDeviceNetworkObjectsContainer(devicename, session, task_id)
        uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        uri = uri + '/network-objects'
        payload = networkobject.toXml()
        util.log_debug('addNetworkObject: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addVirtualDeviceObjectGroupsContainer(self, devicename, session, task_id, add_ref = False):
        vd_uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        xml_output = yang.Sdk.getData(vd_uri, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.virtual_device, 'object_groups'):
            payload = '<object-groups/>'
            yang.Sdk.createData(vd_uri, payload, session, False)
            self.device.set_field_value('object_groups', [])

    def addVirtualDeviceObjectGroup(self, devicename, objectgroup, session, task_id, addreference=True):
        """
        add objectgroup for the given device
        Args: objectgroup object, session
        Return: None
        """
        self.addVirtualDeviceObjectGroupsContainer(devicename, session, task_id)
        uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        uri = uri + '/object-groups'
        payload = objectgroup.toXml()
        util.log_debug('addObjectGroups: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addVirtualDeviceTiPolicyMapClass(self, devicename, policymapclass, policy_map_name, session, add_ref = True):
        """
        add addVirtualDeviceTiPolicyMapClass for the given device
        Args: policymapclass object, session
        Return: None
        """
        uri = self.url + '/virtual-devices/virtual-device=%s/ti-policy-maps/policy-map=%s' % (devicename, policy_map_name)
        payload = policymapclass.toXml()
        util.log_debug('addVirtualDeviceTiPolicyMapClass: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addVirtualDeviceTiPolicyMapClassInspect(self, devicename, policymapclassinspect, policy_map_name, class_map_name, session, add_ref = True):
        """
        add addTiPolicyMapClassInspect for the given device
        Args: policymapclassinspect object, session
        Return: None
        """
        uri = self.url + '/virtual-devices/virtual-device=%s/ti-policy-maps/policy-map=%s/class=%s' % (devicename, policy_map_name, class_map_name)
        payload = policymapclassinspect.toXml()
        util.log_debug('addVirtualDeviceTiPolicyMapClassInspect: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)


    def addDmvpnTunnelContainer(self, session, add_ref = False):
        dmvpntunnels = self.device.get_field_value('dmvpntunnels')
        if(dmvpntunnels == None):
            payload = '<dmvpntunnels/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('dmvpntunnels', [])

    def addDmvpnTunnel(self, intf, session, add_ref = True):
        """
        add tunnel for the given device
        Args: tunnel object, session
        Return: None
        """
        self.addDmvpnTunnelContainer(session)
        uri = self.url + '/dmvpntunnels'
        payload = intf.toXml()
        util.log_debug('addTunnel: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addIpPrefixListListsContainer(self, session, add_ref = False):
        ipprefixlistlists = self.device.get_field_value('ip_prefixlist_list')
        if(ipprefixlistlists == None):
            payload = '<ip-prefixlist-list/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('ip_prefixlist_list', [])

    def addIpPrefixList(self, ipprefixlist, session, add_ref = True):
        """
        add ipprefixlist for the given device
        Args: ipprefixlist object, session
        Return: None
        """
        self.addIpPrefixListListsContainer(session)
        uri = self.url + '/ip-prefixlist-list'
        payload = ipprefixlist.toXml()
        util.log_debug('addIpPrefixList: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addPartitionsContainer(self, session, add_ref = False):
        partitions = self.device.get_field_value('partitions')
        if(partitions == None):
            payload = '<partitions/>'
            yang.Sdk.createData(self.url, payload, session, False)
            self.device.set_field_value('partitions', [])

    def addPartition(self, partition, session, add_ref = True):
        """
        add partition for the given device
        Args: partition object, session
        Return: None
        """
        self.addPartitionsContainer(session)
        uri = self.url + '/partitions'
        payload = partition.toXml()
        util.log_debug('addPartition: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addARecordContainer(self, session, add_ref = False):
        arecords = self.device.get_field_value('a_records')
        if(arecords == None):
           payload = '<a-records/>'
           yang.Sdk.createData(self.url, payload, session, False)
           self.device.set_field_value('a_records', [])

    def addARecord(self, a_record, session, addreference=True):
        """
        add a_record for the given device
        Args: a_record object, session
        Return: None
        """
        self.addARecordContainer(session)
        uri = self.url + '/a-records'
        payload = a_record.toXml()
        util.log_debug('add a_record: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addHostRecordContainer(self, session, add_ref = False):
        arecords = self.device.get_field_value('host_records')
        if(arecords == None):
           payload = '<host-records/>'
           yang.Sdk.createData(self.url, payload, session, False)
           self.device.set_field_value('host_records', [])

    def addHostRecord(self, host_record, session, addreference=True):
        """
        add host_record for the given device
        Args: host_record object, session
        Return: None
        """
        self.addHostRecordContainer(session)
        uri = self.url + '/host-records'
        payload = host_record.toXml()
        util.log_debug('add host_record: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addAddressbooksContainer(self, session, add_ref = False):
        arecords = self.device.get_field_value('addressbooks')
        if(arecords == None):
           payload = '<addressbooks/>'
           yang.Sdk.createData(self.url, payload, session, False)
           self.device.set_field_value('addressbooks', [])

    def addAddressbook(self, address_book, session, addreference=True):
        """
        add address_book for the given device
        Args: address_book object, session
        Return: None
        """
        self.addAddressbooksContainer(session)
        uri = self.url + '/addressbooks'
        payload = address_book.toXml()
        util.log_debug('add address_book: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)


    def addVirtualDeviceAddressesContainer(self, devicename, session, task_id, add_ref = False):
        vd_uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        xml_output = yang.Sdk.getData(vd_uri, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.virtual_device, 'addresses'):
            payload = '<addresses/>'
            yang.Sdk.createData(vd_uri, payload, session, False)
            self.device.set_field_value('addresses', [])

    def addVirtualDeviceAddress(self, devicename, address, session, task_id, add_ref = True):
        """
        add addVirtualDeviceAddress for the given device
        Args: address object, session
        Return: None
        """
        self.addVirtualDeviceAddressesContainer(devicename, session, task_id)
        uri = "%s/virtual-devices/virtual-device=%s/addresses" % (self.url, devicename)
        payload = address.toXml()
        util.log_debug('addVirtualDeviceAddress: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addVirtualDeviceStaticRoutesContainer(self, devicename, session, task_id, add_ref = False):
        vd_uri = "%s/virtual-devices/virtual-device=%s" % (self.url, devicename)
        xml_output = yang.Sdk.getData(vd_uri, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.virtual_device, 'static_routes'):
            payload = '<static-routes/>'
            yang.Sdk.createData(vd_uri, payload, session, False)
            self.device.set_field_value('static-routes', [])

    def addVirtualDeviceStaticRoute(self, devicename, static_route, session, task_id, add_ref = True):
        """
        add addVirtualDeviceStaticRoute for the given device
        Args: static_route object, session
        Return: None
        """
        self.addVirtualDeviceStaticRoutesContainer(devicename, session, task_id)
        uri = "%s/virtual-devices/virtual-device=%s/static-routes" % (self.url, devicename)
        payload = static_route.toXml()
        util.log_debug('addVirtualDeviceStaticRoute: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, add_ref)

    def addAddressesContainer(self, session, add_ref = False):
        addresses = self.device.get_field_value('addresses')
        if(addresses == None):
           payload = '<addresses/>'
           yang.Sdk.createData(self.url, payload, session, False)
           self.device.set_field_value('addresses', [])

    def addAddress(self, address, session, addreference=True):
        """
        add address for the given device
        Args: address object, session
        Return: None
        """
        self.addAddressesContainer(session)
        uri = self.url + '/addresses'
        payload = address.toXml()
        util.log_debug('add address: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addGlobalAddressSetContainer(self, session, add_ref = False):
        address_sets = self.device.get_field_value('address_sets')
        if(address_sets == None):
           payload = '<address-sets/>'
           yang.Sdk.createData(self.url, payload, session, False)
           self.device.set_field_value('address_sets', [])

    def addGlobalAddressSet(self, address_set, session, addreference=True):
        """
        add address_set for the given device
        Args: address_set object, session
        Return: None
        """
        self.addGlobalAddressSetContainer(session)
        uri = self.url + '/address-sets'
        payload = address_set.toXml()
        util.log_debug('add address_set: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)        

    def addRealServersContainer(self, session, add_ref = False):
        real_servers = self.device.get_field_value('real_servers')
        if(real_servers == None):
           payload = '<real-servers/>'
           yang.Sdk.createData(self.url, payload, session, False)
           self.device.set_field_value('real_servers', [])

    def addRealServer(self, real_server, session, addreference=True):
        """
        add real_server for the given device
        Args: real_server object, session
        Return: None
        """
        self.addRealServersContainer(session)
        uri = self.url + '/real-servers'
        payload = real_server.toXml()
        util.log_debug('add real_server: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addRServicePoolsContainer(self, session, add_ref = False):
        rservice_pools = self.device.get_field_value('rservice_pools')
        if(rservice_pools == None):
           payload = '<rservice-pools/>'
           yang.Sdk.createData(self.url, payload, session, False)
           self.device.set_field_value('rservice_pools', [])

    def addRServicePool(self, rservice_pool, session, addreference=True):
        """
        add rservice_pool for the given device
        Args: rservice_pool object, session
        Return: None
        """
        self.addRServicePoolsContainer(session)
        uri = self.url + '/rservice-pools'
        payload = rservice_pool.toXml()
        util.log_debug('add rservice_pool: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)


    def addHealthMonitorOnDevice(self,healthmonitorobj,session,addreference=True):
        """Add Health Monitors on Device instead of on Resource Pools"""
        healthmonitor = self.device.get_field_value('health_monitors')
        if healthmonitor == None:
            payload = '<health-monitors/>'
            yang.Sdk.createData(self.url, payload, session, False)
        uri = '%s/health-monitors' % (self.url)
        payload = healthmonitorobj.toXml()
        util.log_debug('uri = %s\npayload = %s' % (uri, payload))
        return yang.Sdk.createData(uri, payload, session, addreference)



    def addRServicePoolHealthMonitor(self, rser_pool_name, domain_number, partition, hmobj, session, task_id, addReference = True):
        """
        Add allowed health_monitor to given interface
        Args: hmobj, session, taskid
        Return: None
        """
        rser_pool = self.url+'/rservice-pools/rservice-pool=%s,%s,%s' % (rser_pool_name, domain_number, partition)
        xml_output = yang.Sdk.getData(rser_pool, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.rservice_pool, 'health_monitors'):
            payload = '<health-monitors/>'
            yang.Sdk.createData(rser_pool, payload, session, False)
            self.device.add_field_value('health_monitors', [])
        uri = '%s/health-monitors' % (rser_pool)
        payload = hmobj.toXml()
        util.log_debug('uri = %s\npayload = %s' % (uri, payload))
        return yang.Sdk.createData(uri, payload, session, addReference)

    def addRServicePoolPoolMember(self, rser_pool_name, domain_number, partition, pmobj, session, task_id, addReference = True):
        """
        Add pool member to given resource pool
        Args: pmobj, session, taskid
        Return: None
        """
        rser_pool = self.url+'/rservice-pools/rservice-pool=%s,%s,%s' % (rser_pool_name, domain_number, partition)
        xml_output = yang.Sdk.getData(rser_pool, '', task_id)
        obj = util.parseXmlString(xml_output)
        if not hasattr(obj.rservice_pool, 'pool_members'):
            payload = '<pool-members/>'
            yang.Sdk.createData(rser_pool, payload, session, False)
            self.device.add_field_value('pool_members', [])
        uri = '%s/pool-members' % (rser_pool)
        payload = pmobj.toXml()
        util.log_debug('uri = %s\npayload = %s' % (uri, payload))
        return yang.Sdk.createData(uri, payload, session, addReference)        

    def addVirtualServersContainer(self, session, add_ref = False):
        virtual_servers = self.device.get_field_value('virtual_servers')
        if(virtual_servers == None):
           payload = '<virtual-servers/>'
           yang.Sdk.createData(self.url, payload, session, False)
           self.device.set_field_value('virtual_servers', [])

    def addVirtualServer(self, virtual_server, session, addreference=True):
        """
        add virtual_server for the given device
        Args: virtual_server object, session
        Return: None
        """
        self.addVirtualServersContainer(session)
        uri = self.url + '/virtual-servers'
        payload = virtual_server.toXml()
        util.log_debug('add virtual_server: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference) 

    def addCertificatesContainer(self, session, add_ref = False):
        certificates = self.device.get_field_value('certificates')
        if(certificates == None):
           payload = '<certificates/>'
           yang.Sdk.createData(self.url, payload, session, False)
           self.device.set_field_value('certificates', [])

    def addCertificate(self, certificate, session, addreference=True):
        """
        add certificate for the given device
        Args: certificate object, session
        Return: None
        """
        self.addCertificatesContainer(session)
        uri = self.url + '/certificates'
        payload = certificate.toXml()
        util.log_debug('add certificate: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addPortGroupsContainer(self, session, add_ref = False):
        port_groups = self.device.get_field_value('port-groups')
        if(port_groups == None):
           payload = '<port-groups/>'
           yang.Sdk.createData(self.url, payload, session, False)
           self.device.set_field_value('port-groups', [])

    def addPortGroup(self, portgroup, session, addreference=True):
        """
        add port-group for the given device
        Args: port-group object, session
        Return: None
        """
        self.addPortGroupsContainer(session)
        uri = self.url + '/port-groups'
        payload = portgroup.toXml()
        util.log_debug('add portgroup: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session, addreference)

    def addHostRecords(self, session, dns_view,zone,subzone,hostrecordobj,addref=False):
        uri = self.url+'/configurations/configuration=NCX/dns-views/dns-view='+str(dns_view)+'/dns-zone='+str(zone)+'/dns-sub-zone='+str(subzone)
        payload = hostrecordobj.toXml()
        util.log_debug('add portgroup: %s, payload = %s' % (uri, payload))
        yang.Sdk.createData(uri, payload, session,addref)

def getAllDevices(self):
    device_rc_path = yang.Sdk.getRcPathListForXPath("/controller:devices")
    if util.isEmpty(rcpaths):
        util.log_debug('rcpaths for this device = %s are empty' %(ipAddress))
        return None
    rcPath = rcpaths[0]
    if len(rcpaths) > 1:
        util.log_debug('WARN: got multiple rcpaths. count = %d' % (len(rcpaths)))
        util.log_debug('%s' % (rcpaths))
    xml = yang.Sdk.getData(rcPath, '', None, None)
    # util.log_debug('devicexml = %s' % (xml))
    if(xml == None):
        util.log_debug('No xml data. rcPath = %s' % (rcPath))
        return None
    xmlObj = util.parseXmlString(xml)
    return xmlObj



def getDeviceByIp(ipAddress,validate_type = False,task_id=None):
    """
    fetch the device complete tree for given ip
    Args: device ip
    Return: device object which has device information
    """
    rcpaths = yang.Sdk.getRcPathListForXPathAndValue(
            '/controller:devices/device/mgmt-ip-address', ipAddress)
    if util.isEmpty(rcpaths):
        util.log_debug('rcpaths for this device = %s are empty' %(ipAddress))
        return None
    rcPath = rcpaths[0]
    if len(rcpaths) > 1:
        util.log_debug('WARN: got multiple rcpaths. count = %d' % (len(rcpaths)))
        util.log_debug('%s' % (rcpaths))
    xml = yang.Sdk.getData(rcPath, '', task_id, None)
    # util.log_debug('devicexml = %s' % (xml))
    if(xml == None):
        util.log_debug('No xml data. rcPath = %s' % (rcPath))
        return None
    xmlObj = util.parseXmlString(xml)
    dev = Device(xmlObj)

    if validate_type and util.isEmpty(dev.device.get_field_value('device_type')):
        raise Exception('Device type is empty for %s' % (ipAddress))

    return dev

def getDeviceByUniqueName(unique_name, validate_type = False):
    """
    fetch the device complete tree for given unique_name
    Args: device unique_name
    Return: device object which has device information
    """
    rcpaths = yang.Sdk.getRcPathListForXPathAndValue(
            '/controller:devices/device/unique-name', unique_name)
    if util.isEmpty(rcpaths):
        util.log_debug('rcpaths for this device = %s are empty' %(unique_name))
        return None
    rcPath = rcpaths[0]
    if len(rcpaths) > 1:
        util.log_debug('WARN: Found multiple devices for unique-name; count = %d' % (len(rcpaths)))
        util.log_debug('%s' % (rcpaths))
    xml = yang.Sdk.getData(rcPath, '', None, None)
    # util.log_debug('devicexml = %s' % (xml))
    if(xml == None):
        util.log_debug('No xml data. rcPath = %s' % (rcPath))
        return None
    xmlObj = util.parseXmlString(xml)
    dev = Device(xmlObj)

    if validate_type and util.isEmpty(dev.device.get_field_value('device_type')):
        raise Exception('Device type is empty for %s' % (unique_name))

    return dev

def getDeviceByName(name, validate_type = False):
    """
    fetch the device complete tree for given ip
    Args: device name
    Return: device object which has device information
    """
    rcpaths = yang.Sdk.getRcPathListForXPathAndValue(
            '/controller:devices/device/name', name)
    if util.isEmpty(rcpaths):
        return None
    rcPath = rcpaths[0]
    if len(rcpaths) > 1:
        util.log_debug('WARN: Found multiple devices for name; count = %d' % (len(rcpaths)))
        util.log_debug('%s' % (rcpaths))
    xml = yang.Sdk.getData(rcPath, '', None, None)
    # util.log_debug('devicexml = %s' % (xml))
    if(xml == None):
        util.log_debug('No xml data. rcPath = %s' % (rcPath))
        return None
    xmlObj = util.parseXmlString(xml)
    dev = Device(xmlObj)

    if validate_type and util.isEmpty(dev.device.get_field_value('device_type')):
        raise Exception('Device type is empty for %s' % (name))

    return dev

def getDeviceById(id, validate_type = False):
    """
    fetch the device complete tree for given ip
    Args: device ip
    Return: device object which has device information
    """
    rcpaths = yang.Sdk.getRcPathListForXPathAndValue(
            '/controller:devices/device/id', id)
    if util.isEmpty(rcpaths):
        return None
    rcPath = rcpaths[0]
    if len(rcpaths) > 1:
        util.log_debug('WARN: got multiple rcpaths. count = %d' % (len(rcpaths)))
        util.log_debug('%s' % (rcpaths))
    xml = yang.Sdk.getData(rcPath, '', None, None)
    # util.log_debug('devicexml = %s' % (xml))
    if(xml == None):
        util.log_debug('No xml data. rcPath = %s' % (rcPath))
        return None
    xmlObj = util.parseXmlString(xml)
    dev = Device(xmlObj)

    if validate_type and util.isEmpty(dev.device.get_field_value('device_type')):
        raise Exception('Device type is empty for %s' % (id))

    return dev
def getDeviceByInterfaceName(name, validate_type = False):
    """
    fetch the device complete tree for given ip
    Args: device name
    Return: device object which has device information
    """
    rcpaths = yang.Sdk.getRcPathListForXPathAndValue(
            '/controller:devices/device/interfaces/interface/name', name)
    util.log_debug('interface name is %s' % (name))
    if util.isEmpty(rcpaths):
        return None
    rcPath = rcpaths[0]
    util.log_debug('rcpaths is %s' % (rcPath))
    rcpaths = util.get_parent_rcpath(rcPath, 2)
    util.log_debug('new rcpaths is %s' % (rcpaths))
    if len(rcpaths) > 1:
        util.log_debug('WARN: got multiple rcpaths. count = %d' % (len(rcpaths)))
        util.log_debug('%s' % (rcpaths))
    xml = yang.Sdk.getData(rcpaths, '', None, None)
    # util.log_debug('devicexml = %s' % (xml))
    if(xml == None):
        util.log_debug('No xml data. rcPath = %s' % (rcPath))
        return None
    xmlObj = util.parseXmlString(xml)
    dev = Device(xmlObj)

    if validate_type and util.isEmpty(dev.device.get_field_value('device_type')):
        raise Exception('Device type is empty for %s' % (name))

    return dev


class DeviceService:

    _instance = None

    def __init__(self):
        from com.anuta.util import ApplicationContextProvider
        ctx = ApplicationContextProvider.getApplicationContext()
        self.ctx = ctx
        from com.anuta.operation.service import DeviceService
        self.device_service = ctx.getBean(DeviceService)

    @staticmethod
    def newDeviceDO():
        util.log_debug('Creating new device DO')
        return DeviceService.getInstance().device_service.newDeviceDO()

    @staticmethod
    @staticmethod
    def newDeviceCredentialSetDO():
        util.log_debug('Creating new device credential set DO')
        return DeviceService.getInstance().device_service.newDeviceCredentialSetDO()

    @staticmethod
    def fetchDeviceCredentialSetByName(name):
        util.log_debug('getting Cred DO')
        return DeviceService.getInstance().device_service.fetchDeviceCredentialSetByName(name)

    @staticmethod
    def getInstance():
        if(DeviceService._instance == None):
            DeviceService._instance = DeviceService()
        return DeviceService._instance

class AgentManager:

    _instance = None

    def __init__(self):
        from com.anuta.util import ApplicationContextProvider
        ctx = ApplicationContextProvider.getApplicationContext()
        self.ctx = ctx
        from com.anuta.service.configmgr import AgentDeviceManager
        self.agent_device_manager = ctx.getBean(AgentDeviceManager)

    @staticmethod
    def assignAgentForDevice(dev):
        util.log_debug('Assigning Agent to device')
        return AgentManager.getInstance().agent_device_manager.assignAgentForDevice(dev)

    @staticmethod
    def getInstance():
        if(AgentManager._instance == None):
            AgentManager._instance = AgentManager()
        return AgentManager._instance

class NetworkManagementService:

    _instance = None

    def __init__(self):
        from com.anuta.util import ApplicationContextProvider
        ctx = ApplicationContextProvider.getApplicationContext()
        self.ctx = ctx
        from com.anuta.api.provider import NetworkMgmtService
        self.network_mgmt_service = ctx.getBean(NetworkMgmtService)

    @staticmethod
    def invokeDeviceInventoryTasks(ip, id_):
        util.log_debug('Invoking Inventory')
        return NetworkManagementService.getInstance().network_mgmt_service.invokeDeviceInventoryTasks(ip, id_, None)

    @staticmethod
    def getInstance():
        if(NetworkManagementService._instance == None):
            NetworkManagementService._instance = NetworkManagementService()
        return NetworkManagementService._instance

class CreateDevice:
    def __init__(self):
        self.durl =  '/app/restconf/data/controller:devices'

    class AddDevice(util.BaseObject):
        def __init__(self):
            util.BaseObject.__init__(self, 'device')
        
        def setId(self, value):
            self.root.set_field_value('id', value)

        def setName(self, value):
            self.root.set_field_value('name', value)

        def setMgmtIPAddress(self, value):
            self.root.set_field_value('mgmt-ip-address', value)

        def setCredentialSet(self, value):
            self.root.set_field_value('credential-set', value)

        def setUniqueName(self, value):
            self.root.set_field_value('unique-name', value)


    def adddevice(self,deviceobject,session):
        payload = deviceobject.toXml()
        util.log_debug('addDevice: %s, payload = %s' % (self.durl, payload))
        yang.Sdk.createDataWithTaskId(self.durl, payload, session,"COMMON",False)


    def getDeviceStatus(self,ip,taskid):
        rcpath = self.durl + '/device='+str(ip)
        util.log_debug("This is taskid")
        util.log_debug(taskid)
        xml = yang.Sdk.getData(rcpath, '', taskid, None)
        xmlObj = util.parseXmlString(xml)
        util.log_debug("THis is xmlObj")
        util.log_debug(xmlObj)
        status = xmlObj.device.status
        return status


    def IsDevicePresent(self,ip,session):
        rcpath = self.durl
        xml = yang.Sdk.getData(rcpath, '', session, None)
        xmlObj = util.parseXmlString(xml)
        devices_list = xmlObj.devices
        devices_list = util.convert_to_list(devices_list)
        if devices_list == []:
                return False
        for items in devices_list:
            if hasattr(items,'device'):
                device_list = items.device
                device_list = util.convert_to_list(device_list)
                for device in device_list:
                    if str(ip) == str(device.id):
                            return True
        return False


def adddevices():
    deviceobj = CreateDevice()
    return deviceobj


