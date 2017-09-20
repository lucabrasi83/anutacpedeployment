
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
class correlate(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/eem-applets/event-manager-applet/trigger/correlate. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__event1','__logic','__event2',)

  _yang_name = 'correlate'
  _module_name = 'l3features'
  _namespace = 'http://anutanetworks.com/l3features'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__logic = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'and': {}, u'andnot': {}, u'or': {}},), is_leaf=True, yang_name="logic", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)
    self.__event2 = YANGDynClass(base=unicode, is_leaf=True, yang_name="event2", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    self.__event1 = YANGDynClass(base=unicode, is_leaf=True, yang_name="event1", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'eem-applets', u'event-manager-applet', u'trigger', u'correlate']

  def _get_event1(self):
    """
    Getter method for event1, mapped from YANG variable /devices/device/eem_applets/event_manager_applet/trigger/correlate/event1 (string)

    YANG Description: event tag value
    """
    return self.__event1
      
  def _set_event1(self, v, load=False):
    """
    Setter method for event1, mapped from YANG variable /devices/device/eem_applets/event_manager_applet/trigger/correlate/event1 (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_event1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_event1() directly.

    YANG Description: event tag value
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="event1", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """event1 must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="event1", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__event1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_event1(self):
    self.__event1 = YANGDynClass(base=unicode, is_leaf=True, yang_name="event1", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)


  def _get_logic(self):
    """
    Getter method for logic, mapped from YANG variable /devices/device/eem_applets/event_manager_applet/trigger/correlate/logic (enumeration)

    YANG Description: and
andnot
or

    """
    return self.__logic
      
  def _set_logic(self, v, load=False):
    """
    Setter method for logic, mapped from YANG variable /devices/device/eem_applets/event_manager_applet/trigger/correlate/logic (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logic is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logic() directly.

    YANG Description: and
andnot
or

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'and': {}, u'andnot': {}, u'or': {}},), is_leaf=True, yang_name="logic", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logic must be of a type compatible with enumeration""",
          'defined-type': "l3features:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'and': {}, u'andnot': {}, u'or': {}},), is_leaf=True, yang_name="logic", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)""",
        })

    self.__logic = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logic(self):
    self.__logic = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'and': {}, u'andnot': {}, u'or': {}},), is_leaf=True, yang_name="logic", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)


  def _get_event2(self):
    """
    Getter method for event2, mapped from YANG variable /devices/device/eem_applets/event_manager_applet/trigger/correlate/event2 (string)

    YANG Description: event tag value
    """
    return self.__event2
      
  def _set_event2(self, v, load=False):
    """
    Setter method for event2, mapped from YANG variable /devices/device/eem_applets/event_manager_applet/trigger/correlate/event2 (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_event2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_event2() directly.

    YANG Description: event tag value
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="event2", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """event2 must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="event2", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__event2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_event2(self):
    self.__event2 = YANGDynClass(base=unicode, is_leaf=True, yang_name="event2", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)

  event1 = __builtin__.property(_get_event1, _set_event1)
  logic = __builtin__.property(_get_logic, _set_logic)
  event2 = __builtin__.property(_get_event2, _set_event2)


  _pyangbind_elements = collections.OrderedDict([('event1', event1), ('logic', logic), ('event2', event2), ])


