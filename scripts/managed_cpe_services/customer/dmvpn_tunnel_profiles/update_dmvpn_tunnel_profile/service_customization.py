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
                                    dmvpn-tunnel-profiles
                                                         |
                                                         update-dmvpn-tunnel-profile
                                                                                    
Schema Representation:

/services/managed-cpe-services/customer/dmvpn-tunnel-profiles/update-dmvpn-tunnel-profile
"""
"""
Names of Leafs for this Yang Entity
                  id
           tunnel-id
           operation
          nhrp-nw-id
          tunnel-key
nhrp-authentication-key
       wan-tunnel-ip
       wan-public-ip
                 mtu
      tcp-adjust-mss
    tunnel-bandwidth
       ipsec-profile
"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr
from servicemodel.controller.devices.device import dmvpntunnels
from servicemodel.controller.devices.device.dmvpntunnels import dmvpntunnel
from servicemodel.controller.devices.device.dmvpntunnels.dmvpntunnel import nhrp_maps
from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log
from cpedeployment.endpoint_lib import IpsecCreation


class ServiceDataCustomization:

    @staticmethod
    def process_service_create_data(smodelctx, sdata, dev, **kwargs):
        """ Custom API to modify the inputs"""
        modify = True
        if modify and kwargs is not None:
            for key, value in kwargs.iteritems():
                log("%s == %s" %(key,value))

        if modify:
            uri = sdata.getRcPath()
            uri_list = uri.split('/',5)
            url = '/'.join(uri_list[0:4])
            config = kwargs['config']
            inputdict = kwargs['inputdict']
            inputkeydict = kwargs['inputkeydict']
            if inputdict['single_cpe_site'] == "true":
                if len(inputdict['single_cpe_sites']) > 0:
                    if isinstance(inputdict['single_cpe_sites'], list) is True:
                        for site in inputdict['single_cpe_sites']:
                            #uri = sdata.getRcPath()
                            #uri_list = uri.split('/',5)
                            #url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe'
                            if inputdict['operation'] == 'DELETE':
                                delete_dmvpn(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        if inputdict['operation'] == 'DELETE':
                            delete_dmvpn(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)

            if inputdict['dual_cpe_site'] == "true":
                if len(inputdict['dual_cpe_sites']) > 0:
                    if isinstance(inputdict['dual_cpe_sites'], list) is True:
                        for site in inputdict['dual_cpe_sites']:
                            #uri = sdata.getRcPath()
                            #uri_list = uri.split('/',5)
                            #url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary'
                            if inputdict['operation'] == 'DELETE':
                                delete_dmvpn(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                            entity = 'cpe_secondary'
                            if inputdict['operation'] == 'DELETE':
                                delete_dmvpn(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_dmvpn(entity, conf, sdata, smodelctx **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary'
                        if inputdict['operation'] == 'DELETE':
                            delete_dmvpn(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                        entity = 'cpe_secondary'
                        if inputdict['operation'] == 'DELETE':
                            delete_dmvpn(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)

            if inputdict['single_cpe_dual_wan_site'] == "true":
                if len(inputdict['single_cpe_dual_wan_sites']) > 0:
                    if isinstance(inputdict['single_cpe_dual_wan_sites'], list) is True:
                        for site in inputdict['single_cpe_dual_wan_sites']:
                            #uri = sdata.getRcPath()
                            #uri_list = uri.split('/',5)
                            #url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_dual'
                            if inputdict['operation'] == 'DELETE':
                                delete_dmvpn(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        if inputdict['operation'] == 'DELETE':
                            delete_dmvpn(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
            if inputdict['triple_cpe_site'] == "true":
                if len(inputdict['triple_cpe_sites']) > 0:
                    if isinstance(inputdict['triple_cpe_sites'], list) is True:
                        for site in inputdict['triple_cpe_sites']:
                            #uri = sdata.getRcPath()
                            #uri_list = uri.split('/',5)
                            #url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary_triple'
                            if inputdict['operation'] == 'DELETE':
                                delete_dmvpn(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                            entity = 'cpe_secondary_triple'
                            if inputdict['operation'] == 'DELETE':
                                delete_dmvpn(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                            entity = 'cpe_tertiary_triple'
                            if inputdict['operation'] == 'DELETE':
                                delete_dmvpn(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                    else:
                        site = inputdict['triple_cpe_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_triple'
                        if inputdict['operation'] == 'DELETE':
                            delete_dmvpn(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                        entity = 'cpe_secondary_triple'
                        if inputdict['operation'] == 'DELETE':
                            delete_dmvpn(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                        entity = 'cpe_tertiary_triple'
                        if inputdict['operation'] == 'DELETE':
                            delete_dmvpn(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)

            if inputdict['dual_cpe_dual_wan_site'] == "true":
                if len(inputdict['dual_cpe_dual_wan_sites']) > 0:
                    if isinstance(inputdict['dual_cpe_dual_wan_sites'], list) is True:
                        for site in inputdict['dual_cpe_dual_wan_sites']:
                            #uri = sdata.getRcPath()
                            #uri_list = uri.split('/',5)
                            #url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary_dual'
                            if inputdict['operation'] == 'DELETE':
                                delete_dmvpn(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                            entity = 'cpe_secondary_dual'
                            if inputdict['operation'] == 'DELETE':
                                delete_dmvpn(entity, conf, sdata, **kwargs)
                            elif inputdict['operation'] == 'CREATE':
                                create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        #uri = sdata.getRcPath()
                        #uri_list = uri.split('/',5)
                        #url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_dual'
                        if inputdict['operation'] == 'DELETE':
                            delete_dmvpn(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                        entity = 'cpe_secondary_dual'
                        if inputdict['operation'] == 'DELETE':
                            delete_dmvpn(entity, conf, sdata, **kwargs)
                        elif inputdict['operation'] == 'CREATE':
                            create_dmvpn(entity, conf, sdata, smodelctx, **kwargs)
                            
            if util.isNotEmpty(inputdict['device_group']):
                dev_group_output = yang.Sdk.invokeRpc('controller:apply-data-grouping', '''<input><group-name>'''+ inputdict['device_group'] + '''</group-name></input>''')
                dev_group_obj = util.parseXmlString(dev_group_output)
                if hasattr(dev_group_obj, 'output'):
                    if hasattr(dev_group_obj.output, 'result'):
                        for each_dev in util.convert_to_list(dev_group_obj.output.result):
                            if hasattr(each_dev, 'device'):
                                if hasattr(each_dev.device, 'id'):
                                    if inputdict['operation'] == 'DELETE':
                                        delete_dmvpn(each_dev.device.id, None, sdata, **kwargs)
                                    elif inputdict['operation'] == 'CREATE':
                                        create_dmvpn(each_dev.device.id, None, sdata, **kwargs)
            modify_dmvpn(sdata, **kwargs)
    @staticmethod
    def process_service_device_bindings(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the device bindings or Call the Business Login Handlers"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']
        devbindobjs = kwargs['devbindobjs']

    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      #raise Exception('Update forbidden for node update-dmvpn-tunnel-profile at path managed-cpe-services/customer/dmvpn-tunnel-profiles/update-dmvpn-tunnel-profile')
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']

    @staticmethod
    def process_service_delete_data(smodelctx, sdata, **kwargs):
      """callback called for delete operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']

def modify_dmvpn(sdata, **kwargs):
    uri = sdata.getRcPath()
    uri_list = uri.split('/', 5)
    url = '/'.join(uri_list[0:4])
    inputdict = kwargs['inputdict']
    name = ''
    tunnel_id = inputdict['tunnel_id']
    dmvpn_output = yang.Sdk.getData(url+"/dmvpn-tunnel-profiles", '', sdata.getTaskId())
    conf = util.parseXmlString(dmvpn_output)
    if hasattr(conf.dmvpn_tunnel_profiles, 'dmvpn_tunnel_profile'):
        conf.dmvpn_tunnel_profiles.dmvpn_tunnel_profile = util.convert_to_list(conf.dmvpn_tunnel_profiles.dmvpn_tunnel_profile)
        for tunnel in conf.dmvpn_tunnel_profiles.dmvpn_tunnel_profile:
            if tunnel.tunnel_id == tunnel_id:
                name = tunnel.name
    if inputdict['operation'] == 'CREATE' and inputdict['update_profile'] == 'true':
        url = url + "/dmvpn-tunnel-profiles/dmvpn-tunnel-profile=" +str(name)
        if util.isNotEmpty(inputdict['nhrp_nw_id']):
            payload = '''
                            <dmvpn-tunnel-profile>
                                <name>'''+name+'''</name>
                                <nhrp-nw-id>'''+inputdict['nhrp_nw_id']+'''</nhrp-nw-id>
                            </dmvpn-tunnel-profile>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
        if util.isNotEmpty(inputdict['tunnel_key']):
            payload = '''
                            <dmvpn-tunnel-profile>
                                <name>'''+name+'''</name>
                                <tunnel-key>'''+inputdict['tunnel_key']+'''</tunnel-key>
                            </dmvpn-tunnel-profile>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
        if util.isNotEmpty(inputdict['nhrp_authentication_key']):
            payload = '''
                            <dmvpn-tunnel-profile>
                                <name>'''+name+'''</name>
                                <nhrp-authentication-key>'''+inputdict['nhrp_authentication_key']+'''</nhrp-authentication-key>
                            </dmvpn-tunnel-profile>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
        if util.isNotEmpty(inputdict['mtu']):
            payload = '''
                            <dmvpn-tunnel-profile>
                                <name>'''+name+'''</name>
                                <mtu>'''+inputdict['mtu']+'''</mtu>
                            </dmvpn-tunnel-profile>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
        if util.isNotEmpty(inputdict['tcp_adjust_mss']):
            payload = '''
                            <dmvpn-tunnel-profile>
                                <name>'''+name+'''</name>
                                <tcp-adjust-mss>'''+inputdict['tcp_adjust_mss']+'''</tcp-adjust-mss>
                            </dmvpn-tunnel-profile>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
        if util.isNotEmpty(inputdict['ipsec_profile']):
            payload = '''
                            <dmvpn-tunnel-profile>
                                <name>'''+name+'''</name>
                                <ipsec-profile>'''+inputdict['ipsec_profile']+'''</ipsec-profile>
                            </dmvpn-tunnel-profile>
                      '''
            yang.Sdk.patchData(url, payload, sdata, add_reference=False)
        if util.isNotEmpty(inputdict['wan_tunnel_ip']) and util.isNotEmpty(inputdict['wan_public_ip']):
            payload = '''
                            <nhrp-maps>
                                <wan-tunnel-ip>'''+inputdict['wan_tunnel_ip']+'''</wan-tunnel-ip>
                                <wan-public-ip>'''+inputdict['wan_public_ip']+'''</wan-public-ip>
                            </nhrp-maps>
                      '''
            yang.Sdk.createData(url, payload, sdata.getSession(), False)

    if inputdict['operation'] == 'DELETE' and inputdict['update_profile'] == 'true':
        if util.isNotEmpty(inputdict['wan_tunnel_ip']) and util.isNotEmpty(inputdict['wan_public_ip']):
            url = url + "/dmvpn-tunnel-profiles/dmvpn-tunnel-profile=" +str(name) + "/nhrp-maps=" + str(inputdict['wan_tunnel_ip']) + "," + str(inputdict['wan_public_ip'])
            if yang.Sdk.dataExists(url):
                yang.Sdk.deleteData(url, '', sdata.getTaskId(), sdata.getSession())


def delete_dmvpn(entity, conf, sdata, **kwargs):
    if entity == 'cpe':
        device = devicemgr.getDeviceById(conf.single_cpe_site_services.cpe.device_ip)
    elif entity == 'cpe_primary':
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_primary.device_ip)
    elif entity == 'cpe_secondary':
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_secondary.device_ip)
    elif entity == 'cpe_dual':
        device = devicemgr.getDeviceById(conf.single_cpe_dual_wan_site_services.cpe.device_ip)
    elif entity == 'cpe_primary_dual':
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip)
    elif entity == 'cpe_secondary_dual':
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip)
    elif entity == 'cpe_primary_triple':
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_primary.device_ip)
    elif entity == 'cpe_secondary_triple':
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_secondary.device_ip)
    elif entity == 'cpe_tertiary_triple':
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_tertiary.device_ip)
    else:
        device = devicemgr.getDeviceById(entity)

    inputdict = kwargs['inputdict']
    tunnel_id = inputdict['tunnel_id']
    wan_tunnel_ip = inputdict['wan_tunnel_ip']
    wan_public_ip = inputdict['wan_public_ip']

    url_device_tunnel = '/controller:devices/device=%s/dmvpn:dmvpntunnels/dmvpntunnel=%s' %(device.device.id, tunnel_id)
    '''
    url_device_pre_tunnel = '/controller:devices/device=%s' %(device.device.id)
    device_pre_tunnel = yang.Sdk.getData(url_device_pre_tunnel, '', sdata.getTaskId())
    conf_pre_tunnel = util.parseXmlString(device_pre_tunnel)

    if hasattr(conf_pre_tunnel.device, 'dmvpntunnels'):
        url_device_tunnel = '/controller:devices/device=%s/dmvpn:dmvpntunnels' %(device.device.id)
        device_tunnel = yang.Sdk.getData(url_device_tunnel, '', sdata.getTaskId())
        conf_tunnel = util.parseXmlString(device_tunnel)

        device_tunnel = []
        if hasattr(conf_tunnel.dmvpntunnels, 'dmvpntunnel'):
            conf_tunnel.dmvpntunnels.dmvpntunnel = util.convert_to_list(conf_tunnel.dmvpntunnels.dmvpntunnel)
            #for tunnel in conf_tunnel.dmvpntunnels.dmvpntunnel:
                #device_tunnel.append(tunnel.name)
            device_tunnel = [tunnel.name for tunnel in conf_tunnel.dmvpntunnels.dmvpntunnel]

        if tunnel_id in device_tunnel:
        '''
    if yang.Sdk.dataExists(url_device_tunnel):
        url_device_tunnel_nhrp = '/controller:devices/device=%s/dmvpn:dmvpntunnels/dmvpntunnel=%s' %(device.device.id, tunnel_id)
        device_tunnel_nhrp = yang.Sdk.getData(url_device_tunnel_nhrp, '', sdata.getTaskId())
        conf_tunnel_nhrp = util.parseXmlString(device_tunnel_nhrp)
        device_tunnel_nhrp = []
        if hasattr(conf_tunnel_nhrp.dmvpntunnel, 'nhrp_maps'):
            conf_tunnel_nhrp.dmvpntunnel.nhrp_maps = util.convert_to_list(conf_tunnel_nhrp.dmvpntunnel.nhrp_maps)
            #for nhrp in conf_tunnel_nhrp.dmvpntunnel.nhrp_maps:
                #if nhrp.sourceip == wan_tunnel_ip and nhrp.destip == wan_public_ip:
                    #device_tunnel_nhrp.append(nhrp.sourceip)
            device_tunnel_nhrp = [nhrp.sourceip for nhrp in conf_tunnel_nhrp.dmvpntunnel.nhrp_maps if nhrp.sourceip == wan_tunnel_ip and nhrp.destip == wan_public_ip]
            if wan_tunnel_ip in device_tunnel_nhrp:
                dmvpn_obj_nhrp = nhrp_maps.nhrp_maps()
                dmvpn_obj_nhrp.sourceip = wan_tunnel_ip
                dmvpn_obj_nhrp.nhrp_type = 'nhs'
                dmvpn_obj_nhrp.destip = wan_public_ip
                dmvpn_obj_nhrp_url = '/controller:devices/device=%s/dmvpn:dmvpntunnels/dmvpntunnel=%s/nhrp-maps=%s,%s' % (device.device.id, tunnel_id, wan_tunnel_ip, wan_public_ip)
                output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+dmvpn_obj_nhrp_url+'</rc-path></input>')
                ref = util.parseXmlString(output)
                # log("xml_op:%s" %(ref))
                if hasattr(ref.output, 'references'):
                    if hasattr(ref.output.references, 'reference'):
                        if hasattr(ref.output.references.reference, 'src_node'):
                            for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                                yang.Sdk.removeReference(each_ref, dmvpn_obj_nhrp_url)
                yang.Sdk.deleteData(dmvpn_obj_nhrp_url, dmvpn_obj_nhrp.getxml(filter=True), sdata.getTaskId(), sdata.getSession())
            else:
                yang.Sdk.append_taskdetail(sdata.getTaskId(), "NHRP Map " + str(wan_tunnel_ip) + " " + str(wan_public_ip) + " DMVPN Tunnel Interface ID " + str(tunnel_id) + " not found on device " + str(device.device.id) + ". Skipping this device")
        else:
            yang.Sdk.append_taskdetail(sdata.getTaskId(), "NHRP Mappings on DMVPN Tunnel Interface ID " + str(tunnel_id) + " not found on device " + str(device.device.id) + ". Skipping this device")
    else:
         yang.Sdk.append_taskdetail(sdata.getTaskId(), "DMVPN Tunnel Interface ID " + str(tunnel_id) + " not found on device " + str(device.device.id) + ". Skipping this device")


def create_dmvpn(entity, conf, sdata, smodelctx, **kwargs):
    fvrf = None
    if entity == 'cpe':
        device = devicemgr.getDeviceById(conf.single_cpe_site_services.cpe.device_ip)
        if hasattr(conf.single_cpe_site_services.cpe_wan, 'end_points'):
            conf.single_cpe_site_services.cpe_wan.end_points = util.convert_to_list(conf.single_cpe_site_services.cpe_wan.end_points)
            for end_point in conf.single_cpe_site_services.cpe_wan.end_points:
                if hasattr(end_point, 'fvrf'):
                 fvrf = end_point.fvrf
    elif entity == 'cpe_primary':
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_primary.device_ip)
        if hasattr(conf.dual_cpe_site_services.cpe_primary_wan, 'end_points'):
            conf.dual_cpe_site_services.cpe_primary_wan.end_points = util.convert_to_list(conf.dual_cpe_site_services.cpe_primary_wan.end_points)
            for end_point in conf.dual_cpe_site_services.cpe_primary_wan.end_points:
                if hasattr(end_point, 'fvrf'):
                    fvrf = end_point.fvrf
    elif entity == 'cpe_secondary':
        device = devicemgr.getDeviceById(conf.dual_cpe_site_services.cpe_secondary.device_ip)
        if hasattr(conf.dual_cpe_site_services.cpe_secondary_wan, 'end_points'):
            conf.dual_cpe_site_services.cpe_secondary_wan.end_points = util.convert_to_list(conf.dual_cpe_site_services.cpe_secondary_wan.end_points)
            for end_point in conf.dual_cpe_site_services.cpe_secondary_wan.end_points:
                if hasattr(end_point, 'fvrf'):
                    fvrf = end_point.fvrf
    elif entity == 'cpe_dual':
        device = devicemgr.getDeviceById(conf.single_cpe_dual_wan_site_services.cpe.device_ip)
        if hasattr(conf.single_cpe_dual_wan_site_services.cpe_primary_wan, 'end_points'):
            conf.single_cpe_dual_wan_site_services.cpe_primary_wan.end_points = util.convert_to_list(conf.single_cpe_dual_wan_site_services.cpe_primary_wan.end_points)
            for end_point in conf.single_cpe_dual_wan_site_services.cpe_primary_wan.end_points:
                if hasattr(end_point, 'fvrf'):
                    fvrf = end_point.fvrf
    elif entity == 'cpe_primary_dual':
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_primary.device_ip)
    elif entity == 'cpe_secondary_dual':
        device = devicemgr.getDeviceById(conf.dual_cpe_dual_wan_site_services.cpe_secondary.device_ip)
    elif entity == 'cpe_primary_triple':
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_primary.device_ip)
    elif entity == 'cpe_secondary_triple':
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_secondary.device_ip)
    elif entity == 'cpe_tertiary_triple':
        device = devicemgr.getDeviceById(conf.triple_cpe_site_services.cpe_tertiary.device_ip)

    inputdict = kwargs['inputdict']
    tunnel_id = inputdict['tunnel_id']
    nhrp_nw_id = inputdict['nhrp_nw_id']
    tunnel_key = inputdict['tunnel_key']
    nhrp_authentication_key = inputdict['nhrp_authentication_key']
    nhrp_holdtime = inputdict['nhrp_holdtime']
    wan_tunnel_ip = inputdict['wan_tunnel_ip']
    wan_public_ip = inputdict['wan_public_ip']
    mtu = inputdict['mtu']
    tcp_adjust_mss = inputdict['tcp_adjust_mss']
    tunnel_bandwidth = inputdict['tunnel_bandwidth']
    ipsec_profile = inputdict['ipsec_profile']
    fvrf = inputdict['fvrf']

    url_device_tunnel = '/controller:devices/device=%s/dmvpn:dmvpntunnels/dmvpntunnel=%s' %(device.device.id, tunnel_id)

    '''
    url_device_pre_tunnel = '/controller:devices/device=%s' %(device.device.id)
    device_pre_tunnel = yang.Sdk.getData(url_device_pre_tunnel, '', sdata.getTaskId())
    conf_pre_tunnel = util.parseXmlString(device_pre_tunnel)

    if hasattr(conf_pre_tunnel.device, 'dmvpntunnels'):
       
        device_tunnel = yang.Sdk.getData(url_device_tunnel, '', sdata.getTaskId())
        conf_tunnel = util.parseXmlString(device_tunnel)

        device_tunnel = []
        if hasattr(conf_tunnel.dmvpntunnels, 'dmvpntunnel'):
            conf_tunnel.dmvpntunnels.dmvpntunnel = util.convert_to_list(conf_tunnel.dmvpntunnels.dmvpntunnel)
            #for tunnel in conf_tunnel.dmvpntunnels.dmvpntunnel:
                #device_tunnel.append(tunnel.name)
            device_tunnel = [tunnel.name for tunnel in conf_tunnel.dmvpntunnels.dmvpntunnel]

        if tunnel_id in device_tunnel:
        '''
    if yang.Sdk.dataExists(url_device_tunnel):
        dmvpn_obj = dmvpntunnels.dmvpntunnel.dmvpntunnel()
        dmvpn_obj.name = tunnel_id
        if util.isNotEmpty(tunnel_bandwidth):
            dmvpn_obj.bandwidth = tunnel_bandwidth
        if util.isNotEmpty(nhrp_authentication_key):
            dmvpn_obj.nhrp_auth_key = nhrp_authentication_key
        if util.isNotEmpty(nhrp_nw_id):
            dmvpn_obj.nhrp_network_id = nhrp_nw_id
        if util.isNotEmpty(mtu):
            dmvpn_obj.mtu = mtu
        if util.isNotEmpty(nhrp_holdtime):
            dmvpn_obj.nhrp_holdtime = nhrp_holdtime
        if util.isNotEmpty(tcp_adjust_mss):
            dmvpn_obj.tcp_adjust_mss = tcp_adjust_mss
        if util.isNotEmpty(tunnel_key):
            dmvpn_obj.tunnel_key = tunnel_key
        if util.isNotEmpty(fvrf) and fvrf != 'GLOBAL':
            dmvpn_obj.front_vrf_name = fvrf
        if util.isNotEmpty(ipsec_profile):
            IpsecCreation(sdata, device, ipsec_profile, fvrf, wan_public_ip, smodelctx)
            dmvpn_obj.ipsec_profile_name = ipsec_profile
            uri = sdata.getRcPath()
            uri_list = uri.split('/', 5)
            url = '/'.join(uri_list[0:4])
            xml_output = yang.Sdk.getData(url+"/ipsec/ipsec-profiles/ipsec-profile="+str(ipsec_profile), '', sdata.getTaskId())
            obj1 = util.parseXmlString(xml_output)
            dmvpn_obj.shared = obj1.ipsec_profile.get_field_value('shared')
        if util.isNotEmpty(wan_tunnel_ip) and util.isNotEmpty(wan_public_ip):
            nhrp_maps_obj_2 = nhrp_maps.nhrp_maps()
            nhrp_maps_obj_2.sourceip = wan_tunnel_ip
            nhrp_maps_obj_2.destip = wan_public_ip
            nhrp_maps_obj_2.nhrp_type = 'nhs'
            yang.Sdk.patchData(device.url+'/dmvpn:dmvpntunnels/dmvpntunnel=%s' % tunnel_id, dmvpn_obj.getxml(filter=True), sdata, add_reference=False)
    else:
        yang.Sdk.append_taskdetail(sdata.getTaskId(), "DMVPN Tunnel Interface ID " + str(tunnel_id) + " not found on device " + str(device.device.id) + ". Skipping this device")         
   


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
