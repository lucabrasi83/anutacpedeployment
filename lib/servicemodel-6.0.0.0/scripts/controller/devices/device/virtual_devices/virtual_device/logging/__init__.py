
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
import logging_hosts
class logging(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/virtual-devices/virtual-device/logging. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__interface_name','__ip_address','__facility_number','__facility_name','__no_logging_console','__logging_trap','__buffer_size','__logging_hosts',)

  _yang_name = 'logging'
  _module_name = 'firewall'
  _namespace = 'http://anutanetworks.com/firewall'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__logging_hosts = YANGDynClass(base=YANGListType("ip_address",logging_hosts.logging_hosts, yang_name="logging-hosts", module_name="firewall", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address'), is_container='list', yang_name="logging-hosts", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='list', is_config=True)
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='leafref', is_config=True)
    self.__facility_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="facility-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__logging_trap = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'debugging': {}, u'errors': {}, u'warnings': {}, u'alerts': {}, u'emergencies': {}, u'notifications': {}, u'critical': {}, u'informational': {}},), is_leaf=True, yang_name="logging-trap", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='enumeration', is_config=True)
    self.__buffer_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="buffer-size", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='uint32', is_config=True)
    self.__no_logging_console = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="no-logging-console", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='boolean', is_config=True)
    self.__ip_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-address", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__facility_number = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="facility-number", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='uint32', is_config=True)

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
      return [u'devices', u'device', u'virtual-devices', u'virtual-device', u'logging']

  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/interface_name (leafref)

    YANG Description: interface-name
    """
    return self.__interface_name
      
  def _set_interface_name(self, v, load=False):
    """
    Setter method for interface_name, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/interface_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.

    YANG Description: interface-name
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='leafref', is_config=True)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='leafref', is_config=True)


  def _get_ip_address(self):
    """
    Getter method for ip_address, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/ip_address (string)

    YANG Description: string
    """
    return self.__ip_address
      
  def _set_ip_address(self, v, load=False):
    """
    Setter method for ip_address, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/ip_address (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_address() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ip-address", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_address must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-address", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_address(self):
    self.__ip_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-address", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_facility_number(self):
    """
    Getter method for facility_number, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/facility_number (uint32)

    YANG Description: 0..4294967295
    """
    return self.__facility_number
      
  def _set_facility_number(self, v, load=False):
    """
    Setter method for facility_number, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/facility_number (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_facility_number is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_facility_number() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="facility-number", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """facility_number must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="facility-number", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='uint32', is_config=True)""",
        })

    self.__facility_number = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_facility_number(self):
    self.__facility_number = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="facility-number", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='uint32', is_config=True)


  def _get_facility_name(self):
    """
    Getter method for facility_name, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/facility_name (string)

    YANG Description: string
    """
    return self.__facility_name
      
  def _set_facility_name(self, v, load=False):
    """
    Setter method for facility_name, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/facility_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_facility_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_facility_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="facility-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """facility_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="facility-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__facility_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_facility_name(self):
    self.__facility_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="facility-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_no_logging_console(self):
    """
    Getter method for no_logging_console, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/no_logging_console (boolean)

    YANG Description: no-logging-console: True/False
    """
    return self.__no_logging_console
      
  def _set_no_logging_console(self, v, load=False):
    """
    Setter method for no_logging_console, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/no_logging_console (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_logging_console is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_logging_console() directly.

    YANG Description: no-logging-console: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="no-logging-console", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_logging_console must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="no-logging-console", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='boolean', is_config=True)""",
        })

    self.__no_logging_console = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_logging_console(self):
    self.__no_logging_console = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="no-logging-console", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='boolean', is_config=True)


  def _get_logging_trap(self):
    """
    Getter method for logging_trap, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/logging_trap (enumeration)

    YANG Description: emergencies
alerts
critical
errors
warnings
notifications
informational
debugging

    """
    return self.__logging_trap
      
  def _set_logging_trap(self, v, load=False):
    """
    Setter method for logging_trap, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/logging_trap (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logging_trap is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logging_trap() directly.

    YANG Description: emergencies
alerts
critical
errors
warnings
notifications
informational
debugging

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'debugging': {}, u'errors': {}, u'warnings': {}, u'alerts': {}, u'emergencies': {}, u'notifications': {}, u'critical': {}, u'informational': {}},), is_leaf=True, yang_name="logging-trap", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logging_trap must be of a type compatible with enumeration""",
          'defined-type': "firewall:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'debugging': {}, u'errors': {}, u'warnings': {}, u'alerts': {}, u'emergencies': {}, u'notifications': {}, u'critical': {}, u'informational': {}},), is_leaf=True, yang_name="logging-trap", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='enumeration', is_config=True)""",
        })

    self.__logging_trap = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logging_trap(self):
    self.__logging_trap = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'debugging': {}, u'errors': {}, u'warnings': {}, u'alerts': {}, u'emergencies': {}, u'notifications': {}, u'critical': {}, u'informational': {}},), is_leaf=True, yang_name="logging-trap", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='enumeration', is_config=True)


  def _get_buffer_size(self):
    """
    Getter method for buffer_size, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/buffer_size (uint32)

    YANG Description: 0..4294967295
    """
    return self.__buffer_size
      
  def _set_buffer_size(self, v, load=False):
    """
    Setter method for buffer_size, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/buffer_size (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_buffer_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_buffer_size() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="buffer-size", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """buffer_size must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="buffer-size", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='uint32', is_config=True)""",
        })

    self.__buffer_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_buffer_size(self):
    self.__buffer_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="buffer-size", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='uint32', is_config=True)


  def _get_logging_hosts(self):
    """
    Getter method for logging_hosts, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/logging_hosts (list)
    """
    return self.__logging_hosts
      
  def _set_logging_hosts(self, v, load=False):
    """
    Setter method for logging_hosts, mapped from YANG variable /devices/device/virtual_devices/virtual_device/logging/logging_hosts (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logging_hosts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logging_hosts() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("ip_address",logging_hosts.logging_hosts, yang_name="logging-hosts", module_name="firewall", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address'), is_container='list', yang_name="logging-hosts", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logging_hosts must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ip_address",logging_hosts.logging_hosts, yang_name="logging-hosts", module_name="firewall", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address'), is_container='list', yang_name="logging-hosts", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='list', is_config=True)""",
        })

    self.__logging_hosts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logging_hosts(self):
    self.__logging_hosts = YANGDynClass(base=YANGListType("ip_address",logging_hosts.logging_hosts, yang_name="logging-hosts", module_name="firewall", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address'), is_container='list', yang_name="logging-hosts", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='list', is_config=True)

  interface_name = __builtin__.property(_get_interface_name, _set_interface_name)
  ip_address = __builtin__.property(_get_ip_address, _set_ip_address)
  facility_number = __builtin__.property(_get_facility_number, _set_facility_number)
  facility_name = __builtin__.property(_get_facility_name, _set_facility_name)
  no_logging_console = __builtin__.property(_get_no_logging_console, _set_no_logging_console)
  logging_trap = __builtin__.property(_get_logging_trap, _set_logging_trap)
  buffer_size = __builtin__.property(_get_buffer_size, _set_buffer_size)
  logging_hosts = __builtin__.property(_get_logging_hosts, _set_logging_hosts)


  _pyangbind_elements = collections.OrderedDict([('interface_name', interface_name), ('ip_address', ip_address), ('facility_number', facility_number), ('facility_name', facility_name), ('no_logging_console', no_logging_console), ('logging_trap', logging_trap), ('buffer_size', buffer_size), ('logging_hosts', logging_hosts), ])


