
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
import site
class multi_homing(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/vpls/multi-homing. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Multi-homing configuration for FEC129 VPLS
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__peer_active','__site',)

  _yang_name = 'multi-homing'
  _module_name = 'vpls'
  _namespace = 'http://anutanetworks.com/vpls'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__peer_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="peer-active", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)
    self.__site = YANGDynClass(base=YANGListType("site_name",site.site, yang_name="site", module_name="vpls", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='site-name'), is_container='list', yang_name="site", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='list', is_config=True)

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
      return [u'devices', u'device', u'vpls', u'multi-homing']

  def _get_peer_active(self):
    """
    Getter method for peer_active, mapped from YANG variable /devices/device/vpls/multi_homing/peer_active (empty)

    YANG Description: Keep CE interfaces in up state when all BGP peers go down
    """
    return self.__peer_active
      
  def _set_peer_active(self, v, load=False):
    """
    Setter method for peer_active, mapped from YANG variable /devices/device/vpls/multi_homing/peer_active (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_active is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_active() directly.

    YANG Description: Keep CE interfaces in up state when all BGP peers go down
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="peer-active", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_active must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="peer-active", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)""",
        })

    self.__peer_active = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_active(self):
    self.__peer_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="peer-active", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='empty', is_config=True)


  def _get_site(self):
    """
    Getter method for site, mapped from YANG variable /devices/device/vpls/multi_homing/site (list)

    YANG Description: Sites connected to this provider equipment
    """
    return self.__site
      
  def _set_site(self, v, load=False):
    """
    Setter method for site, mapped from YANG variable /devices/device/vpls/multi_homing/site (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_site is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_site() directly.

    YANG Description: Sites connected to this provider equipment
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("site_name",site.site, yang_name="site", module_name="vpls", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='site-name'), is_container='list', yang_name="site", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """site must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("site_name",site.site, yang_name="site", module_name="vpls", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='site-name'), is_container='list', yang_name="site", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='list', is_config=True)""",
        })

    self.__site = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_site(self):
    self.__site = YANGDynClass(base=YANGListType("site_name",site.site, yang_name="site", module_name="vpls", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='site-name'), is_container='list', yang_name="site", module_name="vpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/vpls', defining_module='vpls', yang_type='list', is_config=True)

  peer_active = __builtin__.property(_get_peer_active, _set_peer_active)
  site = __builtin__.property(_get_site, _set_site)


  _pyangbind_elements = collections.OrderedDict([('peer_active', peer_active), ('site', site), ])


