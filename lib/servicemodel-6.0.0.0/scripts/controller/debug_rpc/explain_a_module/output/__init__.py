
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
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module debug - based on the path /debug_rpc/explain-a-module/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_netconf_operation_type', '_path_helper', '_yang_name', '_extmethods', '_module_name', '_namespace','__content',)

  _yang_name = 'output'
  _module_name = 'debug'
  _namespace = 'http://anutanetworks.com/debug'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__content = YANGDynClass(base=unicode, is_leaf=True, yang_name="content", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='ncx-types:cdata', is_config=True)

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
      return [u'debug_rpc', u'explain-a-module', u'output']

  def _get_content(self):
    """
    Getter method for content, mapped from YANG variable /debug_rpc/explain_a_module/output/content (ncx-types:cdata)

    YANG Description: string
    """
    return self.__content
      
  def _set_content(self, v, load=False):
    """
    Setter method for content, mapped from YANG variable /debug_rpc/explain_a_module/output/content (ncx-types:cdata)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_content is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_content() directly.

    YANG Description: string
    """
    try:
      if isEmpty(v):
        return
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="content", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='ncx-types:cdata', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """content must be of a type compatible with ncx-types:cdata""",
          'defined-type': "ncx-types:cdata",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="content", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='ncx-types:cdata', is_config=True)""",
        })

    self.__content = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_content(self):
    self.__content = YANGDynClass(base=unicode, is_leaf=True, yang_name="content", module_name="debug", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://anutanetworks.com/debug', defining_module='debug', yang_type='ncx-types:cdata', is_config=True)

  content = __builtin__.property(_get_content, _set_content)


  _pyangbind_elements = collections.OrderedDict([('content', content), ])


