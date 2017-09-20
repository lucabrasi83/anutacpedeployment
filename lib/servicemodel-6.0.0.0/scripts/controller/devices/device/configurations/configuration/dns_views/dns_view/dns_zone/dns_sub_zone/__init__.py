
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
import resource_record
class dns_sub_zone(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/configurations/configuration/dns-views/dns-view/dns-zone/dns-sub-zone. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__id','__absolute_name','__resource_record',)

  _yang_name = 'dns-sub-zone'
  _module_name = 'bluecat'
  _namespace = 'http://anutanetworks.com/bluecat'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__absolute_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="absolute-name", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=True)
    self.__resource_record = YANGDynClass(base=YANGListType("fqdn",resource_record.resource_record, yang_name="resource-record", module_name="bluecat", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fqdn'), is_container='list', yang_name="resource-record", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='list', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=True)
    self.__id = YANGDynClass(base=unicode, is_leaf=True, yang_name="id", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=False)

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
      return [u'devices', u'device', u'configurations', u'configuration', u'dns-views', u'dns-view', u'dns-zone', u'dns-sub-zone']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /devices/device/configurations/configuration/dns_views/dns_view/dns_zone/dns_sub_zone/name (string)

    YANG Description: string
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /devices/device/configurations/configuration/dns_views/dns_view/dns_zone/dns_sub_zone/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=True)


  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /devices/device/configurations/configuration/dns_views/dns_view/dns_zone/dns_sub_zone/id (string)

    YANG Description: string
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /devices/device/configurations/configuration/dns_views/dns_view/dns_zone/dns_sub_zone/id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="id", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="id", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=False)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=unicode, is_leaf=True, yang_name="id", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=False)


  def _get_absolute_name(self):
    """
    Getter method for absolute_name, mapped from YANG variable /devices/device/configurations/configuration/dns_views/dns_view/dns_zone/dns_sub_zone/absolute_name (string)

    YANG Description: string
    """
    return self.__absolute_name
      
  def _set_absolute_name(self, v, load=False):
    """
    Setter method for absolute_name, mapped from YANG variable /devices/device/configurations/configuration/dns_views/dns_view/dns_zone/dns_sub_zone/absolute_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_absolute_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_absolute_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="absolute-name", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """absolute_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="absolute-name", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=True)""",
        })

    self.__absolute_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_absolute_name(self):
    self.__absolute_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="absolute-name", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=True)


  def _get_resource_record(self):
    """
    Getter method for resource_record, mapped from YANG variable /devices/device/configurations/configuration/dns_views/dns_view/dns_zone/dns_sub_zone/resource_record (list)
    """
    return self.__resource_record
      
  def _set_resource_record(self, v, load=False):
    """
    Setter method for resource_record, mapped from YANG variable /devices/device/configurations/configuration/dns_views/dns_view/dns_zone/dns_sub_zone/resource_record (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_resource_record is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_resource_record() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("fqdn",resource_record.resource_record, yang_name="resource-record", module_name="bluecat", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fqdn'), is_container='list', yang_name="resource-record", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """resource_record must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("fqdn",resource_record.resource_record, yang_name="resource-record", module_name="bluecat", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fqdn'), is_container='list', yang_name="resource-record", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='list', is_config=True)""",
        })

    self.__resource_record = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_resource_record(self):
    self.__resource_record = YANGDynClass(base=YANGListType("fqdn",resource_record.resource_record, yang_name="resource-record", module_name="bluecat", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fqdn'), is_container='list', yang_name="resource-record", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='list', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  id = __builtin__.property(_get_id)
  absolute_name = __builtin__.property(_get_absolute_name, _set_absolute_name)
  resource_record = __builtin__.property(_get_resource_record, _set_resource_record)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('id', id), ('absolute_name', absolute_name), ('resource_record', resource_record), ])


