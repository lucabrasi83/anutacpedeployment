
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
import naas_events
class event_subscriber_template(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /system/tables/event-subscriber-templates/event-subscriber-template. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__name','__subscriber_template_type','__default_template','__naas_events',)

  _yang_name = 'event-subscriber-template'
  _module_name = 'system'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__default_template = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-template", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    self.__naas_events = YANGDynClass(base=naas_events.naas_events, is_container='container', yang_name="naas-events", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__subscriber_template_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AMQP_BROKER': {}, u'USER': {}},), is_leaf=True, yang_name="subscriber-template-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='event-subscriber-type', is_config=True)

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
      return [u'system', u'tables', u'event-subscriber-templates', u'event-subscriber-template']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/tables/event_subscriber_templates/event_subscriber_template/name (string)

    YANG Description: string
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/tables/event_subscriber_templates/event_subscriber_template/name (string)
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


  def _get_subscriber_template_type(self):
    """
    Getter method for subscriber_template_type, mapped from YANG variable /system/tables/event_subscriber_templates/event_subscriber_template/subscriber_template_type (event-subscriber-type)

    YANG Description: USER
AMQP_BROKER

    """
    return self.__subscriber_template_type
      
  def _set_subscriber_template_type(self, v, load=False):
    """
    Setter method for subscriber_template_type, mapped from YANG variable /system/tables/event_subscriber_templates/event_subscriber_template/subscriber_template_type (event-subscriber-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subscriber_template_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subscriber_template_type() directly.

    YANG Description: USER
AMQP_BROKER

    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AMQP_BROKER': {}, u'USER': {}},), is_leaf=True, yang_name="subscriber-template-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='event-subscriber-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subscriber_template_type must be of a type compatible with event-subscriber-type""",
          'defined-type': "controller:event-subscriber-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AMQP_BROKER': {}, u'USER': {}},), is_leaf=True, yang_name="subscriber-template-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='event-subscriber-type', is_config=True)""",
        })

    self.__subscriber_template_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subscriber_template_type(self):
    self.__subscriber_template_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AMQP_BROKER': {}, u'USER': {}},), is_leaf=True, yang_name="subscriber-template-type", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='event-subscriber-type', is_config=True)


  def _get_default_template(self):
    """
    Getter method for default_template, mapped from YANG variable /system/tables/event_subscriber_templates/event_subscriber_template/default_template (boolean)

    YANG Description: default-template: True/False
    """
    return self.__default_template
      
  def _set_default_template(self, v, load=False):
    """
    Setter method for default_template, mapped from YANG variable /system/tables/event_subscriber_templates/event_subscriber_template/default_template (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_template is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_template() directly.

    YANG Description: default-template: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="default-template", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_template must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-template", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)""",
        })

    self.__default_template = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_template(self):
    self.__default_template = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-template", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)


  def _get_naas_events(self):
    """
    Getter method for naas_events, mapped from YANG variable /system/tables/event_subscriber_templates/event_subscriber_template/naas_events (container)
    """
    return self.__naas_events
      
  def _set_naas_events(self, v, load=False):
    """
    Setter method for naas_events, mapped from YANG variable /system/tables/event_subscriber_templates/event_subscriber_template/naas_events (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_naas_events is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_naas_events() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=naas_events.naas_events, is_container='container', yang_name="naas-events", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """naas_events must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=naas_events.naas_events, is_container='container', yang_name="naas-events", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)""",
        })

    self.__naas_events = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_naas_events(self):
    self.__naas_events = YANGDynClass(base=naas_events.naas_events, is_container='container', yang_name="naas-events", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  subscriber_template_type = __builtin__.property(_get_subscriber_template_type, _set_subscriber_template_type)
  default_template = __builtin__.property(_get_default_template, _set_default_template)
  naas_events = __builtin__.property(_get_naas_events, _set_naas_events)


  _pyangbind_elements = collections.OrderedDict([('name', name), ('subscriber_template_type', subscriber_template_type), ('default_template', default_template), ('naas_events', naas_events), ])


