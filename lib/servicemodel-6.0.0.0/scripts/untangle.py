#!/usr/bin/env python

"""
 untangle

 Converts xml to python objects.

 The only method you need to call is parse()
"""
import os
import sys
import keyword
from xml.sax import make_parser, handler
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
try:
    from types import StringTypes
    is_string = lambda x: isinstance(x, StringTypes)
except ImportError:
    is_string = lambda x: isinstance(x, str)

__version__ = '1.1.0'

def untangle_safe_name(name):
  name = name.replace('-', '_')
  name = name.replace('.', '_')
  name = name.replace(':', '_')
  if keyword.iskeyword(name):
    name += '_'
  return name

def trim_xpath(xpath):
  xpathlist = xpath.split('/')
  xpathlist_trimmed = []
  lmname = xpathlist[0].split(':')[0]
  xpathlist_trimmed.append(xpathlist[0])
  for xp in xpathlist[1:]:
    if xp.split(':')[0] == lmname:
      xpathlist_trimmed.append(xp.split(':')[-1])
    else:
      if len(xp.split(':')) > 1:
        lmname = xp.split(':')[0]
      xpathlist_trimmed.append(xp)
  xpath_new = "/".join(xpathlist_trimmed)
  return xpath_new

def remove_prefix(xpath):
  xpathlist = xpath.split('/')
  xpathlist_trimmed = []
  for xp in xpathlist:
    xpathlist_trimmed.append(xp.split(':')[-1])
  xpath_new = "/".join(xpathlist_trimmed)
  return xpath_new

def dummy_contained_xpath(xpath=None):
  return True

class Element(object):
    """
    Representation of an XML element.
    """
    def __init__(self, name, xmlname, attributes):
        self._name = name
        self._xmlname = xmlname
        self._attributes = attributes
        if self._attributes is None:
          self._attributes = {}
        self.children = []
        self.is_root = False
        self.cdata = ''

    def add_child(self, element):
        """
        Store child elements.
        """
        self.children.append(element)

    def add_cdata(self, cdata):
        """
        Store cdata
        """
        self.cdata = self.cdata + cdata

    def get_field_value(self, name):
        for child in self.children:
          if child._name == name:
            if child.cdata == '':
              return None
            else:
              return child.cdata
        return None

    def get_attribute(self, key):
        """
        Get attributes by key
        """
        return self._attributes.get(key)

    def get_attributes(self):
        """
        Get attributes by key
        """
        return self._attributes

    def get_attributes_repr(self):
        """
        Get attributes string
        """
        attr = ''
        if self._attributes is not None or len(self._attributes) != 0:
          for key, val in self._attributes.items():
            attr += "{0}=\"{1}\" ".format(key, val)

        return attr

    def get_elements(self, name=None):
        """
        Find a child element by name
        """
        if name:
            return [e for e in self.children if e._name == name]
        else:
            return self.children

    def toXml(self, rootelem=None, spaces=2):
        """
        Convert BaseObj to xml

        Args:
        None
        Returns
        xml structure equivalent to BaseObj
        """
        buf = ''
        attrstr = self.get_attributes_repr()
        if attrstr != '':
          attrstr = " "+attrstr
        if len(self.children) == 0:
          if self.cdata == '':
            buf += " "*spaces+"<{0}{1}/>\n".format(self._xmlname, attrstr)
          else:
            buf += " "*spaces+"<{0}{2}>{1}</{0}>\n".format(self._xmlname, self.cdata, attrstr)
        else:
          for child in self.children:
            buf += child.toXml(spaces=spaces+2)
          buf = " "*spaces+"<{0}{2}>\n{1}".format(self._xmlname, buf, attrstr)
          buf += " "*spaces+"</{0}>\n".format(self._xmlname, buf, attrstr)

        if rootelem is not None:
            buf = '<%s>%s</%s>' % (rootelem, buf, rootelem)
        return buf

    def toNcxDeviceDict(self, curr_dict, parent_xpath="/controller:devices/device", contained_xpaths_callback=dummy_contained_xpath, modulename=None):
        """
        Convert BaseObj to NCX understandable json

        Args:
        None
        Returns
        xml structure equivalent to BaseObj
        """
        if len(self._xmlname.split(':')) == 1:
          xpath = '%s/%s:%s'%(parent_xpath, modulename, self._xmlname)
        else:
          xpath = '%s/%s'%(parent_xpath, self._xmlname)
        valid_fields = contained_xpaths_callback(xpath=remove_prefix(xpath))
        if valid_fields is not None:
          if valid_fields.get('_xpath') is not None:
            xpath = valid_fields['_xpath']
          elif valid_fields.get('_module_name') is not None:
            xpath = '%s/%s:%s'%(parent_xpath, valid_fields.get('_module_name'), self._xmlname)

          curr_dict['xpath'] = trim_xpath(xpath)
          curr_dict['fields'] = {}
          fields =  curr_dict['fields']
          curr_dict['children'] = {}
          children =  curr_dict['children']

          #attributes are also considered as candidates for leafs
          for key, value in self._attributes.items():
            if contained_xpaths_callback(xpath=remove_prefix(xpath+'/'+key)) is not None:
              if len(valid_fields) != 0:
                if key not in valid_fields:
                  continue
              if value == '':
                fields[key] = [""]
              else:
                if key in fields:
                  fields[key].append(value)
                else:
                  fields[key] = [value]

          for child in self.children:
            if len(child.children) == 0 and not contained_xpaths_callback(xpath=remove_prefix(xpath+'/'+child._xmlname)):
              if len(valid_fields) != 0:
                if child._xmlname not in valid_fields:
                  continue
              if child.cdata == '':
                fields[child._xmlname] = [""]
              else:
                if child._xmlname in fields:
                  fields[child._xmlname].append(child.cdata)
                else:
                  fields[child._xmlname] = [child.cdata]
            else:
              if contained_xpaths_callback(xpath=remove_prefix(xpath+'/'+child._xmlname)) is not None:
                recur_dict = {}
                if children.get(child._xmlname) is not None:
                  children[child._xmlname].append(recur_dict)
                else:
                  children[child._xmlname] = [recur_dict]

                child.toNcxDeviceDict(recur_dict, parent_xpath=curr_dict['xpath'], contained_xpaths_callback=contained_xpaths_callback, modulename=modulename)

        return

    def __getitem__(self, key):
        return self.get_attribute(key)

    def __getattr__(self, key):
        matching_children = [x for x in self.children if x._name == key]
        if matching_children:
            if len(matching_children) == 1:
                self.__dict__[key] = matching_children[0]
                return matching_children[0]
            else:
                self.__dict__[key] = matching_children
                return matching_children
        else:
            raise AttributeError(
                "'%s' has no attribute '%s'" % (self._name, key)
            )

    def __hasattribute__(self, name):
        if name in self.__dict__:
            return True
        return any(self.children, lambda x: x._name == name)

    def __iter__(self):
        yield self

    def __str__(self):
        return self.cdata

    def __repr__(self):
        if self.cdata != '':
          return self.cdata
        else:
          return (
              "Element(name = %s, attributes = %s, cdata = %s)" %
              (self._name, self._attributes, self.cdata)
          )

    def __nonzero__(self):
        return self.is_root or self._name is not None

    def __eq__(self, val):
        return self.cdata == val

    def __dir__(self):
        children_names = [x._name for x in self.children]
        return children_names

    def __len__(self):
        return len(self.children)


