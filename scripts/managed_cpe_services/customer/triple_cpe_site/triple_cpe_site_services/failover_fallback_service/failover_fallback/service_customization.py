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
                                    triple-cpe-site
                                                   |
                                                   triple-cpe-site-services
                                                                           |
                                                                           failover-fallback-service
                                                                                                    |
                                                                                                    failover-fallback
                                                                                                                     
Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/failover-fallback-service/failover-fallback
"""
"""
Names of Leafs for this Yang Entity
                name
              device
cpe-primary-mpls-wan-neighbor
cpe-primary-inet-wan-neighbor
cpe-secondary-mpls-wan-neighbor
cpe-secondary-inet-wan-neighbor
cpe-tertiary-mpls-wan-neighbor
cpe-tertiary-inet-wan-neighbor
        failover-wan
        fallback-wan
        failover-b2b
        fallback-b2b
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
    raise Exception("Site Failover/Fallback not supported for this site type")
    inputdict = kwargs['inputdict']
    obj_prim = getLocalObject(sdata, 'triple-cpe-site-services=')
    pri_device = obj_prim.triple_cpe_site_services.cpe_primary.device_ip
    pri_dev = devicemgr.getDeviceById(pri_device)
    sec_device = obj_prim.triple_cpe_site_services.cpe_secondary.device_ip
    sec_dev = devicemgr.getDeviceById(sec_device)
    failover_state = obj_prim.triple_cpe_site_services.failover_state
    operation_type = inputdict['operation_type']

    if operation_type == "failover":
        if failover_state == "true":
            raise Exception("Site is already in failover state. Fallback Site service first to initiate a new failover.")
        else:

                    acl_url = pri_dev.url + '/acl:access-lists'

                    acl_payload = '''
                                   <access-list>
                            <name>COPP-ACL</name>
                            <acl-type>extended</acl-type>
                            <acl-rules>
                                <acl-rule>
                                    <name>permit tcp any any eq bgp</name>
                                    <action>permit</action>
                                    <layer4protocol>tcp</layer4protocol>
                                    <source-condition-type>any</source-condition-type>
                                    <dest-condition-type>any</dest-condition-type>
                                    <dest-port-operator>eq</dest-port-operator>
                                    <dest-port>bgp</dest-port>
                                </acl-rule>
                                <acl-rule>
                                    <name>permit tcp any eq bgp any</name>
                                    <action>permit</action>
                                    <layer4protocol>tcp</layer4protocol>
                                    <source-condition-type>any</source-condition-type>
                                    <source-port-operator>eq</source-port-operator>
                                    <source-port>bgp</source-port>
                                    <dest-condition-type>any</dest-condition-type>
                                </acl-rule>
                                <acl-rule>
                                    <name>permit ospf any any</name>
                                    <action>permit</action>
                                    <layer4protocol>ospf</layer4protocol>
                                    <source-condition-type>any</source-condition-type>
                                    <dest-condition-type>any</dest-condition-type>
                                </acl-rule>
                                <acl-rule>
                                    <name>permit eigrp any any</name>
                                    <action>permit</action>
                                    <layer4protocol>eigrp</layer4protocol>
                                    <source-condition-type>any</source-condition-type>
                                    <dest-condition-type>any</dest-condition-type>
                                </acl-rule>
                                <acl-rule>
                                    <name>permit ip any host 224.0.0.2</name>
                                    <action>permit</action>
                                    <layer4protocol>ip</layer4protocol>
                                    <source-condition-type>any</source-condition-type>
                                    <dest-condition-type>host</dest-condition-type>
                                    <dest-ip>224.0.0.2</dest-ip>
                                </acl-rule>
                                <acl-rule>
                                    <name>permit ip host 224.0.0.2 any</name>
                                    <action>permit</action>
                                    <layer4protocol>ip</layer4protocol>
                                    <source-condition-type>host</source-condition-type>
                                    <source-ip>224.0.0.2</source-ip>
                                    <dest-condition-type>any</dest-condition-type>
                                </acl-rule>
                                <acl-rule>
                                    <name>permit ip any host 224.0.0.102</name>
                                    <action>permit</action>
                                    <layer4protocol>ip</layer4protocol>
                                    <source-condition-type>any</source-condition-type>
                                    <dest-condition-type>host</dest-condition-type>
                                    <dest-ip>224.0.0.102</dest-ip>
                                </acl-rule>
                                <acl-rule>
                                    <name>permit ip host 224.0.0.102 any</name>
                                    <action>permit</action>
                                    <layer4protocol>ip</layer4protocol>
                                    <source-condition-type>host</source-condition-type>
                                    <source-ip>224.0.0.102</source-ip>
                                    <dest-condition-type>any</dest-condition-type>
                                </acl-rule>
                                <acl-rule>
                                    <name>permit ip any host 224.0.0.18</name>
                                    <action>permit</action>
                                    <layer4protocol>ip</layer4protocol>
                                    <source-condition-type>any</source-condition-type>
                                    <dest-condition-type>host</dest-condition-type>
                                    <dest-ip>224.0.0.18</dest-ip>
                                </acl-rule>
                                <acl-rule>
                                    <name>permit ip host 224.0.0.18 any</name>
                                    <action>permit</action>
                                    <layer4protocol>ip</layer4protocol>
                                    <source-condition-type>host</source-condition-type>
                                    <source-ip>224.0.0.18</source-ip>
                                    <dest-condition-type>any</dest-condition-type>
                                </acl-rule>
                            </acl-rules>
                        </access-list>
                                 '''

                    yang.Sdk.createData(acl_url, acl_payload, sdata.getSession(), False)

                    class_map_url = pri_dev.url + '/qos:class-maps'

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

                    policy_map_url = pri_dev.url + '/qos:policy-maps'

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

                    yang.Sdk.createData(pri_dev.url, control_plane_obj.getxml(filter=True), sdata.getSession(), False)

                    uri = sdata.getRcPath()
                    uri_list = uri.split('/',6)
                    site_url = '/'.join(uri_list[0:6])

                    site_payload = '''
                                        <failover-state>true</failover-state>
                                   '''
                    yang.Sdk.createData(site_url, site_payload, sdata.getSession(), False)

    elif operation_type == "fallback":
        if failover_state == "true":

            control_plane_obj = control_plane.control_plane()
            control_plane_obj.input_service_policy._empty_tag = True
            control_plane_obj.output_service_policy._empty_tag = True

            if yang.Sdk.dataExists(pri_dev.url + '/l3features:control-plane'):
                yang.Sdk.patchData(pri_dev.url + '/l3features:control-plane', control_plane_obj.getxml(filter=True), sdata, add_reference=False)
            else:
                yang.Sdk.append_taskdetail(sdata.getTaskId(), "No Control-Plane entity found in primary CPE device model")

            if yang.Sdk.dataExists(sec_dev.url + '/l3features:control-plane'):
                yang.Sdk.patchData(sec_dev.url + '/l3features:control-plane', control_plane_obj.getxml(filter=True), sdata, add_reference=False)
            else:
                yang.Sdk.append_taskdetail(sdata.getTaskId(), "No Control-Plane entity found in secondary CPE device model")

            if yang.Sdk.dataExists(pri_dev.url + '/acl:access-lists/access-list=COPP-ACL'):
                yang.Sdk.deleteData(pri_dev.url + '/acl:access-lists/access-list=COPP-ACL', '', sdata.getTaskId(), sdata.getSession())

            else:
                 yang.Sdk.append_taskdetail(sdata.getTaskId(), "No ACL COPP-ACL entity found in primary CPE device model")

            if yang.Sdk.dataExists(sec_dev.url + '/acl:access-lists/access-list=COPP-ACL'):
                yang.Sdk.deleteData(sec_dev.url + '/acl:access-lists/access-list=COPP-ACL', '', sdata.getTaskId(), sdata.getSession())

            else:
                 yang.Sdk.append_taskdetail(sdata.getTaskId(), "No ACL COPP-ACL entity found in secondary CPE device model")

            if yang.Sdk.dataExists(pri_dev.url + '/qos:policy-maps/policy-map=COPP-POLICY'):
                yang.Sdk.deleteData(pri_dev.url + '/qos:policy-maps/policy-map=COPP-POLICY', '', sdata.getTaskId(), sdata.getSession())

            else:
                 yang.Sdk.append_taskdetail(sdata.getTaskId(), "No Policy-Map COPP-POLICY entity found in primary CPE device model")

            if yang.Sdk.dataExists(sec_dev.url + '/qos:policy-maps/policy-map=COPP-POLICY'):
                yang.Sdk.deleteData(sec_dev.url + '/qos:policy-maps/policy-map=COPP-POLICY', '', sdata.getTaskId(), sdata.getSession())

            else:
                 yang.Sdk.append_taskdetail(sdata.getTaskId(), "No Policy-Map COPP-POLICY entity found in secondary CPE device model")

            if yang.Sdk.dataExists(pri_dev.url + '/qos:class-maps/class-map=COPP-CLASS'):
                yang.Sdk.deleteData(pri_dev.url + '/qos:class-maps/class-map=COPP-CLASS', '', sdata.getTaskId(), sdata.getSession())

            else:
                 yang.Sdk.append_taskdetail(sdata.getTaskId(), "No Class-Map COPP-CLASS entity found in primary CPE device model")

            if yang.Sdk.dataExists(sec_dev.url + '/qos:class-maps/class-map=COPP-CLASS'):
                yang.Sdk.deleteData(sec_dev.url + '/qos:class-maps/class-map=COPP-CLASS', '', sdata.getTaskId(), sdata.getSession())

            else:
                 yang.Sdk.append_taskdetail(sdata.getTaskId(), "No Class-Map COPP-CLASS entity found in secondary CPE device model")

            uri = sdata.getRcPath()
            uri_list = uri.split('/',6)
            site_url = '/'.join(uri_list[0:6])

            site_payload = '''
                           <failover-state>false</failover-state>
                           '''
            yang.Sdk.createData(site_url, site_payload, sdata.getSession(), False)
        else:
            raise Exception("Site Service is already in fallback mode (Failover-state checkbox is false).")

    elif operation_type == "switch-off-dps":
        if failover_state == "true":
            raise Exception("Site is already in failover state. Fallback Site service first to initiate a new failover.")
        if yang.Sdk.dataExists(sec_dev.url + '/dmvpn:dmvpntunnels/dmvpntunnel=100'):
            dps_tunnel_output = yang.Sdk.getData(sec_dev.url + '/dmvpn:dmvpntunnels/dmvpntunnel=100', '', sdata.getTaskId())
            dps_tunnel_obj = util.parseXmlString(dps_tunnel_output)
            if hasattr(dps_tunnel_obj, 'dmvpntunnel'):
                if hasattr(dps_tunnel_obj.dmvpntunnel, 'vrf_name'):
                    if util.isNotEmpty(dps_tunnel_obj.dmvpntunnel.vrf_name) and dps_tunnel_obj.dmvpntunnel.vrf_name != "DPS":
                        raise Exception("No Valid DPS Tunnel100 found on device. Cannot Proceed with DPS switch off.")
                    elif util.isEmpty(dps_tunnel_obj.dmvpntunnel.vrf_name):
                        raise Exception("No Valid DPS Tunnel100 found on device. Cannot Proceed with DPS switch off.")
                if hasattr(dps_tunnel_obj.dmvpntunnel, 'ipaddress'):
                    if util.isNotEmpty(dps_tunnel_obj.dmvpntunnel.ipaddress):
                        dps_tunnel_ip = dps_tunnel_obj.dmvpntunnel.ipaddress
                        acl_url = sec_dev.url + '/acl:access-lists'

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
                                        <name>permit ospf any host ''' + dps_tunnel_ip + '''</name>
                                        <action>permit</action>
                                        <layer4protocol>ospf</layer4protocol>
                                        <source-condition-type>any</source-condition-type>
                                        <dest-condition-type>host</dest-condition-type>
                                        <dest-ip>''' + dps_tunnel_ip + '''</dest-ip>
                                    </acl-rule>
                                    </acl-rules>
                                    </access-list>
                                     '''

                        yang.Sdk.createData(acl_url, acl_payload, sdata.getSession(), False)

                        class_map_url = sec_dev.url + '/qos:class-maps'

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

                        policy_map_url = sec_dev.url + '/qos:policy-maps'

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

                        yang.Sdk.createData(sec_dev.url, control_plane_obj.getxml(filter=True), sdata.getSession(), False)

                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',6)
                        site_url = '/'.join(uri_list[0:6])

                        site_payload = '''
                                        <failover-state>true</failover-state>
                                       '''
                        yang.Sdk.createData(site_url, site_payload, sdata.getSession(), False)
                    else:
                        raise Exception("No IP Address found on DPS Tunnel100. Cannot Proceed with DPS switch off.")
        else:
            raise Exception("No Overlay Tunnel100 interface found on device. Cannot Proceed with DPS switch off.")
    

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
