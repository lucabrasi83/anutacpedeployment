
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
import ipv4
import interface
import application
import counter
import art
import transport
import timestamp
class collect(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/netflow/flow-records/flow-record/collect. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__ipv4','__interface','__application','__counter','__art','__transport','__timestamp',)

  _yang_name = 'collect'
  _module_name = 'l3features'
  _namespace = 'http://anutanetworks.com/l3features'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__art = YANGDynClass(base=art.art, is_container='container', yang_name="art", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    self.__timestamp = YANGDynClass(base=timestamp.timestamp, is_container='container', yang_name="timestamp", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    self.__counter = YANGDynClass(base=counter.counter, is_container='container', yang_name="counter", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    self.__application = YANGDynClass(base=application.application, is_container='container', yang_name="application", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    self.__ipv4 = YANGDynClass(base=ipv4.ipv4, is_container='container', yang_name="ipv4", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    self.__transport = YANGDynClass(base=transport.transport, is_container='container', yang_name="transport", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)

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
      return [u'devices', u'device', u'netflow', u'flow-records', u'flow-record', u'collect']

  def _get_ipv4(self):
    """
    Getter method for ipv4, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/ipv4 (container)
    """
    return self.__ipv4
      
  def _set_ipv4(self, v, load=False):
    """
    Setter method for ipv4, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/ipv4 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=ipv4.ipv4, is_container='container', yang_name="ipv4", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv4.ipv4, is_container='container', yang_name="ipv4", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)""",
        })

    self.__ipv4 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4(self):
    self.__ipv4 = YANGDynClass(base=ipv4.ipv4, is_container='container', yang_name="ipv4", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/interface (container)
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=interface.interface, is_container='container', yang_name="interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)


  def _get_application(self):
    """
    Getter method for application, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/application (container)
    """
    return self.__application
      
  def _set_application(self, v, load=False):
    """
    Setter method for application, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/application (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_application is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_application() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=application.application, is_container='container', yang_name="application", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """application must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=application.application, is_container='container', yang_name="application", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)""",
        })

    self.__application = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_application(self):
    self.__application = YANGDynClass(base=application.application, is_container='container', yang_name="application", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)


  def _get_counter(self):
    """
    Getter method for counter, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/counter (container)
    """
    return self.__counter
      
  def _set_counter(self, v, load=False):
    """
    Setter method for counter, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/counter (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_counter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_counter() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=counter.counter, is_container='container', yang_name="counter", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """counter must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=counter.counter, is_container='container', yang_name="counter", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)""",
        })

    self.__counter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_counter(self):
    self.__counter = YANGDynClass(base=counter.counter, is_container='container', yang_name="counter", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)


  def _get_art(self):
    """
    Getter method for art, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/art (container)
    """
    return self.__art
      
  def _set_art(self, v, load=False):
    """
    Setter method for art, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/art (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_art is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_art() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=art.art, is_container='container', yang_name="art", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """art must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=art.art, is_container='container', yang_name="art", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)""",
        })

    self.__art = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_art(self):
    self.__art = YANGDynClass(base=art.art, is_container='container', yang_name="art", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)


  def _get_transport(self):
    """
    Getter method for transport, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/transport (container)
    """
    return self.__transport
      
  def _set_transport(self, v, load=False):
    """
    Setter method for transport, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/transport (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transport is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transport() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=transport.transport, is_container='container', yang_name="transport", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transport must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=transport.transport, is_container='container', yang_name="transport", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)""",
        })

    self.__transport = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transport(self):
    self.__transport = YANGDynClass(base=transport.transport, is_container='container', yang_name="transport", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)


  def _get_timestamp(self):
    """
    Getter method for timestamp, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/timestamp (container)
    """
    return self.__timestamp
      
  def _set_timestamp(self, v, load=False):
    """
    Setter method for timestamp, mapped from YANG variable /devices/device/netflow/flow_records/flow_record/collect/timestamp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timestamp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timestamp() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=timestamp.timestamp, is_container='container', yang_name="timestamp", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timestamp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=timestamp.timestamp, is_container='container', yang_name="timestamp", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)""",
        })

    self.__timestamp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timestamp(self):
    self.__timestamp = YANGDynClass(base=timestamp.timestamp, is_container='container', yang_name="timestamp", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='container', is_config=True)

  ipv4 = __builtin__.property(_get_ipv4, _set_ipv4)
  interface = __builtin__.property(_get_interface, _set_interface)
  application = __builtin__.property(_get_application, _set_application)
  counter = __builtin__.property(_get_counter, _set_counter)
  art = __builtin__.property(_get_art, _set_art)
  transport = __builtin__.property(_get_transport, _set_transport)
  timestamp = __builtin__.property(_get_timestamp, _set_timestamp)


  _pyangbind_elements = collections.OrderedDict([('ipv4', ipv4), ('interface', interface), ('application', application), ('counter', counter), ('art', art), ('transport', transport), ('timestamp', timestamp), ])


