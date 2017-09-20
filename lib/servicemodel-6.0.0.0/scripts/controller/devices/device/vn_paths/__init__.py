
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
import vn_path
class vn_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/vn-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__vn_path',)

  _yang_name = 'vn-paths'
  _module_name = 'l2features'
  _namespace = 'http://anutanetworks.com/l2features'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vn_path = YANGDynClass(base=YANGListType("path_name",vn_path.vn_path, yang_name="vn-path", module_name="l2features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path-name'), is_container='list', yang_name="vn-path", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='list', is_config=True)

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
      return [u'devices', u'device', u'vn-paths']

  def _get_vn_path(self):
    """
    Getter method for vn_path, mapped from YANG variable /devices/device/vn_paths/vn_path (list)
    """
    return self.__vn_path
      
  def _set_vn_path(self, v, load=False):
    """
    Setter method for vn_path, mapped from YANG variable /devices/device/vn_paths/vn_path (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vn_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vn_path() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("path_name",vn_path.vn_path, yang_name="vn-path", module_name="l2features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path-name'), is_container='list', yang_name="vn-path", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vn_path must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("path_name",vn_path.vn_path, yang_name="vn-path", module_name="l2features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path-name'), is_container='list', yang_name="vn-path", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='list', is_config=True)""",
        })

    self.__vn_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vn_path(self):
    self.__vn_path = YANGDynClass(base=YANGListType("path_name",vn_path.vn_path, yang_name="vn-path", module_name="l2features", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path-name'), is_container='list', yang_name="vn-path", module_name="l2features", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/l2features', defining_module='l2features', yang_type='list', is_config=True)

  vn_path = __builtin__.property(_get_vn_path, _set_vn_path)


  _pyangbind_elements = collections.OrderedDict([('vn_path', vn_path), ])


