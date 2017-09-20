
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
import openstack_resource_mapping
class openstack_resource_mappings(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /system/tables/openstack-resource-mappings. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__openstack_resource_mapping',)

  _yang_name = 'openstack-resource-mappings'
  _module_name = 'system'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__openstack_resource_mapping = YANGDynClass(base=YANGListType("openstack_resource_mapping_id",openstack_resource_mapping.openstack_resource_mapping, yang_name="openstack-resource-mapping", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='openstack-resource-mapping-id'), is_container='list', yang_name="openstack-resource-mapping", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)

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
      return [u'system', u'tables', u'openstack-resource-mappings']

  def _get_openstack_resource_mapping(self):
    """
    Getter method for openstack_resource_mapping, mapped from YANG variable /system/tables/openstack_resource_mappings/openstack_resource_mapping (list)
    """
    return self.__openstack_resource_mapping
      
  def _set_openstack_resource_mapping(self, v, load=False):
    """
    Setter method for openstack_resource_mapping, mapped from YANG variable /system/tables/openstack_resource_mappings/openstack_resource_mapping (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_openstack_resource_mapping is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_openstack_resource_mapping() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("openstack_resource_mapping_id",openstack_resource_mapping.openstack_resource_mapping, yang_name="openstack-resource-mapping", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='openstack-resource-mapping-id'), is_container='list', yang_name="openstack-resource-mapping", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """openstack_resource_mapping must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("openstack_resource_mapping_id",openstack_resource_mapping.openstack_resource_mapping, yang_name="openstack-resource-mapping", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='openstack-resource-mapping-id'), is_container='list', yang_name="openstack-resource-mapping", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)""",
        })

    self.__openstack_resource_mapping = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_openstack_resource_mapping(self):
    self.__openstack_resource_mapping = YANGDynClass(base=YANGListType("openstack_resource_mapping_id",openstack_resource_mapping.openstack_resource_mapping, yang_name="openstack-resource-mapping", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='openstack-resource-mapping-id'), is_container='list', yang_name="openstack-resource-mapping", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)

  openstack_resource_mapping = __builtin__.property(_get_openstack_resource_mapping, _set_openstack_resource_mapping)


  _pyangbind_elements = collections.OrderedDict([('openstack_resource_mapping', openstack_resource_mapping), ])


