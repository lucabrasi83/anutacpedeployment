
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
class backup_neighbor(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/vpls/mesh-group/neighbor/backup-neighbor. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration of redundant l2circuit
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__neighbor_id','__static','__community','__psn_tunnel_endpoint','__standby',)

  _yang_name = 'backup-neighbor'
  _module_name = 'vpls'
  _namespace = 'http://anutanetworks.com/vpls'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__standby = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="standby", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)
    self.__static = YANGDynClass(base=static.static, is_container='container', yang_name="static", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='container', is_config=True)
    self.__neighbor_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor-id", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='ipv4addr', is_config=True)
    self.__community = YANGDynClass(base=unicode, is_leaf=True, yang_name="community", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='string', is_config=True)
    self.__psn_tunnel_endpoint = YANGDynClass(base=unicode, is_leaf=True, yang_name="psn-tunnel-endpoint", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='ipv4addr', is_config=True)

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
      return [u'devices', u'device', u'vpls', u'mesh-group', u'neighbor', u'backup-neighbor']

  def _get_neighbor_id(self):
    """
    Getter method for neighbor_id, mapped from YANG variable /devices/device/vpls/mesh_group/neighbor/backup_neighbor/neighbor_id (ipv4addr)

    YANG Description: Neighbor ID
    """
    return self.__neighbor_id
      
  def _set_neighbor_id(self, v, load=False):
    """
    Setter method for neighbor_id, mapped from YANG variable /devices/device/vpls/mesh_group/neighbor/backup_neighbor/neighbor_id (ipv4addr)
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
    Getter method for static, mapped from YANG variable /devices/device/vpls/mesh_group/neighbor/backup_neighbor/static (container)

    YANG Description: Configuration of static vpls
    """
    return self.__static
      
  def _set_static(self, v, load=False):
    """
    Setter method for static, mapped from YANG variable /devices/device/vpls/mesh_group/neighbor/backup_neighbor/static (container)
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


  def _get_community(self):
    """
    Getter method for community, mapped from YANG variable /devices/device/vpls/mesh_group/neighbor/backup_neighbor/community (string)

    YANG Description: Community associated with this Layer 2 circuit
    """
    return self.__community
      
  def _set_community(self, v, load=False):
    """
    Setter method for community, mapped from YANG variable /devices/device/vpls/mesh_group/neighbor/backup_neighbor/community (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_community() directly.

    YANG Description: Community associated with this Layer 2 circuit
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


  def _get_psn_tunnel_endpoint(self):
    """
    Getter method for psn_tunnel_endpoint, mapped from YANG variable /devices/device/vpls/mesh_group/neighbor/backup_neighbor/psn_tunnel_endpoint (ipv4addr)

    YANG Description: Endpoint of the transport tunnel on the remote PE
    """
    return self.__psn_tunnel_endpoint
      
  def _set_psn_tunnel_endpoint(self, v, load=False):
    """
    Setter method for psn_tunnel_endpoint, mapped from YANG variable /devices/device/vpls/mesh_group/neighbor/backup_neighbor/psn_tunnel_endpoint (ipv4addr)
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


  def _get_standby(self):
    """
    Getter method for standby, mapped from YANG variable /devices/device/vpls/mesh_group/neighbor/backup_neighbor/standby (empty)

    YANG Description: Keep backup pseudowire in continuous standby
    """
    return self.__standby
      
  def _set_standby(self, v, load=False):
    """
    Setter method for standby, mapped from YANG variable /devices/device/vpls/mesh_group/neighbor/backup_neighbor/standby (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_standby is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_standby() directly.

    YANG Description: Keep backup pseudowire in continuous standby
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="standby", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """standby must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="standby", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)""",
        })

    self.__standby = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_standby(self):
    self.__standby = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="standby", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)

  neighbor_id = __builtin__.property(_get_neighbor_id, _set_neighbor_id)
  static = __builtin__.property(_get_static, _set_static)
  community = __builtin__.property(_get_community, _set_community)
  psn_tunnel_endpoint = __builtin__.property(_get_psn_tunnel_endpoint, _set_psn_tunnel_endpoint)
  standby = __builtin__.property(_get_standby, _set_standby)


  _pyangbind_elements = collections.OrderedDict([('neighbor_id', neighbor_id), ('static', static), ('community', community), ('psn_tunnel_endpoint', psn_tunnel_endpoint), ('standby', standby), ])


