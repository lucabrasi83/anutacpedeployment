
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
class openstack_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /system/tables/openstack-info/openstack-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__ip_address','__credential_set_name','__vimtype','__serial_number','__network_type','__project_sync_type','__project','__service_type','__provider_network','__route_target','__segment_start_id','__segment_end_id',)

  _yang_name = 'openstack-info'
  _module_name = 'system'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__route_target = YANGDynClass(base=unicode, is_leaf=True, yang_name="route-target", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__vimtype = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'OPENSTACK': {}, u'JUNIPERContrail': {}, u'VMWARE': {}},), is_leaf=True, yang_name="vimtype", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='vim-type', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__credential_set_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="credential-set-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)
    self.__provider_network = YANGDynClass(base=unicode, is_leaf=True, yang_name="provider-network", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__project = YANGDynClass(base=unicode, is_leaf=True, yang_name="project", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__project_sync_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INDIVIDUALPROJECT': {}, u'SYSTEMPROJECT': {}},), is_leaf=True, yang_name="project-sync-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='project-sync-type', is_config=True)
    self.__segment_end_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="segment-end-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__service_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NONE': {}, u'ContrailAPI': {}, u'OpenStackAPI': {}},), is_leaf=True, yang_name="service-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='contrail-service-type', is_config=True)
    self.__serial_number = YANGDynClass(base=unicode, is_leaf=True, yang_name="serial-number", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__ip_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-address", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__network_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="network-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__segment_start_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="segment-start-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

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
      return [u'system', u'tables', u'openstack-info', u'openstack-info']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/tables/openstack_info/openstack_info/name (string)

    YANG Description: string
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/tables/openstack_info/openstack_info/name (string)
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
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_ip_address(self):
    """
    Getter method for ip_address, mapped from YANG variable /system/tables/openstack_info/openstack_info/ip_address (string)

    YANG Description: string
    """
    return self.__ip_address
      
  def _set_ip_address(self, v, load=False):
    """
    Setter method for ip_address, mapped from YANG variable /system/tables/openstack_info/openstack_info/ip_address (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_address() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ip-address", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_address must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-address", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_address(self):
    self.__ip_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-address", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_credential_set_name(self):
    """
    Getter method for credential_set_name, mapped from YANG variable /system/tables/openstack_info/openstack_info/credential_set_name (leafref)

    YANG Description: credential-set-name
    """
    return self.__credential_set_name
      
  def _set_credential_set_name(self, v, load=False):
    """
    Setter method for credential_set_name, mapped from YANG variable /system/tables/openstack_info/openstack_info/credential_set_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_credential_set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_credential_set_name() directly.

    YANG Description: credential-set-name
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="credential-set-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """credential_set_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="credential-set-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)""",
        })

    self.__credential_set_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_credential_set_name(self):
    self.__credential_set_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="credential-set-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)


  def _get_vimtype(self):
    """
    Getter method for vimtype, mapped from YANG variable /system/tables/openstack_info/openstack_info/vimtype (vim-type)

    YANG Description: OPENSTACK
JUNIPERContrail
VMWARE

    """
    return self.__vimtype
      
  def _set_vimtype(self, v, load=False):
    """
    Setter method for vimtype, mapped from YANG variable /system/tables/openstack_info/openstack_info/vimtype (vim-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vimtype is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vimtype() directly.

    YANG Description: OPENSTACK
JUNIPERContrail
VMWARE

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'OPENSTACK': {}, u'JUNIPERContrail': {}, u'VMWARE': {}},), is_leaf=True, yang_name="vimtype", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='vim-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vimtype must be of a type compatible with vim-type""",
          'defined-type': "controller:vim-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'OPENSTACK': {}, u'JUNIPERContrail': {}, u'VMWARE': {}},), is_leaf=True, yang_name="vimtype", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='vim-type', is_config=True)""",
        })

    self.__vimtype = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vimtype(self):
    self.__vimtype = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'OPENSTACK': {}, u'JUNIPERContrail': {}, u'VMWARE': {}},), is_leaf=True, yang_name="vimtype", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='vim-type', is_config=True)


  def _get_serial_number(self):
    """
    Getter method for serial_number, mapped from YANG variable /system/tables/openstack_info/openstack_info/serial_number (string)

    YANG Description: string
    """
    return self.__serial_number
      
  def _set_serial_number(self, v, load=False):
    """
    Setter method for serial_number, mapped from YANG variable /system/tables/openstack_info/openstack_info/serial_number (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_serial_number is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_serial_number() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="serial-number", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """serial_number must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="serial-number", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__serial_number = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_serial_number(self):
    self.__serial_number = YANGDynClass(base=unicode, is_leaf=True, yang_name="serial-number", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_network_type(self):
    """
    Getter method for network_type, mapped from YANG variable /system/tables/openstack_info/openstack_info/network_type (string)

    YANG Description: string
    """
    return self.__network_type
      
  def _set_network_type(self, v, load=False):
    """
    Setter method for network_type, mapped from YANG variable /system/tables/openstack_info/openstack_info/network_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_type() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="network-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="network-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__network_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_type(self):
    self.__network_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="network-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_project_sync_type(self):
    """
    Getter method for project_sync_type, mapped from YANG variable /system/tables/openstack_info/openstack_info/project_sync_type (project-sync-type)

    YANG Description: SYSTEMPROJECT
INDIVIDUALPROJECT

    """
    return self.__project_sync_type
      
  def _set_project_sync_type(self, v, load=False):
    """
    Setter method for project_sync_type, mapped from YANG variable /system/tables/openstack_info/openstack_info/project_sync_type (project-sync-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_project_sync_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_project_sync_type() directly.

    YANG Description: SYSTEMPROJECT
INDIVIDUALPROJECT

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INDIVIDUALPROJECT': {}, u'SYSTEMPROJECT': {}},), is_leaf=True, yang_name="project-sync-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='project-sync-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """project_sync_type must be of a type compatible with project-sync-type""",
          'defined-type': "controller:project-sync-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INDIVIDUALPROJECT': {}, u'SYSTEMPROJECT': {}},), is_leaf=True, yang_name="project-sync-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='project-sync-type', is_config=True)""",
        })

    self.__project_sync_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_project_sync_type(self):
    self.__project_sync_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INDIVIDUALPROJECT': {}, u'SYSTEMPROJECT': {}},), is_leaf=True, yang_name="project-sync-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='project-sync-type', is_config=True)


  def _get_project(self):
    """
    Getter method for project, mapped from YANG variable /system/tables/openstack_info/openstack_info/project (string)

    YANG Description: string
    """
    return self.__project
      
  def _set_project(self, v, load=False):
    """
    Setter method for project, mapped from YANG variable /system/tables/openstack_info/openstack_info/project (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_project is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_project() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="project", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """project must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="project", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__project = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_project(self):
    self.__project = YANGDynClass(base=unicode, is_leaf=True, yang_name="project", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_service_type(self):
    """
    Getter method for service_type, mapped from YANG variable /system/tables/openstack_info/openstack_info/service_type (contrail-service-type)

    YANG Description: NONE
OpenStackAPI
ContrailAPI

    """
    return self.__service_type
      
  def _set_service_type(self, v, load=False):
    """
    Setter method for service_type, mapped from YANG variable /system/tables/openstack_info/openstack_info/service_type (contrail-service-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_service_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_service_type() directly.

    YANG Description: NONE
OpenStackAPI
ContrailAPI

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NONE': {}, u'ContrailAPI': {}, u'OpenStackAPI': {}},), is_leaf=True, yang_name="service-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='contrail-service-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """service_type must be of a type compatible with contrail-service-type""",
          'defined-type': "controller:contrail-service-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NONE': {}, u'ContrailAPI': {}, u'OpenStackAPI': {}},), is_leaf=True, yang_name="service-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='contrail-service-type', is_config=True)""",
        })

    self.__service_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_service_type(self):
    self.__service_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NONE': {}, u'ContrailAPI': {}, u'OpenStackAPI': {}},), is_leaf=True, yang_name="service-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='contrail-service-type', is_config=True)


  def _get_provider_network(self):
    """
    Getter method for provider_network, mapped from YANG variable /system/tables/openstack_info/openstack_info/provider_network (string)

    YANG Description: string
    """
    return self.__provider_network
      
  def _set_provider_network(self, v, load=False):
    """
    Setter method for provider_network, mapped from YANG variable /system/tables/openstack_info/openstack_info/provider_network (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_provider_network is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_provider_network() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="provider-network", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """provider_network must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="provider-network", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__provider_network = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_provider_network(self):
    self.__provider_network = YANGDynClass(base=unicode, is_leaf=True, yang_name="provider-network", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_route_target(self):
    """
    Getter method for route_target, mapped from YANG variable /system/tables/openstack_info/openstack_info/route_target (string)

    YANG Description: string
    """
    return self.__route_target
      
  def _set_route_target(self, v, load=False):
    """
    Setter method for route_target, mapped from YANG variable /system/tables/openstack_info/openstack_info/route_target (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_target is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_target() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="route-target", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_target must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="route-target", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__route_target = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_target(self):
    self.__route_target = YANGDynClass(base=unicode, is_leaf=True, yang_name="route-target", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_segment_start_id(self):
    """
    Getter method for segment_start_id, mapped from YANG variable /system/tables/openstack_info/openstack_info/segment_start_id (string)

    YANG Description: string
    """
    return self.__segment_start_id
      
  def _set_segment_start_id(self, v, load=False):
    """
    Setter method for segment_start_id, mapped from YANG variable /system/tables/openstack_info/openstack_info/segment_start_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_segment_start_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_segment_start_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="segment-start-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """segment_start_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="segment-start-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__segment_start_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_segment_start_id(self):
    self.__segment_start_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="segment-start-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_segment_end_id(self):
    """
    Getter method for segment_end_id, mapped from YANG variable /system/tables/openstack_info/openstack_info/segment_end_id (string)

    YANG Description: string
    """
    return self.__segment_end_id
      
  def _set_segment_end_id(self, v, load=False):
    """
    Setter method for segment_end_id, mapped from YANG variable /system/tables/openstack_info/openstack_info/segment_end_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_segment_end_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_segment_end_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="segment-end-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """segment_end_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="segment-end-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__segment_end_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_segment_end_id(self):
    self.__segment_end_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="segment-end-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  ip_address = __builtin__.property(_get_ip_address, _set_ip_address)
  credential_set_name = __builtin__.property(_get_credential_set_name, _set_credential_set_name)
  vimtype = __builtin__.property(_get_vimtype, _set_vimtype)
  serial_number = __builtin__.property(_get_serial_number, _set_serial_number)
  network_type = __builtin__.property(_get_network_type, _set_network_type)
  project_sync_type = __builtin__.property(_get_project_sync_type, _set_project_sync_type)
  project = __builtin__.property(_get_project, _set_project)
  service_type = __builtin__.property(_get_service_type, _set_service_type)
  provider_network = __builtin__.property(_get_provider_network, _set_provider_network)
  route_target = __builtin__.property(_get_route_target, _set_route_target)
  segment_start_id = __builtin__.property(_get_segment_start_id, _set_segment_start_id)
  segment_end_id = __builtin__.property(_get_segment_end_id, _set_segment_end_id)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('ip_address', ip_address), ('credential_set_name', credential_set_name), ('vimtype', vimtype), ('serial_number', serial_number), ('network_type', network_type), ('project_sync_type', project_sync_type), ('project', project), ('service_type', service_type), ('provider_network', provider_network), ('route_target', route_target), ('segment_start_id', segment_start_id), ('segment_end_id', segment_end_id), ])


