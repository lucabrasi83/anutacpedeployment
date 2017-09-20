
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
import device
import resource_group_policies
import capacities
import network_connection
class resource_pool(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module resourcepool - based on the path /resource-pools/resource-pool. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__description','__available_for_services','__device','__parent_resource_pool','__location','__deploy','__resource_group_policies','__capacities','__network_connection',)

  _yang_name = 'resource-pool'
  _module_name = 'resourcepool'
  _namespace = 'http://anutanetworks.com/resourcepool'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[a-zA-Z0-9_-]+$', 'length': [u'1..36']}), is_leaf=True, yang_name="name", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='string', is_config=True)
    self.__deploy = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="deploy", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='boolean', is_config=True)
    self.__capacities = YANGDynClass(base=YANGListType("capacity_id",capacities.capacities, yang_name="capacities", module_name="capacities", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='capacity-id'), is_container='list', yang_name="capacities", module_name="capacities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/capacities', defining_module='capacities', yang_type='list', is_config=True)
    self.__network_connection = YANGDynClass(base=YANGListType("id",network_connection.network_connection, yang_name="network-connection", module_name="topology", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id'), is_container='list', yang_name="network-connection", module_name="topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/topology', defining_module='topology', yang_type='list', is_config=True)
    self.__parent_resource_pool = YANGDynClass(base=unicode, is_leaf=True, yang_name="parent-resource-pool", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='leafref', is_config=True)
    self.__available_for_services = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="available-for-services", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='boolean', is_config=True)
    self.__location = YANGDynClass(base=unicode, is_leaf=True, yang_name="location", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='leafref', is_config=True)
    self.__device = YANGDynClass(base=YANGListType("id",device.device, yang_name="device", module_name="resourcepool", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id'), is_container='list', yang_name="device", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='list', is_config=True)
    self.__resource_group_policies = YANGDynClass(base=resource_group_policies.resource_group_policies, is_container='container', yang_name="resource-group-policies", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='container', is_config=True)
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='string', is_config=True)

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
      return [u'resource-pools', u'resource-pool']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /resource_pools/resource_pool/name (string)

    YANG Description: Name of the resource pool. This also acts as Unique Key. Allows AlphaNumerics, hyphen, underscore characters only. Max length is 36
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /resource_pools/resource_pool/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name of the resource pool. This also acts as Unique Key. Allows AlphaNumerics, hyphen, underscore characters only. Max length is 36
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[a-zA-Z0-9_-]+$', 'length': [u'1..36']}), is_leaf=True, yang_name="name", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[a-zA-Z0-9_-]+$', 'length': [u'1..36']}), is_leaf=True, yang_name="name", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[a-zA-Z0-9_-]+$', 'length': [u'1..36']}), is_leaf=True, yang_name="name", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='string', is_config=True)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /resource_pools/resource_pool/description (string)

    YANG Description: Description of the resource pool
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /resource_pools/resource_pool/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: Description of the resource pool
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="description", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='string', is_config=True)


  def _get_available_for_services(self):
    """
    Getter method for available_for_services, mapped from YANG variable /resource_pools/resource_pool/available_for_services (boolean)

    YANG Description:  Flag to indicated whether this resource-pool can be used for services. Typically set to false if the resource pool doesn't match the required criterion 
    """
    return self.__available_for_services
      
  def _set_available_for_services(self, v, load=False):
    """
    Setter method for available_for_services, mapped from YANG variable /resource_pools/resource_pool/available_for_services (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_available_for_services is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_available_for_services() directly.

    YANG Description:  Flag to indicated whether this resource-pool can be used for services. Typically set to false if the resource pool doesn't match the required criterion 
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="available-for-services", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """available_for_services must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="available-for-services", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='boolean', is_config=True)""",
        })

    self.__available_for_services = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_available_for_services(self):
    self.__available_for_services = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="available-for-services", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='boolean', is_config=True)


  def _get_device(self):
    """
    Getter method for device, mapped from YANG variable /resource_pools/resource_pool/device (list)
    """
    return self.__device
      
  def _set_device(self, v, load=False):
    """
    Setter method for device, mapped from YANG variable /resource_pools/resource_pool/device (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_device is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_device() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("id",device.device, yang_name="device", module_name="resourcepool", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id'), is_container='list', yang_name="device", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """device must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",device.device, yang_name="device", module_name="resourcepool", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id'), is_container='list', yang_name="device", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='list', is_config=True)""",
        })

    self.__device = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_device(self):
    self.__device = YANGDynClass(base=YANGListType("id",device.device, yang_name="device", module_name="resourcepool", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id'), is_container='list', yang_name="device", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='list', is_config=True)


  def _get_parent_resource_pool(self):
    """
    Getter method for parent_resource_pool, mapped from YANG variable /resource_pools/resource_pool/parent_resource_pool (leafref)

    YANG Description: parent-resource-pool
    """
    return self.__parent_resource_pool
      
  def _set_parent_resource_pool(self, v, load=False):
    """
    Setter method for parent_resource_pool, mapped from YANG variable /resource_pools/resource_pool/parent_resource_pool (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_parent_resource_pool is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_parent_resource_pool() directly.

    YANG Description: parent-resource-pool
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="parent-resource-pool", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """parent_resource_pool must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="parent-resource-pool", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='leafref', is_config=True)""",
        })

    self.__parent_resource_pool = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_parent_resource_pool(self):
    self.__parent_resource_pool = YANGDynClass(base=unicode, is_leaf=True, yang_name="parent-resource-pool", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='leafref', is_config=True)


  def _get_location(self):
    """
    Getter method for location, mapped from YANG variable /resource_pools/resource_pool/location (leafref)

    YANG Description: location
    """
    return self.__location
      
  def _set_location(self, v, load=False):
    """
    Setter method for location, mapped from YANG variable /resource_pools/resource_pool/location (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_location is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_location() directly.

    YANG Description: location
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="location", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """location must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="location", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='leafref', is_config=True)""",
        })

    self.__location = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_location(self):
    self.__location = YANGDynClass(base=unicode, is_leaf=True, yang_name="location", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='leafref', is_config=True)


  def _get_deploy(self):
    """
    Getter method for deploy, mapped from YANG variable /resource_pools/resource_pool/deploy (boolean)

    YANG Description: Set to false if the resource pool needs to be decommisioned
    """
    return self.__deploy
      
  def _set_deploy(self, v, load=False):
    """
    Setter method for deploy, mapped from YANG variable /resource_pools/resource_pool/deploy (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_deploy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_deploy() directly.

    YANG Description: Set to false if the resource pool needs to be decommisioned
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="deploy", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """deploy must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="deploy", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='boolean', is_config=True)""",
        })

    self.__deploy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_deploy(self):
    self.__deploy = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="deploy", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='boolean', is_config=True)


  def _get_resource_group_policies(self):
    """
    Getter method for resource_group_policies, mapped from YANG variable /resource_pools/resource_pool/resource_group_policies (container)

    YANG Description: Resource group policies that provide hints to the individual modules
    """
    return self.__resource_group_policies
      
  def _set_resource_group_policies(self, v, load=False):
    """
    Setter method for resource_group_policies, mapped from YANG variable /resource_pools/resource_pool/resource_group_policies (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_resource_group_policies is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_resource_group_policies() directly.

    YANG Description: Resource group policies that provide hints to the individual modules
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=resource_group_policies.resource_group_policies, is_container='container', yang_name="resource-group-policies", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """resource_group_policies must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=resource_group_policies.resource_group_policies, is_container='container', yang_name="resource-group-policies", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='container', is_config=True)""",
        })

    self.__resource_group_policies = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_resource_group_policies(self):
    self.__resource_group_policies = YANGDynClass(base=resource_group_policies.resource_group_policies, is_container='container', yang_name="resource-group-policies", module_name="resourcepool", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/resourcepool', defining_module='resourcepool', yang_type='container', is_config=True)


  def _get_capacities(self):
    """
    Getter method for capacities, mapped from YANG variable /resource_pools/resource_pool/capacities (list)
    """
    return self.__capacities
      
  def _set_capacities(self, v, load=False):
    """
    Setter method for capacities, mapped from YANG variable /resource_pools/resource_pool/capacities (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_capacities is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_capacities() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("capacity_id",capacities.capacities, yang_name="capacities", module_name="capacities", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='capacity-id'), is_container='list', yang_name="capacities", module_name="capacities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/capacities', defining_module='capacities', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """capacities must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("capacity_id",capacities.capacities, yang_name="capacities", module_name="capacities", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='capacity-id'), is_container='list', yang_name="capacities", module_name="capacities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/capacities', defining_module='capacities', yang_type='list', is_config=True)""",
        })

    self.__capacities = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_capacities(self):
    self.__capacities = YANGDynClass(base=YANGListType("capacity_id",capacities.capacities, yang_name="capacities", module_name="capacities", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='capacity-id'), is_container='list', yang_name="capacities", module_name="capacities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/capacities', defining_module='capacities', yang_type='list', is_config=True)


  def _get_network_connection(self):
    """
    Getter method for network_connection, mapped from YANG variable /resource_pools/resource_pool/network_connection (list)
    """
    return self.__network_connection
      
  def _set_network_connection(self, v, load=False):
    """
    Setter method for network_connection, mapped from YANG variable /resource_pools/resource_pool/network_connection (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_connection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_connection() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("id",network_connection.network_connection, yang_name="network-connection", module_name="topology", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id'), is_container='list', yang_name="network-connection", module_name="topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/topology', defining_module='topology', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_connection must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",network_connection.network_connection, yang_name="network-connection", module_name="topology", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id'), is_container='list', yang_name="network-connection", module_name="topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/topology', defining_module='topology', yang_type='list', is_config=True)""",
        })

    self.__network_connection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_connection(self):
    self.__network_connection = YANGDynClass(base=YANGListType("id",network_connection.network_connection, yang_name="network-connection", module_name="topology", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id'), is_container='list', yang_name="network-connection", module_name="topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/topology', defining_module='topology', yang_type='list', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  description = __builtin__.property(_get_description, _set_description)
  available_for_services = __builtin__.property(_get_available_for_services, _set_available_for_services)
  device = __builtin__.property(_get_device, _set_device)
  parent_resource_pool = __builtin__.property(_get_parent_resource_pool, _set_parent_resource_pool)
  location = __builtin__.property(_get_location, _set_location)
  deploy = __builtin__.property(_get_deploy, _set_deploy)
  resource_group_policies = __builtin__.property(_get_resource_group_policies, _set_resource_group_policies)
  capacities = __builtin__.property(_get_capacities, _set_capacities)
  network_connection = __builtin__.property(_get_network_connection, _set_network_connection)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('description', description), ('available_for_services', available_for_services), ('device', device), ('parent_resource_pool', parent_resource_pool), ('location', location), ('deploy', deploy), ('resource_group_policies', resource_group_policies), ('capacities', capacities), ('network_connection', network_connection), ])


