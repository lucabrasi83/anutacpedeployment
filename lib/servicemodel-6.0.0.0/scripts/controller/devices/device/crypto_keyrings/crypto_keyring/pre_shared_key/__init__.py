
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
class pre_shared_key(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/crypto-keyrings/crypto-keyring/pre-shared-key. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__ip_address','__netmask','__pre_shared_secret',)

  _yang_name = 'pre-shared-key'
  _module_name = 'dmvpn'
  _namespace = 'http://anutanetworks.com/dmvpn'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__netmask = YANGDynClass(base=unicode, is_leaf=True, yang_name="netmask", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)
    self.__ip_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="ip-address", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='inet:ip-address', is_config=True)
    self.__pre_shared_secret = YANGDynClass(base=unicode, is_leaf=True, yang_name="pre-shared-secret", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'crypto-keyrings', u'crypto-keyring', u'pre-shared-key']

  def _get_ip_address(self):
    """
    Getter method for ip_address, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/pre_shared_key/ip_address (inet:ip-address)

    YANG Description: Valid IPv4/v6 Address (A.B.C.D for e.x: 172.16.1.1 or X::Y for e.x: 2001::1)
    """
    return self.__ip_address
      
  def _set_ip_address(self, v, load=False):
    """
    Setter method for ip_address, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/pre_shared_key/ip_address (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_address() directly.

    YANG Description: Valid IPv4/v6 Address (A.B.C.D for e.x: 172.16.1.1 or X::Y for e.x: 2001::1)
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="ip-address", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_address must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="ip-address", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='inet:ip-address', is_config=True)""",
        })

    self.__ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_address(self):
    self.__ip_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="ip-address", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='inet:ip-address', is_config=True)


  def _get_netmask(self):
    """
    Getter method for netmask, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/pre_shared_key/netmask (string)

    YANG Description: string
    """
    return self.__netmask
      
  def _set_netmask(self, v, load=False):
    """
    Setter method for netmask, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/pre_shared_key/netmask (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_netmask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_netmask() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="netmask", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """netmask must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="netmask", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)""",
        })

    self.__netmask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_netmask(self):
    self.__netmask = YANGDynClass(base=unicode, is_leaf=True, yang_name="netmask", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)


  def _get_pre_shared_secret(self):
    """
    Getter method for pre_shared_secret, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/pre_shared_key/pre_shared_secret (string)

    YANG Description: string
    """
    return self.__pre_shared_secret
      
  def _set_pre_shared_secret(self, v, load=False):
    """
    Setter method for pre_shared_secret, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/pre_shared_key/pre_shared_secret (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pre_shared_secret is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pre_shared_secret() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="pre-shared-secret", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pre_shared_secret must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="pre-shared-secret", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)""",
        })

    self.__pre_shared_secret = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pre_shared_secret(self):
    self.__pre_shared_secret = YANGDynClass(base=unicode, is_leaf=True, yang_name="pre-shared-secret", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)

  ip_address = __builtin__.property(_get_ip_address, _set_ip_address)
  netmask = __builtin__.property(_get_netmask, _set_netmask)
  pre_shared_secret = __builtin__.property(_get_pre_shared_secret, _set_pre_shared_secret)


  _pyangbind_elements = collections.OrderedDict([('ip_address', ip_address), ('netmask', netmask), ('pre_shared_secret', pre_shared_secret), ])


