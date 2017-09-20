
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
  from YANG module packages - based on the path /packages_rpc/delete-package/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__task_id',)

  _yang_name = 'output'
  _module_name = 'packages'
  _namespace = 'http://anutanetworks.com/packages'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__task_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="task-id", module_name="packages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/packages', defining_module='packages', yang_type='string', is_config=True)

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
      return [u'packages_rpc', u'delete-package', u'output']

  def _get_task_id(self):
    """
    Getter method for task_id, mapped from YANG variable /packages_rpc/delete_package/output/task_id (string)

    YANG Description: string
    """
    return self.__task_id
      
  def _set_task_id(self, v, load=False):
    """
    Setter method for task_id, mapped from YANG variable /packages_rpc/delete_package/output/task_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_task_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_task_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="task-id", module_name="packages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/packages', defining_module='packages', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """task_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="task-id", module_name="packages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/packages', defining_module='packages', yang_type='string', is_config=True)""",
        })

    self.__task_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_task_id(self):
    self.__task_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="task-id", module_name="packages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/packages', defining_module='packages', yang_type='string', is_config=True)

  task_id = __builtin__.property(_get_task_id, _set_task_id)


  _pyangbind_elements = collections.OrderedDict([('task_id', task_id), ])


