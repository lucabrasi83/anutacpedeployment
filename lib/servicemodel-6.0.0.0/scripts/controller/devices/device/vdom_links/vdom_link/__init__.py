
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
class vdom_link(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/vdom-links/vdom-link. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__vdom_link_interface0','__interface0_vdom_name','__interface0_ip_address','__interface0_netmask','__interface0_access_types','__vdom_link_interface1','__interface1_vdom_name','__interface1_ip_address','__interface1_netmask','__interface1_access_types',)

  _yang_name = 'vdom-link'
  _module_name = 'firewall'
  _namespace = 'http://anutanetworks.com/firewall'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface1_ip_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="interface1-ip-address", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='inet:ip-address', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__interface1_netmask = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface1-netmask", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__interface0_ip_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="interface0-ip-address", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='inet:ip-address', is_config=True)
    self.__interface0_access_types = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface0-access-types", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__interface1_access_types = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface1-access-types", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__interface0_netmask = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface0-netmask", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__interface1_vdom_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface1-vdom-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='leafref', is_config=True)
    self.__interface0_vdom_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface0-vdom-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='leafref', is_config=True)
    self.__vdom_link_interface1 = YANGDynClass(base=unicode, is_leaf=True, yang_name="vdom-link-interface1", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__vdom_link_interface0 = YANGDynClass(base=unicode, is_leaf=True, yang_name="vdom-link-interface0", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'vdom-links', u'vdom-link']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /devices/device/vdom_links/vdom_link/name (string)

    YANG Description: string
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /devices/device/vdom_links/vdom_link/name (string)
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
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_vdom_link_interface0(self):
    """
    Getter method for vdom_link_interface0, mapped from YANG variable /devices/device/vdom_links/vdom_link/vdom_link_interface0 (string)

    YANG Description: string
    """
    return self.__vdom_link_interface0
      
  def _set_vdom_link_interface0(self, v, load=False):
    """
    Setter method for vdom_link_interface0, mapped from YANG variable /devices/device/vdom_links/vdom_link/vdom_link_interface0 (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vdom_link_interface0 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vdom_link_interface0() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vdom-link-interface0", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vdom_link_interface0 must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vdom-link-interface0", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__vdom_link_interface0 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vdom_link_interface0(self):
    self.__vdom_link_interface0 = YANGDynClass(base=unicode, is_leaf=True, yang_name="vdom-link-interface0", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_interface0_vdom_name(self):
    """
    Getter method for interface0_vdom_name, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface0_vdom_name (leafref)

    YANG Description: interface0-vdom-name
    """
    return self.__interface0_vdom_name
      
  def _set_interface0_vdom_name(self, v, load=False):
    """
    Setter method for interface0_vdom_name, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface0_vdom_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface0_vdom_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface0_vdom_name() directly.

    YANG Description: interface0-vdom-name
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface0-vdom-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface0_vdom_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface0-vdom-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='leafref', is_config=True)""",
        })

    self.__interface0_vdom_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface0_vdom_name(self):
    self.__interface0_vdom_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface0-vdom-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='leafref', is_config=True)


  def _get_interface0_ip_address(self):
    """
    Getter method for interface0_ip_address, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface0_ip_address (inet:ip-address)

    YANG Description: Valid IPv4/v6 Address (A.B.C.D for e.x: 172.16.1.1 or X::Y for e.x: 2001::1)
    """
    return self.__interface0_ip_address
      
  def _set_interface0_ip_address(self, v, load=False):
    """
    Setter method for interface0_ip_address, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface0_ip_address (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface0_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface0_ip_address() directly.

    YANG Description: Valid IPv4/v6 Address (A.B.C.D for e.x: 172.16.1.1 or X::Y for e.x: 2001::1)
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="interface0-ip-address", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface0_ip_address must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="interface0-ip-address", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='inet:ip-address', is_config=True)""",
        })

    self.__interface0_ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface0_ip_address(self):
    self.__interface0_ip_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="interface0-ip-address", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='inet:ip-address', is_config=True)


  def _get_interface0_netmask(self):
    """
    Getter method for interface0_netmask, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface0_netmask (string)

    YANG Description: string
    """
    return self.__interface0_netmask
      
  def _set_interface0_netmask(self, v, load=False):
    """
    Setter method for interface0_netmask, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface0_netmask (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface0_netmask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface0_netmask() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface0-netmask", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface0_netmask must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface0-netmask", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__interface0_netmask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface0_netmask(self):
    self.__interface0_netmask = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface0-netmask", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_interface0_access_types(self):
    """
    Getter method for interface0_access_types, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface0_access_types (string)

    YANG Description: string
    """
    return self.__interface0_access_types
      
  def _set_interface0_access_types(self, v, load=False):
    """
    Setter method for interface0_access_types, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface0_access_types (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface0_access_types is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface0_access_types() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface0-access-types", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface0_access_types must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface0-access-types", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__interface0_access_types = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface0_access_types(self):
    self.__interface0_access_types = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface0-access-types", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_vdom_link_interface1(self):
    """
    Getter method for vdom_link_interface1, mapped from YANG variable /devices/device/vdom_links/vdom_link/vdom_link_interface1 (string)

    YANG Description: string
    """
    return self.__vdom_link_interface1
      
  def _set_vdom_link_interface1(self, v, load=False):
    """
    Setter method for vdom_link_interface1, mapped from YANG variable /devices/device/vdom_links/vdom_link/vdom_link_interface1 (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vdom_link_interface1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vdom_link_interface1() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vdom-link-interface1", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vdom_link_interface1 must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vdom-link-interface1", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__vdom_link_interface1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vdom_link_interface1(self):
    self.__vdom_link_interface1 = YANGDynClass(base=unicode, is_leaf=True, yang_name="vdom-link-interface1", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_interface1_vdom_name(self):
    """
    Getter method for interface1_vdom_name, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface1_vdom_name (leafref)

    YANG Description: interface1-vdom-name
    """
    return self.__interface1_vdom_name
      
  def _set_interface1_vdom_name(self, v, load=False):
    """
    Setter method for interface1_vdom_name, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface1_vdom_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface1_vdom_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface1_vdom_name() directly.

    YANG Description: interface1-vdom-name
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface1-vdom-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface1_vdom_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface1-vdom-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='leafref', is_config=True)""",
        })

    self.__interface1_vdom_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface1_vdom_name(self):
    self.__interface1_vdom_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface1-vdom-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='leafref', is_config=True)


  def _get_interface1_ip_address(self):
    """
    Getter method for interface1_ip_address, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface1_ip_address (inet:ip-address)

    YANG Description: Valid IPv4/v6 Address (A.B.C.D for e.x: 172.16.1.1 or X::Y for e.x: 2001::1)
    """
    return self.__interface1_ip_address
      
  def _set_interface1_ip_address(self, v, load=False):
    """
    Setter method for interface1_ip_address, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface1_ip_address (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface1_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface1_ip_address() directly.

    YANG Description: Valid IPv4/v6 Address (A.B.C.D for e.x: 172.16.1.1 or X::Y for e.x: 2001::1)
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="interface1-ip-address", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface1_ip_address must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="interface1-ip-address", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='inet:ip-address', is_config=True)""",
        })

    self.__interface1_ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface1_ip_address(self):
    self.__interface1_ip_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="interface1-ip-address", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='inet:ip-address', is_config=True)


  def _get_interface1_netmask(self):
    """
    Getter method for interface1_netmask, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface1_netmask (string)

    YANG Description: string
    """
    return self.__interface1_netmask
      
  def _set_interface1_netmask(self, v, load=False):
    """
    Setter method for interface1_netmask, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface1_netmask (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface1_netmask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface1_netmask() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface1-netmask", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface1_netmask must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface1-netmask", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__interface1_netmask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface1_netmask(self):
    self.__interface1_netmask = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface1-netmask", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_interface1_access_types(self):
    """
    Getter method for interface1_access_types, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface1_access_types (string)

    YANG Description: string
    """
    return self.__interface1_access_types
      
  def _set_interface1_access_types(self, v, load=False):
    """
    Setter method for interface1_access_types, mapped from YANG variable /devices/device/vdom_links/vdom_link/interface1_access_types (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface1_access_types is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface1_access_types() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface1-access-types", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface1_access_types must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface1-access-types", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__interface1_access_types = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface1_access_types(self):
    self.__interface1_access_types = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface1-access-types", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  vdom_link_interface0 = __builtin__.property(_get_vdom_link_interface0, _set_vdom_link_interface0)
  interface0_vdom_name = __builtin__.property(_get_interface0_vdom_name, _set_interface0_vdom_name)
  interface0_ip_address = __builtin__.property(_get_interface0_ip_address, _set_interface0_ip_address)
  interface0_netmask = __builtin__.property(_get_interface0_netmask, _set_interface0_netmask)
  interface0_access_types = __builtin__.property(_get_interface0_access_types, _set_interface0_access_types)
  vdom_link_interface1 = __builtin__.property(_get_vdom_link_interface1, _set_vdom_link_interface1)
  interface1_vdom_name = __builtin__.property(_get_interface1_vdom_name, _set_interface1_vdom_name)
  interface1_ip_address = __builtin__.property(_get_interface1_ip_address, _set_interface1_ip_address)
  interface1_netmask = __builtin__.property(_get_interface1_netmask, _set_interface1_netmask)
  interface1_access_types = __builtin__.property(_get_interface1_access_types, _set_interface1_access_types)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('vdom_link_interface0', vdom_link_interface0), ('interface0_vdom_name', interface0_vdom_name), ('interface0_ip_address', interface0_ip_address), ('interface0_netmask', interface0_netmask), ('interface0_access_types', interface0_access_types), ('vdom_link_interface1', vdom_link_interface1), ('interface1_vdom_name', interface1_vdom_name), ('interface1_ip_address', interface1_ip_address), ('interface1_netmask', interface1_netmask), ('interface1_access_types', interface1_access_types), ])


