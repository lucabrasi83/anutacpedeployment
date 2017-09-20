
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
import networks
import securities
import services
class object_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/object-groups-acl/object-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__type','__description','__networks','__securities','__services',)

  _yang_name = 'object-group'
  _module_name = 'acl'
  _namespace = 'http://anutanetworks.com/acl'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='string', is_config=True)
    self.__securities = YANGDynClass(base=securities.securities, is_container='container', yang_name="securities", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='container', is_config=True)
    self.__services = YANGDynClass(base=services.services, is_container='container', yang_name="services", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='container', is_config=True)
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'security': {}, u'network': {}, u'service': {}},), is_leaf=True, yang_name="type", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='enumeration', is_config=True)
    self.__networks = YANGDynClass(base=networks.networks, is_container='container', yang_name="networks", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='container', is_config=True)
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'object-groups-acl', u'object-group']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /devices/device/object_groups_acl/object_group/name (string)

    YANG Description: string
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /devices/device/object_groups_acl/object_group/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='string', is_config=True)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /devices/device/object_groups_acl/object_group/type (enumeration)

    YANG Description: network
security
service

    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /devices/device/object_groups_acl/object_group/type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: network
security
service

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'security': {}, u'network': {}, u'service': {}},), is_leaf=True, yang_name="type", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with enumeration""",
          'defined-type': "acl:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'security': {}, u'network': {}, u'service': {}},), is_leaf=True, yang_name="type", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='enumeration', is_config=True)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'security': {}, u'network': {}, u'service': {}},), is_leaf=True, yang_name="type", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='enumeration', is_config=True)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /devices/device/object_groups_acl/object_group/description (string)

    YANG Description: string
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /devices/device/object_groups_acl/object_group/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="description", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='string', is_config=True)


  def _get_networks(self):
    """
    Getter method for networks, mapped from YANG variable /devices/device/object_groups_acl/object_group/networks (container)
    """
    return self.__networks
      
  def _set_networks(self, v, load=False):
    """
    Setter method for networks, mapped from YANG variable /devices/device/object_groups_acl/object_group/networks (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_networks is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_networks() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=networks.networks, is_container='container', yang_name="networks", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """networks must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=networks.networks, is_container='container', yang_name="networks", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='container', is_config=True)""",
        })

    self.__networks = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_networks(self):
    self.__networks = YANGDynClass(base=networks.networks, is_container='container', yang_name="networks", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='container', is_config=True)


  def _get_securities(self):
    """
    Getter method for securities, mapped from YANG variable /devices/device/object_groups_acl/object_group/securities (container)
    """
    return self.__securities
      
  def _set_securities(self, v, load=False):
    """
    Setter method for securities, mapped from YANG variable /devices/device/object_groups_acl/object_group/securities (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_securities is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_securities() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=securities.securities, is_container='container', yang_name="securities", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """securities must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=securities.securities, is_container='container', yang_name="securities", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='container', is_config=True)""",
        })

    self.__securities = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_securities(self):
    self.__securities = YANGDynClass(base=securities.securities, is_container='container', yang_name="securities", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='container', is_config=True)


  def _get_services(self):
    """
    Getter method for services, mapped from YANG variable /devices/device/object_groups_acl/object_group/services (container)
    """
    return self.__services
      
  def _set_services(self, v, load=False):
    """
    Setter method for services, mapped from YANG variable /devices/device/object_groups_acl/object_group/services (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_services is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_services() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=services.services, is_container='container', yang_name="services", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """services must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=services.services, is_container='container', yang_name="services", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='container', is_config=True)""",
        })

    self.__services = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_services(self):
    self.__services = YANGDynClass(base=services.services, is_container='container', yang_name="services", module_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/acl', defining_module='acl', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  type = __builtin__.property(_get_type, _set_type)
  description = __builtin__.property(_get_description, _set_description)
  networks = __builtin__.property(_get_networks, _set_networks)
  securities = __builtin__.property(_get_securities, _set_securities)
  services = __builtin__.property(_get_services, _set_services)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('type', type), ('description', description), ('networks', networks), ('securities', securities), ('services', services), ])


