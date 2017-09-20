
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import collections
def isEmpty(val):
    """ Check weather val is empty 
    
    Args:
    Val : Value need to check
    Returns:
    True: if the value is empty
    False: if the value is not empty
    """
    if(val == None):
        return True
    if isinstance(val, list):
        return len(val) == 0
    if isinstance(val, str):
        return val.strip() == ''
    if isinstance(val, unicode):
        return str(val).strip() == ''
       
    return False
import events
import actions
class event_manager_applet(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/eem-applets/event-manager-applet. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__applet_name','__events','__actions',)

  _yang_name = 'event-manager-applet'
  _module_name = 'l3features'
  _namespace = 'http://anutanetworks.com/l3features'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__applet_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="applet-name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    self.__actions = YANGDynClass(base=actions.actions, is_container='container', yang_name="actions", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    self.__events = YANGDynClass(base=events.events, is_container='container', yang_name="events", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'devices', u'device', u'eem-applets', u'event-manager-applet']

  def _get_applet_name(self):
    """
    Getter method for applet_name, mapped from YANG variable /devices/device/eem_applets/event_manager_applet/applet_name (string)

    YANG Description: Name of the Event Manager applet
    """
    return self.__applet_name
      
  def _set_applet_name(self, v, load=False):
    """
    Setter method for applet_name, mapped from YANG variable /devices/device/eem_applets/event_manager_applet/applet_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_applet_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_applet_name() directly.

    YANG Description: Name of the Event Manager applet
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="applet-name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """applet_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="applet-name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__applet_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_applet_name(self):
    self.__applet_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="applet-name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)


  def _get_events(self):
    """
    Getter method for events, mapped from YANG variable /devices/device/eem_applets/event_manager_applet/events (container)
    """
    return self.__events
      
  def _set_events(self, v, load=False):
    """
    Setter method for events, mapped from YANG variable /devices/device/eem_applets/event_manager_applet/events (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_events is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_events() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=events.events, is_container='container', yang_name="events", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """events must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=events.events, is_container='container', yang_name="events", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)""",
        })

    self.__events = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_events(self):
    self.__events = YANGDynClass(base=events.events, is_container='container', yang_name="events", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)


  def _get_actions(self):
    """
    Getter method for actions, mapped from YANG variable /devices/device/eem_applets/event_manager_applet/actions (container)
    """
    return self.__actions
      
  def _set_actions(self, v, load=False):
    """
    Setter method for actions, mapped from YANG variable /devices/device/eem_applets/event_manager_applet/actions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_actions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_actions() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=actions.actions, is_container='container', yang_name="actions", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """actions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=actions.actions, is_container='container', yang_name="actions", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)""",
        })

    self.__actions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_actions(self):
    self.__actions = YANGDynClass(base=actions.actions, is_container='container', yang_name="actions", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)

  applet_name = __builtin__.property(_get_applet_name, _set_applet_name)
  events = __builtin__.property(_get_events, _set_events)
  actions = __builtin__.property(_get_actions, _set_actions)


  _pyangbind_elements = collections.OrderedDict([('applet_name', applet_name), ('events', events), ('actions', actions), ])


