
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
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /controller_rpc/show-device-config/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__result',)

  _yang_name = 'output'
  _module_name = 'controller'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__result = YANGDynClass(base=unicode, is_leaf=True, yang_name="result", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

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
      return [u'controller_rpc', u'show-device-config', u'output']

  def _get_result(self):
    """
    Getter method for result, mapped from YANG variable /controller_rpc/show_device_config/output/result (string)

    YANG Description: string
    """
    return self.__result
      
  def _set_result(self, v, load=False):
    """
    Setter method for result, mapped from YANG variable /controller_rpc/show_device_config/output/result (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_result is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_result() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="result", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """result must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="result", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__result = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_result(self):
    self.__result = YANGDynClass(base=unicode, is_leaf=True, yang_name="result", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

  result = __builtin__.property(_get_result, _set_result)


  _pyangbind_elements = collections.OrderedDict([('result', result), ])


