
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
class resource_record(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/resource-records/resource-record. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__zone_name','__domain_name','__ttl','__virtual_ip',)

  _yang_name = 'resource-record'
  _module_name = 'dns'
  _namespace = 'http://anutanetworks.com/dns'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__zone_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="zone-name", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='leafref', is_config=True)
    self.__virtual_ip = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="virtual-ip", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='inet:ip-address', is_config=True)
    self.__domain_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="domain-name", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='string', is_config=True)
    self.__ttl = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ttl", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='uint32', is_config=True)

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
      return [u'devices', u'device', u'resource-records', u'resource-record']

  def _get_zone_name(self):
    """
    Getter method for zone_name, mapped from YANG variable /devices/device/resource_records/resource_record/zone_name (leafref)

    YANG Description: zone-name
    """
    return self.__zone_name
      
  def _set_zone_name(self, v, load=False):
    """
    Setter method for zone_name, mapped from YANG variable /devices/device/resource_records/resource_record/zone_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_zone_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_zone_name() directly.

    YANG Description: zone-name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="zone-name", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """zone_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="zone-name", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='leafref', is_config=True)""",
        })

    self.__zone_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_zone_name(self):
    self.__zone_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="zone-name", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='leafref', is_config=True)


  def _get_domain_name(self):
    """
    Getter method for domain_name, mapped from YANG variable /devices/device/resource_records/resource_record/domain_name (string)

    YANG Description: string
    """
    return self.__domain_name
      
  def _set_domain_name(self, v, load=False):
    """
    Setter method for domain_name, mapped from YANG variable /devices/device/resource_records/resource_record/domain_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_domain_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_domain_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="domain-name", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """domain_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="domain-name", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='string', is_config=True)""",
        })

    self.__domain_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_domain_name(self):
    self.__domain_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="domain-name", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='string', is_config=True)


  def _get_ttl(self):
    """
    Getter method for ttl, mapped from YANG variable /devices/device/resource_records/resource_record/ttl (uint32)

    YANG Description: 0..4294967295
    """
    return self.__ttl
      
  def _set_ttl(self, v, load=False):
    """
    Setter method for ttl, mapped from YANG variable /devices/device/resource_records/resource_record/ttl (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ttl is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ttl() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ttl", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ttl must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ttl", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='uint32', is_config=True)""",
        })

    self.__ttl = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ttl(self):
    self.__ttl = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ttl", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='uint32', is_config=True)


  def _get_virtual_ip(self):
    """
    Getter method for virtual_ip, mapped from YANG variable /devices/device/resource_records/resource_record/virtual_ip (inet:ip-address)

    YANG Description: Valid IPv4/v6 Address (A.B.C.D for e.x: 172.16.1.1 or X::Y for e.x: 2001::1)
    """
    return self.__virtual_ip
      
  def _set_virtual_ip(self, v, load=False):
    """
    Setter method for virtual_ip, mapped from YANG variable /devices/device/resource_records/resource_record/virtual_ip (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_ip() directly.

    YANG Description: Valid IPv4/v6 Address (A.B.C.D for e.x: 172.16.1.1 or X::Y for e.x: 2001::1)
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="virtual-ip", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_ip must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="virtual-ip", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='inet:ip-address', is_config=True)""",
        })

    self.__virtual_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_ip(self):
    self.__virtual_ip = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="virtual-ip", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='inet:ip-address', is_config=True)

  zone_name = __builtin__.property(_get_zone_name, _set_zone_name)
  domain_name = __builtin__.property(_get_domain_name, _set_domain_name)
  ttl = __builtin__.property(_get_ttl, _set_ttl)
  virtual_ip = __builtin__.property(_get_virtual_ip, _set_virtual_ip)


  _pyangbind_elements = collections.OrderedDict([('zone_name', zone_name), ('domain_name', domain_name), ('ttl', ttl), ('virtual_ip', virtual_ip), ])


