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
import sys

#from com.anuta.model.base import YangSessionThreadLocal

class Infoblox:

    _instance = None
    _use_remote = False

    def __init__(self):
        from com.anuta.util import ApplicationContextProvider
        ctx = ApplicationContextProvider.getApplicationContext()
        self.ctx = ctx
        from com.anuta.api import InfobloxService
        self.infobloxSession = ctx.getBean(InfobloxService)

    @staticmethod
    def getBean(val):
        return Infoblox.getInstance().ctx.getBean(val)

    @staticmethod
    def getInstance():
        if(Infoblox._instance == None):
            if Infoblox._use_remote:
                import ipamremote
                Infoblox._instance = InfobloxRemote.getInstance()
            else:
                Infoblox._instance = Infoblox()
        return Infoblox._instance

    def createCPENATReservation(self, dev_ip, cidn, cust_name, dns_name, view_name):
        return self.infobloxSession.createCPENATReservation(dev_ip, cidn, cust_name, dns_name, view_name)

    def getCustomerNetworkRange(self, dev_ip, cidn):
        return self.infobloxSession.getCustomerNetworkRange(dev_ip, cidn)

    def getCPENATNetworkRange(self, dev_ip, cidn):
        return self.infobloxSession.getCPENATNetworkRange(dev_ip, cidn)

    def getNetworkByTypeAndCidn(self, dev_ip, network_type, cidn):
        return self.infobloxSession.getNetworkByTypeAndCidn(dev_ip, network_type, cidn)

    def getNetworkByIpAddress(self, dev_ip, ip_address):
        return self.infobloxSession.getNetworkByIpAddress(dev_ip, ip_address)

    def getIpAddressesFromNetwork(self, dev_ip, network_type, no_of_ips):
        return self.infobloxSession.getIpAddressesFromNetwork(dev_ip, network_type, no_of_ips)

    def createContextInsideReservation(self, device_ip, cidn, cust_name, cmi_pop_name, dns_name, dns_mappings_list, num_of_ips, view = 'default'):
        import java.util.ArrayList as ArrayList
        rip_dns_mappings_list = ArrayList()
        for a in dns_mappings_list:
            rip_dns_mappings_list.add(a)
        return self.infobloxSession.createContextInsideReservation(device_ip, cidn, cust_name, cmi_pop_name, dns_name, rip_dns_mappings_list, num_of_ips, view)

    def getContextInsideIpAddresses(self, dev_ip, no_of_ips):
        return self.infobloxSession.getContextInsideIpAddresses(dev_ip, no_of_ips)

    def getContextOutsideIpAddresses(self, dev_ip, cidn, no_of_ips):
        return self.infobloxSession.getContextOutsideIpAddresses(dev_ip, cidn, no_of_ips)

    def createDNSHostReservation(self, dev_ip, ip_address, record_name, cidn, cust_name, view_name, address_type):
        import java.util.HashMap as HashMap
        fields = HashMap()
        fields.put("CIDN", cidn)
        fields.put("CUSTNAME", cust_name)
        fields.put("ADDRESSTYPE", address_type)
        return self.infobloxSession.createDNSHostReservation(dev_ip, ip_address, record_name, fields, view_name)

    def createDNSAReservation(self, dev_ip, ip_address, record_name, cidn, cust_name, view_name, address_type):
        import java.util.HashMap as HashMap
        fields = HashMap()
        fields.put("CIDN", cidn)
        fields.put("CUSTNAME", cust_name)
        fields.put("ADDRESSTYPE", address_type)
        return self.infobloxSession.createDNSAReservation(dev_ip, ip_address, record_name, fields, view_name)

    def deleteDNSHostReservation(self, dev_ip, ip_address, record_name, view_name):
        return self.infobloxSession.deleteDNSHostReservation(dev_ip, ip_address, record_name, view_name)

    def deleteDNSAReservation(self, dev_ip, ip_address, record_name, view_name):
        return self.infobloxSession.deleteDNSAReservation(dev_ip, ip_address, record_name, view_name)

