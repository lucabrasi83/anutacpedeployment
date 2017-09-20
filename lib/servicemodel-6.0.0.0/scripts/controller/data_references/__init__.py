
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
import data_reference
class data_references(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /data-references. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__data_reference',)

  _yang_name = 'data-references'
  _module_name = 'controller'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__data_reference = YANGDynClass(base=YANGListType("rcpath taskId",data_reference.data_reference, yang_name="data-reference", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rcpath taskId'), is_container='list', yang_name="data-reference", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)

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
      return [u'data-references']

  def _get_data_reference(self):
    """
    Getter method for data_reference, mapped from YANG variable /data_references/data_reference (list)
    """
    return self.__data_reference
      
  def _set_data_reference(self, v, load=False):
    """
    Setter method for data_reference, mapped from YANG variable /data_references/data_reference (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_reference is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_reference() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("rcpath taskId",data_reference.data_reference, yang_name="data-reference", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rcpath taskId'), is_container='list', yang_name="data-reference", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_reference must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("rcpath taskId",data_reference.data_reference, yang_name="data-reference", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rcpath taskId'), is_container='list', yang_name="data-reference", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)""",
        })

    self.__data_reference = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_reference(self):
    self.__data_reference = YANGDynClass(base=YANGListType("rcpath taskId",data_reference.data_reference, yang_name="data-reference", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rcpath taskId'), is_container='list', yang_name="data-reference", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)

  data_reference = __builtin__.property(_get_data_reference, _set_data_reference)


  _pyangbind_elements = collections.OrderedDict([('data_reference', data_reference), ])


