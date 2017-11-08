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
                                                                           cpe-primary
                                                                                      |
                                                                                      loopback
                                                                                              |
                                                                                              loopback
                                                                                                      
Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-primary/loopback/loopback
"""
"""
Names of Leafs for this Yang Entity
loopback-interface-id
                cidr
                  ip
                 vrf

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
from cpedeployment.endpoint_lib import loopback
from servicemodel.controller.devices.device import interfaces


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
        loopback(smodelctx, sdata, dev, **kwargs)

    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      #raise Exception('Update forbidden for node loopback at path managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-primary/loopback/loopback')
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
        dev = kwargs['dev']
        vrf = inputdict['vrf']
        description = inputdict['description']
        loopback_interface_id = inputdict['loopback_interface_id']
        ip = inputdict['ip']
        for device in util.convert_to_list(dev):
            loopback_url = '/controller:devices/device=%s/interface:interfaces/interface=Loopback%s' % (device.device.id, loopback_interface_id)
            output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>'+loopback_url+'</rc-path></input>')
            ref = util.parseXmlString(output)
            util.log_debug("loopback_xml:%s" %(ref))
            ref_exist = False
            ref_exist_trans = False
            uri = sdata.getRcPath()
            if hasattr(ref.output, 'references'):
                if hasattr(ref.output.references, 'reference'):
                    for each_ref_ref in util.convert_to_list(ref.output.references.reference):
                        if hasattr(each_ref_ref, 'details'):
                            if hasattr(each_ref_ref.details, 'reference_source'):
                                for each_ref_source in util.convert_to_list(each_ref_ref.details.reference_source):
                                    type = each_ref_source.type
                                    rcpath = each_ref_source.rcpath
                                    if rcpath == uri and type != 'OWNED':
                                        ref_exist_trans = True
                        if hasattr(each_ref_ref, 'src_node'):
                            for each_ref in util.convert_to_list(each_ref_ref.src_node):
                                if each_ref == uri:
                                    ref_exist = True

            util.log_debug("loopback_ref:%s,%s" %(ref_exist, ref_exist_trans))

            if ref_exist and ref_exist_trans:
                intf_obj = interfaces.interface.interface()
                loopback_int = 'Loopback' + str(loopback_interface_id)
                intf_obj.name = loopback_int
                intf_obj.long_name = loopback_int
                if util.isNotEmpty(vrf):
                    intf_obj.vrf._empty_tag = True
                if util.isNotEmpty(description):
                    intf_obj.description._empty_tag = True
                if util.isNotEmpty(ip):
                    intf_obj.ip_address._empty_tag = True
                    intf_obj.netmask._empty_tag = True
                uri = device.url + '/interface:interfaces/interface=%s' % (str(loopback_int).replace('/', '%2F'))
                payload = intf_obj.getxml(filter=True)
                yang.Sdk.patchData(uri, payload, sdata, add_reference=False)

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
