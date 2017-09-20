
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
import site
class tenant(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/tenants/tenant. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__tenant_name','__network_name','__tenant_type','__tenant_admin','__tenant_admin_password','__site',)

  _yang_name = 'tenant'
  _module_name = 'cso'
  _namespace = 'http://anutanetworks.com/cso'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tenant_admin = YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant_admin", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)
    self.__tenant_admin_password = YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant_admin_password", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)
    self.__tenant_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant_type", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)
    self.__tenant_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant_name", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)
    self.__site = YANGDynClass(base=YANGListType("site_name",site.site, yang_name="site", module_name="cso", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='site_name'), is_container='list', yang_name="site", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='list', is_config=True)
    self.__network_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="network_name", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'tenants', u'tenant']

  def _get_tenant_name(self):
    """
    Getter method for tenant_name, mapped from YANG variable /devices/device/tenants/tenant/tenant_name (string)

    YANG Description: string
    """
    return self.__tenant_name
      
  def _set_tenant_name(self, v, load=False):
    """
    Setter method for tenant_name, mapped from YANG variable /devices/device/tenants/tenant/tenant_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tenant_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tenant_name() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="tenant_name", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tenant_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant_name", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)""",
        })

    self.__tenant_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tenant_name(self):
    self.__tenant_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant_name", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)


  def _get_network_name(self):
    """
    Getter method for network_name, mapped from YANG variable /devices/device/tenants/tenant/network_name (string)

    YANG Description: string
    """
    return self.__network_name
      
  def _set_network_name(self, v, load=False):
    """
    Setter method for network_name, mapped from YANG variable /devices/device/tenants/tenant/network_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="network_name", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="network_name", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)""",
        })

    self.__network_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_name(self):
    self.__network_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="network_name", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)


  def _get_tenant_type(self):
    """
    Getter method for tenant_type, mapped from YANG variable /devices/device/tenants/tenant/tenant_type (string)

    YANG Description: string
    """
    return self.__tenant_type
      
  def _set_tenant_type(self, v, load=False):
    """
    Setter method for tenant_type, mapped from YANG variable /devices/device/tenants/tenant/tenant_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tenant_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tenant_type() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="tenant_type", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tenant_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant_type", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)""",
        })

    self.__tenant_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tenant_type(self):
    self.__tenant_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant_type", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)


  def _get_tenant_admin(self):
    """
    Getter method for tenant_admin, mapped from YANG variable /devices/device/tenants/tenant/tenant_admin (string)

    YANG Description: string
    """
    return self.__tenant_admin
      
  def _set_tenant_admin(self, v, load=False):
    """
    Setter method for tenant_admin, mapped from YANG variable /devices/device/tenants/tenant/tenant_admin (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tenant_admin is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tenant_admin() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="tenant_admin", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tenant_admin must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant_admin", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)""",
        })

    self.__tenant_admin = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tenant_admin(self):
    self.__tenant_admin = YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant_admin", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)


  def _get_tenant_admin_password(self):
    """
    Getter method for tenant_admin_password, mapped from YANG variable /devices/device/tenants/tenant/tenant_admin_password (string)

    YANG Description: string
    """
    return self.__tenant_admin_password
      
  def _set_tenant_admin_password(self, v, load=False):
    """
    Setter method for tenant_admin_password, mapped from YANG variable /devices/device/tenants/tenant/tenant_admin_password (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tenant_admin_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tenant_admin_password() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="tenant_admin_password", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tenant_admin_password must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant_admin_password", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)""",
        })

    self.__tenant_admin_password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tenant_admin_password(self):
    self.__tenant_admin_password = YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant_admin_password", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='string', is_config=True)


  def _get_site(self):
    """
    Getter method for site, mapped from YANG variable /devices/device/tenants/tenant/site (list)
    """
    return self.__site
      
  def _set_site(self, v, load=False):
    """
    Setter method for site, mapped from YANG variable /devices/device/tenants/tenant/site (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_site is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_site() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("site_name",site.site, yang_name="site", module_name="cso", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='site_name'), is_container='list', yang_name="site", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """site must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("site_name",site.site, yang_name="site", module_name="cso", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='site_name'), is_container='list', yang_name="site", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='list', is_config=True)""",
        })

    self.__site = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_site(self):
    self.__site = YANGDynClass(base=YANGListType("site_name",site.site, yang_name="site", module_name="cso", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='site_name'), is_container='list', yang_name="site", module_name="cso", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/cso', defining_module='cso', yang_type='list', is_config=True)

  tenant_name = __builtin__.property(_get_tenant_name, _set_tenant_name)
  network_name = __builtin__.property(_get_network_name, _set_network_name)
  tenant_type = __builtin__.property(_get_tenant_type, _set_tenant_type)
  tenant_admin = __builtin__.property(_get_tenant_admin, _set_tenant_admin)
  tenant_admin_password = __builtin__.property(_get_tenant_admin_password, _set_tenant_admin_password)
  site = __builtin__.property(_get_site, _set_site)


  _pyangbind_elements = collections.OrderedDict([('tenant_name', tenant_name), ('network_name', network_name), ('tenant_type', tenant_type), ('tenant_admin', tenant_admin), ('tenant_admin_password', tenant_admin_password), ('site', site), ])


