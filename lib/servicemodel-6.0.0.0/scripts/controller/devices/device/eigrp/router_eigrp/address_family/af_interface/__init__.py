
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
import summary_network
class af_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/eigrp/router-eigrp/address-family/af-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__interface','__passive_interface','__auth_mode','__key_chain','__hello_interval','__hold_time','__split_horizon','__stub_site','__summary_network',)

  _yang_name = 'af-interface'
  _module_name = 'l3features'
  _namespace = 'http://anutanetworks.com/l3features'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__passive_interface = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="passive-interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    self.__key_chain = YANGDynClass(base=unicode, is_leaf=True, yang_name="key-chain", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    self.__auth_mode = YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-mode", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    self.__split_horizon = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="split-horizon", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    self.__summary_network = YANGDynClass(base=YANGListType("ip_address netmask",summary_network.summary_network, yang_name="summary-network", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address netmask'), is_container='list', yang_name="summary-network", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)
    self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="hello-interval", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)
    self.__interface = YANGDynClass(base=[unicode,unicode,], is_leaf=True, yang_name="interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='union', is_config=True)
    self.__stub_site = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="stub-site", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    self.__hold_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="hold-time", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)

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
      return [u'devices', u'device', u'eigrp', u'router-eigrp', u'address-family', u'af-interface']

  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/interface (union)

    YANG Description: Union Input types:
leafref
string

    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/interface (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Union Input types:
leafref
string

    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=[unicode,unicode,], is_leaf=True, yang_name="interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with union""",
          'defined-type': "l3features:union",
          'generated-type': """YANGDynClass(base=[unicode,unicode,], is_leaf=True, yang_name="interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='union', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=[unicode,unicode,], is_leaf=True, yang_name="interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='union', is_config=True)


  def _get_passive_interface(self):
    """
    Getter method for passive_interface, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/passive_interface (boolean)

    YANG Description: passive-interface: True/False
    """
    return self.__passive_interface
      
  def _set_passive_interface(self, v, load=False):
    """
    Setter method for passive_interface, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/passive_interface (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive_interface() directly.

    YANG Description: passive-interface: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="passive-interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive_interface must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="passive-interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)""",
        })

    self.__passive_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive_interface(self):
    self.__passive_interface = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="passive-interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)


  def _get_auth_mode(self):
    """
    Getter method for auth_mode, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/auth_mode (string)

    YANG Description: string
    """
    return self.__auth_mode
      
  def _set_auth_mode(self, v, load=False):
    """
    Setter method for auth_mode, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/auth_mode (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_mode() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="auth-mode", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_mode must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-mode", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__auth_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_mode(self):
    self.__auth_mode = YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-mode", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)


  def _get_key_chain(self):
    """
    Getter method for key_chain, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/key_chain (string)

    YANG Description: string
    """
    return self.__key_chain
      
  def _set_key_chain(self, v, load=False):
    """
    Setter method for key_chain, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/key_chain (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_chain is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_chain() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="key-chain", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_chain must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="key-chain", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__key_chain = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_chain(self):
    self.__key_chain = YANGDynClass(base=unicode, is_leaf=True, yang_name="key-chain", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)


  def _get_hello_interval(self):
    """
    Getter method for hello_interval, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/hello_interval (uint16)

    YANG Description: 1..65535
    """
    return self.__hello_interval
      
  def _set_hello_interval(self, v, load=False):
    """
    Setter method for hello_interval, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/hello_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_interval() directly.

    YANG Description: 1..65535
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="hello-interval", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="hello-interval", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)""",
        })

    self.__hello_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_interval(self):
    self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="hello-interval", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)


  def _get_hold_time(self):
    """
    Getter method for hold_time, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/hold_time (uint16)

    YANG Description: 1..65535
    """
    return self.__hold_time
      
  def _set_hold_time(self, v, load=False):
    """
    Setter method for hold_time, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/hold_time (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hold_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hold_time() directly.

    YANG Description: 1..65535
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="hold-time", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hold_time must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="hold-time", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)""",
        })

    self.__hold_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hold_time(self):
    self.__hold_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="hold-time", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='uint16', is_config=True)


  def _get_split_horizon(self):
    """
    Getter method for split_horizon, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/split_horizon (boolean)

    YANG Description: split-horizon: True/False
    """
    return self.__split_horizon
      
  def _set_split_horizon(self, v, load=False):
    """
    Setter method for split_horizon, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/split_horizon (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_split_horizon is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_split_horizon() directly.

    YANG Description: split-horizon: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="split-horizon", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """split_horizon must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="split-horizon", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)""",
        })

    self.__split_horizon = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_split_horizon(self):
    self.__split_horizon = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="split-horizon", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)


  def _get_stub_site(self):
    """
    Getter method for stub_site, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/stub_site (boolean)

    YANG Description: stub-site: True/False
    """
    return self.__stub_site
      
  def _set_stub_site(self, v, load=False):
    """
    Setter method for stub_site, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/stub_site (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_stub_site is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_stub_site() directly.

    YANG Description: stub-site: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="stub-site", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """stub_site must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="stub-site", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)""",
        })

    self.__stub_site = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_stub_site(self):
    self.__stub_site = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="stub-site", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='boolean', is_config=True)


  def _get_summary_network(self):
    """
    Getter method for summary_network, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/summary_network (list)
    """
    return self.__summary_network
      
  def _set_summary_network(self, v, load=False):
    """
    Setter method for summary_network, mapped from YANG variable /devices/device/eigrp/router_eigrp/address_family/af_interface/summary_network (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summary_network is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summary_network() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("ip_address netmask",summary_network.summary_network, yang_name="summary-network", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address netmask'), is_container='list', yang_name="summary-network", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summary_network must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ip_address netmask",summary_network.summary_network, yang_name="summary-network", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address netmask'), is_container='list', yang_name="summary-network", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)""",
        })

    self.__summary_network = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summary_network(self):
    self.__summary_network = YANGDynClass(base=YANGListType("ip_address netmask",summary_network.summary_network, yang_name="summary-network", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address netmask'), is_container='list', yang_name="summary-network", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)

  interface = __builtin__.property(_get_interface, _set_interface)
  passive_interface = __builtin__.property(_get_passive_interface, _set_passive_interface)
  auth_mode = __builtin__.property(_get_auth_mode, _set_auth_mode)
  key_chain = __builtin__.property(_get_key_chain, _set_key_chain)
  hello_interval = __builtin__.property(_get_hello_interval, _set_hello_interval)
  hold_time = __builtin__.property(_get_hold_time, _set_hold_time)
  split_horizon = __builtin__.property(_get_split_horizon, _set_split_horizon)
  stub_site = __builtin__.property(_get_stub_site, _set_stub_site)
  summary_network = __builtin__.property(_get_summary_network, _set_summary_network)


  _pyangbind_elements = collections.OrderedDict([('interface', interface), ('passive_interface', passive_interface), ('auth_mode', auth_mode), ('key_chain', key_chain), ('hello_interval', hello_interval), ('hold_time', hold_time), ('split_horizon', split_horizon), ('stub_site', stub_site), ('summary_network', summary_network), ])


