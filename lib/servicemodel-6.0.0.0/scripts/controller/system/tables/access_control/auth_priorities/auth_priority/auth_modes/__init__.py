
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
class auth_modes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /system/tables/access-control/auth-priorities/auth-priority/auth-modes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__priority','__authentication_mode',)

  _yang_name = 'auth-modes'
  _module_name = 'accesscontrol'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="priority", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)
    self.__authentication_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TACACS': {}, u'ACTIVE_DIRECTORY': {}, u'OPENLDAP': {}, u'LOCAL': {}},), is_leaf=True, yang_name="authentication-mode", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='auth-mode', is_config=True)

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
      return [u'system', u'tables', u'access-control', u'auth-priorities', u'auth-priority', u'auth-modes']

  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /system/tables/access_control/auth_priorities/auth_priority/auth_modes/priority (uint32)

    YANG Description: 0..4294967295
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /system/tables/access_control/auth_priorities/auth_priority/auth_modes/priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: 0..4294967295
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="priority", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="priority", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="priority", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)


  def _get_authentication_mode(self):
    """
    Getter method for authentication_mode, mapped from YANG variable /system/tables/access_control/auth_priorities/auth_priority/auth_modes/authentication_mode (auth-mode)

    YANG Description: LOCAL
OPENLDAP
ACTIVE_DIRECTORY
TACACS

    """
    return self.__authentication_mode
      
  def _set_authentication_mode(self, v, load=False):
    """
    Setter method for authentication_mode, mapped from YANG variable /system/tables/access_control/auth_priorities/auth_priority/auth_modes/authentication_mode (auth-mode)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication_mode() directly.

    YANG Description: LOCAL
OPENLDAP
ACTIVE_DIRECTORY
TACACS

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TACACS': {}, u'ACTIVE_DIRECTORY': {}, u'OPENLDAP': {}, u'LOCAL': {}},), is_leaf=True, yang_name="authentication-mode", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='auth-mode', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication_mode must be of a type compatible with auth-mode""",
          'defined-type': "controller:auth-mode",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TACACS': {}, u'ACTIVE_DIRECTORY': {}, u'OPENLDAP': {}, u'LOCAL': {}},), is_leaf=True, yang_name="authentication-mode", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='auth-mode', is_config=True)""",
        })

    self.__authentication_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication_mode(self):
    self.__authentication_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TACACS': {}, u'ACTIVE_DIRECTORY': {}, u'OPENLDAP': {}, u'LOCAL': {}},), is_leaf=True, yang_name="authentication-mode", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='auth-mode', is_config=True)

  priority = __builtin__.property(_get_priority, _set_priority)
  authentication_mode = __builtin__.property(_get_authentication_mode, _set_authentication_mode)


  _pyangbind_elements = collections.OrderedDict([('priority', priority), ('authentication_mode', authentication_mode), ])


