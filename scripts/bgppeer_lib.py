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

from cpedeployment_lib import getLocalObject


def get_payload_for_import_export_update_service(endpoint, import_route_map=None, export_route_map=None, root=None):
    buf = '<end-point>%s</end-point>' % endpoint
    if import_route_map:
        buf += '<import-route-map>%s</import-route-map>' % import_route_map
    if export_route_map:
        buf += '<export-route-map>%s</export-route-map>' % export_route_map

    if root:
        buf = '<%s>%s</%s>' % (root, buf, root)
    return buf


def get_payload_for_import_export_update_service1(endpoint, import_route_map=None, export_route_map=None, root=None):
    if root == 'cpe_primary_dual':
        buf = '<end-point>cpe-primary-wan</end-point>'
        buf += '<name>%s</name>' % endpoint
        buf += '<end-point1>%s</end-point1>' % endpoint
    else:
        buf = '<end-point>cpe-secondary-wan</end-point>'
        buf += '<name>%s</name>' % endpoint
        buf += '<end-point2>%s</end-point2>' % endpoint
    if import_route_map:
        buf += '<import-route-map>%s</import-route-map>' % import_route_map
    if export_route_map:
        buf += '<export-route-map>%s</export-route-map>' % export_route_map

    if root:
        buf = '<cpe>%s</cpe>' % (buf)
    return buf


def get_payload_for_import_export_update_service2(endpoint, import_route_map=None, export_route_map=None, root=None):
    buf = '<end-point>%s</end-point>' % endpoint
    if import_route_map:
        buf += '<import-route-map>%s</import-route-map>' % import_route_map
    if export_route_map:
        buf += '<export-route-map>%s</export-route-map>' % export_route_map

    if root:
        buf = '<%s>%s</%s>' % (root, buf, root)
    return buf


