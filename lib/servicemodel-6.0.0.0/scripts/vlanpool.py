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
import sys

class VlanPool:

    _instance = None
    _use_remote = False

    def __init__(self):
        from com.anuta.util import ApplicationContextProvider
        ctx = ApplicationContextProvider.getApplicationContext()
        self.ctx = ctx
        from com.anuta.resourcemgmt.vlan import VlanPoolService
        self.vlanPoolSvc = ctx.getBean(VlanPoolService)

    @staticmethod
    def getInstance():
        if(VlanPool._instance == None):
            if VlanPool._use_remote:
                import vlanremote
                VlanPool._instance = ipamremote.VlanPool.getInstance()
            else:
                VlanPool._instance = VlanPool()
        return VlanPool._instance

    @staticmethod
    def __get_pool_svc():
        poolsvc = VlanPool.getInstance().vlanPoolSvc.getVlanService()
        if poolsvc == None:
            raise(Exception('IPAM service is not available'))
        return poolsvc

    @util.wrappedmethod()
    def allocate_vlan(self, vlanPoolGroupName, vlanPoolName, vlan = -1):
        if vlan < 0:
            return self.__get_pool_svc().allocateVlan(vlanPoolGroupName, vlanPoolName)
        else:
            return self.__get_pool_svc().allocateVlan(vlanPoolGroupName, vlanPoolName, vlan)

    @util.wrappedmethod()
    def deallocate_vlan(self, vlanPoolGroupName, vlanPoolName, vlan):
        self.__get_pool_svc().deallocateVlan(vlanPoolGroupName, vlanPoolName, int(vlan))

    @util.wrappedmethod()
    def deallocate_vlan_by_resource_pool(self, vlanPoolGroupName, resourcePoolName, vlan):
        self.__get_pool_svc().deallocateVlanByResourcePool(vlanPoolGroupName, resourcePoolName, int(vlan))

    @util.wrappedmethod()
    def allocate_vlan_by_group(self, vlanPoolGroupName):
        return self.__get_pool_svc().allocateVlanByVlanPoolGroup(vlanPoolGroupName)

    @util.wrappedmethod()
    def allocate_vlan_by_group_and_vlan(self, vlanPoolGroupName, vlan):
        return self.__get_pool_svc().allocateVlanByVlanPoolGroup(vlanPoolGroupName, int(vlan))

    @util.wrappedmethod()
    def allocate_vlan_by_resource_pool(self, vlanPoolGroupName, resourcePoolName):
        return self.__get_pool_svc().allocateVlanByResourcePool(vlanPoolGroupName, resourcePoolName)

def allocate_vlan(vlanPoolGroupName, vlanPoolName, vlan = -1):
    return VlanPool.getInstance().allocate_vlan(vlanPoolGroupName, vlanPoolName, vlan)

def deallocate_vlan(vlanPoolGroupName, vlanPoolName, vlan):
    return VlanPool.getInstance().deallocate_vlan(vlanPoolGroupName, vlanPoolName, vlan)

def deallocate_vlan_by_resource_pool(vlanPoolGroupName, resourcePoolName, vlan):
    VlanPool.getInstance().deallocate_vlan_by_resource_pool(vlanPoolGroupName, resourcePoolName, vlan)

def allocate_vlan_by_group(vlanPoolGroupName):
    return VlanPool.getInstance().allocate_vlan_by_group(vlanPoolGroupName)

def allocate_vlan_by_group_and_vlan(vlanPoolGroupName, vlan):
    return VlanPool.getInstance().allocate_vlan_by_group_and_vlan(vlanPoolGroupName, vlan)

def allocate_vlan_by_resource_pool(vlanPoolGroupName, resourcePoolName):
    return VlanPool.getInstance().allocate_vlan_by_resource_pool(vlanPoolGroupName, resourcePoolName)
