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
                                    dual-cpe-site
                                                 |
                                                 dual-cpe-site-services
                                                                       |
                                                                       cpe-secondary
                                                                                    |
                                                                                    vrfs
                                                                                        |
                                                                                        vrf
                                                                                           
Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/cpe-secondary/vrfs/vrf
"""
"""
Names of Leafs for this Yang Entity
                name
            vrf-name
       bgp-router-id
redistribute-connected
redistribute-connected-route-policy
 redistribute-static
redistribute-static-route-policy
aggregate-summary-networks
    summary-networks

"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr


from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log,vrf

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

      if isinstance(dev, list) is True:
          for device in dev:
              vrf('cpe_secondary', device, sdata, **kwargs)
      else:
          vrf('cpe_secondary', dev, sdata, **kwargs)

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
      raise Exception('Update forbidden for node vrf at path managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/cpe-secondary/vrfs/vrf')
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
