
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
import general_service_settings
import peering_rules
import transport_settings
import service_ports
class network_services(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/network-services. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__general_service_settings','__peering_rules','__transport_settings','__service_ports',)

  _yang_name = 'network-services'
  _module_name = 'wanoptimizer'
  _namespace = 'http://anutanetworks.com/wanoptimizer'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__peering_rules = YANGDynClass(base=peering_rules.peering_rules, is_container='container', yang_name="peering-rules", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)
    self.__transport_settings = YANGDynClass(base=transport_settings.transport_settings, is_container='container', yang_name="transport-settings", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)
    self.__general_service_settings = YANGDynClass(base=general_service_settings.general_service_settings, is_container='container', yang_name="general-service-settings", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)
    self.__service_ports = YANGDynClass(base=service_ports.service_ports, is_container='container', yang_name="service-ports", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)

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
      return [u'devices', u'device', u'network-services']

  def _get_general_service_settings(self):
    """
    Getter method for general_service_settings, mapped from YANG variable /devices/device/network_services/general_service_settings (container)
    """
    return self.__general_service_settings
      
  def _set_general_service_settings(self, v, load=False):
    """
    Setter method for general_service_settings, mapped from YANG variable /devices/device/network_services/general_service_settings (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_general_service_settings is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_general_service_settings() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=general_service_settings.general_service_settings, is_container='container', yang_name="general-service-settings", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """general_service_settings must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=general_service_settings.general_service_settings, is_container='container', yang_name="general-service-settings", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)""",
        })

    self.__general_service_settings = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_general_service_settings(self):
    self.__general_service_settings = YANGDynClass(base=general_service_settings.general_service_settings, is_container='container', yang_name="general-service-settings", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)


  def _get_peering_rules(self):
    """
    Getter method for peering_rules, mapped from YANG variable /devices/device/network_services/peering_rules (container)
    """
    return self.__peering_rules
      
  def _set_peering_rules(self, v, load=False):
    """
    Setter method for peering_rules, mapped from YANG variable /devices/device/network_services/peering_rules (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peering_rules is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peering_rules() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=peering_rules.peering_rules, is_container='container', yang_name="peering-rules", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peering_rules must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=peering_rules.peering_rules, is_container='container', yang_name="peering-rules", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)""",
        })

    self.__peering_rules = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peering_rules(self):
    self.__peering_rules = YANGDynClass(base=peering_rules.peering_rules, is_container='container', yang_name="peering-rules", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)


  def _get_transport_settings(self):
    """
    Getter method for transport_settings, mapped from YANG variable /devices/device/network_services/transport_settings (container)
    """
    return self.__transport_settings
      
  def _set_transport_settings(self, v, load=False):
    """
    Setter method for transport_settings, mapped from YANG variable /devices/device/network_services/transport_settings (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transport_settings is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transport_settings() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=transport_settings.transport_settings, is_container='container', yang_name="transport-settings", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transport_settings must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=transport_settings.transport_settings, is_container='container', yang_name="transport-settings", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)""",
        })

    self.__transport_settings = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transport_settings(self):
    self.__transport_settings = YANGDynClass(base=transport_settings.transport_settings, is_container='container', yang_name="transport-settings", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)


  def _get_service_ports(self):
    """
    Getter method for service_ports, mapped from YANG variable /devices/device/network_services/service_ports (container)
    """
    return self.__service_ports
      
  def _set_service_ports(self, v, load=False):
    """
    Setter method for service_ports, mapped from YANG variable /devices/device/network_services/service_ports (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_service_ports is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_service_ports() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=service_ports.service_ports, is_container='container', yang_name="service-ports", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """service_ports must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=service_ports.service_ports, is_container='container', yang_name="service-ports", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)""",
        })

    self.__service_ports = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_service_ports(self):
    self.__service_ports = YANGDynClass(base=service_ports.service_ports, is_container='container', yang_name="service-ports", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)

  general_service_settings = __builtin__.property(_get_general_service_settings, _set_general_service_settings)
  peering_rules = __builtin__.property(_get_peering_rules, _set_peering_rules)
  transport_settings = __builtin__.property(_get_transport_settings, _set_transport_settings)
  service_ports = __builtin__.property(_get_service_ports, _set_service_ports)


  _pyangbind_elements = collections.OrderedDict([('general_service_settings', general_service_settings), ('peering_rules', peering_rules), ('transport_settings', transport_settings), ('service_ports', service_ports), ])


