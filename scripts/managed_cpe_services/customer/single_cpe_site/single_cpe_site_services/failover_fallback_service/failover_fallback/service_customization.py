#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2016-2017 Anuta Networks, Inc. All Rights Reserved.
#

#
#ALL THE CUSTOMIZATIONS REGARDING DATAPROCESSING SHOULD BE WRITTEN INTO THIS FILE
#
"""
Tree Structure of Handled XPATH:

services
        |
        managed-cpe-services
                            |
                            customer
                                    |
                                    single-cpe-site
                                                   |
                                                   single-cpe-site-services
                                                                           |
                                                                           failover-fallback-service
                                                                                                    |
                                                                                                    failover-fallback
                                                                                                                     
Schema Representation:

/services/managed-cpe-services/customer/single-cpe-site/single-cpe-site-services/failover-fallback-service/failover-fallback
"""
"""
Names of Leafs for this Yang Entity
                name
              device
        failover-lan
        fallback-lan

"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import getPreviousObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log
from servicemodel.controller.devices.device import control_plane
import time


class ServiceDataCustomization:

    @staticmethod
    def process_service_create_data(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the inputs"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']

    @staticmethod
    def process_service_device_bindings(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the device bindings or Call the Business Login Handlers"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']
        devbindobjs = kwargs['devbindobjs']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']
        fail_fall(smodelctx, sdata, **kwargs)

    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']

        #Previous config and previous inputdict
        pconfig = kwargs['pconfig']
        pinputdict = kwargs['pinputdict']

        dev = kwargs['dev']

    @staticmethod
    def process_service_delete_data(smodelctx, sdata, **kwargs):
      """callback called for delete operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        dev = kwargs['dev']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']


