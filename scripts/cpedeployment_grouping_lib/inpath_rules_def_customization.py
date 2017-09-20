
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
           rule-type            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/rule-type
     packet-mode-uni            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/packet-mode-uni
             srcaddr            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/srcaddr
             srcport            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/srcport
             dstaddr            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/dstaddr
             dstport            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/dstport
          dst-domain            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/dst-domain
            dst-host            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/dst-host
        optimization            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/optimization
     preoptimization            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/preoptimization
         latency-opt            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/latency-opt
                vlan            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/vlan
         neural-mode            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/neural-mode
         cloud-accel            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/cloud-accel
           web-proxy            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/web-proxy
      wan-visibility            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/wan-visibility
         description            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/description
        auto-kickoff            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/auto-kickoff
         rule-enable            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/rule-enable
             rulenum            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/rulenum
            protocol            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/protocol
         target-addr            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/target-addr
         target-port            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/target-port
         backup-addr            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/backup-addr
         backup-port            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/inpath-rules-def/backup-port

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API
"""
def grouping_create_inpath_rules_def_inpath_rules(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API
"""
def grouping_update_inpath_rules_def_inpath_rules(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API
"""
def grouping_delete_inpath_rules_def_inpath_rules(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
       from-rule-num            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/move-rule/from-rule-num
         to-rule-num            maps-to  /ac:devices/ac:device/wanop-device:inpath-rules/move-rule/to-rule-num

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API
"""
def grouping_create_inpath_rules_def_move_rule(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API
"""
def grouping_update_inpath_rules_def_move_rule(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API
"""
def grouping_delete_inpath_rules_def_move_rule(smodelctx, sdata, **kwargs):
    pass