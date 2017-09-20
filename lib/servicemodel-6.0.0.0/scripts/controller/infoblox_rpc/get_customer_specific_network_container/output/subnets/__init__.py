
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
import subnet
class subnets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module infoblox - based on the path /infoblox_rpc/get-customer-specific-network-container/output/subnets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__subnet',)

  _yang_name = 'subnets'
  _module_name = 'infoblox'
  _namespace = 'http://anutanetworks.com/infoblox'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subnet = YANGDynClass(base=subnet.subnet, is_container='container', yang_name="subnet", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='container', is_config=True)

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
      return [u'infoblox_rpc', u'get-customer-specific-network-container', u'output', u'subnets']

  def _get_subnet(self):
    """
    Getter method for subnet, mapped from YANG variable /infoblox_rpc/get_customer_specific_network_container/output/subnets/subnet (container)
    """
    return self.__subnet
      
  def _set_subnet(self, v, load=False):
    """
    Setter method for subnet, mapped from YANG variable /infoblox_rpc/get_customer_specific_network_container/output/subnets/subnet (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subnet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subnet() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=subnet.subnet, is_container='container', yang_name="subnet", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subnet must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=subnet.subnet, is_container='container', yang_name="subnet", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='container', is_config=True)""",
        })

    self.__subnet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subnet(self):
    self.__subnet = YANGDynClass(base=subnet.subnet, is_container='container', yang_name="subnet", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='container', is_config=True)

  subnet = __builtin__.property(_get_subnet, _set_subnet)


  _pyangbind_elements = collections.OrderedDict([('subnet', subnet), ])