def fail_fall(smodelctx, sdata, **kwargs):
    obj_prim = getLocalObject(sdata, 'single-cpe-site-services=')
    device = obj_prim.single_cpe_site_services.cpe.device_ip
    failover_state = obj_prim.single_cpe_site_services.failover_state
    inputdict = kwargs['inputdict']
    dev = devicemgr.getDeviceById(device)
    operation_type = inputdict['operation_type']
    wan_ebgp_neighbor = inputdict['wan_ebgp_neighbor']
    vrf = None
    if dev.device.status == "OFFLINE":
        raise Exception("Device " + str(dev.device.id) + " is currently offline. Cannot proceed with operation.")
    if operation_type == "failover":
        if failover_state != "false":
            raise Exception("Site Failover State is not clean. Restore state by selecting fallback/switch-on-dps")
        if hasattr(obj_prim.single_cpe_site_services.cpe_wan, 'end_points'):
            endpoints = util.convert_to_list(obj_prim.single_cpe_site_services.cpe_wan.end_points)
            bgp_peers_list = []
            for endpoint in endpoints:
                if hasattr(endpoint, 'bgp_peers'):
                    check_bgp_peers = util.convert_to_list(endpoint.bgp_peers)
                    bgp_peers_list = [check_peer.peer_ip for check_peer in check_bgp_peers]
            if len(bgp_peers_list) < 2 :
                raise Exception("Less than 2 eBGP peers found in device. Cannot proceed with failover.")
            for endpoint in endpoints:
                if hasattr(endpoint, 'ivrf'):
                    vrf = endpoint.ivrf
                if hasattr(endpoint, 'vrf'):
                    vrf = endpoint.vrf
                if vrf is None:
                    vrf = "GLOBAL"
                if hasattr(endpoint, 'bgp_peers'):
                    bgp_peers = util.convert_to_list(endpoint.bgp_peers)
                    for peer in bgp_peers:
                        if peer.peer_ip == wan_ebgp_neighbor:
                   
                            prefix_list_url = dev.url + '/l3features:ip-prefixlist-list'

                            mgmt_prefix_list_payload =  '''
                                                    <ip-prefixlist>
                                                    <name>FAILOVER-MGMT-PREFIX-LIST</name>
                                                    <ip-prefixlist-entries>
                                                        <ip-prefixlist-entry>
                                                            <subnet>121.244.196.0/24</subnet>
                                                            <condition>permit</condition>
                                                            <rule-num>5</rule-num>
                                                            <compare>le</compare>
                                                            <num>32</num>
                                                        </ip-prefixlist-entry>
                                                        <ip-prefixlist-entry>
                                                            <subnet>121.244.180.0/24</subnet>
                                                            <condition>permit</condition>
                                                            <rule-num>10</rule-num>
                                                            <compare>le</compare>
                                                            <num>32</num>
                                                        </ip-prefixlist-entry>
                                                        <ip-prefixlist-entry>
                                                            <subnet>115.114.221.0/24</subnet>
                                                            <condition>permit</condition>
                                                            <rule-num>15</rule-num>
                                                            <compare>le</compare>
                                                            <num>32</num>
                                                        </ip-prefixlist-entry>
                                                        <ip-prefixlist-entry>
                                                            <subnet>115.114.227.0/24</subnet>
                                                            <condition>permit</condition>
                                                            <rule-num>20</rule-num>
                                                            <compare>le</compare>
                                                            <num>32</num>
                                                        </ip-prefixlist-entry>
                                                        <ip-prefixlist-entry>
                                                            <subnet>115.110.222.0/24</subnet>
                                                            <condition>permit</condition>
                                                            <rule-num>25</rule-num>
                                                            <compare>le</compare>
                                                            <num>32</num>
                                                        </ip-prefixlist-entry>
                                                        </ip-prefixlist-entries>
                                                        </ip-prefixlist>
                                                        '''

                            yang.Sdk.createData(dev.url + '/l3features:ip-prefixlist-list', mgmt_prefix_list_payload, sdata.getSession(), False)

                            route_map_url = dev.url + '/l3features:route-maps'

                            in_failover_route_map = '''
                                                    <route-map>
                                                    <name>FAILOVER-INBOUND-POLICY</name>
                                                    <route-map-entries>
                                                        <seq>5</seq>
                                                        <action>permit</action>
                                                        <match-condition>
                                                            <condition-type>prefix-list</condition-type>
                                                            <value>FAILOVER-MGMT-PREFIX-LIST</value>
                                                        </match-condition>
                                                        <set-action>
                                                            <set-type>weight</set-type>
                                                            <value>65000</value>
                                                        </set-action>
                                                        </route-map-entries>
                                                    </route-map>
                                                    '''

                            yang.Sdk.createData(dev.url + '/l3features:route-maps', in_failover_route_map, sdata.getSession(), False)


                            if yang.Sdk.dataExists(dev.url + '/interface:interfaces/interface=Loopback0'):
                                loopback_output = yang.Sdk.getData(dev.url + '/interface:interfaces/interface=Loopback0', '', sdata.getTaskId())
                                loopback_obj = util.parseXmlString(loopback_output)
                                if hasattr(loopback_obj, 'interface'):
                                    if util.isNotEmpty(loopback_obj.interface.ip_address):
                                        loopback_ip = loopback_obj.interface.ip_address

                                        loopback_prefix_payload = '''
                                                                   <ip-prefixlist>
                                                                    <name>FAILOVER-LOOPBACK-PREFIX-LIST</name>
                                                                    <ip-prefixlist-entries>
                                                                        <ip-prefixlist-entry>
                                                                            <subnet>''' + loopback_ip +'''/32</subnet>
                                                                            <condition>permit</condition>
                                                                            <rule-num>5</rule-num>
                                                                        </ip-prefixlist-entry>
                                                                    </ip-prefixlist-entries>
                                                                    </ip-prefixlist>
                                                                  '''
                                        yang.Sdk.createData(dev.url + '/l3features:ip-prefixlist-list', loopback_prefix_payload, sdata.getSession(), False)

                                        out_failover_route_map = '''
                                                                <route-map>
                                                                <name>FAILOVER-OUTBOUND-POLICY</name>
                                                                <route-map-entries>
                                                                    <seq>5</seq>
                                                                    <action>permit</action>
                                                                    <match-condition>
                                                                        <condition-type>prefix-list</condition-type>
                                                                        <value>FAILOVER-LOOPBACK-PREFIX-LIST</value>
                                                                    </match-condition>
                                                                </route-map-entries>
                                                                </route-map>
                                                                '''

                                        yang.Sdk.createData(dev.url + '/l3features:route-maps', out_failover_route_map, sdata.getSession(), False)
                                    else:
                                        raise Exception("No IP Address found on Loopback0 on device. Cannot proceed with failover.")

                            else:
                                raise Exception("No Mgmt Loopback0 Found on device. Cannot proceed with failover.")


                            bgp_peer_url = dev.url + '/l3features:vrfs/vrf=%s/router-bgp/neighbor=%s' % (vrf, wan_ebgp_neighbor)

                            bgp_peer_payload = '''
                                                <neighbor>
                                                <ip-address>''' + wan_ebgp_neighbor + '''</ip-address>
                                                <in-route-map>FAILOVER-INBOUND-POLICY</in-route-map>
                                                <out-route-map>FAILOVER-OUTBOUND-POLICY</out-route-map>
                                                </neighbor>
                                               '''
                            if yang.Sdk.dataExists(bgp_peer_url):
                                yang.Sdk.patchData(bgp_peer_url, bgp_peer_payload, sdata, add_reference=False)
                            else:
                                raise Exception("eBGP Peer not found on device. Cannot proceed with failover.")

                            uri = sdata.getRcPath()
                            uri_list = uri.split('/',6)
                            site_url = '/'.join(uri_list[0:6])

                            site_payload = '''
                                           <failover-state>true</failover-state>
                                           '''
                            yang.Sdk.createData(site_url, site_payload, sdata.getSession(), False)
                   
    elif operation_type == "switch-on-dps":
        if failover_state == "dps-off":

            control_plane_obj = control_plane.control_plane()
            control_plane_obj.input_service_policy._empty_tag = True
            control_plane_obj.output_service_policy._empty_tag = True

            if yang.Sdk.dataExists(dev.url + '/l3features:control-plane'):
                yang.Sdk.patchData(dev.url + '/l3features:control-plane', control_plane_obj.getxml(filter=True), sdata, add_reference=False)
            else:
                yang.Sdk.append_taskdetail(sdata.getTaskId(), "No Control-Plane entity found in device model")

            if yang.Sdk.dataExists(dev.url + '/acl:access-lists/access-list=COPP-ACL'):
                yang.Sdk.deleteData(dev.url + '/acl:access-lists/access-list=COPP-ACL', '', sdata.getTaskId(), sdata.getSession())

            else:
                 yang.Sdk.append_taskdetail(sdata.getTaskId(), "No ACL COPP-ACL entity found in device model")

            if yang.Sdk.dataExists(dev.url + '/qos:policy-maps/policy-map=COPP-POLICY'):
                yang.Sdk.deleteData(dev.url + '/qos:policy-maps/policy-map=COPP-POLICY', '', sdata.getTaskId(), sdata.getSession())

            else:
                 yang.Sdk.append_taskdetail(sdata.getTaskId(), "No Policy-Map COPP-POLICY entity found in device model")

            if yang.Sdk.dataExists(dev.url + '/qos:class-maps/class-map=COPP-CLASS'):
                yang.Sdk.deleteData(dev.url + '/qos:class-maps/class-map=COPP-CLASS', '', sdata.getTaskId(), sdata.getSession())

            else:
                 yang.Sdk.append_taskdetail(sdata.getTaskId(), "No Class-Map COPP-CLASS entity found in device model")


            uri = sdata.getRcPath()
            uri_list = uri.split('/',6)
            site_url = '/'.join(uri_list[0:6])

            site_payload = '''
                           <failover-state>false</failover-state>
                           '''
            yang.Sdk.createData(site_url, site_payload, sdata.getSession(), False)
        else:
            raise Exception("Site Service failover state is not dps-off. Cannot proceed with DPS Switch Off.")
        

    elif operation_type == "fallback":
        if failover_state == "true":

            if hasattr(obj_prim.single_cpe_site_services.cpe_wan, 'end_points'):
                endpoints = util.convert_to_list(obj_prim.single_cpe_site_services.cpe_wan.end_points)
                for endpoint in endpoints:
                    if hasattr(endpoint, 'ivrf'):
                        vrf = endpoint.ivrf
                    if hasattr(endpoint, 'vrf'):
                        vrf = endpoint.vrf
                    if vrf is None:
                        vrf = "GLOBAL"
                    if hasattr(endpoint, 'bgp_peers'):
                        bgp_peers = util.convert_to_list(endpoint.bgp_peers)
                        for peer in bgp_peers:
                            if peer.peer_ip == wan_ebgp_neighbor:

                                if hasattr(peer, 'import_route_map'):
                                    if util.isNotEmpty(peer.import_route_map):
                                        svc_peer_in_route_map = peer.import_route_map
                                    else:
                                        svc_peer_in_route_map = ''
                                else:
                                    svc_peer_in_route_map = ''

                                if hasattr(peer, 'export_route_map'):
                                    if util.isNotEmpty(peer.export_route_map):
                                        svc_peer_out_route_map = peer.export_route_map
                                    else:
                                        svc_peer_out_route_map = ''
                                else:
                                    svc_peer_out_route_map = ''

                                bgp_peer_payload = '''
                                                    <neighbor>
                                                    <ip-address>''' + wan_ebgp_neighbor + '''</ip-address>
                                                    <in-route-map>''' + svc_peer_in_route_map + '''</in-route-map>
                                                    <out-route-map>''' + svc_peer_out_route_map + '''</out-route-map>
                                                    </neighbor>
                                                   '''

                                bgp_peer_url = dev.url + '/l3features:vrfs/vrf=%s/router-bgp/neighbor=%s' % (vrf, wan_ebgp_neighbor)          
                                if yang.Sdk.dataExists(bgp_peer_url):
                                    yang.Sdk.patchData(bgp_peer_url, bgp_peer_payload, sdata, add_reference=False)
                                else:
                                    raise Exception("eBGP Peer not found on device. Cannot proceed with fallback.")

                                if yang.Sdk.dataExists(dev.url + '/l3features:route-maps/route-map=FAILOVER-INBOUND-POLICY'):
                                    yang.Sdk.deleteData(dev.url + '/l3features:route-maps/route-map=FAILOVER-INBOUND-POLICY', '', sdata.getTaskId(), sdata.getSession())

                                else:
                                     yang.Sdk.append_taskdetail(sdata.getTaskId(), "No Route-Map FAILOVER-INBOUND-POLICY entity found in device model")

                                if yang.Sdk.dataExists(dev.url + '/l3features:route-maps/route-map=FAILOVER-OUTBOUND-POLICY'):
                                    yang.Sdk.deleteData(dev.url + '/l3features:route-maps/route-map=FAILOVER-OUTBOUND-POLICY', '', sdata.getTaskId(), sdata.getSession())

                                else:
                                     yang.Sdk.append_taskdetail(sdata.getTaskId(), "No Route-Map FAILOVER-OUTBOUND-POLICY entity found in device model")

                                if yang.Sdk.dataExists(dev.url + '/l3features:ip-prefixlist-list/ip-prefixlist=FAILOVER-LOOPBACK-PREFIX-LIST'):
                                    yang.Sdk.deleteData(dev.url + '/l3features:ip-prefixlist-list/ip-prefixlist=FAILOVER-LOOPBACK-PREFIX-LIST', '', sdata.getTaskId(), sdata.getSession())

                                else:
                                     yang.Sdk.append_taskdetail(sdata.getTaskId(), "No IP Prefix-List FAILOVER-LOOPBACK-PREFIX-LIST entity found in device model")

                                if yang.Sdk.dataExists(dev.url + '/l3features:ip-prefixlist-list/ip-prefixlist=FAILOVER-MGMT-PREFIX-LIST'):
                                    yang.Sdk.deleteData(dev.url + '/l3features:ip-prefixlist-list/ip-prefixlist=FAILOVER-MGMT-PREFIX-LIST', '', sdata.getTaskId(), sdata.getSession())

                                else:
                                     yang.Sdk.append_taskdetail(sdata.getTaskId(), "No IP Prefix-List FAILOVER-MGMT-PREFIX-LIST entity found in device model")

            uri = sdata.getRcPath()
            uri_list = uri.split('/',6)
            site_url = '/'.join(uri_list[0:6])

            site_payload = '''
                           <failover-state>false</failover-state>
                           '''
            yang.Sdk.createData(site_url, site_payload, sdata.getSession(), False)
        else:
            raise Exception("Site Service failover state is not active. No need to fallback again.")

    elif operation_type == "switch-off-dps":
        if failover_state != "false":
            raise Exception("Site failover state is already active. Restore failover state by selecting appropriate operation-type.")
        if yang.Sdk.dataExists(dev.url + '/dmvpn:dmvpntunnels/dmvpntunnel=100'):
            dps_tunnel_output = yang.Sdk.getData(dev.url + '/dmvpn:dmvpntunnels/dmvpntunnel=100', '', sdata.getTaskId())
            dps_tunnel_obj = util.parseXmlString(dps_tunnel_output)
            if hasattr(dps_tunnel_obj, 'dmvpntunnel'):
                if hasattr(dps_tunnel_obj.dmvpntunnel, 'vrf_name'):
                    if util.isNotEmpty(dps_tunnel_obj.dmvpntunnel.vrf_name) and dps_tunnel_obj.dmvpntunnel.vrf_name != "DPS":
                        raise Exception("No Valid DPS Tunnel100 found on device. Cannot Proceed with DPS switch off.")
                    elif util.isEmpty(dps_tunnel_obj.dmvpntunnel.vrf_name):
                        raise Exception("No Valid DPS Tunnel100 found on device. Cannot Proceed with DPS switch off.")
                if hasattr(dps_tunnel_obj.dmvpntunnel, 'ipaddress'):
                    if util.isNotEmpty(dps_tunnel_obj.dmvpntunnel.ipaddress):
                        from cpedeployment import ipaddr_lib
                        dps_tunnel_ip = dps_tunnel_obj.dmvpntunnel.ipaddress
                        dps_tunnel_mask = dps_tunnel_obj.dmvpntunnel.netmask
                        dps_tunnel_subnet = str(ipaddr_lib.IPv4Network(unicode(dps_tunnel_ip + '/' + dps_tunnel_mask), strict=False).network)
                        dps_tunnel_wildcard = str(ipaddr_lib.IPv4Network(unicode(dps_tunnel_ip + '/' + dps_tunnel_mask), strict=False).hostmask)

                        acl_url = dev.url + '/acl:access-lists'

                        acl_payload = '''
                                      <access-list>
                                      <name>COPP-ACL</name>
                                      <acl-type>extended</acl-type>
                                      <acl-rules>
                                      <acl-rule>
                                        <name>permit ospf host ''' + dps_tunnel_ip  + ''' any</name>
                                        <action>permit</action>
                                        <layer4protocol>ospf</layer4protocol>
                                        <source-condition-type>host</source-condition-type>
                                        <source-ip>'''+ dps_tunnel_ip +'''</source-ip>
                                        <dest-condition-type>any</dest-condition-type>
                                        
                                    </acl-rule>
                                    <acl-rule>
                                        <name>permit ospf ''' + dps_tunnel_subnet + ' '  + dps_tunnel_wildcard + ''' any</name>
                                        <action>permit</action>
                                        <layer4protocol>ospf</layer4protocol>
                                        <source-condition-type>cidr</source-condition-type>
                                        <source-ip>''' + dps_tunnel_subnet + '''</source-ip>
                                        <source-mask>''' + dps_tunnel_wildcard + '''</source-mask>
                                        <dest-condition-type>any</dest-condition-type>
                                       
                                    </acl-rule>
                                    </acl-rules>
                                    </access-list>
                                     '''

                        yang.Sdk.createData(acl_url, acl_payload, sdata.getSession(), False)

                        class_map_url = dev.url + '/qos:class-maps'

                        class_map_payload = '''
                                             
                                            <class-map>
                                                <name>COPP-CLASS</name>
                                                <match-type>match-any</match-type>
                                                <class-match-condition>
                                                    <match-value>COPP-ACL</match-value>
                                                    <condition-type>access-group</condition-type>
                                                </class-match-condition>
                                            </class-map>
                                       
                                            '''

                        yang.Sdk.createData(class_map_url, class_map_payload, sdata.getSession(), False)

                        policy_map_url = dev.url + '/qos:policy-maps'

                        policy_map_payload = '''
                                           
                                            <policy-map>
                                                <name>COPP-POLICY</name>
                                                <class-entry>
                                                    <class-name>COPP-CLASS</class-name>
                                                    <cir-rate>8000</cir-rate>
                                                    <police-conform-action>drop</police-conform-action>
                                                </class-entry>
                                                <class-entry>
                                                    <class-name>class-default</class-name>
                                                </class-entry>
                                            </policy-map>
                                        
                                             '''
                        yang.Sdk.createData(policy_map_url, policy_map_payload, sdata.getSession(), False)

                        control_plane_obj = control_plane.control_plane()

                        control_plane_obj.input_service_policy = "COPP-POLICY"
                        control_plane_obj.output_service_policy = "COPP-POLICY"

                        yang.Sdk.createData(dev.url, control_plane_obj.getxml(filter=True), sdata.getSession(), False)

                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',6)
                        site_url = '/'.join(uri_list[0:6])

                        site_payload = '''
                                        <failover-state>dps-off</failover-state>
                                       '''
                        yang.Sdk.createData(site_url, site_payload, sdata.getSession(), False)
                    else:
                        raise Exception("No IP Address found on DPS Tunnel100. Cannot Proceed with DPS switch off.")
        else:
            raise Exception("No Overlay Tunnel100 interface found on device. Cannot Proceed with DPS switch off.")

    now = time.strftime("%Y-%b-%d %I:%M %p %Z", time.localtime())
    payload_time = '<created-on>' + now + '</created-on>'
        
    yang.Sdk.createData(sdata.getRcPath(), payload_time, sdata.getSession(), False)

    taskid = sdata.getTaskId()

    output = yang.Sdk.invokeRpc('tasks:get-basic-task-detail', '<taskId>' + str(taskid) + '</taskId>')
    basic_task_details_out = util.parseXmlString(output)
    if hasattr(basic_task_details_out, 'taskDetail'):
        if hasattr(basic_task_details_out.taskDetail, 'userName'):
          taskuser = basic_task_details_out.taskDetail.userName

          payload_user = '<created-by>' + str(taskuser) + '</created-by>'
          yang.Sdk.createData(sdata.getRcPath(), payload_user, sdata.getSession(), False)

class DeletePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for Deletion"""
        log('operations: %s' % (operations))

class CreatePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for creation"""
        log('operations: %s' % (operations))
        yang.moveOperations(operations, ['UpdateRouterBGPNeighbor'], ['CreateRouteMap','CreateRouteMapConditions'], True)
