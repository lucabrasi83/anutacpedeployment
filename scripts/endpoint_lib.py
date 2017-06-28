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
from servicemodel.controller import devices
import re
from com.anuta.api import DataNodeNotFoundException
from operator import attrgetter

from cpedeployment_lib import getLocalObject
from cpedeployment_lib import ServiceModelContext
from cpedeployment_lib import route_maps
from ipaddr_lib import IPAddress
from ipaddr_lib import IPNetwork
managed_cpe_services_debug = False

def log(s):
    if managed_cpe_services_debug:
        util.log_debug(s)
def get_used_ip_list_from_ippool(ipaddress_pool_name, sdata):
    print "inside get_used_ip_list_from_ippool"
    ipaddress_pool_name = util.make_interfacename(ipaddress_pool_name)
    ipaddress_pool_name = ipaddress_pool_name.replace(' ', '%20')
    ip_used_list = []
    get_ipaddress_pool_url = "/app/restconf/data/ipam:ipaddress-pools/ipaddress-pool=%s" %(ipaddress_pool_name)
    pool = yang.Sdk.getData(get_ipaddress_pool_url, '', sdata.getTaskId())
    pool = util.parseXmlString(pool)
    if hasattr(pool.ipaddress_pool, 'ipaddress_entries'):
        get_ipaddress_pool_entries_url = "/app/restconf/data/ipam:ipaddress-pools/ipaddress-pool=%s/ipaddress-entries" %(ipaddress_pool_name)
        entries = yang.Sdk.getData(get_ipaddress_pool_entries_url, '', sdata.getTaskId())
        entries = util.parseXmlString(entries)
        #print "list of ip_address_pool_entries is:", entries

        if hasattr(entries.ipaddress_entries, 'ipaddress_entry'):
            for entry in util.convert_to_list(entries.ipaddress_entries.ipaddress_entry):
                ip_used_list.append(entry.ipaddress)

    return ip_used_list


def get_freeip_from_cidr(cidr, used_list):
    print "inside get_freeip_from_cidr"
    cidr_obj = util.IPPrefix(cidr)
    gateway_ip = cidr_obj.gateway_ip()
    #used_list.sort()
    #ip_address = used_list[0]
    #last_ip_address = used_list[used_list.__len__()-1]

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
    print "gateway_ip for /32 cidr", gateway_ip
    print "cidr_obj.masklen is", cidr_obj.masklen
    if str(cidr_obj.masklen) == str(32):
        return gateway_ip
    else:
        gateway_ip = util.next_ip_address(ip_address)
        print "gateway_ip is:", gateway_ip
        while (True):
            if gateway_ip not in used_list:
                break
            else:
                gateway_ip = util.next_ip_address(gateway_ip)
        print "final gateway_ip is :", gateway_ip
        ip = IPAddress(gateway_ip)
        if not network_given.Contains(ip):
            raise Exception('Invalid IP address for this cidr')
        return gateway_ip


def add_ipaddress_entries(ipaddress_pool_name, ip_address,sdata):
    payload = '<ipaddress-entries/>'
    ipaddress_pool_name = util.make_interfacename(ipaddress_pool_name)
    ipaddress_pool_name = ipaddress_pool_name.replace(' ', '%20')
    url = '/app/restconf/data/ipam:ipaddress-pools/ipaddress-pool=%s'%(ipaddress_pool_name)
    yang.Sdk.createData(url, payload, sdata.getSession(), False)

    ## Update used count
    payload_ippool = '''<ipaddress-entry>
                        <ipaddress>'''+ip_address+'''</ipaddress>
                        <name>'''+ipaddress_pool_name+'_'+ip_address+'''</name>
                        </ipaddress-entry>'''
    yang.Sdk.createData("/app/restconf/data/ipam:ipaddress-pools/ipaddress-pool=%s/ipaddress-entries" %(ipaddress_pool_name), payload_ippool, sdata.getSession())


