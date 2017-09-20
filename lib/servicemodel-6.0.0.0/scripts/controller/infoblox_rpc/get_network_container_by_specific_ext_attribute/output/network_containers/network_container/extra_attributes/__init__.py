
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
import attributes
class extra_attributes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module infoblox - based on the path /infoblox_rpc/get-network-container-by-specific-ext-attribute/output/network-containers/network-container/extra-attributes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__attributes',)

  _yang_name = 'extra-attributes'
  _module_name = 'infoblox'
  _namespace = 'http://anutanetworks.com/infoblox'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attributes = YANGDynClass(base=YANGListType(False,attributes.attributes, yang_name="attributes", module_name="infoblox", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False'), is_container='list', yang_name="attributes", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='list', is_config=True)

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
      return [u'infoblox_rpc', u'get-network-container-by-specific-ext-attribute', u'output', u'network-containers', u'network-container', u'extra-attributes']

  def _get_attributes(self):
    """
    Getter method for attributes, mapped from YANG variable /infoblox_rpc/get_network_container_by_specific_ext_attribute/output/network_containers/network_container/extra_attributes/attributes (list)
    """
    return self.__attributes
      
  def _set_attributes(self, v, load=False):
    """
    Setter method for attributes, mapped from YANG variable /infoblox_rpc/get_network_container_by_specific_ext_attribute/output/network_containers/network_container/extra_attributes/attributes (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attributes() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType(False,attributes.attributes, yang_name="attributes", module_name="infoblox", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False'), is_container='list', yang_name="attributes", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attributes must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,attributes.attributes, yang_name="attributes", module_name="infoblox", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False'), is_container='list', yang_name="attributes", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='list', is_config=True)""",
        })

    self.__attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attributes(self):
    self.__attributes = YANGDynClass(base=YANGListType(False,attributes.attributes, yang_name="attributes", module_name="infoblox", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False'), is_container='list', yang_name="attributes", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='list', is_config=True)

  attributes = __builtin__.property(_get_attributes, _set_attributes)


  _pyangbind_elements = collections.OrderedDict([('attributes', attributes), ])


