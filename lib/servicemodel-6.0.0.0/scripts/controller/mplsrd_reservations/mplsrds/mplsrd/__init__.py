
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
class mplsrd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /mplsrd-reservations/mplsrds/mplsrd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__tenant','__rd','__vpn_identifier','__allocated','__admin_created','__mplsrd_range','__mplsrd_to_devices',)

  _yang_name = 'mplsrd'
  _module_name = 'controller'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vpn_identifier = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4294967295']}), is_leaf=True, yang_name="vpn-identifier", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[a-zA-Z0-9_\\s-]+$', 'length': [u'1..36']}), is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__mplsrd_to_devices = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="mplsrd-to-devices", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=False)
    self.__rd = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="rd", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint16', is_config=True)
    self.__mplsrd_range = YANGDynClass(base=unicode, is_leaf=True, yang_name="mplsrd-range", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=False)
    self.__allocated = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="allocated", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)
    self.__tenant = YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)
    self.__admin_created = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="admin-created", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)

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
      return [u'mplsrd-reservations', u'mplsrds', u'mplsrd']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/name (string)

    YANG Description: Allows AlphaNumerics, hyphen, underscore and space character only. Max length is 36
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Allows AlphaNumerics, hyphen, underscore and space character only. Max length is 36
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[a-zA-Z0-9_\\s-]+$', 'length': [u'1..36']}), is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[a-zA-Z0-9_\\s-]+$', 'length': [u'1..36']}), is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[a-zA-Z0-9_\\s-]+$', 'length': [u'1..36']}), is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_tenant(self):
    """
    Getter method for tenant, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/tenant (leafref)

    YANG Description: tenant
    """
    return self.__tenant
      
  def _set_tenant(self, v, load=False):
    """
    Setter method for tenant, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/tenant (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tenant is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tenant() directly.

    YANG Description: tenant
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="tenant", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tenant must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)""",
        })

    self.__tenant = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tenant(self):
    self.__tenant = YANGDynClass(base=unicode, is_leaf=True, yang_name="tenant", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)


  def _get_rd(self):
    """
    Getter method for rd, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/rd (uint16)

    YANG Description: 1..65535
    """
    return self.__rd
      
  def _set_rd(self, v, load=False):
    """
    Setter method for rd, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/rd (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rd() directly.

    YANG Description: 1..65535
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="rd", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rd must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="rd", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint16', is_config=True)""",
        })

    self.__rd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rd(self):
    self.__rd = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="rd", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint16', is_config=True)


  def _get_vpn_identifier(self):
    """
    Getter method for vpn_identifier, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/vpn_identifier (uint32)

    YANG Description: 1..4294967295
    """
    return self.__vpn_identifier
      
  def _set_vpn_identifier(self, v, load=False):
    """
    Setter method for vpn_identifier, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/vpn_identifier (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vpn_identifier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vpn_identifier() directly.

    YANG Description: 1..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4294967295']}), is_leaf=True, yang_name="vpn-identifier", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vpn_identifier must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4294967295']}), is_leaf=True, yang_name="vpn-identifier", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)""",
        })

    self.__vpn_identifier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vpn_identifier(self):
    self.__vpn_identifier = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4294967295']}), is_leaf=True, yang_name="vpn-identifier", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)


  def _get_allocated(self):
    """
    Getter method for allocated, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/allocated (boolean)

    YANG Description: allocated: True/False
    """
    return self.__allocated
      
  def _set_allocated(self, v, load=False):
    """
    Setter method for allocated, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/allocated (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allocated is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allocated() directly.

    YANG Description: allocated: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="allocated", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allocated must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="allocated", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)""",
        })

    self.__allocated = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allocated(self):
    self.__allocated = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="allocated", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)


  def _get_admin_created(self):
    """
    Getter method for admin_created, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/admin_created (boolean)

    YANG Description: admin-created: True/False
    """
    return self.__admin_created
      
  def _set_admin_created(self, v, load=False):
    """
    Setter method for admin_created, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/admin_created (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_admin_created is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_admin_created() directly.

    YANG Description: admin-created: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="admin-created", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """admin_created must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="admin-created", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)""",
        })

    self.__admin_created = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_admin_created(self):
    self.__admin_created = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="admin-created", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)


  def _get_mplsrd_range(self):
    """
    Getter method for mplsrd_range, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/mplsrd_range (leafref)

    YANG Description: mplsrd-range
    """
    return self.__mplsrd_range
      
  def _set_mplsrd_range(self, v, load=False):
    """
    Setter method for mplsrd_range, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/mplsrd_range (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mplsrd_range is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mplsrd_range() directly.

    YANG Description: mplsrd-range
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mplsrd-range", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mplsrd_range must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mplsrd-range", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=False)""",
        })

    self.__mplsrd_range = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mplsrd_range(self):
    self.__mplsrd_range = YANGDynClass(base=unicode, is_leaf=True, yang_name="mplsrd-range", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=False)


  def _get_mplsrd_to_devices(self):
    """
    Getter method for mplsrd_to_devices, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/mplsrd_to_devices (leafref)

    YANG Description: mplsrd-to-devices
    """
    return self.__mplsrd_to_devices
      
  def _set_mplsrd_to_devices(self, v, load=False):
    """
    Setter method for mplsrd_to_devices, mapped from YANG variable /mplsrd_reservations/mplsrds/mplsrd/mplsrd_to_devices (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mplsrd_to_devices is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mplsrd_to_devices() directly.

    YANG Description: mplsrd-to-devices
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="mplsrd-to-devices", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mplsrd_to_devices must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="mplsrd-to-devices", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=False)""",
        })

    self.__mplsrd_to_devices = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mplsrd_to_devices(self):
    self.__mplsrd_to_devices = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="mplsrd-to-devices", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=False)

  name = __builtin__.property(_get_name, _set_name)
  tenant = __builtin__.property(_get_tenant, _set_tenant)
  rd = __builtin__.property(_get_rd, _set_rd)
  vpn_identifier = __builtin__.property(_get_vpn_identifier, _set_vpn_identifier)
  allocated = __builtin__.property(_get_allocated)
  admin_created = __builtin__.property(_get_admin_created)
  mplsrd_range = __builtin__.property(_get_mplsrd_range)
  mplsrd_to_devices = __builtin__.property(_get_mplsrd_to_devices)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('tenant', tenant), ('rd', rd), ('vpn_identifier', vpn_identifier), ('allocated', allocated), ('admin_created', admin_created), ('mplsrd_range', mplsrd_range), ('mplsrd_to_devices', mplsrd_to_devices), ])


