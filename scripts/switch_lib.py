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

from servicemodel import yang
from servicemodel import util
from servicemodel import ipam
from servicemodel import devicemgr
from servicemodel.controller.devices.device import spanning_tree
from servicemodel.controller.devices.device import vlans
from servicemodel.controller.devices.device import interfaces

from cpedeployment_lib import getLocalObject
from ipaddr_lib import IPAddress
from ipaddr_lib import IPNetwork
from endpoint_lib import get_used_ip_list_from_ippool
from endpoint_lib import get_freeip_from_cidr
from endpoint_lib import add_ipaddress_entries

def spanningtree(smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs['inputdict']
    options = inputdict['options']
    mode = inputdict['mode']
    extend_system_id = inputdict['extend_system_id']
    vlan_range = inputdict['vlan_range']
    priority = inputdict['priority']
    util.log_debug("mode:"+str(options))
    if options == 'mode':
        util.log_debug("in mode")
        spanningtreeobj = spanning_tree.mode.mode()
        spanningtreeobj.mode = mode
        if extend_system_id == 'true':
            spanningtreeobj.extend_system_id = extend_system_id
        spanningtree = dev.url.split("/data")[1]
        if not yang.Sdk.dataExists(spanningtree+"/basicDeviceConfigs:spanning-tree"):
            yang.Sdk.createData(dev.url, '<spanning-tree/>', sdata.getSession(), False)
        yang.Sdk.createData(dev.url + '/spanning-tree', spanningtreeobj.getxml(filter=True), sdata.getSession())
    elif options == 'vlan':
        spanningtree = dev.url.split("/data")[1]
        if not yang.Sdk.dataExists(spanningtree+"/basicDeviceConfigs:spanning-tree"):
            yang.Sdk.createData(dev.url, '<spanning-tree/>', sdata.getSession(), False)
        xml_output = yang.Sdk.getData(dev.url+"/basicDeviceConfigs:spanning-tree", '', sdata.getTaskId())
        obj = util.parseXmlString(xml_output)
        if hasattr(obj.spanning_tree,"vlan"):
            vlan_list = []
            for vlan in util.convert_to_list(obj.spanning_tree.vlan):
                if priority == vlan.priority:
                    yang.Sdk.deleteData(dev.url+"/basicDeviceConfigs:spanning-tree/vlan="+vlan.vlan.replace(',','%2C'), '', sdata.getTaskId(), sdata.getSession())
                    vlan_list.append(vlan.vlan)
                else:
                    vlan = vlan_range
            if vlan_list != []:
                vlan = ",".join(vlan_list)
                vlan = vlan+","+vlan_range
                vlan = format_vlan(vlan)
                util.log_debug("vlan:"+str(vlan))

        else:
            vlan = vlan_range
        spanningtreeobj = spanning_tree.vlan.vlan()
        spanningtreeobj.vlan = format_vlan(vlan)
        spanningtreeobj.priority = priority
        yang.Sdk.createData(dev.url + '/spanning-tree', spanningtreeobj.getxml(filter=True), sdata.getSession())

def format_vlan(vlan):
    l = vlan.split(",")
    list1 = []
    for i in l:
        if "-" in i:
            list1.extend(range(int(i.split("-")[0]),int(i.split("-")[1])+1))
        else:
            list1.append(int(i))
    list2 = list(set(list1))
    list2.sort(key=lambda x: [int(y) for y in str(x).split('-')])
    ret = []
    a = b = list2[0]

    for el in list2[1:]:
        if el == b+1:
            b = el
        else:
            ret.append(str(a) if a==b else str(a)+"-"+str(b)) # is a single or a range?
            a = b = el                       # let's start again with a single
    ret.append(str(a) if a==b else str(a)+"-"+str(b))
    vlan = ','.join(ret)
    return vlan

def vlandef(smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs['inputdict']
    vlan_id = inputdict['vlan_id']
    name = inputdict['name']
    vlandefobj = vlans.vlan.vlan()
    vlandefobj.id = vlan_id
    vlandefobj.name = name
    yang.Sdk.createData(dev.url, '<vlans/>', sdata.getSession(), False)
    yang.Sdk.createData(dev.url + '/vlans', vlandefobj.getxml(filter=True), sdata.getSession())


def interfacedef(smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs['inputdict']
    interface_type = inputdict['interface_type']
    interface_name = inputdict['interface_name']
    vlan_id = inputdict['vlan_id']
    cidr = inputdict['cidr']
    interface_ip = inputdict['interface_ip']
    interface_description = inputdict['interface_description']
    interfacedefobj = interfaces.interface.interface()
    interfacedefobj.description = interface_description
    if interface_type == "Physical":
        interfacedefobj.mode = "l3-interface"
    elif interface_type == "SVI":
        #     interfacedefobj.mode = "vlan"
        interfacedefobj.vlan = vlan_id

    next_ip_address = None
    if interface_type == 'Physical':
        interfacedefobj.name = interface_name
        interfacedefobj.long_name = interface_name
        yang.Sdk.createData(dev.url, '<interfaces/>', sdata.getSession(), False)
        yang.Sdk.createData(dev.url + '/interfaces', interfacedefobj.getxml(filter=True), sdata.getSession(), False)
    elif interface_type == 'SVI':
        if util.isEmpty(vlan_id):
            raise Exception("vlan_id should not empty when interface_type is SVI")
        interfacedefobj.name = 'Vlan' + str(vlan_id)
        interfacedefobj.long_name = 'Vlan' + str(vlan_id)
        ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr)
        ip_addr_obj = ip_addr.ipam_pool_obj
        prefix = util.IPPrefix(ip_addr_obj.cidr)
        netmask = prefix.netmask
        wildcard = prefix.wildcard
        if util.isEmpty(interface_ip) or interface_ip == None:
            used_ips_list = get_used_ip_list_from_ippool(ip_addr_obj.name, sdata)
            interface_ip = get_freeip_from_cidr(ip_addr_obj.cidr, used_ips_list)
            add_ipaddress_entries(ip_addr_obj.name, interface_ip, sdata)
        else:
            ip_addr_obj = ip_addr.ipam_pool_obj
            prefix = util.IPPrefix(ip_addr_obj.cidr)
            netmask = prefix.netmask
            wildcard = prefix.wildcard
            used_ips_list = get_used_ip_list_from_ippool(ip_addr_obj.name, sdata)
            if used_ips_list.__len__() >= 0:
                if str(prefix.masklen) != str(32):
                    if interface_ip in used_ips_list:
                        raise Exception("IP given is already used in the given pool")
                used_ips_list.sort()
                cidr = ip_addr_obj.cidr
                ip = IPAddress(interface_ip)
                network_given = IPNetwork(cidr)
                (addrStr, cidrStr) = cidr.split('/')
                addr = addrStr.split('.')
                cidr = int(cidrStr)
                mask = [0, 0, 0, 0]
                for i in range(cidr):
                    mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
                net = []
                for i in range(4):
                    net.append(int(addr[i]) & mask[i])
                network = ".".join(map(str, net))
                ip_address = network

                broad = list(net)
                brange = 32 - cidr
                for i in range(brange):
                    broad[3 - i/8] = broad[3 - i/8] + (1 << (i % 8))
                last_ip_address = ".".join(map(str, broad))
                if str(prefix.masklen) != str(32):
                    if interface_ip == last_ip_address:
                        raise Exception('Broadcast IP cant be used')
                if not network_given.Contains(ip):
                    raise Exception('Invalid IP address for this cidr')
            add_ipaddress_entries(ip_addr_obj.name, interface_ip, sdata)
        payload = "<interface-ip>%s</interface-ip>" % interface_ip
        serv_uri = sdata.getRcPath()
        yang.Sdk.createData(serv_uri, payload, sdata.getSession())

        if interface_ip is not None:
            interfacedefobj.ip_address = interface_ip
            interfacedefobj.netmask = netmask
        yang.Sdk.createData(dev.url, '<interfaces/>', sdata.getSession(), False)
        yang.Sdk.createData(dev.url + '/interfaces', interfacedefobj.getxml(filter=True), sdata.getSession(), False)


def delete_int(smodelctx, sdata, device, **kwargs):
    config = util.parseXmlString(sdata.getPayload())
    config = config.interface
    interface_type = config.get_field_value('interface_type')
    interface_name = config.get_field_value('interface_name')
    if config.get_field_value('vlan_id') is not None:
        vlan_id = config.get_field_value('vlan_id')
    else:
        vlan_id = None

    if interface_type == "SVI":
        intf_obj = interfaces.interface.interface()
        interface_name1 = "Vlan" + str(vlan_id)
        intf_obj.name = interface_name1
        intf_obj.long_name = interface_name1
        intf_obj.mode = "vlan"
        uri = device.url + '/interface:interfaces/interface=%s' % (str(interface_name1).replace('/', '%2F'))
        payload = intf_obj.getxml(filter=True)
        if device.isInterfaceInDeviceExists(interface_name1):
            yang.Sdk.deleteData(uri, payload, sdata.getTaskId(), sdata.getSession())
    elif interface_type == "Physical":
        intf_obj = interfaces.interface.interface()
        intf_obj.name = interface_name
        intf_obj.long_name = interface_name
        intf_obj.description._empty_tag = True
        uri = device.url + '/interface:interfaces/interface=%s' % (str(interface_name).replace('/', '%2F'))
        payload = intf_obj.getxml(filter=True)
        print 'Patch Interface: %s, payload = %s' % (uri, payload)
        if device.isInterfaceInDeviceExists(interface_name):
            yang.Sdk.patchData(uri, payload, sdata, add_reference=False)
            intf_obj_phy1 = interfaces.interface.interface()
            intf_obj_phy1.name = interface_name
            intf_obj_phy1.long_name = interface_name
            intf_obj_phy1.mode._empty_tag = True
            payload1 = intf_obj_phy1.getxml(filter=True)
            yang.Sdk.patchData(uri, payload1, sdata, add_reference=False)
        else:
            print "skipping delete for interface as it does not exists on device"


def switchport(smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs['inputdict']
    options = inputdict['options']
    port_security_options = inputdict['port_security_options']
    maximum = inputdict['maximum']
    violation = inputdict['violation']
    trunk_options = inputdict['trunk_options']
    encapsulation = inputdict['encapsulation']
    allowed_vlan = inputdict['allowed_vlan']
    access = inputdict['access']
    mode = inputdict['mode']

    obj = getLocalObject(sdata, 'interface')
    interface_type = obj.interface.interface_type
    if hasattr(obj.interface, 'interface_name'):
        interface_name = obj.interface.interface_name
    # if hasattr(obj.interface, 'vlan_id'):
    #     vlan_id = obj.interface.vlan_id
    if interface_type == 'Physical':
        if options == "mode":
            interfacedefobj = interfaces.interface.interface()
            interfacedefobj.name = interface_name
            interfacedefobj.long_name = interface_name
            interfacedefobj.mode = mode
            yang.Sdk.createData(dev.url + '/interfaces', interfacedefobj.getxml(filter=True), sdata.getSession(), False)
            switchportobj = interfaces.interface.allowed_vlans.allowed_vlans()
            switchportobj.is_mode = 'true'
            allowvlanurl = dev.url + '/interfaces/interface=%s'  % (str(interface_name).replace('/', '%2F'))
            yang.Sdk.createData(allowvlanurl, switchportobj.getxml(filter=True), sdata.getSession())
        elif options == "access":
            interfacedefobj = interfaces.interface.interface()
            interfacedefobj.name = interface_name
            interfacedefobj.long_name = interface_name
            interfacedefobj.mode = 'access'
            yang.Sdk.createData(dev.url + '/interfaces', interfacedefobj.getxml(filter=True), sdata.getSession(), False)
            switchportobj = interfaces.interface.allowed_vlans.vlan.vlan()
            switchportobj.id = access
            vlanurl = dev.url + '/interfaces/interface=%s' % (str(interface_name).replace('/', '%2F'))
            yang.Sdk.createData(vlanurl, '<allowed-vlans/>', sdata.getSession(), False)

            allowvlanurl = dev.url + '/interfaces/interface=%s/allowed-vlans'  % (str(interface_name).replace('/', '%2F'))
            yang.Sdk.createData(allowvlanurl, switchportobj.getxml(filter=True), sdata.getSession())
        elif options == "trunk":
            interfacedefobj = interfaces.interface.interface()
            interfacedefobj.name = interface_name
            interfacedefobj.long_name = interface_name
            interfacedefobj.mode = 'trunk'
            yang.Sdk.createData(dev.url + '/interfaces', interfacedefobj.getxml(filter=True), sdata.getSession(), False)
            if trunk_options == "allowed":
                switchportobj = interfaces.interface.allowed_vlans.vlan.vlan()
                switchportobj.id = allowed_vlan
                vlanurl = dev.url + '/interfaces/interface=%s' % (str(interface_name).replace('/', '%2F'))
                yang.Sdk.createData(vlanurl, '<allowed-vlans/>', sdata.getSession(), False)

                allowvlanurl = dev.url + '/interfaces/interface=%s/allowed-vlans'  % (str(interface_name).replace('/', '%2F'))
                yang.Sdk.createData(allowvlanurl, switchportobj.getxml(filter=True), sdata.getSession())
            elif trunk_options == "encapsulation":
                switchportobj = interfaces.interface.allowed_vlans.allowed_vlans()
                switchportobj.is_encap = 'true'
                allowvlanurl = dev.url + '/interfaces/interface=%s'  % (str(interface_name).replace('/', '%2F'))
                vlanurl = dev.url + '/interfaces/interface=%s' % (str(interface_name).replace('/', '%2F'))
                yang.Sdk.createData(vlanurl, '<allowed-vlans/>', sdata.getSession(), False)
                yang.Sdk.createData(allowvlanurl, switchportobj.getxml(filter=True), sdata.getSession())
        elif options == "port-security":
            switchportobj = interfaces.interface.port_security.port_security()
            if port_security_options == 'maximum':
                switchportobj.portSecurityMaximum = maximum
            elif port_security_options == 'violation':
                switchportobj.portViolation = violation
            porturl = dev.url + '/interfaces/interface=%s'  % (str(interface_name).replace('/', '%2F'))
            yang.Sdk.createData(porturl, switchportobj.getxml(filter=True), sdata.getSession())



class IpamPoolID(yang.ServiceModelContext):

    """ The service context used by all the Application_delivery Resource Unit service handlers
    """
    def __init__(self, id, sdata, cidr = None):
        yang.ServiceModelContext.__init__(self, id, sdata)
        self.load_service_object(cidr)
        self.ipam_pool_obj = None
        self.cidr = cidr
        # if isinstance(self.ipaddresspools.ipaddress_pool, list):
        #     for pool  in  self.ipaddresspools.ipaddress_pool:
        #         if pool.name == self.cidr:
        #             self.ipam_pool_obj = pool
        #             print "ipam_pool_obj", str(self.ipam_pool_obj)
        #             return
        # else:
        #     if self.ipaddresspools.ipaddress_pool.name == self.cidr:
        #         self.ipam_pool_obj = self.ipaddresspools.ipaddress_pool
        #         print "ipam_pool_obj", str(self.ipam_pool_obj)
        if self.ipaddresspool.name == self.cidr:
            self.ipam_pool_obj = self.ipaddresspool
            util.log_debug( "ipam_pool_obj", str(self.ipam_pool_obj))

    def load_service_object(self, cidr):
        cidr_name_local = cidr
        cidr_name_local = cidr_name_local.replace('/', '%2F')
        cidr_name_local = cidr_name_local.replace(' ', '%20')
        cidr_name_local = cidr_name_local.replace('&', '%26')
        self.service_rcpath = "/ipam:ipaddress-pools/ipaddress-pool=%s" %(cidr_name_local)
        print 'setting rcpath = %s' % (self.service_rcpath)
        yang.ServiceModelContext.load_service_object(self, self.service_rcpath)
        self.ipaddresspool = self.service_xmlobj.ipaddress_pool

        print 'service_obj: %s, tostr: %s' % (self.ipaddresspool, self.ipaddresspool.toXml())