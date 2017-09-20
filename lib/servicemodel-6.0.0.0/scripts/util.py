#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2014-2015 Anuta Networks, Inc. All Rights Reserved.

import uuid
import sys, traceback
#from servicemodel import yang
try:
  from com.anuta.python import LogWriter
except ImportError:
  pass
try:
  from java.util import Collection
  from org.xml.sax import InputSource
  from com.anuta.yang.base import YangSchemaNode
  from com.anuta.util import ApplicationContextProvider
  from java.io import StringReader
  from javax.xml.parsers import DocumentBuilderFactory
  from org.xml.sax import InputSource
  from com.anuta.security import AnutaEncryptor
  from java.util import Arrays
  from com.anuta.service.devicemgr.execplan.dto import ScriptDeviceResultAggregator
except ImportError:
  exc_type, exc_value, exc_traceback = sys.exc_info()
  LogWriter.log_error('Exception: %s\n' % (traceback.format_exception(exc_type, exc_value, exc_traceback)))


import re
import sys
import traceback
import untangle

def test():
    xmlstr = '<l3service><params><param><name>test</name><value>value1</value></param><param><name>name2</name><value>value2</value></param></params></l3service>'
    document = getDocument(xmlstr)
    xml = XmlWrapper(document.getDocumentElement()).parse()
    log_debug('--------------------------------------')
    log_debug('%s' % (xml.l3service.params.param[1].name))
    log_debug('--------------------------------------')
    log_debug('%s' % (xml.toXml()))


def getDocument(xmlstr):
    try:
        return DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(InputSource(StringReader(xmlstr)))
    except ImportError:
        obj = untangle.parse(xmlstr)
        return obj


def parseXmlString(xmlstr):
    try:
        document = getDocument(xmlstr)
        return XmlWrapper(document.getDocumentElement()).parse()
    except ImportError:
        obj = untangle.parse(xmlstr)
        return obj


def getRootElementName(baseobj):
    fields = baseobj.get_field_names()
    if fields == None or len(fields) == 0:
        return None
    log_debug('len = %d, fields = %s' % (len(fields), fields))
    if len(fields) > 1:
        log_debug('Root element has more fields. count = %d' % len(fields))
    return fields[0]

def getUUID():
    return str(uuid.uuid1())

def create_yang_subtree(name, build_mode = True):
    if build_mode:
        obj = DynamicBaseObj(build_mode)
    else:
        obj = BaseObj(build_mode)
        
    obj.set_name(name)
    return obj

class BaseObject(object):

    """ A wrapper object that represents the root element of the xml document """

    def __init__(self, root_element_name):
        self.xmlObj = BaseObj()
        self.root = BaseObj()
        self.xmlObj.add_field_value(root_element_name, self.root)

    def set_field_value(self, name, value):
        """
        Set value to the field
        
        Args:
        field name: name of the field
        value: value to be assigned 
        Returns
        none
        """
        self.root.set_field_value(name, value)

    def toXml(self):
        """
        Convert BaseObj to xml

        Args:
        None
        Returns
        xml structure equivalent to BaseObj
        """
        return self.xmlObj.toXml()

