
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
import network
import match_conditions
import eigrp
class router_eigrp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/vrfs/vrf/router-eigrp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__process_id','__eigrp_stub','__network','__match_conditions','__eigrp',)

  _yang_name = 'router-eigrp'
  _module_name = 'l3features'
  _namespace = 'http://anutanetworks.com/l3features'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__match_conditions = YANGDynClass(base=match_conditions.match_conditions, is_container='container', yang_name="match-conditions", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    self.__eigrp = YANGDynClass(base=YANGListType("process_id",eigrp.eigrp, yang_name="eigrp", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='process-id'), is_container='list', yang_name="eigrp", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)
    self.__process_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="process-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='process-id', is_config=True)
    self.__eigrp_stub = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static': {}, u'receive-only': {}, u'connected': {}, u'summary': {}},), is_leaf=True, yang_name="eigrp-stub", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)
    self.__network = YANGDynClass(base=YANGListType("ip_address",network.network, yang_name="network", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address'), is_container='list', yang_name="network", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)

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
      return [u'devices', u'device', u'vrfs', u'vrf', u'router-eigrp']

  def _get_process_id(self):
    """
    Getter method for process_id, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/process_id (process-id)

    YANG Description: 1..65535
    """
    return self.__process_id
      
  def _set_process_id(self, v, load=False):
    """
    Setter method for process_id, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/process_id (process-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_process_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_process_id() directly.

    YANG Description: 1..65535
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="process-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='process-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """process_id must be of a type compatible with process-id""",
          'defined-type': "l3features:process-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="process-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='process-id', is_config=True)""",
        })

    self.__process_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_process_id(self):
    self.__process_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="process-id", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='process-id', is_config=True)


  def _get_eigrp_stub(self):
    """
    Getter method for eigrp_stub, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/eigrp_stub (enumeration)

    YANG Description: receive-only
connected
static
summary

    """
    return self.__eigrp_stub
      
  def _set_eigrp_stub(self, v, load=False):
    """
    Setter method for eigrp_stub, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/eigrp_stub (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_eigrp_stub is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_eigrp_stub() directly.

    YANG Description: receive-only
connected
static
summary

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static': {}, u'receive-only': {}, u'connected': {}, u'summary': {}},), is_leaf=True, yang_name="eigrp-stub", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """eigrp_stub must be of a type compatible with enumeration""",
          'defined-type': "l3features:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static': {}, u'receive-only': {}, u'connected': {}, u'summary': {}},), is_leaf=True, yang_name="eigrp-stub", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)""",
        })

    self.__eigrp_stub = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_eigrp_stub(self):
    self.__eigrp_stub = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static': {}, u'receive-only': {}, u'connected': {}, u'summary': {}},), is_leaf=True, yang_name="eigrp-stub", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='enumeration', is_config=True)


  def _get_network(self):
    """
    Getter method for network, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/network (list)
    """
    return self.__network
      
  def _set_network(self, v, load=False):
    """
    Setter method for network, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/network (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("ip_address",network.network, yang_name="network", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address'), is_container='list', yang_name="network", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ip_address",network.network, yang_name="network", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address'), is_container='list', yang_name="network", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)""",
        })

    self.__network = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network(self):
    self.__network = YANGDynClass(base=YANGListType("ip_address",network.network, yang_name="network", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address'), is_container='list', yang_name="network", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)


  def _get_match_conditions(self):
    """
    Getter method for match_conditions, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/match_conditions (container)
    """
    return self.__match_conditions
      
  def _set_match_conditions(self, v, load=False):
    """
    Setter method for match_conditions, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/match_conditions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match_conditions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match_conditions() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=match_conditions.match_conditions, is_container='container', yang_name="match-conditions", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match_conditions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=match_conditions.match_conditions, is_container='container', yang_name="match-conditions", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)""",
        })

    self.__match_conditions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match_conditions(self):
    self.__match_conditions = YANGDynClass(base=match_conditions.match_conditions, is_container='container', yang_name="match-conditions", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)


  def _get_eigrp(self):
    """
    Getter method for eigrp, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/eigrp (list)
    """
    return self.__eigrp
      
  def _set_eigrp(self, v, load=False):
    """
    Setter method for eigrp, mapped from YANG variable /devices/device/vrfs/vrf/router_eigrp/eigrp (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_eigrp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_eigrp() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("process_id",eigrp.eigrp, yang_name="eigrp", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='process-id'), is_container='list', yang_name="eigrp", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """eigrp must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("process_id",eigrp.eigrp, yang_name="eigrp", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='process-id'), is_container='list', yang_name="eigrp", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)""",
        })

    self.__eigrp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_eigrp(self):
    self.__eigrp = YANGDynClass(base=YANGListType("process_id",eigrp.eigrp, yang_name="eigrp", module_name="l3features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='process-id'), is_container='list', yang_name="eigrp", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='list', is_config=True)

  process_id = __builtin__.property(_get_process_id, _set_process_id)
  eigrp_stub = __builtin__.property(_get_eigrp_stub, _set_eigrp_stub)
  network = __builtin__.property(_get_network, _set_network)
  match_conditions = __builtin__.property(_get_match_conditions, _set_match_conditions)
  eigrp = __builtin__.property(_get_eigrp, _set_eigrp)


  _pyangbind_elements = collections.OrderedDict([('process_id', process_id), ('eigrp_stub', eigrp_stub), ('network', network), ('match_conditions', match_conditions), ('eigrp', eigrp), ])


