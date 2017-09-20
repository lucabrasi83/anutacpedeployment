
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
class application(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/virtual-devices/virtual-device/applications/application. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__description','__category','__app_protocol_name','__protocol_name','__protocol_number','__source_port','__dest_port','__icmp_type','__icmp_code','__icmp6_type','__icmp6_code','__device_group',)

  _yang_name = 'application'
  _module_name = 'firewall'
  _namespace = 'http://anutanetworks.com/firewall'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__category = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Remote Access': {}, u'business-systems': {}, u'networking': {}, u'Web Access': {}, u'media': {}, u'Network Services': {}, u'VoIP -Messaging and Other Applications': {}, u'General': {}, u'collaboration': {}, u'Authentication': {}, u'Web Proxy': {}, u'File Access': {}, u'Tunneling': {}, u'Email': {}, u'general-internet': {}},), is_leaf=True, yang_name="category", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='category-type', is_config=True)
    self.__icmp_code = YANGDynClass(base=unicode, is_leaf=True, yang_name="icmp-code", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__protocol_name = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IP': {}, u'ICMP': {}, u'TCP|UDP|SCTP': {}},), is_leaf=True, yang_name="protocol-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='protocol-type', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__icmp6_code = YANGDynClass(base=unicode, is_leaf=True, yang_name="icmp6-code", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__protocol_number = YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol-number", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__device_group = YANGDynClass(base=unicode, is_leaf=True, yang_name="device-group", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__app_protocol_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="app-protocol-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__icmp6_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="icmp6-type", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__icmp_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="icmp-type", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__source_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="source-port", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__dest_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="dest-port", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'virtual-devices', u'virtual-device', u'applications', u'application']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/name (string)

    YANG Description: string
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/name (string)
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


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/description (string)

    YANG Description: string
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="description", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_category(self):
    """
    Getter method for category, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/category (category-type)

    YANG Description: General
Web Access
File Access
Email
Network Services
Authentication
Remote Access
Tunneling
VoIP -Messaging and Other Applications
Web Proxy
business-systems
collaboration
general-internet
media
networking

    """
    return self.__category
      
  def _set_category(self, v, load=False):
    """
    Setter method for category, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/category (category-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_category is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_category() directly.

    YANG Description: General
Web Access
File Access
Email
Network Services
Authentication
Remote Access
Tunneling
VoIP -Messaging and Other Applications
Web Proxy
business-systems
collaboration
general-internet
media
networking

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Remote Access': {}, u'business-systems': {}, u'networking': {}, u'Web Access': {}, u'media': {}, u'Network Services': {}, u'VoIP -Messaging and Other Applications': {}, u'General': {}, u'collaboration': {}, u'Authentication': {}, u'Web Proxy': {}, u'File Access': {}, u'Tunneling': {}, u'Email': {}, u'general-internet': {}},), is_leaf=True, yang_name="category", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='category-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """category must be of a type compatible with category-type""",
          'defined-type': "firewall:category-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Remote Access': {}, u'business-systems': {}, u'networking': {}, u'Web Access': {}, u'media': {}, u'Network Services': {}, u'VoIP -Messaging and Other Applications': {}, u'General': {}, u'collaboration': {}, u'Authentication': {}, u'Web Proxy': {}, u'File Access': {}, u'Tunneling': {}, u'Email': {}, u'general-internet': {}},), is_leaf=True, yang_name="category", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='category-type', is_config=True)""",
        })

    self.__category = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_category(self):
    self.__category = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Remote Access': {}, u'business-systems': {}, u'networking': {}, u'Web Access': {}, u'media': {}, u'Network Services': {}, u'VoIP -Messaging and Other Applications': {}, u'General': {}, u'collaboration': {}, u'Authentication': {}, u'Web Proxy': {}, u'File Access': {}, u'Tunneling': {}, u'Email': {}, u'general-internet': {}},), is_leaf=True, yang_name="category", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='category-type', is_config=True)


  def _get_app_protocol_name(self):
    """
    Getter method for app_protocol_name, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/app_protocol_name (string)

    YANG Description: string
    """
    return self.__app_protocol_name
      
  def _set_app_protocol_name(self, v, load=False):
    """
    Setter method for app_protocol_name, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/app_protocol_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_app_protocol_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_app_protocol_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="app-protocol-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """app_protocol_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="app-protocol-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__app_protocol_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_app_protocol_name(self):
    self.__app_protocol_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="app-protocol-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_protocol_name(self):
    """
    Getter method for protocol_name, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/protocol_name (protocol-type)

    YANG Description: IP
TCP|UDP|SCTP
ICMP

    """
    return self.__protocol_name
      
  def _set_protocol_name(self, v, load=False):
    """
    Setter method for protocol_name, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/protocol_name (protocol-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol_name() directly.

    YANG Description: IP
TCP|UDP|SCTP
ICMP

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IP': {}, u'ICMP': {}, u'TCP|UDP|SCTP': {}},), is_leaf=True, yang_name="protocol-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='protocol-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol_name must be of a type compatible with protocol-type""",
          'defined-type': "firewall:protocol-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IP': {}, u'ICMP': {}, u'TCP|UDP|SCTP': {}},), is_leaf=True, yang_name="protocol-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='protocol-type', is_config=True)""",
        })

    self.__protocol_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol_name(self):
    self.__protocol_name = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IP': {}, u'ICMP': {}, u'TCP|UDP|SCTP': {}},), is_leaf=True, yang_name="protocol-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='protocol-type', is_config=True)


  def _get_protocol_number(self):
    """
    Getter method for protocol_number, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/protocol_number (string)

    YANG Description: string
    """
    return self.__protocol_number
      
  def _set_protocol_number(self, v, load=False):
    """
    Setter method for protocol_number, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/protocol_number (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol_number is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol_number() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="protocol-number", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol_number must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol-number", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__protocol_number = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol_number(self):
    self.__protocol_number = YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol-number", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_source_port(self):
    """
    Getter method for source_port, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/source_port (string)

    YANG Description: string
    """
    return self.__source_port
      
  def _set_source_port(self, v, load=False):
    """
    Setter method for source_port, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/source_port (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_port() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="source-port", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_port must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="source-port", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__source_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_port(self):
    self.__source_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="source-port", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_dest_port(self):
    """
    Getter method for dest_port, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/dest_port (string)

    YANG Description: string
    """
    return self.__dest_port
      
  def _set_dest_port(self, v, load=False):
    """
    Setter method for dest_port, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/dest_port (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dest_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dest_port() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="dest-port", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dest_port must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="dest-port", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__dest_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dest_port(self):
    self.__dest_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="dest-port", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_icmp_type(self):
    """
    Getter method for icmp_type, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/icmp_type (string)

    YANG Description: string
    """
    return self.__icmp_type
      
  def _set_icmp_type(self, v, load=False):
    """
    Setter method for icmp_type, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/icmp_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_icmp_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_icmp_type() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="icmp-type", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """icmp_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="icmp-type", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__icmp_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_icmp_type(self):
    self.__icmp_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="icmp-type", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_icmp_code(self):
    """
    Getter method for icmp_code, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/icmp_code (string)

    YANG Description: string
    """
    return self.__icmp_code
      
  def _set_icmp_code(self, v, load=False):
    """
    Setter method for icmp_code, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/icmp_code (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_icmp_code is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_icmp_code() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="icmp-code", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """icmp_code must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="icmp-code", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__icmp_code = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_icmp_code(self):
    self.__icmp_code = YANGDynClass(base=unicode, is_leaf=True, yang_name="icmp-code", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_icmp6_type(self):
    """
    Getter method for icmp6_type, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/icmp6_type (string)

    YANG Description: string
    """
    return self.__icmp6_type
      
  def _set_icmp6_type(self, v, load=False):
    """
    Setter method for icmp6_type, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/icmp6_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_icmp6_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_icmp6_type() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="icmp6-type", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """icmp6_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="icmp6-type", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__icmp6_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_icmp6_type(self):
    self.__icmp6_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="icmp6-type", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_icmp6_code(self):
    """
    Getter method for icmp6_code, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/icmp6_code (string)

    YANG Description: string
    """
    return self.__icmp6_code
      
  def _set_icmp6_code(self, v, load=False):
    """
    Setter method for icmp6_code, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/icmp6_code (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_icmp6_code is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_icmp6_code() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="icmp6-code", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """icmp6_code must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="icmp6-code", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__icmp6_code = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_icmp6_code(self):
    self.__icmp6_code = YANGDynClass(base=unicode, is_leaf=True, yang_name="icmp6-code", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)


  def _get_device_group(self):
    """
    Getter method for device_group, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/device_group (string)

    YANG Description: string
    """
    return self.__device_group
      
  def _set_device_group(self, v, load=False):
    """
    Setter method for device_group, mapped from YANG variable /devices/device/virtual_devices/virtual_device/applications/application/device_group (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_device_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_device_group() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="device-group", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """device_group must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="device-group", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__device_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_device_group(self):
    self.__device_group = YANGDynClass(base=unicode, is_leaf=True, yang_name="device-group", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  description = __builtin__.property(_get_description, _set_description)
  category = __builtin__.property(_get_category, _set_category)
  app_protocol_name = __builtin__.property(_get_app_protocol_name, _set_app_protocol_name)
  protocol_name = __builtin__.property(_get_protocol_name, _set_protocol_name)
  protocol_number = __builtin__.property(_get_protocol_number, _set_protocol_number)
  source_port = __builtin__.property(_get_source_port, _set_source_port)
  dest_port = __builtin__.property(_get_dest_port, _set_dest_port)
  icmp_type = __builtin__.property(_get_icmp_type, _set_icmp_type)
  icmp_code = __builtin__.property(_get_icmp_code, _set_icmp_code)
  icmp6_type = __builtin__.property(_get_icmp6_type, _set_icmp6_type)
  icmp6_code = __builtin__.property(_get_icmp6_code, _set_icmp6_code)
  device_group = __builtin__.property(_get_device_group, _set_device_group)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('description', description), ('category', category), ('app_protocol_name', app_protocol_name), ('protocol_name', protocol_name), ('protocol_number', protocol_number), ('source_port', source_port), ('dest_port', dest_port), ('icmp_type', icmp_type), ('icmp_code', icmp_code), ('icmp6_type', icmp6_type), ('icmp6_code', icmp6_code), ('device_group', device_group), ])


