
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
import pre_shared_key
class crypto_keyring(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/crypto-keyrings/crypto-keyring. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__key_ring_name','__ike_version','__auth_type','__vrf_name','__pre_shared_key','__cryptoisakmpkey','__peer_name',)

  _yang_name = 'crypto-keyring'
  _module_name = 'dmvpn'
  _namespace = 'http://anutanetworks.com/dmvpn'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__auth_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rsa-sig': {}, u'pre-share': {}},), is_leaf=True, yang_name="auth-type", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='auth-mode', is_config=True)
    self.__key_ring_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="key-ring-name", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)
    self.__pre_shared_key = YANGDynClass(base=YANGListType("ip_address",pre_shared_key.pre_shared_key, yang_name="pre-shared-key", module_name="dmvpn", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address'), is_container='list', yang_name="pre-shared-key", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='list', is_config=True)
    self.__vrf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)
    self.__cryptoisakmpkey = YANGDynClass(base=unicode, is_leaf=True, yang_name="cryptoisakmpkey", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)
    self.__peer_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="peer-name", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)
    self.__ike_version = YANGDynClass(base=unicode, is_leaf=True, yang_name="ike-version", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'crypto-keyrings', u'crypto-keyring']

  def _get_key_ring_name(self):
    """
    Getter method for key_ring_name, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/key_ring_name (string)

    YANG Description: string
    """
    return self.__key_ring_name
      
  def _set_key_ring_name(self, v, load=False):
    """
    Setter method for key_ring_name, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/key_ring_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_ring_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_ring_name() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="key-ring-name", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_ring_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="key-ring-name", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)""",
        })

    self.__key_ring_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_ring_name(self):
    self.__key_ring_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="key-ring-name", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)


  def _get_ike_version(self):
    """
    Getter method for ike_version, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/ike_version (string)

    YANG Description: string
    """
    return self.__ike_version
      
  def _set_ike_version(self, v, load=False):
    """
    Setter method for ike_version, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/ike_version (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ike_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ike_version() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ike-version", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ike_version must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ike-version", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)""",
        })

    self.__ike_version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ike_version(self):
    self.__ike_version = YANGDynClass(base=unicode, is_leaf=True, yang_name="ike-version", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)


  def _get_auth_type(self):
    """
    Getter method for auth_type, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/auth_type (auth-mode)

    YANG Description: pre-share
rsa-sig

    """
    return self.__auth_type
      
  def _set_auth_type(self, v, load=False):
    """
    Setter method for auth_type, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/auth_type (auth-mode)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_type() directly.

    YANG Description: pre-share
rsa-sig

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rsa-sig': {}, u'pre-share': {}},), is_leaf=True, yang_name="auth-type", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='auth-mode', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_type must be of a type compatible with auth-mode""",
          'defined-type': "dmvpn:auth-mode",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rsa-sig': {}, u'pre-share': {}},), is_leaf=True, yang_name="auth-type", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='auth-mode', is_config=True)""",
        })

    self.__auth_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_type(self):
    self.__auth_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rsa-sig': {}, u'pre-share': {}},), is_leaf=True, yang_name="auth-type", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='auth-mode', is_config=True)


  def _get_vrf_name(self):
    """
    Getter method for vrf_name, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/vrf_name (string)

    YANG Description: string
    """
    return self.__vrf_name
      
  def _set_vrf_name(self, v, load=False):
    """
    Setter method for vrf_name, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/vrf_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vrf-name", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)""",
        })

    self.__vrf_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf_name(self):
    self.__vrf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)


  def _get_pre_shared_key(self):
    """
    Getter method for pre_shared_key, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/pre_shared_key (list)
    """
    return self.__pre_shared_key
      
  def _set_pre_shared_key(self, v, load=False):
    """
    Setter method for pre_shared_key, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/pre_shared_key (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pre_shared_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pre_shared_key() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("ip_address",pre_shared_key.pre_shared_key, yang_name="pre-shared-key", module_name="dmvpn", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address'), is_container='list', yang_name="pre-shared-key", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pre_shared_key must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ip_address",pre_shared_key.pre_shared_key, yang_name="pre-shared-key", module_name="dmvpn", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address'), is_container='list', yang_name="pre-shared-key", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='list', is_config=True)""",
        })

    self.__pre_shared_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pre_shared_key(self):
    self.__pre_shared_key = YANGDynClass(base=YANGListType("ip_address",pre_shared_key.pre_shared_key, yang_name="pre-shared-key", module_name="dmvpn", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address'), is_container='list', yang_name="pre-shared-key", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='list', is_config=True)


  def _get_cryptoisakmpkey(self):
    """
    Getter method for cryptoisakmpkey, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/cryptoisakmpkey (string)

    YANG Description: string
    """
    return self.__cryptoisakmpkey
      
  def _set_cryptoisakmpkey(self, v, load=False):
    """
    Setter method for cryptoisakmpkey, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/cryptoisakmpkey (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cryptoisakmpkey is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cryptoisakmpkey() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="cryptoisakmpkey", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cryptoisakmpkey must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="cryptoisakmpkey", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)""",
        })

    self.__cryptoisakmpkey = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cryptoisakmpkey(self):
    self.__cryptoisakmpkey = YANGDynClass(base=unicode, is_leaf=True, yang_name="cryptoisakmpkey", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)


  def _get_peer_name(self):
    """
    Getter method for peer_name, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/peer_name (string)

    YANG Description: string
    """
    return self.__peer_name
      
  def _set_peer_name(self, v, load=False):
    """
    Setter method for peer_name, mapped from YANG variable /devices/device/crypto_keyrings/crypto_keyring/peer_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="peer-name", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="peer-name", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)""",
        })

    self.__peer_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_name(self):
    self.__peer_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="peer-name", module_name="dmvpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dmvpn', defining_module='dmvpn', yang_type='string', is_config=True)

  key_ring_name = __builtin__.property(_get_key_ring_name, _set_key_ring_name)
  ike_version = __builtin__.property(_get_ike_version, _set_ike_version)
  auth_type = __builtin__.property(_get_auth_type, _set_auth_type)
  vrf_name = __builtin__.property(_get_vrf_name, _set_vrf_name)
  pre_shared_key = __builtin__.property(_get_pre_shared_key, _set_pre_shared_key)
  cryptoisakmpkey = __builtin__.property(_get_cryptoisakmpkey, _set_cryptoisakmpkey)
  peer_name = __builtin__.property(_get_peer_name, _set_peer_name)


  _pyangbind_elements = collections.OrderedDict([('key_ring_name', key_ring_name), ('ike_version', ike_version), ('auth_type', auth_type), ('vrf_name', vrf_name), ('pre_shared_key', pre_shared_key), ('cryptoisakmpkey', cryptoisakmpkey), ('peer_name', peer_name), ])


