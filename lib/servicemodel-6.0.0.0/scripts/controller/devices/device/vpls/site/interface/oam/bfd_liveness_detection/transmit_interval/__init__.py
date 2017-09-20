
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
class transmit_interval(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/vpls/site/interface/oam/bfd-liveness-detection/transmit-interval. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Transmit-interval options
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__minimum_interval','__threshold',)

  _yang_name = 'transmit-interval'
  _module_name = 'vpls'
  _namespace = 'http://anutanetworks.com/vpls'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__threshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="threshold", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)
    self.__minimum_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 255000']}), is_leaf=True, yang_name="minimum-interval", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)

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
      return [u'devices', u'device', u'vpls', u'site', u'interface', u'oam', u'bfd-liveness-detection', u'transmit-interval']

  def _get_minimum_interval(self):
    """
    Getter method for minimum_interval, mapped from YANG variable /devices/device/vpls/site/interface/oam/bfd_liveness_detection/transmit_interval/minimum_interval (uint32)

    YANG Description: Minimum transmit interval
    """
    return self.__minimum_interval
      
  def _set_minimum_interval(self, v, load=False):
    """
    Setter method for minimum_interval, mapped from YANG variable /devices/device/vpls/site/interface/oam/bfd_liveness_detection/transmit_interval/minimum_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_minimum_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_minimum_interval() directly.

    YANG Description: Minimum transmit interval
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 255000']}), is_leaf=True, yang_name="minimum-interval", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """minimum_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 255000']}), is_leaf=True, yang_name="minimum-interval", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)""",
        })

    self.__minimum_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_minimum_interval(self):
    self.__minimum_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 255000']}), is_leaf=True, yang_name="minimum-interval", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)


  def _get_threshold(self):
    """
    Getter method for threshold, mapped from YANG variable /devices/device/vpls/site/interface/oam/bfd_liveness_detection/transmit_interval/threshold (uint32)

    YANG Description: High transmit interval triggering a trap
    """
    return self.__threshold
      
  def _set_threshold(self, v, load=False):
    """
    Setter method for threshold, mapped from YANG variable /devices/device/vpls/site/interface/oam/bfd_liveness_detection/transmit_interval/threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_threshold() directly.

    YANG Description: High transmit interval triggering a trap
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="threshold", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="threshold", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)""",
        })

    self.__threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_threshold(self):
    self.__threshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="threshold", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)

  minimum_interval = __builtin__.property(_get_minimum_interval, _set_minimum_interval)
  threshold = __builtin__.property(_get_threshold, _set_threshold)


  _pyangbind_elements = collections.OrderedDict([('minimum_interval', minimum_interval), ('threshold', threshold), ])


