
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
class log_receivers(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module logging - based on the path /settings/log-receivers. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__host','__port','__active','__level','__format',)

  _yang_name = 'log-receivers'
  _module_name = 'logging'
  _namespace = 'http://anutanetworks.com/logging'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="active", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='boolean', is_config=True)
    self.__host = YANGDynClass(base=unicode, is_leaf=True, yang_name="host", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='string', is_config=True)
    self.__format = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Syslog': {}, u'JSON': {}},), is_leaf=True, yang_name="format", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='enumeration', is_config=True)
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=int,restriction_dict={'range': ['-32768..32767']}, int_size=16), is_leaf=True, yang_name="port", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='int16', is_config=True)
    self.__level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'WARN': {}, u'DEBUG': {}, u'TRACE': {}, u'INFO': {}, u'ERROR': {}},), is_leaf=True, yang_name="level", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='enumeration', is_config=True)

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
      return [u'settings', u'log-receivers']

  def _get_host(self):
    """
    Getter method for host, mapped from YANG variable /settings/log_receivers/host (string)

    YANG Description: Host of the Log receiving Server
    """
    return self.__host
      
  def _set_host(self, v, load=False):
    """
    Setter method for host, mapped from YANG variable /settings/log_receivers/host (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host() directly.

    YANG Description: Host of the Log receiving Server
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="host", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="host", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='string', is_config=True)""",
        })

    self.__host = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host(self):
    self.__host = YANGDynClass(base=unicode, is_leaf=True, yang_name="host", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='string', is_config=True)


  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /settings/log_receivers/port (int16)

    YANG Description: Port of the Log receiving Server
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /settings/log_receivers/port (int16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.

    YANG Description: Port of the Log receiving Server
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int,restriction_dict={'range': ['-32768..32767']}, int_size=16), is_leaf=True, yang_name="port", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='int16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with int16""",
          'defined-type': "int16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int,restriction_dict={'range': ['-32768..32767']}, int_size=16), is_leaf=True, yang_name="port", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='int16', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=int,restriction_dict={'range': ['-32768..32767']}, int_size=16), is_leaf=True, yang_name="port", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='int16', is_config=True)


  def _get_active(self):
    """
    Getter method for active, mapped from YANG variable /settings/log_receivers/active (boolean)

    YANG Description: Active if enabled
    """
    return self.__active
      
  def _set_active(self, v, load=False):
    """
    Setter method for active, mapped from YANG variable /settings/log_receivers/active (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_active is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_active() directly.

    YANG Description: Active if enabled
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="active", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """active must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="active", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='boolean', is_config=True)""",
        })

    self.__active = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_active(self):
    self.__active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="active", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='boolean', is_config=True)


  def _get_level(self):
    """
    Getter method for level, mapped from YANG variable /settings/log_receivers/level (enumeration)

    YANG Description: Level of logging
    """
    return self.__level
      
  def _set_level(self, v, load=False):
    """
    Setter method for level, mapped from YANG variable /settings/log_receivers/level (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level() directly.

    YANG Description: Level of logging
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'WARN': {}, u'DEBUG': {}, u'TRACE': {}, u'INFO': {}, u'ERROR': {}},), is_leaf=True, yang_name="level", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level must be of a type compatible with enumeration""",
          'defined-type': "logging:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'WARN': {}, u'DEBUG': {}, u'TRACE': {}, u'INFO': {}, u'ERROR': {}},), is_leaf=True, yang_name="level", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='enumeration', is_config=True)""",
        })

    self.__level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level(self):
    self.__level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'WARN': {}, u'DEBUG': {}, u'TRACE': {}, u'INFO': {}, u'ERROR': {}},), is_leaf=True, yang_name="level", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='enumeration', is_config=True)


  def _get_format(self):
    """
    Getter method for format, mapped from YANG variable /settings/log_receivers/format (enumeration)

    YANG Description: Logging layout
    """
    return self.__format
      
  def _set_format(self, v, load=False):
    """
    Setter method for format, mapped from YANG variable /settings/log_receivers/format (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_format is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_format() directly.

    YANG Description: Logging layout
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Syslog': {}, u'JSON': {}},), is_leaf=True, yang_name="format", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """format must be of a type compatible with enumeration""",
          'defined-type': "logging:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Syslog': {}, u'JSON': {}},), is_leaf=True, yang_name="format", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='enumeration', is_config=True)""",
        })

    self.__format = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_format(self):
    self.__format = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Syslog': {}, u'JSON': {}},), is_leaf=True, yang_name="format", module_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/logging', defining_module='logging', yang_type='enumeration', is_config=True)

  host = __builtin__.property(_get_host, _set_host)
  port = __builtin__.property(_get_port, _set_port)
  active = __builtin__.property(_get_active, _set_active)
  level = __builtin__.property(_get_level, _set_level)
  format = __builtin__.property(_get_format, _set_format)


  _pyangbind_elements = collections.OrderedDict([('host', host), ('port', port), ('active', active), ('level', level), ('format', format), ])