class BaseObj(object):

    """ Base object representing the parsed xml object.

    The xml element tree is parsed into a set of BaseObj objects. For example, for a xml input
    '<root><elem1>some val</elem1><elem2></elem2></root>', we can access the elements as root.elem1 and root.elem2
    It can handle nested objects. Leaf objects (including containers) are converted into arrays when required

    get_field_value() method is used so that any missing/optional elements dont result in an exception

    toXml() converts the object tree into a xml string
    """

    def __init__(self):
        self._fields = {}

    def add_field(self, field, value=None):
        """ Add field with given value

        Args:
        fieldname: name of the field
        value: value to be assigned
        Returns:
        None if the attribute doesn't exist
        """
        if(value == None):
            value = field
        self._fields[field] = value

    def get_field_names(self):
        """ Get names of the field

        Args:
        None
        Returns:
        Attributes of the BaseObj
        """
        return self._fields.keys()

    def get_first_field(self):
        if isEmpty(self._fields):
            return None
        return self.get_field_value(self._fields.keys()[0])

    def get_fields(self):
        """

        Args:
        None
        Returns
        BaseObj
        """
        return self._fields

    def add_field_value(self, fieldname, value, xmlfield=None):
        """
        Add value to the field

        Args:
        field name: name of the field
        value: value to be assigned 
        Returns
        none
        """
        self.process_field_value(fieldname, value, xmlfield)

    def set_field_value(self, fieldname, value, xmlfield=None):
        """
        Set value to the field

        Args:
        field name: name of the field
        value: value to be assigned 
        Returns
        none
        """
        if hasattr(self, fieldname):
            delattr(self, fieldname)
        self.process_field_value(fieldname, value, xmlfield)

    def process_field_value(self, fieldname, value, xmlfield=None):
        """
        Process field for the given value
        If the field is not having the value and it will be added with the given value

        Args:
        field name: name of the field
        value: value to be assigned 
        Returns
        none
        """
        # log_debug('process_field_value: .....setting %s' % (fieldname))
        if isEmpty(xmlfield):
            xmlfield = fieldname
        fieldname = fieldname.replace(':', '_')
        fieldname = fieldname.replace('-', '_')

        if not hasattr(self, fieldname):
            self.add_field(fieldname, xmlfield)
            setattr(self, fieldname, value)
            return
        curval = getattr(self, fieldname)
        if not isinstance(curval, list):
            #log_debug('converted to an array')
            curval = [curval]
            setattr(self, fieldname, curval)
        curval.append(value)

    def get_field_value(self, fieldname, as_array=False):
        """ Get the field value for a given field name

        Args:
        fieldname: name of the field
        as_array: convert the result into an array
        Returns:
        None if the attribute doesn't exist
        Empty array of as_array is True
        A valid value (or list of as_array is true - even if a non-list value is present, it will be converted to a list)
        """
        if not hasattr(self, fieldname):
            if as_array:
                return []
            return None
        curval = getattr(self, fieldname)
        if not as_array:
            return curval
        if isinstance(curval, list):
            return curval
        if isinstance(curval, Collection):
            return curval
        return [curval]

    @staticmethod
    def get_string_value(name, value):
        """
        Get string corresponding to value
        
        Args:
        value: Need to convert to string
        Returns:
        String corresponding to value
        """

        if isinstance(value, list):
            strval = ''
            for val in value:
                strval += BaseObj.get_string_value(val)
            return strval

        return '%s' % (value)

    def toXml(self, rootelem=None):
        """
        Convert BaseObj to xml
        
        Args:
        None
        Returns
        xml structure equivalent to BaseObj
        """
        buf = '\n'
        for field, xmlfield in self._fields.items():
            value = getattr(self, field)
            if isinstance(value, BaseObj):
                buf += '<%s>%s</%s>' % (xmlfield, value.toXml(), xmlfield)
                continue
            if isinstance(value, BaseObject):
                buf += value.toXml()
                continue
            if not isinstance(value, list):
                if isEmpty(value):
                    buf += '<%s />' % (xmlfield)
                else:
                    buf += '<%s>%s</%s>' % (xmlfield, value, xmlfield)
                continue
            # this is a list type
            if len(value) == 0:
                buf += '<%s />' % (xmlfield)
                continue
            #log_debug('Array: [%s]' % (value))
            for val in value:
                if isinstance(val, BaseObj):
                    #buf += '<%s>%s</%s>' % (xmlfield, val.toXml(), xmlfield)
                    buf += val.toXml()
                elif isinstance(val, BaseObject):
                    #buf += '<%s>%s</%s>' % (xmlfield, val.toXml(), xmlfield)
                    buf += val.toXml()
                else:
                    buf += '<%s>%s</%s>' % (xmlfield, val, xmlfield)

        if rootelem is not None:
            buf = '<%s>%s</%s>' % (rootelem, buf, rootelem)
        return buf

    def __str__(self):
        buf = '{'
        for field in self._fields.keys():
            val = getattr(self, field)
            if isinstance(val, list):
                valbuf = '['
                for v in val:
                    valbuf += ('%s, ' % (v))
                valbuf += ']'
                val = valbuf

            str = '%s: %s' % (field, val)
            buf += str
            buf += "\n"
        buf += '}'
        return buf

