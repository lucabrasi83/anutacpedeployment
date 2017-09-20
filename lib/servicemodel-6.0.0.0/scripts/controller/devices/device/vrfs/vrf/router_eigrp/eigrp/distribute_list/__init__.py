
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
class distribute_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/vrfs/vrf/router-eigrp/eigrp/distribute-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__filter','__interface','__route_map',)

  _yang_name = 'distribute-list'
  _module_name = 'l3features'
  _namespace = 'http://anutanetworks.com/l3features'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__filter = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'out': {}, u'in': {}},), is_leaf=True, yang_name="filter", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)
    self.__interface = YANGDynClass(base=[unicode,unicode,], is_leaf=True, yang_name="interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='union', is_config=True)
    self.__route_map = YANGDynClass(base=unicode, is_leaf=True, yang_name="route-map", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'vrfs', u'vrf', u'router-eigrp', u'eigrp', u'distribute-list']

  def _get_filter(self):
    """
    Getter method for filter, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/eigrp/distribute_list/filter (enumeration)

    YANG Description: in
out

    """
    return self.__filter
      
  def _set_filter(self, v, load=False):
    """
    Setter method for filter, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/eigrp/distribute_list/filter (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filter() directly.

    YANG Description: in
out

    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'out': {}, u'in': {}},), is_leaf=True, yang_name="filter", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filter must be of a type compatible with enumeration""",
          'defined-type': "l3features:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'out': {}, u'in': {}},), is_leaf=True, yang_name="filter", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)""",
        })

    self.__filter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filter(self):
    self.__filter = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'out': {}, u'in': {}},), is_leaf=True, yang_name="filter", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/eigrp/distribute_list/interface (union)

    YANG Description: Union Input types:
leafref
string

    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/eigrp/distribute_list/interface (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Union Input types:
leafref
string

    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=[unicode,unicode,], is_leaf=True, yang_name="interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with union""",
          'defined-type': "l3features:union",
          'generated-type': """YANGDynClass(base=[unicode,unicode,], is_leaf=True, yang_name="interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='union', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=[unicode,unicode,], is_leaf=True, yang_name="interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='union', is_config=True)


  def _get_route_map(self):
    """
    Getter method for route_map, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/eigrp/distribute_list/route_map (string)

    YANG Description: string
    """
    return self.__route_map
      
  def _set_route_map(self, v, load=False):
    """
    Setter method for route_map, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/eigrp/distribute_list/route_map (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_map() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="route-map", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_map must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="route-map", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_map(self):
    self.__route_map = YANGDynClass(base=unicode, is_leaf=True, yang_name="route-map", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)

  filter = __builtin__.property(_get_filter, _set_filter)
  interface = __builtin__.property(_get_interface, _set_interface)
  route_map = __builtin__.property(_get_route_map, _set_route_map)


  _pyangbind_elements = collections.OrderedDict([('filter', filter), ('interface', interface), ('route_map', route_map), ])


