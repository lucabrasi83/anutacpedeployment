
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
import vm_power_on
import vm_power_off
import vm_suspend
import vm_reboot
import vm_assign_port_group
import vm_destroy
import update_vm_status
import get_vm_state
import deploy_vm
class vnfdriver(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module vnfdriver - based on the path /vnfdriver_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__vm_power_on','__vm_power_off','__vm_suspend','__vm_reboot','__vm_assign_port_group','__vm_destroy','__update_vm_status','__get_vm_state','__deploy_vm',)

  _yang_name = 'vnfdriver'
  _module_name = 'vnfdriver'
  _namespace = 'http://anutanetworks.com/vnfdriver'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vm_power_on = YANGDynClass(base=vm_power_on.vm_power_on, is_leaf=True, yang_name="vm-power-on", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    self.__deploy_vm = YANGDynClass(base=deploy_vm.deploy_vm, is_leaf=True, yang_name="deploy-vm", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    self.__vm_power_off = YANGDynClass(base=vm_power_off.vm_power_off, is_leaf=True, yang_name="vm-power-off", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    self.__get_vm_state = YANGDynClass(base=get_vm_state.get_vm_state, is_leaf=True, yang_name="get-vm-state", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    self.__update_vm_status = YANGDynClass(base=update_vm_status.update_vm_status, is_leaf=True, yang_name="update-vm-status", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    self.__vm_assign_port_group = YANGDynClass(base=vm_assign_port_group.vm_assign_port_group, is_leaf=True, yang_name="vm-assign-port-group", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    self.__vm_destroy = YANGDynClass(base=vm_destroy.vm_destroy, is_leaf=True, yang_name="vm-destroy", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    self.__vm_reboot = YANGDynClass(base=vm_reboot.vm_reboot, is_leaf=True, yang_name="vm-reboot", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    self.__vm_suspend = YANGDynClass(base=vm_suspend.vm_suspend, is_leaf=True, yang_name="vm-suspend", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)

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
      return [u'vnfdriver_rpc']

  def _get_vm_power_on(self):
    """
    Getter method for vm_power_on, mapped from YANG variable /vnfdriver_rpc/vm_power_on (rpc)

    YANG Description: Power on the VM
    """
    return self.__vm_power_on
      
  def _set_vm_power_on(self, v, load=False):
    """
    Setter method for vm_power_on, mapped from YANG variable /vnfdriver_rpc/vm_power_on (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vm_power_on is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vm_power_on() directly.

    YANG Description: Power on the VM
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=vm_power_on.vm_power_on, is_leaf=True, yang_name="vm-power-on", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vm_power_on must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=vm_power_on.vm_power_on, is_leaf=True, yang_name="vm-power-on", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)""",
        })

    self.__vm_power_on = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vm_power_on(self):
    self.__vm_power_on = YANGDynClass(base=vm_power_on.vm_power_on, is_leaf=True, yang_name="vm-power-on", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)


  def _get_vm_power_off(self):
    """
    Getter method for vm_power_off, mapped from YANG variable /vnfdriver_rpc/vm_power_off (rpc)

    YANG Description: Power off the VM
    """
    return self.__vm_power_off
      
  def _set_vm_power_off(self, v, load=False):
    """
    Setter method for vm_power_off, mapped from YANG variable /vnfdriver_rpc/vm_power_off (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vm_power_off is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vm_power_off() directly.

    YANG Description: Power off the VM
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=vm_power_off.vm_power_off, is_leaf=True, yang_name="vm-power-off", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vm_power_off must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=vm_power_off.vm_power_off, is_leaf=True, yang_name="vm-power-off", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)""",
        })

    self.__vm_power_off = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vm_power_off(self):
    self.__vm_power_off = YANGDynClass(base=vm_power_off.vm_power_off, is_leaf=True, yang_name="vm-power-off", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)


  def _get_vm_suspend(self):
    """
    Getter method for vm_suspend, mapped from YANG variable /vnfdriver_rpc/vm_suspend (rpc)

    YANG Description: Suspend the VM
    """
    return self.__vm_suspend
      
  def _set_vm_suspend(self, v, load=False):
    """
    Setter method for vm_suspend, mapped from YANG variable /vnfdriver_rpc/vm_suspend (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vm_suspend is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vm_suspend() directly.

    YANG Description: Suspend the VM
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=vm_suspend.vm_suspend, is_leaf=True, yang_name="vm-suspend", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vm_suspend must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=vm_suspend.vm_suspend, is_leaf=True, yang_name="vm-suspend", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)""",
        })

    self.__vm_suspend = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vm_suspend(self):
    self.__vm_suspend = YANGDynClass(base=vm_suspend.vm_suspend, is_leaf=True, yang_name="vm-suspend", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)


  def _get_vm_reboot(self):
    """
    Getter method for vm_reboot, mapped from YANG variable /vnfdriver_rpc/vm_reboot (rpc)

    YANG Description: Reboot the VM
    """
    return self.__vm_reboot
      
  def _set_vm_reboot(self, v, load=False):
    """
    Setter method for vm_reboot, mapped from YANG variable /vnfdriver_rpc/vm_reboot (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vm_reboot is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vm_reboot() directly.

    YANG Description: Reboot the VM
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=vm_reboot.vm_reboot, is_leaf=True, yang_name="vm-reboot", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vm_reboot must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=vm_reboot.vm_reboot, is_leaf=True, yang_name="vm-reboot", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)""",
        })

    self.__vm_reboot = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vm_reboot(self):
    self.__vm_reboot = YANGDynClass(base=vm_reboot.vm_reboot, is_leaf=True, yang_name="vm-reboot", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)


  def _get_vm_assign_port_group(self):
    """
    Getter method for vm_assign_port_group, mapped from YANG variable /vnfdriver_rpc/vm_assign_port_group (rpc)

    YANG Description: Assign port group in VM
    """
    return self.__vm_assign_port_group
      
  def _set_vm_assign_port_group(self, v, load=False):
    """
    Setter method for vm_assign_port_group, mapped from YANG variable /vnfdriver_rpc/vm_assign_port_group (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vm_assign_port_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vm_assign_port_group() directly.

    YANG Description: Assign port group in VM
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=vm_assign_port_group.vm_assign_port_group, is_leaf=True, yang_name="vm-assign-port-group", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vm_assign_port_group must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=vm_assign_port_group.vm_assign_port_group, is_leaf=True, yang_name="vm-assign-port-group", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)""",
        })

    self.__vm_assign_port_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vm_assign_port_group(self):
    self.__vm_assign_port_group = YANGDynClass(base=vm_assign_port_group.vm_assign_port_group, is_leaf=True, yang_name="vm-assign-port-group", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)


  def _get_vm_destroy(self):
    """
    Getter method for vm_destroy, mapped from YANG variable /vnfdriver_rpc/vm_destroy (rpc)

    YANG Description: Destroy the VM
    """
    return self.__vm_destroy
      
  def _set_vm_destroy(self, v, load=False):
    """
    Setter method for vm_destroy, mapped from YANG variable /vnfdriver_rpc/vm_destroy (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vm_destroy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vm_destroy() directly.

    YANG Description: Destroy the VM
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=vm_destroy.vm_destroy, is_leaf=True, yang_name="vm-destroy", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vm_destroy must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=vm_destroy.vm_destroy, is_leaf=True, yang_name="vm-destroy", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)""",
        })

    self.__vm_destroy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vm_destroy(self):
    self.__vm_destroy = YANGDynClass(base=vm_destroy.vm_destroy, is_leaf=True, yang_name="vm-destroy", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)


  def _get_update_vm_status(self):
    """
    Getter method for update_vm_status, mapped from YANG variable /vnfdriver_rpc/update_vm_status (rpc)

    YANG Description: Update the VM status
    """
    return self.__update_vm_status
      
  def _set_update_vm_status(self, v, load=False):
    """
    Setter method for update_vm_status, mapped from YANG variable /vnfdriver_rpc/update_vm_status (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_update_vm_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_update_vm_status() directly.

    YANG Description: Update the VM status
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=update_vm_status.update_vm_status, is_leaf=True, yang_name="update-vm-status", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """update_vm_status must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=update_vm_status.update_vm_status, is_leaf=True, yang_name="update-vm-status", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)""",
        })

    self.__update_vm_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_update_vm_status(self):
    self.__update_vm_status = YANGDynClass(base=update_vm_status.update_vm_status, is_leaf=True, yang_name="update-vm-status", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)


  def _get_get_vm_state(self):
    """
    Getter method for get_vm_state, mapped from YANG variable /vnfdriver_rpc/get_vm_state (rpc)

    YANG Description: Get the VM state
    """
    return self.__get_vm_state
      
  def _set_get_vm_state(self, v, load=False):
    """
    Setter method for get_vm_state, mapped from YANG variable /vnfdriver_rpc/get_vm_state (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_vm_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_vm_state() directly.

    YANG Description: Get the VM state
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=get_vm_state.get_vm_state, is_leaf=True, yang_name="get-vm-state", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_vm_state must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_vm_state.get_vm_state, is_leaf=True, yang_name="get-vm-state", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)""",
        })

    self.__get_vm_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_vm_state(self):
    self.__get_vm_state = YANGDynClass(base=get_vm_state.get_vm_state, is_leaf=True, yang_name="get-vm-state", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)


  def _get_deploy_vm(self):
    """
    Getter method for deploy_vm, mapped from YANG variable /vnfdriver_rpc/deploy_vm (rpc)

    YANG Description: Deploying VM
    """
    return self.__deploy_vm
      
  def _set_deploy_vm(self, v, load=False):
    """
    Setter method for deploy_vm, mapped from YANG variable /vnfdriver_rpc/deploy_vm (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_deploy_vm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_deploy_vm() directly.

    YANG Description: Deploying VM
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=deploy_vm.deploy_vm, is_leaf=True, yang_name="deploy-vm", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """deploy_vm must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=deploy_vm.deploy_vm, is_leaf=True, yang_name="deploy-vm", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)""",
        })

    self.__deploy_vm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_deploy_vm(self):
    self.__deploy_vm = YANGDynClass(base=deploy_vm.deploy_vm, is_leaf=True, yang_name="deploy-vm", module_name="vnfdriver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/vnfdriver', defining_module='vnfdriver', yang_type='rpc', is_config=True)

  vm_power_on = __builtin__.property(_get_vm_power_on, _set_vm_power_on)
  vm_power_off = __builtin__.property(_get_vm_power_off, _set_vm_power_off)
  vm_suspend = __builtin__.property(_get_vm_suspend, _set_vm_suspend)
  vm_reboot = __builtin__.property(_get_vm_reboot, _set_vm_reboot)
  vm_assign_port_group = __builtin__.property(_get_vm_assign_port_group, _set_vm_assign_port_group)
  vm_destroy = __builtin__.property(_get_vm_destroy, _set_vm_destroy)
  update_vm_status = __builtin__.property(_get_update_vm_status, _set_update_vm_status)
  get_vm_state = __builtin__.property(_get_get_vm_state, _set_get_vm_state)
  deploy_vm = __builtin__.property(_get_deploy_vm, _set_deploy_vm)


  _pyangbind_elements = collections.OrderedDict([('vm_power_on', vm_power_on), ('vm_power_off', vm_power_off), ('vm_suspend', vm_suspend), ('vm_reboot', vm_reboot), ('vm_assign_port_group', vm_assign_port_group), ('vm_destroy', vm_destroy), ('update_vm_status', update_vm_status), ('get_vm_state', get_vm_state), ('deploy_vm', deploy_vm), ])