class Handler(handler.ContentHandler):
    """
    SAX handler which creates the Python object structure out of ``Element``s
    """
    def __init__(self):
        self.root = Element(None, None, None)
        self.root.is_root = True
        self.elements = []

    def startElement(self, name, attributes):
        xmlname = name
        name = untangle_safe_name(name)
        attrs = dict()
        for k, v in attributes.items():
            attrs[k] = v
        element = Element(name, xmlname, attrs)
        if len(self.elements) > 0:
            self.elements[-1].add_child(element)
        else:
            self.root.add_child(element)
        self.elements.append(element)

    def endElement(self, name):
        self.elements.pop()

    def characters(self, cdata):
        self.elements[-1].add_cdata(cdata)


def parse(filename):
    """
    Interprets the given string as a filename, URL or XML data string,
    parses it and returns a Python object which represents the given
    document.

    Raises ``ValueError`` if the argument is None / empty string.

    Raises ``xml.sax.SAXParseException`` if something goes wrong
    during parsing.
    """
    if (filename is None or (is_string(filename) and filename.strip()) == ''):
        raise ValueError('parse() takes a filename, URL or XML string')
    parser = make_parser()
    sax_handler = Handler()
    parser.setContentHandler(sax_handler)
    if is_string(filename) and (os.path.exists(filename) or is_url(filename)):
        parser.parse(filename)
    else:
        if hasattr(filename, 'read'):
            parser.parse(filename)
        else:
            parser.parse(StringIO(filename))

    return sax_handler.root


def is_url(string):
    """
    Checks if the given string starts with 'http(s)'.
    """
    try:
        return string.startswith('http://') or string.startswith('https://')
    except AttributeError:
        return False


#Test parse function with a xml file
if __name__ == "__main__":
  assert (sys.argv[1] is not None)
  config = parse(sys.argv[1])

  userlist = []
  if hasattr(config.data, 'configuration'):
    if isinstance(config.data.configuration.system.login.user, list):
      for user in config.data.configuration.system.login.user:
        userlist.append(user.name)
        print user.get_field_value('name1')

  print(userlist)
  print(config.data.toXml())
