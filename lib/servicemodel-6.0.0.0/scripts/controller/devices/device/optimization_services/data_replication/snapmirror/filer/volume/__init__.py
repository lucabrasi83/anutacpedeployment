
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
class volume(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/optimization-services/data-replication/snapmirror/filer/volume. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__volume','__description','__policy','__priority',)

  _yang_name = 'volume'
  _module_name = 'wanoptimizer'
  _namespace = 'http://anutanetworks.com/wanoptimizer'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__volume = YANGDynClass(base=unicode, is_leaf=True, yang_name="volume", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='string', is_config=True)
    self.__policy = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'filer-default': {}, u'sdr-default': {}, u'lz-only': {}, u'none': {}},), is_leaf=True, yang_name="policy", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='enumeration', is_config=True)
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='string', is_config=True)
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'1': {}, u'0': {}, u'3': {}, u'2': {}, u'4': {}, u'254': {}, u'255': {}},), is_leaf=True, yang_name="priority", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='enumeration', is_config=True)

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
      return [u'devices', u'device', u'optimization-services', u'data-replication', u'snapmirror', u'filer', u'volume']

  def _get_volume(self):
    """
    Getter method for volume, mapped from YANG variable /devices/device/optimization_services/data_replication/snapmirror/filer/volume/volume (string)

    YANG Description: Volume
    """
    return self.__volume
      
  def _set_volume(self, v, load=False):
    """
    Setter method for volume, mapped from YANG variable /devices/device/optimization_services/data_replication/snapmirror/filer/volume/volume (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_volume is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_volume() directly.

    YANG Description: Volume
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="volume", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """volume must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="volume", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='string', is_config=True)""",
        })

    self.__volume = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_volume(self):
    self.__volume = YANGDynClass(base=unicode, is_leaf=True, yang_name="volume", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='string', is_config=True)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /devices/device/optimization_services/data_replication/snapmirror/filer/volume/description (string)

    YANG Description: Description
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /devices/device/optimization_services/data_replication/snapmirror/filer/volume/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: Description
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="description", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='string', is_config=True)


  def _get_policy(self):
    """
    Getter method for policy, mapped from YANG variable /devices/device/optimization_services/data_replication/snapmirror/filer/volume/policy (enumeration)

    YANG Description: sdr-default
lz-only
filer-default
none

    """
    return self.__policy
      
  def _set_policy(self, v, load=False):
    """
    Setter method for policy, mapped from YANG variable /devices/device/optimization_services/data_replication/snapmirror/filer/volume/policy (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policy() directly.

    YANG Description: sdr-default
lz-only
filer-default
none

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'filer-default': {}, u'sdr-default': {}, u'lz-only': {}, u'none': {}},), is_leaf=True, yang_name="policy", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policy must be of a type compatible with enumeration""",
          'defined-type': "wanoptimizer:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'filer-default': {}, u'sdr-default': {}, u'lz-only': {}, u'none': {}},), is_leaf=True, yang_name="policy", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='enumeration', is_config=True)""",
        })

    self.__policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policy(self):
    self.__policy = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'filer-default': {}, u'sdr-default': {}, u'lz-only': {}, u'none': {}},), is_leaf=True, yang_name="policy", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='enumeration', is_config=True)


  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /devices/device/optimization_services/data_replication/snapmirror/filer/volume/priority (enumeration)

    YANG Description: highest-0,high-1,medium-2,low-3,lowest-4,none-255
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /devices/device/optimization_services/data_replication/snapmirror/filer/volume/priority (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: highest-0,high-1,medium-2,low-3,lowest-4,none-255
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'1': {}, u'0': {}, u'3': {}, u'2': {}, u'4': {}, u'254': {}, u'255': {}},), is_leaf=True, yang_name="priority", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with enumeration""",
          'defined-type': "wanoptimizer:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'1': {}, u'0': {}, u'3': {}, u'2': {}, u'4': {}, u'254': {}, u'255': {}},), is_leaf=True, yang_name="priority", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='enumeration', is_config=True)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'1': {}, u'0': {}, u'3': {}, u'2': {}, u'4': {}, u'254': {}, u'255': {}},), is_leaf=True, yang_name="priority", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='enumeration', is_config=True)

  volume = __builtin__.property(_get_volume, _set_volume)
  description = __builtin__.property(_get_description, _set_description)
  policy = __builtin__.property(_get_policy, _set_policy)
  priority = __builtin__.property(_get_priority, _set_priority)


  _pyangbind_elements = collections.OrderedDict([('volume', volume), ('description', description), ('policy', policy), ('priority', priority), ])


