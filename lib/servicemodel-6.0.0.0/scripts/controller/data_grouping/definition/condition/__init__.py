
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
class condition(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /data-grouping/definition/condition. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__property','__operation_type','__value','__expression',)

  _yang_name = 'condition'
  _module_name = 'datagrouping'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__operation_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'PRECONFIG': {}, u'PARSE_TEMPLATE': {}, u'CREATE': {}, u'UPDATE': {}, u'SYSTEM': {}, u'PARSE': {}, u'POSTCONFIG': {}, u'FETCH': {}, u'DELETE': {}},), is_leaf=True, yang_name="operation-type", module_name="controller", parent=self, choice=(u'condition-type', u'property'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='operation-type', is_config=True)
    self.__property = YANGDynClass(base=unicode, is_leaf=True, yang_name="property", module_name="controller", parent=self, choice=(u'condition-type', u'property'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__expression = YANGDynClass(base=unicode, is_leaf=True, yang_name="expression", module_name="controller", parent=self, choice=(u'condition-type', u'expression'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__value = YANGDynClass(base=unicode, is_leaf=True, yang_name="value", module_name="controller", parent=self, choice=(u'condition-type', u'property'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

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
      return [u'data-grouping', u'definition', u'condition']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /data_grouping/definition/condition/name (string)

    YANG Description: Unique name for conditions.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /data_grouping/definition/condition/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Unique name for conditions.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_property(self):
    """
    Getter method for property, mapped from YANG variable /data_grouping/definition/condition/property (string)

    YANG Description: string
    """
    return self.__property
      
  def _set_property(self, v, load=False):
    """
    Setter method for property, mapped from YANG variable /data_grouping/definition/condition/property (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_property is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_property() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="property", module_name="controller", parent=self, choice=(u'condition-type', u'property'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """property must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="property", module_name="controller", parent=self, choice=(u'condition-type', u'property'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__property = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_property(self):
    self.__property = YANGDynClass(base=unicode, is_leaf=True, yang_name="property", module_name="controller", parent=self, choice=(u'condition-type', u'property'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_operation_type(self):
    """
    Getter method for operation_type, mapped from YANG variable /data_grouping/definition/condition/operation_type (operation-type)

    YANG Description: equals
not-equals
gt
lt
gte
lte
in
starts-with
contains

    """
    return self.__operation_type
      
  def _set_operation_type(self, v, load=False):
    """
    Setter method for operation_type, mapped from YANG variable /data_grouping/definition/condition/operation_type (operation-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_operation_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_operation_type() directly.

    YANG Description: equals
not-equals
gt
lt
gte
lte
in
starts-with
contains

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'PRECONFIG': {}, u'PARSE_TEMPLATE': {}, u'CREATE': {}, u'UPDATE': {}, u'SYSTEM': {}, u'PARSE': {}, u'POSTCONFIG': {}, u'FETCH': {}, u'DELETE': {}},), is_leaf=True, yang_name="operation-type", module_name="controller", parent=self, choice=(u'condition-type', u'property'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='operation-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """operation_type must be of a type compatible with operation-type""",
          'defined-type': "controller:operation-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'PRECONFIG': {}, u'PARSE_TEMPLATE': {}, u'CREATE': {}, u'UPDATE': {}, u'SYSTEM': {}, u'PARSE': {}, u'POSTCONFIG': {}, u'FETCH': {}, u'DELETE': {}},), is_leaf=True, yang_name="operation-type", module_name="controller", parent=self, choice=(u'condition-type', u'property'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='operation-type', is_config=True)""",
        })

    self.__operation_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_operation_type(self):
    self.__operation_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'PRECONFIG': {}, u'PARSE_TEMPLATE': {}, u'CREATE': {}, u'UPDATE': {}, u'SYSTEM': {}, u'PARSE': {}, u'POSTCONFIG': {}, u'FETCH': {}, u'DELETE': {}},), is_leaf=True, yang_name="operation-type", module_name="controller", parent=self, choice=(u'condition-type', u'property'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='operation-type', is_config=True)


  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /data_grouping/definition/condition/value (string)

    YANG Description: string
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /data_grouping/definition/condition/value (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="value", module_name="controller", parent=self, choice=(u'condition-type', u'property'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="value", module_name="controller", parent=self, choice=(u'condition-type', u'property'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=unicode, is_leaf=True, yang_name="value", module_name="controller", parent=self, choice=(u'condition-type', u'property'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_expression(self):
    """
    Getter method for expression, mapped from YANG variable /data_grouping/definition/condition/expression (string)

    YANG Description: xpath expression. Ex: propertyname='value', prop1='val1' and prop2='val2', prop1='val1' or prop2='val2'
    """
    return self.__expression
      
  def _set_expression(self, v, load=False):
    """
    Setter method for expression, mapped from YANG variable /data_grouping/definition/condition/expression (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_expression is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_expression() directly.

    YANG Description: xpath expression. Ex: propertyname='value', prop1='val1' and prop2='val2', prop1='val1' or prop2='val2'
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="expression", module_name="controller", parent=self, choice=(u'condition-type', u'expression'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """expression must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="expression", module_name="controller", parent=self, choice=(u'condition-type', u'expression'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__expression = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_expression(self):
    self.__expression = YANGDynClass(base=unicode, is_leaf=True, yang_name="expression", module_name="controller", parent=self, choice=(u'condition-type', u'expression'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  property = __builtin__.property(_get_property, _set_property)
  operation_type = __builtin__.property(_get_operation_type, _set_operation_type)
  value = __builtin__.property(_get_value, _set_value)
  expression = __builtin__.property(_get_expression, _set_expression)

  __choices__ = {u'condition-type': {u'property': [u'property', u'operation_type', u'value'], u'expression': [u'expression']}}
  _pyangbind_elements = collections.OrderedDict([('name', name), ('property', property), ('operation_type', operation_type), ('value', value), ('expression', expression), ])


