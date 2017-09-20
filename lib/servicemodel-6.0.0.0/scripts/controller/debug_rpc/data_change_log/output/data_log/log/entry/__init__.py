
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
class entry(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module debug - based on the path /debug_rpc/data-change-log/output/data-log/log/entry. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__id','__rcpath','__task_id','__owner','__what_happened','__previous_value','__current_value','__mfd','__responsible_party',)

  _yang_name = 'entry'
  _module_name = 'debug'
  _namespace = 'http://anutanetworks.com/debug'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mfd = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mfd", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='boolean', is_config=True)
    self.__task_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="task-id", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)
    self.__what_happened = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deleted': {}, u'updated': {}, u'created': {}},), is_leaf=True, yang_name="what-happened", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='data-change-type-enum', is_config=True)
    self.__current_value = YANGDynClass(base=unicode, is_leaf=True, yang_name="current-value", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='pcdata', is_config=True)
    self.__responsible_party = YANGDynClass(base=unicode, is_leaf=True, yang_name="responsible-party", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)
    self.__owner = YANGDynClass(base=unicode, is_leaf=True, yang_name="owner", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)
    self.__previous_value = YANGDynClass(base=unicode, is_leaf=True, yang_name="previous-value", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='pcdata', is_config=True)
    self.__id = YANGDynClass(base=unicode, is_leaf=True, yang_name="id", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)
    self.__rcpath = YANGDynClass(base=unicode, is_leaf=True, yang_name="rcpath", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='pcdata', is_config=True)

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
      return [u'debug_rpc', u'data-change-log', u'output', u'data-log', u'log', u'entry']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/id (string)

    YANG Description: string
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="id", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="id", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=unicode, is_leaf=True, yang_name="id", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)


  def _get_rcpath(self):
    """
    Getter method for rcpath, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/rcpath (pcdata)

    YANG Description: string
    """
    return self.__rcpath
      
  def _set_rcpath(self, v, load=False):
    """
    Setter method for rcpath, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/rcpath (pcdata)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rcpath is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rcpath() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="rcpath", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='pcdata', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rcpath must be of a type compatible with pcdata""",
          'defined-type': "debug:pcdata",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="rcpath", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='pcdata', is_config=True)""",
        })

    self.__rcpath = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rcpath(self):
    self.__rcpath = YANGDynClass(base=unicode, is_leaf=True, yang_name="rcpath", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='pcdata', is_config=True)


  def _get_task_id(self):
    """
    Getter method for task_id, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/task_id (string)

    YANG Description: string
    """
    return self.__task_id
      
  def _set_task_id(self, v, load=False):
    """
    Setter method for task_id, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/task_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_task_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_task_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="task-id", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """task_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="task-id", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)""",
        })

    self.__task_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_task_id(self):
    self.__task_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="task-id", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)


  def _get_owner(self):
    """
    Getter method for owner, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/owner (string)

    YANG Description: string
    """
    return self.__owner
      
  def _set_owner(self, v, load=False):
    """
    Setter method for owner, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/owner (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_owner is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_owner() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="owner", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """owner must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="owner", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)""",
        })

    self.__owner = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_owner(self):
    self.__owner = YANGDynClass(base=unicode, is_leaf=True, yang_name="owner", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)


  def _get_what_happened(self):
    """
    Getter method for what_happened, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/what_happened (data-change-type-enum)

    YANG Description: created
updated
deleted

    """
    return self.__what_happened
      
  def _set_what_happened(self, v, load=False):
    """
    Setter method for what_happened, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/what_happened (data-change-type-enum)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_what_happened is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_what_happened() directly.

    YANG Description: created
