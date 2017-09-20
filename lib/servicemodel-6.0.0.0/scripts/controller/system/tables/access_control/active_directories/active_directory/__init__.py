
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
class active_directory(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module controller - based on the path /system/tables/access-control/active-directories/active-directory. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__url','__domain','__accept_allthe_certifications','__row_version',)

  _yang_name = 'active-directory'
  _module_name = 'accesscontrol'
  _namespace = 'http://anutanetworks.com/controller'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__url = YANGDynClass(base=unicode, is_leaf=True, yang_name="url", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__accept_allthe_certifications = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="accept-allthe-certifications", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)
    self.__domain = YANGDynClass(base=unicode, is_leaf=True, yang_name="domain", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    self.__row_version = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="row-version", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=False)

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
      return [u'system', u'tables', u'access-control', u'active-directories', u'active-directory']

  def _get_url(self):
    """
    Getter method for url, mapped from YANG variable /system/tables/access_control/active_directories/active_directory/url (string)

    YANG Description: Eg: ldap://dc.example.com
    """
    return self.__url
      
  def _set_url(self, v, load=False):
    """
    Setter method for url, mapped from YANG variable /system/tables/access_control/active_directories/active_directory/url (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_url is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_url() directly.

    YANG Description: Eg: ldap://dc.example.com
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="url", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """url must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="url", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__url = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_url(self):
    self.__url = YANGDynClass(base=unicode, is_leaf=True, yang_name="url", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_domain(self):
    """
    Getter method for domain, mapped from YANG variable /system/tables/access_control/active_directories/active_directory/domain (string)

    YANG Description: Eg: example.com
    """
    return self.__domain
      
  def _set_domain(self, v, load=False):
    """
    Setter method for domain, mapped from YANG variable /system/tables/access_control/active_directories/active_directory/domain (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_domain is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_domain() directly.

    YANG Description: Eg: example.com
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="domain", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """domain must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="domain", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)""",
        })

    self.__domain = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_domain(self):
    self.__domain = YANGDynClass(base=unicode, is_leaf=True, yang_name="domain", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='string', is_config=True)


  def _get_accept_allthe_certifications(self):
    """
    Getter method for accept_allthe_certifications, mapped from YANG variable /system/tables/access_control/active_directories/active_directory/accept_allthe_certifications (boolean)

    YANG Description: accept-allthe-certifications: True/False
    """
    return self.__accept_allthe_certifications
      
  def _set_accept_allthe_certifications(self, v, load=False):
    """
    Setter method for accept_allthe_certifications, mapped from YANG variable /system/tables/access_control/active_directories/active_directory/accept_allthe_certifications (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_accept_allthe_certifications is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_accept_allthe_certifications() directly.

    YANG Description: accept-allthe-certifications: True/False
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="accept-allthe-certifications", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """accept_allthe_certifications must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="accept-allthe-certifications", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)""",
        })

    self.__accept_allthe_certifications = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_accept_allthe_certifications(self):
    self.__accept_allthe_certifications = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="accept-allthe-certifications", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='boolean', is_config=False)


  def _get_row_version(self):
    """
    Getter method for row_version, mapped from YANG variable /system/tables/access_control/active_directories/active_directory/row_version (uint32)

    YANG Description: 0..4294967295
    """
    return self.__row_version
      
  def _set_row_version(self, v, load=False):
    """
    Setter method for row_version, mapped from YANG variable /system/tables/access_control/active_directories/active_directory/row_version (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_row_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_row_version() directly.

    YANG Description: 0..4294967295
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="row-version", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """row_version must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="row-version", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=False)""",
        })

    self.__row_version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_row_version(self):
    self.__row_version = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="row-version", module_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://anutanetworks.com/controller', defining_module='controller', yang_type='uint32', is_config=False)

  url = __builtin__.property(_get_url, _set_url)
  domain = __builtin__.property(_get_domain, _set_domain)
  accept_allthe_certifications = __builtin__.property(_get_accept_allthe_certifications)
  row_version = __builtin__.property(_get_row_version)


  _pyangbind_elements = collections.OrderedDict([('url', url), ('domain', domain), ('accept_allthe_certifications', accept_allthe_certifications), ('row_version', row_version), ])


