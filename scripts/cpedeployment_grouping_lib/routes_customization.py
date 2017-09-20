
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
     dest-ip-address            maps-to  /ac:devices/ac:device/wanop-device:routes/route/dest-ip-address
           dest-mask            maps-to  /ac:devices/ac:device/wanop-device:routes/route/dest-mask

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_routes_route(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_routes_route(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_routes_route(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
                  id            maps-to  /ac:devices/ac:device/wanop-device:routes/route/options/id
         next-hop-ip            maps-to  /ac:devices/ac:device/wanop-device:routes/route/options/next-hop-ip
      interface-name            maps-to  /ac:devices/ac:device/wanop-device:routes/route/options/interface-name

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_routes_route_options(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_routes_route_options(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_routes_route_options(smodelctx, sdata, **kwargs):
    pass
