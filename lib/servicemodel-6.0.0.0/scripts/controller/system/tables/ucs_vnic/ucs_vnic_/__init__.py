
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
class ucs_vnic(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /system/tables/ucs-vnic/ucs-vnic. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__chassis_pattern','__equipment_dn','__dn','__mac','__switch_id','__chassis','__blade','__vcA','__vcB','__cluster_ip','__fic_ip','__nw_templ_name',)

  _yang_name = 'ucs-vnic'
  _module_name = 'system'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__dn = YANGDynClass(base=unicode, is_leaf=True, yang_name="dn", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__equipment_dn = YANGDynClass(base=unicode, is_leaf=True, yang_name="equipment-dn", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__vcB = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="vcB", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int64', is_config=True)
    self.__fic_ip = YANGDynClass(base=unicode, is_leaf=True, yang_name="fic-ip", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__vcA = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="vcA", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int64', is_config=True)
    self.__chassis_pattern = YANGDynClass(base=unicode, is_leaf=True, yang_name="chassis-pattern", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__blade = YANGDynClass(base=unicode, is_leaf=True, yang_name="blade", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__switch_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="switch-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__chassis = YANGDynClass(base=unicode, is_leaf=True, yang_name="chassis", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__nw_templ_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="nw-templ-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__cluster_ip = YANGDynClass(base=unicode, is_leaf=True, yang_name="cluster-ip", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

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
      return [u'system', u'tables', u'ucs-vnic', u'ucs-vnic']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/name (string)

    YANG Description: string
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/name (string)
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
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_chassis_pattern(self):
    """
    Getter method for chassis_pattern, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/chassis_pattern (string)

    YANG Description: string
    """
    return self.__chassis_pattern
      
  def _set_chassis_pattern(self, v, load=False):
    """
    Setter method for chassis_pattern, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/chassis_pattern (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_chassis_pattern is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_chassis_pattern() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="chassis-pattern", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """chassis_pattern must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="chassis-pattern", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__chassis_pattern = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_chassis_pattern(self):
    self.__chassis_pattern = YANGDynClass(base=unicode, is_leaf=True, yang_name="chassis-pattern", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_equipment_dn(self):
    """
    Getter method for equipment_dn, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/equipment_dn (string)

    YANG Description: string
    """
    return self.__equipment_dn
      
  def _set_equipment_dn(self, v, load=False):
    """
    Setter method for equipment_dn, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/equipment_dn (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_equipment_dn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_equipment_dn() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="equipment-dn", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """equipment_dn must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="equipment-dn", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__equipment_dn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_equipment_dn(self):
    self.__equipment_dn = YANGDynClass(base=unicode, is_leaf=True, yang_name="equipment-dn", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_dn(self):
    """
    Getter method for dn, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/dn (string)

    YANG Description: string
    """
    return self.__dn
      
  def _set_dn(self, v, load=False):
    """
    Setter method for dn, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/dn (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dn() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="dn", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dn must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="dn", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__dn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dn(self):
    self.__dn = YANGDynClass(base=unicode, is_leaf=True, yang_name="dn", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_mac(self):
    """
    Getter method for mac, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/mac (string)

    YANG Description: string
    """
    return self.__mac
      
  def _set_mac(self, v, load=False):
    """
    Setter method for mac, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/mac (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mac", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mac", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac(self):
    self.__mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_switch_id(self):
    """
    Getter method for switch_id, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/switch_id (string)

    YANG Description: string
    """
    return self.__switch_id
      
  def _set_switch_id(self, v, load=False):
    """
    Setter method for switch_id, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/switch_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_switch_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_switch_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="switch-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """switch_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="switch-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__switch_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_switch_id(self):
    self.__switch_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="switch-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_chassis(self):
    """
    Getter method for chassis, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/chassis (string)

    YANG Description: string
    """
    return self.__chassis
      
  def _set_chassis(self, v, load=False):
    """
    Setter method for chassis, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/chassis (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_chassis is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_chassis() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="chassis", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """chassis must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="chassis", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__chassis = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_chassis(self):
    self.__chassis = YANGDynClass(base=unicode, is_leaf=True, yang_name="chassis", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_blade(self):
    """
    Getter method for blade, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/blade (string)

    YANG Description: string
    """
    return self.__blade
      
  def _set_blade(self, v, load=False):
    """
    Setter method for blade, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/blade (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_blade is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_blade() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="blade", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """blade must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="blade", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__blade = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_blade(self):
    self.__blade = YANGDynClass(base=unicode, is_leaf=True, yang_name="blade", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_vcA(self):
    """
    Getter method for vcA, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/vcA (int64)

    YANG Description: -9223372036854775808..9223372036854775807
    """
    return self.__vcA
      
  def _set_vcA(self, v, load=False):
    """
    Setter method for vcA, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/vcA (int64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vcA is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vcA() directly.

    YANG Description: -9223372036854775808..9223372036854775807
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="vcA", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vcA must be of a type compatible with int64""",
          'defined-type': "int64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="vcA", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int64', is_config=True)""",
        })

    self.__vcA = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vcA(self):
    self.__vcA = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="vcA", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int64', is_config=True)


  def _get_vcB(self):
    """
    Getter method for vcB, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/vcB (int64)

    YANG Description: -9223372036854775808..9223372036854775807
    """
    return self.__vcB
      
  def _set_vcB(self, v, load=False):
    """
    Setter method for vcB, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/vcB (int64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vcB is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vcB() directly.

    YANG Description: -9223372036854775808..9223372036854775807
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="vcB", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vcB must be of a type compatible with int64""",
          'defined-type': "int64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="vcB", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int64', is_config=True)""",
        })

    self.__vcB = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vcB(self):
    self.__vcB = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="vcB", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int64', is_config=True)


  def _get_cluster_ip(self):
    """
    Getter method for cluster_ip, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/cluster_ip (string)

    YANG Description: string
    """
    return self.__cluster_ip
      
  def _set_cluster_ip(self, v, load=False):
    """
    Setter method for cluster_ip, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/cluster_ip (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cluster_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cluster_ip() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="cluster-ip", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cluster_ip must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="cluster-ip", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__cluster_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cluster_ip(self):
    self.__cluster_ip = YANGDynClass(base=unicode, is_leaf=True, yang_name="cluster-ip", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_fic_ip(self):
    """
    Getter method for fic_ip, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/fic_ip (string)

    YANG Description: string
    """
    return self.__fic_ip
      
  def _set_fic_ip(self, v, load=False):
    """
    Setter method for fic_ip, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/fic_ip (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fic_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fic_ip() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="fic-ip", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fic_ip must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="fic-ip", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__fic_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fic_ip(self):
    self.__fic_ip = YANGDynClass(base=unicode, is_leaf=True, yang_name="fic-ip", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_nw_templ_name(self):
    """
    Getter method for nw_templ_name, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/nw_templ_name (string)

    YANG Description: string
    """
    return self.__nw_templ_name
      
  def _set_nw_templ_name(self, v, load=False):
    """
    Setter method for nw_templ_name, mapped from YANG variable /system/tables/ucs_vnic/ucs_vnic/nw_templ_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nw_templ_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nw_templ_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="nw-templ-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nw_templ_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="nw-templ-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__nw_templ_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nw_templ_name(self):
    self.__nw_templ_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="nw-templ-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  chassis_pattern = __builtin__.property(_get_chassis_pattern, _set_chassis_pattern)
  equipment_dn = __builtin__.property(_get_equipment_dn, _set_equipment_dn)
  dn = __builtin__.property(_get_dn, _set_dn)
  mac = __builtin__.property(_get_mac, _set_mac)
  switch_id = __builtin__.property(_get_switch_id, _set_switch_id)
  chassis = __builtin__.property(_get_chassis, _set_chassis)
  blade = __builtin__.property(_get_blade, _set_blade)
  vcA = __builtin__.property(_get_vcA, _set_vcA)
  vcB = __builtin__.property(_get_vcB, _set_vcB)
  cluster_ip = __builtin__.property(_get_cluster_ip, _set_cluster_ip)
  fic_ip = __builtin__.property(_get_fic_ip, _set_fic_ip)
  nw_templ_name = __builtin__.property(_get_nw_templ_name, _set_nw_templ_name)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('chassis_pattern', chassis_pattern), ('equipment_dn', equipment_dn), ('dn', dn), ('mac', mac), ('switch_id', switch_id), ('chassis', chassis), ('blade', blade), ('vcA', vcA), ('vcB', vcB), ('cluster_ip', cluster_ip), ('fic_ip', fic_ip), ('nw_templ_name', nw_templ_name), ])


