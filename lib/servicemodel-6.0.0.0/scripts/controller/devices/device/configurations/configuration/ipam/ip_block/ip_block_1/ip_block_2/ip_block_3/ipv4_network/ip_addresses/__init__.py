
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
class ip_addresses(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/configurations/configuration/ipam/ip-block/ip-block-1/ip-block-2/ip-block-3/ipv4-network/ip-addresses. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__ip_address','__hostname',)

  _yang_name = 'ip-addresses'
  _module_name = 'bluecat'
  _namespace = 'http://anutanetworks.com/bluecat'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__hostname = YANGDynClass(base=unicode, is_leaf=True, yang_name="hostname", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=True)
    self.__ip_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-address", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='inet:ipv4-address', is_config=True)

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
      return [u'devices', u'device', u'configurations', u'configuration', u'ipam', u'ip-block', u'ip-block-1', u'ip-block-2', u'ip-block-3', u'ipv4-network', u'ip-addresses']

  def _get_ip_address(self):
    """
    Getter method for ip_address, mapped from YANG variable /devices/device/configurations/configuration/ipam/ip_block/ip_block_1/ip_block_2/ip_block_3/ipv4_network/ip_addresses/ip_address (inet:ipv4-address)

    YANG Description: Valid IPv4 Address (A.B.C.D for e.x: 172.16.1.1)
    """
    return self.__ip_address
      
  def _set_ip_address(self, v, load=False):
    """
    Setter method for ip_address, mapped from YANG variable /devices/device/configurations/configuration/ipam/ip_block/ip_block_1/ip_block_2/ip_block_3/ipv4_network/ip_addresses/ip_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_address() directly.

    YANG Description: Valid IPv4 Address (A.B.C.D for e.x: 172.16.1.1)
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-address", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-address", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_address(self):
    self.__ip_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-address", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='inet:ipv4-address', is_config=True)


  def _get_hostname(self):
    """
    Getter method for hostname, mapped from YANG variable /devices/device/configurations/configuration/ipam/ip_block/ip_block_1/ip_block_2/ip_block_3/ipv4_network/ip_addresses/hostname (string)

    YANG Description: string
    """
    return self.__hostname
      
  def _set_hostname(self, v, load=False):
    """
    Setter method for hostname, mapped from YANG variable /devices/device/configurations/configuration/ipam/ip_block/ip_block_1/ip_block_2/ip_block_3/ipv4_network/ip_addresses/hostname (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hostname is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hostname() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="hostname", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hostname must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="hostname", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=True)""",
        })

    self.__hostname = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hostname(self):
    self.__hostname = YANGDynClass(base=unicode, is_leaf=True, yang_name="hostname", module_name="bluecat", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/bluecat', defining_module='bluecat', yang_type='string', is_config=True)

  ip_address = __builtin__.property(_get_ip_address, _set_ip_address)
  hostname = __builtin__.property(_get_hostname, _set_hostname)


  _pyangbind_elements = collections.OrderedDict([('ip_address', ip_address), ('hostname', hostname), ])


