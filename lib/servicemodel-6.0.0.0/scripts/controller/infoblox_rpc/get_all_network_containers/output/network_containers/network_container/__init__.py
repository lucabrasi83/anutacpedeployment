
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
class network_container(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module infoblox - based on the path /infoblox_rpc/get-all-network-containers/output/network-containers/network-container. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','___ref','__network','__network_view',)

  _yang_name = 'network-container'
  _module_name = 'infoblox'
  _namespace = 'http://anutanetworks.com/infoblox'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.___ref = YANGDynClass(base=unicode, is_leaf=True, yang_name="_ref", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    self.__network = YANGDynClass(base=unicode, is_leaf=True, yang_name="network", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    self.__network_view = YANGDynClass(base=unicode, is_leaf=True, yang_name="network_view", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)

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
      return [u'infoblox_rpc', u'get-all-network-containers', u'output', u'network-containers', u'network-container']

  def _get__ref(self):
    """
    Getter method for _ref, mapped from YANG variable /infoblox_rpc/get_all_network_containers/output/network_containers/network_container/_ref (string)

    YANG Description: string
    """
    return self.___ref
      
  def _set__ref(self, v, load=False):
    """
    Setter method for _ref, mapped from YANG variable /infoblox_rpc/get_all_network_containers/output/network_containers/network_container/_ref (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set__ref is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set__ref() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="_ref", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """_ref must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="_ref", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.___ref = t
    if hasattr(self, '_set'):
      self._set()

  def _unset__ref(self):
    self.___ref = YANGDynClass(base=unicode, is_leaf=True, yang_name="_ref", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)


  def _get_network(self):
    """
    Getter method for network, mapped from YANG variable /infoblox_rpc/get_all_network_containers/output/network_containers/network_container/network (string)

    YANG Description: string
    """
    return self.__network
      
  def _set_network(self, v, load=False):
    """
    Setter method for network, mapped from YANG variable /infoblox_rpc/get_all_network_containers/output/network_containers/network_container/network (string)
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


  def _get_network_view(self):
    """
    Getter method for network_view, mapped from YANG variable /infoblox_rpc/get_all_network_containers/output/network_containers/network_container/network_view (string)

    YANG Description: string
    """
    return self.__network_view
      
  def _set_network_view(self, v, load=False):
    """
    Setter method for network_view, mapped from YANG variable /infoblox_rpc/get_all_network_containers/output/network_containers/network_container/network_view (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_view is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_view() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="network_view", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_view must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="network_view", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.__network_view = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_view(self):
    self.__network_view = YANGDynClass(base=unicode, is_leaf=True, yang_name="network_view", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)

  _ref = __builtin__.property(_get__ref, _set__ref)
  network = __builtin__.property(_get_network, _set_network)
  network_view = __builtin__.property(_get_network_view, _set_network_view)


  _pyangbind_elements = collections.OrderedDict([('_ref', _ref), ('network', network), ('network_view', network_view), ])


