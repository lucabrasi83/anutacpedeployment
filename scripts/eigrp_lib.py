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
from servicemodel.controller.devices.device import vrfs
from servicemodel.controller.devices.device import interfaces

from cpedeployment_lib import getLocalObject
from cpedeployment_lib import route_maps

def eigrpEnd(entity, smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs['inputdict']
    as_number = inputdict['as_number']
    in_route_map = inputdict['in_route_map']
    out_route_map = inputdict['out_route_map']
    passive_interface = inputdict['passive_interface']
    key_chain = inputdict['key_chain']
    hello_interval = inputdict['hello_interval']
    hold_time = inputdict['hold_time']
    split_horizon = inputdict['split_horizon']

    vrf = None
    obj = getLocalObject(sdata, 'end-points')
    if hasattr(obj.end_points, 'ivrf'):
        vrf = obj.end_points.ivrf
    if hasattr(obj.end_points, 'vrf'):
        vrf = obj.end_points.vrf

    if vrf is None:
        vrf = "GLOBAL"

    interface_type = obj.end_points.interface_type
    if interface_type == "Sub-Interface" or interface_type == "Physical":
        interface = obj.end_points.interface_name
        if hasattr(obj.end_points, 'vlan_id'):
            vlan_id = obj.end_points.vlan_id
        if interface_type == "Sub-Interface":
            if vlan_id is not None:
                interface = interface + '.' + str(vlan_id)
    if interface_type == "SVI":
        if hasattr(obj.end_points, 'vlan_id'):
            vlan_id = obj.end_points.vlan_id
        interface = "Vlan" + str(vlan_id)
    if interface_type == "Tunnel":
        if hasattr(obj.end_points, 'dmvpn_profile'):
            dmvpn_profile = obj.end_points.dmvpn_profile
            uri = sdata.getRcPath()
            uri_list = uri.split('/', 5)
            url = '/'.join(uri_list[0:4])

            xml_output = yang.Sdk.getData(url+"/dmvpn-tunnel-profiles/dmvpn-tunnel-profile="+str(dmvpn_profile), '', sdata.getTaskId())
            obj = util.parseXmlString(xml_output)
            util.log_debug( "obj: ", obj)
            interface = 'Tunnel' + obj.dmvpn_tunnel_profile.tunnel_id

    eigrp_passive_obj = vrfs.vrf.router_eigrp.eigrp.passive_interface.passive_interface()
    if util.isNotEmpty(interface):
        eigrp_passive_obj.interface = interface
    if util.isNotEmpty(passive_interface):
        eigrp_passive_obj.passive_interface = passive_interface

    eigrp_passive_url = dev.url + '/l3features:vrfs/vrf=%s/router-eigrp/eigrp=%s' % (vrf,as_number)
    yang.Sdk.createData(eigrp_passive_url, eigrp_passive_obj.getxml(filter=True), sdata.getSession())

    eigrpdistlistobj = vrfs.vrf.router_eigrp.eigrp.distribute_list.distribute_list()
    eigrpdistlistobj.interface = interface
    eigrp_distlist_url = dev.url + '/l3features:vrfs/vrf=%s/router-eigrp/eigrp=%s' % (vrf, as_number)
    if util.isNotEmpty(in_route_map):
        eigrpdistlistobj.route_map = in_route_map
        eigrpdistlistobj.filter = 'in'
        route_maps(in_route_map, dev, sdata)
        yang.Sdk.createData(eigrp_distlist_url, eigrpdistlistobj.getxml(filter=True), sdata.getSession())

    if util.isNotEmpty(out_route_map):
        eigrpdistlistobj.route_map = out_route_map
        eigrpdistlistobj.filter = 'out'
        route_maps(out_route_map, dev, sdata)
        yang.Sdk.createData(eigrp_distlist_url, eigrpdistlistobj.getxml(filter=True), sdata.getSession())

    eigrpintobj = interfaces.interface.eigrp.as_number.as_number()
    eigrpintobj.as_number = as_number
    if util.isNotEmpty(key_chain):
        key_chain_add(key_chain, sdata, dev, **kwargs)
        eigrpintobj.key_chain = key_chain
    eigrpintobj.hello_interval = hello_interval
    eigrpintobj.hold_time = hold_time
    if split_horizon == 'true':
        eigrpintobj.split_horizon = split_horizon
    eigrpinturl = dev.url + '/interface:interfaces/interface=%s/eigrp' % (str(interface).replace('/', '%2F'))
    yang.Sdk.createData(eigrpinturl, eigrpintobj.getxml(filter=True), sdata.getSession())


def eigrpSummary(entity, smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs['inputdict']
    prefix = inputdict['prefix']
    summary_metric = inputdict['summary_metric']
    bandwidth_metric = inputdict['bandwidth_metric']
    delay_metric = inputdict['delay_metric']
    reliability_metric = inputdict['reliability_metric']
    load_metric = inputdict['load_metric']
    mtu = inputdict['mtu']

    vrf = None
    obj = getLocalObject(sdata, 'end-points')
    if hasattr(obj.end_points, 'ivrf'):
        vrf = obj.end_points.ivrf
    if hasattr(obj.end_points, 'vrf'):
        vrf = obj.end_points.vrf

    if vrf is None:
        vrf = "GLOBAL"
    if hasattr(obj.end_points, 'eigrp'):
        as_number = obj.end_points.eigrp.as_number
    interface_type = obj.end_points.interface_type
    if interface_type == "Sub-Interface" or interface_type == "Physical":
        interface = obj.end_points.interface_name
        if hasattr(obj.end_points, 'vlan_id'):
            vlan_id = obj.end_points.vlan_id
        if interface_type == "Sub-Interface":
            if vlan_id is not None:
                interface = interface + '.' + str(vlan_id)
    if interface_type == "Tunnel":
        if hasattr(obj.end_points, 'dmvpn_profile'):
            dmvpn_profile = obj.end_points.dmvpn_profile
            uri = sdata.getRcPath()
            uri_list = uri.split('/', 5)
            url = '/'.join(uri_list[0:4])

            xml_output = yang.Sdk.getData(url+"/dmvpn-tunnel-profiles/dmvpn-tunnel-profile="+str(dmvpn_profile), '', sdata.getTaskId())
            obj = util.parseXmlString(xml_output)
            util.log_debug( "obj: ", obj)
            interface = 'Tunnel' + obj.dmvpn_tunnel_profile.tunnel_id
    prefix_in = util.IPPrefix(prefix)
    ip_address = prefix_in.address
    netmask = prefix_in.netmask
    (addrStr, cidrStr) = prefix.split('/')
    addr = addrStr.split('.')
    cidr = int(cidrStr)
    mask = [0, 0, 0, 0]
    for i in xrange(cidr):
        mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
    #net = []
    #for i in range(4):
        #net.append(int(addr[i]) & mask[i])
    net = [int(addr[i]) & mask[i] for i in xrange(4)]

    network = ".".join(map(str, net))
    eigrpsumnet = interfaces.interface.eigrp.as_number.summary_network.summary_network()
    eigrpsumnet.ip_address = network
    eigrpsumnet.netmask = netmask
    eigrpinturl = dev.url + '/interface:interfaces/interface=%s/eigrp/as-number=%s' % (str(interface).replace('/', '%2F'), as_number)
    yang.Sdk.createData(eigrpinturl, eigrpsumnet.getxml(filter=True), sdata.getSession())

    if summary_metric == 'true' and util.isNotEmpty(bandwidth_metric) and util.isNotEmpty(delay_metric) and util.isNotEmpty(reliability_metric) and util.isNotEmpty(load_metric) and util.isNotEmpty(mtu):
        eigrpsummetric = vrfs.vrf.router_eigrp.eigrp.summary_metric.summary_metric()
        eigrpsummetric.summary = network + '/' + cidrStr
        eigrpsummetric.bandwidth_metric = bandwidth_metric
        eigrpsummetric.delay_metric = delay_metric
        eigrpsummetric.reliability_metric = reliability_metric
        eigrpsummetric.load_metric = load_metric
        eigrpsummetric.mtu = mtu
        eigrp_summetric_url = dev.url + '/l3features:vrfs/vrf=%s/router-eigrp/eigrp=%s' % (vrf, as_number)
        yang.Sdk.createData(eigrp_summetric_url, eigrpsummetric.getxml(filter=True), sdata.getSession())


def key_chain_add(key_chain_name, sdata, dev, **kwargs):
    from servicemodel.controller.devices.device import key_chain
    uri = sdata.getRcPath()
    uri_list = uri.split('/', 5)
    url = '/'.join(uri_list[0:4])

    xml_output = yang.Sdk.getData(url+"/key-chain/router-key-chain="+str(key_chain_name), '', sdata.getTaskId())
    obj = util.parseXmlString(xml_output)
    util.log_debug("obj: ", obj)
    key_chain_name = obj.router_key_chain.key_chain_name
    keychainobj = key_chain.router_key_chain.router_key_chain()
    keychainobj.key_chain_name = key_chain_name
    yang.Sdk.createData(dev.url, '<key-chain/>', sdata.getSession(), False)
    key_chain_url = dev.url + '/l3features:key-chain'
    yang.Sdk.createData(key_chain_url, keychainobj.getxml(filter=True), sdata.getSession())

    if hasattr(obj.router_key_chain, 'keys'):
        keys = util.convert_to_list(obj.router_key_chain.keys)
        for key in keys:
            keyobj = key_chain.router_key_chain.keys.keys()
            keyobj.key_identifier = key.key_identifier
            keyobj.key_string_password = key.key_string_password
            key_url = dev.url + '/l3features:key-chain/router-key-chain=%s' % (key_chain_name)
            yang.Sdk.createData(key_url, keyobj.getxml(filter=True), sdata.getSession())
