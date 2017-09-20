
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
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module vnfdriver - based on the path /vnfdriver_rpc/vm-power-off/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__mgmt_ip','__user_name','__password','__name','__request_timeout',)

  _yang_name = 'input'
  _module_name = 'vnfdriver'
  _namespace = 'http://anutanetworks.com/vnfdriver'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__request_timeout = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), default=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64)(500), is_leaf=True, yang_name="request-timeout", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='uint64', is_config=True)
    self.__password = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="password", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='ndt:password', is_config=True)
    self.__user_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="user-name", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='string', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='string', is_config=True)
    self.__mgmt_ip = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="mgmt-ip", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='inet:ip-address', is_config=True)

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
      return [u'vnfdriver_rpc', u'vm-power-off', u'input']

  def _get_mgmt_ip(self):
    """
    Getter method for mgmt_ip, mapped from YANG variable /vnfdriver_rpc/vm_power_off/input/mgmt_ip (inet:ip-address)

    YANG Description: Management Ip Address of Virtual Machine
    """
    return self.__mgmt_ip
      
  def _set_mgmt_ip(self, v, load=False):
    """
    Setter method for mgmt_ip, mapped from YANG variable /vnfdriver_rpc/vm_power_off/input/mgmt_ip (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mgmt_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mgmt_ip() directly.

    YANG Description: Management Ip Address of Virtual Machine
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="mgmt-ip", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mgmt_ip must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="mgmt-ip", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='inet:ip-address', is_config=True)""",
        })

    self.__mgmt_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mgmt_ip(self):
    self.__mgmt_ip = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="mgmt-ip", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='inet:ip-address', is_config=True)


  def _get_user_name(self):
    """
    Getter method for user_name, mapped from YANG variable /vnfdriver_rpc/vm_power_off/input/user_name (string)

    YANG Description: User Name to manage the Virtual Machine
    """
    return self.__user_name
      
  def _set_user_name(self, v, load=False):
    """
    Setter method for user_name, mapped from YANG variable /vnfdriver_rpc/vm_power_off/input/user_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_user_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_user_name() directly.

    YANG Description: User Name to manage the Virtual Machine
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="user-name", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """user_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="user-name", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='string', is_config=True)""",
        })

    self.__user_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_user_name(self):
    self.__user_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="user-name", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='string', is_config=True)


  def _get_password(self):
    """
    Getter method for password, mapped from YANG variable /vnfdriver_rpc/vm_power_off/input/password (ndt:password)

    YANG Description: Password to manage the Virtual Machine
    """
    return self.__password
      
  def _set_password(self, v, load=False):
    """
    Setter method for password, mapped from YANG variable /vnfdriver_rpc/vm_power_off/input/password (ndt:password)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_password() directly.

    YANG Description: Password to manage the Virtual Machine
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="password", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='ndt:password', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """password must be of a type compatible with ndt:password""",
          'defined-type': "ndt:password",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="password", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='ndt:password', is_config=True)""",
        })

    self.__password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_password(self):
    self.__password = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="password", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='ndt:password', is_config=True)


  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /vnfdriver_rpc/vm_power_off/input/name (string)

    YANG Description: Alias Name of Virtual Machine
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /vnfdriver_rpc/vm_power_off/input/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Alias Name of Virtual Machine
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='string', is_config=True)


  def _get_request_timeout(self):
    """
    Getter method for request_timeout, mapped from YANG variable /vnfdriver_rpc/vm_power_off/input/request_timeout (uint64)

    YANG Description: Operation timeout in seconds
    """
    return self.__request_timeout
      
  def _set_request_timeout(self, v, load=False):
    """
    Setter method for request_timeout, mapped from YANG variable /vnfdriver_rpc/vm_power_off/input/request_timeout (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_request_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_request_timeout() directly.

    YANG Description: Operation timeout in seconds
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), default=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64)(500), is_leaf=True, yang_name="request-timeout", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """request_timeout must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), default=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64)(500), is_leaf=True, yang_name="request-timeout", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='uint64', is_config=True)""",
        })

    self.__request_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_request_timeout(self):
    self.__request_timeout = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), default=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64)(500), is_leaf=True, yang_name="request-timeout", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='uint64', is_config=True)

  mgmt_ip = __builtin__.property(_get_mgmt_ip, _set_mgmt_ip)
  user_name = __builtin__.property(_get_user_name, _set_user_name)
  password = __builtin__.property(_get_password, _set_password)
  name = __builtin__.property(_get_name, _set_name)
  request_timeout = __builtin__.property(_get_request_timeout, _set_request_timeout)


  _pyangbind_elements = collections.OrderedDict([('mgmt_ip', mgmt_ip), ('user_name', user_name), ('password', password), ('name', name), ('request_timeout', request_timeout), ])


