#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2014-2015 Anuta Networks, Inc. All Rights Reserved.

import util
import sys
import remote

#from com.anuta.model.base import YangSessionThreadLocal

class InfobloxRemote:

    _instance = None

    @staticmethod
    def getBean(val):
        raise Exception('unsupported')

    @staticmethod
    def getInstance():
        if(InfobloxRemote._instance == None):
            InfobloxRemote._instance = InfobloxRemote()
        return InfobloxRemote._instance

    def createCPENATReservation(self, dev_ip, cidn, cust_name, dns_name, view_name):
        obj = {'requestType' : 'createCPENATReservation', 'params' : {'deviceIp' : dev_ip, 'cidn' : cidn, 'custName' : cust_name, 'dnsName' : dns_name, 'viewName' : view_name}}
        resp_obj = remote.Session.instance().send_and_get_response(obj)

    def getCustomerNetworkRange(self, dev_ip, cidn):
        obj = {'requestType' : 'getCustomerNetworkRange', 'params' : {'deviceIp' : dev_ip, 'cidn' : cidn}}
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        return resp_obj['payload']

    def getCPENATNetworkRange(self, dev_ip, cidn):
        obj = {'requestType' : 'getCPENATNetworkRange', 'params' : {'deviceIp' : dev_ip, 'cidn' : cidn}}
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        return resp_obj['payload']

    def getNetworkByTypeAndCidn(self, dev_ip, network_type, cidn):
        obj = {'requestType' : 'getNetworkByTypeAndCidn', 'params' : {'deviceIp' : dev_ip, 'networkType' : network_type, 'cidn' : cidn}}
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        return resp_obj['payload']

    def getNetworkByIpAddress(self, dev_ip, ip_address):
        obj = {'requestType' : 'getNetworkByIpAddress', 'params' : {'deviceIp' : dev_ip, 'ipAddress' : ip_address}}
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        return resp_obj['payload']

    def getIpAddressesFromNetwork(self, dev_ip, network_type, no_of_ips):
        obj = {'requestType' : 'getIpAddressesFromNetwork', 'params' : {'deviceIp' : dev_ip, 'networkType' : network_type, 'numOfIps' : no_of_ips}}
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        return resp_obj['resultList']

    def createContextInsideReservation(self, device_ip, cidn, cust_name, cmi_pop_name, dns_name, dns_mappings_list, num_of_ips, view = 'default'):
        params = {'deviceIp' : device_ip, 'cidn' : cidn, 'custName' : cust_name, 'cmiPopName' : cmi_pop_name, 'dnsName' : dns_name, 'numOfIps' : num_of_ips, 'viewName' : view}
        obj = {'requestType' : 'createContextInsideReservation', 'params' : params, 'paramMap' : {'dnsMappings' : dns_mappings_list}}
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        return resp_obj['payload']

    def getContextInsideIpAddresses(self, dev_ip, no_of_ips):
        params = {'deviceIp' : dev_ip, 'numOfIps' : no_of_ips}
        obj = {'requestType' : 'getContextInsideIpAddresses', 'params' : params}
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        return resp_obj['resultList']

    def getContextOutsideIpAddresses(self, dev_ip, cidn, no_of_ips):
        obj = {'requestType' : 'getContextOutsideIpAddresses', 'params' : {'deviceIp' : dev_ip, 'cidn' : cidn, 'numOfIps' : no_of_ips}}
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        return resp_obj['resultList']

    def createDNSHostReservation(self, dev_ip, ip_address, record_name, cidn, cust_name, view_name, address_type):
        params = {'deviceIp' : dev_ip, 'ipAddress' : ip_address, 'dnsRecordName' : record_name, 'cidn' : cidn, 'custName' : cust_name, 'viewName' : view_name, 'addressType' : address_type}
        obj = {'requestType' : 'createDNSHostReservation', 'params' : params}
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        return resp_obj['payload']

    def createDNSAReservation(self, dev_ip, ip_address, record_name, cidn, cust_name, view_name, address_type):
        params = {'deviceIp' : dev_ip, 'ipAddress' : ip_address, 'dnsRecordName' : record_name, 'cidn' : cidn, 'custName' : cust_name, 'viewName' : view_name, 'address_type' : address_type}
        obj = {'requestType' : 'createDNSAReservation', 'params' : params}
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        return resp_obj['payload']

class IPAMRemote:

    _instance = None

    @staticmethod
    def getBean(val):
        raise Exception('unsupported')

    @staticmethod
    def getInstance():
        if(IPAMRemote._instance == None):
            IPAMRemote._instance = IPAMRemote()
        return IPAMRemote._instance

    def allocateIpAddressFromGroupAndResourcePool(self, ipaddress, desc, ipamGroup = None, resourcePool = None):
        obj = {'requestType' : 'ipam.allocateIpAddressFromGroupAndResourcePool', 'params' : {'ipAddress' : ipaddress, 'desc' : desc, 'ipamGroup' : ipamGroup, 'resourcePool' : resourcePool}}
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        return resp_obj['payload']

    def deallocateIpAddressFromGroupAndResourcePool(ipAddress, ipamGroup, resourcePool = None):
        obj = {'requestType' : 'ipam.deallocateIpAddressFromGroupAndResourcePool', 'params' : {'ipAddress' : ipaddress, 'ipamGroup' : ipamGroup, 'resourcePool' : resourcePool}}
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        return resp_obj['payload']
