
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
import wccp
import inpath
import agent_interception
class interception(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/wanop/interception. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__wccp','__inpath','__agent_interception',)

  _yang_name = 'interception'
  _module_name = 'wanoptimizer'
  _namespace = 'http://anutanetworks.com/wanoptimizer'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__agent_interception = YANGDynClass(base=agent_interception.agent_interception, is_container='container', yang_name="agent-interception", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)
    self.__inpath = YANGDynClass(base=inpath.inpath, is_container='container', yang_name="inpath", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)
    self.__wccp = YANGDynClass(base=wccp.wccp, is_container='container', yang_name="wccp", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)

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
      return [u'devices', u'device', u'wanop', u'interception']

  def _get_wccp(self):
    """
    Getter method for wccp, mapped from YANG variable /devices/device/wanop/interception/wccp (container)
    """
    return self.__wccp
      
  def _set_wccp(self, v, load=False):
    """
    Setter method for wccp, mapped from YANG variable /devices/device/wanop/interception/wccp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wccp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wccp() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=wccp.wccp, is_container='container', yang_name="wccp", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wccp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=wccp.wccp, is_container='container', yang_name="wccp", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)""",
        })

    self.__wccp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wccp(self):
    self.__wccp = YANGDynClass(base=wccp.wccp, is_container='container', yang_name="wccp", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)


  def _get_inpath(self):
    """
    Getter method for inpath, mapped from YANG variable /devices/device/wanop/interception/inpath (container)
    """
    return self.__inpath
      
  def _set_inpath(self, v, load=False):
    """
    Setter method for inpath, mapped from YANG variable /devices/device/wanop/interception/inpath (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_inpath is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_inpath() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=inpath.inpath, is_container='container', yang_name="inpath", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """inpath must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=inpath.inpath, is_container='container', yang_name="inpath", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)""",
        })

    self.__inpath = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_inpath(self):
    self.__inpath = YANGDynClass(base=inpath.inpath, is_container='container', yang_name="inpath", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)


  def _get_agent_interception(self):
    """
    Getter method for agent_interception, mapped from YANG variable /devices/device/wanop/interception/agent_interception (container)
    """
    return self.__agent_interception
      
  def _set_agent_interception(self, v, load=False):
    """
    Setter method for agent_interception, mapped from YANG variable /devices/device/wanop/interception/agent_interception (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_agent_interception is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_agent_interception() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=agent_interception.agent_interception, is_container='container', yang_name="agent-interception", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """agent_interception must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=agent_interception.agent_interception, is_container='container', yang_name="agent-interception", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)""",
        })

    self.__agent_interception = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_agent_interception(self):
    self.__agent_interception = YANGDynClass(base=agent_interception.agent_interception, is_container='container', yang_name="agent-interception", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='container', is_config=True)

  wccp = __builtin__.property(_get_wccp, _set_wccp)
  inpath = __builtin__.property(_get_inpath, _set_inpath)
  agent_interception = __builtin__.property(_get_agent_interception, _set_agent_interception)


  _pyangbind_elements = collections.OrderedDict([('wccp', wccp), ('inpath', inpath), ('agent_interception', agent_interception), ])


