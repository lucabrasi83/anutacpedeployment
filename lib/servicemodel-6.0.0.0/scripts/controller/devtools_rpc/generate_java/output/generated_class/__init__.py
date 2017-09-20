
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
class generated_class(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module devtools - based on the path /devtools_rpc/generate-java/output/generated-class. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__file_name','__file_location','__content',)

  _yang_name = 'generated-class'
  _module_name = 'devtools'
  _namespace = 'http://anutanetworks.com/devtools'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__content = YANGDynClass(base=unicode, is_leaf=True, yang_name="content", module_name="devtools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/devtools', defining_module='devtools', yang_type='string', is_config=True)
    self.__file_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="file-name", module_name="devtools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/devtools', defining_module='devtools', yang_type='string', is_config=True)
    self.__file_location = YANGDynClass(base=unicode, is_leaf=True, yang_name="file-location", module_name="devtools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/devtools', defining_module='devtools', yang_type='string', is_config=True)

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
      return [u'devtools_rpc', u'generate-java', u'output', u'generated-class']

  def _get_file_name(self):
    """
    Getter method for file_name, mapped from YANG variable /devtools_rpc/generate_java/output/generated_class/file_name (string)

    YANG Description: string
    """
    return self.__file_name
      
  def _set_file_name(self, v, load=False):
    """
    Setter method for file_name, mapped from YANG variable /devtools_rpc/generate_java/output/generated_class/file_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_file_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_file_name() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="file-name", module_name="devtools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/devtools', defining_module='devtools', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """file_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="file-name", module_name="devtools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/devtools', defining_module='devtools', yang_type='string', is_config=True)""",
        })

    self.__file_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_file_name(self):
    self.__file_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="file-name", module_name="devtools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/devtools', defining_module='devtools', yang_type='string', is_config=True)


  def _get_file_location(self):
    """
    Getter method for file_location, mapped from YANG variable /devtools_rpc/generate_java/output/generated_class/file_location (string)

    YANG Description: string
    """
    return self.__file_location
      
  def _set_file_location(self, v, load=False):
    """
    Setter method for file_location, mapped from YANG variable /devtools_rpc/generate_java/output/generated_class/file_location (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_file_location is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_file_location() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="file-location", module_name="devtools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/devtools', defining_module='devtools', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """file_location must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="file-location", module_name="devtools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/devtools', defining_module='devtools', yang_type='string', is_config=True)""",
        })

    self.__file_location = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_file_location(self):
    self.__file_location = YANGDynClass(base=unicode, is_leaf=True, yang_name="file-location", module_name="devtools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/devtools', defining_module='devtools', yang_type='string', is_config=True)


  def _get_content(self):
    """
    Getter method for content, mapped from YANG variable /devtools_rpc/generate_java/output/generated_class/content (string)

    YANG Description: generated java class content 
    """
    return self.__content
      
  def _set_content(self, v, load=False):
    """
    Setter method for content, mapped from YANG variable /devtools_rpc/generate_java/output/generated_class/content (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_content is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_content() directly.

    YANG Description: generated java class content 
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="content", module_name="devtools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/devtools', defining_module='devtools', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """content must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="content", module_name="devtools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/devtools', defining_module='devtools', yang_type='string', is_config=True)""",
        })

    self.__content = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_content(self):
    self.__content = YANGDynClass(base=unicode, is_leaf=True, yang_name="content", module_name="devtools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/devtools', defining_module='devtools', yang_type='string', is_config=True)

  file_name = __builtin__.property(_get_file_name, _set_file_name)
  file_location = __builtin__.property(_get_file_location, _set_file_location)
  content = __builtin__.property(_get_content, _set_content)


  _pyangbind_elements = collections.OrderedDict([('file_name', file_name), ('file_location', file_location), ('content', content), ])


