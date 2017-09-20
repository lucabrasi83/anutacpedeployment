
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
import vlan
class allowed_vlans(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/interface-ranges/interface-range/allowed-vlans. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__vlan','__vlan_range',)

  _yang_name = 'allowed-vlans'
  _module_name = 'interface'
  _namespace = 'http://anutanetworks.com/interface'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vlan_range = YANGDynClass(base=unicode, is_leaf=True, yang_name="vlan-range", module_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/interface', defining_module='interface', yang_type='string', is_config=True)
    self.__vlan = YANGDynClass(base=YANGListType("id",vlan.vlan, yang_name="vlan", module_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id'), is_container='list', yang_name="vlan", module_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/interface', defining_module='interface', yang_type='list', is_config=True)

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
      return [u'devices', u'device', u'interface-ranges', u'interface-range', u'allowed-vlans']

  def _get_vlan(self):
    """
    Getter method for vlan, mapped from YANG variable /devices/device/interface_ranges/interface_range/allowed_vlans/vlan (list)
    """
    return self.__vlan
      
  def _set_vlan(self, v, load=False):
    """
    Setter method for vlan, mapped from YANG variable /devices/device/interface_ranges/interface_range/allowed_vlans/vlan (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("id",vlan.vlan, yang_name="vlan", module_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id'), is_container='list', yang_name="vlan", module_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/interface', defining_module='interface', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",vlan.vlan, yang_name="vlan", module_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id'), is_container='list', yang_name="vlan", module_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/interface', defining_module='interface', yang_type='list', is_config=True)""",
        })

    self.__vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan(self):
    self.__vlan = YANGDynClass(base=YANGListType("id",vlan.vlan, yang_name="vlan", module_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id'), is_container='list', yang_name="vlan", module_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/interface', defining_module='interface', yang_type='list', is_config=True)


  def _get_vlan_range(self):
    """
    Getter method for vlan_range, mapped from YANG variable /devices/device/interface_ranges/interface_range/allowed_vlans/vlan_range (string)

    YANG Description: string
    """
    return self.__vlan_range
      
  def _set_vlan_range(self, v, load=False):
    """
    Setter method for vlan_range, mapped from YANG variable /devices/device/interface_ranges/interface_range/allowed_vlans/vlan_range (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_range is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_range() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vlan-range", module_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/interface', defining_module='interface', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_range must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vlan-range", module_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/interface', defining_module='interface', yang_type='string', is_config=True)""",
        })

    self.__vlan_range = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_range(self):
    self.__vlan_range = YANGDynClass(base=unicode, is_leaf=True, yang_name="vlan-range", module_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/interface', defining_module='interface', yang_type='string', is_config=True)

  vlan = __builtin__.property(_get_vlan, _set_vlan)
  vlan_range = __builtin__.property(_get_vlan_range, _set_vlan_range)


  _pyangbind_elements = collections.OrderedDict([('vlan', vlan), ('vlan_range', vlan_range), ])


