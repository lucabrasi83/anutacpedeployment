
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
class address(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/interfaces/interface/hsrp/additional-ipv6-address/address. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__ip','__prefix_length','__family','__mtu','__acl_inbound_name','__acl_outbound_name','__source_ip','__destination_ip','__destination_vrf','__allow_fragmentation',)

  _yang_name = 'address'
  _module_name = 'hsrp'
  _namespace = 'http://anutanetworks.com/hsrp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__destination_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destination-ip", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='inet:ipv6-address', is_config=True)
    self.__family = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'inet6': {}, u'inet': {}},), is_leaf=True, yang_name="family", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='family-type', is_config=True)
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='inet:ipv6-address', is_config=True)
    self.__acl_outbound_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="acl-outbound-name", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='string', is_config=True)
    self.__source_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source-ip", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='inet:ipv6-address', is_config=True)
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mtu", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='uint32', is_config=True)
    self.__destination_vrf = YANGDynClass(base=unicode, is_leaf=True, yang_name="destination-vrf", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='string', is_config=True)
    self.__allow_fragmentation = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="allow-fragmentation", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='boolean', is_config=True)
    self.__prefix_length = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..128']}), is_leaf=True, yang_name="prefix-length", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='nt:ipv6-prefix-length', is_config=True)
    self.__acl_inbound_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="acl-inbound-name", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'interfaces', u'interface', u'hsrp', u'additional-ipv6-address', u'address']

  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/ip (inet:ipv6-address)

    YANG Description: Valid IPv6 Address (X::Y for e.x: 2001::1)
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/ip (inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: Valid IPv6 Address (X::Y for e.x: 2001::1)
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='inet:ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with inet:ipv6-address""",
          'defined-type': "inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='inet:ipv6-address', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='inet:ipv6-address', is_config=True)


  def _get_prefix_length(self):
    """
    Getter method for prefix_length, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/prefix_length (nt:ipv6-prefix-length)

    YANG Description: IPv6 prefix length in CIDR notation.
    """
    return self.__prefix_length
      
  def _set_prefix_length(self, v, load=False):
    """
    Setter method for prefix_length, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/prefix_length (nt:ipv6-prefix-length)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_length is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_length() directly.

    YANG Description: IPv6 prefix length in CIDR notation.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..128']}), is_leaf=True, yang_name="prefix-length", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='nt:ipv6-prefix-length', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_length must be of a type compatible with nt:ipv6-prefix-length""",
          'defined-type': "nt:ipv6-prefix-length",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..128']}), is_leaf=True, yang_name="prefix-length", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='nt:ipv6-prefix-length', is_config=True)""",
        })

    self.__prefix_length = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_length(self):
    self.__prefix_length = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..128']}), is_leaf=True, yang_name="prefix-length", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='nt:ipv6-prefix-length', is_config=True)


  def _get_family(self):
    """
    Getter method for family, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/family (family-type)

    YANG Description: inet
inet6

    """
    return self.__family
      
  def _set_family(self, v, load=False):
    """
    Setter method for family, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/family (family-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_family is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_family() directly.

    YANG Description: inet
inet6

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'inet6': {}, u'inet': {}},), is_leaf=True, yang_name="family", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='family-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """family must be of a type compatible with family-type""",
          'defined-type': "hsrp:family-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'inet6': {}, u'inet': {}},), is_leaf=True, yang_name="family", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='family-type', is_config=True)""",
        })

    self.__family = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_family(self):
    self.__family = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'inet6': {}, u'inet': {}},), is_leaf=True, yang_name="family", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='family-type', is_config=True)


  def _get_mtu(self):
    """
    Getter method for mtu, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/mtu (uint32)

    YANG Description: 0..4294967295
    """
    return self.__mtu
      
  def _set_mtu(self, v, load=False):
    """
    Setter method for mtu, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/mtu (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mtu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mtu() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mtu", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mtu must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mtu", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='uint32', is_config=True)""",
        })

    self.__mtu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mtu(self):
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mtu", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='uint32', is_config=True)


  def _get_acl_inbound_name(self):
    """
    Getter method for acl_inbound_name, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/acl_inbound_name (string)

    YANG Description: string
    """
    return self.__acl_inbound_name
      
  def _set_acl_inbound_name(self, v, load=False):
    """
    Setter method for acl_inbound_name, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/acl_inbound_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_acl_inbound_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_acl_inbound_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="acl-inbound-name", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """acl_inbound_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="acl-inbound-name", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='string', is_config=True)""",
        })

    self.__acl_inbound_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_acl_inbound_name(self):
    self.__acl_inbound_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="acl-inbound-name", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='string', is_config=True)


  def _get_acl_outbound_name(self):
    """
    Getter method for acl_outbound_name, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/acl_outbound_name (string)

    YANG Description: string
    """
    return self.__acl_outbound_name
      
  def _set_acl_outbound_name(self, v, load=False):
    """
    Setter method for acl_outbound_name, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/acl_outbound_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_acl_outbound_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_acl_outbound_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="acl-outbound-name", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """acl_outbound_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="acl-outbound-name", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='string', is_config=True)""",
        })

    self.__acl_outbound_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_acl_outbound_name(self):
    self.__acl_outbound_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="acl-outbound-name", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='string', is_config=True)


  def _get_source_ip(self):
    """
    Getter method for source_ip, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/source_ip (inet:ipv6-address)

    YANG Description: Valid IPv6 Address (X::Y for e.x: 2001::1)
    """
    return self.__source_ip
      
  def _set_source_ip(self, v, load=False):
    """
    Setter method for source_ip, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/source_ip (inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_ip() directly.

    YANG Description: Valid IPv6 Address (X::Y for e.x: 2001::1)
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source-ip", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='inet:ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_ip must be of a type compatible with inet:ipv6-address""",
          'defined-type': "inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source-ip", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='inet:ipv6-address', is_config=True)""",
        })

    self.__source_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_ip(self):
    self.__source_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source-ip", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='inet:ipv6-address', is_config=True)


  def _get_destination_ip(self):
    """
    Getter method for destination_ip, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/destination_ip (inet:ipv6-address)

    YANG Description: Valid IPv6 Address (X::Y for e.x: 2001::1)
    """
    return self.__destination_ip
      
  def _set_destination_ip(self, v, load=False):
    """
    Setter method for destination_ip, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/destination_ip (inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination_ip() directly.

    YANG Description: Valid IPv6 Address (X::Y for e.x: 2001::1)
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destination-ip", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='inet:ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination_ip must be of a type compatible with inet:ipv6-address""",
          'defined-type': "inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destination-ip", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='inet:ipv6-address', is_config=True)""",
        })

    self.__destination_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination_ip(self):
    self.__destination_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destination-ip", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='inet:ipv6-address', is_config=True)


  def _get_destination_vrf(self):
    """
    Getter method for destination_vrf, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/destination_vrf (string)

    YANG Description: string
    """
    return self.__destination_vrf
      
  def _set_destination_vrf(self, v, load=False):
    """
    Setter method for destination_vrf, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/destination_vrf (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination_vrf() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="destination-vrf", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination_vrf must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="destination-vrf", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='string', is_config=True)""",
        })

    self.__destination_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination_vrf(self):
    self.__destination_vrf = YANGDynClass(base=unicode, is_leaf=True, yang_name="destination-vrf", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='string', is_config=True)


  def _get_allow_fragmentation(self):
    """
    Getter method for allow_fragmentation, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/allow_fragmentation (boolean)

    YANG Description: allow-fragmentation: True/False
    """
    return self.__allow_fragmentation
      
  def _set_allow_fragmentation(self, v, load=False):
    """
    Setter method for allow_fragmentation, mapped from YANG variable /devices/device/interfaces/interface/hsrp/additional_ipv6_address/address/allow_fragmentation (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allow_fragmentation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allow_fragmentation() directly.

    YANG Description: allow-fragmentation: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="allow-fragmentation", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allow_fragmentation must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="allow-fragmentation", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='boolean', is_config=True)""",
        })

    self.__allow_fragmentation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allow_fragmentation(self):
    self.__allow_fragmentation = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="allow-fragmentation", module_name="hsrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/hsrp', defining_module='hsrp', yang_type='boolean', is_config=True)

  ip = __builtin__.property(_get_ip, _set_ip)
  prefix_length = __builtin__.property(_get_prefix_length, _set_prefix_length)
  family = __builtin__.property(_get_family, _set_family)
  mtu = __builtin__.property(_get_mtu, _set_mtu)
  acl_inbound_name = __builtin__.property(_get_acl_inbound_name, _set_acl_inbound_name)
  acl_outbound_name = __builtin__.property(_get_acl_outbound_name, _set_acl_outbound_name)
  source_ip = __builtin__.property(_get_source_ip, _set_source_ip)
  destination_ip = __builtin__.property(_get_destination_ip, _set_destination_ip)
  destination_vrf = __builtin__.property(_get_destination_vrf, _set_destination_vrf)
  allow_fragmentation = __builtin__.property(_get_allow_fragmentation, _set_allow_fragmentation)


  _pyangbind_elements = collections.OrderedDict([('ip', ip), ('prefix_length', prefix_length), ('family', family), ('mtu', mtu), ('acl_inbound_name', acl_inbound_name), ('acl_outbound_name', acl_outbound_name), ('source_ip', source_ip), ('destination_ip', destination_ip), ('destination_vrf', destination_vrf), ('allow_fragmentation', allow_fragmentation), ])