def bgp_peer(cpeentity, entity, smodelctx, sdata, device, **kwargs):
    inputdict = kwargs['inputdict']
    BGP_peer_name = inputdict['BGP_peer_name']
    #peer = inputdict['peer']
    peer_ip = inputdict['peer_ip']
    peer_group = inputdict['peer_group']
    #listen_cidr = inputdict['listen_cidr']
    peer_description = inputdict['peer_description']
    remote_as = inputdict['remote_as']
    password = inputdict['password']
    import_route_map = inputdict['import_route_map']
    export_route_map = inputdict['export_route_map']
    next_hop_self = inputdict['next_hop_self']
    soft_reconfiguration = inputdict['soft_reconfiguration']
    default_originate = inputdict['default_originate']
    default_originate_route_map = inputdict['default_originate_route_map']
    send_community = inputdict['send_community']
    #encrypted_password = inputdict['encrypted_password']
    advertisement_interval = inputdict['advertisement_interval']
    time_in_sec = inputdict['time_in_sec']
    timers = inputdict['timers']
    keepalive_interval = inputdict['keepalive_interval']
    holdtime = inputdict['holdtime']
    # if util.isEmpty(peer):
    #     raise Exception("Peer is empty")
    #if peer == 'peer-ip':
    bgp_neighbor_obj = vrfs.vrf.router_bgp.neighbor.neighbor()
    bgp_neighbor_obj.ip_address = peer_ip
    # elif peer == 'peer-group':
    #     if util.isEmpty(peer_group):
    #         raise Exception("Peer group is empty")
    #     bgp_neighbor_obj = vrfs.vrf.router_bgp.peer_group.peer_group()
    #     bgp_neighbor_obj.name = peer_group
    #     bgp_neighbor_obj.cidr = listen_cidr
    bgp_neighbor_obj.peer_group = peer_group
    bgp_neighbor_obj.remote_as = remote_as
    bgp_neighbor_obj.description = peer_description
    bgp_neighbor_obj.next_hop_self = next_hop_self
    bgp_neighbor_obj.send_community = send_community

    if import_route_map != "":
        from cpedeployment_lib import route_maps
        route_maps(import_route_map, device, sdata, None, cpeentity)
        bgp_neighbor_obj.in_route_map = import_route_map
    if export_route_map != "":
        from cpedeployment_lib import route_maps
        route_maps(export_route_map, device, sdata, None, cpeentity)
        bgp_neighbor_obj.out_route_map = export_route_map
    bgp_neighbor_obj.soft_reconfiguration = soft_reconfiguration
    bgp_neighbor_obj.password = password
    bgp_neighbor_obj.default_originate = default_originate
    bgp_neighbor_obj.def_originate_route_map = default_originate_route_map
    if timers == 'true':
        bgp_neighbor_obj.keepalive_interval = keepalive_interval
        bgp_neighbor_obj.holdtime = holdtime
    if advertisement_interval == 'true':
        bgp_neighbor_obj.advertisement_interval = time_in_sec

    vrf = None
    obj = getLocalObject(sdata, 'end-points')
    if hasattr(obj.end_points, 'ivrf'):
        vrf = obj.end_points.ivrf
    if hasattr(obj.end_points, 'vrf'):
        vrf = obj.end_points.vrf

    if vrf is None:
        vrf = "GLOBAL"

    router_bgp_neighbor_url = device.url + '/l3features:vrfs/vrf=%s/router-bgp' % (vrf)
    yang.Sdk.createData(router_bgp_neighbor_url, bgp_neighbor_obj.getxml(filter=True), sdata.getSession())

    # creating entries for associated services
    if entity == 'cpe_primary' or entity == 'cpe_secondary':
        obj = getLocalObject(sdata, 'end-points')
        uri = sdata.getRcPath()
        parent_uri = uri[:uri.rfind(uri.split('/')[-3])]
        if entity == 'cpe_primary':
            pyld = get_payload_for_import_export_update_service(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe-primary')
        else:
            pyld = get_payload_for_import_export_update_service(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe-secondary')
        yang.Sdk.createData('%s' % parent_uri, '<policy-update-services/>', sdata.getSession(), False)
        yang.Sdk.createData('%spolicy-update-services' % parent_uri, pyld, sdata.getSession(), False)

    if entity == 'cpe_primary_dual' or entity == 'cpe_secondary_dual':
        obj = getLocalObject(sdata, 'end-points')
        uri = sdata.getRcPath()
        parent_uri = uri[:uri.rfind(uri.split('/')[-3])]
        if entity == 'cpe_primary_dual':
            pyld = get_payload_for_import_export_update_service1(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe_primary_dual')
        else:
            pyld = get_payload_for_import_export_update_service1(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe_secondary_dual')
        yang.Sdk.createData('%s' % parent_uri, '<policy-update-services/>', sdata.getSession(), False)
        yang.Sdk.createData('%spolicy-update-services' % parent_uri, pyld, sdata.getSession(), False)

    if entity == 'cpe_primary_inet_dual' or entity == 'cpe_primary_mpls_dual':
        obj = getLocalObject(sdata, 'end-points')
        uri = sdata.getRcPath()
        parent_uri = uri[:uri.rfind(uri.split('/')[-3])]
        if entity == 'cpe_primary_inet_dual':
            pyld = get_payload_for_import_export_update_service2(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe-primary-inet')
        else:
            pyld = get_payload_for_import_export_update_service2(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe-primary-mpls')
        yang.Sdk.createData('%s' % parent_uri, '<policy-update-services/>', sdata.getSession(), False)
        yang.Sdk.createData('%spolicy-update-services' % parent_uri, pyld, sdata.getSession(), False)

    if entity == 'cpe_secondary_inet_dual' or entity == 'cpe_secondary_mpls_dual':
        obj = getLocalObject(sdata, 'end-points')
        uri = sdata.getRcPath()
        parent_uri = uri[:uri.rfind(uri.split('/')[-3])]
        if entity == 'cpe_secondary_inet_dual':
            pyld = get_payload_for_import_export_update_service2(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe-secondary-inet')
        else:
            pyld = get_payload_for_import_export_update_service2(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe-secondary-mpls')
        yang.Sdk.createData('%s' % parent_uri, '<policy-update-services/>', sdata.getSession(), False)
        yang.Sdk.createData('%spolicy-update-services' % parent_uri, pyld, sdata.getSession(), False)

    if entity == 'cpe_primary_inet_triple' or entity == 'cpe_primary_mpls_triple':
        obj = getLocalObject(sdata, 'end-points')
        uri = sdata.getRcPath()
        parent_uri = uri[:uri.rfind(uri.split('/')[-3])]
        if entity == 'cpe_primary_inet_triple':
            pyld = get_payload_for_import_export_update_service2(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe-primary-inet')
        else:
            pyld = get_payload_for_import_export_update_service2(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe-primary-mpls')
        yang.Sdk.createData('%s' % parent_uri, '<policy-update-services/>', sdata.getSession(), False)
        yang.Sdk.createData('%spolicy-update-services' % parent_uri, pyld, sdata.getSession(), False)

    if entity == 'cpe_secondary_inet_triple' or entity == 'cpe_secondary_mpls_triple':
        obj = getLocalObject(sdata, 'end-points')
        uri = sdata.getRcPath()
        parent_uri = uri[:uri.rfind(uri.split('/')[-3])]
        if entity == 'cpe_secondary_inet_triple':
            pyld = get_payload_for_import_export_update_service2(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe-secondary-inet')
        else:
            pyld = get_payload_for_import_export_update_service2(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe-secondary-mpls')
        yang.Sdk.createData('%s' % parent_uri, '<policy-update-services/>', sdata.getSession(), False)
        yang.Sdk.createData('%spolicy-update-services' % parent_uri, pyld, sdata.getSession(), False)

    if entity == 'cpe_tertiary_inet_triple' or entity == 'cpe_tertiary_mpls_triple':
        obj = getLocalObject(sdata, 'end-points')
        uri = sdata.getRcPath()
        parent_uri = uri[:uri.rfind(uri.split('/')[-3])]
        if entity == 'cpe_tertiary_inet_triple':
            pyld = get_payload_for_import_export_update_service2(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe-tertiary-inet')
        else:
            pyld = get_payload_for_import_export_update_service2(obj.end_points.endpoint_name, import_route_map, export_route_map, 'cpe-tertiary-mpls')
        yang.Sdk.createData('%s' % parent_uri, '<policy-update-services/>', sdata.getSession(), False)
        yang.Sdk.createData('%spolicy-update-services' % parent_uri, pyld, sdata.getSession(), False)


def update_bgp_peer(cpeentity, entity, smodelctx, sdata, device, **kwargs):
    config = util.parseXmlString(sdata.getPayload()).bgp_peers
    previousconfig = util.parseXmlString(sdata.getPreviousPayload()).bgp_peers
    peer_ip = previousconfig.get_field_value('peer_ip')
    in_route_map = config.get_field_value('import_route_map')
    out_route_map = config.get_field_value('export_route_map')

    bgp_neighbor_obj = vrfs.vrf.router_bgp.neighbor.neighbor()
    bgp_neighbor_obj.ip_address = peer_ip

    if in_route_map is None:
        in_route_map = ''
    if out_route_map is None:
        out_route_map = ''

    rcpath = util.get_parent_rcpath(sdata.getRcPath())
    print 'setting rcpath= %s' % (rcpath)

    xml_output = yang.Sdk.getData(rcpath, '', sdata.getTaskId())
    obj = util.parseXmlString(xml_output)

    vrf = None
    obj = getLocalObject(sdata, 'end-points')
    if hasattr(obj.end_points, 'ivrf'):
        vrf = obj.end_points.ivrf
    if hasattr(obj.end_points, 'vrf'):
        vrf = obj.end_points.vrf

    if vrf is None:
        vrf = "GLOBAL"

    router_bgp_neighbor_url = device.url + '/l3features:vrfs/vrf=%s/router-bgp/neighbor=%s' % (vrf, peer_ip)

    payload = bgp_neighbor_obj.getxml(filter=True)

    if in_route_map is not None:
        from cpedeployment_lib import route_maps
        route_maps(in_route_map, device, sdata, None, cpeentity)
        raw_payload = '<%s>%s</%s>' % ('in-route-map', in_route_map, 'in-route-map')

        payload = payload.replace('</neighbor>', '%s</neighbor>' % raw_payload)

        yang.Sdk.createData(router_bgp_neighbor_url, raw_payload, sdata.getSession(), False)

    if out_route_map is not None:
        from cpedeployment_lib import route_maps
        route_maps(out_route_map, device, sdata, None, cpeentity)
        raw_payload = '<%s>%s</%s>' % ('out-route-map', out_route_map, 'out-route-map')
        payload = payload.replace('</neighbor>', '%s</neighbor>' % raw_payload)

        yang.Sdk.createData(router_bgp_neighbor_url, raw_payload, sdata.getSession(), False)