updated
deleted

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deleted': {}, u'updated': {}, u'created': {}},), is_leaf=True, yang_name="what-happened", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='data-change-type-enum', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """what_happened must be of a type compatible with data-change-type-enum""",
          'defined-type': "debug:data-change-type-enum",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deleted': {}, u'updated': {}, u'created': {}},), is_leaf=True, yang_name="what-happened", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='data-change-type-enum', is_config=True)""",
        })

    self.__what_happened = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_what_happened(self):
    self.__what_happened = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deleted': {}, u'updated': {}, u'created': {}},), is_leaf=True, yang_name="what-happened", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='data-change-type-enum', is_config=True)


  def _get_previous_value(self):
    """
    Getter method for previous_value, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/previous_value (pcdata)

    YANG Description: string
    """
    return self.__previous_value
      
  def _set_previous_value(self, v, load=False):
    """
    Setter method for previous_value, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/previous_value (pcdata)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_previous_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_previous_value() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="previous-value", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='pcdata', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """previous_value must be of a type compatible with pcdata""",
          'defined-type': "debug:pcdata",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="previous-value", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='pcdata', is_config=True)""",
        })

    self.__previous_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_previous_value(self):
    self.__previous_value = YANGDynClass(base=unicode, is_leaf=True, yang_name="previous-value", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='pcdata', is_config=True)


  def _get_current_value(self):
    """
    Getter method for current_value, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/current_value (pcdata)

    YANG Description: string
    """
    return self.__current_value
      
  def _set_current_value(self, v, load=False):
    """
    Setter method for current_value, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/current_value (pcdata)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_current_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_current_value() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="current-value", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='pcdata', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """current_value must be of a type compatible with pcdata""",
          'defined-type': "debug:pcdata",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="current-value", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='pcdata', is_config=True)""",
        })

    self.__current_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_current_value(self):
    self.__current_value = YANGDynClass(base=unicode, is_leaf=True, yang_name="current-value", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='pcdata', is_config=True)


  def _get_mfd(self):
    """
    Getter method for mfd, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/mfd (boolean)

    YANG Description: mfd: True/False
    """
    return self.__mfd
      
  def _set_mfd(self, v, load=False):
    """
    Setter method for mfd, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/mfd (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mfd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mfd() directly.

    YANG Description: mfd: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mfd", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mfd must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mfd", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='boolean', is_config=True)""",
        })

    self.__mfd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mfd(self):
    self.__mfd = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mfd", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='boolean', is_config=True)


  def _get_responsible_party(self):
    """
    Getter method for responsible_party, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/responsible_party (string)

    YANG Description: some identifier that can pin point which component of the server or client 
                                     responsible for the data change. Apart from data changes originating from a client payloads, there may be 
                                     other components in the system that will cause changes.
    """
    return self.__responsible_party
      
  def _set_responsible_party(self, v, load=False):
    """
    Setter method for responsible_party, mapped from YANG variable /debug_rpc/data_change_log/output/data_log/log/entry/responsible_party (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_responsible_party is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_responsible_party() directly.

    YANG Description: some identifier that can pin point which component of the server or client 
                                     responsible for the data change. Apart from data changes originating from a client payloads, there may be 
                                     other components in the system that will cause changes.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="responsible-party", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """responsible_party must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="responsible-party", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)""",
        })

    self.__responsible_party = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_responsible_party(self):
    self.__responsible_party = YANGDynClass(base=unicode, is_leaf=True, yang_name="responsible-party", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='string', is_config=True)

  id = __builtin__.property(_get_id, _set_id)
  rcpath = __builtin__.property(_get_rcpath, _set_rcpath)
  task_id = __builtin__.property(_get_task_id, _set_task_id)
  owner = __builtin__.property(_get_owner, _set_owner)
  what_happened = __builtin__.property(_get_what_happened, _set_what_happened)
  previous_value = __builtin__.property(_get_previous_value, _set_previous_value)
  current_value = __builtin__.property(_get_current_value, _set_current_value)
  mfd = __builtin__.property(_get_mfd, _set_mfd)
  responsible_party = __builtin__.property(_get_responsible_party, _set_responsible_party)


  _pyangbind_elements = collections.OrderedDict([('id', id), ('rcpath', rcpath), ('task_id', task_id), ('owner', owner), ('what_happened', what_happened), ('previous_value', previous_value), ('current_value', current_value), ('mfd', mfd), ('responsible_party', responsible_party), ])


