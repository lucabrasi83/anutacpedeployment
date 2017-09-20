
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
class pool(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/ip-nat/address-translation/pool. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__pool_name','__redundancy_id','__mapping_id','__vrf','__overload','__oer','__match_in_vrf','__extended','__add_route',)

  _yang_name = 'pool'
  _module_name = 'l3features'
  _namespace = 'http://anutanetworks.com/l3features'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__pool_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="pool-name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    self.__extended = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="extended", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    self.__redundancy_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="redundancy-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint8', is_config=True)
    self.__oer = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="oer", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    self.__add_route = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="add-route", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    self.__overload = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="overload", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    self.__mapping_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mapping-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint32', is_config=True)
    self.__match_in_vrf = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="match-in-vrf", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    self.__vrf = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'ip-nat', u'address-translation', u'pool']

  def _get_pool_name(self):
    """
    Getter method for pool_name, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/pool_name (string)

    YANG Description: string
    """
    return self.__pool_name
      
  def _set_pool_name(self, v, load=False):
    """
    Setter method for pool_name, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/pool_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pool_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pool_name() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="pool-name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pool_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="pool-name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__pool_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pool_name(self):
    self.__pool_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="pool-name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)


  def _get_redundancy_id(self):
    """
    Getter method for redundancy_id, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/redundancy_id (uint8)

    YANG Description: 0..255
    """
    return self.__redundancy_id
      
  def _set_redundancy_id(self, v, load=False):
    """
    Setter method for redundancy_id, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/redundancy_id (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redundancy_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redundancy_id() directly.

    YANG Description: 0..255
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="redundancy-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redundancy_id must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="redundancy-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint8', is_config=True)""",
        })

    self.__redundancy_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redundancy_id(self):
    self.__redundancy_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="redundancy-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint8', is_config=True)


  def _get_mapping_id(self):
    """
    Getter method for mapping_id, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/mapping_id (uint32)

    YANG Description: 0..4294967295
    """
    return self.__mapping_id
      
  def _set_mapping_id(self, v, load=False):
    """
    Setter method for mapping_id, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/mapping_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mapping_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mapping_id() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mapping-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mapping_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mapping-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint32', is_config=True)""",
        })

    self.__mapping_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mapping_id(self):
    self.__mapping_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mapping-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint32', is_config=True)


  def _get_vrf(self):
    """
    Getter method for vrf, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/vrf (string)

    YANG Description: string
    """
    return self.__vrf
      
  def _set_vrf(self, v, load=False):
    """
    Setter method for vrf, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/vrf (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vrf", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf(self):
    self.__vrf = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)


  def _get_overload(self):
    """
    Getter method for overload, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/overload (boolean)

    YANG Description: overload: True/False
    """
    return self.__overload
      
  def _set_overload(self, v, load=False):
    """
    Setter method for overload, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/overload (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_overload is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_overload() directly.

    YANG Description: overload: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="overload", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """overload must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="overload", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)""",
        })

    self.__overload = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_overload(self):
    self.__overload = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="overload", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)


  def _get_oer(self):
    """
    Getter method for oer, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/oer (boolean)

    YANG Description: oer: True/False
    """
    return self.__oer
      
  def _set_oer(self, v, load=False):
    """
    Setter method for oer, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/oer (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oer() directly.

    YANG Description: oer: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="oer", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oer must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="oer", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)""",
        })

    self.__oer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oer(self):
    self.__oer = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="oer", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)


  def _get_match_in_vrf(self):
    """
    Getter method for match_in_vrf, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/match_in_vrf (boolean)

    YANG Description: match-in-vrf: True/False
    """
    return self.__match_in_vrf
      
  def _set_match_in_vrf(self, v, load=False):
    """
    Setter method for match_in_vrf, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/match_in_vrf (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match_in_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match_in_vrf() directly.

    YANG Description: match-in-vrf: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="match-in-vrf", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match_in_vrf must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="match-in-vrf", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)""",
        })

    self.__match_in_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match_in_vrf(self):
    self.__match_in_vrf = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="match-in-vrf", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)


  def _get_extended(self):
    """
    Getter method for extended, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/extended (boolean)

    YANG Description: extended: True/False
    """
    return self.__extended
      
  def _set_extended(self, v, load=False):
    """
    Setter method for extended, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/extended (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extended is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extended() directly.

    YANG Description: extended: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="extended", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extended must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="extended", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)""",
        })

    self.__extended = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extended(self):
    self.__extended = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="extended", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)


  def _get_add_route(self):
    """
    Getter method for add_route, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/add_route (boolean)

    YANG Description: add-route: True/False
    """
    return self.__add_route
      
  def _set_add_route(self, v, load=False):
    """
    Setter method for add_route, mapped from YANG variable /devices/device/ip_nat/address_translation/pool/add_route (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_add_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_add_route() directly.

    YANG Description: add-route: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="add-route", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """add_route must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="add-route", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)""",
        })

    self.__add_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_add_route(self):
    self.__add_route = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="add-route", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)

  pool_name = __builtin__.property(_get_pool_name, _set_pool_name)
  redundancy_id = __builtin__.property(_get_redundancy_id, _set_redundancy_id)
  mapping_id = __builtin__.property(_get_mapping_id, _set_mapping_id)
  vrf = __builtin__.property(_get_vrf, _set_vrf)
  overload = __builtin__.property(_get_overload, _set_overload)
  oer = __builtin__.property(_get_oer, _set_oer)
  match_in_vrf = __builtin__.property(_get_match_in_vrf, _set_match_in_vrf)
  extended = __builtin__.property(_get_extended, _set_extended)
  add_route = __builtin__.property(_get_add_route, _set_add_route)


  _pyangbind_elements = collections.OrderedDict([('pool_name', pool_name), ('redundancy_id', redundancy_id), ('mapping_id', mapping_id), ('vrf', vrf), ('overload', overload), ('oer', oer), ('match_in_vrf', match_in_vrf), ('extended', extended), ('add_route', add_route), ])


