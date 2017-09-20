#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2014-2015 Anuta Networks, Inc. All Rights Reserved.
#
import util
import yang
import devicemgr
import copy
from untangle import untangle_safe_name

class AbstractDeviceMgr(object):
    def device_convert_to_list(self):
      if isinstance(self.dev, list):
        return self.dev
      else:
        self.dev = [self.dev]
        return self.dev

    def make_objname(self, ilist):
      objname = ''
      for obj in ilist:
        objname += obj.replace('-','_').split(':')[-1]+'.'
    
      return objname[:-1]

    def obj_list_search(self, objs, values, keys):
      value_list = values.split(',')
    
      #for key value dict
      key_dict = {}
      for i, key in enumerate(keys):
        key_dict[key] = value_list[i]
    
      #iterate over list objects
      objs = util.convert_to_list(objs)
      for obj in objs:
        non_match = False
        #compare all the keys and values, if same return the object
        for key, value in key_dict.items():
          if value != str(getattr(obj, untangle_safe_name(key))):
            non_match = True
            break
    
        if not non_match:
          return obj
    
    def get_obj_by_url(self, obj, path, key_hints):
      tags = path.split("/")
      key_hint_count = 0
      for tag in tags:
        tag = tag.split(":")[-1]
        ctag = tag.split("=")
        if hasattr(obj, untangle_safe_name(ctag[0])):
          if len(ctag) > 1:
            lobj = getattr(obj, untangle_safe_name(ctag[0]))
            obj = self.obj_list_search(lobj, ctag[-1], key_hints[key_hint_count])
            key_hint_count += 1
            if obj is None:
              return
          else:
            obj = getattr(obj, untangle_safe_name(tag))
        else:
          return
    
      return obj

    def get_list_relative_distance(self, rcpath):
      rcpath_split = rcpath.split('=')
      if len(rcpath_split) == 1:
        return 0
    
      loc = 0
      rcpath_split = rcpath.split('/')
      for i, path in enumerate(rcpath_split):
        if len(path.split('=')) > 1:
          loc = i+1
    
      if loc == i+1:
        return -1

      return loc

    def create_(self, sdata, dev, **kwargs):
      self.rcpath = kwargs.get('rcpath')
      self.sdata = sdata
      self.dev = dev
      self.device_convert_to_list()
      self.payload = kwargs.get('payload')
      self.key_hints = kwargs.get('key_hints')
      self.operation = "CREATE"
      self.create_linkage_nodes(dev, self.key_hints)

      self.dump_(sdata=sdata)
      for dev_iterator in self.dev:
        yang.Sdk.createData(dev_iterator.url+'/'+self.rcpath, self.payload, sdata.getSession(), kwargs.get('addref', True))

      #mapping_dict is key value pair of device node and (service value and service node)
      #The same could be used in future to map back-to-back service to device leaf level with service rcpath

    def create_linkage_nodes(self, dev, key_hints):
      rcpath_split_list = self.rcpath.split('/')

      loc = self.get_list_relative_distance(self.rcpath)
      if loc == -1:
        return

      for iteration, rctoken in enumerate(rcpath_split_list[loc:]):
        #Do a create data for container elements
        for dev_iterator in self.dev:
          url = "/".join(rcpath_split_list[:loc+iteration])
          mobj = self.get_obj_by_url(dev_iterator.device, url, key_hints)
          curl = dev_iterator.url if url == '' else dev_iterator.url+'/'+url
          if not hasattr(mobj, rctoken.replace('-','_').split(':')[-1]):
            yang.Sdk.createData(curl, '<%s/>'%(rctoken.split(':')[-1]), self.sdata.getSession(), False)

    def delete_(self, sdata, dev, rcpath, fail_silently=False, payload=None, remove_reference=False, **kwargs):
      self.rcpath = rcpath
      self.payload = payload
      self.operation = "DELETE"

      self.dump_(sdata=sdata)
      for dev_iterator in dev:
        #remove the reference and delete the entry
        output = yang.Sdk.invokeRpc('ncxsdk:get-inbound-references', '<input><rc-path>%s/%s</rc-path></input>'%(dev_iterator.url, rcpath))
        ref = util.parseXmlString(output)
        if hasattr(ref.output, 'references'):
          if hasattr(ref.output.references, 'reference'):
            if hasattr(ref.output.references.reference, 'src_node'):
              if remove_reference:
                for each_ref in util.convert_to_list(ref.output.references.reference.src_node):
                  yang.Sdk.removeReference(each_ref, dev_iterator.url+'/'+rcpath, sdata.getSession())
              else:
                raise Exception("Cannot delete the entry %s because entry is referred at %s"%(dev_iterator.url+'/'+rcpath, ref.output.references.reference.src_node))
                #yang.sdk.append_taskdetail("Cannot delete the entry %s because entry is referred at %s"%(dev_iterator.url+'/'+rcpath, ref.output.references.reference.src_node))
                continue
            else:
              #check for any self references
              if remove_reference:
                try:
                  yang.Sdk.removeReference(sdata.getRcPath(), dev_iterator.url+'/'+rcpath, sdata.getSession())
                except Exception as e:
                  continue

        yang.Sdk.deleteData(dev_iterator.url+'/'+rcpath, payload, sdata.getTaskId(), sdata.getSession(), fail_silently)

    def update_(self, sdata, dev, **kwargs):
      self.rcpath = kwargs.get('rcpath')
      self.sdata = sdata
      self.dev = dev
      self.device_convert_to_list()
      self.payload = kwargs.get('payload')
      self.key_hints = kwargs.get('key_hints')
      self.operation = "UPDATE"
      self.create_linkage_nodes(dev, self.key_hints)

      self.dump_(sdata=sdata)
      for dev_iterator in self.dev:
        yang.Sdk.patchData(dev_iterator.url+'/'+self.rcpath, self.payload, sdata, kwargs.get('addref', False))

      #mapping_dict is key value pair of device node and (service value and service node)
      #The same could be used in future to map back-to-back service to device leaf level with service rcpath

    def dump_(self, sdata=None, *keys, **kwargs):
      util.log_debug("operation %s"%self.operation)
      util.log_debug("rcpath %s"%self.rcpath)
      util.log_debug("payload %s"%self.payload)
      #util.log_debug("keys %s"%self.keys)
      #util.log_debug("operation %s"%self.kwargs)

    def commit_(self, sdata=None, operation = "CREATE", dev=None, addref=True, autocommit=True, *keys, **kwargs):
      util.log_debug(self.rcpath)
      util.log_debug(self.payload)
      util.log_debug(self.operation)
      util.log_debug("commit")