def wan_endpoint(entity, smodelctx, sdata, device, **kwargs):
    load_interval = None
    hierarchical_outbound_policy = None
    load_interval_delay = None
    policy_name = None
    full_obj = None
    shape_average = None
    child_qos_policy = None
    hold_queue_in = None
    hold_queue_out = None
    in_queue_length = None
    out_queue_length = None
    auto_negotiation = None
    dmvpn_obj = None

    inputdict = kwargs['inputdict']
    interface_type = inputdict['interface_type']
    interface_name = inputdict['interface_name']
    interface_description = inputdict['interface_description']
    if entity == 'cpe':
        obj = getLocalObject(sdata, 'cpe-wan')
        full_obj = obj.cpe_wan
    elif entity == 'cpe_primary':
        obj = getLocalObject(sdata, 'cpe-primary-wan')
        full_obj = obj.cpe_primary_wan
    elif entity == 'cpe_secondary':
        obj = getLocalObject(sdata, 'cpe-secondary-wan')
        full_obj = obj.cpe_secondary_wan
    elif entity == 'cpe_primary_dual':
        obj = getLocalObject(sdata, 'cpe-primary-wan')
        full_obj = obj.cpe_primary_wan
    elif entity == 'cpe_secondary_dual':
        obj = getLocalObject(sdata, 'cpe-secondary-wan')
        full_obj = obj.cpe_secondary_wan
    elif entity == 'cpe_primary_inet_dual':
        obj = getLocalObject(sdata, 'cpe-primary-inet-wan')
        full_obj = obj.cpe_primary_inet_wan
    elif entity == 'cpe_primary_mpls_dual':
        obj = getLocalObject(sdata, 'cpe-primary-mpls-wan')
        full_obj = obj.cpe_primary_mpls_wan
    elif entity == 'cpe_secondary_inet_dual':
        obj = getLocalObject(sdata, 'cpe-secondary-inet-wan')
        full_obj = obj.cpe_secondary_inet_wan
    elif entity == 'cpe_secondary_mpls_dual':
        obj = getLocalObject(sdata, 'cpe-secondary-mpls-wan')
        full_obj = obj.cpe_secondary_mpls_wan
    elif entity == 'cpe_primary_inet_triple':
        obj = getLocalObject(sdata, 'cpe-primary-inet-wan')
        full_obj = obj.cpe_primary_inet_wan
    elif entity == 'cpe_primary_mpls_triple':
        obj = getLocalObject(sdata, 'cpe-primary-mpls-wan')
        full_obj = obj.cpe_primary_mpls_wan
    elif entity == 'cpe_secondary_inet_triple':
        obj = getLocalObject(sdata, 'cpe-secondary-inet-wan')
        full_obj = obj.cpe_secondary_inet_wan
    elif entity == 'cpe_secondary_mpls_triple':
        obj = getLocalObject(sdata, 'cpe-secondary-mpls-wan')
        full_obj = obj.cpe_secondary_mpls_wan
    elif entity == 'cpe_tertiary_inet_triple':
        obj = getLocalObject(sdata, 'cpe-tertiary-inet-wan')
        full_obj = obj.cpe_tertiary_inet_wan
    elif entity == 'cpe_tertiary_mpls_triple':
        obj = getLocalObject(sdata, 'cpe-tertiary-mpls-wan')
        full_obj = obj.cpe_tertiary_mpls_wan

    outbound_policy = None
    class_entry = None
    hierarchical_policy = None
    if hasattr(full_obj, 'outbound_policy'):
        outbound_policy = full_obj.outbound_policy
    if hasattr(full_obj, 'hierarchical_outbound_policy'):
        hierarchical_outbound_policy = full_obj.hierarchical_outbound_policy
    if hasattr(full_obj, 'policy_name'):
        policy_name = full_obj.policy_name
    if hasattr(full_obj, 'shape_average'):
        shape_average = full_obj.shape_average
    if hasattr(full_obj, 'child_qos_policy'):
        child_qos_policy = full_obj.child_qos_policy
    if hasattr(full_obj, 'class_entry'):
        log("In class entry")
        log("class entry: %s" %(class_entry))
        class_entry = full_obj.class_entry
    if hasattr(full_obj, 'hierarchical_policy'):
        hierarchical_policy = full_obj.hierarchical_policy
    if hasattr(full_obj, 'auto_negotiation'):
        auto_negotiation = full_obj.auto_negotiation
    speed = None
    duplex = None
    if hasattr(full_obj, 'speed'):
        speed = full_obj.speed
    if hasattr(full_obj, 'duplex'):
        duplex = full_obj.duplex
    if hasattr(full_obj, 'load_interval'):
        load_interval = full_obj.load_interval
    if hasattr(full_obj, 'load_interval_delay'):
        load_interval_delay = full_obj.load_interval_delay
    if hasattr(full_obj, 'hold_queue_in'):
        hold_queue_in = full_obj.hold_queue_in
    if hasattr(full_obj, 'in_queue_length'):
        in_queue_length = full_obj.in_queue_length
    if hasattr(full_obj, 'hold_queue_out'):
        hold_queue_out = full_obj.hold_queue_out
    if hasattr(full_obj, 'out_queue_length'):
        out_queue_length = full_obj.out_queue_length

    vlan_id = None
    dmvpn_profile = inputdict['dmvpn_profile']
    tunnel_ip_address = inputdict['tunnel_interface_ip_address']
    bandwidth = inputdict['tunnel_bandwidth']
    p2p = inputdict['p2p']
    global_inbound_acl = inputdict['global_inbound_acl']
    site_inbound_acl = inputdict['site_inbound_acl']
    global_outbound_acl = inputdict['global_outbound_acl']
    site_outbound_acl = inputdict['site_outbound_acl']
    nat_inside = inputdict['nat_inside']
    nat_outside = inputdict['nat_outside']
    if interface_type == "Sub-Interface" or interface_type == "SVI":
        if '.' not in interface_name:
            vlan_id = inputdict['vlan_id']
            if util.isEmpty(vlan_id):
                raise Exception("vlan_id should not empty when interface_type is Sub-Interface or SVI")
    access_lists = []
    vrf = None
    if 'vrf' in kwargs['inputdict']:
        vrf = kwargs['inputdict']['vrf']

    if util.isEmpty(vrf) or vrf is None:
        vrf = "GLOBAL"
    if interface_type == "Sub-Interface" or interface_type == "SVI" or interface_type == "Physical":
        if entity == "cpe":
            obj = getLocalObject(sdata, 'single-cpe-site-services')
            if hasattr(obj.single_cpe_site_services.cpe, 'access_lists'):
                if hasattr(obj.single_cpe_site_services.cpe.access_lists, 'access_list'):
                    obj.single_cpe_site_services.cpe.access_lists.access_list = util.convert_to_list(obj.single_cpe_site_services.cpe.access_lists.access_list)
                    for access_list_dynamic in obj.single_cpe_site_services.cpe.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.single_cpe_site_services.wan.wan_connectivity
        elif entity == "cpe_primary":
            obj = getLocalObject(sdata, 'dual-cpe-site-services')
            if hasattr(obj.dual_cpe_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.dual_cpe_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.dual_cpe_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.dual_cpe_site_services.primary_wan.primary_wan_connectivity
        elif entity == "cpe_secondary":
            obj = getLocalObject(sdata, 'dual-cpe-site-services')
            if hasattr(obj.dual_cpe_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.dual_cpe_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.dual_cpe_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.dual_cpe_site_services.secondary_wan.secondary_wan_connectivity
        elif entity == "cpe_primary_dual":
            obj = getLocalObject(sdata, 'single-cpe-dual-wan-site-services')
            if hasattr(obj.single_cpe_dual_wan_site_services.cpe, 'access_lists'):
                if hasattr(obj.single_cpe_dual_wan_site_services.cpe.access_lists, 'access_list'):
                    obj.single_cpe_dual_wan_site_services.cpe.access_lists.access_list = util.convert_to_list(obj.single_cpe_dual_wan_site_services.cpe.access_lists.access_list)
                    for access_list_dynamic in obj.single_cpe_dual_wan_site_services.cpe.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.single_cpe_dual_wan_site_services.primary_wan.primary_wan_connectivity
        elif entity == "cpe_secondary_dual":
            obj = getLocalObject(sdata, 'single-cpe-dual-wan-site-services')
            if hasattr(obj.single_cpe_dual_wan_site_services.cpe, 'access_lists'):
                if hasattr(obj.single_cpe_dual_wan_site_services.cpe.access_lists, 'access_list'):
                    obj.single_cpe_dual_wan_site_services.cpe.access_lists.access_list = util.convert_to_list(obj.single_cpe_dual_wan_site_services.cpe.access_lists.access_list)
                    for access_list_dynamic in obj.single_cpe_dual_wan_site_services.cpe.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.single_cpe_dual_wan_site_services.secondary_wan.secondary_wan_connectivity
        elif entity == "cpe_primary_inet_dual":
            obj = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
            if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.dual_cpe_dual_wan_site_services.primary_inet_wan.primary_inet_wan_connectivity
        elif entity == "cpe_primary_mpls_dual":
            obj = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
            if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.dual_cpe_dual_wan_site_services.primary_mpls_wan.primary_mpls_wan_connectivity
        elif entity == "cpe_secondary_inet_dual":
            obj = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
            if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.dual_cpe_dual_wan_site_services.secondary_inet_wan.secondary_inet_wan_connectivity
        elif entity == "cpe_secondary_mpls_dual":
            obj = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
            if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.dual_cpe_dual_wan_site_services.secondary_mpls_wan.secondary_mpls_wan_connectivity
        elif entity == "cpe_primary_inet_triple":
            obj = getLocalObject(sdata, 'triple-cpe-site-services')
            if hasattr(obj.triple_cpe_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.triple_cpe_site_services.primary_inet_wan.primary_inet_wan_connectivity
        elif entity == "cpe_primary_mpls_triple":
            obj = getLocalObject(sdata, 'triple-cpe-site-services')
            if hasattr(obj.triple_cpe_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.triple_cpe_site_services.primary_mpls_wan.primary_mpls_wan_connectivity
        elif entity == "cpe_secondary_inet_triple":
            obj = getLocalObject(sdata, 'triple-cpe-site-services')
            if hasattr(obj.triple_cpe_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.triple_cpe_site_services.secondary_inet_wan.secondary_inet_wan_connectivity
        elif entity == "cpe_secondary_mpls_triple":
            obj = getLocalObject(sdata, 'triple-cpe-site-services')
            if hasattr(obj.triple_cpe_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.triple_cpe_site_services.secondary_mpls_wan.secondary_mpls_wan_connectivity
        elif entity == "cpe_tertiary_inet_triple":
            obj = getLocalObject(sdata, 'triple-cpe-site-services')
            if hasattr(obj.triple_cpe_site_services.cpe_tertiary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_tertiary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_tertiary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_tertiary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_tertiary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.triple_cpe_site_services.tertiary_inet_wan.tertiary_inet_wan_connectivity
        elif entity == "cpe_tertiary_mpls_triple":
            obj = getLocalObject(sdata, 'triple-cpe-site-services')
            if hasattr(obj.triple_cpe_site_services.cpe_tertiary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_tertiary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_tertiary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_tertiary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_tertiary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
            entity_obj = obj.triple_cpe_site_services.tertiary_mpls_wan.tertiary_mpls_wan_connectivity

        mode = "None"
        if hierarchical_outbound_policy == 'true':
            device.addQosPolicyMapsContainer(sdata.getSession())
            class_entry = 'false'
            if class_entry == 'false':
                if util.isNotEmpty(policy_name):
                    map_obj = devices.device.policy_maps.policy_map.policy_map()
                    map_obj.name = policy_name
                    yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession())

                    cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
                    cls_obj.class_name = 'class-default'
                    if util.isNotEmpty(shape_average):
                        cls_obj.shape_average = shape_average
                    if util.isNotEmpty(child_qos_policy):
                        cls_obj.service_policy = child_qos_policy
                        qos_child(entity, child_qos_policy, device, sdata)
                    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s" %(policy_name), cls_obj.getxml(filter=True), sdata.getSession())
            elif class_entry == 'true':
                if util.isNotEmpty(hierarchical_policy):
                    hierarchical_policy_class(entity, hierarchical_policy, device, sdata)
        link_negotiation = None
        if util.isNotEmpty(outbound_policy):
            qos_child(entity, outbound_policy, device, sdata)

        if interface_type == "Physical" or interface_type == "Sub-Interface":
            if util.isEmpty(interface_name):
                raise Exception("interface_name should not be empty when interface_type is Physical and sub-interface")
        int_name_phy = interface_name
        if interface_type == "Physical":
            mode = "l3-interface"
        elif interface_type == "Sub-Interface":
            mode = "sub-interface"
            if vlan_id is not None:
                interface_name = interface_name + '.' + str(vlan_id)
        elif interface_type == "SVI":
            mode = "vlan"
        if auto_negotiation == "true":
            link_negotiation = "auto"

        intf_obj = devices.device.interfaces.interface.interface()
        if mode == "sub-interface" or mode == "l3-interface":
            intf_obj.name = interface_name
            intf_obj.long_name = interface_name
        intf_obj.description = interface_description

        if nat_inside == 'true':
            intf_obj.nat_name = 'inside'
        if nat_outside == 'true':
            intf_obj.nat_name = 'outside'


        if mode == "sub-interface":
            if not device.isInterfaceInDeviceExists(interface_name):
                intf_obj.mode = "sub-interface"
                intf_obj.vlan = vlan_id
        elif mode == "vlan":
            intf_obj.mode = "vlan"
            intf_obj.vlan = vlan_id
            intf_obj.long_name = "Vlan" + str(vlan_id)
            intf_obj.name = "Vlan" + str(vlan_id)
        else:
            intf_obj.mode = "l3-interface"
        if mode == "sub-interface" or mode == "l3-interface":
            if vrf is not None and vrf != 'GLOBAL':
                uri = sdata.getRcPath()
                uri_list = uri.split('/', 5)
                url = '/'.join(uri_list[0:4])
                xml_output = yang.Sdk.getData(url+"/vrfs/vrf="+str(vrf), '', sdata.getTaskId())
                obj_local = util.parseXmlString(xml_output)
                util.log_debug("obj_local: ", obj_local)
                intf_obj.vrf_definition_mode = obj_local.vrf.vrf_definition_mode
                intf_obj.vrf = vrf
            if util.isNotEmpty(outbound_policy):
                intf_obj.outbound_qos = outbound_policy
            if hierarchical_outbound_policy == 'true':
                if class_entry == 'false':
                    if util.isNotEmpty(policy_name):
                        intf_obj.outbound_qos = policy_name
                elif class_entry == 'true':
                    if util.isNotEmpty(hierarchical_policy):
                        intf_obj.outbound_qos = hierarchical_policy
            uri = sdata.getRcPath()
            uri_list = uri.split('/',5)
            url = '/'.join(uri_list[0:4])
            if util.isNotEmpty(global_inbound_acl):
                access_group_def(url, global_inbound_acl, device, sdata)
                intf_obj.acl_inbound_name = global_inbound_acl
            if util.isNotEmpty(global_outbound_acl):
                access_group_def(url, global_outbound_acl, device, sdata)
                intf_obj.acl_outbound_name = global_outbound_acl
            if util.isNotEmpty(site_inbound_acl):
                if site_inbound_acl in access_lists:
                    intf_obj.acl_inbound_name = site_inbound_acl
                else:
                    raise Exception("Make sure that provided site_inbound_acl should be present on router access-lists")
            if util.isNotEmpty(site_outbound_acl):
                if site_outbound_acl in access_lists:
                    intf_obj.acl_outbound_name = site_outbound_acl
                else:
                    raise Exception("Make sure that provided site_outbound_acl should be present on router access-lists")
        if interface_type == "Physical":
            if link_negotiation is not None:
                intf_obj.link_negotiation = link_negotiation

            if nat_inside == 'true':
                intf_obj.nat_name = 'inside'
            if nat_outside == 'true':
                intf_obj.nat_name = 'outside'
                
            if auto_negotiation != "true":
                if util.isNotEmpty(speed):
                    intf_obj.speed = speed
                if util.isNotEmpty(duplex):
                    intf_obj.duplex = duplex
            if load_interval == 'true':
                if util.isNotEmpty(load_interval_delay):
                    intf_obj.load_interval_delay = load_interval_delay
            if hold_queue_in == 'true':
                if util.isNotEmpty(in_queue_length):
                    intf_obj.in_queue_length = in_queue_length
            if hold_queue_out == 'true':
                if util.isNotEmpty(out_queue_length):
                    intf_obj.out_queue_length = out_queue_length
            yang.Sdk.createData(device.url+'/interfaces', intf_obj.getxml(filter=True), sdata.getSession(), False)
        else:
            yang.Sdk.createData(device.url+'/interfaces', intf_obj.getxml(filter=True), sdata.getSession(), False)

        if mode == "sub-interface":
            intf_obj_phy = devices.device.interfaces.interface.interface()
            intf_obj_phy.name = int_name_phy
            intf_obj_phy.long_name = int_name_phy
            intf_obj_phy.mode = "l3-interface"
            if link_negotiation is not None:
                intf_obj_phy.link_negotiation = link_negotiation
            if auto_negotiation != "true":
                if util.isNotEmpty(speed):
                    intf_obj_phy.speed = speed
                if util.isNotEmpty(duplex):
                    intf_obj_phy.duplex = duplex
            if load_interval == 'true':
                if util.isNotEmpty(load_interval_delay):
                    intf_obj_phy.load_interval_delay = load_interval_delay
            if hold_queue_in == 'true':
                if util.isNotEmpty(in_queue_length):
                    intf_obj_phy.in_queue_length = in_queue_length
            if hold_queue_out == 'true':
                if util.isNotEmpty(out_queue_length):
                    intf_obj_phy.out_queue_length = out_queue_length
            yang.Sdk.createData(device.url+'/interfaces', intf_obj_phy.getxml(filter=True), sdata.getSession(), False)

    if interface_type == "Tunnel":
        # if util.isEmpty(dmvpn_profile):
        #     raise Exception("dmvpn_profile should not be empty when interface_type is Tunnel")
        fvrf = None
        ivrf = None
        if 'fvrf' in kwargs['inputdict']:
            fvrf = kwargs['inputdict']['fvrf']

        if 'ivrf' in kwargs['inputdict']:
            ivrf = kwargs['inputdict']['ivrf']

        if util.isEmpty(fvrf) or fvrf is None:
            fvrf = "GLOBAL"

        present = None
        vrf_url = '/app/restconf/data/controller:devices/device=%s/l3features:vrfs'% str(device.device.id)
        xml_output = yang.Sdk.getData(vrf_url, '', sdata.getTaskId())
        obj = util.parseXmlString(xml_output)
        util.log_debug( "obj: ", obj)
        if hasattr(obj.vrfs, 'vrf'):
            obj.vrfs.vrf = util.convert_to_list(obj.vrfs.vrf)
            for vrf in obj.vrfs.vrf:
                if vrf.name == fvrf:
                    present = 'yes'
        if present is None and fvrf != 'GLOBAL':
            raise Exception('FVRF not configured as part of Day 0')
        if util.isEmpty(ivrf) or ivrf is None:
            ivrf = "GLOBAL"

        if entity == 'cpe':
            obj = getLocalObject(sdata, 'cpe-wan')
            obj = util.convert_to_list(obj.cpe_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_primary':
            obj = getLocalObject(sdata, 'cpe-primary-wan')
            obj = util.convert_to_list(obj.cpe_primary_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_secondary':
            obj = getLocalObject(sdata, 'cpe-secondary-wan')
            obj = util.convert_to_list(obj.cpe_secondary_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_primary_dual':
            obj = getLocalObject(sdata, 'cpe-primary-wan')
            obj = util.convert_to_list(obj.cpe_primary_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_secondary_dual':
            obj = getLocalObject(sdata, 'cpe-secondary-wan')
            obj = util.convert_to_list(obj.cpe_secondary_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_primary_inet_dual':
            obj = getLocalObject(sdata, 'cpe-primary-inet-wan')
            obj = util.convert_to_list(obj.cpe_primary_inet_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_primary_mpls_dual':
            obj = getLocalObject(sdata, 'cpe-primary-mpls-wan')
            obj = util.convert_to_list(obj.cpe_primary_mpls_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_secondary_inet_dual':
            obj = getLocalObject(sdata, 'cpe-secondary-inet-wan')
            obj = util.convert_to_list(obj.cpe_secondary_inet_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_secondary_mpls_dual':
            obj = getLocalObject(sdata, 'cpe-secondary-mpls-wan')
            obj = util.convert_to_list(obj.cpe_secondary_mpls_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_primary_inet_triple':
            obj = getLocalObject(sdata, 'cpe-primary-inet-wan')
            obj = util.convert_to_list(obj.cpe_primary_inet_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_primary_mpls_triple':
            obj = getLocalObject(sdata, 'cpe-primary-mpls-wan')
            obj = util.convert_to_list(obj.cpe_primary_mpls_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_secondary_inet_triple':
            obj = getLocalObject(sdata, 'cpe-secondary-inet-wan')
            obj = util.convert_to_list(obj.cpe_secondary_inet_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_secondary_mpls_triple':
            obj = getLocalObject(sdata, 'cpe-secondary-mpls-wan')
            obj = util.convert_to_list(obj.cpe_secondary_mpls_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_tertiary_inet_triple':
            obj = getLocalObject(sdata, 'cpe-tertiary-inet-wan')
            obj = util.convert_to_list(obj.cpe_tertiary_inet_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name
        elif entity == 'cpe_tertiary_mpls_triple':
            obj = getLocalObject(sdata, 'cpe-tertiary-mpls-wan')
            obj = util.convert_to_list(obj.cpe_tertiary_mpls_wan.end_points)
            for endpoint in obj:
                if endpoint.interface_type == "Sub-Interface":
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if endpoint.interface_type == "Physical":
                    interface_name = endpoint.interface_name

        uri = sdata.getRcPath()
        uri_list = uri.split('/', 5)
        url = '/'.join(uri_list[0:4])

        if util.isNotEmpty(dmvpn_profile):
            xml_output = yang.Sdk.getData(url+"/dmvpn-tunnel-profiles/dmvpn-tunnel-profile="+str(dmvpn_profile), '', sdata.getTaskId())
            obj = util.parseXmlString(xml_output)
            util.log_debug( "obj: ", obj)
            #if util.isNotEmpty(dmvpn_profile):
                #yang.Sdk.createData(device.url, '<dmvpntunnels/>', sdata.getSession(), False)
            dmvpn_obj = devices.device.dmvpntunnels.dmvpntunnel.dmvpntunnel()
            if util.isNotEmpty(fvrf) and fvrf != 'GLOBAL':
                dmvpn_obj.front_vrf_name = fvrf
        else:
            tunnel_mask = inputdict['tunnel_interface_mask']
            tunnel_id = inputdict['tunnel_interface_id']
            tunnel_destination = inputdict['tunnel_interface_destination']
            if util.isEmpty(tunnel_id):
                 raise Exception("Tunnel id should not be empty when interface_type is Tunnel & dmvpn profile is not selected")

            #yang.Sdk.createData(device.url, '<dmvpntunnels/>', sdata.getSession(), False)
            dmvpn_obj = devices.device.dmvpntunnels.dmvpntunnel.dmvpntunnel()
            if util.isNotEmpty(fvrf) and fvrf != 'GLOBAL':
                dmvpn_obj.front_vrf_name = fvrf
            dmvpn_obj.name = tunnel_id
            dmvpn_obj.description = interface_description
            dmvpn_obj.tcp_adjust_mss = "1300"
            dmvpn_obj.ipaddress = tunnel_ip_address
            dmvpn_obj.netmask = tunnel_mask
            dmvpn_obj.tunnel_destination = tunnel_destination
            #dmvpn_obj.tunnel_mode = 'gre'
            dmvpn_obj.tunnel_keepalive_period = '10'
            dmvpn_obj.tunnel_keepalive_retries = '3'
            tunnel_source = inputdict['tunnel_source']
            if util.isNotEmpty(tunnel_source):
                dmvpn_obj.tunnel_source = tunnel_source
            else:
                dmvpn_obj.tunnel_source = interface_name
            if util.isNotEmpty(bandwidth):
                dmvpn_obj.bandwidth = bandwidth
            yang.Sdk.createData(device.url+'/dmvpntunnels', dmvpn_obj.getxml(filter=True), sdata.getSession())
            return

        if hasattr(obj.dmvpn_tunnel_profile, 'delay'):
            delay = obj.dmvpn_tunnel_profile.delay
        else:
            delay = None
        if delay is not None:
            dmvpn_obj.delay = delay

        if hasattr(obj.dmvpn_tunnel_profile, 'no_nhrp_route_watch'):
            no_nhrp_route_watch = obj.dmvpn_tunnel_profile.no_nhrp_route_watch
        else:
            no_nhrp_route_watch = None
        if no_nhrp_route_watch is not None:
            dmvpn_obj.no_nhrp_route_watch = no_nhrp_route_watch

        if hasattr(obj.dmvpn_tunnel_profile, 'nhrp_reg_no_uniq'):
            nhrp_reg_no_uniq = obj.dmvpn_tunnel_profile.nhrp_reg_no_uniq
        else:
            nhrp_reg_no_uniq = None
        if nhrp_reg_no_uniq is not None:
            dmvpn_obj.nhrp_reg_no_uniq = nhrp_reg_no_uniq

        if hasattr(obj.dmvpn_tunnel_profile, 'nhrp_reg_timeout'):
            nhrp_reg_timeout = obj.dmvpn_tunnel_profile.nhrp_reg_timeout
        else:
            nhrp_reg_timeout = None
        if nhrp_reg_timeout is not None:
            dmvpn_obj.nhrp_reg_timeout = nhrp_reg_timeout

        if hasattr(obj.dmvpn_tunnel_profile, 'nhrp_holdtime'):
            nhrp_holdtime = obj.dmvpn_tunnel_profile.nhrp_holdtime
        else:
            nhrp_holdtime = None
        if nhrp_holdtime is not None:
            dmvpn_obj.nhrp_holdtime = nhrp_holdtime

        if hasattr(obj.dmvpn_tunnel_profile, 'nhrp_redirect'):
            nhrp_redirect = obj.dmvpn_tunnel_profile.nhrp_redirect
        else:
            nhrp_redirect = None
        if nhrp_redirect is not None:
            dmvpn_obj.nhrp_redirect = nhrp_redirect

        if hasattr(obj.dmvpn_tunnel_profile, 'nhrp_shortcut'):
            nhrp_shortcut = obj.dmvpn_tunnel_profile.nhrp_shortcut
        else:
            nhrp_shortcut = None
        if nhrp_shortcut is not None:
            dmvpn_obj.nhrp_shortcut = nhrp_shortcut

        if hasattr(obj.dmvpn_tunnel_profile, 'tunnel_keepalive_period'):
            tunnel_keepalive_period = obj.dmvpn_tunnel_profile.tunnel_keepalive_period
        else:
            tunnel_keepalive_period = None
        if tunnel_keepalive_period is not None:
            dmvpn_obj.tunnel_keepalive_period = tunnel_keepalive_period

        if hasattr(obj.dmvpn_tunnel_profile, 'tunnel_keepalive_retries'):
            tunnel_keepalive_retries = obj.dmvpn_tunnel_profile.tunnel_keepalive_retries
        else:
            tunnel_keepalive_retries = None
        if tunnel_keepalive_retries is not None:
            dmvpn_obj.tunnel_keepalive_retries = tunnel_keepalive_retries

        if ivrf != 'GLOBAL':
            uri = sdata.getRcPath()
            uri_list = uri.split('/', 5)
            url = '/'.join(uri_list[0:4])
            xml_output = yang.Sdk.getData(url+"/vrfs/vrf="+str(ivrf), '', sdata.getTaskId())
            obj_local = util.parseXmlString(xml_output)
            util.log_debug("obj_local: ", obj_local)
            dmvpn_obj.vrf_definition_mode = obj_local.vrf.vrf_definition_mode
            dmvpn_obj.vrf_name = ivrf
        if p2p == 'true':
            dmvpn_obj.tunnel_destination = obj.dmvpn_tunnel_profile.wan_public_ip
        else:
            dmvpn_obj.tunnel_mode = 'gre'
        if util.isNotEmpty(bandwidth):
            dmvpn_obj.bandwidth = bandwidth
        dmvpn_obj.type = "SPOKE"
        dmvpn_obj.name = obj.dmvpn_tunnel_profile.tunnel_id
        dmvpn_obj.nhrp_auth_key = obj.dmvpn_tunnel_profile.nhrp_authentication_key
        dmvpn_obj.nhrp_network_id = obj.dmvpn_tunnel_profile.nhrp_nw_id
        dmvpn_obj.tunnel_key = obj.dmvpn_tunnel_profile.tunnel_key
        dmvpn_obj.description = interface_description
        if hasattr(obj.dmvpn_tunnel_profile, 'mtu'):
            mtu = obj.dmvpn_tunnel_profile.mtu
        else:
            mtu = None
        if util.isNotEmpty(mtu):
            dmvpn_obj.mtu = mtu
        else:
            dmvpn_obj.mtu = "1400"
        if hasattr(obj.dmvpn_tunnel_profile, 'tcp_adjust_mss'):
            tcp_adjust_mss = obj.dmvpn_tunnel_profile.tcp_adjust_mss
        else:
            tcp_adjust_mss = None
        if util.isNotEmpty(tcp_adjust_mss):
            dmvpn_obj.tcp_adjust_mss = tcp_adjust_mss
        else:
            dmvpn_obj.tcp_adjust_mss = "1360"

        ip_addr = IpamPoolID(sdata.getTaskId(), sdata, obj.dmvpn_tunnel_profile.tunnel_prefix)
        ip_addr_obj = ip_addr.ipam_pool_obj
        if util.isEmpty(tunnel_ip_address):
            used_ips_list = get_used_ip_list_from_ippool(ip_addr_obj.name, sdata)
            tunnel_ip_address = get_freeip_from_cidr(ip_addr_obj.cidr, used_ips_list)
            add_ipaddress_entries(ip_addr_obj.name, tunnel_ip_address, sdata)
        else:
            add_ipaddress_entries(ip_addr_obj.name, tunnel_ip_address, sdata)

        if obj.dmvpn_tunnel_profile.wan_public_ip == tunnel_ip_address:
            add_ipaddress_entries(ip_addr_obj.name, tunnel_ip_address, sdata)
        dmvpn_obj.ipaddress = tunnel_ip_address

        payload = "<tunnel-interface-ip-address>%s</tunnel-interface-ip-address>" % tunnel_ip_address
        serv_uri = sdata.getRcPath()
        yang.Sdk.createData(serv_uri, payload, sdata.getSession(), False)

        tunnel_prefix = ip_addr_obj.cidr
        netmask = util.IPPrefix(tunnel_prefix).netmask
        dmvpn_obj.netmask = netmask
        tunnel_source = inputdict['tunnel_source']
        if util.isNotEmpty(tunnel_source):
            dmvpn_obj.tunnel_source = tunnel_source
        else:
            dmvpn_obj.tunnel_source = interface_name
        if hasattr(obj.dmvpn_tunnel_profile, 'ipsec_profile'):
            ipsecProfileSelected = obj.dmvpn_tunnel_profile.ipsec_profile
            IpsecCreation(sdata, device, ipsecProfileSelected, fvrf, obj.dmvpn_tunnel_profile.wan_public_ip, smodelctx)
            dmvpn_obj.ipsec_profile_name = obj.dmvpn_tunnel_profile.ipsec_profile
            xml_output = yang.Sdk.getData(url+"/ipsec/ipsec-profiles/ipsec-profile="+str(obj.dmvpn_tunnel_profile.ipsec_profile), '', sdata.getTaskId())
            obj1 = util.parseXmlString(xml_output)
            dmvpn_obj.shared = obj1.ipsec_profile.get_field_value('shared')

        # adding nhrp-maps
        nhrp_maps_obj_2 = dmvpn_obj.nhrp_maps.add(sourceip=obj.dmvpn_tunnel_profile.wan_tunnel_ip, destip=obj.dmvpn_tunnel_profile.wan_public_ip)
        nhrp_maps_obj_2.nhrp_type = 'nhs'
        yang.Sdk.createData(device.url+'/dmvpntunnels', dmvpn_obj.getxml(filter=True), sdata.getSession())
        if hasattr(obj.dmvpn_tunnel_profile, 'nhrp_maps'):
            dmvpn_obj_nhrp = devices.device.dmvpntunnels.dmvpntunnel.nhrp_maps.nhrp_maps()
            obj.dmvpn_tunnel_profile.nhrp_maps = util.convert_to_list(obj.dmvpn_tunnel_profile.nhrp_maps)
            for nhrpmaps in obj.dmvpn_tunnel_profile.nhrp_maps:
                dmvpn_obj_nhrp.sourceip = nhrpmaps.wan_tunnel_ip
                dmvpn_obj_nhrp.nhrp_type = 'nhs'
                dmvpn_obj_nhrp.destip = nhrpmaps.wan_public_ip
                yang.Sdk.createData(device.url+'/dmvpntunnels/dmvpntunnel=%s' % (obj.dmvpn_tunnel_profile.tunnel_id), dmvpn_obj_nhrp.getxml(filter=True), sdata.getSession())


def IpsecCreation(sdata, device, ipsecProfileSelected, fvrf, wan_public_ip, smodelctx):
    obj = getLocalObject(sdata, 'customer')
    ike_profile_name = None
    crpto_type = None
    key_ring_name = None
    pre_shared_secret = None
    vrf_name = None
    crypto_profile_selection = None
    transform_set_selection = None

    transform_set = None
    ipsec_encryption_type = None
    ipsec_authentication_type = None
    ike_encryption_type = None
    hash1 = None
    group = None
    life_time = None
    policy_number = None

    if hasattr(obj.customer.ipsec.ipsec_profiles, 'ipsec_profile'):
        obj.customer.ipsec.ipsec_profiles.ipsec_profile = util.convert_to_list(obj.customer.ipsec.ipsec_profiles.ipsec_profile)
        for ipsec_profile_dynamic in obj.customer.ipsec.ipsec_profiles.ipsec_profile:
            if ipsec_profile_dynamic.get_field_value('ipsec_profile_name') == ipsecProfileSelected:
                transform_set_selection = ipsec_profile_dynamic.get_field_value('transform_set')
                if transform_set_selection is None:
                    raise Exception('[INFO] Transform set in ipsec profile is empty')
                crypto_profile_selection = ipsec_profile_dynamic.get_field_value('crypto_profile')
                if crypto_profile_selection is None:
                    raise Exception('[INFO] Crypto profile in ipsec profile is empty')
                sa_lifetime = ipsec_profile_dynamic.get_field_value('sa_lifetime')

    if hasattr(obj.customer.ipsec.crypto_profiles, 'crypto_profile'):
        obj.customer.ipsec.crypto_profiles.crypto_profile = util.convert_to_list(obj.customer.ipsec.crypto_profiles.crypto_profile)
        for crypto_profile_dynamic in obj.customer.ipsec.crypto_profiles.crypto_profile:
            if crypto_profile_dynamic.get_field_value('crypto_profile_name') == crypto_profile_selection:
                ike_profile_name = crypto_profile_dynamic.get_field_value('crypto_profile_name')
                if ike_profile_name is None:
                    raise Exception('[INFO] Crypto profile in crypto profile is empty')
                crpto_type = crypto_profile_dynamic.get_field_value('crypto_type')
                key_ring_name = crypto_profile_dynamic.get_field_value('keyring')
                allow_all = crypto_profile_dynamic.get_field_value('allow_all')
                pre_shared_secret = crypto_profile_dynamic.get_field_value('pre_shared_key')
                vrf_name = crypto_profile_dynamic.get_field_value('vrf')
                ike_encryption_type = crypto_profile_dynamic.get_field_value('encryption')
                hash1 = crypto_profile_dynamic.get_field_value('authentication')
                group = crypto_profile_dynamic.get_field_value('group')
                life_time = crypto_profile_dynamic.get_field_value('life_time')
                policy_number = crypto_profile_dynamic.get_field_value('policy_number')
                auth_type = crypto_profile_dynamic.get_field_value('auth_type')

    if hasattr(obj.customer.ipsec.transform_sets, 'transform_set'):
        obj.customer.ipsec.transform_sets.transform_set = util.convert_to_list(obj.customer.ipsec.transform_sets.transform_set)
        for transform_set_dynamic in obj.customer.ipsec.transform_sets.transform_set:
            if transform_set_dynamic.get_field_value('transform_set_name') == transform_set_selection:
                transform_set = transform_set_dynamic.get_field_value('transform_set_name')
                if transform_set is None:
                    raise Exception('[INFO] Transform set in transform set is empty')
                ipsec_encryption_type = transform_set_dynamic.get_field_value('encryption')
                ipsec_authentication_type = transform_set_dynamic.get_field_value('authentication')
                mode = transform_set_dynamic.get_field_value('mode')
    if allow_all == "true":
        ipaddress = '0.0.0.0'
        netmask = '0.0.0.0'
    else:
        ipaddress = wan_public_ip
        netmask = '255.255.255.255'
    keyring_payload = devices.device.crypto_keyrings.crypto_keyring.crypto_keyring()
    keyring_payload.key_ring_name = key_ring_name
    keyring_payload.ike_version = crpto_type
    #keyring_payload.auth_type = auth_type
    if vrf_name is not None and vrf_name == fvrf:
        keyring_payload.vrf_name = vrf_name
    #keyring_payload.pre_shared_key.add(ip_address=ipaddress, netmask=netmask, pre_shared_secret=pre_shared_secret)
    pre_shared_obj = keyring_payload.pre_shared_key.add(ip_address=ipaddress)
    #pre_shared_obj.netmask = netmask
    pre_shared_obj.pre_shared_secret = pre_shared_secret
    yang.Sdk.createData(device.url, '<crypto-keyrings/>', sdata.getSession())
    yang.Sdk.createData(device.url+'/crypto-keyrings', keyring_payload.getxml(filter=True), sdata.getSession())

    policy_payload = devices.device.crypto_policies.crypto_policy.crypto_policy()
    policy_payload.policy_number = policy_number
    policy_payload.ike_version = crpto_type
    policy_payload.auth_type = auth_type
    policy_payload.ike_encryption_type = ike_encryption_type
    policy_payload.hash = hash1
    policy_payload.group = group
    policy_payload.life_time = life_time
    yang.Sdk.createData(device.url, '<crypto-policies/>', sdata.getSession())
    yang.Sdk.createData(device.url+'/crypto-policies', policy_payload.getxml(filter=True), sdata.getSession())

    profile_payload = devices.device.crypto.crypto_profile.crypto_profile()
    profile_payload.ike_profile_name = ike_profile_name
    profile_payload.life_time = life_time
    profile_payload.ike_version = crpto_type
    profile_payload.key_ring_name = key_ring_name
    if crpto_type == 'IKEV2':
        profile_payload.auth_type = auth_type
    profile_match = profile_payload.match.add(ip_address=ipaddress)
    if vrf_name is not None and vrf_name == fvrf:
        profile_match.vrf_name = vrf_name
    yang.Sdk.createData(device.url, '<crypto/>', sdata.getSession())
    yang.Sdk.createData(device.url+'/crypto', profile_payload.getxml(filter=True), sdata.getSession())

    transform_payload = devices.device.transform_sets.transform_set.transform_set()
    transform_payload.transform_set = transform_set
    transform_payload.ipsec_encryption_type = ipsec_encryption_type
    transform_payload.ipsec_authentication_type = ipsec_authentication_type
    transform_payload.mode = mode
    yang.Sdk.createData(device.url, '<transform-sets/>', sdata.getSession())
    yang.Sdk.createData(device.url+'/transform-sets', transform_payload.getxml(filter=True), sdata.getSession())

    ipsec_payload = devices.device.ipsec_profiles.ipsec_profile.ipsec_profile()
    ipsec_payload.ipsec_profile_name = ipsecProfileSelected
    if util.isNotEmpty(sa_lifetime):
        ipsec_payload.life_time = sa_lifetime
    ipsec_payload.transform_set = transform_set
    ipsec_payload.ike_profile_name = ike_profile_name
    ipsec_payload.ike_version = crpto_type
    yang.Sdk.createData(device.url, '<ipsec-profiles/>', sdata.getSession())
    yang.Sdk.createData(device.url+'/ipsec-profiles', ipsec_payload.getxml(filter=True), sdata.getSession())


def hierarchical_policy_class(entity, hierarchical_policy, device, sdata):
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])

    xml_output = yang.Sdk.getData(url+"/qos-service/hierarchical-policy/policy="+str(hierarchical_policy), '',sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    util.log_debug( "obj: ",obj)
    device.addQosPolicyMapsContainer(sdata.getSession())

    map_obj = devices.device.policy_maps.policy_map.policy_map()
    map_obj.name = obj.policy.name
    yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession())

    if hasattr(obj.policy, 'classes'):
        obj.policy.classes = util.convert_to_list(obj.policy.classes)
        log("classes sequence:%s" %(obj.policy.classes))
        for class_entry in obj.policy.classes:
            cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            if util.isNotEmpty(class_entry.class_name):
                class_map(entity, url, class_entry.class_name, device, sdata)
                cls_obj.class_name = class_entry.class_name
            if util.isNotEmpty(class_entry.child_qos_policy):
                cls_obj.service_policy = class_entry.child_qos_policy
                qos_child(entity, class_entry.child_qos_policy, device, sdata)
            yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s" %(obj.policy.name), cls_obj.getxml(filter=True), sdata.getSession())


def qos_child(entity, qos_policy, dev, sdata):
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])

    xml_output = yang.Sdk.getData(url+"/qos-service/policies/policy="+str(qos_policy), '',sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    util.log_debug( "obj: ",obj)
    dev.addQosPolicyMapsContainer(sdata.getSession())
    policy_name = obj.policy.name
    map_obj = devices.device.policy_maps.policy_map.policy_map()
    map_obj.name = policy_name
    yang.Sdk.createData(dev.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession())
    for cls in sorted(obj.policy.classes.get_field_value('class_name', True), key=attrgetter('name')):
        cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
        cls_name = cls.name
        # Generates Configs for Class Maps
        if cls_name != 'class-default' and cls_name != 'CLASS-DEFAULT':
            class_map(entity, url, cls_name, dev, sdata)
            cls_obj.class_name = cls_name
        else:
            cls_obj.class_name = 'class-default'
        packet_handling = cls.get_field_value('packet_handling')
        print "packet_handling: ",packet_handling
        if packet_handling is not None and hasattr(packet_handling,"remarking") and packet_handling.remarking is not None:
            print "remarking: ",packet_handling.remarking
            remarking = packet_handling.remarking
            dscp_tunnel = remarking.get_field_value("dscp_tunnel")
            if util.isNotEmpty(dscp_tunnel):
                cls_obj.is_dscp_tunnel = dscp_tunnel
            mark_dscp = remarking.get_field_value("mark_dscp")
            if util.isNotEmpty(mark_dscp):
                cls_obj.dscp_value = mark_dscp
        if packet_handling is not None and hasattr(packet_handling,"bandwidth") and packet_handling.bandwidth is not None:
            print "bandwidth: ",packet_handling.bandwidth
            bandwidth = packet_handling.bandwidth
            rate_percentage = bandwidth.get_field_value("rate_percentage")
            if util.isNotEmpty(rate_percentage):
                cls_obj.bandwidth_remaining_percentage = rate_percentage
            percentage = bandwidth.get_field_value("percentage")
            if util.isNotEmpty(percentage):
                cls_obj.bandwidth_percentage = percentage
            bandwidth_remaining_ratio = bandwidth.get_field_value("bandwidth_remaining_ratio")
            if util.isNotEmpty(bandwidth_remaining_ratio):
                cls_obj.bandwidth_remaining_ratio = bandwidth_remaining_ratio
            if hasattr(bandwidth,"random_detect") and bandwidth.random_detect is not None:
                print "random_detect: ",bandwidth.random_detect
                random_detect = bandwidth.random_detect
                random_detect_value = random_detect.get_field_value("random_detect")
                if util.isNotEmpty(random_detect_value):
                    cls_obj.random_detect = random_detect_value
        if packet_handling is not None and hasattr(packet_handling,"priority") and packet_handling.priority is not None:
            print "priority: ",packet_handling.priority
            priority_value = packet_handling.priority.get_field_value("bandwidth_rate")
            if util.isNotEmpty(priority_value):
                cls_obj.priority_value = priority_value
            priority_percentage = packet_handling.priority.get_field_value("percentage")
            if util.isNotEmpty(priority_percentage):
                cls_obj.priority_percentage = priority_percentage
            priority_level = packet_handling.priority.get_field_value("priority_level")
            if util.isNotEmpty(priority_level):
                cls_obj.priority_level = priority_level
        if packet_handling is not None and hasattr(packet_handling,"police") and packet_handling.police is not None:
            print "police: ",packet_handling.police
            police = packet_handling.police
            bit_rate = packet_handling.police.get_field_value("bit_rate")
            bit_rate_percent = packet_handling.police.get_field_value("bit_rate_percent")
            if util.isNotEmpty(bit_rate):
                cls_obj.bit_rate = bit_rate
            if util.isNotEmpty(bit_rate_percent):
                cls_obj.bit_rate_percent = bit_rate_percent
            police_cir_percentage = packet_handling.police.get_field_value("police_cir_percentage")
            if util.isNotEmpty(police_cir_percentage):
                cls_obj.police_cir_percentage = police_cir_percentage
        yang.Sdk.createData(dev.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession())

        if cls.get_field_value('queue_limit') is not None:
            queue_limit_obj = devices.device.policy_maps.policy_map.class_entry.queue_limit.queue_limit()
            queue_limit = cls.queue_limit.get_field_value('queue_limit')
            packets = cls.queue_limit.get_field_value('packets')
            if util.isNotEmpty(queue_limit):
                queue_limit_obj.queue_limit = queue_limit
                queue_limit_obj.packet = packets

            yang.Sdk.createData(dev.url+"/policy-maps/policy-map=%s/class-entry=%s"%(policy_name,cls_name), queue_limit_obj.getxml(filter=True), sdata.getSession())

        if cls.get_field_value('qos_group') is not None:
            #qos_group_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
            qos_group_value = cls.qos_group.get_field_value('qos_group')
            if util.isNotEmpty(qos_group_value):
                cls_obj.qos_group = qos_group_value

            yang.Sdk.createData(dev.url+"/policy-maps/policy-map=%s"%(policy_name), cls_obj.getxml(filter=True), sdata.getSession())


def class_map(entity, url, cls_name, dev, sdata):
    xml_output = yang.Sdk.getData(url+"/qos-service/class-maps/class-map="+str(cls_name), '',sdata.getTaskId())
    obj_class = util.parseXmlString(xml_output)
    util.log_debug("obj: ",obj_class)
    description = obj_class.class_map.get_field_value("description")
    match_type = obj_class.class_map.get_field_value("match_type")

    dev.addQOSClassMapsContainer(sdata.getSession())

    cls_map_obj = devices.device.class_maps.class_map.class_map()
    cls_map_obj.name = cls_name
    if util.isNotEmpty(description):
        cls_map_obj.description = description
    if util.isNotEmpty(match_type):
        cls_map_obj.match_type = match_type
    yang.Sdk.createData(dev.url+"/class-maps", cls_map_obj.getxml(filter=True), sdata.getSession())
    dscp = obj_class.class_map.get_field_value("dscp")
    if util.isNotEmpty(dscp):
        for ds in util.convert_to_list(dscp):
            match_obj = devices.device.class_maps.class_map.class_match_condition.class_match_condition()
            match_obj.condition_type = "ip dscp"
            match_obj.match_value = ds
            yang.Sdk.createData(dev.url+"/class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession())

    protocol = obj_class.class_map.get_field_value("protocol")
    if util.isNotEmpty(protocol):
        for pr in util.convert_to_list(protocol):
            match_obj = devices.device.class_maps.class_map.class_match_condition.class_match_condition()
            match_obj.condition_type = "protocol"
            match_obj.match_value = pr
            yang.Sdk.createData(dev.url+"/class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession())
            if pr == "http":
                match_object = devices.device.class_maps.class_map.class_match_condition.http_url.http_url()
                http_url = obj_class.class_map.get_field_value("http_url")
                print "http_url is:",http_url
                if util.isNotEmpty(http_url):
                    for url_http in util.convert_to_list(http_url):
                        match_object.url = url_http
                        yang.Sdk.createData(dev.url+"/class-maps/class-map=%s/class-match-condition=%s,%s" %(cls_name,'protocol','http'), match_object.getxml(filter=True), sdata.getSession())
                else:
                    match_obj.only_http = 'true'
                    yang.Sdk.createData(dev.url+"/class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession())

    class_map_access_list = None
    if entity == 'cpe' or entity == 'cpe_lan':
        content = getLocalObject(sdata, 'single-cpe-site-services')
        if hasattr(content.single_cpe_site_services.cpe, 'class_maps'):
            for class_map in util.convert_to_list(content.single_cpe_site_services.cpe.class_maps.class_map):
                class_map_name = class_map.name
                if class_map_name == cls_name:
                    class_map_access_list = class_map.access_list
    elif entity == "cpe_primary":
        content = getLocalObject(sdata, 'dual-cpe-site-services')
        if hasattr(content.dual_cpe_site_services.cpe_primary, 'class_maps'):
            for class_map in util.convert_to_list(content.dual_cpe_site_services.cpe_primary.class_maps.class_map):
                class_map_name = class_map.name
                if class_map_name == cls_name:
                    class_map_access_list = class_map.access_list
    elif entity == "cpe_secondary":
        content = getLocalObject(sdata, 'dual-cpe-site-services')
        if hasattr(content.dual_cpe_site_services.cpe_secondary, 'class_maps'):
            for class_map in util.convert_to_list(content.dual_cpe_site_services.cpe_secondary.class_maps.class_map):
                class_map_name = class_map.name
                if class_map_name == cls_name:
                    class_map_access_list = class_map.access_list
    elif entity == 'cpe_primary_dual' or entity == 'cpe_secondary_dual':
        content = getLocalObject(sdata, 'single-cpe-dual-wan-site-services')
        if hasattr(content.single_cpe_dual_wan_site_services.cpe, 'class_maps'):
            for class_map in util.convert_to_list(content.single_cpe_dual_wan_site_services.cpe.class_maps.class_map):
                class_map_name = class_map.name
                if class_map_name == cls_name:
                    class_map_access_list = class_map.access_list
    elif entity == "cpe_primary_inet_dual" or entity == "cpe_primary_mpls_dual":
        content = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
        if hasattr(content.dual_cpe_dual_wan_site_services.cpe_primary, 'class_maps'):
            for class_map in util.convert_to_list(content.dual_cpe_dual_wan_site_services.cpe_primary.class_maps.class_map):
                class_map_name = class_map.name
                if class_map_name == cls_name:
                    class_map_access_list = class_map.access_list
    elif entity == "cpe_secondary_inet_dual" or entity == "cpe_secondary_mpls_dual":
        content = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
        if hasattr(content.dual_cpe_dual_wan_site_services.cpe_secondary, 'class_maps'):
            for class_map in util.convert_to_list(content.dual_cpe_dual_wan_site_services.cpe_secondary.class_maps.class_map):
                class_map_name = class_map.name
                if class_map_name == cls_name:
                    class_map_access_list = class_map.access_list
    elif entity == "cpe_primary_inet_triple" or entity == "cpe_primary_mpls_triple":
        content = getLocalObject(sdata, 'triple-cpe-site-services')
        if hasattr(content.triple_cpe_site_services.cpe_primary, 'class_maps'):
            for class_map in util.convert_to_list(content.triple_cpe_site_services.cpe_primary.class_maps.class_map):
                class_map_name = class_map.name
                if class_map_name == cls_name:
                    class_map_access_list = class_map.access_list
    elif entity == "cpe_secondary_inet_triple" or entity == "cpe_secondary_mpls_triple":
        content = getLocalObject(sdata, 'triple-cpe-site-services')
        if hasattr(content.triple_cpe_site_services.cpe_secondary, 'class_maps'):
            for class_map in util.convert_to_list(content.triple_cpe_site_services.cpe_secondary.class_maps.class_map):
                class_map_name = class_map.name
                if class_map_name == cls_name:
                    class_map_access_list = class_map.access_list
    elif entity == "cpe_tertiary_inet_triple" or entity == "cpe_tertiary_mpls_triple":
        content = getLocalObject(sdata, 'triple-cpe-site-services')
        if hasattr(content.triple_cpe_site_services.cpe_tertiary, 'class_maps'):
            for class_map in util.convert_to_list(content.triple_cpe_site_services.cpe_tertiary.class_maps.class_map):
                class_map_name = class_map.name
                if class_map_name == cls_name:
                    class_map_access_list = class_map.access_list

    access_group = obj_class.class_map.get_field_value("access_group")
    if class_map_access_list is None:
        if util.isNotEmpty(access_group):
            for each_access_group in util.convert_to_list(access_group):
                access_group_def(url, each_access_group, dev, sdata)
    else:
        access_group = class_map_access_list
    if util.isNotEmpty(access_group):
        for each_access_group in util.convert_to_list(access_group):
            match_obj = devices.device.class_maps.class_map.class_match_condition.class_match_condition()
            match_obj.condition_type = "access-group"
            match_obj.match_value = each_access_group
            yang.Sdk.createData(dev.url+"/class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession())

    qos_group = obj_class.class_map.get_field_value("qos_group")
    if util.isNotEmpty(qos_group):
        match_obj = devices.device.class_maps.class_map.class_match_condition.class_match_condition()
        match_obj.condition_type = "qos-group"
        match_obj.match_value = qos_group
        yang.Sdk.createData(dev.url+"/class-maps/class-map=%s" %(cls_name), match_obj.getxml(filter=True), sdata.getSession())


def object_group_def(source_object_group, dev, sdata):
    uri = sdata.getRcPath()
    uri_list = uri.split('/', 5)
    url = '/'.join(uri_list[0:4])
    xml_output = yang.Sdk.getData(url+"/object-groups/object-group="+str(source_object_group), '', sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    objectgroup_obj = devices.device.object_groups_acl.object_group.object_group()
    objectgroup_obj.name = obj.object_group.name
    objectgroup_obj.type = obj.object_group.type
    if hasattr(obj.object_group, 'description'):
        if util.isNotEmpty(obj.object_group.description):
            objectgroup_obj.description = obj.object_group.description
    objectgroup_url = dev.url + '/object-groups-acl'
    #yang.Sdk.createData(dev.url, '<object-groups-acl/>', sdata.getSession())
    yang.Sdk.createData(objectgroup_url, objectgroup_obj.getxml(filter=True), sdata.getSession())
    if hasattr(obj.object_group, 'networks'):
        if hasattr(obj.object_group.networks, 'network'):
            for objectgroup in util.convert_to_list(obj.object_group.networks.network):
                net_url = dev.url + '/object-groups-acl/object-group=%s' %(obj.object_group.name)
                #yang.Sdk.createData(net_url, '<networks/>', sdata.getSession())

                if hasattr(objectgroup, 'group_object'):
                    if util.isNotEmpty(objectgroup.group_object):
                        network_obj = devices.device.object_groups_acl.object_group.networks.network.network()
                        network_obj.group_object = objectgroup.group_object
                        network_obj.name = "group-object" + " " + objectgroup.group_object
                        network_url = dev.url + '/object-groups-acl/object-group=%s/networks' %(obj.object_group.name)
                        yang.Sdk.createData(network_url, network_obj.getxml(filter=True), sdata.getSession())

                if hasattr(objectgroup, 'host'):
                    if util.isNotEmpty(objectgroup.host):
                        network_obj1 = devices.device.object_groups_acl.object_group.networks.network.network()
                        network_obj1.host = objectgroup.host
                        network_obj1.name = "host" + " " + objectgroup.host
                        network_url = dev.url + '/object-groups-acl/object-group=%s/networks' %(obj.object_group.name)
                        yang.Sdk.createData(network_url, network_obj1.getxml(filter=True), sdata.getSession())

                if hasattr(objectgroup, 'prefix'):
                    if util.isNotEmpty(objectgroup.prefix):
                        network_obj2 = devices.device.object_groups_acl.object_group.networks.network.network()
                        prefix = util.IPPrefix(objectgroup.prefix)
                        ip_address = prefix.address
                        netmask = prefix.netmask
                        network_obj2.ip_address = ip_address
                        network_obj2.netmask = netmask
                        network_obj2.name = ip_address + " " + netmask
                        network_url = dev.url + '/object-groups-acl/object-group=%s/networks' %(obj.object_group.name)
                        yang.Sdk.createData(network_url, network_obj2.getxml(filter=True), sdata.getSession())


def access_group_def(url, access_group, dev, sdata):
    xml_output = yang.Sdk.getData(url+"/access-lists/access-list="+str(access_group), '', sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    util.log_debug("obj: ", obj)
    name = obj.access_list.name
    access_list_entry = obj.access_list.access_list_entry
    access_obj = devices.device.access_lists.access_list.access_list()
    if access_list_entry == 'extended':
        access_obj.acl_type = access_list_entry
        if name is not None:
            access_obj.name = name
    #yang.Sdk.createData(dev.url, '<access-lists/>', sdata.getSession(), False)

    access_obj_url = dev.url + '/access-lists'
    yang.Sdk.createData(access_obj_url, access_obj.getxml(filter=True), sdata.getSession())
    for rule in util.convert_to_list(obj.access_list.access_list_rules):
        action = rule.action
        protocol = rule.protocol
        if hasattr(rule, 'service_obj_name') and util.isNotEmpty(rule.service_obj_name):
            service_obj_name = rule.service_obj_name
        else:
            service_obj_name = None
        source_condition = rule.source_condition
        if hasattr(rule, 'source_object') and util.isNotEmpty(rule.source_object):
            source_object = rule.source_object
        destination_condition = rule.destination_condition
        if hasattr(rule, 'destination_object') and util.isNotEmpty(rule.destination_object):
            destination_object = rule.destination_object
        if hasattr(rule, 'port_number') and util.isNotEmpty(rule.port_number):
            port_number = rule.port_number
        else:
            port_number = None
        if hasattr(rule, 'source_port') and util.isNotEmpty(rule.source_port):
            source_port = rule.source_port
        else:
            source_port = None
        if hasattr(rule, 'match_packets') and util.isNotEmpty(rule.match_packets):
            match_packets = rule.match_packets
        else:
            match_packets = None
        if hasattr(rule, 'precedence') and util.isNotEmpty(rule.precedence):
            precedence = rule.precedence
        else:
            precedence = None
        if hasattr(rule, 'dscp') and util.isNotEmpty(rule.dscp):
            dscp = rule.dscp
        else:
            dscp = None
        if hasattr(rule, 'source_object_group') and util.isNotEmpty(rule.source_object_group):
            source_object_group = rule.source_object_group
        else:
            source_object_group = None
        if hasattr(rule, 'destination_object_group') and util.isNotEmpty(rule.destination_object_group):
            destination_object_group = rule.destination_object_group
        else:
            destination_object_group = None
        #name_rule = rule.name
        access_rule_obj = devices.device.access_lists.access_list.acl_rules.acl_rule.acl_rule()

        port_dict = {
        '23': 'telnet',
        '80': 'www',
        '179': 'bgp',
        '500': 'isakmp',
        '53': 'domain',
        '21': 'ftp',
        '20': 'ftp-data',
        '135': 'msrpc',
        '110': 'pop3',
        '25': 'smtp',
        '514': 'syslog',
        '49': 'tacacs'
        }

        access_rule_obj.action = action
        access_rule_obj.layer4protocol = protocol
        name_rule = action + ' ' + protocol
        if util.isNotEmpty(service_obj_name):
            object_group_def(service_obj_name, dev, sdata)
            access_rule_obj.service_obj_name = service_obj_name
            name_rule += ' ' + service_obj_name
        access_rule_obj.source_condition_type = source_condition
        if source_condition == 'cidr':
            cidr_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])' + '/(([0-9])|([1-2][0-9])|(3[0-2]))$'; 
            if re.match(cidr_pattern,source_object) == None:
                raise Exception ("Please provide valid CIDR for source-object in access-list")
            prefix = util.IPPrefix(source_object)
            ip_address = prefix.address
            netmask = prefix.wildcard
            access_rule_obj.source_mask = netmask
            (addrStr, cidrStr) = source_object.split('/')
            addr = addrStr.split('.')
            cidr = int(cidrStr)
            mask = [0, 0, 0, 0]
            for i in range(cidr):
                mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
            net = []
            for i in range(4):
                net.append(int(addr[i]) & mask[i])

            network = ".".join(map(str, net))
            name_rule += ' ' + network + ' ' + netmask
            access_rule_obj.source_ip = network
        if source_condition == 'host':
            host_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$';
            if re.match(host_pattern,source_object) == None:
                raise Exception ("Please provide valid ip-address for source-object in access-list")
            access_rule_obj.source_ip = source_object
            name_rule += ' ' + 'host' + ' ' + source_object
        if source_condition == 'objectgroup':
            if source_object_group is not None:
                object_group_def(source_object_group, dev, sdata)
                access_rule_obj.source_obj_name = source_object_group
                name_rule += ' ' + 'object-group' + ' ' + source_object_group
        if source_condition == 'any':
            name_rule += ' ' + 'any'
        if util.isNotEmpty(source_port):
            access_rule_obj.source_port_operator = 'eq'
            if source_port in port_dict:
                source_port = port_dict[source_port]

            access_rule_obj.source_port = source_port
            name_rule += ' eq ' + source_port
        access_rule_obj.dest_condition_type = destination_condition
        if destination_condition == 'cidr':
            cidr_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])' + '/(([0-9])|([1-2][0-9])|(3[0-2]))$';
            if re.match(cidr_pattern,destination_object) == None:
                raise Exception ("Please provide valid CIDR for destination-object in access-list")
            prefix = util.IPPrefix(destination_object)
            ip_address = prefix.address
            netmask = prefix.wildcard
            access_rule_obj.dest_mask = netmask
            (addrStr, cidrStr) = destination_object.split('/')
            addr = addrStr.split('.')
            cidr = int(cidrStr)
            mask = [0, 0, 0, 0]
            for i in range(cidr):
                mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
            net = []
            for i in range(4):
                net.append(int(addr[i]) & mask[i])

            network = ".".join(map(str, net))
            name_rule += ' ' + network + ' ' + netmask
            access_rule_obj.dest_ip = network
        if destination_condition == 'host':
            host_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$';
            if re.match(host_pattern,destination_object) == None:
                raise Exception ("Please provide valid ip-address for destination-object in access-list")
            access_rule_obj.dest_ip = destination_object
            name_rule += ' ' + 'host' + ' ' + destination_object
        if destination_condition == 'objectgroup':
            if destination_object_group is not None:
                object_group_def(destination_object_group, dev, sdata)
                access_rule_obj.dest_obj_name = destination_object_group
                name_rule += ' ' + 'object-group' + ' ' + destination_object_group
        if destination_condition == 'any':
            name_rule += ' ' + 'any'
        if util.isNotEmpty(port_number):
            access_rule_obj.dest_port_operator = 'eq'
            if port_number in port_dict:
                port_number = port_dict[port_number]
            access_rule_obj.dest_port = port_number
            name_rule += ' eq ' + port_number
        if util.isNotEmpty(match_packets):
            access_rule_obj.match_packets = match_packets
            name_rule += ' ' + match_packets
        if match_packets == 'precedence':
            if util.isNotEmpty(precedence):
                access_rule_obj.precedence = precedence
                name_rule += ' ' + precedence
        else:
            if util.isNotEmpty(dscp):
                access_rule_obj.precedence = dscp
                name_rule += ' ' + dscp
        print "ACL_RULE_NAME: ", name_rule
        access_rule_obj.name = name_rule
        access_rules_url = dev.url + "/access-lists/access-list=%s" %(name)
        #yang.Sdk.createData(access_rules_url, '<acl-rules/>', sdata.getSession())

        access_rule_url = dev.url + '/access-lists/access-list=%s/acl-rules' %(name)
        yang.Sdk.createData(access_rule_url, access_rule_obj.getxml(filter=True), sdata.getSession())


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


def unregister_from_ipam(id, sdata, cidr, ip_address):
    if util.isEmpty(ip_address):
        return
    ip_addr = IpamPoolID(id, sdata, cidr)
    ip_addr_obj = ip_addr.ipam_pool_obj
    status = ipam.IPAM.getInstance().deallocateIpAddressInIpam(ip_addr_obj.name, ip_address)
    print "result for deallocate Ip Address In Ipam: %s" % status


def deallocate_ipaddress_from_ipam(entity, smodelctx, sdata, device, **kwarg):
    cidr = None

    if entity == 'cpe_primary_cpe_secondary_ic':
        obj = getLocalObject(sdata, 'dual-cpe-site-services')
        parent_entity = obj.dual_cpe_site_services.cpe_primary_cpe_secondary_ic
        if hasattr(parent_entity, 'cidr'):
            cidr = parent_entity.cidr
        config = util.parseXmlString(sdata.getPayload())
        config = config.end_points
        interface_ip = config.get_field_value('interface_ip')
        unregister_from_ipam(sdata.getTaskId(), sdata, cidr, interface_ip)
    elif entity == 'customer_lan_ic':
        obj = getLocalObject(sdata, 'dual-cpe-site-services')
        parent_entity = obj.dual_cpe_site_services.lan_ic
        if hasattr(parent_entity, 'cidr'):
            cidr = parent_entity.cidr
        config = util.parseXmlString(sdata.getPayload())
        config = config.end_points
        interface_ip = config.get_field_value('interface_ip')
        unregister_from_ipam(sdata.getTaskId(), sdata, cidr, interface_ip)
    elif entity == 'cpe_primary':
        obj = getLocalObject(sdata, 'dual-cpe-site-services')
        if hasattr(obj.dual_cpe_site_services.cpe_primary_ic.end_points, 'dmvpn_profile'):
            profile = obj.dual_cpe_site_services.cpe_primary_ic.end_points.dmvpn_profile
            if util.isNotEmpty(profile):
                uri = sdata.getRcPath()
                uri_list = uri.split('/', 5)
                url = '/'.join(uri_list[0:4])
                xml_output = yang.Sdk.getData(url+"/dmvpn-tunnel-profiles/dmvpn-tunnel-profile="+str(profile), '', sdata.getTaskId())
                obj = util.parseXmlString(xml_output)
                cidr = obj.dmvpn_tunnel_profile.tunnel_prefix
                config = util.parseXmlString(sdata.getPayload())
                config = config.end_points
                interface_ip = config.get_field_value('tunnel_interface_ip_address')
                if interface_ip is not None:
                    unregister_from_ipam(sdata.getTaskId(), sdata, cidr, interface_ip)
    elif entity == 'cpe_secondary':
        obj = getLocalObject(sdata, 'dual-cpe-site-services')
        if hasattr(obj.dual_cpe_site_services.cpe_secondary_ic.end_points, 'dmvpn_profile'):
            profile = obj.dual_cpe_site_services.cpe_secondary_ic.end_points.dmvpn_profile
            if util.isNotEmpty(profile):
                uri = sdata.getRcPath()
                uri_list = uri.split('/', 5)
                url = '/'.join(uri_list[0:4])
                xml_output = yang.Sdk.getData(url+"/dmvpn-tunnel-profiles/dmvpn-tunnel-profile="+str(profile), '', sdata.getTaskId())
                obj = util.parseXmlString(xml_output)
                cidr = obj.dmvpn_tunnel_profile.tunnel_prefix
                config = util.parseXmlString(sdata.getPayload())
                config = config.end_points
                interface_ip = config.get_field_value('tunnel_interface_ip_address')
                if interface_ip is not None:
                    unregister_from_ipam(sdata.getTaskId(), sdata, cidr, interface_ip)
    elif entity == 'cpe':
        obj = getLocalObject(sdata, 'single-cpe-site-services')
        if hasattr(obj.single_cpe_site_services.cpe_ic.end_points, 'dmvpn_profile'):
            profile = obj.single_cpe_site_services.cpe_ic.end_points.dmvpn_profile
            if util.isNotEmpty(profile):
                uri = sdata.getRcPath()
                uri_list = uri.split('/', 5)
                url = '/'.join(uri_list[0:4])
                xml_output = yang.Sdk.getData(url+"/dmvpn-tunnel-profiles/dmvpn-tunnel-profile="+str(profile), '', sdata.getTaskId())
                obj = util.parseXmlString(xml_output)
                cidr = obj.dmvpn_tunnel_profile.tunnel_prefix
                config = util.parseXmlString(sdata.getPayload())
                config = config.end_points
                interface_ip = config.get_field_value('tunnel_interface_ip_address')
                if interface_ip is not None:
                    unregister_from_ipam(sdata.getTaskId(), sdata, cidr, interface_ip)
    elif entity == 'cpe_lan':
        obj = getLocalObject(sdata, 'single-cpe-site-services')
        parent_entity = obj.single_cpe_site_services.cpe_lan
        if hasattr(parent_entity, 'cidr'):
            cidr = parent_entity.cidr
        config = util.parseXmlString(sdata.getPayload())
        config = config.end_points
        interface_ip = config.get_field_value('interface_ip')
        unregister_from_ipam(sdata.getTaskId(), sdata, cidr, interface_ip)
    else:
        raise Exception('Unknown exception occured')


def delete_physical_interface(entity, smodelctx, sdata, device, **kwarg):
    config = util.parseXmlString(sdata.getPayload())
    config = config.end_points
    inet_mpls = None
    vrf = None
    ivrf = None
    if hasattr(config, 'vrf'):
        vrf = config.vrf
    if util.isEmpty(vrf) or vrf is None:
        vrf = 'GLOBAL'

    if entity == 'cpe_primary_cpe_secondary_ic':
        obj = getLocalObject(sdata, 'cpe-primary-cpe-secondary-ic')
        parent_entity = obj.cpe_primary_cpe_secondary_ic
    elif entity == 'customer_lan_ic':
        obj = getLocalObject(sdata, 'cpe-lan')
        parent_entity = obj.cpe_lan
    elif entity == 'cpe_primary':
        obj = getLocalObject(sdata, 'dual-cpe-site-services')
        parent_entity = obj.dual_cpe_site_services.cpe_primary_wan
        inet_mpls = obj.dual_cpe_site_services.primary_wan.primary_wan_connectivity
        if hasattr(obj.dual_cpe_site_services.cpe_primary, 'vrf_name'):
            ivrf = obj.dual_cpe_site_services.cpe_primary.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe_primary_dual':
        obj = getLocalObject(sdata, 'single-cpe-dual-wan-site-services')
        parent_entity = obj.single_cpe_dual_wan_site_services.cpe_primary_wan
        inet_mpls = obj.single_cpe_dual_wan_site_services.primary_wan.primary_wan_connectivity
        if hasattr(obj.single_cpe_dual_wan_site_services.cpe, 'vrf_name'):
            ivrf = obj.single_cpe_dual_wan_site_services.cpe.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe_secondary':
        obj = getLocalObject(sdata, 'dual-cpe-site-services')
        parent_entity = obj.dual_cpe_site_services.cpe_secondary_wan
        inet_mpls = obj.dual_cpe_site_services.secondary_wan.secondary_wan_connectivity
        if hasattr(obj.dual_cpe_site_services.cpe_secondary, 'vrf_name'):
            ivrf = obj.dual_cpe_site_services.cpe_secondary.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe_secondary_dual':
        obj = getLocalObject(sdata, 'single-cpe-dual-wan-site-services')
        parent_entity = obj.single_cpe_dual_wan_site_services.cpe_secondary_wan
        inet_mpls = obj.single_cpe_dual_wan_site_services.secondary_wan.secondary_wan_connectivity
        if hasattr(obj.single_cpe_dual_wan_site_services.cpe, 'vrf_name'):
            ivrf = obj.single_cpe_dual_wan_site_services.cpe.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe':
        obj = getLocalObject(sdata, 'single-cpe-site-services')
        parent_entity = obj.single_cpe_site_services.cpe_wan
        inet_mpls = obj.single_cpe_site_services.wan.wan_connectivity
        if hasattr(obj.single_cpe_site_services.cpe, 'vrf_name'):
            ivrf = obj.single_cpe_site_services.cpe.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe_lan':
        obj = getLocalObject(sdata, 'single-cpe-site-services')
        parent_entity = obj.single_cpe_site_services.cpe_lan
    elif entity == 'cpe_lan_dual':
        obj = getLocalObject(sdata, 'single-cpe-dual-wan-site-services')
        parent_entity = obj.single_cpe_dual_wan_site_services.cpe_lan
    elif entity == 'cpe_primary_inet_dual':
        obj = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
        parent_entity = obj.dual_cpe_dual_wan_site_services.cpe_primary_inet_wan
        inet_mpls = obj.dual_cpe_dual_wan_site_services.primary_inet_wan.primary_inet_wan_connectivity
        if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_primary, 'vrf_name'):
            ivrf = obj.dual_cpe_dual_wan_site_services.cpe_primary.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe_primary_mpls_dual':
        obj = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
        parent_entity = obj.dual_cpe_dual_wan_site_services.cpe_primary_mpls_wan
        inet_mpls = obj.dual_cpe_dual_wan_site_services.primary_mpls_wan.primary_mpls_wan_connectivity
        if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_primary, 'vrf_name'):
            ivrf = obj.dual_cpe_dual_wan_site_services.cpe_primary.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe_secondary_inet_dual':
        obj = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
        parent_entity = obj.dual_cpe_dual_wan_site_services.cpe_secondary_inet_wan
        inet_mpls = obj.dual_cpe_dual_wan_site_services.secondary_inet_wan.secondary_inet_wan_connectivity
        if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_secondary, 'vrf_name'):
            ivrf = obj.dual_cpe_dual_wan_site_services.cpe_secondary.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe_secondary_mpls_dual':
        obj = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
        parent_entity = obj.dual_cpe_dual_wan_site_services.cpe_secondary_mpls_wan
        inet_mpls = obj.dual_cpe_dual_wan_site_services.secondary_mpls_wan.secondary_mpls_wan_connectivity
        if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_secondary, 'vrf_name'):
            ivrf = obj.dual_cpe_dual_wan_site_services.cpe_secondary.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'customer_lan_ic_lan':
        obj = getLocalObject(sdata, 'cpe-lan')
        parent_entity = obj.cpe_lan
    elif entity == 'cpe_primary_cpe_secondary_ic_dual':
        obj = getLocalObject(sdata, 'cpe-primary-cpe-secondary-ic')
        parent_entity = obj.cpe_primary_cpe_secondary_ic
    elif entity == 'customer_lan_ic_dual':
        obj = getLocalObject(sdata, 'cpe-lan')
        parent_entity = obj.cpe_lan
    elif entity == 'cpe_primary_cpe_secondary_ic_triple':
        obj = getLocalObject(sdata, 'cpe-primary-cpe-secondary-ic')
        parent_entity = obj.cpe_primary_cpe_secondary_ic
    elif entity == 'cpe_secondary_cpe_tertiary_ic_triple':
        obj = getLocalObject(sdata, 'cpe-secondary-cpe-tertiary-ic')
        parent_entity = obj.cpe_secondary_cpe_tertiary_ic
    elif entity == 'cpe_tertiary_cpe_primary_ic_triple':
        obj = getLocalObject(sdata, 'cpe-tertiary-cpe-primary-ic')
        parent_entity = obj.cpe_tertiary_cpe_primary_ic
    elif entity == 'customer_lan_ic_triple':
        obj = getLocalObject(sdata, 'cpe-lan')
        parent_entity = obj.cpe_lan
    elif entity == 'cpe_primary_inet_triple':
        obj = getLocalObject(sdata, 'triple-cpe-site-services')
        parent_entity = obj.triple_cpe_site_services.cpe_primary_inet_wan
        inet_mpls = obj.triple_cpe_site_services.primary_inet_wan.primary_inet_wan_connectivity
        if hasattr(obj.triple_cpe_site_services.cpe_primary, 'vrf_name'):
            ivrf = obj.triple_cpe_site_services.cpe_primary.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe_primary_mpls_triple':
        obj = getLocalObject(sdata, 'triple-cpe-site-services')
        parent_entity = obj.triple_cpe_site_services.cpe_primary_mpls_wan
        inet_mpls = obj.triple_cpe_site_services.primary_mpls_wan.primary_mpls_wan_connectivity
        if hasattr(obj.triple_cpe_site_services.cpe_primary, 'vrf_name'):
            ivrf = obj.triple_cpe_site_services.cpe_primary.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe_secondary_inet_triple':
        obj = getLocalObject(sdata, 'triple-cpe-site-services')
        parent_entity = obj.triple_cpe_site_services.cpe_secondary_inet_wan
        inet_mpls = obj.triple_cpe_site_services.secondary_inet_wan.secondary_inet_wan_connectivity
        if hasattr(obj.triple_cpe_site_services.cpe_secondary, 'vrf_name'):
            ivrf = obj.triple_cpe_site_services.cpe_secondary.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe_secondary_mpls_triple':
        obj = getLocalObject(sdata, 'triple-cpe-site-services')
        parent_entity = obj.triple_cpe_site_services.cpe_secondary_mpls_wan
        inet_mpls = obj.triple_cpe_site_services.secondary_mpls_wan.secondary_mpls_wan_connectivity
        if hasattr(obj.triple_cpe_site_services.cpe_secondary, 'vrf_name'):
            ivrf = obj.triple_cpe_site_services.cpe_secondary.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe_tertiary_inet_triple':
        obj = getLocalObject(sdata, 'triple-cpe-site-services')
        parent_entity = obj.triple_cpe_site_services.cpe_tertiary_inet_wan
        inet_mpls = obj.triple_cpe_site_services.tertiary_inet_wan.tertiary_inet_wan_connectivity
        if hasattr(obj.triple_cpe_site_services.cpe_tertiary, 'vrf_name'):
            ivrf = obj.triple_cpe_site_services.cpe_tertiary.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    elif entity == 'cpe_tertiary_mpls_triple':
        obj = getLocalObject(sdata, 'triple-cpe-site-services')
        parent_entity = obj.triple_cpe_site_services.cpe_tertiary_mpls_wan
        inet_mpls = obj.triple_cpe_site_services.tertiary_mpls_wan.tertiary_mpls_wan_connectivity
        if hasattr(obj.triple_cpe_site_services.cpe_tertiary, 'vrf_name'):
            ivrf = obj.triple_cpe_site_services.cpe_tertiary.vrf_name
        if ivrf is None:
            ivrf = "GLOBAL"
    else:
        raise Exception('Unknown exception occured')

    interface_type = config.get_field_value('interface_type')
    interface_name = config.get_field_value('interface_name')
    interface_description = config.get_field_value('interface_description')
    interface_ip = config.get_field_value('interface_ip')
    if hasattr(parent_entity, 'auto_negotiation'):
        auto_negotiation = parent_entity.auto_negotiation
    else:
        auto_negotiation = None
    if hasattr(parent_entity, 'speed'):
        speed = parent_entity.speed
    if hasattr(parent_entity, 'duplex'):
        duplex = parent_entity.duplex
    if hasattr(parent_entity, 'outbound_policy'):
        outbound_policy = parent_entity.outbound_policy
    elif hasattr(parent_entity, 'policy_name'):
        outbound_policy = parent_entity.policy_name
    else:
        outbound_policy = None
    if hasattr(parent_entity, 'inbound_policy'):
        inbound_policy = parent_entity.inbound_policy
    else:
        inbound_policy = None
    if hasattr(parent_entity, 'load_interval_delay'):
        load_interval_delay = parent_entity.load_interval_delay
    else:
        load_interval_delay = None
    if hasattr(parent_entity, 'in_queue_length'):
        in_queue_length = parent_entity.in_queue_length
    else:
        in_queue_length = None
    if hasattr(parent_entity, 'out_queue_length'):
        out_queue_length = parent_entity.out_queue_length
    else:
        out_queue_length = None
    next_ip_address = config.get_field_value('interface_ip')

    mode = None

    vlan_id = None
    cidr = None
    link_negotiation = None
    netmask = None

    if config.get_field_value('vlan_id') is not None:
        vlan_id = config.get_field_value('vlan_id')
    if hasattr(parent_entity, 'cidr'):
        cidr = parent_entity.cidr
    # if cidr is not None:
    #     prefix = util.IPPrefix(cidr)
    #     netmask = prefix.netmask

    if interface_type == "Physical":
        mode = "l3-interface"

    if auto_negotiation == "true":
        link_negotiation = "auto"

    if entity == 'cpe_primary_cpe_secondary_ic' or entity == 'cpe_lan' or entity == 'customer_lan_ic' or entity == 'cpe_lan_dual' or entity == 'customer_lan_ic_dual' or entity == 'cpe_primary_cpe_secondary_ic_dual' or entity == 'cpe_primary_cpe_secondary_ic_triple' or entity == 'cpe_secondary_cpe_tertiary_ic_triple' or entity == 'cpe_tertiary_cpe_primary_ic_triple' or entity == 'customer_lan_ic_triple':
        if interface_type == "Sub-Interface":
            intf_obj = devices.device.interfaces.interface.interface()
            interface_name1 = interface_name + '.' + str(vlan_id)
            intf_obj.name = interface_name1
            intf_obj.long_name = interface_name1
            intf_obj.mode = "sub-interface"
            uri = device.url + '/interface:interfaces/interface=%s' % (str(interface_name1).replace('/', '%2F'))
            payload = intf_obj.getxml(filter=True)
            if device.isInterfaceInDeviceExists(interface_name1):
                yang.Sdk.deleteData(uri, payload, sdata.getTaskId(), sdata.getSession())
            intf_obj_phy = devices.device.interfaces.interface.interface()
            intf_obj_phy.name = interface_name
            intf_obj_phy.long_name = interface_name
            intf_obj_phy.mode = "l3-interface"
            intf_obj_phy.vrf._empty_tag = True
            intf_obj_phy.link_negotiation._empty_tag = True
            intf_obj_phy.outbound_qos._empty_tag = True
            intf_obj_phy.inbound_qos._empty_tag = True
            intf_obj_phy.acl_inbound_name._empty_tag = True
            intf_obj_phy.acl_outbound_name._empty_tag = True
            intf_obj.nat_name._empty_tag = True
            #if load_interval_delay is not None:
            intf_obj_phy.load_interval_delay._empty_tag = True
            #if in_queue_length is not None:
            intf_obj_phy.in_queue_length._empty_tag = True
            #if out_queue_length is not None:
            intf_obj_phy.out_queue_length._empty_tag = True
            uri = device.url + '/interface:interfaces/interface=%s' % (str(interface_name).replace('/', '%2F'))
            payload = intf_obj_phy.getxml(filter=True)
            if device.isInterfaceInDeviceExists(interface_name):
                #yang.Sdk.deleteData(uri, payload, sdata.getTaskId(), sdata.getSession())
                yang.Sdk.patchData(uri, payload, sdata, add_reference=False)
                intf_obj_phy1 = devices.device.interfaces.interface.interface()
                intf_obj_phy1.name = interface_name
                intf_obj_phy1.long_name = interface_name
                intf_obj_phy1.mode._empty_tag = True
                payload1 = intf_obj_phy1.getxml(filter=True)
                yang.Sdk.patchData(uri, payload1, sdata, add_reference=False)
        elif interface_type == "SVI":
            intf_obj = devices.device.interfaces.interface.interface()
            interface_name1 = "Vlan" + str(vlan_id)
            intf_obj.name = interface_name1
            intf_obj.long_name = interface_name1
            intf_obj.mode = "vlan"
            uri = device.url + '/interface:interfaces/interface=%s' % (str(interface_name1).replace('/', '%2F'))
            payload = intf_obj.getxml(filter=True)
            if device.isInterfaceInDeviceExists(interface_name1):
                yang.Sdk.deleteData(uri, payload, sdata.getTaskId(), sdata.getSession())
        else:
            intf_obj = devices.device.interfaces.interface.interface()
            intf_obj.ip_address._empty_tag = True
            intf_obj.netmask._empty_tag = True
            intf_obj.name = interface_name
            intf_obj.long_name = interface_name
            intf_obj.description._empty_tag = True
            intf_obj.mode = "l3-interface"
            intf_obj.vrf._empty_tag = True
            intf_obj.link_negotiation._empty_tag = True
            intf_obj.outbound_qos._empty_tag = True
            intf_obj.inbound_qos._empty_tag = True
            intf_obj.acl_inbound_name._empty_tag = True
            intf_obj.acl_outbound_name._empty_tag = True
            intf_obj.nat_name._empty_tag = True
            intf_obj.pbr_policy._empty_tag = True
            #if load_interval_delay is not None:
            intf_obj.load_interval_delay._empty_tag = True
            #if in_queue_length is not None:
            intf_obj.in_queue_length._empty_tag = True
            #if out_queue_length is not None:
            intf_obj.out_queue_length._empty_tag = True
            uri = device.url + '/interface:interfaces/interface=%s' % (str(interface_name).replace('/', '%2F'))
            payload = intf_obj.getxml(filter=True)
            print 'delete Interface: %s, payload = %s' % (uri, payload)
            if device.isInterfaceInDeviceExists(interface_name):
                #yang.Sdk.deleteData(uri, payload, sdata.getTaskId(), sdata.getSession())
                yang.Sdk.patchData(uri, payload, sdata, add_reference=False)
                intf_obj_phy1 = devices.device.interfaces.interface.interface()
                intf_obj_phy1.name = interface_name
                intf_obj_phy1.long_name = interface_name
                intf_obj_phy1.mode._empty_tag = True
                payload1 = intf_obj_phy1.getxml(filter=True)
                yang.Sdk.patchData(uri, payload1, sdata, add_reference=False)
            else:
                print "skipping delete for interface as it does not exists on device"
    else:
        if interface_type == "Sub-Interface":
            intf_obj = devices.device.interfaces.interface.interface()
            interface_name1 = interface_name + '.' + str(vlan_id)
            intf_obj.name = interface_name1
            intf_obj.long_name = interface_name1
            intf_obj.mode = "sub-interface"
            intf_obj.outbound_qos._empty_tag = True
            intf_obj.inbound_qos._empty_tag = True
            intf_obj.acl_inbound_name._empty_tag = True
            intf_obj.acl_outbound_name._empty_tag = True
            #if ((vrf is not None and vrf != 'GLOBAL') or (ivrf is not None and ivrf != 'GLOBAL')) and inet_mpls == 'MPLS':
            intf_obj.vrf._empty_tag = True
            uri = device.url + '/interface:interfaces/interface=%s' % (str(interface_name1).replace('/', '%2F'))
            payload = intf_obj.getxml(filter=True)
            if device.isInterfaceInDeviceExists(interface_name1):
                yang.Sdk.patchData(uri, payload, sdata, add_reference=False)
            intf_obj_phy = devices.device.interfaces.interface.interface()
            intf_obj_phy.name = interface_name
            intf_obj_phy.long_name = interface_name
            intf_obj_phy.mode = "l3-interface"
            #intf_obj_phy.vrf._empty_tag = True
            intf_obj_phy.link_negotiation._empty_tag = True
            intf_obj_phy.outbound_qos._empty_tag = True
            intf_obj_phy.inbound_qos._empty_tag = True
            intf_obj_phy.acl_inbound_name._empty_tag = True
            intf_obj_phy.acl_outbound_name._empty_tag = True
            #if load_interval_delay is not None:
            intf_obj_phy.load_interval_delay._empty_tag = True
            #if in_queue_length is not None:
            intf_obj_phy.in_queue_length._empty_tag = True
            #if out_queue_length is not None:
            intf_obj_phy.out_queue_length._empty_tag = True
            uri = device.url + '/interface:interfaces/interface=%s' % (str(interface_name).replace('/', '%2F'))
            payload = intf_obj_phy.getxml(filter=True)
            print 'delete Interface: %s, payload = %s' % (uri, payload)
            if device.isInterfaceInDeviceExists(interface_name):
                #yang.Sdk.deleteData(uri, payload, sdata.getTaskId(), sdata.getSession())
                yang.Sdk.patchData(uri, payload, sdata, add_reference=False)
                intf_obj_phy1 = devices.device.interfaces.interface.interface()
                intf_obj_phy1.name = interface_name
                intf_obj_phy1.long_name = interface_name
                intf_obj_phy1.mode._empty_tag = True
                payload1 = intf_obj_phy1.getxml(filter=True)
                yang.Sdk.patchData(uri, payload1, sdata, add_reference=False)
        elif interface_type == "SVI":
            intf_obj = devices.device.interfaces.interface.interface()
            interface_name1 = "Vlan" + str(vlan_id)
            intf_obj.name = interface_name1
            intf_obj.long_name = interface_name1
            intf_obj.mode = "vlan"
            uri = device.url + '/interface:interfaces/interface=%s' % (str(interface_name1).replace('/', '%2F'))
            payload = intf_obj.getxml(filter=True)
            if device.isInterfaceInDeviceExists(interface_name1):
                yang.Sdk.deleteData(uri, payload, sdata.getTaskId(), sdata.getSession())
        else:
            intf_obj = devices.device.interfaces.interface.interface()
            intf_obj.name = interface_name
            intf_obj.long_name = interface_name
            intf_obj.description._empty_tag = True
            intf_obj.mode = "l3-interface"
            intf_obj.link_negotiation._empty_tag = True
            intf_obj.outbound_qos._empty_tag = True
            intf_obj.inbound_qos._empty_tag = True
            intf_obj.acl_inbound_name._empty_tag = True
            intf_obj.acl_outbound_name._empty_tag = True
            #if ((vrf is not None and vrf != 'GLOBAL') or (ivrf is not None and ivrf != 'GLOBAL')) and inet_mpls == 'MPLS':
            intf_obj.vrf._empty_tag = True
            #if load_interval_delay is not None:
            intf_obj.load_interval_delay._empty_tag = True
            #if in_queue_length is not None:
            intf_obj.in_queue_length._empty_tag = True
            #if out_queue_length is not None:
            intf_obj.out_queue_length._empty_tag = True
            uri = device.url + '/interface:interfaces/interface=%s' % (str(interface_name).replace('/', '%2F'))
            payload = intf_obj.getxml(filter=True)
            print 'delete Interface: %s, payload = %s' % (uri, payload)
            if device.isInterfaceInDeviceExists(interface_name):
                #yang.Sdk.deleteData(uri, payload, sdata.getTaskId(), sdata.getSession())
                yang.Sdk.patchData(uri, payload, sdata, add_reference=False)
                intf_obj_phy1 = devices.device.interfaces.interface.interface()
                intf_obj_phy1.name = interface_name
                intf_obj_phy1.long_name = interface_name
                intf_obj_phy1.mode._empty_tag = True
                payload1 = intf_obj_phy1.getxml(filter=True)
                yang.Sdk.patchData(uri, payload1, sdata, add_reference=False)
            else:
                print "skipping delete for interface as it does not exists on device"


def back_endpoint(entity, smodelctx, sdata, device, **kwargs):
    inputdict = kwargs['inputdict']
    if entity != "cpe_primary_cpe_secondary_ic":
        profile_name = inputdict['profile_name']
    if entity != "cpe_primary_cpe_secondary_ic" and util.isEmpty(profile_name):
        raise Exception("Profile name in cpe-lan can not be empty.")
    vrf = inputdict['vrf']
    interface_type = inputdict['interface_type']
    interface_name = inputdict['interface_name']
    if interface_type == "Physical" or interface_type == "Sub-Interface":
        if util.isEmpty(interface_name):
            raise Exception("interface_name should not be empty when interface_type is Physical and sub-interface")

    interface_description = inputdict['interface_description']
    interface_ip = inputdict['interface_ip']
    device_ip = inputdict['device_ip']
    global_inbound_acl = inputdict['global_inbound_acl']
    site_inbound_acl = inputdict['site_inbound_acl']
    global_outbound_acl = inputdict['global_outbound_acl']
    site_outbound_acl = inputdict['site_outbound_acl']
    nat_inside = None
    nat_outside = None
    if entity != "cpe_primary_cpe_secondary_ic":
        nat_inside = inputdict['nat_inside']
        nat_outside = inputdict['nat_outside']
    #vlan_id = None
    vlan_id = inputdict['vlan_id']
    if util.isNotEmpty(interface_name):
        if '.' not in interface_name and interface_type == "Sub-Interface":
            if util.isEmpty(vlan_id):
                raise Exception("vlan_id should not be empty when interface_type is Sub-Interface")

    if interface_type == "SVI":
        if util.isEmpty(vlan_id):
            raise Exception("vlan_id should not empty when interface_type is SVI")

    if 'hsrp_priority' in inputdict:
        hsrp_priority = inputdict['hsrp_priority']
    else:
        hsrp_priority = None

    mode = None
    cidr = None
    link_negotiation = None
    netmask = None
    if util.isEmpty(vrf):
        vrf = 'GLOBAL'
    parent_entity = None
    access_lists = []
    if entity == "cpe_primary_cpe_secondary_ic":
        obj = getLocalObject(sdata, 'dual-cpe-site-services')
        parent_entity = obj.dual_cpe_site_services.cpe_primary_cpe_secondary_ic
        if device_ip == obj.dual_cpe_site_services.cpe_primary.device_ip:
            if hasattr(obj.dual_cpe_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.dual_cpe_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.dual_cpe_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
        if device_ip == obj.dual_cpe_site_services.cpe_secondary.device_ip:
            if hasattr(obj.dual_cpe_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.dual_cpe_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.dual_cpe_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
    elif entity == "customer_lan_ic":
        obj = getLocalObject(sdata, 'dual-cpe-site-services')
        if device_ip == obj.dual_cpe_site_services.cpe_primary.device_ip:
            if hasattr(obj.dual_cpe_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.dual_cpe_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.dual_cpe_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
        if device_ip == obj.dual_cpe_site_services.cpe_secondary.device_ip:
            if hasattr(obj.dual_cpe_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.dual_cpe_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.dual_cpe_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
    elif entity == "cpe_lan":
        obj = getLocalObject(sdata, 'single-cpe-site-services')
        if device_ip == obj.single_cpe_site_services.cpe.device_ip:
            if hasattr(obj.single_cpe_site_services.cpe, 'access_lists'):
                if hasattr(obj.single_cpe_site_services.cpe.access_lists, 'access_list'):
                    obj.single_cpe_site_services.cpe.access_lists.access_list = util.convert_to_list(obj.single_cpe_site_services.cpe.access_lists.access_list)
                    for access_list_dynamic in obj.single_cpe_site_services.cpe.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
    elif entity == "cpe_lan_dual":
        obj = getLocalObject(sdata, 'single-cpe-dual-wan-site-services')
        if device_ip == obj.single_cpe_dual_wan_site_services.cpe.device_ip:
            if hasattr(obj.single_cpe_dual_wan_site_services.cpe, 'access_lists'):
                if hasattr(obj.single_cpe_dual_wan_site_services.cpe.access_lists, 'access_list'):
                    obj.single_cpe_dual_wan_site_services.cpe.access_lists.access_list = util.convert_to_list(obj.single_cpe_dual_wan_site_services.cpe.access_lists.access_list)
                    for access_list_dynamic in obj.single_cpe_dual_wan_site_services.cpe.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)

    if entity != "cpe_primary_cpe_secondary_ic":
        obj = getLocalObject(sdata, 'cpe-lan')
        if hasattr(obj.cpe_lan, 'lan_profile'):
            lan_prof = 'false'
            obj.cpe_lan.lan_profile = util.convert_to_list(obj.cpe_lan.lan_profile)
            for lanprof in obj.cpe_lan.lan_profile:
                if lanprof.profile_name == profile_name:
                    lan_prof = 'true'
                    parent_entity = lanprof
            if lan_prof != 'true':
                raise Exception("Invalid Profile Name")
        else:
            raise Exception("No lan profile found")
    if hasattr(parent_entity, 'auto_negotiation'):
        auto_negotiation = parent_entity.auto_negotiation
    else:
        auto_negotiation = None
    if hasattr(parent_entity, 'speed'):
        speed = parent_entity.speed
    else:
        speed = None
    if hasattr(parent_entity, 'duplex'):
        duplex = parent_entity.duplex
    else:
        duplex = None
    if hasattr(parent_entity, 'inbound_policy'):
        inbound_policy = parent_entity.inbound_policy
    else:
        inbound_policy = None
    if hasattr(parent_entity, 'load_interval'):
        load_interval = parent_entity.load_interval
    else:
        load_interval = None
    if hasattr(parent_entity, 'load_interval_delay'):
        load_interval_delay = parent_entity.load_interval_delay
    else:
        load_interval_delay = None
    if hasattr(parent_entity, 'hold_queue_in'):
        hold_queue_in = parent_entity.hold_queue_in
    else:
        hold_queue_in = None
    if hasattr(parent_entity, 'in_queue_length'):
        in_queue_length = parent_entity.in_queue_length
    else:
        in_queue_length = None
    if hasattr(parent_entity, 'hold_queue_out'):
        hold_queue_out = parent_entity.hold_queue_out
    else:
        hold_queue_out = None
    if hasattr(parent_entity, 'out_queue_length'):
        out_queue_length = parent_entity.out_queue_length
    else:
        out_queue_length = None
    if hasattr(parent_entity, 'hierarchical_inbound_policy'):
        hierarchical_inbound_policy = parent_entity.hierarchical_inbound_policy
    else:
        hierarchical_inbound_policy = None
    if hasattr(parent_entity, 'hierarchical_policy'):
        hierarchical_policy = parent_entity.hierarchical_policy
    else:
        hierarchical_policy = None
    if hasattr(parent_entity, 'cidr'):
        cidr = parent_entity.cidr

    if hierarchical_inbound_policy == 'false':
        if util.isNotEmpty(inbound_policy):
            qos_child(entity, inbound_policy, device, sdata)
    elif hierarchical_inbound_policy == 'true':
        if util.isNotEmpty(hierarchical_policy):
            hierarchical_policy_class(entity, hierarchical_policy, device, sdata)

    next_ip_address = None
    ip_addr = None
    if entity == "cpe_primary_cpe_secondary_ic":
        ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr)

    #Seb's added    
    elif cidr is not None:
        prefix = util.IPPrefix(cidr)
        if str(prefix.masklen) == str(32):
            raise Exception("Bad mask /32 for address")
        obj_cidr = getLocalObject(sdata, 'customer')
        if entity == 'cpe_lan':
            obj_site = getLocalObject(sdata, 'single-cpe-site-services')
            cidr_name = obj_cidr.customer.name + '_' + obj_site.single_cpe_site_services.site_name + '_' + cidr
            cidr_gateway = util.next_ip_address(prefix.address)
            rp = obj_site.single_cpe_site_services.resource_pool
        if entity == "customer_lan_ic":
            obj_site = getLocalObject(sdata, 'dual-cpe-site-services')
            cidr_name = obj_cidr.customer.name + '_' + obj_site.dual_cpe_site_services.site_name + '_' + cidr
            cidr_gateway = util.next_ip_address(prefix.address)
            rp = obj_site.dual_cpe_site_services.resource_pool
        if entity == "cpe_lan_dual":
            obj_site = getLocalObject(sdata, 'single-cpe-dual-wan-site-services')
            cidr_name = obj_cidr.customer.name + '_' + obj_site.single_cpe_dual_wan_site_services.site_name + '_' + cidr
            cidr_gateway = util.next_ip_address(prefix.address)
            rp = obj_site.single_cpe_dual_wan_site_services.resource_pool

        payload = '''<ipaddress-pool>
                    <name>'''+cidr_name+'''</name>
                    <cidr>'''+cidr+'''</cidr>
                    <gateway>'''+cidr_gateway+'''</gateway>
                    <resource-pool>'''+rp+'''</resource-pool>
                    </ipaddress-pool>'''
        cidr_url = "/app/restconf/data/ipam:ipaddress-pools"

        try:
            cidr_name_local = cidr_name
            cidr_name_local = cidr_name_local.replace('/', '%2F')
            get_ipaddress_pool_url = "/app/restconf/data/ipam:ipaddress-pools/ipaddress-pool=%s" %(cidr_name_local)
            pool = yang.Sdk.getData(get_ipaddress_pool_url, '', sdata.getTaskId())
            pool = util.parseXmlString(pool)
        except DataNodeNotFoundException:
            yang.Sdk.createData(cidr_url, payload, sdata.getSession())
        ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr_name)

        #Seb's added indent
        ip_addr_obj = ip_addr.ipam_pool_obj
        prefix = util.IPPrefix(ip_addr_obj.cidr)
        netmask = prefix.netmask
        wildcard = prefix.wildcard

    #Seb's added
    if util.isEmpty(interface_ip) or interface_ip == None:
        #used_ips_list = get_used_ip_list_from_ippool(ip_addr_obj.name, sdata)
        #interface_ip = get_freeip_from_cidr(ip_addr_obj.cidr, used_ips_list)
        #add_ipaddress_entries(ip_addr_obj.name, interface_ip, sdata)
        # next_ip_address = ipam.IPAM.getInstance().allocateIpAddressInIpam(ip_addr_obj.name, kwargs['inputdict']['endpoint_name'])
        interface_ip = ""
        netmask = ""
        print 'TEST OK'
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
            if entity == "cpe_primary_cpe_secondary_ic":
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
        # next_ip_address = ipam.IPAM.getInstance().allocateIpAddressInIpam(ip_addr_obj.name, kwargs['inputdict']['endpoint_name'], interface_ip)
    payload = "<interface-ip>%s</interface-ip>" % interface_ip
    serv_uri = sdata.getRcPath()
    yang.Sdk.createData(serv_uri, payload, sdata.getSession())

    if interface_type == "Physical" or interface_type == "Sub-Interface":
        if util.isEmpty(interface_name):
            raise Exception("interface_name should not be empty when interface_type is Physical and sub-interface")
    int_name_phy = interface_name
    if interface_type == "Physical":
        mode = "l3-interface"
    elif interface_type == "Sub-Interface":
        mode = "sub-interface"
        if vlan_id is not None:
            interface_name = interface_name + '.' + str(vlan_id)
    elif interface_type == "SVI":
        mode = "vlan"
    if auto_negotiation == "true":
        link_negotiation = "auto"

    intf_obj = devices.device.interfaces.interface.interface()
    if mode == "sub-interface" or mode == "l3-interface":
        intf_obj.name = interface_name
        intf_obj.long_name = interface_name
    intf_obj.description = interface_description
    if mode == "sub-interface":
        intf_obj.mode = "sub-interface"
        intf_obj.vlan = vlan_id
    elif mode == "vlan":
        intf_obj.mode = "vlan"
        intf_obj.vlan = vlan_id
        intf_obj.long_name = "Vlan" + str(vlan_id)
        intf_obj.name = "Vlan" + str(vlan_id)
    else:
        intf_obj.mode = "l3-interface"

    #Seb's added    
    if interface_ip is not None:
        intf_obj.ip_address = interface_ip
        intf_obj.netmask = netmask
    else:
        intf_obj.ip_address = ""
        intf_obj.netmask = ""
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    if mode == "sub-interface" or mode == "l3-interface":
        if vrf is not None and vrf != 'GLOBAL':
            xml_output = yang.Sdk.getData(url+"/vrfs/vrf="+str(vrf), '', sdata.getTaskId())
            obj_local = util.parseXmlString(xml_output)
            util.log_debug("obj_local: ", obj_local)
            intf_obj.vrf_definition_mode = obj_local.vrf.vrf_definition_mode
            intf_obj.vrf = vrf
        if entity != "cpe_primary_cpe_secondary_ic":
            if util.isNotEmpty(inputdict['pbr_policy']):
                route_maps(inputdict['pbr_policy'], device, sdata)
                intf_obj.pbr_policy = inputdict['pbr_policy']
        if hierarchical_inbound_policy == 'false':
            if util.isNotEmpty(inbound_policy):
                intf_obj.inbound_qos = inbound_policy
        elif hierarchical_inbound_policy == 'true':
            if util.isNotEmpty(hierarchical_policy):
                intf_obj.inbound_qos = hierarchical_policy
        if util.isNotEmpty(global_inbound_acl):
            access_group_def(url, global_inbound_acl, device, sdata)
            intf_obj.acl_inbound_name = global_inbound_acl
        if util.isNotEmpty(global_outbound_acl):
            access_group_def(url, global_outbound_acl, device, sdata)
            intf_obj.acl_outbound_name = global_outbound_acl
        if util.isNotEmpty(site_inbound_acl):
            if site_inbound_acl in access_lists:
                intf_obj.acl_inbound_name = site_inbound_acl
            else:
                raise Exception("Make sure that provided site_inbound_acl should be present on router access-lists")
        if util.isNotEmpty(site_outbound_acl):
            if site_outbound_acl in access_lists:
                intf_obj.acl_outbound_name = site_outbound_acl
            else:
                raise Exception("Make sure that provided site_outbound_acl should be present on router access-lists")
        if nat_inside == 'true':
            intf_obj.nat_name = 'inside'
        elif nat_outside == 'true':
            intf_obj.nat_name = 'outside'
    if interface_type == "Physical":
        if link_negotiation is not None:
            intf_obj.link_negotiation = link_negotiation
        if auto_negotiation != "true":
            if util.isNotEmpty(speed):
                intf_obj.speed = speed
            if util.isNotEmpty(duplex):
                intf_obj.duplex = duplex
        if load_interval == 'true':
            if util.isNotEmpty(load_interval_delay):
                intf_obj.load_interval_delay = load_interval_delay
        if hold_queue_in == 'true':
            if util.isNotEmpty(in_queue_length):
                intf_obj.in_queue_length = in_queue_length
        if hold_queue_out == 'true':
            if util.isNotEmpty(out_queue_length):
                intf_obj.out_queue_length = out_queue_length
        yang.Sdk.createData(device.url+'/interfaces', intf_obj.getxml(filter=True), sdata.getSession(), False)
    else:
        yang.Sdk.createData(device.url+'/interfaces', intf_obj.getxml(filter=True), sdata.getSession(), False)

    if mode == "sub-interface":
        intf_obj_phy = devices.device.interfaces.interface.interface()
        intf_obj_phy.name = int_name_phy
        intf_obj_phy.long_name = int_name_phy
        intf_obj_phy.mode = "l3-interface"
        if link_negotiation is not None:
            intf_obj_phy.link_negotiation = link_negotiation
        if auto_negotiation != "true":
            if util.isNotEmpty(speed):
                intf_obj_phy.speed = speed
            if util.isNotEmpty(duplex):
                intf_obj_phy.duplex = duplex
        if load_interval == 'true':
            if util.isNotEmpty(load_interval_delay):
                intf_obj_phy.load_interval_delay = load_interval_delay
        if hold_queue_in == 'true':
            if util.isNotEmpty(in_queue_length):
                intf_obj_phy.in_queue_length = in_queue_length
        if hold_queue_out == 'true':
            if util.isNotEmpty(out_queue_length):
                intf_obj_phy.out_queue_length = out_queue_length
        yang.Sdk.createData(device.url+'/interfaces', intf_obj_phy.getxml(filter=True), sdata.getSession(), False)

    # creating hsrp policy on the given interface
    hsrp_obj = devices.device.interfaces.interface.hsrp.hsrp()

    hsrp_obj.ip_address = parent_entity.get_field_value('hsrp_standby_ip')
    hsrp_obj.group = parent_entity.get_field_value('hsrp_group')
    if parent_entity.get_field_value('hsrp_preempt') == 'true':
        hsrp_obj.hsrp_preempt = parent_entity.get_field_value('hsrp_preempt')
        hsrp_obj.preempt_reload = parent_entity.get_field_value('hsrp_preempt_reload_delay')
    hsrp_obj.auth_type = parent_entity.get_field_value('auth_type')
    hsrp_obj.auth_key = parent_entity.get_field_value('auth_password')
    if parent_entity.get_field_value('hsrp_timers') == 'true':
        if util.isNotEmpty(parent_entity.get_field_value('hello_interval_sec')):
            hsrp_obj.timer1_msec = 'false'
            hsrp_obj.timer1 = parent_entity.get_field_value('hello_interval_sec')
        if util.isNotEmpty(parent_entity.get_field_value('hello_interval_msec')):
            hsrp_obj.timer1_msec = 'true'
            hsrp_obj.timer1 = parent_entity.get_field_value('hello_interval_msec')
        if util.isNotEmpty(parent_entity.get_field_value('hold_time_sec')):
            hsrp_obj.timer2_msec = 'false'
            hsrp_obj.timer2 = parent_entity.get_field_value('hold_time_sec')
        if util.isNotEmpty(parent_entity.get_field_value('hold_time_msec')):
            hsrp_obj.timer2_msec = 'true'
            hsrp_obj.timer2 = parent_entity.get_field_value('hold_time_msec')
    if 'hsrp_priority' in kwargs['inputdict']:
        if util.isNotEmpty(kwargs['inputdict']['hsrp_priority']):
            hsrp_obj.priority = kwargs['inputdict']['hsrp_priority']

    if 'track' in kwargs['inputdict']:
        if util.isNotEmpty(kwargs['inputdict']['track']):
            hsrp_obj.track = kwargs['inputdict']['track']
            if 'decrement' in kwargs['inputdict']:
                if util.isNotEmpty(kwargs['inputdict']['decrement']):
                    hsrp_obj.decrement = kwargs['inputdict']['decrement']

    if mode == "sub-interface" or mode == "l3-interface":
        hsrp_url = device.url + "/interfaces/interface=%s" % util.make_interfacename(interface_name)
        print 'hsrp_url:', hsrp_url
        if util.isNotEmpty(hsrp_obj.getxml(filter=True)):
            hsrp_obj.version = parent_entity.get_field_value('hsrp_version')
            yang.Sdk.createData(hsrp_url, hsrp_obj.getxml(filter=True), sdata.getSession())

    ospf_obj = devices.device.interfaces.interface.ospf.ospf()
    ospf_new = devices.device.vrfs.vrf.router_ospf.router_ospf()
    ospf_net_obj = devices.device.vrfs.vrf.router_ospf.network.network()
    if 'ospf' in kwargs['inputdict']:
        if kwargs['inputdict']['ospf'] == 'true':
            if 'priority' in kwargs['inputdict']:
                if util.isNotEmpty(kwargs['inputdict']['priority']):
                    ospf_obj.priority = kwargs['inputdict']['priority']
            if 'cost' in kwargs['inputdict']:
                if util.isNotEmpty(kwargs['inputdict']['cost']):
                    ospf_obj.cost = kwargs['inputdict']['cost']
            if kwargs['inputdict']['fast_hello'] == 'false':
                if 'hello_interval' in kwargs['inputdict']:
                    if util.isNotEmpty(kwargs['inputdict']['hello_interval']):
                        ospf_obj.hello_interval = kwargs['inputdict']['hello_interval']
                if 'dead_interval' in kwargs['inputdict']:
                    if util.isNotEmpty(kwargs['inputdict']['dead_interval']):
                        ospf_obj.dead_interval = kwargs['inputdict']['dead_interval']
            if kwargs['inputdict']['fast_hello'] == 'true':
                if 'hello_multiplier' in kwargs['inputdict']:
                    if util.isNotEmpty(kwargs['inputdict']['hello_multiplier']):
                        ospf_obj.hello_multiplier = kwargs['inputdict']['hello_multiplier']
            if 'ospf_id' in kwargs['inputdict']:
                if util.isNotEmpty(kwargs['inputdict']['ospf_id']):
                    ospf_new.process_id = kwargs['inputdict']['ospf_id']

            if 'area' in kwargs['inputdict']:
                if util.isNotEmpty(kwargs['inputdict']['area']):
                    ospf_net_obj.ip_address = interface_ip
                    ospf_net_obj.wild_card = wildcard
                    ospf_net_obj.area = kwargs['inputdict']['area']

    if mode == "sub-interface" or mode == "l3-interface":
        ospf_url = device.url + "/interfaces/interface=%s" % util.make_interfacename(interface_name)
        print 'ospf_url:', ospf_url
        if util.isNotEmpty(ospf_obj.getxml(filter=True)):
            yang.Sdk.createData(ospf_url, ospf_obj.getxml(filter=True), sdata.getSession())

        if 'ospf_id' in kwargs['inputdict']:
            ospf_net_url = device.url + '/vrfs/vrf=%s/router-ospf=%s' % (vrf, kwargs['inputdict']['ospf_id'])
            ospf_networks_url1 = device.url + '/vrfs/vrf=%s' % (vrf)
            if util.isNotEmpty(ospf_net_obj.getxml(filter=True)):
                #yang.Sdk.createData(ospf_networks_url1, ospf_new.getxml(filter=True), sdata.getSession())
                yang.Sdk.createData(ospf_net_url, ospf_net_obj.getxml(filter=True), sdata.getSession())

    # creating entities for update services
    if entity == "customer_lan_ic":
        uri = sdata.getRcPath()
        parent_uri = uri[:uri.rfind(uri.split('/')[-2])]
        print parent_uri
        yang.Sdk.createData('%spolicy-update-services' % parent_uri, '<hsrp-update-service/>', sdata.getSession(), False)


def new_back_endpoint(entity, smodelctx, sdata, device, **kwargs):
    inputdict = kwargs['inputdict']
    profile_name = inputdict['profile_name']
    if util.isEmpty(profile_name):
        raise Exception("Profile name in cpe-lan/cpe's interconnect can not be empty.")
    vrf = inputdict['vrf']
    interface_type = inputdict['interface_type']
    interface_name = inputdict['interface_name']
    if interface_type == "Physical" or interface_type == "Sub-Interface":
        if util.isEmpty(interface_name):
            raise Exception("interface_name should not be empty when interface_type is Physical and sub-interface")

    interface_description = inputdict['interface_description']
    interface_ip = inputdict['interface_ip']
    device_ip = inputdict['device_ip']
    global_inbound_acl = inputdict['global_inbound_acl']
    site_inbound_acl = inputdict['site_inbound_acl']
    global_outbound_acl = inputdict['global_outbound_acl']
    site_outbound_acl = inputdict['site_outbound_acl']
    nat_inside = None
    nat_outside = None
    if entity == "customer_lan_ic_dual" or entity == "customer_lan_ic_triple":
        nat_inside = inputdict['nat_inside']
        nat_outside = inputdict['nat_outside']
    #vlan_id = None
    vlan_id = inputdict['vlan_id']
    if util.isNotEmpty(interface_name):
        if '.' not in interface_name and interface_type == "Sub-Interface":
            if util.isEmpty(vlan_id):
                raise Exception("vlan_id should not be empty when interface_type is Sub-Interface")

    if interface_type == "SVI":
        if util.isEmpty(vlan_id):
            raise Exception("vlan_id should not empty when interface_type is SVI")

    if 'hsrp_priority' in inputdict:
        hsrp_priority = inputdict['hsrp_priority']
    else:
        hsrp_priority = None

    mode = None
    cidr = None
    link_negotiation = None
    netmask = None
    if util.isEmpty(vrf):
        vrf = 'GLOBAL'
    parent_entity = None
    access_lists = []
    if entity == "cpe_primary_cpe_secondary_ic_dual":
        obj = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
        parent_entity = obj.dual_cpe_dual_wan_site_services.cpe_primary_cpe_secondary_ic
        if device_ip == obj.dual_cpe_dual_wan_site_services.cpe_primary.device_ip:
            if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
        if device_ip == obj.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip:
            if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
    elif entity == "cpe_primary_cpe_secondary_ic_triple":
        obj = getLocalObject(sdata, 'triple-cpe-site-services')
        parent_entity = obj.triple_cpe_site_services.cpe_primary_cpe_secondary_ic
        if device_ip == obj.triple_cpe_site_services.cpe_primary.device_ip:
            if hasattr(obj.triple_cpe_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
        if device_ip == obj.triple_cpe_site_services.cpe_secondary.device_ip:
            if hasattr(obj.triple_cpe_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
    elif entity == "cpe_secondary_cpe_tertiary_ic_triple":
        obj = getLocalObject(sdata, 'triple-cpe-site-services')
        parent_entity = obj.triple_cpe_site_services.cpe_secondary_cpe_tertiary_ic
        if device_ip == obj.triple_cpe_site_services.cpe_primary.device_ip:
            if hasattr(obj.triple_cpe_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
        if device_ip == obj.triple_cpe_site_services.cpe_secondary.device_ip:
            if hasattr(obj.triple_cpe_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
    elif entity == "cpe_tertiary_cpe_primary_ic_triple":
        obj = getLocalObject(sdata, 'triple-cpe-site-services')
        parent_entity = obj.triple_cpe_site_services.cpe_tertiary_cpe_primary_ic
        if device_ip == obj.triple_cpe_site_services.cpe_primary.device_ip:
            if hasattr(obj.triple_cpe_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
        if device_ip == obj.triple_cpe_site_services.cpe_secondary.device_ip:
            if hasattr(obj.triple_cpe_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
    elif entity == "customer_lan_ic_dual":
        obj = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
        if device_ip == obj.dual_cpe_dual_wan_site_services.cpe_primary.device_ip:
            if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_dual_wan_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
        if device_ip == obj.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip:
            if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.dual_cpe_dual_wan_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
    elif entity == "customer_lan_ic_triple":
        obj = getLocalObject(sdata, 'triple-cpe-site-services')
        if device_ip == obj.triple_cpe_site_services.cpe_primary.device_ip:
            if hasattr(obj.triple_cpe_site_services.cpe_primary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_primary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_primary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_primary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_primary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)
        if device_ip == obj.triple_cpe_site_services.cpe_secondary.device_ip:
            if hasattr(obj.triple_cpe_site_services.cpe_secondary, 'access_lists'):
                if hasattr(obj.triple_cpe_site_services.cpe_secondary.access_lists, 'access_list'):
                    obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list = util.convert_to_list(obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list)
                    for access_list_dynamic in obj.triple_cpe_site_services.cpe_secondary.access_lists.access_list:
                        access_list_name = access_list_dynamic.name
                        access_lists.append(access_list_name)

    if entity == "customer_lan_ic_dual":
        obj = getLocalObject(sdata, 'cpe-lan')
        if hasattr(obj.cpe_lan, 'lan_profile'):
            lan_prof = 'false'
            obj.cpe_lan.lan_profile = util.convert_to_list(obj.cpe_lan.lan_profile)
            for lanprof in obj.cpe_lan.lan_profile:
                if lanprof.profile_name == profile_name:
                    lan_prof = 'true'
                    parent_entity = lanprof
            if lan_prof != 'true':
                raise Exception("Invalid Profile Name")
        else:
            raise Exception("No lan profile found")
    elif entity == "cpe_primary_cpe_secondary_ic_dual":
        obj = getLocalObject(sdata, 'cpe-primary-cpe-secondary-ic')
        if hasattr(obj.cpe_primary_cpe_secondary_ic, 'ic_profile'):
            ic_prof = 'false'
            obj.cpe_primary_cpe_secondary_ic.ic_profile = util.convert_to_list(obj.cpe_primary_cpe_secondary_ic.ic_profile)
            for lanprof in obj.cpe_primary_cpe_secondary_ic.ic_profile:
                if lanprof.profile_name == profile_name:
                    ic_prof = 'true'
                    parent_entity = lanprof
            if ic_prof != 'true':
                raise Exception("Invalid Profile Name")
        else:
            raise Exception("No ic profile found")
    elif entity == "cpe_primary_cpe_secondary_ic_triple":
        obj = getLocalObject(sdata, 'cpe-primary-cpe-secondary-ic')
        if hasattr(obj.cpe_primary_cpe_secondary_ic, 'ic_profile'):
            ic_prof = 'false'
            obj.cpe_primary_cpe_secondary_ic.ic_profile = util.convert_to_list(obj.cpe_primary_cpe_secondary_ic.ic_profile)
            for lanprof in obj.cpe_primary_cpe_secondary_ic.ic_profile:
                if lanprof.profile_name == profile_name:
                    ic_prof = 'true'
                    parent_entity = lanprof
            if ic_prof != 'true':
                raise Exception("Invalid Profile Name")
        else:
            raise Exception("No ic profile found")
    elif entity == "cpe_secondary_cpe_tertiary_ic_triple":
        obj = getLocalObject(sdata, 'cpe-secondary-cpe-tertiary-ic')
        if hasattr(obj.cpe_secondary_cpe_tertiary_ic, 'ic_profile'):
            ic_prof = 'false'
            obj.cpe_secondary_cpe_tertiary_ic.ic_profile = util.convert_to_list(obj.cpe_secondary_cpe_tertiary_ic.ic_profile)
            for lanprof in obj.cpe_secondary_cpe_tertiary_ic.ic_profile:
                if lanprof.profile_name == profile_name:
                    ic_prof = 'true'
                    parent_entity = lanprof
            if ic_prof != 'true':
                raise Exception("Invalid Profile Name")
        else:
            raise Exception("No ic profile found")
    elif entity == "cpe_tertiary_cpe_primary_ic_triple":
        obj = getLocalObject(sdata, 'cpe-tertiary-cpe-primary-ic')
        if hasattr(obj.cpe_tertiary_cpe_primary_ic, 'ic_profile'):
            ic_prof = 'false'
            obj.cpe_tertiary_cpe_primary_ic.ic_profile = util.convert_to_list(obj.cpe_tertiary_cpe_primary_ic.ic_profile)
            for lanprof in obj.cpe_tertiary_cpe_primary_ic.ic_profile:
                if lanprof.profile_name == profile_name:
                    ic_prof = 'true'
                    parent_entity = lanprof
            if ic_prof != 'true':
                raise Exception("Invalid Profile Name")
        else:
            raise Exception("No ic profile found")
    elif entity == "customer_lan_ic_triple":
        obj = getLocalObject(sdata, 'cpe-lan')
        if hasattr(obj.cpe_lan, 'lan_profile'):
            lan_prof = 'false'
            obj.cpe_lan.lan_profile = util.convert_to_list(obj.cpe_lan.lan_profile)
            for lanprof in obj.cpe_lan.lan_profile:
                if lanprof.profile_name == profile_name:
                    lan_prof = 'true'
                    parent_entity = lanprof
            if lan_prof != 'true':
                raise Exception("Invalid Profile Name")
        else:
            raise Exception("No lan profile found")
    if hasattr(parent_entity, 'auto_negotiation'):
        auto_negotiation = parent_entity.auto_negotiation
    else:
        auto_negotiation = None
    if hasattr(parent_entity, 'speed'):
        speed = parent_entity.speed
    else:
        speed = None
    if hasattr(parent_entity, 'duplex'):
        duplex = parent_entity.duplex
    else:
        duplex = None
    if hasattr(parent_entity, 'inbound_policy'):
        inbound_policy = parent_entity.inbound_policy
    else:
        inbound_policy = None
    if hasattr(parent_entity, 'load_interval'):
        load_interval = parent_entity.load_interval
    else:
        load_interval = None
    if hasattr(parent_entity, 'load_interval_delay'):
        load_interval_delay = parent_entity.load_interval_delay
    else:
        load_interval_delay = None
    if hasattr(parent_entity, 'hold_queue_in'):
        hold_queue_in = parent_entity.hold_queue_in
    else:
        hold_queue_in = None
    if hasattr(parent_entity, 'in_queue_length'):
        in_queue_length = parent_entity.in_queue_length
    else:
        in_queue_length = None
    if hasattr(parent_entity, 'hold_queue_out'):
        hold_queue_out = parent_entity.hold_queue_out
    else:
        hold_queue_out = None
    if hasattr(parent_entity, 'out_queue_length'):
        out_queue_length = parent_entity.out_queue_length
    else:
        out_queue_length = None
    if hasattr(parent_entity, 'hierarchical_inbound_policy'):
        hierarchical_inbound_policy = parent_entity.hierarchical_inbound_policy
    else:
        hierarchical_inbound_policy = None
    if hasattr(parent_entity, 'hierarchical_policy'):
        hierarchical_policy = parent_entity.hierarchical_policy
    else:
        hierarchical_policy = None
    if hasattr(parent_entity, 'cidr'):
        cidr = parent_entity.cidr

    if hierarchical_inbound_policy == 'false':
        if util.isNotEmpty(inbound_policy):
            qos_child(entity, inbound_policy, device, sdata)
    elif hierarchical_inbound_policy == 'true':
        if util.isNotEmpty(hierarchical_policy):
            hierarchical_policy_class(entity, hierarchical_policy, device, sdata)

    next_ip_address = None
    ip_addr = None
    if entity == "cpe_primary_cpe_secondary_ic_dual" or entity == "cpe_primary_cpe_secondary_ic_triple" or entity == "cpe_secondary_cpe_tertiary_ic_triple" or entity == "cpe_tertiary_cpe_primary_ic_triple":
        ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr)
    else:
        prefix = util.IPPrefix(cidr)
        if str(prefix.masklen) == str(32):
            raise Exception("Bad mask /32 for address")
        obj_cidr = getLocalObject(sdata, 'customer')
        if entity == "customer_lan_ic_dual":
            obj_site = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
            cidr_name = obj_cidr.customer.name + '_' + obj_site.dual_cpe_dual_wan_site_services.site_name + '_' + cidr
            cidr_gateway = util.next_ip_address(prefix.address)
            rp = obj_site.dual_cpe_dual_wan_site_services.resource_pool
        elif entity == "customer_lan_ic_triple":
            obj_site = getLocalObject(sdata, 'triple-cpe-site-services')
            cidr_name = obj_cidr.customer.name + '_' + obj_site.triple_cpe_site_services.site_name + '_' + cidr
            cidr_gateway = util.next_ip_address(prefix.address)
            rp = obj_site.triple_cpe_site_services.resource_pool

        payload = '''<ipaddress-pool>
                    <name>'''+cidr_name+'''</name>
                    <cidr>'''+cidr+'''</cidr>
                    <gateway>'''+cidr_gateway+'''</gateway>
                    <resource-pool>'''+rp+'''</resource-pool>
                    </ipaddress-pool>'''
        cidr_url = "/app/restconf/data/ipam:ipaddress-pools"

        try:
            cidr_name_local = cidr_name
            cidr_name_local = cidr_name_local.replace('/', '%2F')
            get_ipaddress_pool_url = "/app/restconf/data/ipam:ipaddress-pools/ipaddress-pool=%s" %(cidr_name_local)
            pool = yang.Sdk.getData(get_ipaddress_pool_url, '', sdata.getTaskId())
            pool = util.parseXmlString(pool)
        except DataNodeNotFoundException:
            yang.Sdk.createData(cidr_url, payload, sdata.getSession())
        ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr_name)
    ip_addr_obj = ip_addr.ipam_pool_obj
    prefix = util.IPPrefix(ip_addr_obj.cidr)
    netmask = prefix.netmask
    wildcard = prefix.wildcard
    if util.isEmpty(interface_ip) or interface_ip == None:
        used_ips_list = get_used_ip_list_from_ippool(ip_addr_obj.name, sdata)
        interface_ip = get_freeip_from_cidr(ip_addr_obj.cidr, used_ips_list)
        add_ipaddress_entries(ip_addr_obj.name, interface_ip, sdata)
        # next_ip_address = ipam.IPAM.getInstance().allocateIpAddressInIpam(ip_addr_obj.name, kwargs['inputdict']['endpoint_name'])
    else:
        used_ips_list = get_used_ip_list_from_ippool(ip_addr_obj.name, sdata)
        if used_ips_list.__len__() >= 0:
            if str(prefix.masklen) != str(32):
                if interface_ip in used_ips_list:
                    raise Exception("IP given is already used in the given pool")
            used_ips_list.sort()
            if entity == "cpe_primary_cpe_secondary_ic_dual" or entity == "cpe_primary_cpe_secondary_ic_triple" or entity == "cpe_secondary_cpe_tertiary_ic_triple" or entity == "cpe_tertiary_cpe_primary_ic_triple":
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
        # next_ip_address = ipam.IPAM.getInstance().allocateIpAddressInIpam(ip_addr_obj.name, kwargs['inputdict']['endpoint_name'], interface_ip)
    payload = "<interface-ip>%s</interface-ip>" % interface_ip
    serv_uri = sdata.getRcPath()
    yang.Sdk.createData(serv_uri, payload, sdata.getSession())

    if interface_type == "Physical" or interface_type == "Sub-Interface":
        if util.isEmpty(interface_name):
            raise Exception("interface_name should not be empty when interface_type is Physical and sub-interface")
    int_name_phy = interface_name
    if interface_type == "Physical":
        mode = "l3-interface"
    elif interface_type == "Sub-Interface":
        mode = "sub-interface"
        if vlan_id is not None:
            interface_name = interface_name + '.' + str(vlan_id)
    elif interface_type == "SVI":
        mode = "vlan"
    if auto_negotiation == "true":
        link_negotiation = "auto"

    intf_obj = devices.device.interfaces.interface.interface()
    if mode == "sub-interface" or mode == "l3-interface":
        intf_obj.name = interface_name
        intf_obj.long_name = interface_name
    intf_obj.description = interface_description
    if mode == "sub-interface":
        intf_obj.mode = "sub-interface"
        intf_obj.vlan = vlan_id
    elif mode == "vlan":
        intf_obj.mode = "vlan"
        intf_obj.vlan = vlan_id
        intf_obj.long_name = "Vlan" + str(vlan_id)
        intf_obj.name = "Vlan" + str(vlan_id)
    else:
        intf_obj.mode = "l3-interface"
    intf_obj.ip_address = interface_ip
    intf_obj.netmask = netmask
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    if mode == "sub-interface" or mode == "l3-interface":
        if vrf is not None and vrf != 'GLOBAL':
            xml_output = yang.Sdk.getData(url+"/vrfs/vrf="+str(vrf), '', sdata.getTaskId())
            obj_local = util.parseXmlString(xml_output)
            util.log_debug("obj_local: ", obj_local)
            intf_obj.vrf_definition_mode = obj_local.vrf.vrf_definition_mode
            intf_obj.vrf = vrf
        if entity != "cpe_primary_cpe_secondary_ic_dual" and entity != "cpe_primary_cpe_secondary_ic_triple" and entity != "cpe_secondary_cpe_tertiary_ic_triple" and entity != "cpe_tertiary_cpe_primary_ic_triple":
            if util.isNotEmpty(inputdict['pbr_policy']):
                route_maps(inputdict['pbr_policy'], device, sdata)
                intf_obj.pbr_policy = inputdict['pbr_policy']
        if hierarchical_inbound_policy == 'false':
            if util.isNotEmpty(inbound_policy):
                intf_obj.inbound_qos = inbound_policy
        elif hierarchical_inbound_policy == 'true':
            if util.isNotEmpty(hierarchical_policy):
                intf_obj.inbound_qos = hierarchical_policy
        if util.isNotEmpty(global_inbound_acl):
            access_group_def(url, global_inbound_acl, device, sdata)
            intf_obj.acl_inbound_name = global_inbound_acl
        if util.isNotEmpty(global_outbound_acl):
            access_group_def(url, global_outbound_acl, device, sdata)
            intf_obj.acl_outbound_name = global_outbound_acl
        if util.isNotEmpty(site_inbound_acl):
            if site_inbound_acl in access_lists:
                intf_obj.acl_inbound_name = site_inbound_acl
            else:
                raise Exception("Make sure that provided site_inbound_acl should be present on router access-lists")
        if util.isNotEmpty(site_outbound_acl):
            if site_outbound_acl in access_lists:
                intf_obj.acl_outbound_name = site_outbound_acl
            else:
                raise Exception("Make sure that provided site_outbound_acl should be present on router access-lists")
        if nat_inside == 'true':
            intf_obj.nat_name = 'inside'
        elif nat_outside == 'true':
            intf_obj.nat_name = 'outside'
    if interface_type == "Physical":
        if link_negotiation is not None:
            intf_obj.link_negotiation = link_negotiation
        if auto_negotiation != "true":
            if util.isNotEmpty(speed):
                intf_obj.speed = speed
            if util.isNotEmpty(duplex):
                intf_obj.duplex = duplex
        if load_interval == 'true':
            if util.isNotEmpty(load_interval_delay):
                intf_obj.load_interval_delay = load_interval_delay
        if hold_queue_in == 'true':
            if util.isNotEmpty(in_queue_length):
                intf_obj.in_queue_length = in_queue_length
        if hold_queue_out == 'true':
            if util.isNotEmpty(out_queue_length):
                intf_obj.out_queue_length = out_queue_length
        yang.Sdk.createData(device.url+'/interfaces', intf_obj.getxml(filter=True), sdata.getSession(), False)
    else:
        yang.Sdk.createData(device.url+'/interfaces', intf_obj.getxml(filter=True), sdata.getSession(), False)

    if mode == "sub-interface":
        intf_obj_phy = devices.device.interfaces.interface.interface()
        intf_obj_phy.name = int_name_phy
        intf_obj_phy.long_name = int_name_phy
        intf_obj_phy.mode = "l3-interface"
        if link_negotiation is not None:
            intf_obj_phy.link_negotiation = link_negotiation
        if auto_negotiation != "true":
            if util.isNotEmpty(speed):
                intf_obj_phy.speed = speed
            if util.isNotEmpty(duplex):
                intf_obj_phy.duplex = duplex
        if load_interval == 'true':
            if util.isNotEmpty(load_interval_delay):
                intf_obj_phy.load_interval_delay = load_interval_delay
        if hold_queue_in == 'true':
            if util.isNotEmpty(in_queue_length):
                intf_obj_phy.in_queue_length = in_queue_length
        if hold_queue_out == 'true':
            if util.isNotEmpty(out_queue_length):
                intf_obj_phy.out_queue_length = out_queue_length
        yang.Sdk.createData(device.url+'/interfaces', intf_obj_phy.getxml(filter=True), sdata.getSession(), False)

    # creating hsrp policy on the given interface
    hsrp_obj = devices.device.interfaces.interface.hsrp.hsrp()

    hsrp_obj.ip_address = parent_entity.get_field_value('hsrp_standby_ip')
    hsrp_obj.group = parent_entity.get_field_value('hsrp_group')
    if parent_entity.get_field_value('hsrp_preempt') == 'true':
        hsrp_obj.hsrp_preempt = parent_entity.get_field_value('hsrp_preempt')
        hsrp_obj.preempt_reload = parent_entity.get_field_value('hsrp_preempt_reload_delay')
    hsrp_obj.auth_type = parent_entity.get_field_value('auth_type')
    hsrp_obj.auth_key = parent_entity.get_field_value('auth_password')
    if parent_entity.get_field_value('hsrp_timers') == 'true':
        if util.isNotEmpty(parent_entity.get_field_value('hello_interval_sec')):
            hsrp_obj.timer1_msec = 'false'
            hsrp_obj.timer1 = parent_entity.get_field_value('hello_interval_sec')
        if util.isNotEmpty(parent_entity.get_field_value('hello_interval_msec')):
            hsrp_obj.timer1_msec = 'true'
            hsrp_obj.timer1 = parent_entity.get_field_value('hello_interval_msec')
        if util.isNotEmpty(parent_entity.get_field_value('hold_time_sec')):
            hsrp_obj.timer2_msec = 'false'
            hsrp_obj.timer2 = parent_entity.get_field_value('hold_time_sec')
        if util.isNotEmpty(parent_entity.get_field_value('hold_time_msec')):
            hsrp_obj.timer2_msec = 'true'
            hsrp_obj.timer2 = parent_entity.get_field_value('hold_time_msec')
    if 'hsrp_priority' in kwargs['inputdict']:
        if util.isNotEmpty(kwargs['inputdict']['hsrp_priority']):
            hsrp_obj.priority = kwargs['inputdict']['hsrp_priority']

    if 'track' in kwargs['inputdict']:
        if util.isNotEmpty(kwargs['inputdict']['track']):
            hsrp_obj.track = kwargs['inputdict']['track']
            if 'decrement' in kwargs['inputdict']:
                if util.isNotEmpty(kwargs['inputdict']['decrement']):
                    hsrp_obj.decrement = kwargs['inputdict']['decrement']

    if mode == "sub-interface" or mode == "l3-interface":
        hsrp_url = device.url + "/interfaces/interface=%s" % util.make_interfacename(interface_name)
        print 'hsrp_url:', hsrp_url
        if util.isNotEmpty(hsrp_obj.getxml(filter=True)):
            hsrp_obj.version = parent_entity.get_field_value('hsrp_version')
            yang.Sdk.createData(hsrp_url, hsrp_obj.getxml(filter=True), sdata.getSession())

    ospf_obj = devices.device.interfaces.interface.ospf.ospf()
    ospf_new = devices.device.vrfs.vrf.router_ospf.router_ospf()
    ospf_net_obj = devices.device.vrfs.vrf.router_ospf.network.network()
    if 'ospf' in kwargs['inputdict']:
        if kwargs['inputdict']['ospf'] == 'true':
            if 'priority' in kwargs['inputdict']:
                if util.isNotEmpty(kwargs['inputdict']['priority']):
                    ospf_obj.priority = kwargs['inputdict']['priority']
            if 'cost' in kwargs['inputdict']:
                if util.isNotEmpty(kwargs['inputdict']['cost']):
                    ospf_obj.cost = kwargs['inputdict']['cost']
            if kwargs['inputdict']['fast_hello'] == 'false':
                if 'hello_interval' in kwargs['inputdict']:
                    if util.isNotEmpty(kwargs['inputdict']['hello_interval']):
                        ospf_obj.hello_interval = kwargs['inputdict']['hello_interval']
                if 'dead_interval' in kwargs['inputdict']:
                    if util.isNotEmpty(kwargs['inputdict']['dead_interval']):
                        ospf_obj.dead_interval = kwargs['inputdict']['dead_interval']
            if kwargs['inputdict']['fast_hello'] == 'true':
                if 'hello_multiplier' in kwargs['inputdict']:
                    if util.isNotEmpty(kwargs['inputdict']['hello_multiplier']):
                        ospf_obj.hello_multiplier = kwargs['inputdict']['hello_multiplier']
            if 'ospf_id' in kwargs['inputdict']:
                if util.isNotEmpty(kwargs['inputdict']['ospf_id']):
                    ospf_new.process_id = kwargs['inputdict']['ospf_id']

            if 'area' in kwargs['inputdict']:
                if util.isNotEmpty(kwargs['inputdict']['area']):
                    ospf_net_obj.ip_address = interface_ip
                    ospf_net_obj.wild_card = wildcard
                    ospf_net_obj.area = kwargs['inputdict']['area']

    if mode == "sub-interface" or mode == "l3-interface":
        ospf_url = device.url + "/interfaces/interface=%s" % util.make_interfacename(interface_name)
        print 'ospf_url:', ospf_url
        if util.isNotEmpty(ospf_obj.getxml(filter=True)):
            yang.Sdk.createData(ospf_url, ospf_obj.getxml(filter=True), sdata.getSession())

        if 'ospf_id' in kwargs['inputdict']:
            ospf_net_url = device.url + '/vrfs/vrf=%s/router-ospf=%s' % (vrf, kwargs['inputdict']['ospf_id'])
            ospf_networks_url1 = device.url + '/vrfs/vrf=%s' % (vrf)
            if util.isNotEmpty(ospf_net_obj.getxml(filter=True)):
                #yang.Sdk.createData(ospf_networks_url1, ospf_new.getxml(filter=True), sdata.getSession())
                yang.Sdk.createData(ospf_net_url, ospf_net_obj.getxml(filter=True), sdata.getSession())

    # creating entities for update services
    if entity == "customer_lan_ic_dual" or entity == "customer_lan_ic_triple":
        uri = sdata.getRcPath()
        parent_uri = uri[:uri.rfind(uri.split('/')[-2])]
        print parent_uri
        yang.Sdk.createData('%spolicy-update-services' % parent_uri, '<hsrp-update-service/>', sdata.getSession(), False)


def update_hsrp_priority(entity, smodelctx, sdata, device, **kwarg):
    config = util.parseXmlString(sdata.getPayload())
    config = config.end_points
    vrf = config.get_field_value('vrf')
    hsrp_priority = config.get_field_value('hsrp_priority')
    # interface_type = config.get_field_value('interface_type')
    # interface_name = config.get_field_value('interface_name')
    track = config.get_field_value('track')
    decrement = config.get_field_value('decrement')

    prevconfig = util.parseXmlString(sdata.getPreviousPayload())
    prevconfig = prevconfig.end_points
    prev_hsrp_priority = prevconfig.get_field_value('hsrp_priority')
    prev_track = prevconfig.get_field_value('track')
    prev_decrement = prevconfig.get_field_value('decrement')
    interface_type = prevconfig.get_field_value('interface_type')
    interface_name = prevconfig.get_field_value('interface_name')

    if vrf is None:
        vrf = "GLOBAL"

    if entity == 'customer_lan_ic':
        obj = getLocalObject(sdata, 'dual-cpe-site-services')
        parent_entity = obj.dual_cpe_site_services.cpe_lan
    elif entity == 'customer_lan_ic_dual':
        obj = getLocalObject(sdata, 'dual-cpe-dual-wan-site-services')
        parent_entity = obj.dual_cpe_dual_wan_site_services.cpe_lan
    elif entity == 'customer_lan_ic_triple':
        obj = getLocalObject(sdata, 'triple-cpe-site-services')
        parent_entity = obj.triple_cpe_site_services.cpe_lan
    else:
        raise Exception('Unknown exception occured')
    vlan_id = None
    cidr = None
    if hasattr(parent_entity.end_points, 'vlan_id'):
        vlan_id = parent_entity.end_points.vlan_id
    if hasattr(parent_entity, 'cidr'):
        cidr = parent_entity.cidr

    if interface_type == "Physical":
        mode = "l3-interface"
    elif interface_type == "Sub-Interface":
        mode = "sub-interface"
        if vlan_id is not None:
            interface_name = interface_name + '.' + str(vlan_id)

    # creating hsrp policy on the given interface
    hsrp_obj = devices.device.interfaces.interface.hsrp.hsrp()
    if hsrp_priority != prev_hsrp_priority or track != prev_track or decrement != prev_decrement:
        hsrp_obj.priority = hsrp_priority
        hsrp_obj.track = track
        hsrp_obj.decrement = decrement
    hsrp_obj.group = parent_entity.get_field_value('hsrp_group')
    hsrp_url = device.url + "/interfaces/interface=%s" % util.make_interfacename(interface_name)
    print 'hsrp_url:', hsrp_url
    if util.isNotEmpty(hsrp_obj.getxml(filter=True)):
        yang.Sdk.createData(hsrp_url, hsrp_obj.getxml(filter=True), sdata.getSession(), False)


def modifiedGetLocalObject(sdata, elem):
    smodelctx = ServiceModelContext(id, sdata)
    rcpath = sdata.getRcPath() + '/'
    print 'rcpath = %s' % (rcpath)
    pattern = '/controller:services'
    idx = rcpath.find(pattern)
    if idx < 0:
        print 'cant find pattern in rcpath = %s' % (rcpath)
        return rcpath
    idx = rcpath.find(elem, idx)
    if idx < 0:
        print 'cant find pattern in rcpath = %s' % (rcpath)
        return rcpath
    idx = rcpath.find('/', idx)
    print 'idx = %d' % (idx)
    if idx < 0:
        print 'cant find / in rcpath = %s, idx = %d' % (rcpath, idx)
        return rcpath
    print 'rcpath = %s, new = %s' % (rcpath, rcpath[:idx])
    rcpath = rcpath[:idx]
    print 'setting rcpath= %s' % (rcpath)

    xml_output = yang.Sdk.getData(rcpath, '', smodelctx.task_id)
    obj = util.parseXmlString(xml_output)
    return obj

def get_device_by_id(sdata, dev_id):
    key = 'deviceid.%s' % (dev_id)
    dev = sdata.getSessionItem(key)
    if dev != None:
        util.log_debug('get_device_by_id:cache-hit key=%s' % (key))
        return dev
    util.log_debug('get_device_by_id:cache-miss key=%s' % (key))
    dev = devicemgr.getDeviceById(dev_id)
    if dev != None:
        sdata.setSessionItem(key, dev, True)
    return dev

def update_shape_avg(sdata, entity):
    device = None
    config = util.parseXmlString(sdata.getPayload())
    prevconfig = util.parseXmlString(sdata.getPreviousPayload())
    util.log_debug( "prevconfig is:", prevconfig)
    if entity == 'cpe':
        config = config.cpe_wan
        prevconfig = prevconfig.cpe_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_primary':
        config = config.cpe_primary_wan
        prevconfig = prevconfig.cpe_primary_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_secondary':
        config = config.cpe_secondary_wan
        prevconfig = prevconfig.cpe_secondary_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_primary_dual':
        config = config.cpe_primary_wan
        prevconfig = prevconfig.cpe_primary_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_secondary_dual':
        config = config.cpe_secondary_wan
        prevconfig = prevconfig.cpe_secondary_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_primary_inet_dual':
        config = config.cpe_primary_inet_wan
        prevconfig = prevconfig.cpe_primary_inet_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_primary_mpls_dual':
        config = config.cpe_primary_mpls_wan
        prevconfig = prevconfig.cpe_primary_mpls_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_secondary_inet_dual':
        config = config.cpe_secondary_inet_wan
        prevconfig = prevconfig.cpe_secondary_inet_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_secondary_mpls_dual':
        config = config.cpe_secondary_mpls_wan
        prevconfig = prevconfig.cpe_secondary_mpls_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_primary_inet_triple':
        config = config.cpe_primary_inet_wan
        prevconfig = prevconfig.cpe_primary_inet_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_primary_mpls_triple':
        config = config.cpe_primary_mpls_wan
        prevconfig = prevconfig.cpe_primary_mpls_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_secondary_inet_triple':
        config = config.cpe_secondary_inet_wan
        prevconfig = prevconfig.cpe_secondary_inet_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_secondary_mpls_triple':
        config = config.cpe_secondary_mpls_wan
        prevconfig = prevconfig.cpe_secondary_mpls_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_tertiary_inet_triple':
        config = config.cpe_tertiary_inet_wan
        prevconfig = prevconfig.cpe_tertiary_inet_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    elif entity == 'cpe_tertiary_mpls_triple':
        config = config.cpe_tertiary_mpls_wan
        prevconfig = prevconfig.cpe_tertiary_mpls_wan
        obj = util.convert_to_list(prevconfig.end_points)
        dev = None
        for endpoint in obj:
            dev = endpoint.device_ip
        device = get_device_by_id(sdata, dev)
    shape_average = config.get_field_value('shape_average')
    # child_qos_policy = config.get_field_value('child_qos_policy')

    prev_policy_name = prevconfig.get_field_value('policy_name')
    prev_shape_average = prevconfig.get_field_value('shape_average')
    print "prevpolicyname is:", prev_policy_name
    print "prevshapeavg is:", prev_shape_average

    map_obj = devices.device.policy_maps.policy_map.policy_map()
    map_obj.name = prev_policy_name
    yang.Sdk.createData(device.url+"/policy-maps", map_obj.getxml(filter=True), sdata.getSession(), False)

    cls_obj = devices.device.policy_maps.policy_map.class_entry.class_entry()
    cls_obj.class_name = 'class-default'
    if util.isNotEmpty(shape_average):
        if shape_average != prev_shape_average:
            cls_obj.shape_average = shape_average
    yang.Sdk.createData(device.url+"/policy-maps/policy-map=%s" %(prev_policy_name), cls_obj.getxml(filter=True), sdata.getSession())


def loopback(smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs["inputdict"]

    int_id = inputdict['loopback_interface_id']
    loopback_int_id = 'Loopback' + str(int_id)
    cidr = inputdict['cidr']
    vrf = inputdict['vrf']
    ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr)
    ip_addr_obj = ip_addr.ipam_pool_obj
    prefix = util.IPPrefix(ip_addr_obj.cidr)
    netmask = prefix.netmask
    loopback_ip = inputdict['ip']
    if util.isEmpty(loopback_ip) or loopback_ip is None:
        used_ips_list = get_used_ip_list_from_ippool(ip_addr_obj.name, sdata)
        loopback_ip = get_freeip_from_cidr(ip_addr_obj.cidr, used_ips_list)
        add_ipaddress_entries(ip_addr_obj.name, loopback_ip, sdata)
    else:
        used_ips_list = get_used_ip_list_from_ippool(ip_addr_obj.name, sdata)
        if used_ips_list.__len__() > 0:
            if str(prefix.masklen) != str(32):
                if loopback_ip in used_ips_list:
                    raise Exception("IP given is already used in the given pool")
            used_ips_list.sort()
            ip = IPAddress(loopback_ip)
            network_given = IPNetwork(ip_addr_obj.cidr)
            (addrStr, cidrStr) = ip_addr_obj.cidr.split('/')
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
                if loopback_ip == last_ip_address:
                    raise Exception('Broadcast IP cant be used')
            if not network_given.Contains(ip):
                raise Exception('Invalid IP address for this cidr')
        add_ipaddress_entries(ip_addr_obj.name, loopback_ip, sdata)
    payload = "<ip>%s</ip>" % loopback_ip
    serv_uri = sdata.getRcPath()
    yang.Sdk.createData(serv_uri, payload, sdata.getSession())
    intf_obj = devices.device.interfaces.interface.interface()
    if util.isNotEmpty(loopback_int_id):
        print 'loopback_int_id:', loopback_int_id
        intf_obj.name = loopback_int_id
        intf_obj.long_name = loopback_int_id
    if util.isNotEmpty(loopback_ip):
        intf_obj.ip_address = loopback_ip
        intf_obj.netmask = netmask
    uri = sdata.getRcPath()
    uri_list = uri.split('/',5)
    url = '/'.join(uri_list[0:4])
    if util.isNotEmpty(vrf):
        vrf_url = url + '/vrfs/vrf=%s' % (vrf)
        xml_output = yang.Sdk.getData(vrf_url, '',sdata.getTaskId())
        obj = util.parseXmlString(xml_output)
        util.log_debug( "obj: ",obj)
        intf_obj.vrf = vrf
        if util.isNotEmpty(obj.vrf.vrf_definition_mode):
            intf_obj.vrf_definition_mode = obj.vrf.vrf_definition_mode
    for dev_iterator in dev:
        yang.Sdk.createData(dev_iterator.url+'/interfaces', intf_obj.getxml(filter=True), sdata.getSession())

