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
                                                  applications
                                                              |
                                                              update-application
                                                                                
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/applications/update-application
"""
"""
Names of Leafs for this Yang Entity
    application-name            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/name
               group            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/group
       business-crit            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/business-crit
            category            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/category
         description
        traffic-type            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/traffic-type
      transport-prot            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/transport-prot
                dscp            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/dscp
                vlan            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/vlan
          local-port            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/local-port
         remote-port            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/remote-port
           local-net            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/local-net
          remote-net            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/remote-net
            app-prot            maps-to  /ac:devices/ac:device/wanop-device:wanop-applications/wanop-application/app-prot
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

        import cpedeployment.cpedeployment_grouping_lib.application_def_customization
        dev = cpedeployment.cpedeployment_grouping_lib.application_def_customization.grouping_create_application_def_update_application(smodelctx, sdata, dev, **kwargs)

        from servicemodel.device_abs_lib import device_wanop_applications

        if inputdict['application_name'] is not None and inputdict['operation'] == "CREATE":
          for dev_iterator in dev:
            device_wanop_applications.wanop_applications.wanop_application().create(sdata, dev_iterator, fill_map_devices_device_wanop_applications_wanop_application(inputdict), addref=False)

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

        from servicemodel.device_abs_lib import device_wanop_applications

        import cpedeployment.cpedeployment_grouping_lib.application_def_customization
        dev = cpedeployment.cpedeployment_grouping_lib.application_def_customization.grouping_update_application_def_update_application(smodelctx, sdata, **kwargs)

        if dev is not None:
          for dev_iterator in util.convert_to_list(dev):
            up_map_devices_device_wanop_applications_wanop_application = fill_up_map_devices_device_wanop_applications_wanop_application(inputdict, pinputdict)
            if up_map_devices_device_wanop_applications_wanop_application[1] == 'key-delete-create' or up_map_devices_device_wanop_applications_wanop_application[1] == 'key-delete':
              device_wanop_applications.wanop_applications.wanop_application().delete(sdata, dev_iterator, pinputdict)
            if up_map_devices_device_wanop_applications_wanop_application[1] == 'key-delete-create' or up_map_devices_device_wanop_applications_wanop_application[1] == 'key-create':
              device_wanop_applications.wanop_applications.wanop_application().create(sdata, dev_iterator, up_map_devices_device_wanop_applications_wanop_application[0], addref=up_map_devices_device_wanop_applications_wanop_application)
            if up_map_devices_device_wanop_applications_wanop_application[1] == 'key-unchanged':
              device_wanop_applications.wanop_applications.wanop_application().update(sdata, dev_iterator, fill_map_devices_device_wanop_applications_wanop_application(inputdict))


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

        import cpedeployment.cpedeployment_grouping_lib.application_def_customization
        cpedeployment.cpedeployment_grouping_lib.application_def_customization.grouping_delete_application_def_update_application(smodelctx, sdata, **kwargs)

def fill_map_devices_device_wanop_applications_wanop_application(inputdict, delete=False):
  mapping_dict_devices_device_wanop_applications_wanop_application = {}
  mapping_dict_devices_device_wanop_applications_wanop_application['business_crit'] = inputdict['business_crit'] if not delete else ''
  mapping_dict_devices_device_wanop_applications_wanop_application['transport_prot'] = inputdict['transport_prot'] if not delete else ''
  mapping_dict_devices_device_wanop_applications_wanop_application['remote_net'] = inputdict['remote_net'] if not delete else ''
  mapping_dict_devices_device_wanop_applications_wanop_application['name'] = inputdict['application_name']
  mapping_dict_devices_device_wanop_applications_wanop_application['remote_port'] = inputdict['remote_port'] if not delete else ''
  mapping_dict_devices_device_wanop_applications_wanop_application['group'] = inputdict['group'] if not delete else ''
  mapping_dict_devices_device_wanop_applications_wanop_application['local_port'] = inputdict['local_port'] if not delete else ''
  mapping_dict_devices_device_wanop_applications_wanop_application['traffic_type'] = inputdict['traffic_type'] if not delete else ''
  mapping_dict_devices_device_wanop_applications_wanop_application['dscp'] = inputdict['dscp'] if not delete else ''
  mapping_dict_devices_device_wanop_applications_wanop_application['vlan'] = inputdict['vlan'] if not delete else ''
  mapping_dict_devices_device_wanop_applications_wanop_application['local_net'] = inputdict['local_net'] if not delete else ''
  mapping_dict_devices_device_wanop_applications_wanop_application['app_prot'] = inputdict['app_prot'] if not delete else ''
  mapping_dict_devices_device_wanop_applications_wanop_application['category'] = inputdict['category'] if not delete else ''
  mapping_dict_devices_device_wanop_applications_wanop_application['description'] = inputdict['description'] if not delete else ''

  #Below are Helper mapping_dict device leafs which are not mapped in service yang
  return mapping_dict_devices_device_wanop_applications_wanop_application


def fill_up_map_devices_device_wanop_applications_wanop_application(inputdict, pinputdict):
  up_mapping_dict_devices_device_wanop_applications_wanop_application = {}
  up_mapping_dict_devices_device_wanop_applications_wanop_application['business_crit'] = inputdict['business_crit']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['transport_prot'] = inputdict['transport_prot']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['remote_net'] = inputdict['remote_net']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['name'] = inputdict['application_name'] if inputdict['application_name'] is not None and inputdict['application_name'] != '' else pinputdict['application_name']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['remote_port'] = inputdict['remote_port']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['group'] = inputdict['group']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['local_port'] = inputdict['local_port']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['traffic_type'] = inputdict['traffic_type']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['dscp'] = inputdict['dscp']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['vlan'] = inputdict['vlan']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['local_net'] = inputdict['local_net']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['app_prot'] = inputdict['app_prot']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['category'] = inputdict['category']
  up_mapping_dict_devices_device_wanop_applications_wanop_application['description'] = inputdict['description']
  up_schema = 'key-unchanged'
  del_mandatory = False
  if inputdict['application_name'] is not None and pinputdict['application_name'] is not None:
    up_schema = 'key-delete-create'
    return [up_mapping_dict_devices_device_wanop_applications_wanop_application, up_schema]
  elif inputdict['application_name'] == '':
    up_schema = 'key-delete'
    del_mandatory = True
  elif inputdict['application_name'] is not None:
    up_schema = 'key-create'
  else:
    up_schema = 'key-unchanged'
  if del_mandatory and up_schema != 'key-create':
    up_schema = 'key-delete'
  elif del_mandatory and up_schema == 'key-create':
    up_schema = 'key-delete-create'
  return [up_mapping_dict_devices_device_wanop_applications_wanop_application, up_schema]


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
