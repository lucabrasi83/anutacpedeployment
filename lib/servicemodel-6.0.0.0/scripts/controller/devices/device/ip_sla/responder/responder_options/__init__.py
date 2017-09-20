
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
class responder_options(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/ip-sla/responder/responder-options. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__operation_type','__host','__auto_register_type','__client_id','__endpoint_list_name','__endpoint_list_type','__retry_timer','__ipaddress','__port',)

  _yang_name = 'responder-options'
  _module_name = 'l3features'
  _namespace = 'http://anutanetworks.com/l3features'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__endpoint_list_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-list-name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    self.__endpoint_list_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'client-id': {}, u'retry-timer': {}},), is_leaf=True, yang_name="endpoint-list-type", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)
    self.__auto_register_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'client-id': {}, u'endpoint-list': {}, u'retry-timer': {}},), is_leaf=True, yang_name="auto-register-type", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)
    self.__retry_timer = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..1440']}), is_leaf=True, yang_name="retry-timer", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)
    self.__host = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='inet:ipv4-address', is_config=True)
    self.__client_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="client-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    self.__operation_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto-register': {}, u'udp-echo': {}, u'twamp': {}, u'tcp-connect': {}},), is_leaf=True, yang_name="operation-type", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)
    self.__ipaddress = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipaddress", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='inet:ipv4-address', is_config=True)
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="port", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)

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
      return [u'devices', u'device', u'ip-sla', u'responder', u'responder-options']

  def _get_operation_type(self):
    """
    Getter method for operation_type, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/operation_type (enumeration)

    YANG Description: Select one of the operttion-type from list
    """
    return self.__operation_type
      
  def _set_operation_type(self, v, load=False):
    """
    Setter method for operation_type, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/operation_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_operation_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_operation_type() directly.

    YANG Description: Select one of the operttion-type from list
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto-register': {}, u'udp-echo': {}, u'twamp': {}, u'tcp-connect': {}},), is_leaf=True, yang_name="operation-type", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """operation_type must be of a type compatible with enumeration""",
          'defined-type': "l3features:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto-register': {}, u'udp-echo': {}, u'twamp': {}, u'tcp-connect': {}},), is_leaf=True, yang_name="operation-type", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)""",
        })

    self.__operation_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_operation_type(self):
    self.__operation_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto-register': {}, u'udp-echo': {}, u'twamp': {}, u'tcp-connect': {}},), is_leaf=True, yang_name="operation-type", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)


  def _get_host(self):
    """
    Getter method for host, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/host (inet:ipv4-address)

    YANG Description: Valid IPv4 Address (A.B.C.D for e.x: 172.16.1.1)
    """
    return self.__host
      
  def _set_host(self, v, load=False):
    """
    Setter method for host, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/host (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host() directly.

    YANG Description: Valid IPv4 Address (A.B.C.D for e.x: 172.16.1.1)
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__host = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host(self):
    self.__host = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='inet:ipv4-address', is_config=True)


  def _get_auto_register_type(self):
    """
    Getter method for auto_register_type, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/auto_register_type (enumeration)

    YANG Description: client-id
endpoint-list
retry-timer

    """
    return self.__auto_register_type
      
  def _set_auto_register_type(self, v, load=False):
    """
    Setter method for auto_register_type, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/auto_register_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auto_register_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auto_register_type() directly.

    YANG Description: client-id
