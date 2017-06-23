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
                                                                           policy-update-services
                                                                                                 |
                                                                                                 hsrp-update-service
                                                                                                                    
Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/hsrp-update-service
"""
"""
Names of Leafs for this Yang Entity
cpe-primary-hsrp-priority
cpe-secondary-hsrp-priority
cpe-tertiary-hsrp-priority

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
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        uri = sdata.getRcPath()
        parent_uri = uri[:uri.rfind('/policy-update-services')]
        print parent_uri

        xml_output = yang.Sdk.getData(parent_uri, '', sdata.getTaskId())
        serv_data = util.parseXmlString(xml_output).triple_cpe_site_services
        print 'service_obj: %s' % (serv_data)

        inputdict = {}
        inputdict['cpe_primary_hsrp_priority'] = config.get_field_value('cpe_primary_hsrp_priority')
        inputdict['cpe_secondary_hsrp_priority'] = config.get_field_value('cpe_secondary_hsrp_priority')
        inputdict['cpe_tertiary_hsrp_priority'] = config.get_field_value('cpe_tertiary_hsrp_priority')
        if inputdict['cpe_primary_hsrp_priority']:
            eps = get_endpoint_with_deviceip(serv_data.cpe_primary.device_ip, serv_data.cpe_lan.get_field_value('end_points', True))
            if not eps:
                raise Exception('Unable to get end-points for cpe-primary device')
            else:
                # trigger update on the entities
                for ep in eps:
                    device = devicemgr.getDeviceById(serv_data.cpe_primary.device_ip)
                    # lan_uri = "%s/cpe-lan" % (parent_uri)
                    # site_output = yang.Sdk.getData(lan_uri, '', sdata.getTaskId())
                    # conf = util.parseXmlString(site_output)
                    version = None
                    lan_ic_uri1 = "%s/cpe-lan/end-points=%s" % (parent_uri, ep.endpoint_name)
                    site_output1 = yang.Sdk.getData(lan_ic_uri1, '', sdata.getTaskId())
                    conf1 = util.parseXmlString(site_output1)
                    interface_name = conf1.end_points.interface_name
                    if hasattr(conf1.end_points, 'profile_name'):
                        lan_profile = conf1.end_points.profile_name
                        lan_ic_uri2 = "%s/cpe-lan/lan-profile=%s" % (parent_uri, lan_profile)
                        site_output2 = yang.Sdk.getData(lan_ic_uri2, '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output2)
                        hsrp_obj = devices.device.interfaces.interface.hsrp.hsrp()
                        if hasattr(conf.lan_profile, 'hsrp_version'):
                            version = conf.lan_profile.hsrp_version
                        # else:
                        #     raise Exception("Lan profile does not have hsrp version")
                        if hasattr(conf.lan_profile, 'hsrp_group'):
                            hsrp_obj.group = conf.lan_profile.hsrp_group
                            # else:
                            #     raise Exception("Lan profile does not have hsrp group")
                    else:
                        lan_uri = "%s/cpe-lan" % (parent_uri)
                        site_output = yang.Sdk.getData(lan_uri, '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        hsrp_obj = devices.device.interfaces.interface.hsrp.hsrp()
                        if hasattr(conf.cpe_lan, 'hsrp_version'):
                            version = conf.cpe_lan.hsrp_version
                        # else:
                        #     raise Exception("Cpe lan does not have hsrp version")
                        if hasattr(conf.cpe_lan, 'hsrp_group'):
                            hsrp_obj.group = conf.cpe_lan.hsrp_group
                            # else:
                            #     raise Exception("Cpe lan does not have hsrp group")
                    if util.isNotEmpty(hsrp_obj.getxml(filter=True)):
                        hsrp_obj.version = version
                        hsrp_obj.priority = inputdict['cpe_primary_hsrp_priority']

                        hsrp_url = device.url + "/interfaces/interface=%s" % util.make_interfacename(interface_name)
                        yang.Sdk.createData(hsrp_url, hsrp_obj.getxml(filter=True), sdata.getSession(), False)
                        lan_ic_uri = "%s/cpe-lan/end-points=%s" % (parent_uri, ep.endpoint_name)
                        prefix = "<end-points><endpoint-name>%s</endpoint-name>" % ep.endpoint_name
                        suffix = "</end-points>"
                        payload = "%s<hsrp-priority>%s</hsrp-priority>%s" % (prefix, inputdict['cpe_primary_hsrp_priority'], suffix)
                        yang.Sdk.patchData(lan_ic_uri, payload, sdata, False)

        if inputdict['cpe_secondary_hsrp_priority']:
            eps = get_endpoint_with_deviceip(serv_data.cpe_secondary.device_ip, serv_data.cpe_lan.get_field_value('end_points', True))
            if not eps:
                raise Exception('Unable to get end-points for cpe-secondary device')
            else:
                # trigger update on the entities
                for ep in eps:
                    device = devicemgr.getDeviceById(serv_data.cpe_secondary.device_ip)
                    # lan_uri = "%s/cpe-lan" % (parent_uri)
                    # site_output = yang.Sdk.getData(lan_uri, '', sdata.getTaskId())
                    # conf = util.parseXmlString(site_output)
                    version = None
                    lan_ic_uri1 = "%s/cpe-lan/end-points=%s" % (parent_uri, ep.endpoint_name)
                    site_output1 = yang.Sdk.getData(lan_ic_uri1, '', sdata.getTaskId())
                    conf1 = util.parseXmlString(site_output1)
                    interface_name = conf1.end_points.interface_name
                    if hasattr(conf1.end_points, 'profile_name'):
                        lan_profile = conf1.end_points.profile_name
                        lan_ic_uri2 = "%s/cpe-lan/lan-profile=%s" % (parent_uri, lan_profile)
                        site_output2 = yang.Sdk.getData(lan_ic_uri2, '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output2)
                        hsrp_obj = devices.device.interfaces.interface.hsrp.hsrp()
                        if hasattr(conf.lan_profile, 'hsrp_version'):
                            version = conf.lan_profile.hsrp_version
                        # else:
                        #     raise Exception("Lan profile does not have hsrp version")
                        if hasattr(conf.lan_profile, 'hsrp_group'):
                            hsrp_obj.group = conf.lan_profile.hsrp_group
                            # else:
                            #     raise Exception("Lan profile does not have hsrp group")
                    else:
                        lan_uri = "%s/cpe-lan" % (parent_uri)
                        site_output = yang.Sdk.getData(lan_uri, '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        hsrp_obj = devices.device.interfaces.interface.hsrp.hsrp()
                        if hasattr(conf.cpe_lan, 'hsrp_version'):
                            version = conf.cpe_lan.hsrp_version
                        # else:
                        #     raise Exception("Cpe lan does not have hsrp version")
                        if hasattr(conf.cpe_lan, 'hsrp_group'):
                            hsrp_obj.group = conf.cpe_lan.hsrp_group
                            # else:
                            #     raise Exception("Cpe lan does not have hsrp group")

                    if util.isNotEmpty(hsrp_obj.getxml(filter=True)):
                        hsrp_obj.version = version
                        hsrp_obj.priority = inputdict['cpe_secondary_hsrp_priority']

                        hsrp_url = device.url + "/interfaces/interface=%s" % util.make_interfacename(interface_name)
                        yang.Sdk.createData(hsrp_url, hsrp_obj.getxml(filter=True), sdata.getSession(), False)
                        lan_ic_uri = "%s/cpe-lan/end-points=%s" % (parent_uri, ep.endpoint_name)
                        prefix = "<end-points><endpoint-name>%s</endpoint-name>" % ep.endpoint_name
                        suffix = "</end-points>"
                        payload = "%s<hsrp-priority>%s</hsrp-priority>%s" % (prefix, inputdict['cpe_secondary_hsrp_priority'], suffix)
                        yang.Sdk.patchData(lan_ic_uri, payload, sdata, False)

        if inputdict['cpe_tertiary_hsrp_priority']:
            eps = get_endpoint_with_deviceip(serv_data.cpe_tertiary.device_ip, serv_data.cpe_lan.get_field_value('end_points', True))
            if not eps:
                raise Exception('Unable to get end-points for cpe-tertiary device')
            else:
                # trigger update on the entities
                for ep in eps:
                    device = devicemgr.getDeviceById(serv_data.cpe_secondary.device_ip)
                    # lan_uri = "%s/cpe-lan" % (parent_uri)
                    # site_output = yang.Sdk.getData(lan_uri, '', sdata.getTaskId())
                    # conf = util.parseXmlString
                    version = None
                    lan_ic_uri1 = "%s/cpe-lan/end-points=%s" % (parent_uri, ep.endpoint_name)
                    site_output1 = yang.Sdk.getData(lan_ic_uri1, '', sdata.getTaskId())
                    conf1 = util.parseXmlString(site_output1)
                    interface_name = conf1.end_points.interface_name
                    if hasattr(conf1.end_points, 'profile_name'):
                        lan_profile = conf1.end_points.profile_name
                        lan_ic_uri2 = "%s/cpe-lan/lan-profile=%s" % (parent_uri, lan_profile)
                        site_output2 = yang.Sdk.getData(lan_ic_uri2, '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output2)
                        hsrp_obj = devices.device.interfaces.interface.hsrp.hsrp()
                        if hasattr(conf.lan_profile, 'hsrp_version'):
                            version = conf.lan_profile.hsrp_version
                        # else:
                        #     raise Exception("Lan profile does not have hsrp version")
                        if hasattr(conf.lan_profile, 'hsrp_group'):
                            hsrp_obj.group = conf.lan_profile.hsrp_group
                            # else:
                            #     raise Exception("Lan profile does not have hsrp group")
                    else:
                        lan_uri = "%s/cpe-lan" % (parent_uri)
                        site_output = yang.Sdk.getData(lan_uri, '', sdata.getTaskId())
                        conf = util.parseXmlString(site_output)
                        hsrp_obj = devices.device.interfaces.interface.hsrp.hsrp()
                        if hasattr(conf.cpe_lan, 'hsrp_version'):
                            version = conf.cpe_lan.hsrp_version
                        # else:
                        #     raise Exception("Cpe lan does not have hsrp version")
                        if hasattr(conf.cpe_lan, 'hsrp_group'):
                            hsrp_obj.group = conf.cpe_lan.hsrp_group
                            # else:
                            #     raise Exception("Cpe lan does not have hsrp group")

                    if util.isNotEmpty(hsrp_obj.getxml(filter=True)):
                        hsrp_obj.version = version
                        hsrp_obj.priority = inputdict['cpe_tertiary_hsrp_priority']

                        hsrp_url = device.url + "/interfaces/interface=%s" % util.make_interfacename(interface_name)
                        yang.Sdk.createData(hsrp_url, hsrp_obj.getxml(filter=True), sdata.getSession(), False)
                        lan_ic_uri = "%s/cpe-lan/end-points=%s" % (parent_uri, ep.endpoint_name)
                        prefix = "<end-points><endpoint-name>%s</endpoint-name>" % ep.endpoint_name
                        suffix = "</end-points>"
                        payload = "%s<hsrp-priority>%s</hsrp-priority>%s" % (prefix, inputdict['cpe_tertiary_hsrp_priority'], suffix)
                        yang.Sdk.patchData(lan_ic_uri, payload, sdata, False)

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


def get_endpoint_with_deviceip(device_ip, endpoints_list):
    items = []
    for item in endpoints_list:
        print "%s, %s" % (device_ip, item)
        if item.device_ip == device_ip:
            items.append(item)
    return items


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
