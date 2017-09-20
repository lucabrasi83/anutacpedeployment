
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
import deployment_profile
class deployment_profiles(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /virtual-appliance/deployment-profiles. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__deployment_profile',)

  _yang_name = 'deployment-profiles'
  _module_name = 'virtualappliance'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__deployment_profile = YANGDynClass(base=YANGListType("vim_ip",deployment_profile.deployment_profile, yang_name="deployment-profile", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vim-ip'), is_container='list', yang_name="deployment-profile", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)

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
      return [u'virtual-appliance', u'deployment-profiles']

  def _get_deployment_profile(self):
    """
    Getter method for deployment_profile, mapped from YANG variable /virtual_appliance/deployment_profiles/deployment_profile (list)
    """
    return self.__deployment_profile
      
  def _set_deployment_profile(self, v, load=False):
    """
    Setter method for deployment_profile, mapped from YANG variable /virtual_appliance/deployment_profiles/deployment_profile (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_deployment_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_deployment_profile() directly.
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGListType("vim_ip",deployment_profile.deployment_profile, yang_name="deployment-profile", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vim-ip'), is_container='list', yang_name="deployment-profile", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """deployment_profile must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vim_ip",deployment_profile.deployment_profile, yang_name="deployment-profile", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vim-ip'), is_container='list', yang_name="deployment-profile", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)""",
        })

    self.__deployment_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_deployment_profile(self):
    self.__deployment_profile = YANGDynClass(base=YANGListType("vim_ip",deployment_profile.deployment_profile, yang_name="deployment-profile", module_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vim-ip'), is_container='list', yang_name="deployment-profile", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='list', is_config=True)

  deployment_profile = __builtin__.property(_get_deployment_profile, _set_deployment_profile)


  _pyangbind_elements = collections.OrderedDict([('deployment_profile', deployment_profile), ])


