
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
class test(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module test - based on the path /test. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__test',)

  _yang_name = 'test'
  _module_name = 'test'
  _namespace = 'http://anutanetworks.com/test'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__test = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="test", module_name="test", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/test', defining_module='test', yang_type='empty', is_config=True)

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
      return [u'test']

  def _get_test(self):
    """
    Getter method for test, mapped from YANG variable /test/test (empty)

    YANG Description: empty
    """
    return self.__test
      
  def _set_test(self, v, load=False):
    """
    Setter method for test, mapped from YANG variable /test/test (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_test is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_test() directly.

    YANG Description: empty
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="test", module_name="test", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/test', defining_module='test', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """test must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="test", module_name="test", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/test', defining_module='test', yang_type='empty', is_config=True)""",
        })

    self.__test = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_test(self):
    self.__test = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="test", module_name="test", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/test', defining_module='test', yang_type='empty', is_config=True)

  test = __builtin__.property(_get_test, _set_test)


  _pyangbind_elements = collections.OrderedDict([('test', test), ])


