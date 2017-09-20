
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
import dns_zone
class dns_zones(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/dns-zones. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__dns_zone',)

  _yang_name = 'dns-zones'
  _module_name = 'dns'
  _namespace = 'http://anutanetworks.com/dns'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__dns_zone = YANGDynClass(base=YANGListType("name",dns_zone.dns_zone, yang_name="dns-zone", module_name="dns", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name'), is_container='list', yang_name="dns-zone", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='list', is_config=True)

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
      return [u'devices', u'device', u'dns-zones']

  def _get_dns_zone(self):
    """
    Getter method for dns_zone, mapped from YANG variable /devices/device/dns_zones/dns_zone (list)
    """
    return self.__dns_zone
      
  def _set_dns_zone(self, v, load=False):
    """
    Setter method for dns_zone, mapped from YANG variable /devices/device/dns_zones/dns_zone (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dns_zone is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dns_zone() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("name",dns_zone.dns_zone, yang_name="dns-zone", module_name="dns", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name'), is_container='list', yang_name="dns-zone", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dns_zone must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",dns_zone.dns_zone, yang_name="dns-zone", module_name="dns", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name'), is_container='list', yang_name="dns-zone", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='list', is_config=True)""",
        })

    self.__dns_zone = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dns_zone(self):
    self.__dns_zone = YANGDynClass(base=YANGListType("name",dns_zone.dns_zone, yang_name="dns-zone", module_name="dns", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name'), is_container='list', yang_name="dns-zone", module_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/dns', defining_module='dns', yang_type='list', is_config=True)

  dns_zone = __builtin__.property(_get_dns_zone, _set_dns_zone)


  _pyangbind_elements = collections.OrderedDict([('dns_zone', dns_zone), ])


