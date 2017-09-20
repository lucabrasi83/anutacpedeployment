
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
import output
class list_active_packages(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module packages - based on the path /packages_rpc/list-active-packages. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Lists all the known versions of specified package and which one is currently active, if active.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__output',)

  _yang_name = 'list-active-packages'
  _module_name = 'packages'
  _namespace = 'http://anutanetworks.com/packages'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__output = YANGDynClass(base=output.output, is_leaf=True, yang_name="output", module_name="packages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/packages', defining_module='packages', yang_type='output', is_config=True)

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
      return [u'packages_rpc', u'list-active-packages']

  def _get_output(self):
    """
    Getter method for output, mapped from YANG variable /packages_rpc/list_active_packages/output (output)
    """
    return self.__output
      
  def _set_output(self, v, load=False):
    """
    Setter method for output, mapped from YANG variable /packages_rpc/list_active_packages/output (output)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_output is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_output() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=output.output, is_leaf=True, yang_name="output", module_name="packages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/packages', defining_module='packages', yang_type='output', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """output must be of a type compatible with output""",
          'defined-type': "packages:output",
          'generated-type': """YANGDynClass(base=output.output, is_leaf=True, yang_name="output", module_name="packages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/packages', defining_module='packages', yang_type='output', is_config=True)""",
        })

    self.__output = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_output(self):
    self.__output = YANGDynClass(base=output.output, is_leaf=True, yang_name="output", module_name="packages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/packages', defining_module='packages', yang_type='output', is_config=True)

  output = __builtin__.property(_get_output, _set_output)


  _pyangbind_elements = collections.OrderedDict([('output', output), ])


