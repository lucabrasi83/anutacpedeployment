
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
import qos_complaince
import l2l3_compliance
class audit_report(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /system/tables/compliance/audit-reports/audit-report. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__report_id','__lb_comp','__security','__vpc_id','__qos','__l2l3','__last_successful','__last_executed','__details','__qos_complaince','__l2l3_compliance',)

  _yang_name = 'audit-report'
  _module_name = 'system'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__l2l3_compliance = YANGDynClass(base=l2l3_compliance.l2l3_compliance, is_container='container', yang_name="l2l3-compliance", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)
    self.__qos = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="qos", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    self.__qos_complaince = YANGDynClass(base=qos_complaince.qos_complaince, is_container='container', yang_name="qos-complaince", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)
    self.__last_executed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-executed", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)
    self.__details = YANGDynClass(base=unicode, is_leaf=True, yang_name="details", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__vpc_id = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vpc-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    self.__security = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="security", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    self.__lb_comp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lb-comp", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    self.__l2l3 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l2l3", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    self.__last_successful = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-successful", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)
    self.__report_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="report-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)

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
      return [u'system', u'tables', u'compliance', u'audit-reports', u'audit-report']

  def _get_report_id(self):
    """
    Getter method for report_id, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/report_id (string)

    YANG Description: string
    """
    return self.__report_id
      
  def _set_report_id(self, v, load=False):
    """
    Setter method for report_id, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/report_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_report_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_report_id() directly.

    YANG Description: string
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="report-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """report_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="report-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__report_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_report_id(self):
    self.__report_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="report-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_lb_comp(self):
    """
    Getter method for lb_comp, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/lb_comp (boolean)

    YANG Description: lb-comp: True/False
    """
    return self.__lb_comp
      
  def _set_lb_comp(self, v, load=False):
    """
    Setter method for lb_comp, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/lb_comp (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lb_comp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lb_comp() directly.

    YANG Description: lb-comp: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lb-comp", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lb_comp must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lb-comp", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)""",
        })

    self.__lb_comp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lb_comp(self):
    self.__lb_comp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lb-comp", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)


  def _get_security(self):
    """
    Getter method for security, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/security (boolean)

    YANG Description: security: True/False
    """
    return self.__security
      
  def _set_security(self, v, load=False):
    """
    Setter method for security, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/security (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_security is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_security() directly.

    YANG Description: security: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="security", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """security must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="security", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)""",
        })

    self.__security = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_security(self):
    self.__security = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="security", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)


  def _get_vpc_id(self):
    """
    Getter method for vpc_id, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/vpc_id (boolean)

    YANG Description: vpc-id: True/False
    """
    return self.__vpc_id
      
  def _set_vpc_id(self, v, load=False):
    """
    Setter method for vpc_id, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/vpc_id (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vpc_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vpc_id() directly.

    YANG Description: vpc-id: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="vpc-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vpc_id must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vpc-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)""",
        })

    self.__vpc_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vpc_id(self):
    self.__vpc_id = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vpc-id", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)


  def _get_qos(self):
    """
    Getter method for qos, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/qos (boolean)

    YANG Description: qos: True/False
    """
    return self.__qos
      
  def _set_qos(self, v, load=False):
    """
    Setter method for qos, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/qos (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_qos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_qos() directly.

    YANG Description: qos: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="qos", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """qos must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="qos", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)""",
        })

    self.__qos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_qos(self):
    self.__qos = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="qos", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)


  def _get_l2l3(self):
    """
    Getter method for l2l3, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/l2l3 (boolean)

    YANG Description: l2l3: True/False
    """
    return self.__l2l3
      
  def _set_l2l3(self, v, load=False):
    """
    Setter method for l2l3, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/l2l3 (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l2l3 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l2l3() directly.

    YANG Description: l2l3: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="l2l3", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l2l3 must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l2l3", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)""",
        })

    self.__l2l3 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l2l3(self):
    self.__l2l3 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l2l3", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=True)


  def _get_last_successful(self):
    """
    Getter method for last_successful, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/last_successful (uint32)

    YANG Description: 0..4294967295
    """
    return self.__last_successful
      
  def _set_last_successful(self, v, load=False):
    """
    Setter method for last_successful, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/last_successful (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_successful is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_successful() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-successful", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_successful must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-successful", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)""",
        })

    self.__last_successful = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_successful(self):
    self.__last_successful = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-successful", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)


  def _get_last_executed(self):
    """
    Getter method for last_executed, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/last_executed (uint32)

    YANG Description: 0..4294967295
    """
    return self.__last_executed
      
  def _set_last_executed(self, v, load=False):
    """
    Setter method for last_executed, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/last_executed (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_executed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_executed() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-executed", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_executed must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-executed", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)""",
        })

    self.__last_executed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_executed(self):
    self.__last_executed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-executed", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=True)


  def _get_details(self):
    """
    Getter method for details, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/details (string)

    YANG Description: string
    """
    return self.__details
      
  def _set_details(self, v, load=False):
    """
    Setter method for details, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/details (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_details is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_details() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="details", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """details must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="details", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__details = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_details(self):
    self.__details = YANGDynClass(base=unicode, is_leaf=True, yang_name="details", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_qos_complaince(self):
    """
    Getter method for qos_complaince, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/qos_complaince (container)
    """
    return self.__qos_complaince
      
  def _set_qos_complaince(self, v, load=False):
    """
    Setter method for qos_complaince, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/qos_complaince (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_qos_complaince is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_qos_complaince() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=qos_complaince.qos_complaince, is_container='container', yang_name="qos-complaince", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """qos_complaince must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=qos_complaince.qos_complaince, is_container='container', yang_name="qos-complaince", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)""",
        })

    self.__qos_complaince = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_qos_complaince(self):
    self.__qos_complaince = YANGDynClass(base=qos_complaince.qos_complaince, is_container='container', yang_name="qos-complaince", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)


  def _get_l2l3_compliance(self):
    """
    Getter method for l2l3_compliance, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/l2l3_compliance (container)
    """
    return self.__l2l3_compliance
      
  def _set_l2l3_compliance(self, v, load=False):
    """
    Setter method for l2l3_compliance, mapped from YANG variable /system/tables/compliance/audit_reports/audit_report/l2l3_compliance (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l2l3_compliance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l2l3_compliance() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=l2l3_compliance.l2l3_compliance, is_container='container', yang_name="l2l3-compliance", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l2l3_compliance must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=l2l3_compliance.l2l3_compliance, is_container='container', yang_name="l2l3-compliance", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)""",
        })

    self.__l2l3_compliance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l2l3_compliance(self):
    self.__l2l3_compliance = YANGDynClass(base=l2l3_compliance.l2l3_compliance, is_container='container', yang_name="l2l3-compliance", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='container', is_config=True)

  report_id = __builtin__.property(_get_report_id, _set_report_id)
  lb_comp = __builtin__.property(_get_lb_comp, _set_lb_comp)
  security = __builtin__.property(_get_security, _set_security)
  vpc_id = __builtin__.property(_get_vpc_id, _set_vpc_id)
  qos = __builtin__.property(_get_qos, _set_qos)
  l2l3 = __builtin__.property(_get_l2l3, _set_l2l3)
  last_successful = __builtin__.property(_get_last_successful, _set_last_successful)
  last_executed = __builtin__.property(_get_last_executed, _set_last_executed)
  details = __builtin__.property(_get_details, _set_details)
  qos_complaince = __builtin__.property(_get_qos_complaince, _set_qos_complaince)
  l2l3_compliance = __builtin__.property(_get_l2l3_compliance, _set_l2l3_compliance)


  _pyangbind_elements = collections.OrderedDict([('report_id', report_id), ('lb_comp', lb_comp), ('security', security), ('vpc_id', vpc_id), ('qos', qos), ('l2l3', l2l3), ('last_successful', last_successful), ('last_executed', last_executed), ('details', details), ('qos_complaince', qos_complaince), ('l2l3_compliance', l2l3_compliance), ])