class DynamicBaseObj(object):

    """ Base object representing the parsed xml object.

    The xml element tree is parsed into a set of BaseObj objects. For example, for a xml input
    '<root><elem1>some val</elem1><elem2></elem2></root>', we can access the elements as root.elem1 and root.elem2
    It can handle nested objects. Leaf objects (including containers) are converted into arrays when required

    get_field_value() method is used so that any missing/optional elements dont result in an exception

    toXml() converts the object tree into a xml string
    """

    def __init__(self, build_mode = False, name = None):
        object.__setattr__(self, '_fields', {})
        object.__setattr__(self, '_map', {})
        object.__setattr__(self, '_build_mode', build_mode)
        object.__setattr__(self, '_name', name)

    def set_build_mode(self, val):
        self._build_mode = val

    def get_first_field(self):
        if isEmpty(self._fields):
            return None
        return self.get_field_value(self._fields.keys()[0])
 
    def set_name(self, name):
        object.__setattr__(self, '_name', name)

    def __setattr__(self, fieldname, value):
        fieldname = self.py2xmlfield(fieldname)
        self.set_field_value(fieldname, value)

    def __getattr__(self, name):
        val = self.get_field_value(name)
        if val == None:
            if self._build_mode:
                newobj = DynamicBaseObj(True, name)
                self.__setattr__(name, newobj)
                return newobj
        return val

    def __getitem__(self, index):
        try:
            arr = object.__getattribute__(self, '_array_')
        except AttributeError:
            arr = None
        if arr == None:
            arr = []
            object.__setattr__(self, '_array_', arr)
        if index == len(arr):
            if self._build_mode:
                newobj = DynamicBaseObj(True, self._name)
                arr.append(newobj)
        return arr[index]
    
    def __setitem__(self, idx, value):
        try:
            arr = object.__getattribute__(self, '_array_')
        except AttributeError:
            arr = None
        if arr == None:
            arr = []
            object.__setattr__(self, '_array_', arr)
        if idx == len(arr):
            if self._build_mode:
                arr.append(value)
                return value
        arr[value]
        return value
    
    def append(self, value):
        try:
            arr = object.__getattribute__(self, '_array_')
        except AttributeError:
            arr = None
        if arr == None:
            raise Exception('%s is not a list' % (type(self)))
        arr.append(value)

    def __iter__(self):
        try:
            arr = object.__getattribute__(self, '_array_')
        except AttributeError:
            arr = None
        if arr == None:
            arr = [self]
        return arr.__iter__()
 
    def add_field(self, field, value=None):
        """ Add field with given value

        Args:
        fieldname: name of the field
        value: value to be assigned
        Returns:
        None if the attribute doesn't exist
        """
        if field not in self._fields:
            if(value == None):
                value = field
            self._fields[field] = value

    def get_field_names(self):
        """ Get names of the field
        
        Args:
        None
        Returns:
        Attributes of the BaseObj
        """
        return self._fields.keys()

    def get_fields(self):
        """
        
        Args:
        None
        Returns
        BaseObj
        """
        return self._fields

    def add_field_value(self, fieldname, value, xmlfield=None):
        """
        Add value to the field
        
        Args:
        field name: name of the field
        value: value to be assigned 
        Returns
        none
        """
        self.process_field_value(fieldname, value, xmlfield)

    def set_field_value(self, fieldname, value, xmlfield=None):
        """
        Set value to the field
        
        Args:
        field name: name of the field
        value: value to be assigned 
        Returns
        none
        """
        self.process_field_value(fieldname, value, xmlfield)

    def py2xmlfield(self, fieldname):
        fieldname = fieldname.replace('_', '-')
        fieldname = fieldname.replace('\-', '_')
        return fieldname

    def xml2pyfield(self, fieldname):
        fieldname = fieldname.replace(':', '_')
        fieldname = fieldname.replace('-', '_')
        return fieldname
        
    def process_field_value(self, fieldname, value, xmlfield=None):
        """
        Process field for the given value
        If the field is not having the value and it will be added with the given value
        
        Args:
        field name: name of the field
        value: value to be assigned 
        Returns
        none
        """
        # log_debug('process_field_value: .....setting %s' % (fieldname))
        if isEmpty(xmlfield):
            xmlfield = fieldname
        fieldname = self.xml2pyfield(fieldname)

        if isinstance(value, dict):
            value = DynamicBaseObj(self._build_mode, fieldname)

        if fieldname not in self._map:
            self.add_field(fieldname, xmlfield)
            self._map[fieldname] = value
            return
        curval = self._map[fieldname]
        if not isinstance(curval, list):
            #log_debug('converted to an array')
            curval = [curval]
            self._map[fieldname] =  curval
        curval.append(value)

    def get_field_value(self, fieldname, as_array=False):
        """ Get the field value for a given field name

        Args:
        fieldname: name of the field
        as_array: convert the result into an array
        Returns:
        None if the attribute doesn't exist
        Empty array of as_array is True
        A valid value (or list of as_array is true - even if a non-list value is present, it will be converted to a list)
        """
        if fieldname not in self._map:
            if as_array:
                return []
            return None
        curval = self._map[fieldname]
        if not as_array:
            return curval
        if isinstance(curval, list):
            return curval
        if isinstance(curval, Collection):
            return curval
        return [curval]

    @staticmethod
    def get_string_value(name, value):
        """
        Get string corresponding to value
        
        Args:
        value: Need to convert to string
        Returns:
        String corresponding to value
        """

        if isinstance(value, list):
            strval = ''
            for val in value:
                strval += BaseObj.get_string_value(val)
            return strval

        return '%s' % (value)

    def toXml(self, rootelem=None, level = 0):
        #log_debug('TOXML: %d' % (level))
        """
        Convert BaseObj to xml
        
        Args:
        None
        Returns
        xml structure equivalent to BaseObj
        """
        INDENT_STR = '   '
        buf = ''
        if rootelem is None and level == 0:
            rootelem = self._name
        rootelem = self.py2xmlfield(rootelem)
        indent = INDENT_STR * level

        try:
            arr = object.__getattribute__(self, '_array_')
        except AttributeError:
            arr = None

        if arr != None:
            value = arr
            buf = self.indent(buf, indent)
            if len(value) == 0:
                buf = self.indent(buf, indent)
                return buf
            #log_debug('Array: [%s]' % (value))
            for val in value:
                if isinstance(val, BaseObj):
                    #buf += '<%s>%s</%s>' % (xmlfield, val.toXml(), xmlfield)
                    if len(buf) > 0:
                        buf += '\n'
                    buf += val.toXml(level + 1)
                elif isinstance(val, BaseObject):
                    #buf += '<%s>%s</%s>' % (xmlfield, val.toXml(), xmlfield)
                    buf += '\n'
                    buf += val.toXml(level + 1)
                elif isinstance(val, DynamicBaseObj):
                    #buf += '<%s>%s</%s>' % (xmlfield, val.toXml(), xmlfield)
                    buf += '\n%s' % (indent)
                    buf += val.toXml(val._name, level)
                else:
                    buf += self.indent(buf, indent)
                    buf += val
            return buf
            
        for field, xmlfield in self._fields.items():
            value = getattr(self, field)
            #log_debug('TYPE: field = [%s], type = [%s], values = [%s]' % (field, type(value), value))
            if isinstance(value, BaseObj):
                buf = self.indent(buf, indent)
                buf += '<%s>\n' % (xmlfield)
                buf += value.toXml(None, level + 1)
                buf = self.indent(buf, indent)
                buf += '</%s>' % (xmlfield)
                continue
            if isinstance(value, BaseObject):
                buf += value.toXml(level + 1)
                continue
            if isinstance(value, DynamicBaseObj):
                #buf += '<%s>%s</%s>' % (xmlfield, value.toXml(None, level + 1), xmlfield)
                buf = self.indent(buf, indent + INDENT_STR)
                buf += value.toXml(value._name, level + 1)
                continue
            if not isinstance(value, list):
                buf = self.indent(buf, indent + INDENT_STR)
                if isEmpty(value):
                    buf += '<%s />' % (xmlfield)
                else:
                    buf += '<%s>%s</%s>' % (xmlfield, value, xmlfield)
                continue
            # this is a list type
            if len(value) == 0:
                buf = self.indent(buf, indent)
                buf += '<%s />' % (xmlfield)
                continue
            #log_debug('Array: [%s]' % (value))
            for val in value:
                if isinstance(val, BaseObj):
                    #buf += '<%s>%s</%s>' % (xmlfield, val.toXml(), xmlfield)
                    if len(buf) > 0:
                        buf += '\n'
                    buf += val.toXml(None, level + 1)
                elif isinstance(val, BaseObject):
                    #buf += '<%s>%s</%s>' % (xmlfield, val.toXml(), xmlfield)
                    buf += '\n'
                    buf += val.toXml(level + 1)
                elif isinstance(val, DynamicBaseObj):
                    #buf += '<%s>%s</%s>' % (xmlfield, val.toXml(), xmlfield)
                    buf += '\n'
                    buf += val.toXml(None, level + 1)
                else:
                    buf += self.indent(' ', indent)
                    buf += '<%s>%s</%s>' % (xmlfield, val, xmlfield)
                    
        if rootelem is not None:
            #if level > 0:
            #    indent = '.   ' * (level - 1)
            buf = '<%s>\n%s\n%s</%s>' % (rootelem, buf, indent, rootelem)
        return buf

    def indent(self, buf, indent):
        if len(buf) > 0:
            buf = buf + '\n'
        return buf + indent
        
    def __str__(self):
        buf = '{'
        for field in self._fields.keys():
            val = getattr(self, field)
            if isinstance(val, list):
                valbuf = '['
                for v in val:
                    valbuf += ('%s, ' % (v))
                valbuf += ']'
                val = valbuf

            str = '%s: %s' % (field, val)
            buf += str
            buf += "\n"
        buf += '}'
        return buf

