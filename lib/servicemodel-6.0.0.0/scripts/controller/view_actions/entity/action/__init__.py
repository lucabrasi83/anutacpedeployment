
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
class action(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /view-actions/entity/action. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__default_display_name','__multi_instance','__selection_required','__code','__icon','__service_url','__action_type','__parent_action',)

  _yang_name = 'action'
  _module_name = 'view-actions'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__parent_action = YANGDynClass(base=unicode, is_leaf=True, yang_name="parent-action", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__code = YANGDynClass(base=unicode, is_leaf=True, yang_name="code", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__service_url = YANGDynClass(base=unicode, is_leaf=True, yang_name="service-url", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__action_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'VIEW_TEMPLATE': {}, u'RPC': {}, u'REST': {}, u'rest': {}, u'view-template': {}},), is_leaf=True, yang_name="action-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='v-enums:action-type', is_config=True)
    self.__selection_required = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="selection-required", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    self.__default_display_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="default-display-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__multi_instance = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multi-instance", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    self.__icon = YANGDynClass(base=unicode, is_leaf=True, yang_name="icon", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

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
      return [u'view-actions', u'entity', u'action']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /view_actions/entity/action/name (string)

    YANG Description: string
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /view_actions/entity/action/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: string
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


  def _get_default_display_name(self):
    """
    Getter method for default_display_name, mapped from YANG variable /view_actions/entity/action/default_display_name (string)

    YANG Description: string
    """
    return self.__default_display_name
      
  def _set_default_display_name(self, v, load=False):
    """
    Setter method for default_display_name, mapped from YANG variable /view_actions/entity/action/default_display_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_display_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_display_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="default-display-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_display_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="default-display-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__default_display_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_display_name(self):
    self.__default_display_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="default-display-name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_multi_instance(self):
    """
    Getter method for multi_instance, mapped from YANG variable /view_actions/entity/action/multi_instance (boolean)

    YANG Description: multi-instance: True/False
    """
    return self.__multi_instance
      
  def _set_multi_instance(self, v, load=False):
    """
    Setter method for multi_instance, mapped from YANG variable /view_actions/entity/action/multi_instance (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multi_instance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multi_instance() directly.

    YANG Description: multi-instance: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="multi-instance", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multi_instance must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multi-instance", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)""",
        })

    self.__multi_instance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multi_instance(self):
    self.__multi_instance = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multi-instance", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)


  def _get_selection_required(self):
    """
    Getter method for selection_required, mapped from YANG variable /view_actions/entity/action/selection_required (boolean)

    YANG Description: selection-required: True/False
    """
    return self.__selection_required
      
  def _set_selection_required(self, v, load=False):
    """
    Setter method for selection_required, mapped from YANG variable /view_actions/entity/action/selection_required (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_selection_required is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_selection_required() directly.

    YANG Description: selection-required: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="selection-required", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """selection_required must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="selection-required", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)""",
        })

    self.__selection_required = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_selection_required(self):
    self.__selection_required = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="selection-required", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)


  def _get_code(self):
    """
    Getter method for code, mapped from YANG variable /view_actions/entity/action/code (string)

    YANG Description: string
    """
    return self.__code
      
  def _set_code(self, v, load=False):
    """
    Setter method for code, mapped from YANG variable /view_actions/entity/action/code (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_code is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_code() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="code", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """code must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="code", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__code = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_code(self):
    self.__code = YANGDynClass(base=unicode, is_leaf=True, yang_name="code", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_icon(self):
    """
    Getter method for icon, mapped from YANG variable /view_actions/entity/action/icon (string)

    YANG Description: string
    """
    return self.__icon
      
  def _set_icon(self, v, load=False):
    """
    Setter method for icon, mapped from YANG variable /view_actions/entity/action/icon (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_icon is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_icon() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="icon", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """icon must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="icon", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__icon = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_icon(self):
    self.__icon = YANGDynClass(base=unicode, is_leaf=True, yang_name="icon", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_service_url(self):
    """
    Getter method for service_url, mapped from YANG variable /view_actions/entity/action/service_url (string)

    YANG Description: string
    """
    return self.__service_url
      
  def _set_service_url(self, v, load=False):
    """
    Setter method for service_url, mapped from YANG variable /view_actions/entity/action/service_url (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_service_url is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_service_url() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="service-url", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """service_url must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="service-url", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__service_url = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_service_url(self):
    self.__service_url = YANGDynClass(base=unicode, is_leaf=True, yang_name="service-url", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_action_type(self):
    """
    Getter method for action_type, mapped from YANG variable /view_actions/entity/action/action_type (v-enums:action-type)

    YANG Description: rest
view-template
REST
RPC
VIEW_TEMPLATE

    """
    return self.__action_type
      
  def _set_action_type(self, v, load=False):
    """
    Setter method for action_type, mapped from YANG variable /view_actions/entity/action/action_type (v-enums:action-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action_type() directly.

    YANG Description: rest
view-template
REST
RPC
VIEW_TEMPLATE

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'VIEW_TEMPLATE': {}, u'RPC': {}, u'REST': {}, u'rest': {}, u'view-template': {}},), is_leaf=True, yang_name="action-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='v-enums:action-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action_type must be of a type compatible with v-enums:action-type""",
          'defined-type': "v-enums:action-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'VIEW_TEMPLATE': {}, u'RPC': {}, u'REST': {}, u'rest': {}, u'view-template': {}},), is_leaf=True, yang_name="action-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='v-enums:action-type', is_config=True)""",
        })

    self.__action_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action_type(self):
    self.__action_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'VIEW_TEMPLATE': {}, u'RPC': {}, u'REST': {}, u'rest': {}, u'view-template': {}},), is_leaf=True, yang_name="action-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='v-enums:action-type', is_config=True)


  def _get_parent_action(self):
    """
    Getter method for parent_action, mapped from YANG variable /view_actions/entity/action/parent_action (string)

    YANG Description: string
    """
    return self.__parent_action
      
  def _set_parent_action(self, v, load=False):
    """
    Setter method for parent_action, mapped from YANG variable /view_actions/entity/action/parent_action (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_parent_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_parent_action() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="parent-action", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """parent_action must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="parent-action", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__parent_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_parent_action(self):
    self.__parent_action = YANGDynClass(base=unicode, is_leaf=True, yang_name="parent-action", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  default_display_name = __builtin__.property(_get_default_display_name, _set_default_display_name)
  multi_instance = __builtin__.property(_get_multi_instance, _set_multi_instance)
  selection_required = __builtin__.property(_get_selection_required, _set_selection_required)
  code = __builtin__.property(_get_code, _set_code)
  icon = __builtin__.property(_get_icon, _set_icon)
  service_url = __builtin__.property(_get_service_url, _set_service_url)
  action_type = __builtin__.property(_get_action_type, _set_action_type)
  parent_action = __builtin__.property(_get_parent_action, _set_parent_action)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('default_display_name', default_display_name), ('multi_instance', multi_instance), ('selection_required', selection_required), ('code', code), ('icon', icon), ('service_url', service_url), ('action_type', action_type), ('parent_action', parent_action), ])


