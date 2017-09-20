
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
class clock(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/clock. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__timezone','__hours','__minutes','__summer_time',)

  _yang_name = 'clock'
  _module_name = 'basicDeviceConfigs'
  _namespace = 'http://anutanetworks.com/basicDeviceConfigs'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__hours = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="hours", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='int32', is_config=True)
    self.__timezone = YANGDynClass(base=unicode, is_leaf=True, yang_name="timezone", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    self.__minutes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="minutes", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='int32', is_config=True)
    self.__summer_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="summer-time", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'clock']

  def _get_timezone(self):
    """
    Getter method for timezone, mapped from YANG variable /devices/device/clock/timezone (string)

    YANG Description: string
    """
    return self.__timezone
      
  def _set_timezone(self, v, load=False):
    """
    Setter method for timezone, mapped from YANG variable /devices/device/clock/timezone (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timezone is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timezone() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="timezone", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timezone must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="timezone", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)""",
        })

    self.__timezone = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timezone(self):
    self.__timezone = YANGDynClass(base=unicode, is_leaf=True, yang_name="timezone", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)


  def _get_hours(self):
    """
    Getter method for hours, mapped from YANG variable /devices/device/clock/hours (int32)

    YANG Description: -2147483648..2147483647
    """
    return self.__hours
      
  def _set_hours(self, v, load=False):
    """
    Setter method for hours, mapped from YANG variable /devices/device/clock/hours (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hours is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hours() directly.

    YANG Description: -2147483648..2147483647
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="hours", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hours must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="hours", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='int32', is_config=True)""",
        })

    self.__hours = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hours(self):
    self.__hours = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="hours", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='int32', is_config=True)


  def _get_minutes(self):
    """
    Getter method for minutes, mapped from YANG variable /devices/device/clock/minutes (int32)

    YANG Description: -2147483648..2147483647
    """
    return self.__minutes
      
  def _set_minutes(self, v, load=False):
    """
    Setter method for minutes, mapped from YANG variable /devices/device/clock/minutes (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_minutes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_minutes() directly.

    YANG Description: -2147483648..2147483647
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="minutes", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """minutes must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="minutes", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='int32', is_config=True)""",
        })

    self.__minutes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_minutes(self):
    self.__minutes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="minutes", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='int32', is_config=True)


  def _get_summer_time(self):
    """
    Getter method for summer_time, mapped from YANG variable /devices/device/clock/summer_time (string)

    YANG Description: string
    """
    return self.__summer_time
      
  def _set_summer_time(self, v, load=False):
    """
    Setter method for summer_time, mapped from YANG variable /devices/device/clock/summer_time (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summer_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summer_time() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="summer-time", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summer_time must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="summer-time", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)""",
        })

    self.__summer_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summer_time(self):
    self.__summer_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="summer-time", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)

  timezone = __builtin__.property(_get_timezone, _set_timezone)
  hours = __builtin__.property(_get_hours, _set_hours)
  minutes = __builtin__.property(_get_minutes, _set_minutes)
  summer_time = __builtin__.property(_get_summer_time, _set_summer_time)


  _pyangbind_elements = collections.OrderedDict([('timezone', timezone), ('hours', hours), ('minutes', minutes), ('summer_time', summer_time), ])


