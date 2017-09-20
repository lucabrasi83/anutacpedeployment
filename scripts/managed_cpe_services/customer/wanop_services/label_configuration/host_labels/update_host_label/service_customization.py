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
                                                                                update-host-label
                                                                                                 
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/update-host-label
"""
"""
Names of Leafs for this Yang Entity
     host-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/host-label-name
            hostname            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/hostname/hostname
              subnet            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/subnet/subnet
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
        id = kwargs['id']
        opaque_args = kwargs['hopaque']
        #if dev is None or (isinstance(dev, list) and len(dev) == 0):
	    # log("returning, len(dev) =" + len(dev))
          #return
        import cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization
        dev = cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization.grouping_create_label_configuration_def_host_labels_update_host_label(smodelctx, sdata, dev, **kwargs)

        from servicemodel.device_abs_lib import device_label_configuration

        if inputdict['host_label_name'] is not None and inputdict['operation'] == "CREATE":
          for dev_iterator in dev:
            device_label_configuration.label_configuration.host_label().create(sdata, dev_iterator, fill_map_devices_device_label_configuration_host_label(inputdict), addref=False)
            if inputdict['subnet'] is not None:
               device_label_configuration.label_configuration.host_label.subnet().create(sdata, dev_iterator, inputdict['host_label_name'], fill_map_devices_device_label_configuration_host_label_subnet(inputdict), addref=False)
            if inputdict['hostname'] is not None:
              device_label_configuration.label_configuration.host_label.hostname().create(sdata, dev_iterator, inputdict['host_label_name'], fill_map_devices_device_label_configuration_host_label_hostname(inputdict), addref=False)

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
        up_map_devices_device_label_configuration_host_label = fill_up_map_devices_device_label_configuration_host_label(inputdict, pinputdict)
        if up_map_devices_device_label_configuration_host_label[1] == 'key-delete-create' or up_map_devices_device_label_configuration_host_label[1] == 'key-delete':
          device_label_configuration.label_configuration.host_label().delete(sdata, dev, pinputdict)
        if up_map_devices_device_label_configuration_host_label[1] == 'key-delete-create' or up_map_devices_device_label_configuration_host_label[1] == 'key-create':
          device_label_configuration.label_configuration.host_label().create(sdata, dev, up_map_devices_device_label_configuration_host_label[0], addref=up_map_devices_device_label_configuration_host_label)
        if up_map_devices_device_label_configuration_host_label[1] == 'key-unchanged':
          device_label_configuration.label_configuration.host_label().update(sdata, dev, fill_map_devices_device_label_configuration_host_label(inputdict, pinputdict, update=True))
        up_map_devices_device_label_configuration_host_label_subnet = fill_up_map_devices_device_label_configuration_host_label_subnet(inputdict, pinputdict)
        if up_map_devices_device_label_configuration_host_label_subnet[1] == 'key-delete-create' or up_map_devices_device_label_configuration_host_label_subnet[1] == 'key-delete':
          device_label_configuration.label_configuration.host_label.subnet().delete(sdata, dev, inputdict['host_label_name'], pinputdict)
        if up_map_devices_device_label_configuration_host_label_subnet[1] == 'key-delete-create' or up_map_devices_device_label_configuration_host_label_subnet[1] == 'key-create':
          device_label_configuration.label_configuration.host_label.subnet().create(sdata, dev, inputdict['host_label_name'], up_map_devices_device_label_configuration_host_label_subnet[0], addref=up_map_devices_device_label_configuration_host_label_subnet)
        if up_map_devices_device_label_configuration_host_label_subnet[1] == 'key-unchanged':
          device_label_configuration.label_configuration.host_label.subnet().update(sdata, dev, inputdict['host_label_name'], fill_map_devices_device_label_configuration_host_label_subnet(inputdict, pinputdict, update=True))
        up_map_devices_device_label_configuration_host_label_hostname = fill_up_map_devices_device_label_configuration_host_label_hostname(inputdict, pinputdict)
        if up_map_devices_device_label_configuration_host_label_hostname[1] == 'key-delete-create' or up_map_devices_device_label_configuration_host_label_hostname[1] == 'key-delete':
          device_label_configuration.label_configuration.host_label.hostname().delete(sdata, dev, inputdict['host_label_name'], pinputdict)
        if up_map_devices_device_label_configuration_host_label_hostname[1] == 'key-delete-create' or up_map_devices_device_label_configuration_host_label_hostname[1] == 'key-create':
          device_label_configuration.label_configuration.host_label.hostname().create(sdata, dev, inputdict['host_label_name'], up_map_devices_device_label_configuration_host_label_hostname[0], addref=up_map_devices_device_label_configuration_host_label_hostname)
        if up_map_devices_device_label_configuration_host_label_hostname[1] == 'key-unchanged':
          device_label_configuration.label_configuration.host_label.hostname().update(sdata, dev, inputdict['host_label_name'], fill_map_devices_device_label_configuration_host_label_hostname(inputdict, pinputdict, update=True))
        import cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization
        cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization.grouping_update_label_configuration_def_host_labels_update_host_label(smodelctx, sdata, **kwargs)

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
        cpedeployment.cpedeployment_grouping_lib.label_configuration_def_customization.grouping_delete_label_configuration_def_host_labels_update_host_label(smodelctx, sdata, **kwargs)

