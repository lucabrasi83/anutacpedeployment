
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
class sdr_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /devices/device/optimization-services/data-replication/datastore/sdr-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__sdr_policy',)

  _yang_name = 'sdr-policy'
  _module_name = 'wanoptimizer'
  _namespace = 'http://anutanetworks.com/wanoptimizer'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sdr_policy = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {}, u'sdr-a-advanced': {}, u'sdr-a': {}, u'sdr-m': {}},), is_leaf=True, yang_name="sdr-policy", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='enumeration', is_config=True)

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
      return [u'devices', u'device', u'optimization-services', u'data-replication', u'datastore', u'sdr-policy']

  def _get_sdr_policy(self):
    """
    Getter method for sdr_policy, mapped from YANG variable /devices/device/optimization_services/data_replication/datastore/sdr_policy/sdr_policy (enumeration)

    YANG Description: Displays the data store SDR policy.
    """
    return self.__sdr_policy
      
  def _set_sdr_policy(self, v, load=False):
    """
    Setter method for sdr_policy, mapped from YANG variable /devices/device/optimization_services/data_replication/datastore/sdr_policy/sdr_policy (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sdr_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sdr_policy() directly.

    YANG Description: Displays the data store SDR policy.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {}, u'sdr-a-advanced': {}, u'sdr-a': {}, u'sdr-m': {}},), is_leaf=True, yang_name="sdr-policy", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sdr_policy must be of a type compatible with enumeration""",
          'defined-type': "wanoptimizer:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {}, u'sdr-a-advanced': {}, u'sdr-a': {}, u'sdr-m': {}},), is_leaf=True, yang_name="sdr-policy", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='enumeration', is_config=True)""",
        })

    self.__sdr_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sdr_policy(self):
    self.__sdr_policy = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {}, u'sdr-a-advanced': {}, u'sdr-a': {}, u'sdr-m': {}},), is_leaf=True, yang_name="sdr-policy", module_name="wanoptimizer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/wanoptimizer', defining_module='wanoptimizer', yang_type='enumeration', is_config=True)

  sdr_policy = __builtin__.property(_get_sdr_policy, _set_sdr_policy)


  _pyangbind_elements = collections.OrderedDict([('sdr_policy', sdr_policy), ])


