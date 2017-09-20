
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
class openstack_network(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /system/tables/third-party/openstack/openstack-networks/openstack-network. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__network_id','__virtual_network_id','__segmentation_id','__external_network',)

  _yang_name = 'openstack-network'
  _module_name = 'system'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__network_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="network-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__segmentation_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="segmentation-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__external_network = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="external-network", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    self.__virtual_network_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="virtual-network-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

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
      return [u'system', u'tables', u'third-party', u'openstack', u'openstack-networks', u'openstack-network']

  def _get_network_id(self):
    """
    Getter method for network_id, mapped from YANG variable /system/tables/third_party/openstack/openstack_networks/openstack_network/network_id (string)

    YANG Description: string
    """
    return self.__network_id
      
  def _set_network_id(self, v, load=False):
    """
    Setter method for network_id, mapped from YANG variable /system/tables/third_party/openstack/openstack_networks/openstack_network/network_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_id() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="network-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="network-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__network_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_id(self):
    self.__network_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="network-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_virtual_network_id(self):
    """
    Getter method for virtual_network_id, mapped from YANG variable /system/tables/third_party/openstack/openstack_networks/openstack_network/virtual_network_id (string)

    YANG Description: string
    """
    return self.__virtual_network_id
      
  def _set_virtual_network_id(self, v, load=False):
    """
    Setter method for virtual_network_id, mapped from YANG variable /system/tables/third_party/openstack/openstack_networks/openstack_network/virtual_network_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_network_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_network_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="virtual-network-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_network_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="virtual-network-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__virtual_network_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_network_id(self):
    self.__virtual_network_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="virtual-network-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_segmentation_id(self):
    """
    Getter method for segmentation_id, mapped from YANG variable /system/tables/third_party/openstack/openstack_networks/openstack_network/segmentation_id (string)

    YANG Description: string
    """
    return self.__segmentation_id
      
  def _set_segmentation_id(self, v, load=False):
    """
    Setter method for segmentation_id, mapped from YANG variable /system/tables/third_party/openstack/openstack_networks/openstack_network/segmentation_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_segmentation_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_segmentation_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="segmentation-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """segmentation_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="segmentation-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__segmentation_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_segmentation_id(self):
    self.__segmentation_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="segmentation-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_external_network(self):
    """
    Getter method for external_network, mapped from YANG variable /system/tables/third_party/openstack/openstack_networks/openstack_network/external_network (boolean)

    YANG Description: external-network: True/False
    """
    return self.__external_network
      
  def _set_external_network(self, v, load=False):
    """
    Setter method for external_network, mapped from YANG variable /system/tables/third_party/openstack/openstack_networks/openstack_network/external_network (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_external_network is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_external_network() directly.

    YANG Description: external-network: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="external-network", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """external_network must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="external-network", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)""",
        })

    self.__external_network = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_external_network(self):
    self.__external_network = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="external-network", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)

  network_id = __builtin__.property(_get_network_id, _set_network_id)
  virtual_network_id = __builtin__.property(_get_virtual_network_id, _set_virtual_network_id)
  segmentation_id = __builtin__.property(_get_segmentation_id, _set_segmentation_id)
  external_network = __builtin__.property(_get_external_network, _set_external_network)


  _pyangbind_elements = collections.OrderedDict([('network_id', network_id), ('virtual_network_id', virtual_network_id), ('segmentation_id', segmentation_id), ('external_network', external_network), ])


