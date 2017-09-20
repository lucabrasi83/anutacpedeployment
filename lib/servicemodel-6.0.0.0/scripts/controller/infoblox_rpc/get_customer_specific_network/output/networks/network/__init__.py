
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
class network(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module infoblox - based on the path /infoblox_rpc/get-customer-specific-network/output/networks/network. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__container','__network',)

  _yang_name = 'network'
  _module_name = 'infoblox'
  _namespace = 'http://anutanetworks.com/infoblox'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__container = YANGDynClass(base=unicode, is_leaf=True, yang_name="container", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    self.__network = YANGDynClass(base=unicode, is_leaf=True, yang_name="network", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)

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
      return [u'infoblox_rpc', u'get-customer-specific-network', u'output', u'networks', u'network']

  def _get_container(self):
    """
    Getter method for container, mapped from YANG variable /infoblox_rpc/get_customer_specific_network/output/networks/network/container (string)

    YANG Description: string
    """
    return self.__container
      
  def _set_container(self, v, load=False):
    """
    Setter method for container, mapped from YANG variable /infoblox_rpc/get_customer_specific_network/output/networks/network/container (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_container is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_container() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="container", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """container must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="container", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.__container = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_container(self):
    self.__container = YANGDynClass(base=unicode, is_leaf=True, yang_name="container", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)


  def _get_network(self):
    """
    Getter method for network, mapped from YANG variable /infoblox_rpc/get_customer_specific_network/output/networks/network/network (string)

    YANG Description: string
    """
    return self.__network
      
  def _set_network(self, v, load=False):
    """
    Setter method for network, mapped from YANG variable /infoblox_rpc/get_customer_specific_network/output/networks/network/network (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="network", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="network", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.__network = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network(self):
    self.__network = YANGDynClass(base=unicode, is_leaf=True, yang_name="network", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)

  container = __builtin__.property(_get_container, _set_container)
  network = __builtin__.property(_get_network, _set_network)


  _pyangbind_elements = collections.OrderedDict([('container', container), ('network', network), ])