try:
  from org.w3c.dom import Node
except ImportError:
  exc_type, exc_value, exc_traceback = sys.exc_info()
  LogWriter.log_error('Exception: type=%s, val=%s, traceback=%s\n%s' % (traceback.format_exception(exc_type, exc_value, exc_traceback)))


class XmlWrapper:

    """ Helper class to parse the xml document """

    def __init__(self, rootelem):
        self.rootelem = rootelem

    @staticmethod
    def is_singleton(elem):
        """  check weather element is singleton
         
        Args:
        element: element needs to check
        Returns:
        True if element is singleton
        False if the element is not singleton  
        
        """
        children = elem.getChildNodes()
        if children.getLength() == 1 and children.item(0).getNodeType() == Node.TEXT_NODE:
            return True
        return False

    @staticmethod
    def parse_element(container, elem, depth):
        """
        Parse the element till the given depth and store in container
        
        Args:
        container: container
        elem: element needs to parsed
        depth: depth till parsed
        Returns:
        None
        
        """
        # log_debug('parse_element: %s%s, %s, %d' % (indent(depth),)
        # elem.getNodeName(), elem.getNodeValue(), elem.getNodeType())

        children = elem.getChildNodes()
        # log_debug('parse_element: children = %s, length = %d' % (children,)
        # children.getLength())

        for i in range(children.getLength()):
            node = children.item(i)
            prefix = '%s%d.%d:' % (indent(depth), depth, i)
            # log_debug('%s: %s, %s, %d' % (prefix, node.getNodeName(),)
            # node.getNodeValue(), node.getNodeType())

            if not node.getNodeType() == Node.ELEMENT_NODE:
                continue

            if XmlWrapper.is_singleton(node):
                # this is a singleton node like.. <xmltoken>value</xmltoken>. We will assign 'value' to container.xmltoken
                # log_debug('parse_element: %s:%s setting %s=%s' % (prefix,)
                # elem.getNodeName(), node.getNodeName(),
                # node.getChildNodes().item(0).getNodeValue())
                container.process_field_value(
                    node.getNodeName(), node.getChildNodes().item(0).getNodeValue())
                continue

            childobj = BaseObj()
            container.process_field_value(node.getNodeName(), childobj)
            # log_debug('parse_element: %s:%s setting obj %s' % (prefix,)
            # elem.getNodeName(), node.getNodeName())
            XmlWrapper.parse_element(childobj, node, depth + 1)

        # log_debug('parse_element: %s:%s [RET] container = %s' % (prefix,)
        # elem.getNodeName(), container)
        return

    def parse(self):
        """
        Parse the BaseoBJ
        
        Args:
        None
        Returns
        XmlObjest parsing all the fields.
        
        """
        obj = BaseObj()
        XmlWrapper.parse_element(obj, self.rootelem, 1)
        xmlobj = BaseObj()
        xmlobj.process_field_value(self.rootelem.getNodeName(), obj)
        return xmlobj

    @staticmethod
    def toXml(obj):
        obj


