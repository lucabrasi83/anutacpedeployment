
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
class http(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/http. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__no_ip_http_server','__no_ip_http_secure_server',)

  _yang_name = 'http'
  _module_name = 'basicDeviceConfigs'
  _namespace = 'http://anutanetworks.com/basicDeviceConfigs'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__no_ip_http_secure_server = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="no-ip-http-secure-server", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='boolean', is_config=True)
    self.__no_ip_http_server = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="no-ip-http-server", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='boolean', is_config=True)

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
      return [u'devices', u'device', u'http']

  def _get_no_ip_http_server(self):
    """
    Getter method for no_ip_http_server, mapped from YANG variable /devices/device/http/no_ip_http_server (boolean)

    YANG Description: no-ip-http-server: True/False
    """
    return self.__no_ip_http_server
      
  def _set_no_ip_http_server(self, v, load=False):
    """
    Setter method for no_ip_http_server, mapped from YANG variable /devices/device/http/no_ip_http_server (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_ip_http_server is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_ip_http_server() directly.

    YANG Description: no-ip-http-server: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="no-ip-http-server", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_ip_http_server must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="no-ip-http-server", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='boolean', is_config=True)""",
        })

    self.__no_ip_http_server = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_ip_http_server(self):
    self.__no_ip_http_server = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="no-ip-http-server", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='boolean', is_config=True)


  def _get_no_ip_http_secure_server(self):
    """
    Getter method for no_ip_http_secure_server, mapped from YANG variable /devices/device/http/no_ip_http_secure_server (boolean)

    YANG Description: no-ip-http-secure-server: True/False
    """
    return self.__no_ip_http_secure_server
      
  def _set_no_ip_http_secure_server(self, v, load=False):
    """
    Setter method for no_ip_http_secure_server, mapped from YANG variable /devices/device/http/no_ip_http_secure_server (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_ip_http_secure_server is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_ip_http_secure_server() directly.

    YANG Description: no-ip-http-secure-server: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="no-ip-http-secure-server", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_ip_http_secure_server must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="no-ip-http-secure-server", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='boolean', is_config=True)""",
        })

    self.__no_ip_http_secure_server = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_ip_http_secure_server(self):
    self.__no_ip_http_secure_server = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="no-ip-http-secure-server", module_name="basicDeviceConfigs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/basicDeviceConfigs', defining_module='basicDeviceConfigs', yang_type='boolean', is_config=True)

  no_ip_http_server = __builtin__.property(_get_no_ip_http_server, _set_no_ip_http_server)
  no_ip_http_secure_server = __builtin__.property(_get_no_ip_http_secure_server, _set_no_ip_http_secure_server)


  _pyangbind_elements = collections.OrderedDict([('no_ip_http_server', no_ip_http_server), ('no_ip_http_secure_server', no_ip_http_secure_server), ])


