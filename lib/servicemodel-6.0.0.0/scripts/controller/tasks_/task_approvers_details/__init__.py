
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
import task_approver_details
class task_approvers_details(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module tasks - based on the path /tasks/task-approvers-details. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__task_approver_details',)

  _yang_name = 'task-approvers-details'
  _module_name = 'tasks'
  _namespace = 'http://anutanetworks.com/tasks'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__task_approver_details = YANGDynClass(base=YANGListType("task_id",task_approver_details.task_approver_details, yang_name="task-approver-details", module_name="tasks", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='task-id'), is_container='list', yang_name="task-approver-details", module_name="tasks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/tasks', defining_module='tasks', yang_type='list', is_config=True)

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
      return [u'tasks', u'task-approvers-details']

  def _get_task_approver_details(self):
    """
    Getter method for task_approver_details, mapped from YANG variable /tasks/task_approvers_details/task_approver_details (list)
    """
    return self.__task_approver_details
      
  def _set_task_approver_details(self, v, load=False):
    """
    Setter method for task_approver_details, mapped from YANG variable /tasks/task_approvers_details/task_approver_details (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_task_approver_details is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_task_approver_details() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("task_id",task_approver_details.task_approver_details, yang_name="task-approver-details", module_name="tasks", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='task-id'), is_container='list', yang_name="task-approver-details", module_name="tasks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/tasks', defining_module='tasks', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """task_approver_details must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("task_id",task_approver_details.task_approver_details, yang_name="task-approver-details", module_name="tasks", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='task-id'), is_container='list', yang_name="task-approver-details", module_name="tasks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/tasks', defining_module='tasks', yang_type='list', is_config=True)""",
        })

    self.__task_approver_details = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_task_approver_details(self):
    self.__task_approver_details = YANGDynClass(base=YANGListType("task_id",task_approver_details.task_approver_details, yang_name="task-approver-details", module_name="tasks", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='task-id'), is_container='list', yang_name="task-approver-details", module_name="tasks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/tasks', defining_module='tasks', yang_type='list', is_config=True)

  task_approver_details = __builtin__.property(_get_task_approver_details, _set_task_approver_details)


  _pyangbind_elements = collections.OrderedDict([('task_approver_details', task_approver_details), ])