def indent(depth, ch=' '):
    str = '[d=%d] ' % (depth)
    for i in range(0, depth):
        str += ch * 4
    return str

try:
  from java.util import Collection
except ImportError:
  exc_type, exc_value, exc_traceback = sys.exc_info()
  LogWriter.log_error('Exception: type=%s, val=%s, traceback=%s\n%s' % (traceback.format_exception(exc_type, exc_value, exc_traceback)))

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
    if Collection.isInstance(val):
        return val.isEmpty()
    if isinstance(val, str):
        return val.strip() == ''
    if isinstance(val, unicode):
        return str(val).strip() == ''
       
    return False


def isNotEmpty(val):
    """ Check weather val is not empty 
    
    Args:
    Val : Value need to check
    Returns:
    True: if the value is not empty
    False: if the value is empty
    """
    if isEmpty(val):
        return False
    return True
    
class IPPrefix(object):

    """ IP Prefix utility class
    """
    def __init__(self, prefix):
        self.prefix = prefix
        arr = prefix.split('/')
        if len(arr) > 1:
            self.address = arr[0]
            self.masklen = int(arr[1])
            mask = IPPrefix.get_mask_num(self.masklen)
            self.netmask = IPPrefix.to_ip_address(mask)
            self.wildcard = IPPrefix.to_ip_address(~mask)
            # FIXME: handle ipv6
            if self.masklen == 32:
                self.is_ipaddress = True
            else:
                self.is_ipaddress = False
        else:
            self.address = prefix
            self.netmask = '255.255.255.255'
            self.wildcard = '0.0.0.0'
            self.masklen = 32
            mask = ~0
            self.is_ipaddress = True
        # convert address to number
        addrnum = IPPrefix.ip2int(self.address) & mask
        self.network = IPPrefix.to_ip_address(addrnum)

    @staticmethod
    def from_ip_and_mask(ip, netmask):
        masklen = netmask2masklen(netmask)
        prefix = '%s/%d' % (ip, masklen)
        return IPPrefix(prefix)
        
    def isIpAddress(self):
        """
        check weather object is valid ip address or not
        
        Args : None
        Returns: True if is valid ip address else False
        """
        return self.is_ipaddress

    @staticmethod
    def get_mask_num(masklen):
        return ~((1 << (32 - masklen)) - 1)

    def gateway_ip(self):
        print "self.masklen is:", self.masklen
        if str(self.masklen) == str(32):
            print "self.address is:", self.address
            return self.address
        return self.next_ip(1)

    def next_ip(self, n):
        return IPPrefix.to_ip_address(IPPrefix.ip2int(self.network) + n)
            
    @staticmethod
    def to_ip_address(val):
        """
        converts val to ip address
        
        Args : value
        Returns: Value will be converted to ip address form
        """
        buf = ''
        buf += '%d' % ((val >> 24) & 0xFF)
        buf += '.%d' % ((val >> 16) & 0xFF)
        buf += '.%d' % ((val >> 8) & 0xFF)
        buf += '.%d' % (val & 0xFF)
        return buf

    @staticmethod
    def masklen_to_netmask(masklen):
        """
        Returns Netmask for given masklen
        
        Args:
        masklen: length of the mask
        Returns:
        Netmask corresponding to given mask length 
        
        """
        masklen = int(masklen)
        mask = IPPrefix.get_mask_num(masklen)
        return IPPrefix.to_ip_address(mask)
       
    @staticmethod
    def ip2int(val):
        """ converts ip address to int
        
        Args: 
        val : ip address need to convert
        Returns: integer value corresponding to ip address
        """
        arr = val.split('.')
        number = 0
        i = 0
        for numtok in arr:
            number = number << 8
            number = number | (int(numtok) & 0xFF)

        return number

    @staticmethod
    def get_network_for_ip(ip, netmasklen):
        """ Get network for given ip address
        
        Args:
        ip  : ip address for which network has to be find
        netmasklen : net mask length
        Returns:
        network for the given ip address.
        """
        number = IPPrefix.ip2int(ip)
        mask = IPPrefix.get_mask_num(netmasklen)
        number = number & mask
        return IPPrefix.to_ip_address(number)

    def is_ip_in_subnet(self, ip):
        """ Check weather ip lies in given subnet
        
        Args:
        ip : ip address that has to check
        masklen : value passed when IpPrefix object is created.
        Returns :
        True: if ip lies in given network
        False: if ip does not lies in given network
        
        """
        network = IPPrefix.get_network_for_ip(ip, self.masklen)
        log_debug('network = %s, mynetwork = %s' % (network, self.network))
        return network == self.network

    def is_child_prefix(self, child):
        """ Check whether the 'child' prefix is part of this network or not
        """
        if child.masklen < self.masklen:
            return False
        return self.is_ip_in_subnet(child.network)
        
    def __str__(self):
        return 'prefix=%s, address=%s, netmask=%s' % (self.prefix, self.address, self.netmask)

