
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
class move_rule(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/network-services/peering-rules/move-rule. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__id','__from_rule_num','__to_rule_num',)

  _yang_name = 'move-rule'
  _module_name = 'wanoptimizer'
  _namespace = 'http://anutanetworks.com/wanoptimizer'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__from_rule_num = YANGDynClass(base=unicode, is_leaf=True, yang_name="from-rule-num", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='leafref', is_config=True)
    self.__id = YANGDynClass(base=unicode, is_leaf=True, yang_name="id", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='string', is_config=True)
    self.__to_rule_num = YANGDynClass(base=unicode, is_leaf=True, yang_name="to-rule-num", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='leafref', is_config=True)

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
      return [u'devices', u'device', u'network-services', u'peering-rules', u'move-rule']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /devices/device/network_services/peering_rules/move_rule/id (string)

    YANG Description: info/description of move-rule or any unique-value as id
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /devices/device/network_services/peering_rules/move_rule/id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: info/description of move-rule or any unique-value as id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="id", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="id", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='string', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=unicode, is_leaf=True, yang_name="id", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='string', is_config=True)


  def _get_from_rule_num(self):
    """
    Getter method for from_rule_num, mapped from YANG variable /devices/device/network_services/peering_rules/move_rule/from_rule_num (leafref)

    YANG Description: from-rule-num
    """
    return self.__from_rule_num
      
  def _set_from_rule_num(self, v, load=False):
    """
    Setter method for from_rule_num, mapped from YANG variable /devices/device/network_services/peering_rules/move_rule/from_rule_num (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_from_rule_num is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_from_rule_num() directly.

    YANG Description: from-rule-num
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="from-rule-num", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """from_rule_num must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="from-rule-num", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='leafref', is_config=True)""",
        })

    self.__from_rule_num = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_from_rule_num(self):
    self.__from_rule_num = YANGDynClass(base=unicode, is_leaf=True, yang_name="from-rule-num", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='leafref', is_config=True)


  def _get_to_rule_num(self):
    """
    Getter method for to_rule_num, mapped from YANG variable /devices/device/network_services/peering_rules/move_rule/to_rule_num (leafref)

    YANG Description: to-rule-num
    """
    return self.__to_rule_num
      
  def _set_to_rule_num(self, v, load=False):
    """
    Setter method for to_rule_num, mapped from YANG variable /devices/device/network_services/peering_rules/move_rule/to_rule_num (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_to_rule_num is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_to_rule_num() directly.

    YANG Description: to-rule-num
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="to-rule-num", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """to_rule_num must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="to-rule-num", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='leafref', is_config=True)""",
        })

    self.__to_rule_num = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_to_rule_num(self):
    self.__to_rule_num = YANGDynClass(base=unicode, is_leaf=True, yang_name="to-rule-num", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='leafref', is_config=True)

  id = __builtin__.property(_get_id, _set_id)
  from_rule_num = __builtin__.property(_get_from_rule_num, _set_from_rule_num)
  to_rule_num = __builtin__.property(_get_to_rule_num, _set_to_rule_num)


  _pyangbind_elements = collections.OrderedDict([('id', id), ('from_rule_num', from_rule_num), ('to_rule_num', to_rule_num), ])


