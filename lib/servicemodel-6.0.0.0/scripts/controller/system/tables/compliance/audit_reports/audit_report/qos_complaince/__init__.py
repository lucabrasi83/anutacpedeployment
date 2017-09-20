
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
import qos_compliance
class qos_complaince(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /system/tables/compliance/audit-reports/audit-report/qos-complaince. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__qos_compliance',)

  _yang_name = 'qos-complaince'
  _module_name = 'compliance'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__qos_compliance = YANGDynClass(base=YANGListType("compliance_id",qos_compliance.qos_compliance, yang_name="qos-compliance", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='compliance-id'), is_container='list', yang_name="qos-compliance", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)

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
      return [u'system', u'tables', u'compliance', u'audit-reports', u'audit-report', u'qos-complaince']

  def _get_qos_compliance(self):
    """
    Getter method for qos_compliance, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/qos_complaince/qos_compliance (list)
    """
    return self.__qos_compliance
      
  def _set_qos_compliance(self, v, load=False):
    """
    Setter method for qos_compliance, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/qos_complaince/qos_compliance (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_qos_compliance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_qos_compliance() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("compliance_id",qos_compliance.qos_compliance, yang_name="qos-compliance", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='compliance-id'), is_container='list', yang_name="qos-compliance", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """qos_compliance must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("compliance_id",qos_compliance.qos_compliance, yang_name="qos-compliance", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='compliance-id'), is_container='list', yang_name="qos-compliance", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)""",
        })

    self.__qos_compliance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_qos_compliance(self):
    self.__qos_compliance = YANGDynClass(base=YANGListType("compliance_id",qos_compliance.qos_compliance, yang_name="qos-compliance", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='compliance-id'), is_container='list', yang_name="qos-compliance", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)

  qos_compliance = __builtin__.property(_get_qos_compliance, _set_qos_compliance)


  _pyangbind_elements = collections.OrderedDict([('qos_compliance', qos_compliance), ])


