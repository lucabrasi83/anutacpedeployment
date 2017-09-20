
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
import added_properties
import removed_properties
class schema_diff_item(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /migrations/migrations/migration-task/upgrade-analysis/schema-diff/schema-diff-item. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__schema_path','__diff_type','__added_properties','__removed_properties',)

  _yang_name = 'schema-diff-item'
  _module_name = 'migration'
  _namespace = 'http://anutanetworks.com/migration'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__diff_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'CREATE': {}, u'UPDATE': {}, u'DELETE': {}},), is_leaf=True, yang_name="diff-type", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='diff-type', is_config=True)
    self.__schema_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="schema-path", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)
    self.__added_properties = YANGDynClass(base=added_properties.added_properties, is_container='container', yang_name="added-properties", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='container', is_config=True)
    self.__removed_properties = YANGDynClass(base=removed_properties.removed_properties, is_container='container', yang_name="removed-properties", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='container', is_config=True)

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
      return [u'migrations', u'migrations', u'migration-task', u'upgrade-analysis', u'schema-diff', u'schema-diff-item']

  def _get_schema_path(self):
    """
    Getter method for schema_path, mapped from YANG variable /migrations/migrations/migration_task/upgrade_analysis/schema_diff/schema_diff_item/schema_path (string)

    YANG Description: string
    """
    return self.__schema_path
      
  def _set_schema_path(self, v, load=False):
    """
    Setter method for schema_path, mapped from YANG variable /migrations/migrations/migration_task/upgrade_analysis/schema_diff/schema_diff_item/schema_path (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_schema_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_schema_path() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="schema-path", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """schema_path must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="schema-path", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)""",
        })

    self.__schema_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_schema_path(self):
    self.__schema_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="schema-path", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)


  def _get_diff_type(self):
    """
    Getter method for diff_type, mapped from YANG variable /migrations/migrations/migration_task/upgrade_analysis/schema_diff/schema_diff_item/diff_type (diff-type)

    YANG Description: CREATE
UPDATE
DELETE

    """
    return self.__diff_type
      
  def _set_diff_type(self, v, load=False):
    """
    Setter method for diff_type, mapped from YANG variable /migrations/migrations/migration_task/upgrade_analysis/schema_diff/schema_diff_item/diff_type (diff-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_diff_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_diff_type() directly.

    YANG Description: CREATE
UPDATE
DELETE

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'CREATE': {}, u'UPDATE': {}, u'DELETE': {}},), is_leaf=True, yang_name="diff-type", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='diff-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """diff_type must be of a type compatible with diff-type""",
          'defined-type': "migration:diff-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'CREATE': {}, u'UPDATE': {}, u'DELETE': {}},), is_leaf=True, yang_name="diff-type", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='diff-type', is_config=True)""",
        })

    self.__diff_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_diff_type(self):
    self.__diff_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'CREATE': {}, u'UPDATE': {}, u'DELETE': {}},), is_leaf=True, yang_name="diff-type", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='diff-type', is_config=True)


  def _get_added_properties(self):
    """
    Getter method for added_properties, mapped from YANG variable /migrations/migrations/migration_task/upgrade_analysis/schema_diff/schema_diff_item/added_properties (container)
    """
    return self.__added_properties
      
  def _set_added_properties(self, v, load=False):
    """
    Setter method for added_properties, mapped from YANG variable /migrations/migrations/migration_task/upgrade_analysis/schema_diff/schema_diff_item/added_properties (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_added_properties is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_added_properties() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=added_properties.added_properties, is_container='container', yang_name="added-properties", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """added_properties must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=added_properties.added_properties, is_container='container', yang_name="added-properties", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='container', is_config=True)""",
        })

    self.__added_properties = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_added_properties(self):
    self.__added_properties = YANGDynClass(base=added_properties.added_properties, is_container='container', yang_name="added-properties", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='container', is_config=True)


  def _get_removed_properties(self):
    """
    Getter method for removed_properties, mapped from YANG variable /migrations/migrations/migration_task/upgrade_analysis/schema_diff/schema_diff_item/removed_properties (container)
    """
    return self.__removed_properties
      
  def _set_removed_properties(self, v, load=False):
    """
    Setter method for removed_properties, mapped from YANG variable /migrations/migrations/migration_task/upgrade_analysis/schema_diff/schema_diff_item/removed_properties (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_removed_properties is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_removed_properties() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=removed_properties.removed_properties, is_container='container', yang_name="removed-properties", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """removed_properties must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=removed_properties.removed_properties, is_container='container', yang_name="removed-properties", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='container', is_config=True)""",
        })

    self.__removed_properties = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_removed_properties(self):
    self.__removed_properties = YANGDynClass(base=removed_properties.removed_properties, is_container='container', yang_name="removed-properties", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='container', is_config=True)

  schema_path = __builtin__.property(_get_schema_path, _set_schema_path)
  diff_type = __builtin__.property(_get_diff_type, _set_diff_type)
  added_properties = __builtin__.property(_get_added_properties, _set_added_properties)
  removed_properties = __builtin__.property(_get_removed_properties, _set_removed_properties)


  _pyangbind_elements = collections.OrderedDict([('schema_path', schema_path), ('diff_type', diff_type), ('added_properties', added_properties), ('removed_properties', removed_properties), ])


