#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2014-2015 Anuta Networks, Inc. All Rights Reserved.

import yang
import util

from com.anuta.service.yang import YangServiceProcessor
from com.anuta.service.yang import YangRpcProcessor

class InventoryRpcProcessor(YangRpcProcessor):
    def __init__(self, rpc):
        self.rpc = rpc
    def processPostRpcOperation(self, res, result):
        task = self.rpc.task_service.getTask(res)
        self.rpc.task_service.waitUntilTaskDone(task, 60)
        task = self.rpc.task_service.getTask(res)
        result.setOutput('status', '%s' % (task.getStatus()))
        details = self.rpc.task_mgr_mongo.getTaskDetails(res)
        if not util.isEmpty(details):
            lines = details.split('\\n')
            for line in lines:
                result.setOutput('details', '<![CDATA[%s]]>' % (line))


    def processRpcOperation(self, result):
        payload = result.getOperationPayload();
        xmlObj = util.parseXmlString(payload)
        print '%s' % (xmlObj)
        inv = xmlObj.start_inventory
        print '%s' % (inv)
        ips = [inv.ip_address]
        print 'ips = %s' % (ips)
        from com.anuta.agentmessage import PingRequestData
        req = PingRequestData(inv.ip_address, 5, 10, None)
        stats = self.rpc.ping_svc.ping(req)
        print 'stats: %s' % (stats)

        if inv.type == 'extended':
            res = self.rpc.network_mgmt_svc.invokeDeviceExtendedInventoryByIp(ips)
            if(util.isEmpty(res)):
                raise('Unable to start')
            res = res.get(0)
        else:
            res = self.rpc.network_mgmt_svc.invokeDeviceInventoryByIp(ips)
            if(util.isEmpty(res)):
                raise('Unable to start')

        print 'task_id = %s' % (res)
        result.setOutput('task-id', res)
        self.rpc.task_mgr.appendTaskDetails(res, 'Invoked from restconf rpc')
        return res

class PingRpcProcessor(YangRpcProcessor):
    def __init__(self, rpc):
        self.rpc = rpc
    def processPostRpcOperation(self, res, result):
        return

    def processRpcOperation(self, result):
        payload = result.getOperationPayload();
        xmlObj = util.parseXmlString(payload)
        print '%s' % (xmlObj)
        inv = xmlObj.device_ping
        print '%s' % (inv)
        from com.anuta.agentmessage import PingRequestData
        req = PingRequestData(inv.ip_address, 5, 10, None)
        stats = self.rpc.ping_svc.ping(req)
        from java.lang import String
        result.setOutput('tx-count', String.valueOf(stats.getTxCount()))
        result.setOutput('rx-count', String.valueOf(stats.getRxCount()))
        result.setOutput('ping-time', String.valueOf(stats.getPingTime()))
        if stats.getErrorMessage() != None:
            result.setOutput('error-msg', stats.getErrorMessage())
        result.setOutput('rtt-min', String.valueOf(stats.getRttMin()))
        result.setOutput('rtt-max', String.valueOf(stats.getRttMax()))
        result.setOutput('rtt-avg', String.valueOf(stats.getRttAverage()))
        result.setOutput('reachable', String.valueOf(stats.isReachable()))
        result.setOutput('successful', String.valueOf(stats.isSuccessful()))
        
        return inv

class Rpc:
    _instance = None

    def __init__(self):
        sdk = yang.Sdk.getInstance()
        print 'sdk = %s' % (sdk)
        self.network_mgmt_svc = sdk.ctx.getBean('networkMgmtService')
        self.yang_service_processor = sdk.ctx.getBean(YangServiceProcessor)
        from com.anuta.api import TaskService
        self.task_service = sdk.ctx.getBean(TaskService)
        from com.anuta.service import TaskManager
        self.task_mgr = sdk.ctx.getBean(TaskManager)
        from com.anuta.service.task import TaskManagerMongoImpl
        self.task_mgr_mongo = sdk.ctx.getBean(TaskManagerMongoImpl)
        self.ping_svc = sdk.ctx.getBean('agentDevicePingTaskRunner')

    def _do_register(self):
        proc = InventoryRpcProcessor(self)
        self.yang_service_processor.registerRpcOperationProcessor('/anuta_rpc/start-inventory', proc)
        proc = PingRpcProcessor(self)
        self.yang_service_processor.registerRpcOperationProcessor('/anuta_rpc/device-ping', proc)

    def _do_unregister(self):
        proc = InventoryRpcProcessor(self)
        self.yang_service_processor.unregisterRpcOperationProcessor('/anuta_rpc/start-inventory')
        self.yang_service_processor.unregisterRpcOperationProcessor('/anuta_rpc/device-ping')
        
    @staticmethod
    def getInstance():
        if Rpc._instance == None:
            Rpc._instance = Rpc()
        return Rpc._instance

    @staticmethod
    def register():
        #Rpc.getInstance()._do_register()
        pass
        
    @staticmethod
    def unregister():
        #Rpc.getInstance()._do_unregister()
        pass
