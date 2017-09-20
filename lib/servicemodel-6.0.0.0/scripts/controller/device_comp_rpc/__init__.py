
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
import info_of_compliance_failed_devices
import run_device_compliance
import convert_to_compliance_template
import initialize_device_compliance_template_lite
class device_comp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module device-comp - based on the path /device_comp_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__info_of_compliance_failed_devices','__run_device_compliance','__convert_to_compliance_template','__initialize_device_compliance_template_lite',)

  _yang_name = 'device-comp'
  _module_name = 'device-comp'
  _namespace = 'http://anutanetworks.com/device-comp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__initialize_device_compliance_template_lite = YANGDynClass(base=initialize_device_compliance_template_lite.initialize_device_compliance_template_lite, is_leaf=True, yang_name="initialize-device-compliance-template-lite", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)
    self.__info_of_compliance_failed_devices = YANGDynClass(base=info_of_compliance_failed_devices.info_of_compliance_failed_devices, is_leaf=True, yang_name="info-of-compliance-failed-devices", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)
    self.__convert_to_compliance_template = YANGDynClass(base=convert_to_compliance_template.convert_to_compliance_template, is_leaf=True, yang_name="convert-to-compliance-template", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)
    self.__run_device_compliance = YANGDynClass(base=run_device_compliance.run_device_compliance, is_leaf=True, yang_name="run-device-compliance", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)

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
      return [u'device_comp_rpc']

  def _get_info_of_compliance_failed_devices(self):
    """
    Getter method for info_of_compliance_failed_devices, mapped from YANG variable /device_comp_rpc/info_of_compliance_failed_devices (rpc)
    """
    return self.__info_of_compliance_failed_devices
      
  def _set_info_of_compliance_failed_devices(self, v, load=False):
    """
    Setter method for info_of_compliance_failed_devices, mapped from YANG variable /device_comp_rpc/info_of_compliance_failed_devices (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_info_of_compliance_failed_devices is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_info_of_compliance_failed_devices() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=info_of_compliance_failed_devices.info_of_compliance_failed_devices, is_leaf=True, yang_name="info-of-compliance-failed-devices", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """info_of_compliance_failed_devices must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=info_of_compliance_failed_devices.info_of_compliance_failed_devices, is_leaf=True, yang_name="info-of-compliance-failed-devices", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)""",
        })

    self.__info_of_compliance_failed_devices = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_info_of_compliance_failed_devices(self):
    self.__info_of_compliance_failed_devices = YANGDynClass(base=info_of_compliance_failed_devices.info_of_compliance_failed_devices, is_leaf=True, yang_name="info-of-compliance-failed-devices", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)


  def _get_run_device_compliance(self):
    """
    Getter method for run_device_compliance, mapped from YANG variable /device_comp_rpc/run_device_compliance (rpc)
    """
    return self.__run_device_compliance
      
  def _set_run_device_compliance(self, v, load=False):
    """
    Setter method for run_device_compliance, mapped from YANG variable /device_comp_rpc/run_device_compliance (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_run_device_compliance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_run_device_compliance() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=run_device_compliance.run_device_compliance, is_leaf=True, yang_name="run-device-compliance", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """run_device_compliance must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=run_device_compliance.run_device_compliance, is_leaf=True, yang_name="run-device-compliance", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)""",
        })

    self.__run_device_compliance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_run_device_compliance(self):
    self.__run_device_compliance = YANGDynClass(base=run_device_compliance.run_device_compliance, is_leaf=True, yang_name="run-device-compliance", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)


  def _get_convert_to_compliance_template(self):
    """
    Getter method for convert_to_compliance_template, mapped from YANG variable /device_comp_rpc/convert_to_compliance_template (rpc)
    """
    return self.__convert_to_compliance_template
      
  def _set_convert_to_compliance_template(self, v, load=False):
    """
    Setter method for convert_to_compliance_template, mapped from YANG variable /device_comp_rpc/convert_to_compliance_template (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_convert_to_compliance_template is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_convert_to_compliance_template() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=convert_to_compliance_template.convert_to_compliance_template, is_leaf=True, yang_name="convert-to-compliance-template", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """convert_to_compliance_template must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=convert_to_compliance_template.convert_to_compliance_template, is_leaf=True, yang_name="convert-to-compliance-template", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)""",
        })

    self.__convert_to_compliance_template = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_convert_to_compliance_template(self):
    self.__convert_to_compliance_template = YANGDynClass(base=convert_to_compliance_template.convert_to_compliance_template, is_leaf=True, yang_name="convert-to-compliance-template", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)


  def _get_initialize_device_compliance_template_lite(self):
    """
    Getter method for initialize_device_compliance_template_lite, mapped from YANG variable /device_comp_rpc/initialize_device_compliance_template_lite (rpc)

    YANG Description: A device compliance template can vary in complexity. 
But, a user can get started with a lite version 
    """
    return self.__initialize_device_compliance_template_lite
      
  def _set_initialize_device_compliance_template_lite(self, v, load=False):
    """
    Setter method for initialize_device_compliance_template_lite, mapped from YANG variable /device_comp_rpc/initialize_device_compliance_template_lite (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_initialize_device_compliance_template_lite is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_initialize_device_compliance_template_lite() directly.

    YANG Description: A device compliance template can vary in complexity. 
But, a user can get started with a lite version 
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=initialize_device_compliance_template_lite.initialize_device_compliance_template_lite, is_leaf=True, yang_name="initialize-device-compliance-template-lite", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """initialize_device_compliance_template_lite must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=initialize_device_compliance_template_lite.initialize_device_compliance_template_lite, is_leaf=True, yang_name="initialize-device-compliance-template-lite", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)""",
        })

    self.__initialize_device_compliance_template_lite = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_initialize_device_compliance_template_lite(self):
    self.__initialize_device_compliance_template_lite = YANGDynClass(base=initialize_device_compliance_template_lite.initialize_device_compliance_template_lite, is_leaf=True, yang_name="initialize-device-compliance-template-lite", module_name="device-comp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/device-comp', defining_module='device-comp', yang_type='rpc', is_config=True)

  info_of_compliance_failed_devices = __builtin__.property(_get_info_of_compliance_failed_devices, _set_info_of_compliance_failed_devices)
  run_device_compliance = __builtin__.property(_get_run_device_compliance, _set_run_device_compliance)
  convert_to_compliance_template = __builtin__.property(_get_convert_to_compliance_template, _set_convert_to_compliance_template)
  initialize_device_compliance_template_lite = __builtin__.property(_get_initialize_device_compliance_template_lite, _set_initialize_device_compliance_template_lite)


  _pyangbind_elements = collections.OrderedDict([('info_of_compliance_failed_devices', info_of_compliance_failed_devices), ('run_device_compliance', run_device_compliance), ('convert_to_compliance_template', convert_to_compliance_template), ('initialize_device_compliance_template_lite', initialize_device_compliance_template_lite), ])


