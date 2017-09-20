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
import devicemgr


def reserve_license(device_id):
    input_obj = util.create_yang_subtree('input')
    input_obj.device_id = device_id
    output_xml = yang.Sdk.invokeRpc('reserve-license', input_obj.toXml())
    if util.isEmpty(output_xml):
        return None
    obj = util.parseXmlString(output_xml)
    obj = obj.output
    print 'obj = %s' % (obj)
    return obj.get_field_value('license_file_url')

def unreserve_license(device_id):
    input_obj = util.create_yang_subtree('input')
    input_obj.device_id = device_id
    output_xml = yang.Sdk.invokeRpc('unreserve-license', input_obj.toXml())
    print 'output = %s' % (output_xml)

class VMRequest(object):
    def __init__(self):
        self.obj = util.create_yang_subtree('input')

    def mgmt_ip(self, val):
        self.obj.mgmt_ip = val
        return self
    
    def deploy_vm(self, val):
        self.obj.deploy_vm = val
        return self

    def netmask(self, val):
        self.obj.netmask = val
        return self

    def gateway(self, val):
        self.obj.gateway = val
        return self
        
    def vm_name(self, val):
        self.obj.vm_name = val
        return self
        
    def hostname(self, val):
        self.obj.hostname = val
        return self

    def virtual_appliance_image(self, val):
        self.obj.virtual_appliance_image = val
        return self

    def vim_ip(self, val):
        self.obj.vim_ip = val
        return self
    
    def user_data(self, val):
        self.obj.user_data = val
        return self
    
    def params(self, val):
        self.obj.params = val
        return self

    def license_file_url(self, val):
        self.obj.license_file_url = val
        return self

    def skip_deployment(self, val):
        self.obj.skip_deployment = val
        return self

    def request_timeout(self, val):
        self.obj.request_timeout = val
        return self
    
def deploy_vm(sdata, vmreq):
    payload = vmreq.obj.toXml()
    output_xml = yang.Sdk.invokeRpc('deploy-vm', payload)
    return output_xml
    #Excluding the validation for poc as workaround
    # if util.isEmpty(output_xml):
    #     raise Exception("Failed to deploy vm. Unknown error")
    # obj = util.parseXmlString(output_xml)
    # output = obj.get_field_value('output')
    # print 'output = %s' % (output)
    # if util.isNotEmpty(output):
    #     success = output.get_field_value('success')
    #     if success == 'false':
    #         resp = output.get_field_value('response')
    #         if util.isEmpty(resp):
    #             resp = "Failed to deploy vm"
    #         else:
    #             resp = "Failed to deploy vm. Response: %s" % (resp)
    #         raise Exception(resp)

def get_credentialset(sdata, device_ip):
    dev = devicemgr.getDeviceByIp(device_ip)
    csetname = dev.device.get_field_value('credential_set')
    if util.isEmpty(csetname):
        raise Exception('Can\'t get the credentialset')
    url = '/controller:credentials/credential-sets/credential-set=%s' % (util.encode_url(csetname))
    if sdata == None:
        taskid = 'COMMON'
    else:
        taskid = sdata.getTaskId()
    cset = yang.YangObject(url, taskid, 'credential_set')
    cset.load()
    return cset.rootobj

def make_input(sdata, device_ip, vmname, timeout = 180):
    dev = devicemgr.getDeviceByIp(device_ip)
    if dev == None:
        return None
    mgmtstation_ip = dev.device.get_field_value('management_station')
    if util.isEmpty(mgmtstation_ip):
        raise Exception('Can\'t find vcenter for: %s' % (device_ip))
    cset = get_credentialset(sdata, mgmtstation_ip)
    username = cset.username
    password = util.decode_password(cset.password)

    if vmname == None:
        name = dev.device.name
    else:
        name = vmname
        
    input_obj = util.create_yang_subtree('input')
    input_obj.mgmt_ip = mgmtstation_ip
    input_obj.device_name = dev.device.name
    input_obj.name = name
    input_obj.user_name = username
    input_obj.request_timeout = '%d' % (timeout)
    payload = input_obj.toXml()
    print 'payload = %s' % (payload)
    input_obj.password = password

    return input_obj
    
def destroy_vm(sdata, device_ip, vmname = None, timeout = 180):
    input_obj = make_input(sdata, device_ip, vmname)
    if input_obj == None:
        return
    payload = input_obj.toXml()
    return yang.Sdk.invokeRpc('vm-destroy', payload, False)
    
def poweroff_vm(sdata, device_ip, vmname = None, timeout = 180):
    input_obj = make_input(sdata, device_ip, vmname)
    if input_obj == None:
        return
    payload = input_obj.toXml()
    return yang.Sdk.invokeRpc('vm-power-off', payload, False)
    
def poweron_vm(sdata, device_ip, vmname = None, timeout = 180):
    input_obj = make_input(sdata, device_ip, vmname)
    if input_obj == None:
        return
    payload = input_obj.toXml()
    return yang.Sdk.invokeRpc('vm-power-on', payload, False)

class Is_ip_used_in_blucecat(object):
    def __init__(self):
        self.obj = util.create_yang_subtree('input')

    def ip_address(self, val):
        self.obj.ip_address = val
        return self
    
    def network_id(self, val):
        self.obj.network_id = val
        return self

    def device_id(self, val):
        self.obj.device_id = val
        return self

class Get_next_IP_address(object):
    def __init__(self):
        self.obj = util.create_yang_subtree('input')

    def ipv4_network_id(self, val):
        self.obj.ipv4_network_id = val
        return self

    def device_id(self, val):
        self.obj.device_id = val
        return self

def is_ip_used(payloadobj):
    payload = payloadobj.obj.toXml()
    return yang.Sdk.invokeRpc('bluecat:is-ip-used', payload, False)

def get_next_ip(payloadobj):
    payload = payloadobj.obj.toXml()
    return yang.Sdk.invokeRpc('bluecat:get-next-available-ip-address', payload, False)


