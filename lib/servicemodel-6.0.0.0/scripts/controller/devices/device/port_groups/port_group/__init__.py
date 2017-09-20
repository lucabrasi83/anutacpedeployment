
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
import assigned_vm
class port_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/port-groups/port-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__vlan_type','__vlan_id','__vlan_name','__port_count','__mode','__promiscuous_mode','__assigned_vm',)

  _yang_name = 'port-group'
  _module_name = 'l2features'
  _namespace = 'http://anutanetworks.com/l2features'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__port_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4096), is_leaf=True, yang_name="port-count", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='uint32', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='string', is_config=True)
    self.__vlan_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'voice': {}, u'vlan': {}, u'vxlan': {}},), is_leaf=True, yang_name="vlan-type", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='vlan-type', is_config=True)
    self.__promiscuous_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Accept': {}, u'Reject': {}},), is_leaf=True, yang_name="promiscuous-mode", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='promiscuous-mode-type', is_config=True)
    self.__vlan_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vlan-name", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='string', is_config=True)
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'downlink': {}, u'uplink': {}},), is_leaf=True, yang_name="mode", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='port-group-mode', is_config=True)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4096']}), is_leaf=True, yang_name="vlan-id", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='uint32', is_config=True)
    self.__assigned_vm = YANGDynClass(base=YANGListType("vm_name interface_name",assigned_vm.assigned_vm, yang_name="assigned-vm", module_name="l2features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vm-name interface-name'), is_container='list', yang_name="assigned-vm", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='list', is_config=True)

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
      return [u'devices', u'device', u'port-groups', u'port-group']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /devices/device/port_groups/port_group/name (string)

    YANG Description: string
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /devices/device/port_groups/port_group/name (string)
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
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='string', is_config=True)


  def _get_vlan_type(self):
    """
    Getter method for vlan_type, mapped from YANG variable /devices/device/port_groups/port_group/vlan_type (vlan-type)

    YANG Description: vxlan
vlan
voice

    """
    return self.__vlan_type
      
  def _set_vlan_type(self, v, load=False):
    """
    Setter method for vlan_type, mapped from YANG variable /devices/device/port_groups/port_group/vlan_type (vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_type() directly.

    YANG Description: vxlan
vlan
voice

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'voice': {}, u'vlan': {}, u'vxlan': {}},), is_leaf=True, yang_name="vlan-type", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_type must be of a type compatible with vlan-type""",
          'defined-type': "l2features:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'voice': {}, u'vlan': {}, u'vxlan': {}},), is_leaf=True, yang_name="vlan-type", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='vlan-type', is_config=True)""",
        })

    self.__vlan_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_type(self):
    self.__vlan_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'voice': {}, u'vlan': {}, u'vxlan': {}},), is_leaf=True, yang_name="vlan-type", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='vlan-type', is_config=True)


  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /devices/device/port_groups/port_group/vlan_id (uint32)

    YANG Description: 1..4096
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /devices/device/port_groups/port_group/vlan_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: 1..4096
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4096']}), is_leaf=True, yang_name="vlan-id", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4096']}), is_leaf=True, yang_name="vlan-id", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='uint32', is_config=True)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4096']}), is_leaf=True, yang_name="vlan-id", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='uint32', is_config=True)


  def _get_vlan_name(self):
    """
    Getter method for vlan_name, mapped from YANG variable /devices/device/port_groups/port_group/vlan_name (string)

    YANG Description: string
    """
    return self.__vlan_name
      
  def _set_vlan_name(self, v, load=False):
    """
    Setter method for vlan_name, mapped from YANG variable /devices/device/port_groups/port_group/vlan_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vlan-name", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vlan-name", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='string', is_config=True)""",
        })

    self.__vlan_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_name(self):
    self.__vlan_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vlan-name", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='string', is_config=True)


  def _get_port_count(self):
    """
    Getter method for port_count, mapped from YANG variable /devices/device/port_groups/port_group/port_count (uint32)

    YANG Description: 0..4294967295
    """
    return self.__port_count
      
  def _set_port_count(self, v, load=False):
    """
    Setter method for port_count, mapped from YANG variable /devices/device/port_groups/port_group/port_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_count() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4096), is_leaf=True, yang_name="port-count", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4096), is_leaf=True, yang_name="port-count", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='uint32', is_config=True)""",
        })

    self.__port_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_count(self):
    self.__port_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4096), is_leaf=True, yang_name="port-count", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='uint32', is_config=True)


  def _get_mode(self):
    """
    Getter method for mode, mapped from YANG variable /devices/device/port_groups/port_group/mode (port-group-mode)

    YANG Description: uplink
downlink

    """
    return self.__mode
      
  def _set_mode(self, v, load=False):
    """
    Setter method for mode, mapped from YANG variable /devices/device/port_groups/port_group/mode (port-group-mode)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode() directly.

    YANG Description: uplink
downlink

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'downlink': {}, u'uplink': {}},), is_leaf=True, yang_name="mode", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='port-group-mode', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode must be of a type compatible with port-group-mode""",
          'defined-type': "l2features:port-group-mode",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'downlink': {}, u'uplink': {}},), is_leaf=True, yang_name="mode", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='port-group-mode', is_config=True)""",
        })

    self.__mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode(self):
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'downlink': {}, u'uplink': {}},), is_leaf=True, yang_name="mode", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='port-group-mode', is_config=True)


  def _get_promiscuous_mode(self):
    """
    Getter method for promiscuous_mode, mapped from YANG variable /devices/device/port_groups/port_group/promiscuous_mode (promiscuous-mode-type)

    YANG Description: Accept
