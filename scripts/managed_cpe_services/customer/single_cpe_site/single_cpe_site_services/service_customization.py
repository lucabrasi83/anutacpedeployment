#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2015-2016 Anuta Networks, Inc. All Rights Reserved.
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
                                                                           
Schema Representation:

/services/managed-cpe-services/customer/single-cpe-site/single-cpe-site-services
"""
"""
Names of Leafs for this Yang Entity
           site-name
              bgp-as
         description
       resource-pool
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
        devbindobjs = kwargs['devbindobjs']
        import time
        now = time.strftime("%Y-%b-%d %I:%M %p %Z", time.localtime())
        if sdata.isServiceDiscoveryEnabled() == True:
            payload = '<brownfield-site>true</brownfield-site>'
        else:
            payload = '<greenfield-site>true</greenfield-site>'

        payload_time = '<created-on>' + now + '</created-on>'
        yang.Sdk.createData(sdata.getRcPath(), payload, sdata.getSession(), False)
        yang.Sdk.createData(sdata.getRcPath(), payload_time, sdata.getSession(), False)

        taskid = sdata.getTaskId()

        output = yang.Sdk.invokeRpc('tasks:get-basic-task-detail', '<taskId>' + str(taskid) + '</taskId>')
        basic_task_details_out = util.parseXmlString(output)
        if hasattr(basic_task_details_out, 'taskDetail'):
            if hasattr(basic_task_details_out.taskDetail, 'userName'):
              taskuser = basic_task_details_out.taskDetail.userName

              payload_user = '<created-by>' + str(taskuser) + '</created-by>'
              yang.Sdk.createData(sdata.getRcPath(), payload_user, sdata.getSession(), False)

    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      #raise Exception('Update forbidden for node single-cpe-site-services at path managed-cpe-services/customer/single-cpe-site/single-cpe-site-services')
      modify = False
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

    @staticmethod
    def process_service_delete_data(smodelctx, sdata, **kwargs):
      """callback called for delete operation"""
      modify = False
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))


class DeletePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for Deletion"""
        log('operations: %s' % (operations))
        #yang.moveOperations(operations, ['DeleteRouteMap', 'DeleteInterface'], ['DeleteRouteMapActions', 'DeleteRouteMapConditions', 'UpdateInterface'], True)
        yang.moveOperations(operations, ['DeleteRouterBGPAggregateSummaryNetwork', 'DeleteRouterBGPNetwork', 'DeleteRouterEigrpRedistribute', 'DeleteRouterEigrpSummaryMetric','deleteVrfRouterEigrpNetwork', 'DeleteRouterEigrpNetwork'], ['DeleteRouterBGPRedistribute'], True)
        print 'pass: operations: %s' % (operations)

        yang.moveOperations(operations, ['DeleteRouterBGP', 'deleteVrfRouterEigrp', 'removeRouterEigrp'], ['DeleteRouterBGPNeighbor', 'DeleteRouterEigrpDistributeList', 'DeleteRouterEigrpRedistribute', 'DeleteRouterEigrpSummaryMetric', 'deleteVrfRouterEigrpNetwork', 'DeleteRouterEigrpNetwork', 'DeleteRouterBGPAggregateSummaryNetwork', 'DeleteRouterBGPNetwork'], True)
        print 'pass0: operations: %s' % (operations)
        print 'pass01: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteInterface', 'DeleteInterfaceEigrp', 'DeleteInterfaceEigrpSummaryNetwork', 'DeleteInterfaceOspf', 'DeleteInterfaceHSRP', 'UpdateInterface'], ['DeleteRouterOspf'], True)
        print 'pass12: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteRouteMap', 'DeleteInterface'], ['DeleteRouteMapActions', 'DeleteRouteMapConditions', 'DeleteInterfaceEigrp', 'DeleteInterfaceEigrpSummaryNetwork', 'DeleteInterfaceOspf', 'DeleteInterfaceHSRP'], True)
        yang.moveOperations(operations, ['DeleteQClassMapMatchCondition','DeleteQClassMapMatchConditionHttpUrl','DeleteVrf'], ['DeleteSLA', 'DeleteCryptoWithIKE', 'DeleteRouterBGP', 'DeleteVrfImportMap', 'DeleteVrfExportMap', 'DeleteVrfRTImport', 'DeleteVrfRTExport', 'DeleteVrfRouteEntry', 'DeleteIpNatTranslationInterface', 'DeleteIpNatTranslationPool', 'UpdateInterface','DeleteInterface'], True)
        print 'pass13: operations: %s' % (operations)
        # yang.moveOperations(operations, ['DeleteQClassMapMatchCondition'], ['DeleteQClassMapMatchConditionHttpUrl'], True)
        # print 'pass1: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteQPolicyMapClassEntryQLimit'], ['DeleteQClassMapMatchCondition', 'DeleteQClassMapMatchConditionHttpUrl'], True)
        print 'pass2: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteQPolicyMapClassEntry','UpdateQPolicyMapClassEntry'], ['DeleteQPolicyMapClassEntryQLimit', 'DeleteQClassMapMatchCondition'], True)
        print 'pass3: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteQPolicyMap'], ['DeleteQPolicyMapClassEntry','UpdateQPolicyMapClassEntry'], True)
        print 'pass4: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteQClassMap'], ['DeleteQPolicyMap'], True)
        print 'pass5: operations: %s' % (operations)
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
        #yang.moveOperations(operations, ['DeleteVrf'], ['DeleteCryptoWithIKE'], True)
        print 'pass11: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteSLA'], ['DeleteTrack', 'Deletelistobject', 'DeleteSLASchedule'], True)
        print 'pass12: operations: %s' % (operations)
        yang.moveOperations(operations, ['DeleteAccessList', 'DeleteAclRule'], ['UpdateInterface'], True)

class CreatePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for creation"""
        log('operations: %s' % (operations))
        yang.moveOperations(operations, ['CreateInterface', 'UpdateInterface'], ['CreateQPolicyMap'], True)
        yang.moveOperations(operations, ['CreateInterfaceOspf', 'CreateInterfaceHSRP'], ['CreateInterface', 'UpdateInterface'], True)
        yang.moveOperations(operations, ['CreateRouterBGPPeerGroup'], ['CreateBGPListenRange'], True)
        util.log_debug('pass00: operations: %s' % (operations))
        '''
        yang.moveOperations(operations, ['CreateQPolicyMap', 'CreateVrf'], ['CreateInterface'], False)
        print 'pass01: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateVrf'], ['CreateInterface', 'UpdateInterface'], False)
        print 'pass02: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateQPolicyMap'], ['CreateVrf'], True)
        print 'pass03: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateInterface', 'UpdateInterface'], ['UpdateVrf'], True)
        print 'pass04: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateAccessList'], ['CreateVrf'], True)
        print 'pass05: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateVrf'], ['CreateRouterBGP'], False)
        print 'pass05: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateInterface'], ['CreateRouteMap'], False)
        print 'pass07: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateInterface'], ['CreateRoute'], False)
        print 'pass08: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateDmvpnTunnel'], ['CreateVrfRouteEntry', 'CreateRoute'], False)
        print 'pass09: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateInterface'], ['CreateVrfRouteEntry', 'CreateRoute'], False)
        print 'pass10: operations: %s' % (operations)
        #yang.moveOperations(operations, ['CreateRoute'], ['CreateDmvpnTunnel','CreateInterface'], True)
        #print 'pass10: operations: %s' % (operations)
        #yang.moveOperations(operations, ['CreateRoute','CreateVrfRouteEntry'], ['createRouterEigrp','createRouterEigrpNetwork'], True)
        #print 'pass11: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateRouterBGPNeighbor'], ['CreateRouterBGP'], True)
        print 'pass12: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateRouterBGPRedistribute'], ['CreateRouterBGP'], True)
        print 'pass13: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateInterface', 'UpdateInterface'], ['CreateQPolicyMap', 'CreateVrf'], True)
        print 'pass14: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateAclRule'], ['CreateAccessList'], True)
        print 'pass15: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateAclRule'], ['UpdateInterface'], False)
        print 'pass16: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateObjectGroup', 'CreateNetworkGroup'], ['CreateAccessList'], False)
        print 'pass17: operations: %s' % (operations)
        '''
        # yang.moveOperations(operations, ['CreateInterface'], ['UpdateVrf'], True)
        # print 'pass01: operations: %s' % (operations)
        # yang.moveOperations(operations, ['CreateInterface'], ['CreateVrf'], True)
        # print 'pass02: operations: %s' % (operations)
        # yang.moveOperations(operations, ['CreateAccessList'], ['CreateVrf'], True)
        # print 'pass03: operations: %s' % (operations)
        # yang.moveOperations(operations, ['CreateAclRule'], ['CreateAccessList'], True)
        # print 'pass04: operations: %s' % (operations)
        # yang.moveOperations(operations, ['CreateQPolicyMap'], ['CreateVrf'], True)
        # print 'pass05: operations: %s' % (operations)
        # #yang.moveOperations(operations, ['CreateVrf'], ['CreateRouterBGP'], False)
        # #print 'pass05: operations: %s' % (operations)
        # yang.moveOperations(operations, ['CreateInterface'], ['CreateRouteMap'], False)
        # print 'pass06: operations: %s' % (operations)
        # yang.moveOperations(operations, ['CreateInterface'], ['CreateRoute'], False)
        # print 'pass07: operations: %s' % (operations)
        # yang.moveOperations(operations, ['CreateVrfRouteEntry'], ['CreateDmvpnTunnel','CreateInterface'], True)
        # print 'pass08: operations: %s' % (operations)
        # yang.moveOperations(operations, ['CreateRoute'], ['CreateDmvpnTunnel','CreateInterface'], True)
        # print 'pass09: operations: %s' % (operations)
        # yang.moveOperations(operations, ['CreateRoute','CreateVrfRouteEntry'], ['createRouterEigrpNetwork'], True)
        # print 'pass10: operations: %s' % (operations)
        # yang.moveOperations(operations, ['CreateRouterBGPNeighbor'], ['CreateRouterBGP'], True)
        # print 'pass11: operations: %s' % (operations)
        # yang.moveOperations(operations, ['CreateRouterBGPRedistribute'], ['CreateRouterBGP'], True)
        # print 'pass12: operations: %s' % (operations)
