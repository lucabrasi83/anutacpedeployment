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
#DO NOT EDIT THIS FILE ITS AUTOGENERATED ONE
#ALL THE CUSTOMIZATIONS REGARDING DATAPROCESSING SHOULD BE WRITTEN INTO service_customization.py FILE
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
                                                  type4-site
                                                            |
                                                            type4-site
                                                                      |
                                                                      wanop-primary
                                                                                   |
                                                                                   inpath-rules
                                                                                               |
                                                                                               inpath-rules
                                                                                                           
Schema Representation:

/services/managed-cpe-services/customer/wanop-services/type4-site/type4-site/wanop-primary/inpath-rules/inpath-rules
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


import service_customization


class InpathRules(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'inpath_rules')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['rule_type'] = config.get_field_value('rule_type')
        inputdict['packet_mode_uni'] = config.get_field_value('packet_mode_uni')
        inputdict['srcaddr'] = config.get_field_value('srcaddr')
        inputdict['srcport'] = config.get_field_value('srcport')
        inputdict['dstaddr'] = config.get_field_value('dstaddr')
        inputdict['dstport'] = config.get_field_value('dstport')
        inputdict['dst_domain'] = config.get_field_value('dst_domain')
        inputdict['dst_host'] = config.get_field_value('dst_host')
        inputdict['optimization'] = config.get_field_value('optimization')
        inputdict['preoptimization'] = config.get_field_value('preoptimization')
        inputdict['latency_opt'] = config.get_field_value('latency_opt')
        inputdict['vlan'] = config.get_field_value('vlan')
        inputdict['neural_mode'] = config.get_field_value('neural_mode')
        inputdict['cloud_accel'] = config.get_field_value('cloud_accel')
        inputdict['web_proxy'] = config.get_field_value('web_proxy')
        inputdict['wan_visibility'] = config.get_field_value('wan_visibility')
        inputdict['description'] = config.get_field_value('description')
        inputdict['auto_kickoff'] = config.get_field_value('auto_kickoff')
        inputdict['rule_enable'] = config.get_field_value('rule_enable')
        inputdict['rulenum'] = config.get_field_value('rulenum')
        inputdict['protocol'] = config.get_field_value('protocol')
        inputdict['target_addr'] = config.get_field_value('target_addr')
        inputdict['target_port'] = config.get_field_value('target_port')
        inputdict['backup_addr'] = config.get_field_value('backup_addr')
        inputdict['backup_port'] = config.get_field_value('backup_port')
        inputdict["wan_vis_opt"] = config.get_field_value('wan_vis_opt')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'wanop-primary')
        device_mgmt_ip_address = _Gen_obj.wanop_primary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['managed_cpe_services_customer_wanop_services_type4_site_type4_site_site_name'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        inputkeydict['managed_cpe_services_customer_name'] = sdata.getRcPath().split('/')[-7].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'inpath_rules')
        pconfig = getPreviousObjectConfig(id, sdata, 'inpath_rules')
        opaque_args = self.opaque_args

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['rule_type'] = config.get_field_value('rule_type')
        inputdict['packet_mode_uni'] = config.get_field_value('packet_mode_uni')
        inputdict['srcaddr'] = config.get_field_value('srcaddr')
        inputdict['srcport'] = config.get_field_value('srcport')
        inputdict['dstaddr'] = config.get_field_value('dstaddr')
        inputdict['dstport'] = config.get_field_value('dstport')
        inputdict['dst_domain'] = config.get_field_value('dst_domain')
        inputdict['dst_host'] = config.get_field_value('dst_host')
        inputdict['optimization'] = config.get_field_value('optimization')
        inputdict['preoptimization'] = config.get_field_value('preoptimization')
        inputdict['latency_opt'] = config.get_field_value('latency_opt')
        inputdict['vlan'] = config.get_field_value('vlan')
        inputdict['neural_mode'] = config.get_field_value('neural_mode')
        inputdict['cloud_accel'] = config.get_field_value('cloud_accel')
        inputdict['web_proxy'] = config.get_field_value('web_proxy')
        inputdict['wan_visibility'] = config.get_field_value('wan_visibility')
        inputdict['description'] = config.get_field_value('description')
        inputdict['auto_kickoff'] = config.get_field_value('auto_kickoff')
        inputdict['rule_enable'] = config.get_field_value('rule_enable')
        inputdict['rulenum'] = config.get_field_value('rulenum')
        inputdict['protocol'] = config.get_field_value('protocol')
        inputdict['target_addr'] = config.get_field_value('target_addr')
        inputdict['target_port'] = config.get_field_value('target_port')
        inputdict['backup_addr'] = config.get_field_value('backup_addr')
        inputdict['backup_port'] = config.get_field_value('backup_port')
        inputdict["wan_vis_opt"] = config.get_field_value('wan_vis_opt')
        # END OF FETCHING THE LEAF PARAMETERS

        pinputdict = {}

        # START OF FETCHING THE PREVIOUS LEAF PARAMETERS
        pinputdict['rule_type'] = pconfig.get_field_value('rule_type')
        pinputdict['packet_mode_uni'] = pconfig.get_field_value('packet_mode_uni')
        pinputdict['srcaddr'] = pconfig.get_field_value('srcaddr')
        pinputdict['srcport'] = pconfig.get_field_value('srcport')
        pinputdict['dstaddr'] = pconfig.get_field_value('dstaddr')
        pinputdict['dstport'] = pconfig.get_field_value('dstport')
        pinputdict['dst_domain'] = pconfig.get_field_value('dst_domain')
        pinputdict['dst_host'] = pconfig.get_field_value('dst_host')
        pinputdict['optimization'] = pconfig.get_field_value('optimization')
        pinputdict['preoptimization'] = pconfig.get_field_value('preoptimization')
        pinputdict['latency_opt'] = pconfig.get_field_value('latency_opt')
        pinputdict['vlan'] = pconfig.get_field_value('vlan')
        pinputdict['neural_mode'] = pconfig.get_field_value('neural_mode')
        pinputdict['cloud_accel'] = pconfig.get_field_value('cloud_accel')
        pinputdict['web_proxy'] = pconfig.get_field_value('web_proxy')
        pinputdict['wan_visibility'] = pconfig.get_field_value('wan_visibility')
        pinputdict['description'] = pconfig.get_field_value('description')
        pinputdict['auto_kickoff'] = pconfig.get_field_value('auto_kickoff')
        pinputdict['rule_enable'] = pconfig.get_field_value('rule_enable')
        pinputdict['rulenum'] = pconfig.get_field_value('rulenum')
        pinputdict['protocol'] = pconfig.get_field_value('protocol')
        pinputdict['target_addr'] = pconfig.get_field_value('target_addr')
        pinputdict['target_port'] = pconfig.get_field_value('target_port')
        pinputdict['backup_addr'] = pconfig.get_field_value('backup_addr')
        pinputdict['backup_port'] = pconfig.get_field_value('backup_port')
        pinputdict["wan_vis_opt"] = pconfig.get_field_value('wan_vis_opt')
        _Gen_obj = getLocalObject(sdata, 'wanop-primary')
        device_mgmt_ip_address = _Gen_obj.wanop_primary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, pconfig=pconfig, hopaque=opaque_args, inputdict=inputdict, pinputdict=pinputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'inpath_rules')
        opaque_args = self.opaque_args

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['rule_type'] = config.get_field_value('rule_type')
        inputdict['packet_mode_uni'] = config.get_field_value('packet_mode_uni')
        inputdict['srcaddr'] = config.get_field_value('srcaddr')
        inputdict['srcport'] = config.get_field_value('srcport')
        inputdict['dstaddr'] = config.get_field_value('dstaddr')
        inputdict['dstport'] = config.get_field_value('dstport')
        inputdict['dst_domain'] = config.get_field_value('dst_domain')
        inputdict['dst_host'] = config.get_field_value('dst_host')
        inputdict['optimization'] = config.get_field_value('optimization')
        inputdict['preoptimization'] = config.get_field_value('preoptimization')
        inputdict['latency_opt'] = config.get_field_value('latency_opt')
        inputdict['vlan'] = config.get_field_value('vlan')
        inputdict['neural_mode'] = config.get_field_value('neural_mode')
        inputdict['cloud_accel'] = config.get_field_value('cloud_accel')
        inputdict['web_proxy'] = config.get_field_value('web_proxy')
        inputdict['wan_visibility'] = config.get_field_value('wan_visibility')
        inputdict['description'] = config.get_field_value('description')
        inputdict['auto_kickoff'] = config.get_field_value('auto_kickoff')
        inputdict['rule_enable'] = config.get_field_value('rule_enable')
        inputdict['rulenum'] = config.get_field_value('rulenum')
        inputdict['protocol'] = config.get_field_value('protocol')
        inputdict['target_addr'] = config.get_field_value('target_addr')
        inputdict['target_port'] = config.get_field_value('target_port')
        inputdict['backup_addr'] = config.get_field_value('backup_addr')
        inputdict['backup_port'] = config.get_field_value('backup_port')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'wanop-primary')
        device_mgmt_ip_address = _Gen_obj.wanop_primary.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(InpathRules._instance == None):
            InpathRules._instance = InpathRules()
        return InpathRules._instance
