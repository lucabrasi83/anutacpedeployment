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
                                                                     port-labels
                                                                                |
                                                                                update-port-label
                                                                                                 
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/port-labels/update-port-label
"""
"""
Names of Leafs for this Yang Entity
     port-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port-label-name
                port            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port
           operation
          type1-site
         type1-sites
          type2-site
         type2-sites

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
        #if dev is None or (isinstance(dev, list) and len(dev) == 0):
        #  return
        import cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization
        dev = cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization.grouping_create_label_configuration_def_port_labels_update_port_label(smodelctx, sdata, dev, **kwargs)

        from servicemodel.device_abs_lib import device_label_configuration

        if inputdict['port_label_name'] is not None and inputdict['port'] is not None and inputdict['operation'] == "CREATE":
          for dev_iterator in dev:
            device_label_configuration.label_configuration.port_label().create(sdata, dev_iterator, fill_map_devices_device_label_configuration_port_label(inputdict), addref=False)

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
        up_map_devices_device_label_configuration_port_label = fill_up_map_devices_device_label_configuration_port_label(inputdict, pinputdict)
        if up_map_devices_device_label_configuration_port_label[1] == 'key-delete-create' or up_map_devices_device_label_configuration_port_label[1] == 'key-delete':
          device_label_configuration.label_configuration.port_label().delete(sdata, dev, pinputdict)
        if up_map_devices_device_label_configuration_port_label[1] == 'key-delete-create' or up_map_devices_device_label_configuration_port_label[1] == 'key-create':
          device_label_configuration.label_configuration.port_label().create(sdata, dev, up_map_devices_device_label_configuration_port_label[0], addref=up_map_devices_device_label_configuration_port_label)
        if up_map_devices_device_label_configuration_port_label[1] == 'key-unchanged':
          device_label_configuration.label_configuration.port_label().update(sdata, dev, fill_map_devices_device_label_configuration_port_label(inputdict))
        import cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization
        cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization.grouping_update_label_configuration_def_port_labels_update_port_label(smodelctx, sdata, **kwargs)

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
        cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization.grouping_delete_label_configuration_def_port_labels_update_port_label(smodelctx, sdata, **kwargs)

def fill_map_devices_device_label_configuration_port_label(inputdict, delete=False):
  mapping_dict_devices_device_label_configuration_port_label = {}
  mapping_dict_devices_device_label_configuration_port_label['port_label_name'] = inputdict['port_label_name']
  mapping_dict_devices_device_label_configuration_port_label['port'] = inputdict['port']
  return mapping_dict_devices_device_label_configuration_port_label


def fill_up_map_devices_device_label_configuration_port_label(inputdict, pinputdict):
  up_mapping_dict_devices_device_label_configuration_port_label = {}
  up_mapping_dict_devices_device_label_configuration_port_label['port_label_name'] = inputdict['port_label_name'] if inputdict['port_label_name'] is not None and inputdict['port_label_name'] != '' else pinputdict['port_label_name']
  up_mapping_dict_devices_device_label_configuration_port_label['port'] = inputdict['port'] if inputdict['port'] is not None and inputdict['port'] != '' else pinputdict['port']
  up_schema = 'key-unchanged'
  del_mandatory = False
  if inputdict['port_label_name'] is not None and pinputdict['port_label_name'] is not None:
    up_schema = 'key-delete-create'
    return [up_mapping_dict_devices_device_label_configuration_port_label, up_schema]
  elif inputdict['port_label_name'] == '':
    up_schema = 'key-delete'
    del_mandatory = True
  elif inputdict['port_label_name'] is not None:
    up_schema = 'key-create'
  else:
    up_schema = 'key-unchanged'
  if del_mandatory and up_schema != 'key-create':
    up_schema = 'key-delete'
  elif del_mandatory and up_schema == 'key-create':
    up_schema = 'key-delete-create'
  return [up_mapping_dict_devices_device_label_configuration_port_label, up_schema]


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
