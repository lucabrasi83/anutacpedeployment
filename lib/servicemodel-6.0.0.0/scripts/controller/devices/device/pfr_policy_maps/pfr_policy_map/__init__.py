
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
import pfr_class_entry
class pfr_policy_map(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/pfr-policy-maps/pfr-policy-map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__domain_name','__vrf_name','__pfr_class_entry',)

  _yang_name = 'pfr-policy-map'
  _module_name = 'qos'
  _namespace = 'http://anutanetworks.com/qos'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__pfr_class_entry = YANGDynClass(base=YANGListType("class_name",pfr_class_entry.pfr_class_entry, yang_name="pfr-class-entry", module_name="qos", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='class-name'), is_container='list', yang_name="pfr-class-entry", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='list', is_config=True)
    self.__vrf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='string', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='string', is_config=True)
    self.__domain_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="domain-name", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'pfr-policy-maps', u'pfr-policy-map']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /devices/device/pfr_policy_maps/pfr_policy_map/name (string)

    YANG Description: string
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /devices/device/pfr_policy_maps/pfr_policy_map/name (string)
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
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='string', is_config=True)


  def _get_domain_name(self):
    """
    Getter method for domain_name, mapped from YANG variable /devices/device/pfr_policy_maps/pfr_policy_map/domain_name (string)

    YANG Description: string
    """
    return self.__domain_name
      
  def _set_domain_name(self, v, load=False):
    """
    Setter method for domain_name, mapped from YANG variable /devices/device/pfr_policy_maps/pfr_policy_map/domain_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_domain_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_domain_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="domain-name", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """domain_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="domain-name", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='string', is_config=True)""",
        })

    self.__domain_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_domain_name(self):
    self.__domain_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="domain-name", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='string', is_config=True)


  def _get_vrf_name(self):
    """
    Getter method for vrf_name, mapped from YANG variable /devices/device/pfr_policy_maps/pfr_policy_map/vrf_name (string)

    YANG Description: string
    """
    return self.__vrf_name
      
  def _set_vrf_name(self, v, load=False):
    """
    Setter method for vrf_name, mapped from YANG variable /devices/device/pfr_policy_maps/pfr_policy_map/vrf_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vrf-name", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='string', is_config=True)""",
        })

    self.__vrf_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf_name(self):
    self.__vrf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='string', is_config=True)


  def _get_pfr_class_entry(self):
    """
    Getter method for pfr_class_entry, mapped from YANG variable /devices/device/pfr_policy_maps/pfr_policy_map/pfr_class_entry (list)
    """
    return self.__pfr_class_entry
      
  def _set_pfr_class_entry(self, v, load=False):
    """
    Setter method for pfr_class_entry, mapped from YANG variable /devices/device/pfr_policy_maps/pfr_policy_map/pfr_class_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pfr_class_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pfr_class_entry() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("class_name",pfr_class_entry.pfr_class_entry, yang_name="pfr-class-entry", module_name="qos", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='class-name'), is_container='list', yang_name="pfr-class-entry", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pfr_class_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("class_name",pfr_class_entry.pfr_class_entry, yang_name="pfr-class-entry", module_name="qos", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='class-name'), is_container='list', yang_name="pfr-class-entry", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='list', is_config=True)""",
        })

    self.__pfr_class_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pfr_class_entry(self):
    self.__pfr_class_entry = YANGDynClass(base=YANGListType("class_name",pfr_class_entry.pfr_class_entry, yang_name="pfr-class-entry", module_name="qos", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='class-name'), is_container='list', yang_name="pfr-class-entry", module_name="qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/qos', defining_module='qos', yang_type='list', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  domain_name = __builtin__.property(_get_domain_name, _set_domain_name)
  vrf_name = __builtin__.property(_get_vrf_name, _set_vrf_name)
  pfr_class_entry = __builtin__.property(_get_pfr_class_entry, _set_pfr_class_entry)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('domain_name', domain_name), ('vrf_name', vrf_name), ('pfr_class_entry', pfr_class_entry), ])


