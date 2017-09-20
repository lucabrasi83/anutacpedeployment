
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
import child_entity
class reconciliation_entity(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /reconciliation-entities/reconciliation-entity. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__entity_rcpath','__device_id','__service_path','__operation_type','__modified_leafs','__child_entity','__payload','__status','__detected_time','__last_action_time',)

  _yang_name = 'reconciliation-entity'
  _module_name = 'controller'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__child_entity = YANGDynClass(base=YANGListType("entity_rcpath",child_entity.child_entity, yang_name="child-entity", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='entity-rcpath'), is_container='list', yang_name="child-entity", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)
    self.__status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IGNORE': {}, u'OVERWRITING_DEVICE': {}, u'DETECTED': {}, u'OVERWRITING_NCX': {}},), is_leaf=True, yang_name="status", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='enumeration', is_config=True)
    self.__detected_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="detected-time", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='ndt:datetime', is_config=True)
    self.__entity_rcpath = YANGDynClass(base=unicode, is_leaf=True, yang_name="entity-rcpath", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__modified_leafs = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="modified-leafs", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__payload = YANGDynClass(base=unicode, is_leaf=True, yang_name="payload", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__operation_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="operation-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__last_action_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-action-time", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='ndt:datetime', is_config=True)
    self.__service_path = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="service-path", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__device_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="device-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)

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
      return [u'reconciliation-entities', u'reconciliation-entity']

  def _get_entity_rcpath(self):
    """
    Getter method for entity_rcpath, mapped from YANG variable /reconciliation_entities/reconciliation_entity/entity_rcpath (string)

    YANG Description: string
    """
    return self.__entity_rcpath
      
  def _set_entity_rcpath(self, v, load=False):
    """
    Setter method for entity_rcpath, mapped from YANG variable /reconciliation_entities/reconciliation_entity/entity_rcpath (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_entity_rcpath is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_entity_rcpath() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="entity-rcpath", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """entity_rcpath must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="entity-rcpath", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__entity_rcpath = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_entity_rcpath(self):
    self.__entity_rcpath = YANGDynClass(base=unicode, is_leaf=True, yang_name="entity-rcpath", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_device_id(self):
    """
    Getter method for device_id, mapped from YANG variable /reconciliation_entities/reconciliation_entity/device_id (leafref)

    YANG Description: device-id
    """
    return self.__device_id
      
  def _set_device_id(self, v, load=False):
    """
    Setter method for device_id, mapped from YANG variable /reconciliation_entities/reconciliation_entity/device_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_device_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_device_id() directly.

    YANG Description: device-id
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="device-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """device_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="device-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)""",
        })

    self.__device_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_device_id(self):
    self.__device_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="device-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='leafref', is_config=True)


  def _get_service_path(self):
    """
    Getter method for service_path, mapped from YANG variable /reconciliation_entities/reconciliation_entity/service_path (string)

    YANG Description: string
    """
    return self.__service_path
      
  def _set_service_path(self, v, load=False):
    """
    Setter method for service_path, mapped from YANG variable /reconciliation_entities/reconciliation_entity/service_path (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_service_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_service_path() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="service-path", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """service_path must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="service-path", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__service_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_service_path(self):
    self.__service_path = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="service-path", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_operation_type(self):
    """
    Getter method for operation_type, mapped from YANG variable /reconciliation_entities/reconciliation_entity/operation_type (string)

    YANG Description: string
    """
    return self.__operation_type
      
  def _set_operation_type(self, v, load=False):
    """
    Setter method for operation_type, mapped from YANG variable /reconciliation_entities/reconciliation_entity/operation_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_operation_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_operation_type() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="operation-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """operation_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="operation-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__operation_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_operation_type(self):
    self.__operation_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="operation-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_modified_leafs(self):
    """
    Getter method for modified_leafs, mapped from YANG variable /reconciliation_entities/reconciliation_entity/modified_leafs (string)

    YANG Description: string
    """
    return self.__modified_leafs
      
  def _set_modified_leafs(self, v, load=False):
    """
    Setter method for modified_leafs, mapped from YANG variable /reconciliation_entities/reconciliation_entity/modified_leafs (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_modified_leafs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_modified_leafs() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="modified-leafs", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """modified_leafs must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="modified-leafs", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__modified_leafs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_modified_leafs(self):
    self.__modified_leafs = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="modified-leafs", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_child_entity(self):
    """
    Getter method for child_entity, mapped from YANG variable /reconciliation_entities/reconciliation_entity/child_entity (list)
    """
    return self.__child_entity
      
  def _set_child_entity(self, v, load=False):
    """
    Setter method for child_entity, mapped from YANG variable /reconciliation_entities/reconciliation_entity/child_entity (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_child_entity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_child_entity() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("entity_rcpath",child_entity.child_entity, yang_name="child-entity", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='entity-rcpath'), is_container='list', yang_name="child-entity", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """child_entity must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("entity_rcpath",child_entity.child_entity, yang_name="child-entity", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='entity-rcpath'), is_container='list', yang_name="child-entity", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)""",
        })

    self.__child_entity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_child_entity(self):
    self.__child_entity = YANGDynClass(base=YANGListType("entity_rcpath",child_entity.child_entity, yang_name="child-entity", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='entity-rcpath'), is_container='list', yang_name="child-entity", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)


  def _get_payload(self):
    """
    Getter method for payload, mapped from YANG variable /reconciliation_entities/reconciliation_entity/payload (string)

    YANG Description: string
    """
    return self.__payload
      
  def _set_payload(self, v, load=False):
    """
    Setter method for payload, mapped from YANG variable /reconciliation_entities/reconciliation_entity/payload (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_payload is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_payload() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="payload", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """payload must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="payload", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__payload = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_payload(self):
    self.__payload = YANGDynClass(base=unicode, is_leaf=True, yang_name="payload", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_status(self):
    """
    Getter method for status, mapped from YANG variable /reconciliation_entities/reconciliation_entity/status (enumeration)

    YANG Description: OVERWRITING_DEVICE
OVERWRITING_NCX
IGNORE
DETECTED

    """
    return self.__status
      
  def _set_status(self, v, load=False):
    """
    Setter method for status, mapped from YANG variable /reconciliation_entities/reconciliation_entity/status (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_status() directly.

    YANG Description: OVERWRITING_DEVICE
OVERWRITING_NCX
IGNORE
DETECTED

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IGNORE': {}, u'OVERWRITING_DEVICE': {}, u'DETECTED': {}, u'OVERWRITING_NCX': {}},), is_leaf=True, yang_name="status", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """status must be of a type compatible with enumeration""",
          'defined-type': "controller:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IGNORE': {}, u'OVERWRITING_DEVICE': {}, u'DETECTED': {}, u'OVERWRITING_NCX': {}},), is_leaf=True, yang_name="status", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='enumeration', is_config=True)""",
        })

    self.__status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_status(self):
    self.__status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IGNORE': {}, u'OVERWRITING_DEVICE': {}, u'DETECTED': {}, u'OVERWRITING_NCX': {}},), is_leaf=True, yang_name="status", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='enumeration', is_config=True)


  def _get_detected_time(self):
    """
    Getter method for detected_time, mapped from YANG variable /reconciliation_entities/reconciliation_entity/detected_time (ndt:datetime)

    YANG Description: 0..4294967295
    """
    return self.__detected_time
      
  def _set_detected_time(self, v, load=False):
    """
    Setter method for detected_time, mapped from YANG variable /reconciliation_entities/reconciliation_entity/detected_time (ndt:datetime)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_detected_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_detected_time() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="detected-time", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='ndt:datetime', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """detected_time must be of a type compatible with ndt:datetime""",
          'defined-type': "ndt:datetime",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="detected-time", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='ndt:datetime', is_config=True)""",
        })

    self.__detected_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_detected_time(self):
    self.__detected_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="detected-time", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='ndt:datetime', is_config=True)


  def _get_last_action_time(self):
    """
    Getter method for last_action_time, mapped from YANG variable /reconciliation_entities/reconciliation_entity/last_action_time (ndt:datetime)

    YANG Description: 0..4294967295
    """
    return self.__last_action_time
      
  def _set_last_action_time(self, v, load=False):
    """
    Setter method for last_action_time, mapped from YANG variable /reconciliation_entities/reconciliation_entity/last_action_time (ndt:datetime)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_action_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_action_time() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-action-time", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='ndt:datetime', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_action_time must be of a type compatible with ndt:datetime""",
          'defined-type': "ndt:datetime",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-action-time", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='ndt:datetime', is_config=True)""",
        })

    self.__last_action_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_action_time(self):
    self.__last_action_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-action-time", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='ndt:datetime', is_config=True)

  entity_rcpath = __builtin__.property(_get_entity_rcpath, _set_entity_rcpath)
  device_id = __builtin__.property(_get_device_id, _set_device_id)
  service_path = __builtin__.property(_get_service_path, _set_service_path)
  operation_type = __builtin__.property(_get_operation_type, _set_operation_type)
  modified_leafs = __builtin__.property(_get_modified_leafs, _set_modified_leafs)
  child_entity = __builtin__.property(_get_child_entity, _set_child_entity)
  payload = __builtin__.property(_get_payload, _set_payload)
  status = __builtin__.property(_get_status, _set_status)
  detected_time = __builtin__.property(_get_detected_time, _set_detected_time)
  last_action_time = __builtin__.property(_get_last_action_time, _set_last_action_time)


  _pyangbind_elements = collections.OrderedDict([('entity_rcpath', entity_rcpath), ('device_id', device_id), ('service_path', service_path), ('operation_type', operation_type), ('modified_leafs', modified_leafs), ('child_entity', child_entity), ('payload', payload), ('status', status), ('detected_time', detected_time), ('last_action_time', last_action_time), ])


