#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2014-2015 Anuta Networks, Inc. All Rights Reserved.

from servicemodel import util
from servicemodel import yang

from com.anuta.model.base import YangSessionThreadLocal

class Network:

    _instance = None

    def __init__(self):
        from com.anuta.util import ApplicationContextProvider
        ctx = ApplicationContextProvider.getApplicationContext()
        from com.anuta.api import RestconfService
        from com.anuta.api.provider import NetworkResourceMgmtService
        self.restconf = ctx.getBean(RestconfService)
        from com.anuta.service.yang import YangServiceProcessor
        from com.anuta.service.tenant import ResourceUtils
        from com.anuta.operation.service import NetworkService
        self.resourceUtils = ctx.getBean(ResourceUtils)
        self.networkService = ctx.getBean(NetworkService)
        self.yangServiceProcessor = ctx.getBean(YangServiceProcessor)
        self.networkResourceMgmtService = ctx.getBean(NetworkResourceMgmtService)
        from com.anuta.api import RestStyleYangService
        self.restStyleYangService = ctx.getBean(RestStyleYangService)
        self.ctx = ctx
        from com.anuta.service import TaskManager
        self.taskmgr = ctx.getBean(TaskManager)

    @staticmethod
    def getBean(val):
        return Network.getInstance().ctx.getBean(val)

    @staticmethod
    def getInstance():
        if(Network._instance == None):
            Network._instance = Network()
        return Network._instance

    @staticmethod
    def append_taskdetail(taskid, detail):
        Network.getInstance().taskmgr.appendTaskDetails(taskid, detail)

    @staticmethod
    def getNetworkConnections(device_id1, device_id2):
        print 'Device1id = %s' % (device_id1)
        print 'Device2id = %s' % (device_id2)
        networkConns = Network.getInstance().networkResourceMgmtService.getNetworkConnections(device_id1, device_id2)
        return networkConns

    @staticmethod
    def getIpAddressesInSubnet(subnet):
        print 'Network = %s' % (subnet)
        IpaddressList = Network.getInstance().resourceUtils.getAllIpAddressesInSubnet(subnet)
        print 'IpAddressList = %s' % (IpaddressList)
        return IpaddressList


    @staticmethod
    def getInterfacesListForDevice(ipaddress):
        print 'Rxvd IpAddress = %s' % (ipaddress)
        deviceInfsList = svc = Network.getInstance().networkResourceMgmtService.fetchDeviceInterfaceByDeviceId(ipaddress)
        print 'DeviceInfsList = %s' % (deviceInfsList)
        return deviceInfsList