def next_ip_address(ipaddr):
    """ Calculate next ip address

    Args:
    ipaddr : ip address
    Returns:
    ip address which comes next to given ip address
    """
    addrnum = IPPrefix.ip2int(ipaddr) + 1
    return IPPrefix.to_ip_address(addrnum)

def prev_ip_address(ipaddr):
    """ Calculate next ip address

    Args:
    ipaddr : ip address
    Returns:
    ip address which comes next to given ip address
    """
    addrnum = IPPrefix.ip2int(ipaddr) - 1
    return IPPrefix.to_ip_address(addrnum)

def get_parent_rcpath(rcpath, level=1):
    """
    Get rcpath at given level

    Args:
    rcpath: rcpath
    level: level
    Returns:
    rcpath corresponds to given level.
    """
    i = 0
    while i < level:
        idx = rcpath.rfind('/')
        if idx < 0:
            return None
        rcpath = rcpath[:idx]
        log_debug('rcpath: %s' % (rcpath))
        i = i + 1
    return rcpath

def make_rcpath(toks):
    if not isinstance(toks, list):
        return toks
    return '/'.join(toks)

def get_suffix(str, pattern):
    """
    get suffix of string for the given pattern

    Args:
    Str: String
    pattern: pattern
    Return:
    Suffix of the string for the given pattern
    """
    try :
        idx = str.index(pattern)
        if idx < 0:
            return None
    except:
        return None
    return str[idx + len(pattern) : ]

