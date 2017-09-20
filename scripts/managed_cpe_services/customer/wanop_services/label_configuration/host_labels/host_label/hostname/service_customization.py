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
                                    wanop-services
                                                  |
                                                  label-configuration
                                                                     |
                                                                     host-labels
                                                                                |
                                                                                host-label
                                                                                          |
                                                                                          hostname
                                                                                                  
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/host-label/hostname
"""
"""
Names of Leafs for this Yang Entity
            hostname            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/hostname/hostname

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
        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return
        import cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization
        cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization.grouping_create_label_configuration_def_host_labels_host_label_hostname(smodelctx, sdata, dev, **kwargs)

        _host_label_obj = getLocalObject(sdata, 'host-label')
        inputdict['managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_host_label_name'] = _host_label_obj.host_label.host_label_name
        from servicemodel.device_abs_lib import device_label_configuration
        if inputdict['managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_host_label_name'] is not None:
          device_label_configuration.label_configuration.host_label.hostname().create(sdata, dev, inputdict['managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_host_label_name'], fill_map_devices_device_label_configuration_host_label_hostname(inputdict), addref=True)

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

        #Previous config and previous inputdict
        pconfig = kwargs['pconfig']
        pinputdict = kwargs['pinputdict']

        dev = kwargs['dev']
        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return
        from servicemodel.device_abs_lib import device_label_configuration
        up_map_devices_device_label_configuration_host_label_hostname = fill_up_map_devices_device_label_configuration_host_label_hostname(inputdict, pinputdict)
        if up_map_devices_device_label_configuration_host_label_hostname[1] == 'key-delete-create' or up_map_devices_device_label_configuration_host_label_hostname[1] == 'key-delete':
          device_label_configuration.label_configuration.host_label.hostname().delete(sdata, dev, inputdict['managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_host_label_name'], pinputdict)
        if up_map_devices_device_label_configuration_host_label_hostname[1] == 'key-delete-create' or up_map_devices_device_label_configuration_host_label_hostname[1] == 'key-create':
          device_label_configuration.label_configuration.host_label.hostname().create(sdata, dev, inputdict['managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_host_label_name'], up_map_devices_device_label_configuration_host_label_hostname[0], addref=up_map_devices_device_label_configuration_host_label_hostname)
        if up_map_devices_device_label_configuration_host_label_hostname[1] == 'key-unchanged':
          device_label_configuration.label_configuration.host_label.hostname().update(sdata, dev, inputdict['managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_host_label_name'], fill_map_devices_device_label_configuration_host_label_hostname(inputdict))
        import cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization
        cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization.grouping_update_label_configuration_def_host_labels_host_label_hostname(smodelctx, sdata, **kwargs)

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
        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return
        import cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization
        cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization.grouping_delete_label_configuration_def_host_labels_host_label_hostname(smodelctx, sdata, **kwargs)

def fill_map_devices_device_label_configuration_host_label_hostname(inputdict, delete=False):
  mapping_dict_devices_device_label_configuration_host_label_hostname = {}
  mapping_dict_devices_device_label_configuration_host_label_hostname['hostname'] = inputdict['hostname'] if not delete else ''
  return mapping_dict_devices_device_label_configuration_host_label_hostname


def fill_up_map_devices_device_label_configuration_host_label_hostname(inputdict, pinputdict):
  up_mapping_dict_devices_device_label_configuration_host_label_hostname = {}
  up_mapping_dict_devices_device_label_configuration_host_label_hostname['hostname'] = inputdict['hostname']
  up_schema = 'key-unchanged'
  del_mandatory = False
  return [up_mapping_dict_devices_device_label_configuration_host_label_hostname, up_schema]


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
