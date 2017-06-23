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
                                    ipsec
                                         |
                                         delete-ipsec-profile
                                                             
Schema Representation:

/services/managed-cpe-services/customer/ipsec/delete-ipsec-profile
"""
"""
Names of Leafs for this Yang Entity
  ipsec-profile-name
"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr
from servicemodel.controller import devices

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log


class ServiceDataCustomization:

    @staticmethod
    def process_service_create_data(smodelctx, sdata, dev, **kwargs):
        """ Custom API to modify the inputs"""
        modify = True
        if modify and kwargs is not None:
            for key, value in kwargs.iteritems():
                log("%s == %s" %(key,value))

        if modify:
            config = kwargs['config']
            inputdict = kwargs['inputdict']
            inputkeydict = kwargs['inputkeydict']
            if inputdict['single_cpe_site'] == "true":
                if len(inputdict['single_cpe_sites']) > 0:
                    if isinstance(inputdict['single_cpe_sites'], list) is True:
                        for site in inputdict['single_cpe_sites']:
                            uri = sdata.getRcPath()
                            uri_list = uri.split('/',5)
                            url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe'
                            delete_ipsec(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-site/single-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe'
                        delete_ipsec(entity, conf, sdata, **kwargs)

            if inputdict['dual_cpe_site'] == "true":
                if len(inputdict['dual_cpe_sites']) > 0:
                    if isinstance(inputdict['dual_cpe_sites'], list) is True:
                        for site in inputdict['dual_cpe_sites']:
                            uri = sdata.getRcPath()
                            uri_list = uri.split('/',5)
                            url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary'
                            delete_ipsec(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary'
                            delete_ipsec(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-site/dual-cpe-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary'
                        delete_ipsec(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary'
                        delete_ipsec(entity, conf, sdata, **kwargs)

            if inputdict['single_cpe_dual_wan_site'] == "true":
                if len(inputdict['single_cpe_dual_wan_sites']) > 0:
                    if isinstance(inputdict['single_cpe_dual_wan_sites'], list) is True:
                        for site in inputdict['single_cpe_dual_wan_sites']:
                            uri = sdata.getRcPath()
                            uri_list = uri.split('/',5)
                            url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_dual'
                            delete_ipsec(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['single_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_dual'
                        delete_ipsec(entity, conf, sdata, **kwargs)

            if inputdict['triple_cpe_site'] == "true":
                if len(inputdict['triple_cpe_sites']) > 0:
                    if isinstance(inputdict['triple_cpe_sites'], list) is True:
                        for site in inputdict['triple_cpe_sites']:
                            uri = sdata.getRcPath()
                            uri_list = uri.split('/',5)
                            url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary_triple'
                            delete_ipsec(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_triple'
                            delete_ipsec(entity, conf, sdata, **kwargs)
                            entity = 'cpe_tertiary_triple'
                            delete_ipsec(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['triple_cpe_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/triple-cpe-site/triple-cpe-site-services="+str(site), '',sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_triple'
                        delete_ipsec(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_triple'
                        delete_ipsec(entity, conf, sdata, **kwargs)
                        entity = 'cpe_tertiary_triple'
                        delete_ipsec(entity, conf, sdata, **kwargs)

            if inputdict['dual_cpe_dual_wan_site'] == "true":
                if len(inputdict['dual_cpe_dual_wan_sites']) > 0:
                    if isinstance(inputdict['dual_cpe_dual_wan_sites'], list) is True:
                        for site in inputdict['dual_cpe_dual_wan_sites']:
                            uri = sdata.getRcPath()
                            uri_list = uri.split('/',5)
                            url = '/'.join(uri_list[0:4])
                            site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                            conf = util.parseXmlString(site_output)
                            entity = 'cpe_primary_dual'
                            delete_ipsec(entity, conf, sdata, **kwargs)
                            entity = 'cpe_secondary_dual'
                            delete_ipsec(entity, conf, sdata, **kwargs)
                    else:
                        site = inputdict['dual_cpe_dual_wan_sites']
                        uri = sdata.getRcPath()
                        uri_list = uri.split('/',5)
                        url = '/'.join(uri_list[0:4])
                        site_output = yang.Sdk.getData(url+"/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services="+str(site), '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        entity = 'cpe_primary_dual'
                        delete_ipsec(entity, conf, sdata, **kwargs)
                        entity = 'cpe_secondary_dual'
                        delete_ipsec(entity, conf, sdata, **kwargs)

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
      raise Exception('Update forbidden for node delete-ipsec-profile at path managed-cpe-services/customer/ipsec/delete-ipsec-profile')
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


def delete_ipsec(entity, conf, sdata, **kwargs):
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

    inputdict = kwargs['inputdict']
    ipsec_profile_name = inputdict['ipsec_profile_name']

    url_device_pre_ipsec = '/controller:devices/device=%s' %(device.device.id)
    device_pre_ipsec = yang.Sdk.getData(url_device_pre_ipsec, '', sdata.getTaskId())
    conf_pre_ipsec = util.parseXmlString(device_pre_ipsec)
    if hasattr(conf_pre_ipsec.device, 'ipsec_profiles'):
        url_device_ipsec = '/controller:devices/device=%s/dmvpn:ipsec-profiles' %(device.device.id)
        device_ipsec = yang.Sdk.getData(url_device_ipsec, '', sdata.getTaskId())
        conf_ipsec = util.parseXmlString(device_ipsec)

        device_tunnel = []
        if hasattr(conf_ipsec.ipsec_profiles, 'ipsec_profile'):
            conf_ipsec.ipsec_profiles.ipsec_profile = util.convert_to_list(conf_ipsec.ipsec_profiles.ipsec_profile)
            for ipsec in conf_ipsec.ipsec_profiles.ipsec_profile:
                device_tunnel.append(ipsec.ipsec_profile_name)

        if ipsec_profile_name in device_tunnel:
            ipsec_payload = devices.device.ipsec_profiles.ipsec_profile.ipsec_profile()
            ipsec_payload.ipsec_profile_name = ipsec_profile_name
            ipsec_url = device.url + '/dmvpn:ipsec-profiles/ipsec-profile=%s' % (ipsec_profile_name)
            yang.Sdk.deleteData(ipsec_url, ipsec_payload.getxml(filter=True), sdata.getTaskId(), sdata.getSession())

            ipsec_url = '/controller:devices/device=%s/dmvpn:ipsec-profiles/ipsec-profile=%s' %(device.device.id, ipsec_profile_name)
            ipsec = yang.Sdk.getData(ipsec_url, '', sdata.getTaskId())
            obj_ipsec = util.parseXmlString(ipsec)
            if hasattr(obj_ipsec.ipsec_profile, 'transform_set'):
                transform_set = obj_ipsec.ipsec_profile.transform_set
                transform_url = device.url + '/dmvpn:transform-sets/transform-set=%s' % (transform_set)
                yang.Sdk.deleteData(transform_url, '', sdata.getTaskId(), sdata.getSession())
            if hasattr(obj_ipsec.ipsec_profile, 'ike_profile_name'):
                ike_profile_name = obj_ipsec.ipsec_profile.ike_profile_name

                uri = sdata.getRcPath()
                uri_list = uri.split('/',5)
                url = '/'.join(uri_list[0:4])
                xml_output = yang.Sdk.getData(url+"/ipsec/crypto-profiles/crypto-profile="+str(ike_profile_name), '',sdata.getTaskId())
                obj = util.parseXmlString(xml_output)
                if hasattr(obj.crypto_profile, 'keyring'):
                    key_ring_name = obj.crypto_profile.keyring
                    crypto_profile_url = device.url + '/dmvpn:crypto-keyrings/crypto-keyring=%s' % (key_ring_name)
                    yang.Sdk.deleteData(crypto_profile_url, '', sdata.getTaskId(), sdata.getSession())

                crypto_profile_url = device.url + '/dmvpn:crypto/crypto-profile=%s' % (ike_profile_name)
                yang.Sdk.deleteData(crypto_profile_url, '', sdata.getTaskId(), sdata.getSession())

                if hasattr(obj.crypto_profile, 'policy_number'):
                    policy_number = obj.crypto_profile.policy_number
                    policy_number_url = device.url + '/dmvpn:crypto-policies/crypto-policy=%s' % (policy_number)
                    yang.Sdk.deleteData(policy_number_url, '', sdata.getTaskId(), sdata.getSession())
        else:
            print "Ipsec profile is not in device: ", device
    else:
        print "Ipsec profiles are not in device: ", device


class DeletePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for Deletion"""
        log('operations: %s' % (operations))
        yang.moveOperations(operations, ['DeleteTransformSetWithIKE'], ['DeleteIpsecProfileWithIKE'], True)
        print 'pass1: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoProfileMatchWithIKE'], ['DeleteTransformSetWithIKE'], True)
        print 'pass2: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoProfileWithIKE'], ['DeleteCryptoProfileMatchWithIKE'], True)
        print 'pass3: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoPolicyWithIKE'], ['DeleteCryptoProfileWithIKE'], True)
        print 'pass4: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoPreSharedKeyWithIKE'], ['DeleteCryptoPolicyWithIKE'], True)
        print 'pass5: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoWithIKE'], ['DeleteCryptoPreSharedKeyWithIKE'], True)
        print 'pass6: operations: %s' % (operations)


class CreatePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for creation"""
        log('operations: %s' % (operations))
        yang.moveOperations(operations, ['DeleteTransformSetWithIKE'], ['DeleteIpsecProfileWithIKE'], True)
        print 'pass1: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoProfileMatchWithIKE'], ['DeleteTransformSetWithIKE'], True)
        print 'pass2: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoProfileWithIKE'], ['DeleteCryptoProfileMatchWithIKE'], True)
        print 'pass3: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoPolicyWithIKE'], ['DeleteCryptoProfileWithIKE'], True)
        print 'pass4: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoPreSharedKeyWithIKE'], ['DeleteCryptoPolicyWithIKE'], True)
        print 'pass5: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoWithIKE'], ['DeleteCryptoPreSharedKeyWithIKE'], True)
        print 'pass6: operations: %s' % (operations)