def raise_exception(msg, default_value):
    if isNotEmpty(msg):
        raise(Exception(msg))
    if isNotEmpty(default_value):
        raise(Exception(default_value))
    raise(Exception('Internal error'))

def make_interfacename(name):
    name = name.replace(':', '%3A')
    name = name.replace(' ', '%20')
    return name.replace('/', '%2F')

def normalize_name(name):
    name = name.replace(':', '%3A')
    name = name.replace(' ', '%20')
    name = name.replace('=', '%3D')
    return name.replace('/', '%2F')

def encode_url(name):
    return YangSchemaNode.encode(name)

def decode_url(name):
    return YangSchemaNode.decode(name)

def netmask2masklen(netmask):
    num = IPPrefix.ip2int(netmask)
    i = 0
    while i < 32:
        mask = (1 << i)
        if (num & mask) != 0:
            return 32 - i
        i = i + 1
    return 32

def get_current_user():
    ctx = ApplicationContextProvider.getApplicationContext()
    taskDbService = ctx.getBean('taskDbService')
    return taskDbService.getCurrentUser().getUsername()

def isAdmin():
    ctx = ApplicationContextProvider.getApplicationContext()
    taskManager = ctx.getBean('taskManager')
    return taskManager.isAdmin()

def convert_to_list(obj):
    if obj is None:
        return None
    if isinstance(obj, list):
        return obj
    else:
        return [obj]

def is_valid_ip(ip_address):
    address_match = re.match(r'^(?:(?:\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])$', \
                             ip_address)
    if address_match:
        return True
    else:
        raise Exception("please provide Valid IP value ")
def is_valid_rd(rd):
    rd_match1 = re.match(r'^(?:(?:\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5]):(:?[0-4][0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-5]|\d{1,9})$', \
                         rd)
    rd_match2 = re.match(r'^(:?[0-4][0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-5]|\d{1,9}):(:?[0-4][0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-5]|\d{1,9})$', rd)

    rd_match3 = re.match(r'auto', rd)

    if rd_match1 or rd_match2 or rd_match3:
        return True
    else:
        raise Exception("please provide Valid rd value ")

