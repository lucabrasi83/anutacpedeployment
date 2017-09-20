
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
class redistribute(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/virtual-devices/virtual-device/router-ospf/redistribute. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__protocol','__bgp_as_number','__metric','__routemap_name',)

  _yang_name = 'redistribute'
  _module_name = 'firewall'
  _namespace = 'http://anutanetworks.com/firewall'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='uint32', is_config=True)
    self.__bgp_as_number = YANGDynClass(base=unicode, is_leaf=True, yang_name="bgp-as-number", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='l3:as-number', is_config=True)
    self.__protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static-connected': {}, u'redistribute-connected': {}, u'rip': {}, u'bgp': {}, u'eigrp': {}, u'connected': {}, u'static': {}, u'ospf': {}},), is_leaf=True, yang_name="protocol", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='protocol', is_config=True)
    self.__routemap_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="routemap-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'virtual-devices', u'virtual-device', u'router-ospf', u'redistribute']

  def _get_protocol(self):
    """
    Getter method for protocol, mapped from YANG variable /devices/device/virtual_devices/virtual_device/router_ospf/redistribute/protocol (protocol)

    YANG Description: static
rip
ospf
bgp
eigrp
connected
static-connected
redistribute-connected

    """
    return self.__protocol
      
  def _set_protocol(self, v, load=False):
    """
    Setter method for protocol, mapped from YANG variable /devices/device/virtual_devices/virtual_device/router_ospf/redistribute/protocol (protocol)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol() directly.

    YANG Description: static
rip
ospf
bgp
eigrp
connected
static-connected
redistribute-connected

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static-connected': {}, u'redistribute-connected': {}, u'rip': {}, u'bgp': {}, u'eigrp': {}, u'connected': {}, u'static': {}, u'ospf': {}},), is_leaf=True, yang_name="protocol", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='protocol', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol must be of a type compatible with protocol""",
          'defined-type': "firewall:protocol",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static-connected': {}, u'redistribute-connected': {}, u'rip': {}, u'bgp': {}, u'eigrp': {}, u'connected': {}, u'static': {}, u'ospf': {}},), is_leaf=True, yang_name="protocol", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='protocol', is_config=True)""",
        })

    self.__protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol(self):
    self.__protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static-connected': {}, u'redistribute-connected': {}, u'rip': {}, u'bgp': {}, u'eigrp': {}, u'connected': {}, u'static': {}, u'ospf': {}},), is_leaf=True, yang_name="protocol", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='protocol', is_config=True)


  def _get_bgp_as_number(self):
    """
    Getter method for bgp_as_number, mapped from YANG variable /devices/device/virtual_devices/virtual_device/router_ospf/redistribute/bgp_as_number (l3:as-number)

    YANG Description: string
    """
    return self.__bgp_as_number
      
  def _set_bgp_as_number(self, v, load=False):
    """
    Setter method for bgp_as_number, mapped from YANG variable /devices/device/virtual_devices/virtual_device/router_ospf/redistribute/bgp_as_number (l3:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bgp_as_number is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bgp_as_number() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="bgp-as-number", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='l3:as-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bgp_as_number must be of a type compatible with l3:as-number""",
          'defined-type': "l3:as-number",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="bgp-as-number", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='l3:as-number', is_config=True)""",
        })

    self.__bgp_as_number = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bgp_as_number(self):
    self.__bgp_as_number = YANGDynClass(base=unicode, is_leaf=True, yang_name="bgp-as-number", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='l3:as-number', is_config=True)


  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /devices/device/virtual_devices/virtual_device/router_ospf/redistribute/metric (uint32)

    YANG Description: 0..4294967295
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /devices/device/virtual_devices/virtual_device/router_ospf/redistribute/metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='uint32', is_config=True)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='uint32', is_config=True)


  def _get_routemap_name(self):
    """
    Getter method for routemap_name, mapped from YANG variable /devices/device/virtual_devices/virtual_device/router_ospf/redistribute/routemap_name (string)

    YANG Description: string
    """
    return self.__routemap_name
      
  def _set_routemap_name(self, v, load=False):
    """
    Setter method for routemap_name, mapped from YANG variable /devices/device/virtual_devices/virtual_device/router_ospf/redistribute/routemap_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_routemap_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_routemap_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="routemap-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """routemap_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="routemap-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)""",
        })

    self.__routemap_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_routemap_name(self):
    self.__routemap_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="routemap-name", module_name="firewall", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/firewall', defining_module='firewall', yang_type='string', is_config=True)

  protocol = __builtin__.property(_get_protocol, _set_protocol)
  bgp_as_number = __builtin__.property(_get_bgp_as_number, _set_bgp_as_number)
  metric = __builtin__.property(_get_metric, _set_metric)
  routemap_name = __builtin__.property(_get_routemap_name, _set_routemap_name)


  _pyangbind_elements = collections.OrderedDict([('protocol', protocol), ('bgp_as_number', bgp_as_number), ('metric', metric), ('routemap_name', routemap_name), ])


