
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
class vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/contexts/context/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__vlan_name',)

  _yang_name = 'vlan'
  _module_name = 'loadbalancer'
  _namespace = 'http://anutanetworks.com/loadbalancer'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vlan_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vlan-name", module_name="loadbalancer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/loadbalancer', defining_module='loadbalancer', yang_type='leafref', is_config=True)

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
      return [u'devices', u'device', u'contexts', u'context', u'vlan']

  def _get_vlan_name(self):
    """
    Getter method for vlan_name, mapped from YANG variable /devices/device/contexts/context/vlan/vlan_name (leafref)

    YANG Description: vlan-name
    """
    return self.__vlan_name
      
  def _set_vlan_name(self, v, load=False):
    """
    Setter method for vlan_name, mapped from YANG variable /devices/device/contexts/context/vlan/vlan_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_name() directly.

    YANG Description: vlan-name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vlan-name", module_name="loadbalancer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/loadbalancer', defining_module='loadbalancer', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vlan-name", module_name="loadbalancer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/loadbalancer', defining_module='loadbalancer', yang_type='leafref', is_config=True)""",
        })

    self.__vlan_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_name(self):
    self.__vlan_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vlan-name", module_name="loadbalancer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/loadbalancer', defining_module='loadbalancer', yang_type='leafref', is_config=True)

  vlan_name = __builtin__.property(_get_vlan_name, _set_vlan_name)


  _pyangbind_elements = collections.OrderedDict([('vlan_name', vlan_name), ])


