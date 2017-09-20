
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
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module infoblox - based on the path /infoblox_rpc/reserve-host-record-with-ext-attributes/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__device_id','__name','__view','__site_id','__cidn','__cust_name','__ip_address',)

  _yang_name = 'input'
  _module_name = 'infoblox'
  _namespace = 'http://anutanetworks.com/infoblox'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    self.__cidn = YANGDynClass(base=unicode, is_leaf=True, yang_name="cidn", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    self.__site_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="site-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    self.__cust_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="cust-name", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    self.__device_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="device-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='leafref', is_config=True)
    self.__ip_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-address", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    self.__view = YANGDynClass(base=unicode, is_leaf=True, yang_name="view", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)

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
      return [u'infoblox_rpc', u'reserve-host-record-with-ext-attributes', u'input']

  def _get_device_id(self):
    """
    Getter method for device_id, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/device_id (leafref)

    YANG Description: device-id
    """
    return self.__device_id
      
  def _set_device_id(self, v, load=False):
    """
    Setter method for device_id, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/device_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_device_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_device_id() directly.

    YANG Description: device-id
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="device-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """device_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="device-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='leafref', is_config=True)""",
        })

    self.__device_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_device_id(self):
    self.__device_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="device-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='leafref', is_config=True)


  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/name (string)

    YANG Description: string
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)


  def _get_view(self):
    """
    Getter method for view, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/view (string)

    YANG Description: string
    """
    return self.__view
      
  def _set_view(self, v, load=False):
    """
    Setter method for view, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/view (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_view is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_view() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="view", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """view must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="view", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.__view = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_view(self):
    self.__view = YANGDynClass(base=unicode, is_leaf=True, yang_name="view", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)


  def _get_site_id(self):
    """
    Getter method for site_id, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/site_id (string)

    YANG Description: string
    """
    return self.__site_id
      
  def _set_site_id(self, v, load=False):
    """
    Setter method for site_id, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/site_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_site_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_site_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="site-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """site_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="site-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.__site_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_site_id(self):
    self.__site_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="site-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)


  def _get_cidn(self):
    """
    Getter method for cidn, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/cidn (string)

    YANG Description: string
    """
    return self.__cidn
      
  def _set_cidn(self, v, load=False):
    """
    Setter method for cidn, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/cidn (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cidn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cidn() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="cidn", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cidn must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="cidn", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.__cidn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cidn(self):
    self.__cidn = YANGDynClass(base=unicode, is_leaf=True, yang_name="cidn", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)


  def _get_cust_name(self):
    """
    Getter method for cust_name, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/cust_name (string)

    YANG Description: string
    """
    return self.__cust_name
      
  def _set_cust_name(self, v, load=False):
    """
    Setter method for cust_name, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/cust_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cust_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cust_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="cust-name", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cust_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="cust-name", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.__cust_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cust_name(self):
    self.__cust_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="cust-name", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)


  def _get_ip_address(self):
    """
    Getter method for ip_address, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/ip_address (string)

    YANG Description: string
    """
    return self.__ip_address
      
  def _set_ip_address(self, v, load=False):
    """
    Setter method for ip_address, mapped from YANG variable /infoblox_rpc/reserve_host_record_with_ext_attributes/input/ip_address (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_address() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ip-address", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_address must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-address", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.__ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_address(self):
    self.__ip_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-address", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)

  device_id = __builtin__.property(_get_device_id, _set_device_id)
  name = __builtin__.property(_get_name, _set_name)
  view = __builtin__.property(_get_view, _set_view)
  site_id = __builtin__.property(_get_site_id, _set_site_id)
  cidn = __builtin__.property(_get_cidn, _set_cidn)
  cust_name = __builtin__.property(_get_cust_name, _set_cust_name)
  ip_address = __builtin__.property(_get_ip_address, _set_ip_address)


  _pyangbind_elements = collections.OrderedDict([('device_id', device_id), ('name', name), ('view', view), ('site_id', site_id), ('cidn', cidn), ('cust_name', cust_name), ('ip_address', ip_address), ])


