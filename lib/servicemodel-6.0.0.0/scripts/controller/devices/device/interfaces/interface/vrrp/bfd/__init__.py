
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
class bfd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/interfaces/interface/vrrp/bfd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__bfd_vrrp_id','__local_','__remote','__peer_ip',)

  _yang_name = 'bfd'
  _module_name = 'vrrp'
  _namespace = 'http://anutanetworks.com/vrrp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__remote = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="remote", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='inet:ip-address', is_config=True)
    self.__local_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='uint32', is_config=True)
    self.__bfd_vrrp_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="bfd-vrrp-id", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='string', is_config=True)
    self.__peer_ip = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="peer-ip", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='inet:ip-address', is_config=True)

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
      return [u'devices', u'device', u'interfaces', u'interface', u'vrrp', u'bfd']

  def _get_bfd_vrrp_id(self):
    """
    Getter method for bfd_vrrp_id, mapped from YANG variable /devices/device/interfaces/interface/vrrp/bfd/bfd_vrrp_id (string)

    YANG Description: string
    """
    return self.__bfd_vrrp_id
      
  def _set_bfd_vrrp_id(self, v, load=False):
    """
    Setter method for bfd_vrrp_id, mapped from YANG variable /devices/device/interfaces/interface/vrrp/bfd/bfd_vrrp_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_vrrp_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_vrrp_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="bfd-vrrp-id", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_vrrp_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="bfd-vrrp-id", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='string', is_config=True)""",
        })

    self.__bfd_vrrp_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_vrrp_id(self):
    self.__bfd_vrrp_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="bfd-vrrp-id", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='string', is_config=True)


  def _get_local_(self):
    """
    Getter method for local_, mapped from YANG variable /devices/device/interfaces/interface/vrrp/bfd/local (uint32)

    YANG Description: 0..4294967295
    """
    return self.__local_
      
  def _set_local_(self, v, load=False):
    """
    Setter method for local_, mapped from YANG variable /devices/device/interfaces/interface/vrrp/bfd/local (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='uint32', is_config=True)""",
        })

    self.__local_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_(self):
    self.__local_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='uint32', is_config=True)


  def _get_remote(self):
    """
    Getter method for remote, mapped from YANG variable /devices/device/interfaces/interface/vrrp/bfd/remote (inet:ip-address)

    YANG Description: Valid IPv4/v6 Address (A.B.C.D for e.x: 172.16.1.1 or X::Y for e.x: 2001::1)
    """
    return self.__remote
      
  def _set_remote(self, v, load=False):
    """
    Setter method for remote, mapped from YANG variable /devices/device/interfaces/interface/vrrp/bfd/remote (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote() directly.

    YANG Description: Valid IPv4/v6 Address (A.B.C.D for e.x: 172.16.1.1 or X::Y for e.x: 2001::1)
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="remote", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="remote", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='inet:ip-address', is_config=True)""",
        })

    self.__remote = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote(self):
    self.__remote = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="remote", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='inet:ip-address', is_config=True)


  def _get_peer_ip(self):
    """
    Getter method for peer_ip, mapped from YANG variable /devices/device/interfaces/interface/vrrp/bfd/peer_ip (inet:ip-address)

    YANG Description: Valid IPv4/v6 Address (A.B.C.D for e.x: 172.16.1.1 or X::Y for e.x: 2001::1)
    """
    return self.__peer_ip
      
  def _set_peer_ip(self, v, load=False):
    """
    Setter method for peer_ip, mapped from YANG variable /devices/device/interfaces/interface/vrrp/bfd/peer_ip (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_ip() directly.

    YANG Description: Valid IPv4/v6 Address (A.B.C.D for e.x: 172.16.1.1 or X::Y for e.x: 2001::1)
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="peer-ip", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_ip must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="peer-ip", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='inet:ip-address', is_config=True)""",
        })

    self.__peer_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_ip(self):
    self.__peer_ip = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="peer-ip", module_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vrrp', defining_module='vrrp', yang_type='inet:ip-address', is_config=True)

  bfd_vrrp_id = __builtin__.property(_get_bfd_vrrp_id, _set_bfd_vrrp_id)
  local_ = __builtin__.property(_get_local_, _set_local_)
  remote = __builtin__.property(_get_remote, _set_remote)
  peer_ip = __builtin__.property(_get_peer_ip, _set_peer_ip)


  _pyangbind_elements = collections.OrderedDict([('bfd_vrrp_id', bfd_vrrp_id), ('local_', local_), ('remote', remote), ('peer_ip', peer_ip), ])


