
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
from cpedeployment.endpoint_lib import get_used_ip_list_from_ippool,add_ipaddress_entries,IpamPoolID,get_freeip_from_cidr
from com.anuta.api import DataNodeNotFoundException


def grouping_create_wanop_ic_local_props_type4_wanop_endpoint(smodelctx, sdata, dev, **kwargs):
    inputdict = kwargs["inputdict"]

    rcpath = sdata.getRcPath()
    cust_name = rcpath.split("/")[3].split("=")[1]
    log("cust_name")
    log(cust_name)
    sctx = ServiceModelContext(kwargs["id"], sdata)
    sobj = sctx.service_obj
    log("sobj")
    log(sobj)
    type4_name = rcpath.split("/")[-4].split("=")[1]
    for each_type4_site in util.convert_to_list(sobj.managed_cpe_services.customer.wanop_services.type4_site.type4_site):
        type4_site_name = each_type4_site.site_name
        if type4_site_name == type4_name:
            site_name = each_type4_site.single_cpe_sites
            rp = each_type4_site.resource_pool
            if "aux" in inputdict["interface_name"] and util.isEmpty(inputdict["profile_name"]):
                aux_cidr = inputdict["cidr"]
                rcpath1 = sdata.getRcPath()
                if rcpath1.split("/")[-3] == "wanop-secondary":
                    obj = getLocalObject(sdata, "type4-site")
                    if util.isNotEmpty(obj):
                        for wanop_endpoint in util.convert_to_list(obj.type4_site.type4_site.wanop_primary.wanop_endpoints.wanop_endpoint):
                            if wanop_endpoint.interface_name == "aux":
                                primary_cidr =  wanop_endpoint.cidr
                                if primary_cidr != aux_cidr:
                                    raise Exception("Cidr provided in wanop_primary and wanop_secondary should be the same")
                cidr_name = cust_name + '_' + type4_site_name + '_' +aux_cidr
                payload = '''<ipaddress-pool>
                            <name>'''+cidr_name+'''</name>
                            <cidr>'''+aux_cidr+'''</cidr>
                            <resource-pool>'''+rp+'''</resource-pool>
                            </ipaddress-pool>'''
                cidr_url = "/app/restconf/data/ipam:ipaddress-pools"

                # try:
                #     cidr_name_local = cidr_name
                #     cidr_name_local = cidr_name_local.replace('/', '%2F')
                #     get_ipaddress_pool_url = "/app/restconf/data/ipam:ipaddress-pools/ipaddress-pool=%s" %(cidr_name_local)
                #     pool = yang.Sdk.getData(get_ipaddress_pool_url, '', sdata.getTaskId())
                #     pool = util.parseXmlString(pool)
                # except DataNodeNotFoundException:
                #     yang.Sdk.createData(cidr_url, payload, sdata.getSession())
                cidr_name_local = cidr_name
                cidr_name_local = cidr_name_local.replace('/', '%2F')
                get_ipaddress_pool_url = "/app/restconf/data/ipam:ipaddress-pools/ipaddress-pool=%s" %(cidr_name_local)
                if not yang.Sdk.dataExists(get_ipaddress_pool_url):
                    yang.Sdk.createData(cidr_url, payload, sdata.getSession())

                if util.isNotEmpty(inputdict["interface_ip"]):
                    prefix = util.IPPrefix(aux_cidr)
                    if prefix.is_ip_in_subnet(inputdict["interface_ip"]):
                        ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr_name)
                        ip_addr_obj = ip_addr.ipam_pool_obj
                        add_ipaddress_entries(ip_addr_obj.name, inputdict["interface_ip"], sdata)
                        return inputdict["interface_ip"],aux_cidr.split("/")[1]
                    else:
                        raise Exception(inputdict["interface_ip"]+" is not in Cidr:"+aux_cidr)
                else:
                    cidr_name = cust_name + '_' + type4_site_name + '_' + aux_cidr
                    ip_addr = IpamPoolID(sdata.getTaskId(), sdata, cidr_name)
                    ip_addr_obj = ip_addr.ipam_pool_obj
                    used_ip_list = get_used_ip_list_from_ippool(cidr_name, sdata)
                    interface_ip = get_freeip_from_cidr(ip_addr_obj.cidr, used_ip_list)
                    add_ipaddress_entries(ip_addr_obj.name, interface_ip, sdata)
                    inputdict["interface_ip"] = interface_ip
                    return inputdict["interface_ip"],aux_cidr.split("/")[1]

            if util.isNotEmpty(inputdict["profile_name"]) is not None:

                url = "/controller:services/cpedeployment:managed-cpe-services/customer="+cust_name+"/single-cpe-site/single-cpe-site-services="+site_name+"/cpe-lan/lan-profile="+inputdict["profile_name"]
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
def grouping_update_wanop_ic_local_props_type4_wanop_endpoint(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_wanop_ic_local_props_type4_wanop_endpoint(smodelctx, sdata, **kwargs):
    pass