def decode_password(password):
    return AnutaEncryptor.decrypt(password)

def wrappedmethod(log_args = True, detailed_log = False):
    def _log_debug(*args):
        log_debug('%s' % ''.join(args))

    def _log_error(*args):
        log_error('ERROR: %s' % ''.join(args))
        
    def summary(ret):
        length = len(ret)
        MAX = 100
        if length > MAX:
            ret = '%s... (%d bytes)' % (ret[0:MAX], length)
        return ret
        
    def format_return(ret, detailed_log):
        if ret == None:
            return ret
        
        ret = str(ret)
        if not detailed_log:
            return summary(ret)
        
        idx = ret.find('\n')
        if idx > 0:
            return '--------------------\n%s\n----------------------' % (ret)
        return ret
        
    def wrap(fn):
        _log_debug('fn = %s' % (fn))
        def get_args(*args):
            arr = []
            for arg in args:
                val = '%s' % (arg)
                idx = val.find('\n')
                if idx >= 0:
                    val = '%s...' % (val[0:idx])
                arr.append(val)
            joined = '\'%s\'' % ('\', \''.join(arr))
            return joined
        
        def get_detailed_args(*args):
            arr = []
            idx = 0
            for arg in args:
                val = '  arg[%d]: \'%s\'' % (idx, arg)
                arr.append(val)
                idx = idx + 1
            return '\n'.join(arr)
        
        def wrapped_fn(*args, **kwargs):
            name = fn.__name__
            if log_args:
                if detailed_log:
                    joined = get_detailed_args(*args)
                else:
                    joined = get_args(*args)
                _log_debug('Entering: %s(%s)' % (name, joined))
            else:
                _log_debug('Entering: %s' % (name))

            try:
                ret = fn(*args, **kwargs)
                retstr = format_return(ret, detailed_log) 
                _log_debug('Exited: %s. Returning %s' % (name, retstr))
            except Exception, e:
                exc_info = sys.exc_info()
                tb = traceback.format_exc()
                _log_error('Exception \'%s\' in: %s. Bailing out. Details:\n------------------\n%s\n-------------------' % (exc_info[1], name, tb))
                raise(e)
            return ret
        return wrapped_fn
    return wrap

def log_debug(*x):
    buf = ''
    for v in x:
        buf = '%s %s' % (buf, v)
    try:
      LogWriter.log_debug(buf)
    except NameError:
      pass

def log_error(x):
    buf = ''
    for v in x:
        buf = '%s %s' % (buf, v)
    try:
      LogWriter.log_error(buf)
    except NameError:
      pass

'''
API to convert json to python object
'''
from collections import namedtuple
import json

def _json_object_hook(d):
  return namedtuple('X', d.keys())(*d.values())

def json2obj(data):
  return json.loads(data, object_hook=_json_object_hook)
class ScriptResultUtil :

    def __init__(self,result):
        self.aggregator = ScriptDeviceResultAggregator()
        self.result = result

    def isFailed(self):
        return self.aggregator.isFailed()

    def setIntermediateOutput(self,deviceId,status,cmds):
        self.aggregator.setOutput(deviceId,status,Arrays.asList(cmds))

    def setErrorMessage(self):
        self.result.setErrorMessage(self.aggregator.buildErrorOutput())

    def setOutput(self):
        self.result.setOutput(self.aggregator.buildOutput())

from com.anuta.service.yang.rpc import RpcRegistrationRequest
class RpcRegistrationRequestBuilder(object):
  def __init__(self, name, processor):
    self.req = RpcRegistrationRequest.newInstance(name, processor)

  def getName(self):
    return self.req.getName()

  def getRpcRequestProcessor(self):
    return self.req.getRpcRequestProcessor()

  def setTaskStatusManaged(self, val):
    self.req.setTaskStatusManaged(val)
    return self

  def isTaskStatusManaged(self):
    return self.req.isTaskStatusManaged()

  def setAsync(self, val):
    self.req.setAsync(val)
    return self

  def isAsync(self):
    return self.req.isAsync()

  def build(self):
    return self.req

