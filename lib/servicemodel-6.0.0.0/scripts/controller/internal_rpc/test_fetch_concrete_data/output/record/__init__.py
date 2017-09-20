
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
class record(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module internal - based on the path /internal_rpc/test-fetch-concrete-data/output/record. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__property','__value',)

  _yang_name = 'record'
  _module_name = 'internal'
  _namespace = 'http://anutanetworks.com/internal'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__property = YANGDynClass(base=unicode, is_leaf=True, yang_name="property", module_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='http://anutanetworks.com/internal', defining_module='internal', yang_type='string', is_config=True)
    self.__value = YANGDynClass(base=unicode, is_leaf=True, yang_name="value", module_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/internal', defining_module='internal', yang_type='string', is_config=True)

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
      return [u'internal_rpc', u'test-fetch-concrete-data', u'output', u'record']

  def _get_property(self):
    """
    Getter method for property, mapped from YANG variable /internal_rpc/test_fetch_concrete_data/output/record/property (string)

    YANG Description: string
    """
    return self.__property
      
  def _set_property(self, v, load=False):
    """
    Setter method for property, mapped from YANG variable /internal_rpc/test_fetch_concrete_data/output/record/property (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_property is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_property() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="property", module_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='http://anutanetworks.com/internal', defining_module='internal', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """property must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="property", module_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='http://anutanetworks.com/internal', defining_module='internal', yang_type='string', is_config=True)""",
        })

    self.__property = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_property(self):
    self.__property = YANGDynClass(base=unicode, is_leaf=True, yang_name="property", module_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='http://anutanetworks.com/internal', defining_module='internal', yang_type='string', is_config=True)


  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /internal_rpc/test_fetch_concrete_data/output/record/value (string)

    YANG Description: string
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /internal_rpc/test_fetch_concrete_data/output/record/value (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="value", module_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/internal', defining_module='internal', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="value", module_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/internal', defining_module='internal', yang_type='string', is_config=True)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=unicode, is_leaf=True, yang_name="value", module_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/internal', defining_module='internal', yang_type='string', is_config=True)

  property = __builtin__.property(_get_property, _set_property)
  value = __builtin__.property(_get_value, _set_value)


  _pyangbind_elements = collections.OrderedDict([('property', property), ('value', value), ])