class IPAM:

    _instance = None
    _use_remote = False

    def __init__(self):
        from com.anuta.util import ApplicationContextProvider
        ctx = ApplicationContextProvider.getApplicationContext()
        self.ctx = ctx
        from com.anuta.service.tenant import YangIpaddressPoolService
        self.ipaddressPoolService = ctx.getBean(YangIpaddressPoolService)

    @staticmethod
    def getInstance():
        if(IPAM._instance == None):
            if IPAM._use_remote:
                import ipamremote
                IPAM._instance = ipamremote.IPAMRemote.getInstance()
            else:
                IPAM._instance = IPAM()
        return IPAM._instance

    @staticmethod
    def __get_pool_svc():
        poolsvc = IPAM.getInstance().ipaddressPoolService.getIpAddresPoolService()
        if poolsvc == None:
            raise(Exception('IPAM service is not available'))
        return poolsvc

    @staticmethod
    @util.wrappedmethod()
    def getFreeIpaddressPoolFromGroup(group, count = 1):
        ipPoolSvc = IPAM.__get_pool_svc()
        return ipPoolSvc.getFreeIpaddressPoolFromGroup(group)

    @staticmethod
    def allocateIpAddressFromGroupAndResourcePool(ipamGroup, resourcePool, ipAddress, desc = None):
        print 'ipamGroupm = %s, resourcePool = %s, ipAddress = %s, desc = %s' % (ipamGroup, resourcePool, ipAddress, desc)
        ipPoolSvc = IPAM.__get_pool_svc()
        return ipPoolSvc.allocateIpAddressFromGroupAndResourcePool(ipamGroup, resourcePool, ipaddress, desc)

    @staticmethod
    def deallocateIpAddressFromGroupAndResourcePool(ipamGroup, ipAddress, resourcePool = None):
        print 'ipAddress = %s, ipamGroup = %s, resourcePool = %s' % (ipamGroup, ipAddress, resourcePool)
        ipPoolSvc = IPAM.__get_pool_svc()
        ipPoolSvc.deallocateIpAddressFromGroupAndResourcePool(ipamGroup, ipAddress, resourcePool)

    @staticmethod
    def allocateIpAddressInIpam(poolId, description, ipAddress=None):
        print 'poolId = %s' % (poolId)
        ipPoolSvc = IPAM.__get_pool_svc()
        Ipaddress = ipPoolSvc.allocateIpAddress(poolId, description, ipAddress)
        print 'IpAddress = %s' % (Ipaddress)
        return Ipaddress

    @staticmethod
    def deallocateIpAddressInIpam(poolId, ipAddress):
        print 'poolId = %s' % (poolId)
        ipPoolSvc = IPAM.__get_pool_svc()
        Ipaddress = ipPoolSvc.deallocateIpAddress(poolId, ipAddress)
        print 'IpAddress = %s' % (Ipaddress)
        return Ipaddress

    @staticmethod
    def allocateIpAddress(ipAddressPool, ipAddress):
        print 'ipAddressPool = %s, ipAddress = %s' % (ipAddressPool, ipAddress)
        ipPoolSvc = IPAM.__get_pool_svc()
        ret = ipPoolSvc.allocateIpAddress(ipAddressPool, ipAddress)
        print 'returning %s' % (ret)
        return ret
    
def get_free_ipaddress_pool_from_group(group, count = 1):
    return IPAM.getInstance().getFreeIpaddressPoolFromGroup(group, count)

def allocate_ipaddress_from_group_and_resource_pool(ipamGroup, resourcePool, ipAddress, desc = None):
    return IPAM.getInstance().allocateIpAddressFromGroupAndResourcePool(ipamGroup, resourcePool, ipAddress, desc)

def deallocate_ipaddress_from_group_and_resource_pool(ipamGroup, ipAddress, resourcePool = None):
    IPAM.getInstance().deallocateIpAddressFromGroupAndResourcePool(ipamGroup, ipAddress, resourcePool)

def allocate_ipaddress_from_ipam_pool(poolId, description, ipAddress=None):
    return IPAM.getInstance().allocateIpAddressInIpam(poolId, description, ipAddress)

def deallocate_ipaddress_from_ipam_pool(poolId, ipAddress):
    return IPAM.getInstance().deallocateIpAddressInIpam(poolId, ipAddress)

def allocate_ip_address(ipAddressPool, ipAddress):
    return IPAM.getInstance().allocateIpAddress(ipAddressPool, ipAddress)

def get_ipam_pool_object(poolname, task_id):
        rcpath = '/ipam:ipaddress-pools/ipaddress-pool=%s' % (util.make_rcpath(poolname))
        yangobj = yang.YangObject(rcpath, task_id, 'ipaddress_pool')
        yangobj.load()
        return yangobj

def get_ipam_group_object(poolname, task_id):
        rcpath = '/ipam:ipaddress-pool-groups/ipaddress-pool-group=%s' % (util.make_rcpath(poolname))
        yangobj = yang.YangObject(rcpath, task_id, 'ipaddress_pool')
        yangobj.load()
        return yangobj

class IpamPool(object):
    def __init__(self, group, count):
        self.group = group
        self.count = count
        self.addresses = []
        self.selected_pool = None
        self.cidr = None
        
    @util.wrappedmethod()
    def set_selected_pool(self, pool):
        self.selected_pool = pool
        yangobj = get_ipam_pool_object(pool, 'COMMON')
        yangobj.load()
        self.cidr = yangobj.rootobj

    @util.wrappedmethod()
    def allocate(self, description = None):
        group = self.group
        count = self.count
        pools = IPAM.getFreeIpaddressPoolFromGroup(group, count)
        if util.isEmpty(pools):
            raise Exception('Unable to allocate from group: %s. count = %s' % (group, count))
        def allocate_from_pool(pool, count, description):
            ips = []
            for i in range(0, count):
                addr = IPAM.allocateIpAddress(pool, description)
                if util.isNotEmpty(addr):
                    ips.append(addr)
                    continue
                # cleanup and return
                print 'Unable to allocate required ips. ips = %s' % (ips)
                for ip in ips:
                    IPAM.deallocateIpAddressInIpam(pool, addr)
                return []
            return ips
        
        if description == None:
            description = 'Allocating from group: %s. count = %d' % (group, count)
        for pool in pools:
            ips = allocate_from_pool(pool, count, description)
            if util.isNotEmpty(ips):
                self.addresses = ips
                self.set_selected_pool(pool)
                return ips
        raise Exception('Unable to allocate from group: %s. count = %s' % (group, count))
        
    @util.wrappedmethod()
    def release(self, ips, resource_pool = None):
        for ip in ips:
            IPAM.deallocateIpAddressFromGroupAndResourcePool(self.group, ip, resource_pool)

