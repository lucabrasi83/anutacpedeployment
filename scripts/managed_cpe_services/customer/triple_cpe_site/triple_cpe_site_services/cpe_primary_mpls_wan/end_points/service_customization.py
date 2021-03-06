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
                                                                           cpe-primary-mpls-wan
                                                                                               |
                                                                                               end-points
                                                                                                         
Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-primary-mpls-wan/end-points
"""
"""
Names of Leafs for this Yang Entity
       endpoint-name
           device-ip
                fvrf
                ivrf
                 vrf
      interface-type
      interface-name
             vlan-id
interface-description
         inbound-acl
  global-inbound-acl
    site-inbound-acl
        outbound-acl
 global-outbound-acl
   site-outbound-acl
       dmvpn-profile
                 p2p
tunnel-interface-ip-address
       tunnel-source
    tunnel-bandwidth

"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr


from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log
from cpedeployment.endpoint_lib import wan_endpoint,update_shape_avg
from cpedeployment.endpoint_lib import deallocate_ipaddress_from_ipam
from cpedeployment.endpoint_lib import delete_physical_interface
from cpedeployment.endpoint_lib import update_wan_endpoint


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
        for device in util.convert_to_list(dev):
            wan_endpoint('cpe_primary_mpls_triple', smodelctx, sdata, device, **kwargs)

    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      #raise Exception('Update forbidden for node end-points at path managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-primary-mpls-wan/end-points')
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
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

        for device in util.convert_to_list(dev):
            update_wan_endpoint(sdata, device, **kwargs)

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
        dev = kwargs['dev']
        for device in util.convert_to_list(dev):
            delete_physical_interface('cpe_primary_mpls_triple', smodelctx, sdata, device, **kwargs)


class DeletePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for Deletion"""
        log('operations: %s' % (operations))
        yang.moveOperations(operations, ['DeleteIpsecProfileWithIKE'], ['DeleteDmvpnTunnel'], True)
        print 'pass6: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteTransformSetWithIKE'], ['DeleteIpsecProfileWithIKE'], True)
        print 'pass7: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoProfileMatchWithIKE'], ['DeleteTransformSetWithIKE'], True)
        print 'pass8: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoProfileWithIKE'], ['DeleteCryptoProfileMatchWithIKE'], True)
        print 'pass8_1: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoPolicyWithIKE'], ['DeleteCryptoProfileWithIKE'], True)
        print 'pass9: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoPreSharedKeyWithIKE'], ['DeleteCryptoPolicyWithIKE'], True)
        print 'pass10: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteCryptoWithIKE'], ['DeleteCryptoPreSharedKeyWithIKE'], True)

class CreatePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for creation"""
        log('operations: %s' % (operations))
