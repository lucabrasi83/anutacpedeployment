
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
         applet-name            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/applet-name

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_applet_event_manager_applet(smodelctx, sdata, dev, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_applet_event_manager_applet(smodelctx, sdata, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_applet_event_manager_applet(smodelctx, sdata, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Names of Leafs for this Yang Entity

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_applet_event_manager_applet_events(smodelctx, sdata, dev, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_applet_event_manager_applet_events(smodelctx, sdata, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_applet_event_manager_applet_events(smodelctx, sdata, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Names of Leafs for this Yang Entity
          tag-number            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/events/tag/tag-number
      interface-name            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/events/tag/interface-name
           parameter            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/events/tag/parameter
       entry-compare            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/events/tag/entry-compare
   entry-counter-val            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/events/tag/entry-counter-val
       poll-interval            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/events/tag/poll-interval

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_applet_event_manager_applet_events_tag(smodelctx, sdata, dev, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_applet_event_manager_applet_events_tag(smodelctx, sdata, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_applet_event_manager_applet_events_tag(smodelctx, sdata, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Names of Leafs for this Yang Entity

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_applet_event_manager_applet_actions(smodelctx, sdata, dev, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_applet_event_manager_applet_actions(smodelctx, sdata, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_applet_event_manager_applet_actions(smodelctx, sdata, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Names of Leafs for this Yang Entity
               label            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/label
    action-statement            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/action-statement
            cli-type            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/cli-type
          cli-string            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/cli-string
       regex-pattern            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/regex-pattern
        input-string            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/input-string
     syslog-priority            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/syslog-priority
          syslog-msg            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/syslog-msg
       first-operand            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/first-operand
             compare            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/compare
      second-operand            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/second-operand
         exit-result            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/exit-result
      comment-string            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/comment-string
   handle-error-type            maps-to  /ac:devices/ac:device/l3:eem-applets/event-manager-applet/actions/action/handle-error-type

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_applet_event_manager_applet_actions_action(smodelctx, sdata, dev, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_applet_event_manager_applet_actions_action(smodelctx, sdata, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_applet_event_manager_applet_actions_action(smodelctx, sdata, **kwargs):
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/events/tag':
      pass
    if kwargs.get('xpath') is not None and kwargs['xpath'] == 'managed-cpe-services/customer/eem-applets/event-manager-applet/actions/action':
      pass

    pass
