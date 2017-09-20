
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
import route_policy_entries
class route_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/route-policies/route-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__cpl_string','__skip_cpl_string','__route_policy_entries',)

  _yang_name = 'route-policy'
  _module_name = 'l3features'
  _namespace = 'http://anutanetworks.com/l3features'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__route_policy_entries = YANGDynClass(base=YANGListType("med",route_policy_entries.route_policy_entries, yang_name="route-policy-entries", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='med'), is_container='list', yang_name="route-policy-entries", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)
    self.__skip_cpl_string = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="skip-cpl-string", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    self.__cpl_string = YANGDynClass(base=unicode, is_leaf=True, yang_name="cpl-string", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'route-policies', u'route-policy']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /devices/device/route_policies/route_policy/name (string)

    YANG Description: string
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /devices/device/route_policies/route_policy/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)


  def _get_cpl_string(self):
    """
    Getter method for cpl_string, mapped from YANG variable /devices/device/route_policies/route_policy/cpl_string (string)

    YANG Description: string
    """
    return self.__cpl_string
      
  def _set_cpl_string(self, v, load=False):
    """
    Setter method for cpl_string, mapped from YANG variable /devices/device/route_policies/route_policy/cpl_string (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cpl_string is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cpl_string() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="cpl-string", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cpl_string must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="cpl-string", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__cpl_string = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cpl_string(self):
    self.__cpl_string = YANGDynClass(base=unicode, is_leaf=True, yang_name="cpl-string", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)


  def _get_skip_cpl_string(self):
    """
    Getter method for skip_cpl_string, mapped from YANG variable /devices/device/route_policies/route_policy/skip_cpl_string (boolean)

    YANG Description: skip-cpl-string: True/False
    """
    return self.__skip_cpl_string
      
  def _set_skip_cpl_string(self, v, load=False):
    """
    Setter method for skip_cpl_string, mapped from YANG variable /devices/device/route_policies/route_policy/skip_cpl_string (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_skip_cpl_string is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_skip_cpl_string() directly.

    YANG Description: skip-cpl-string: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="skip-cpl-string", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """skip_cpl_string must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="skip-cpl-string", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)""",
        })

    self.__skip_cpl_string = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_skip_cpl_string(self):
    self.__skip_cpl_string = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="skip-cpl-string", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)


  def _get_route_policy_entries(self):
    """
    Getter method for route_policy_entries, mapped from YANG variable /devices/device/route_policies/route_policy/route_policy_entries (list)
    """
    return self.__route_policy_entries
      
  def _set_route_policy_entries(self, v, load=False):
    """
    Setter method for route_policy_entries, mapped from YANG variable /devices/device/route_policies/route_policy/route_policy_entries (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_policy_entries is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_policy_entries() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("med",route_policy_entries.route_policy_entries, yang_name="route-policy-entries", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='med'), is_container='list', yang_name="route-policy-entries", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_policy_entries must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("med",route_policy_entries.route_policy_entries, yang_name="route-policy-entries", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='med'), is_container='list', yang_name="route-policy-entries", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)""",
        })

    self.__route_policy_entries = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_policy_entries(self):
    self.__route_policy_entries = YANGDynClass(base=YANGListType("med",route_policy_entries.route_policy_entries, yang_name="route-policy-entries", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='med'), is_container='list', yang_name="route-policy-entries", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  cpl_string = __builtin__.property(_get_cpl_string, _set_cpl_string)
  skip_cpl_string = __builtin__.property(_get_skip_cpl_string, _set_skip_cpl_string)
  route_policy_entries = __builtin__.property(_get_route_policy_entries, _set_route_policy_entries)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('cpl_string', cpl_string), ('skip_cpl_string', skip_cpl_string), ('route_policy_entries', route_policy_entries), ])