endpoint-list
retry-timer

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'client-id': {}, u'endpoint-list': {}, u'retry-timer': {}},), is_leaf=True, yang_name="auto-register-type", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auto_register_type must be of a type compatible with enumeration""",
          'defined-type': "l3features:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'client-id': {}, u'endpoint-list': {}, u'retry-timer': {}},), is_leaf=True, yang_name="auto-register-type", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)""",
        })

    self.__auto_register_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auto_register_type(self):
    self.__auto_register_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'client-id': {}, u'endpoint-list': {}, u'retry-timer': {}},), is_leaf=True, yang_name="auto-register-type", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)


  def _get_client_id(self):
    """
    Getter method for client_id, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/client_id (string)

    YANG Description: string
    """
    return self.__client_id
      
  def _set_client_id(self, v, load=False):
    """
    Setter method for client_id, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/client_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="client-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="client-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__client_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_id(self):
    self.__client_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="client-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)


  def _get_endpoint_list_name(self):
    """
    Getter method for endpoint_list_name, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/endpoint_list_name (string)

    YANG Description: string
    """
    return self.__endpoint_list_name
      
  def _set_endpoint_list_name(self, v, load=False):
    """
    Setter method for endpoint_list_name, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/endpoint_list_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_endpoint_list_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_endpoint_list_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="endpoint-list-name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """endpoint_list_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-list-name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__endpoint_list_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_endpoint_list_name(self):
    self.__endpoint_list_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-list-name", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)


  def _get_endpoint_list_type(self):
    """
    Getter method for endpoint_list_type, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/endpoint_list_type (enumeration)

    YANG Description: client-id
retry-timer

    """
    return self.__endpoint_list_type
      
  def _set_endpoint_list_type(self, v, load=False):
    """
    Setter method for endpoint_list_type, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/endpoint_list_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_endpoint_list_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_endpoint_list_type() directly.

    YANG Description: client-id
retry-timer

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'client-id': {}, u'retry-timer': {}},), is_leaf=True, yang_name="endpoint-list-type", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """endpoint_list_type must be of a type compatible with enumeration""",
          'defined-type': "l3features:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'client-id': {}, u'retry-timer': {}},), is_leaf=True, yang_name="endpoint-list-type", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)""",
        })

    self.__endpoint_list_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_endpoint_list_type(self):
    self.__endpoint_list_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'client-id': {}, u'retry-timer': {}},), is_leaf=True, yang_name="endpoint-list-type", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)


  def _get_retry_timer(self):
    """
    Getter method for retry_timer, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/retry_timer (uint16)

    YANG Description: 1..1440
    """
    return self.__retry_timer
      
  def _set_retry_timer(self, v, load=False):
    """
    Setter method for retry_timer, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/retry_timer (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_retry_timer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_retry_timer() directly.

    YANG Description: 1..1440
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..1440']}), is_leaf=True, yang_name="retry-timer", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """retry_timer must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..1440']}), is_leaf=True, yang_name="retry-timer", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)""",
        })

    self.__retry_timer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_retry_timer(self):
    self.__retry_timer = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..1440']}), is_leaf=True, yang_name="retry-timer", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)


  def _get_ipaddress(self):
    """
    Getter method for ipaddress, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/ipaddress (inet:ipv4-address)

    YANG Description: Valid IPv4 Address (A.B.C.D for e.x: 172.16.1.1)
    """
    return self.__ipaddress
      
  def _set_ipaddress(self, v, load=False):
    """
    Setter method for ipaddress, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/ipaddress (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipaddress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipaddress() directly.

    YANG Description: Valid IPv4 Address (A.B.C.D for e.x: 172.16.1.1)
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipaddress", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipaddress must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipaddress", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ipaddress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipaddress(self):
    self.__ipaddress = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipaddress", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='inet:ipv4-address', is_config=True)


  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/port (uint16)

    YANG Description: 1..65535
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /devices/device/ip_sla/responder/responder_options/port (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.

    YANG Description: 1..65535
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="port", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="port", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="port", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)

  operation_type = __builtin__.property(_get_operation_type, _set_operation_type)
  host = __builtin__.property(_get_host, _set_host)
  auto_register_type = __builtin__.property(_get_auto_register_type, _set_auto_register_type)
  client_id = __builtin__.property(_get_client_id, _set_client_id)
  endpoint_list_name = __builtin__.property(_get_endpoint_list_name, _set_endpoint_list_name)
  endpoint_list_type = __builtin__.property(_get_endpoint_list_type, _set_endpoint_list_type)
  retry_timer = __builtin__.property(_get_retry_timer, _set_retry_timer)
  ipaddress = __builtin__.property(_get_ipaddress, _set_ipaddress)
  port = __builtin__.property(_get_port, _set_port)


  _pyangbind_elements = collections.OrderedDict([('operation_type', operation_type), ('host', host), ('auto_register_type', auto_register_type), ('client_id', client_id), ('endpoint_list_name', endpoint_list_name), ('endpoint_list_type', endpoint_list_type), ('retry_timer', retry_timer), ('ipaddress', ipaddress), ('port', port), ])