Reject

    """
    return self.__promiscuous_mode
      
  def _set_promiscuous_mode(self, v, load=False):
    """
    Setter method for promiscuous_mode, mapped from YANG variable /devices/device/port_groups/port_group/promiscuous_mode (promiscuous-mode-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_promiscuous_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_promiscuous_mode() directly.

    YANG Description: Accept
Reject

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Accept': {}, u'Reject': {}},), is_leaf=True, yang_name="promiscuous-mode", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='promiscuous-mode-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """promiscuous_mode must be of a type compatible with promiscuous-mode-type""",
          'defined-type': "l2features:promiscuous-mode-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Accept': {}, u'Reject': {}},), is_leaf=True, yang_name="promiscuous-mode", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='promiscuous-mode-type', is_config=True)""",
        })

    self.__promiscuous_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_promiscuous_mode(self):
    self.__promiscuous_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Accept': {}, u'Reject': {}},), is_leaf=True, yang_name="promiscuous-mode", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='promiscuous-mode-type', is_config=True)


  def _get_assigned_vm(self):
    """
    Getter method for assigned_vm, mapped from YANG variable /devices/device/port_groups/port_group/assigned_vm (list)
    """
    return self.__assigned_vm
      
  def _set_assigned_vm(self, v, load=False):
    """
    Setter method for assigned_vm, mapped from YANG variable /devices/device/port_groups/port_group/assigned_vm (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_assigned_vm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_assigned_vm() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("vm_name interface_name",assigned_vm.assigned_vm, yang_name="assigned-vm", module_name="l2features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vm-name interface-name'), is_container='list', yang_name="assigned-vm", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """assigned_vm must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vm_name interface_name",assigned_vm.assigned_vm, yang_name="assigned-vm", module_name="l2features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vm-name interface-name'), is_container='list', yang_name="assigned-vm", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='list', is_config=True)""",
        })

    self.__assigned_vm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_assigned_vm(self):
    self.__assigned_vm = YANGDynClass(base=YANGListType("vm_name interface_name",assigned_vm.assigned_vm, yang_name="assigned-vm", module_name="l2features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vm-name interface-name'), is_container='list', yang_name="assigned-vm", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='list', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  vlan_type = __builtin__.property(_get_vlan_type, _set_vlan_type)
  vlan_id = __builtin__.property(_get_vlan_id, _set_vlan_id)
  vlan_name = __builtin__.property(_get_vlan_name, _set_vlan_name)
  port_count = __builtin__.property(_get_port_count, _set_port_count)
  mode = __builtin__.property(_get_mode, _set_mode)
  promiscuous_mode = __builtin__.property(_get_promiscuous_mode, _set_promiscuous_mode)
  assigned_vm = __builtin__.property(_get_assigned_vm, _set_assigned_vm)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('vlan_type', vlan_type), ('vlan_id', vlan_id), ('vlan_name', vlan_name), ('port_count', port_count), ('mode', mode), ('promiscuous_mode', promiscuous_mode), ('assigned_vm', assigned_vm), ])


