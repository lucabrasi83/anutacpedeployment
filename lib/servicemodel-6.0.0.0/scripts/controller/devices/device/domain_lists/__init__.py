
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
import domain_list
class domain_lists(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/domain-lists. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__domain_list',)

  _yang_name = 'domain-lists'
  _module_name = 'wanoptimizer'
  _namespace = 'http://anutanetworks.com/wanoptimizer'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__domain_list = YANGDynClass(base=YANGListType("domain_list_value",domain_list.domain_list, yang_name="domain-list", module_name="wanoptimizer", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='domain-list-value'), is_container='list', yang_name="domain-list", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='list', is_config=True)

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
      return [u'devices', u'device', u'domain-lists']

  def _get_domain_list(self):
    """
    Getter method for domain_list, mapped from YANG variable /devices/device/domain_lists/domain_list (list)
    """
    return self.__domain_list
      
  def _set_domain_list(self, v, load=False):
    """
    Setter method for domain_list, mapped from YANG variable /devices/device/domain_lists/domain_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_domain_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_domain_list() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("domain_list_value",domain_list.domain_list, yang_name="domain-list", module_name="wanoptimizer", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='domain-list-value'), is_container='list', yang_name="domain-list", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """domain_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("domain_list_value",domain_list.domain_list, yang_name="domain-list", module_name="wanoptimizer", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='domain-list-value'), is_container='list', yang_name="domain-list", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='list', is_config=True)""",
        })

    self.__domain_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_domain_list(self):
    self.__domain_list = YANGDynClass(base=YANGListType("domain_list_value",domain_list.domain_list, yang_name="domain-list", module_name="wanoptimizer", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='domain-list-value'), is_container='list', yang_name="domain-list", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='list', is_config=True)

  domain_list = __builtin__.property(_get_domain_list, _set_domain_list)


  _pyangbind_elements = collections.OrderedDict([('domain_list', domain_list), ])


