
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
import static
import associate_profile
import backup_neighbor
import oam
class neighbor(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/vpls/neighbor. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Neighbor for this VPLS instance
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__neighbor_id','__static','__associate_profile','__psn_tunnel_endpoint','__community','__encapsulation_type','__ignore_encapsulation_mismatch','__pseudowire_status_tlv','__switchover_delay','__revert_time','__connection_protection','__backup_neighbor','__oam',)

  _yang_name = 'neighbor'
  _module_name = 'vpls'
  _namespace = 'http://anutanetworks.com/vpls'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__backup_neighbor = YANGDynClass(base=YANGListType("neighbor_id",backup_neighbor.backup_neighbor, yang_name="backup-neighbor", module_name="vpls", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='neighbor-id'), is_container='list', yang_name="backup-neighbor", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='list', is_config=True)
    self.__associate_profile = YANGDynClass(base=associate_profile.associate_profile, is_container='container', yang_name="associate-profile", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)
    self.__psn_tunnel_endpoint = YANGDynClass(base=unicode, is_leaf=True, yang_name="psn-tunnel-endpoint", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='ipv4addr', is_config=True)
    self.__oam = YANGDynClass(base=oam.oam, is_container='container', yang_name="oam", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)
    self.__connection_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="connection-protection", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)
    self.__community = YANGDynClass(base=unicode, is_leaf=True, yang_name="community", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='string', is_config=True)
    self.__pseudowire_status_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pseudowire-status-tlv", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)
    self.__static = YANGDynClass(base=static.static, is_container='container', yang_name="static", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)
    self.__revert_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 600']}), is_leaf=True, yang_name="revert-time", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)
    self.__switchover_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 180000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10000), is_leaf=True, yang_name="switchover-delay", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)
    self.__encapsulation_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet-vlan': {}, u'ethernet': {}},), is_leaf=True, yang_name="encapsulation-type", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='enumeration', is_config=True)
    self.__ignore_encapsulation_mismatch = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ignore-encapsulation-mismatch", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)
    self.__neighbor_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor-id", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='ipv4addr', is_config=True)

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
      return [u'devices', u'device', u'vpls', u'neighbor']

  def _get_neighbor_id(self):
    """
    Getter method for neighbor_id, mapped from YANG variable /devices/device/vpls/neighbor/neighbor_id (ipv4addr)

    YANG Description: Neighbor ID
    """
    return self.__neighbor_id
      
  def _set_neighbor_id(self, v, load=False):
    """
    Setter method for neighbor_id, mapped from YANG variable /devices/device/vpls/neighbor/neighbor_id (ipv4addr)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_id() directly.

    YANG Description: Neighbor ID
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="neighbor-id", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='ipv4addr', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_id must be of a type compatible with ipv4addr""",
          'defined-type': "vpls:ipv4addr",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor-id", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='ipv4addr', is_config=True)""",
        })

    self.__neighbor_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_id(self):
    self.__neighbor_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor-id", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='ipv4addr', is_config=True)


  def _get_static(self):
    """
    Getter method for static, mapped from YANG variable /devices/device/vpls/neighbor/static (container)

    YANG Description: Configuration of static vpls
    """
    return self.__static
      
  def _set_static(self, v, load=False):
    """
    Setter method for static, mapped from YANG variable /devices/device/vpls/neighbor/static (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static() directly.

    YANG Description: Configuration of static vpls
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=static.static, is_container='container', yang_name="static", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=static.static, is_container='container', yang_name="static", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)""",
        })

    self.__static = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static(self):
    self.__static = YANGDynClass(base=static.static, is_container='container', yang_name="static", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)


  def _get_associate_profile(self):
    """
    Getter method for associate_profile, mapped from YANG variable /devices/device/vpls/neighbor/associate_profile (container)

    YANG Description: Associate profile options for dynamic IFL
    """
    return self.__associate_profile
      
  def _set_associate_profile(self, v, load=False):
    """
    Setter method for associate_profile, mapped from YANG variable /devices/device/vpls/neighbor/associate_profile (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_associate_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_associate_profile() directly.

    YANG Description: Associate profile options for dynamic IFL
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=associate_profile.associate_profile, is_container='container', yang_name="associate-profile", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """associate_profile must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=associate_profile.associate_profile, is_container='container', yang_name="associate-profile", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)""",
        })

    self.__associate_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_associate_profile(self):
    self.__associate_profile = YANGDynClass(base=associate_profile.associate_profile, is_container='container', yang_name="associate-profile", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)


  def _get_psn_tunnel_endpoint(self):
    """
    Getter method for psn_tunnel_endpoint, mapped from YANG variable /devices/device/vpls/neighbor/psn_tunnel_endpoint (ipv4addr)

    YANG Description: Endpoint of the transport tunnel on the remote PE
    """
    return self.__psn_tunnel_endpoint
      
  def _set_psn_tunnel_endpoint(self, v, load=False):
    """
    Setter method for psn_tunnel_endpoint, mapped from YANG variable /devices/device/vpls/neighbor/psn_tunnel_endpoint (ipv4addr)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_psn_tunnel_endpoint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_psn_tunnel_endpoint() directly.

    YANG Description: Endpoint of the transport tunnel on the remote PE
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="psn-tunnel-endpoint", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='ipv4addr', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """psn_tunnel_endpoint must be of a type compatible with ipv4addr""",
          'defined-type': "vpls:ipv4addr",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="psn-tunnel-endpoint", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='ipv4addr', is_config=True)""",
        })

    self.__psn_tunnel_endpoint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_psn_tunnel_endpoint(self):
    self.__psn_tunnel_endpoint = YANGDynClass(base=unicode, is_leaf=True, yang_name="psn-tunnel-endpoint", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='ipv4addr', is_config=True)


  def _get_community(self):
    """
    Getter method for community, mapped from YANG variable /devices/device/vpls/neighbor/community (string)

    YANG Description: Community associated with this neighbor
    """
    return self.__community
      
  def _set_community(self, v, load=False):
    """
    Setter method for community, mapped from YANG variable /devices/device/vpls/neighbor/community (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_community() directly.

    YANG Description: Community associated with this neighbor
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="community", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """community must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="community", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='string', is_config=True)""",
        })

    self.__community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_community(self):
    self.__community = YANGDynClass(base=unicode, is_leaf=True, yang_name="community", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='string', is_config=True)


  def _get_encapsulation_type(self):
    """
    Getter method for encapsulation_type, mapped from YANG variable /devices/device/vpls/neighbor/encapsulation_type (enumeration)

    YANG Description: Encapsulation type for VPN
    """
    return self.__encapsulation_type
      
  def _set_encapsulation_type(self, v, load=False):
    """
    Setter method for encapsulation_type, mapped from YANG variable /devices/device/vpls/neighbor/encapsulation_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encapsulation_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encapsulation_type() directly.

    YANG Description: Encapsulation type for VPN
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet-vlan': {}, u'ethernet': {}},), is_leaf=True, yang_name="encapsulation-type", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encapsulation_type must be of a type compatible with enumeration""",
          'defined-type': "vpls:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet-vlan': {}, u'ethernet': {}},), is_leaf=True, yang_name="encapsulation-type", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='enumeration', is_config=True)""",
        })

    self.__encapsulation_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encapsulation_type(self):
    self.__encapsulation_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet-vlan': {}, u'ethernet': {}},), is_leaf=True, yang_name="encapsulation-type", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='enumeration', is_config=True)


  def _get_ignore_encapsulation_mismatch(self):
    """
    Getter method for ignore_encapsulation_mismatch, mapped from YANG variable /devices/device/vpls/neighbor/ignore_encapsulation_mismatch (empty)

    YANG Description: Allow different encapsulation types on local and remote end
    """
    return self.__ignore_encapsulation_mismatch
      
  def _set_ignore_encapsulation_mismatch(self, v, load=False):
    """
    Setter method for ignore_encapsulation_mismatch, mapped from YANG variable /devices/device/vpls/neighbor/ignore_encapsulation_mismatch (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ignore_encapsulation_mismatch is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ignore_encapsulation_mismatch() directly.

    YANG Description: Allow different encapsulation types on local and remote end
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ignore-encapsulation-mismatch", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ignore_encapsulation_mismatch must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ignore-encapsulation-mismatch", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)""",
        })

    self.__ignore_encapsulation_mismatch = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ignore_encapsulation_mismatch(self):
    self.__ignore_encapsulation_mismatch = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ignore-encapsulation-mismatch", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)


  def _get_pseudowire_status_tlv(self):
    """
    Getter method for pseudowire_status_tlv, mapped from YANG variable /devices/device/vpls/neighbor/pseudowire_status_tlv (empty)

    YANG Description: Send pseudowire status TLV
    """
    return self.__pseudowire_status_tlv
      
  def _set_pseudowire_status_tlv(self, v, load=False):
    """
    Setter method for pseudowire_status_tlv, mapped from YANG variable /devices/device/vpls/neighbor/pseudowire_status_tlv (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pseudowire_status_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pseudowire_status_tlv() directly.

    YANG Description: Send pseudowire status TLV
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="pseudowire-status-tlv", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pseudowire_status_tlv must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pseudowire-status-tlv", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)""",
        })

    self.__pseudowire_status_tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pseudowire_status_tlv(self):
    self.__pseudowire_status_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pseudowire-status-tlv", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)


  def _get_switchover_delay(self):
    """
    Getter method for switchover_delay, mapped from YANG variable /devices/device/vpls/neighbor/switchover_delay (uint32)

    YANG Description: Pseudowire switchover delay 
    """
    return self.__switchover_delay
      
  def _set_switchover_delay(self, v, load=False):
    """
    Setter method for switchover_delay, mapped from YANG variable /devices/device/vpls/neighbor/switchover_delay (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_switchover_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_switchover_delay() directly.

    YANG Description: Pseudowire switchover delay 
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 180000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10000), is_leaf=True, yang_name="switchover-delay", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """switchover_delay must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 180000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10000), is_leaf=True, yang_name="switchover-delay", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)""",
        })

    self.__switchover_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_switchover_delay(self):
    self.__switchover_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 180000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10000), is_leaf=True, yang_name="switchover-delay", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)


  def _get_revert_time(self):
    """
    Getter method for revert_time, mapped from YANG variable /devices/device/vpls/neighbor/revert_time (uint32)

    YANG Description: Enable pseudowire redundancy reversion (seconds)
    """
    return self.__revert_time
      
  def _set_revert_time(self, v, load=False):
    """
    Setter method for revert_time, mapped from YANG variable /devices/device/vpls/neighbor/revert_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_revert_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_revert_time() directly.

    YANG Description: Enable pseudowire redundancy reversion (seconds)
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 600']}), is_leaf=True, yang_name="revert-time", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """revert_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 600']}), is_leaf=True, yang_name="revert-time", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)""",
        })

    self.__revert_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_revert_time(self):
    self.__revert_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 600']}), is_leaf=True, yang_name="revert-time", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='uint32', is_config=True)


  def _get_connection_protection(self):
    """
    Getter method for connection_protection, mapped from YANG variable /devices/device/vpls/neighbor/connection_protection (empty)

    YANG Description: End-2-end protection via OAM failure detection
    """
    return self.__connection_protection
      
  def _set_connection_protection(self, v, load=False):
    """
    Setter method for connection_protection, mapped from YANG variable /devices/device/vpls/neighbor/connection_protection (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_protection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_protection() directly.

    YANG Description: End-2-end protection via OAM failure detection
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="connection-protection", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_protection must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="connection-protection", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)""",
        })

    self.__connection_protection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_protection(self):
    self.__connection_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="connection-protection", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)


  def _get_backup_neighbor(self):
    """
    Getter method for backup_neighbor, mapped from YANG variable /devices/device/vpls/neighbor/backup_neighbor (list)

    YANG Description: Configuration of redundant l2circuit
    """
    return self.__backup_neighbor
      
  def _set_backup_neighbor(self, v, load=False):
    """
    Setter method for backup_neighbor, mapped from YANG variable /devices/device/vpls/neighbor/backup_neighbor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_backup_neighbor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_backup_neighbor() directly.

    YANG Description: Configuration of redundant l2circuit
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("neighbor_id",backup_neighbor.backup_neighbor, yang_name="backup-neighbor", module_name="vpls", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='neighbor-id'), is_container='list', yang_name="backup-neighbor", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """backup_neighbor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("neighbor_id",backup_neighbor.backup_neighbor, yang_name="backup-neighbor", module_name="vpls", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='neighbor-id'), is_container='list', yang_name="backup-neighbor", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='list', is_config=True)""",
        })

    self.__backup_neighbor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_backup_neighbor(self):
    self.__backup_neighbor = YANGDynClass(base=YANGListType("neighbor_id",backup_neighbor.backup_neighbor, yang_name="backup-neighbor", module_name="vpls", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='neighbor-id'), is_container='list', yang_name="backup-neighbor", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='list', is_config=True)


  def _get_oam(self):
    """
    Getter method for oam, mapped from YANG variable /devices/device/vpls/neighbor/oam (container)

    YANG Description: OAM Configuration for VPN
    """
    return self.__oam
      
  def _set_oam(self, v, load=False):
    """
    Setter method for oam, mapped from YANG variable /devices/device/vpls/neighbor/oam (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oam is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oam() directly.

    YANG Description: OAM Configuration for VPN
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=oam.oam, is_container='container', yang_name="oam", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oam must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=oam.oam, is_container='container', yang_name="oam", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)""",
        })

    self.__oam = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oam(self):
    self.__oam = YANGDynClass(base=oam.oam, is_container='container', yang_name="oam", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)

  neighbor_id = __builtin__.property(_get_neighbor_id, _set_neighbor_id)
  static = __builtin__.property(_get_static, _set_static)
  associate_profile = __builtin__.property(_get_associate_profile, _set_associate_profile)
  psn_tunnel_endpoint = __builtin__.property(_get_psn_tunnel_endpoint, _set_psn_tunnel_endpoint)
  community = __builtin__.property(_get_community, _set_community)
  encapsulation_type = __builtin__.property(_get_encapsulation_type, _set_encapsulation_type)
  ignore_encapsulation_mismatch = __builtin__.property(_get_ignore_encapsulation_mismatch, _set_ignore_encapsulation_mismatch)
  pseudowire_status_tlv = __builtin__.property(_get_pseudowire_status_tlv, _set_pseudowire_status_tlv)
  switchover_delay = __builtin__.property(_get_switchover_delay, _set_switchover_delay)
  revert_time = __builtin__.property(_get_revert_time, _set_revert_time)
  connection_protection = __builtin__.property(_get_connection_protection, _set_connection_protection)
  backup_neighbor = __builtin__.property(_get_backup_neighbor, _set_backup_neighbor)
  oam = __builtin__.property(_get_oam, _set_oam)


  _pyangbind_elements = collections.OrderedDict([('neighbor_id', neighbor_id), ('static', static), ('associate_profile', associate_profile), ('psn_tunnel_endpoint', psn_tunnel_endpoint), ('community', community), ('encapsulation_type', encapsulation_type), ('ignore_encapsulation_mismatch', ignore_encapsulation_mismatch), ('pseudowire_status_tlv', pseudowire_status_tlv), ('switchover_delay', switchover_delay), ('revert_time', revert_time), ('connection_protection', connection_protection), ('backup_neighbor', backup_neighbor), ('oam', oam), ])