def fill_map_devices_device_label_configuration_host_label(inputdict, pinputdict={}, delete=False, update=False):
  mapping_dict_devices_device_label_configuration_host_label = {}
  mapping_dict_devices_device_label_configuration_host_label['host_label_name'] = inputdict['host_label_name'] if not update else inputdict['host_label_name'] if inputdict['host_label_name'] is not None else pinputdict['host_label_name'] 
  return mapping_dict_devices_device_label_configuration_host_label


def fill_map_devices_device_label_configuration_host_label_subnet(inputdict, pinputdict={}, delete=False, update=False):
  mapping_dict_devices_device_label_configuration_host_label_subnet = {}
  mapping_dict_devices_device_label_configuration_host_label_subnet['subnet'] = inputdict['subnet'] if not delete else ''
  return mapping_dict_devices_device_label_configuration_host_label_subnet


def fill_map_devices_device_label_configuration_host_label_hostname(inputdict, pinputdict={}, delete=False, update=False):
  mapping_dict_devices_device_label_configuration_host_label_hostname = {}
  mapping_dict_devices_device_label_configuration_host_label_hostname['hostname'] = inputdict['hostname'] if not delete else ''
  return mapping_dict_devices_device_label_configuration_host_label_hostname


def fill_up_map_devices_device_label_configuration_host_label(inputdict, pinputdict):
  up_mapping_dict_devices_device_label_configuration_host_label = {}
  up_mapping_dict_devices_device_label_configuration_host_label['host_label_name'] = inputdict['host_label_name'] if inputdict['host_label_name'] is not None and inputdict['host_label_name'] != '' else pinputdict['host_label_name']
  if inputdict['host_label_name'] is None:
    return [up_mapping_dict_devices_device_label_configuration_host_label, 'no-change']
  up_schema = 'key-unchanged'
  del_mandatory = False
  if inputdict['host_label_name'] is not None and pinputdict['host_label_name'] is not None:
    up_schema = 'key-delete-create'
    return [up_mapping_dict_devices_device_label_configuration_host_label, up_schema]
  elif inputdict['host_label_name'] == '':
    up_schema = 'key-delete'
    del_mandatory = True
  elif inputdict['host_label_name'] is not None:
    up_schema = 'key-create'
  else:
    up_schema = 'key-unchanged'
  if del_mandatory and up_schema != 'key-create':
    up_schema = 'key-delete'
  elif del_mandatory and up_schema == 'key-create':
    up_schema = 'key-delete-create'
  return [up_mapping_dict_devices_device_label_configuration_host_label, up_schema]


def fill_up_map_devices_device_label_configuration_host_label_subnet(inputdict, pinputdict):
  up_mapping_dict_devices_device_label_configuration_host_label_subnet = {}
  up_mapping_dict_devices_device_label_configuration_host_label_subnet['subnet'] = inputdict['subnet']
  if inputdict['subnet'] is None:
    return [up_mapping_dict_devices_device_label_configuration_host_label_subnet, 'no-change']
  up_schema = 'key-unchanged'
  del_mandatory = False
  return [up_mapping_dict_devices_device_label_configuration_host_label_subnet, up_schema]


def fill_up_map_devices_device_label_configuration_host_label_hostname(inputdict, pinputdict):
  up_mapping_dict_devices_device_label_configuration_host_label_hostname = {}
  up_mapping_dict_devices_device_label_configuration_host_label_hostname['hostname'] = inputdict['hostname']
  if inputdict['hostname'] is None:
    return [up_mapping_dict_devices_device_label_configuration_host_label_hostname, 'no-change']
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
