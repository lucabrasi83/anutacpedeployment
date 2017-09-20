
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
class vss_chassi(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /system/tables/vss-chassis/vss-chassi. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__vss_chassi_id','__active_switchnumber','__standby_switchNumber','__device_name','__isVss',)

  _yang_name = 'vss-chassi'
  _module_name = 'system'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__active_switchnumber = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="active-switchnumber", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int32', is_config=True)
    self.__device_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="device-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)
    self.__isVss = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isVss", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    self.__standby_switchNumber = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="standby-switchNumber", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int32', is_config=True)
    self.__vss_chassi_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="vss-chassi-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

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
      return [u'system', u'tables', u'vss-chassis', u'vss-chassi']

  def _get_vss_chassi_id(self):
    """
    Getter method for vss_chassi_id, mapped from YANG variable /system/tables/vss_chassis/vss_chassi/vss_chassi_id (string)

    YANG Description: string
    """
    return self.__vss_chassi_id
      
  def _set_vss_chassi_id(self, v, load=False):
    """
    Setter method for vss_chassi_id, mapped from YANG variable /system/tables/vss_chassis/vss_chassi/vss_chassi_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vss_chassi_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vss_chassi_id() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vss-chassi-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vss_chassi_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vss-chassi-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__vss_chassi_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vss_chassi_id(self):
    self.__vss_chassi_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="vss-chassi-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_active_switchnumber(self):
    """
    Getter method for active_switchnumber, mapped from YANG variable /system/tables/vss_chassis/vss_chassi/active_switchnumber (int32)

    YANG Description: -2147483648..2147483647
    """
    return self.__active_switchnumber
      
  def _set_active_switchnumber(self, v, load=False):
    """
    Setter method for active_switchnumber, mapped from YANG variable /system/tables/vss_chassis/vss_chassi/active_switchnumber (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_active_switchnumber is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_active_switchnumber() directly.

    YANG Description: -2147483648..2147483647
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="active-switchnumber", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """active_switchnumber must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="active-switchnumber", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int32', is_config=True)""",
        })

    self.__active_switchnumber = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_active_switchnumber(self):
    self.__active_switchnumber = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="active-switchnumber", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int32', is_config=True)


  def _get_standby_switchNumber(self):
    """
    Getter method for standby_switchNumber, mapped from YANG variable /system/tables/vss_chassis/vss_chassi/standby_switchNumber (int32)

    YANG Description: -2147483648..2147483647
    """
    return self.__standby_switchNumber
      
  def _set_standby_switchNumber(self, v, load=False):
    """
    Setter method for standby_switchNumber, mapped from YANG variable /system/tables/vss_chassis/vss_chassi/standby_switchNumber (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_standby_switchNumber is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_standby_switchNumber() directly.

    YANG Description: -2147483648..2147483647
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="standby-switchNumber", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """standby_switchNumber must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="standby-switchNumber", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int32', is_config=True)""",
        })

    self.__standby_switchNumber = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_standby_switchNumber(self):
    self.__standby_switchNumber = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="standby-switchNumber", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='int32', is_config=True)


  def _get_device_name(self):
    """
    Getter method for device_name, mapped from YANG variable /system/tables/vss_chassis/vss_chassi/device_name (leafref)

    YANG Description: device-name
    """
    return self.__device_name
      
  def _set_device_name(self, v, load=False):
    """
    Setter method for device_name, mapped from YANG variable /system/tables/vss_chassis/vss_chassi/device_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_device_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_device_name() directly.

    YANG Description: device-name
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="device-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """device_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="device-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)""",
        })

    self.__device_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_device_name(self):
    self.__device_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="device-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)


  def _get_isVss(self):
    """
    Getter method for isVss, mapped from YANG variable /system/tables/vss_chassis/vss_chassi/isVss (boolean)

    YANG Description: isVss: True/False
    """
    return self.__isVss
      
  def _set_isVss(self, v, load=False):
    """
    Setter method for isVss, mapped from YANG variable /system/tables/vss_chassis/vss_chassi/isVss (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isVss is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isVss() directly.

    YANG Description: isVss: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="isVss", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isVss must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isVss", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)""",
        })

    self.__isVss = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isVss(self):
    self.__isVss = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isVss", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)

  vss_chassi_id = __builtin__.property(_get_vss_chassi_id, _set_vss_chassi_id)
  active_switchnumber = __builtin__.property(_get_active_switchnumber, _set_active_switchnumber)
  standby_switchNumber = __builtin__.property(_get_standby_switchNumber, _set_standby_switchNumber)
  device_name = __builtin__.property(_get_device_name, _set_device_name)
  isVss = __builtin__.property(_get_isVss, _set_isVss)


  _pyangbind_elements = collections.OrderedDict([('vss_chassi_id', vss_chassi_id), ('active_switchnumber', active_switchnumber), ('standby_switchNumber', standby_switchNumber), ('device_name', device_name), ('isVss', isVss), ])


