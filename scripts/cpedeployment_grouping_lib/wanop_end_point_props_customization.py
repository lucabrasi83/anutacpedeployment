
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
def grouping_create_wanop_end_point_props_(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_wanop_end_point_props_(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_wanop_end_point_props_(smodelctx, sdata, **kwargs):
    pass
