
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
import tenant_capacity
class tenant(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /tenants/tenant. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__description','__tenant_id','__vnmc_dn','__naming_counter','__dry_run','__system_defined','__enterprise_id','__tenant_logo','__tenant_capacity',)

  _yang_name = 'tenant'
  _module_name = 'controller'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[a-zA-Z0-9_-]+$', 'length': [u'1..64']}), is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='ndt:namePattern64', is_config=True)
    self.__dry_run = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dry-run", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    self.__tenant_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="tenant-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__vnmc_dn = YANGDynClass(base=unicode, is_leaf=True, yang_name="vnmc-dn", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=False)
    self.__tenant_capacity = YANGDynClass(base=tenant_capacity.tenant_capacity, is_container='container', yang_name="tenant-capacity", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)
    self.__system_defined = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="system-defined", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)
    self.__tenant_logo = YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant-logo", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=False)
    self.__enterprise_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="enterprise-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=False)
    self.__naming_counter = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="naming-counter", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint16', is_config=False)
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

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
      return [u'tenants', u'tenant']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /tenants/tenant/name (ndt:namePattern64)

    YANG Description: Unique name for tenant.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /tenants/tenant/name (ndt:namePattern64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Unique name for tenant.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[a-zA-Z0-9_-]+$', 'length': [u'1..64']}), is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='ndt:namePattern64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with ndt:namePattern64""",
          'defined-type': "ndt:namePattern64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[a-zA-Z0-9_-]+$', 'length': [u'1..64']}), is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='ndt:namePattern64', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[a-zA-Z0-9_-]+$', 'length': [u'1..64']}), is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='ndt:namePattern64', is_config=True)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /tenants/tenant/description (string)

    YANG Description: string
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /tenants/tenant/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="description", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_tenant_id(self):
    """
    Getter method for tenant_id, mapped from YANG variable /tenants/tenant/tenant_id (string)

    YANG Description: Unique tenant id 
    """
    return self.__tenant_id
      
  def _set_tenant_id(self, v, load=False):
    """
    Setter method for tenant_id, mapped from YANG variable /tenants/tenant/tenant_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tenant_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tenant_id() directly.

    YANG Description: Unique tenant id 
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="tenant-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tenant_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="tenant-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__tenant_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tenant_id(self):
    self.__tenant_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="tenant-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_vnmc_dn(self):
    """
    Getter method for vnmc_dn, mapped from YANG variable /tenants/tenant/vnmc_dn (string)

    YANG Description: string
    """
    return self.__vnmc_dn
      
  def _set_vnmc_dn(self, v, load=False):
    """
    Setter method for vnmc_dn, mapped from YANG variable /tenants/tenant/vnmc_dn (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vnmc_dn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vnmc_dn() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vnmc-dn", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vnmc_dn must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vnmc-dn", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=False)""",
        })

    self.__vnmc_dn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vnmc_dn(self):
    self.__vnmc_dn = YANGDynClass(base=unicode, is_leaf=True, yang_name="vnmc-dn", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=False)


  def _get_naming_counter(self):
    """
    Getter method for naming_counter, mapped from YANG variable /tenants/tenant/naming_counter (uint16)

    YANG Description: 0..65535
    """
    return self.__naming_counter
      
  def _set_naming_counter(self, v, load=False):
    """
    Setter method for naming_counter, mapped from YANG variable /tenants/tenant/naming_counter (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_naming_counter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_naming_counter() directly.

    YANG Description: 0..65535
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="naming-counter", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """naming_counter must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="naming-counter", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint16', is_config=False)""",
        })

    self.__naming_counter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_naming_counter(self):
    self.__naming_counter = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="naming-counter", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint16', is_config=False)


  def _get_dry_run(self):
    """
    Getter method for dry_run, mapped from YANG variable /tenants/tenant/dry_run (boolean)

    YANG Description: Send configuration commands to Devices when dry-run is false.
    """
    return self.__dry_run
      
  def _set_dry_run(self, v, load=False):
    """
    Setter method for dry_run, mapped from YANG variable /tenants/tenant/dry_run (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dry_run is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dry_run() directly.

    YANG Description: Send configuration commands to Devices when dry-run is false.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dry-run", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dry_run must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dry-run", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)""",
        })

    self.__dry_run = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dry_run(self):
    self.__dry_run = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dry-run", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)


  def _get_system_defined(self):
    """
    Getter method for system_defined, mapped from YANG variable /tenants/tenant/system_defined (boolean)

    YANG Description: system-defined: True/False
    """
    return self.__system_defined
      
  def _set_system_defined(self, v, load=False):
    """
    Setter method for system_defined, mapped from YANG variable /tenants/tenant/system_defined (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_system_defined is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_system_defined() directly.

    YANG Description: system-defined: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="system-defined", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """system_defined must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="system-defined", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)""",
        })

    self.__system_defined = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_system_defined(self):
    self.__system_defined = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="system-defined", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)


  def _get_enterprise_id(self):
    """
    Getter method for enterprise_id, mapped from YANG variable /tenants/tenant/enterprise_id (string)

    YANG Description: string
    """
    return self.__enterprise_id
      
  def _set_enterprise_id(self, v, load=False):
    """
    Setter method for enterprise_id, mapped from YANG variable /tenants/tenant/enterprise_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enterprise_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enterprise_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="enterprise-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enterprise_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="enterprise-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=False)""",
        })

    self.__enterprise_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enterprise_id(self):
    self.__enterprise_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="enterprise-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=False)


  def _get_tenant_logo(self):
    """
    Getter method for tenant_logo, mapped from YANG variable /tenants/tenant/tenant_logo (string)

    YANG Description: string
    """
    return self.__tenant_logo
      
  def _set_tenant_logo(self, v, load=False):
    """
    Setter method for tenant_logo, mapped from YANG variable /tenants/tenant/tenant_logo (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tenant_logo is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tenant_logo() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="tenant-logo", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tenant_logo must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant-logo", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=False)""",
        })

    self.__tenant_logo = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tenant_logo(self):
    self.__tenant_logo = YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant-logo", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=False)


  def _get_tenant_capacity(self):
    """
    Getter method for tenant_capacity, mapped from YANG variable /tenants/tenant/tenant_capacity (container)
    """
    return self.__tenant_capacity
      
  def _set_tenant_capacity(self, v, load=False):
    """
    Setter method for tenant_capacity, mapped from YANG variable /tenants/tenant/tenant_capacity (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tenant_capacity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tenant_capacity() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=tenant_capacity.tenant_capacity, is_container='container', yang_name="tenant-capacity", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tenant_capacity must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tenant_capacity.tenant_capacity, is_container='container', yang_name="tenant-capacity", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)""",
        })

    self.__tenant_capacity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tenant_capacity(self):
    self.__tenant_capacity = YANGDynClass(base=tenant_capacity.tenant_capacity, is_container='container', yang_name="tenant-capacity", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  description = __builtin__.property(_get_description, _set_description)
  tenant_id = __builtin__.property(_get_tenant_id, _set_tenant_id)
  vnmc_dn = __builtin__.property(_get_vnmc_dn)
  naming_counter = __builtin__.property(_get_naming_counter)
  dry_run = __builtin__.property(_get_dry_run, _set_dry_run)
  system_defined = __builtin__.property(_get_system_defined)
  enterprise_id = __builtin__.property(_get_enterprise_id)
  tenant_logo = __builtin__.property(_get_tenant_logo)
  tenant_capacity = __builtin__.property(_get_tenant_capacity, _set_tenant_capacity)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('description', description), ('tenant_id', tenant_id), ('vnmc_dn', vnmc_dn), ('naming_counter', naming_counter), ('dry_run', dry_run), ('system_defined', system_defined), ('enterprise_id', enterprise_id), ('tenant_logo', tenant_logo), ('tenant_capacity', tenant_capacity), ])


