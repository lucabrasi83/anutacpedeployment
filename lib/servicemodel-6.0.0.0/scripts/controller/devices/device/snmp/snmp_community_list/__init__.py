
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
class snmp_community_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/snmp/snmp-community-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__snmp_string','__permission_type','__acl',)

  _yang_name = 'snmp-community-list'
  _module_name = 'basicconfigs'
  _namespace = 'http://anutanetworks.com/basicDeviceConfigs'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__snmp_string = YANGDynClass(base=unicode, is_leaf=True, yang_name="snmp-string", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    self.__acl = YANGDynClass(base=unicode, is_leaf=True, yang_name="acl", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    self.__permission_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="permission-type", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'snmp', u'snmp-community-list']

  def _get_snmp_string(self):
    """
    Getter method for snmp_string, mapped from YANG variable /devices/device/snmp/snmp_community_list/snmp_string (string)

    YANG Description: string
    """
    return self.__snmp_string
      
  def _set_snmp_string(self, v, load=False):
    """
    Setter method for snmp_string, mapped from YANG variable /devices/device/snmp/snmp_community_list/snmp_string (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_snmp_string is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_snmp_string() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="snmp-string", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """snmp_string must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="snmp-string", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)""",
        })

    self.__snmp_string = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_snmp_string(self):
    self.__snmp_string = YANGDynClass(base=unicode, is_leaf=True, yang_name="snmp-string", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)


  def _get_permission_type(self):
    """
    Getter method for permission_type, mapped from YANG variable /devices/device/snmp/snmp_community_list/permission_type (string)

    YANG Description: string
    """
    return self.__permission_type
      
  def _set_permission_type(self, v, load=False):
    """
    Setter method for permission_type, mapped from YANG variable /devices/device/snmp/snmp_community_list/permission_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_permission_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_permission_type() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="permission-type", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """permission_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="permission-type", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)""",
        })

    self.__permission_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_permission_type(self):
    self.__permission_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="permission-type", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)


  def _get_acl(self):
    """
    Getter method for acl, mapped from YANG variable /devices/device/snmp/snmp_community_list/acl (string)

    YANG Description: string
    """
    return self.__acl
      
  def _set_acl(self, v, load=False):
    """
    Setter method for acl, mapped from YANG variable /devices/device/snmp/snmp_community_list/acl (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_acl is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_acl() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="acl", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """acl must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="acl", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)""",
        })

    self.__acl = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_acl(self):
    self.__acl = YANGDynClass(base=unicode, is_leaf=True, yang_name="acl", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)

  snmp_string = __builtin__.property(_get_snmp_string, _set_snmp_string)
  permission_type = __builtin__.property(_get_permission_type, _set_permission_type)
  acl = __builtin__.property(_get_acl, _set_acl)


  _pyangbind_elements = collections.OrderedDict([('snmp_string', snmp_string), ('permission_type', permission_type), ('acl', acl), ])


