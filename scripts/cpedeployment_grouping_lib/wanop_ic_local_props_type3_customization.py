
from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr


import copy

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import getPreviousObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject
from cpedeployment.cpedeployment_lib import log
from cpedeployment.endpoint_lib import get_used_ip_list_from_ippool,add_ipaddress_entries,IpamPoolID,get_freeip_from_cidr
from com.anuta.api import DataNodeNotFoundException



"""
Names of Leafs for this Yang Entity
      interface-name            maps-to  /ac:devices/ac:device/if:interfaces/interface/name /ac:devices/ac:device/if:interfaces/interface/long-name
        profile-name
        interface-ip            maps-to  /ac:devices/ac:device/if:interfaces/interface/ip-address
         mask-length            maps-to  /ac:devices/ac:device/if:interfaces/interface/ipv4-prefix-length
interface-description            maps-to  /ac:devices/ac:device/if:interfaces/interface/description
               speed            maps-to  /ac:devices/ac:device/if:interfaces/interface/speed
              duplex            maps-to  /ac:devices/ac:device/if:interfaces/interface/duplex
                 mtu            maps-to  /ac:devices/ac:device/if:interfaces/interface/mtu
                 vrf
             vlan-id

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_wanop_ic_local_props_type3_wanop_endpoint(smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs["inputdict"]
    rcpath = sdata.getRcPath()
    cust_name = rcpath.split("/")[3].split("=")[1]
    log("cust_name")
    log(cust_name)
    sctx = ServiceModelContext(kwargs["id"], sdata)
    sobj = sctx.service_obj
    log("sobj")
    log(sobj)
    type1_name = rcpath.split("/")[-4].split("=")[1]
    for each_type3_site in util.convert_to_list(sobj.managed_cpe_services.customer.wanop_services.type3_site.type3_site):
        type1_site_name = each_type3_site.site_name
        if type1_site_name == type1_name:
            site_name = each_type3_site.dual_cpe_sites
            rp = each_type3_site.resource_pool
            if util.isNotEmpty(inputdict["profile_name"]) is not None:
                url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/dual-cpe-site/dual-cpe-site-services="+site_name+"/cpe-lan/lan-profile="+inputdict["profile_name"]
                obj = yang.Sdk.getData(url, '', sdata.getTaskId())
                log("obj")
                log(obj)
                cidr = util.parseXmlString(obj).lan_profile.cidr
                cidr_name = cust_name + '_' + site_name + '_' + cidr
                if util.isNotEmpty(inputdict["interface_ip"]):
                    prefix = util.IPPrefix(cidr)
                    if prefix.is_ip_in_subnet(inputdict["interface_ip"]):
                        used_ip_list = get_used_ip_list_from_ippool(cidr_name, sdata)
                        if inputdict["interface_ip"] in used_ip_list:
                            raise Exception(inputdict["interface_ip"]+'is already used please provide available ip in the cidr:'+cidr)
                        else:
                            ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr_name)
                            ip_addr_obj = ip_addr.ipam_pool_obj
                            add_ipaddress_entries(ip_addr_obj.name, inputdict["interface_ip"], sdata)
                    else:
                        raise Exception(inputdict["interface_ip"]+" is not in Cidr:"+cidr)
                else:
                    ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr_name)
                    ip_addr_obj = ip_addr.ipam_pool_obj
                    used_ip_list = get_used_ip_list_from_ippool(cidr_name, sdata)
                    interface_ip = get_freeip_from_cidr(ip_addr_obj.cidr, used_ip_list)
                    ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr_name)
                    ip_addr_obj = ip_addr.ipam_pool_obj
                    add_ipaddress_entries(ip_addr_obj.name, interface_ip, sdata)
                    inputdict["interface_ip"] = interface_ip
                return inputdict["interface_ip"],cidr.split("/")[1]

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_wanop_ic_local_props_type3_wanop_endpoint(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_wanop_ic_local_props_type3_wanop_endpoint(smodelctx, sdata, **kwargs):
    pass
