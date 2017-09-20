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
from servicemodel.controller.devices.device import interfaces

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
    inputdict = kwargs['inputdict']
    device = inputdict['device']
    dev = devicemgr.getDeviceById(device)
    failover_lan = inputdict['failover_lan']
    fallback_lan = inputdict['fallback_lan']
    obj = getLocalObject(sdata, 'single-cpe-site-services=')
    if hasattr(obj.single_cpe_site_services.cpe_lan, 'end_points'):
        endpoints = util.convert_to_list(obj.single_cpe_site_services.cpe_lan.end_points)
        for endpoint in endpoints:
            util.log_debug("device: ", device)
            util.log_debug("device: ", endpoint.device_ip)
            if device == endpoint.device_ip:
                if endpoint.interface_type == 'Physical':
                    interface_name = endpoint.interface_name
                elif endpoint.interface_type == 'Sub-Interface':
                    interface_name = endpoint.interface_name + '.' + str(endpoint.vlan_id)
                if failover_lan == 'true':
                    failobj = interfaces.interface.interface()
                    failobj.name = interface_name
                    failobj.long_name = interface_name
                    failobj.admin_state = 'DOWN'
                    yang.Sdk.createData(dev.url + '/interfaces', failobj.getxml(filter=True), sdata.getSession(), False)

                if fallback_lan == 'true':
                    fallobj = interfaces.interface.interface()
                    fallobj.name = interface_name
                    fallobj.long_name = interface_name
                    fallobj.admin_state = 'UP'
                    yang.Sdk.createData(dev.url + '/interfaces', fallobj.getxml(filter=True), sdata.getSession(), False)



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
