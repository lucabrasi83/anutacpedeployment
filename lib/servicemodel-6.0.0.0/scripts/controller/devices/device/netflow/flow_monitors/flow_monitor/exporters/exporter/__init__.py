
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
class exporter(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/netflow/flow-monitors/flow-monitor/exporters/exporter. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__exporter',)

  _yang_name = 'exporter'
  _module_name = 'l3features'
  _namespace = 'http://anutanetworks.com/l3features'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__exporter = YANGDynClass(base=unicode, is_leaf=True, yang_name="exporter", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)

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
      return [u'devices', u'device', u'netflow', u'flow-monitors', u'flow-monitor', u'exporters', u'exporter']

  def _get_exporter(self):
    """
    Getter method for exporter, mapped from YANG variable /devices/device/netflow/flow_monitors/flow_monitor/exporters/exporter/exporter (string)

    YANG Description: Flow Exporter
    """
    return self.__exporter
      
  def _set_exporter(self, v, load=False):
    """
    Setter method for exporter, mapped from YANG variable /devices/device/netflow/flow_monitors/flow_monitor/exporters/exporter/exporter (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exporter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exporter() directly.

    YANG Description: Flow Exporter
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="exporter", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exporter must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="exporter", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)""",
        })

    self.__exporter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exporter(self):
    self.__exporter = YANGDynClass(base=unicode, is_leaf=True, yang_name="exporter", module_name="l3features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/l3features', defining_module='l3features', yang_type='string', is_config=True)

  exporter = __builtin__.property(_get_exporter, _set_exporter)


  _pyangbind_elements = collections.OrderedDict([('exporter', exporter), ])


