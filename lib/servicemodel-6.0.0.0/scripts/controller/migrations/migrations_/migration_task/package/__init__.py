
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
class package(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /migrations/migrations/migration-task/package. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__package_name','__from_version','__to_version',)

  _yang_name = 'package'
  _module_name = 'migration'
  _namespace = 'http://anutanetworks.com/migration'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__to_version = YANGDynClass(base=unicode, is_leaf=True, yang_name="to-version", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)
    self.__from_version = YANGDynClass(base=unicode, is_leaf=True, yang_name="from-version", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)
    self.__package_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="package-name", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)

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
      return [u'migrations', u'migrations', u'migration-task', u'package']

  def _get_package_name(self):
    """
    Getter method for package_name, mapped from YANG variable /migrations/migrations/migration_task/package/package_name (string)

    YANG Description: string
    """
    return self.__package_name
      
  def _set_package_name(self, v, load=False):
    """
    Setter method for package_name, mapped from YANG variable /migrations/migrations/migration_task/package/package_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_package_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_package_name() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="package-name", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """package_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="package-name", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)""",
        })

    self.__package_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_package_name(self):
    self.__package_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="package-name", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)


  def _get_from_version(self):
    """
    Getter method for from_version, mapped from YANG variable /migrations/migrations/migration_task/package/from_version (string)

    YANG Description: string
    """
    return self.__from_version
      
  def _set_from_version(self, v, load=False):
    """
    Setter method for from_version, mapped from YANG variable /migrations/migrations/migration_task/package/from_version (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_from_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_from_version() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="from-version", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """from_version must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="from-version", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)""",
        })

    self.__from_version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_from_version(self):
    self.__from_version = YANGDynClass(base=unicode, is_leaf=True, yang_name="from-version", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)


  def _get_to_version(self):
    """
    Getter method for to_version, mapped from YANG variable /migrations/migrations/migration_task/package/to_version (string)

    YANG Description: string
    """
    return self.__to_version
      
  def _set_to_version(self, v, load=False):
    """
    Setter method for to_version, mapped from YANG variable /migrations/migrations/migration_task/package/to_version (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_to_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_to_version() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="to-version", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """to_version must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="to-version", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)""",
        })

    self.__to_version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_to_version(self):
    self.__to_version = YANGDynClass(base=unicode, is_leaf=True, yang_name="to-version", module_name="migration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/migration', defining_module='migration', yang_type='string', is_config=True)

  package_name = __builtin__.property(_get_package_name, _set_package_name)
  from_version = __builtin__.property(_get_from_version, _set_from_version)
  to_version = __builtin__.property(_get_to_version, _set_to_version)


  _pyangbind_elements = collections.OrderedDict([('package_name', package_name), ('from_version', from_version), ('to_version', to_version), ])


