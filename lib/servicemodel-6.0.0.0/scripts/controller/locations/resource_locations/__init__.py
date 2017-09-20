
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
import location
class resource_locations(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module location - based on the path /locations/resource-locations. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__location',)

  _yang_name = 'resource-locations'
  _module_name = 'location'
  _namespace = 'http://anutanetworks.com/location'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__location = YANGDynClass(base=YANGListType("name",location.location, yang_name="location", module_name="location", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name'), is_container='list', yang_name="location", module_name="location", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/location', defining_module='location', yang_type='list', is_config=True)

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
      return [u'locations', u'resource-locations']

  def _get_location(self):
    """
    Getter method for location, mapped from YANG variable /locations/resource_locations/location (list)
    """
    return self.__location
      
  def _set_location(self, v, load=False):
    """
    Setter method for location, mapped from YANG variable /locations/resource_locations/location (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_location is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_location() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("name",location.location, yang_name="location", module_name="location", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name'), is_container='list', yang_name="location", module_name="location", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/location', defining_module='location', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """location must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",location.location, yang_name="location", module_name="location", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name'), is_container='list', yang_name="location", module_name="location", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/location', defining_module='location', yang_type='list', is_config=True)""",
        })

    self.__location = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_location(self):
    self.__location = YANGDynClass(base=YANGListType("name",location.location, yang_name="location", module_name="location", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name'), is_container='list', yang_name="location", module_name="location", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/location', defining_module='location', yang_type='list', is_config=True)

  location = __builtin__.property(_get_location, _set_location)


  _pyangbind_elements = collections.OrderedDict([('location', location), ])


