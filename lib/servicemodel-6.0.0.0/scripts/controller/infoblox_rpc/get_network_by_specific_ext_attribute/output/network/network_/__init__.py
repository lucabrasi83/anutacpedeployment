
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
import extra_attributes
class network(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module infoblox - based on the path /infoblox_rpc/get-network-by-specific-ext-attribute/output/network/network. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__container_id','__network_id','__network_view','__comment','__extra_attributes',)

  _yang_name = 'network'
  _module_name = 'infoblox'
  _namespace = 'http://anutanetworks.com/infoblox'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__network_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="network-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    self.__comment = YANGDynClass(base=unicode, is_leaf=True, yang_name="comment", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    self.__extra_attributes = YANGDynClass(base=extra_attributes.extra_attributes, is_container='container', yang_name="extra-attributes", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='container', is_config=True)
    self.__container_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="container-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
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
      return [u'infoblox_rpc', u'get-network-by-specific-ext-attribute', u'output', u'network', u'network']

  def _get_container_id(self):
    """
    Getter method for container_id, mapped from YANG variable /infoblox_rpc/get_network_by_specific_ext_attribute/output/network/network/container_id (string)

    YANG Description: string
    """
    return self.__container_id
      
  def _set_container_id(self, v, load=False):
    """
    Setter method for container_id, mapped from YANG variable /infoblox_rpc/get_network_by_specific_ext_attribute/output/network/network/container_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_container_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_container_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="container-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """container_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="container-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.__container_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_container_id(self):
    self.__container_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="container-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)


  def _get_network_id(self):
    """
    Getter method for network_id, mapped from YANG variable /infoblox_rpc/get_network_by_specific_ext_attribute/output/network/network/network_id (string)

    YANG Description: string
    """
    return self.__network_id
      
  def _set_network_id(self, v, load=False):
    """
    Setter method for network_id, mapped from YANG variable /infoblox_rpc/get_network_by_specific_ext_attribute/output/network/network/network_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_id() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="network-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="network-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.__network_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_id(self):
    self.__network_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="network-id", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)


  def _get_network_view(self):
    """
    Getter method for network_view, mapped from YANG variable /infoblox_rpc/get_network_by_specific_ext_attribute/output/network/network/network_view (string)

    YANG Description: string
    """
    return self.__network_view
      
  def _set_network_view(self, v, load=False):
    """
    Setter method for network_view, mapped from YANG variable /infoblox_rpc/get_network_by_specific_ext_attribute/output/network/network/network_view (string)
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


  def _get_comment(self):
    """
    Getter method for comment, mapped from YANG variable /infoblox_rpc/get_network_by_specific_ext_attribute/output/network/network/comment (string)

    YANG Description: string
    """
    return self.__comment
      
  def _set_comment(self, v, load=False):
    """
    Setter method for comment, mapped from YANG variable /infoblox_rpc/get_network_by_specific_ext_attribute/output/network/network/comment (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_comment is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_comment() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="comment", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """comment must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="comment", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)""",
        })

    self.__comment = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_comment(self):
    self.__comment = YANGDynClass(base=unicode, is_leaf=True, yang_name="comment", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='string', is_config=True)


  def _get_extra_attributes(self):
    """
    Getter method for extra_attributes, mapped from YANG variable /infoblox_rpc/get_network_by_specific_ext_attribute/output/network/network/extra_attributes (container)
    """
    return self.__extra_attributes
      
  def _set_extra_attributes(self, v, load=False):
    """
    Setter method for extra_attributes, mapped from YANG variable /infoblox_rpc/get_network_by_specific_ext_attribute/output/network/network/extra_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extra_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extra_attributes() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=extra_attributes.extra_attributes, is_container='container', yang_name="extra-attributes", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extra_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=extra_attributes.extra_attributes, is_container='container', yang_name="extra-attributes", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='container', is_config=True)""",
        })

    self.__extra_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extra_attributes(self):
    self.__extra_attributes = YANGDynClass(base=extra_attributes.extra_attributes, is_container='container', yang_name="extra-attributes", module_name="infoblox", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/infoblox', defining_module='infoblox', yang_type='container', is_config=True)

  container_id = __builtin__.property(_get_container_id, _set_container_id)
  network_id = __builtin__.property(_get_network_id, _set_network_id)
  network_view = __builtin__.property(_get_network_view, _set_network_view)
  comment = __builtin__.property(_get_comment, _set_comment)
  extra_attributes = __builtin__.property(_get_extra_attributes, _set_extra_attributes)


  _pyangbind_elements = collections.OrderedDict([('container_id', container_id), ('network_id', network_id), ('network_view', network_view), ('comment', comment), ('extra_attributes', extra_attributes), ])


