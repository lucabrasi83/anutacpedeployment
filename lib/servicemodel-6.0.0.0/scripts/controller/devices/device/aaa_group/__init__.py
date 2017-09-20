
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
import aaa_servers
import aaa_servers_private
import authentication
import authorization
import accounting
class aaa_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/aaa-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__tacacs_server_group','__vrf','__source_interface','__aaa_new_model','__aaa_servers','__aaa_servers_private','__authentication','__authorization','__accounting',)

  _yang_name = 'aaa-group'
  _module_name = 'basicDeviceConfigs'
  _namespace = 'http://anutanetworks.com/basicDeviceConfigs'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__aaa_new_model = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="aaa-new-model", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='boolean', is_config=True)
    self.__accounting = YANGDynClass(base=accounting.accounting, is_container='container', yang_name="accounting", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='container', is_config=True)
    self.__aaa_servers = YANGDynClass(base=YANGListType("aaa_server",aaa_servers.aaa_servers, yang_name="aaa-servers", module_name="basicDeviceConfigs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='aaa-server'), is_container='list', yang_name="aaa-servers", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='list', is_config=True)
    self.__authentication = YANGDynClass(base=authentication.authentication, is_container='container', yang_name="authentication", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='container', is_config=True)
    self.__vrf = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    self.__source_interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="source-interface", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    self.__aaa_servers_private = YANGDynClass(base=YANGListType("aaa_server_private",aaa_servers_private.aaa_servers_private, yang_name="aaa-servers-private", module_name="basicDeviceConfigs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='aaa-server-private'), is_container='list', yang_name="aaa-servers-private", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='list', is_config=True)
    self.__tacacs_server_group = YANGDynClass(base=unicode, is_leaf=True, yang_name="tacacs-server-group", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    self.__authorization = YANGDynClass(base=authorization.authorization, is_container='container', yang_name="authorization", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='container', is_config=True)

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
      return [u'devices', u'device', u'aaa-group']

  def _get_tacacs_server_group(self):
    """
    Getter method for tacacs_server_group, mapped from YANG variable /devices/device/aaa_group/tacacs_server_group (string)

    YANG Description: string
    """
    return self.__tacacs_server_group
      
  def _set_tacacs_server_group(self, v, load=False):
    """
    Setter method for tacacs_server_group, mapped from YANG variable /devices/device/aaa_group/tacacs_server_group (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tacacs_server_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tacacs_server_group() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="tacacs-server-group", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tacacs_server_group must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="tacacs-server-group", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)""",
        })

    self.__tacacs_server_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tacacs_server_group(self):
    self.__tacacs_server_group = YANGDynClass(base=unicode, is_leaf=True, yang_name="tacacs-server-group", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)


  def _get_vrf(self):
    """
    Getter method for vrf, mapped from YANG variable /devices/device/aaa_group/vrf (string)

    YANG Description: string
    """
    return self.__vrf
      
  def _set_vrf(self, v, load=False):
    """
    Setter method for vrf, mapped from YANG variable /devices/device/aaa_group/vrf (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vrf", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)""",
        })

    self.__vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf(self):
    self.__vrf = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)


  def _get_source_interface(self):
    """
    Getter method for source_interface, mapped from YANG variable /devices/device/aaa_group/source_interface (string)

    YANG Description: string
    """
    return self.__source_interface
      
  def _set_source_interface(self, v, load=False):
    """
    Setter method for source_interface, mapped from YANG variable /devices/device/aaa_group/source_interface (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_interface() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="source-interface", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_interface must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="source-interface", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)""",
        })

    self.__source_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_interface(self):
    self.__source_interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="source-interface", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='string', is_config=True)


  def _get_aaa_new_model(self):
    """
    Getter method for aaa_new_model, mapped from YANG variable /devices/device/aaa_group/aaa_new_model (boolean)

    YANG Description:  Enable NEW access control commands and functions.(Disables OLD commands.)
    """
    return self.__aaa_new_model
      
  def _set_aaa_new_model(self, v, load=False):
    """
    Setter method for aaa_new_model, mapped from YANG variable /devices/device/aaa_group/aaa_new_model (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aaa_new_model is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aaa_new_model() directly.

    YANG Description:  Enable NEW access control commands and functions.(Disables OLD commands.)
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="aaa-new-model", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aaa_new_model must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="aaa-new-model", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='boolean', is_config=True)""",
        })

    self.__aaa_new_model = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aaa_new_model(self):
    self.__aaa_new_model = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="aaa-new-model", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='boolean', is_config=True)


  def _get_aaa_servers(self):
    """
    Getter method for aaa_servers, mapped from YANG variable /devices/device/aaa_group/aaa_servers (list)
    """
    return self.__aaa_servers
      
  def _set_aaa_servers(self, v, load=False):
    """
    Setter method for aaa_servers, mapped from YANG variable /devices/device/aaa_group/aaa_servers (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aaa_servers is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aaa_servers() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("aaa_server",aaa_servers.aaa_servers, yang_name="aaa-servers", module_name="basicDeviceConfigs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='aaa-server'), is_container='list', yang_name="aaa-servers", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aaa_servers must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("aaa_server",aaa_servers.aaa_servers, yang_name="aaa-servers", module_name="basicDeviceConfigs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='aaa-server'), is_container='list', yang_name="aaa-servers", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='list', is_config=True)""",
        })

    self.__aaa_servers = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aaa_servers(self):
    self.__aaa_servers = YANGDynClass(base=YANGListType("aaa_server",aaa_servers.aaa_servers, yang_name="aaa-servers", module_name="basicDeviceConfigs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='aaa-server'), is_container='list', yang_name="aaa-servers", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='list', is_config=True)


  def _get_aaa_servers_private(self):
    """
    Getter method for aaa_servers_private, mapped from YANG variable /devices/device/aaa_group/aaa_servers_private (list)
    """
    return self.__aaa_servers_private
      
  def _set_aaa_servers_private(self, v, load=False):
    """
    Setter method for aaa_servers_private, mapped from YANG variable /devices/device/aaa_group/aaa_servers_private (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aaa_servers_private is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aaa_servers_private() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("aaa_server_private",aaa_servers_private.aaa_servers_private, yang_name="aaa-servers-private", module_name="basicDeviceConfigs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='aaa-server-private'), is_container='list', yang_name="aaa-servers-private", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aaa_servers_private must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("aaa_server_private",aaa_servers_private.aaa_servers_private, yang_name="aaa-servers-private", module_name="basicDeviceConfigs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='aaa-server-private'), is_container='list', yang_name="aaa-servers-private", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='list', is_config=True)""",
        })

    self.__aaa_servers_private = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aaa_servers_private(self):
    self.__aaa_servers_private = YANGDynClass(base=YANGListType("aaa_server_private",aaa_servers_private.aaa_servers_private, yang_name="aaa-servers-private", module_name="basicDeviceConfigs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='aaa-server-private'), is_container='list', yang_name="aaa-servers-private", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='list', is_config=True)


  def _get_authentication(self):
    """
    Getter method for authentication, mapped from YANG variable /devices/device/aaa_group/authentication (container)
    """
    return self.__authentication
      
  def _set_authentication(self, v, load=False):
    """
    Setter method for authentication, mapped from YANG variable /devices/device/aaa_group/authentication (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=authentication.authentication, is_container='container', yang_name="authentication", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=authentication.authentication, is_container='container', yang_name="authentication", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='container', is_config=True)""",
        })

    self.__authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication(self):
    self.__authentication = YANGDynClass(base=authentication.authentication, is_container='container', yang_name="authentication", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='container', is_config=True)


  def _get_authorization(self):
    """
    Getter method for authorization, mapped from YANG variable /devices/device/aaa_group/authorization (container)
    """
    return self.__authorization
      
  def _set_authorization(self, v, load=False):
    """
    Setter method for authorization, mapped from YANG variable /devices/device/aaa_group/authorization (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authorization is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authorization() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=authorization.authorization, is_container='container', yang_name="authorization", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authorization must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=authorization.authorization, is_container='container', yang_name="authorization", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='container', is_config=True)""",
        })

    self.__authorization = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authorization(self):
    self.__authorization = YANGDynClass(base=authorization.authorization, is_container='container', yang_name="authorization", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='container', is_config=True)


  def _get_accounting(self):
    """
    Getter method for accounting, mapped from YANG variable /devices/device/aaa_group/accounting (container)
    """
    return self.__accounting
      
  def _set_accounting(self, v, load=False):
    """
    Setter method for accounting, mapped from YANG variable /devices/device/aaa_group/accounting (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_accounting is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_accounting() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=accounting.accounting, is_container='container', yang_name="accounting", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """accounting must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=accounting.accounting, is_container='container', yang_name="accounting", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='container', is_config=True)""",
        })

    self.__accounting = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_accounting(self):
    self.__accounting = YANGDynClass(base=accounting.accounting, is_container='container', yang_name="accounting", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='container', is_config=True)

  tacacs_server_group = __builtin__.property(_get_tacacs_server_group, _set_tacacs_server_group)
  vrf = __builtin__.property(_get_vrf, _set_vrf)
  source_interface = __builtin__.property(_get_source_interface, _set_source_interface)
  aaa_new_model = __builtin__.property(_get_aaa_new_model, _set_aaa_new_model)
  aaa_servers = __builtin__.property(_get_aaa_servers, _set_aaa_servers)
  aaa_servers_private = __builtin__.property(_get_aaa_servers_private, _set_aaa_servers_private)
  authentication = __builtin__.property(_get_authentication, _set_authentication)
  authorization = __builtin__.property(_get_authorization, _set_authorization)
  accounting = __builtin__.property(_get_accounting, _set_accounting)


  _pyangbind_elements = collections.OrderedDict([('tacacs_server_group', tacacs_server_group), ('vrf', vrf), ('source_interface', source_interface), ('aaa_new_model', aaa_new_model), ('aaa_servers', aaa_servers), ('aaa_servers_private', aaa_servers_private), ('authentication', authentication), ('authorization', authorization), ('accounting', accounting), ])


