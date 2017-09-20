#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2014-2015 Anuta Networks, Inc. All Rights Reserved.

import time
import os
import sys
import traceback

import ncx

from java.lang import Object
from com.fasterxml.jackson.databind import ObjectMapper

from threading import Thread, InterruptedException

class AsyncThread(Thread):
    def __init__(self, session):
        Thread.__init__(self)
        self.session = session
        self.queue = []
        self._shutdown = False

    def add_job(self, job, *args):
        arr = [job]
        for arg in args:
            arr.append(arg)
        self.queue.append(arr)

    def shutdown(self):
        self._shutdown = True
        self.add_job(None)

    def run(self):
        while not self._shutdown:
            if len(self.queue) == 0:
                #print 'queue is empty'
                time.sleep(1)
                continue
            if self._shutdown:
                print 'shutting down'
                break
            job = self.queue.pop(0)
            func = job.pop(0)
            if len(job) == 0:
                print 'Calling %s' % (func)
                func()
            else:
                print 'Calling %s(%s)' % (func, job)
                func(*job)
        print 'AsyncThread: Exiting'

#obj = {'url' : '/controller:devices/device', 'payload' : ''}
#json = ObjectMapper().writeValueAsString(obj)
#print json
#from java.lang import Object
#obj = ObjectMapper().readValue(json, Object)

class YangServiceData:
    def __init__(self, sdata, params):
        self.sdata = sdata
        self.rcPath = sdata['rcPath']
        self.path = sdata['path']
        self.xpath = sdata['xpath']
        self.payload = sdata['payload']
        self.depth = sdata['depth']
        self.taskId = sdata['taskId']
        self.serviceRcPath = sdata['serviceRcPath']
        self.serviceXPath = sdata['serviceXPath']
        self.session = YangServiceData.Session(self.taskId)
        if params == None:
            params = {}
        self.session.params = params

    class Session:
        def __init__(self, taskId):
            self.taskId = taskId
            
        def getTaskId(self):
            return self.taskId

        def getParam(self, name):
            if name in self.params:
                return self.params[name]
            return None

        def getParams(self):
            return self.params
    
    def getRcPath(self):
        return self.rcPath

    def getXPath(self):
        return self.xpath

    def getPayload(self):
        return self.payload

    def getDepth(self):
        return self.depth

    def getTaskId(self):
        return self.taskId

    def getServiceRcPath(self):
        return self.serviceRcPath

    def getServiceXPath(self):
        return self.serviceXPath

    def getSession(self):
        return self.session

    def __str__(self):
        return '%s' % (self.sdata)

def handler_executor(handler, session, sessionId, id, sdata):
    session.sessionId = sessionId
    try:
        handler(id, sdata)
        session.send_complete(sessionId)
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = traceback.format_exc()
        sys.stderr.write( '%s:%s' % (exc_type, exc_value))
        sys.stderr.write( '%s' % (tb))
        session.send_exception_msg(exc_type, exc_value, sessionId, tb)
    finally:
        session.sessionId = None
        
    
class Session:
    _instance = None
    def __init__(self, wsclient):
        self.wsclient = wsclient
        self.queue = []
        self.prefix_map = {}
        self.async_thread = AsyncThread(self)
        self._registered = True
        self._handlers_queue = []

        print 'websocket = %s' % (wsclient)

    def start(self, module_name):
        self.async_thread.start()
        self.register(module_name)
        for arr in self._handlers_queue:
            self._register_yang_handler(arr[0], arr[1], [arr2])
        Session._instance = self

    def data_handler(self, buff):
        print "got %s"% buff
        obj = ObjectMapper().readValue(str(buff), Object)
        self.dispatch_request(obj)

    def register(self, module_name):
        req = {'requestType' : 'register', 'params' : {'module-name' : module_name}};
        json = ObjectMapper().writeValueAsString(req)
        self.write_to_socket(json)

    #self.async_thread.add_job(self.getData, '/controller:modelmaps/map=1515')

    def register_yang_handler(self, prefix, handler, globalMap):
        if not prefix.startswith('/'):
            prefix = '/controller:services/%s' % (prefix)
        if not self._registered:
            self._handlers_queue.append([prefix, handler, globalMap])
            return
        self._register_yang_handler(prefix, handler, globalMap)
        
    def _register_yang_handler(self, prefix, handler, globalMap):
        self.prefix_map[prefix] = handler
        req = {'requestType' : 'registerServiceHandler', 'url' : prefix, 'params' : {'globalMap' : globalMap} };
        json = ObjectMapper().writeValueAsString(req)
        self.write_to_socket(json)
        
    def unregister_yang_handler(self, prefix, globalMap):
        #delete self.prefix_map[prefix]
        req = {'requestType' : 'unregisterServiceHandler', 'url' : prefix, 'params' : {'globalMap' : globalMap} };
        json = ObjectMapper().writeValueAsString(req)
        self.write_to_socket(json)

    def add_reference(self, dest_rcpath, session):
        req = {'requestType' : 'addReference', 'url' : dest_rcpath}
        json = ObjectMapper().writeValueAsString(req)
        self.write_to_socket(json)

    def remove_reference(self, src_rcpath, dest_rcpath):
        req = {'requestType' : 'deleteReference', 'url' : src_rcpath, 'payload' : dest_rcpath}
        json = ObjectMapper().writeValueAsString(req)
        self.write_to_socket(json)

    def dispatch_request(self, obj):
        reqType = obj['requestType']
        if reqType == None:
            return
        syncRequest = obj['syncRequest']

        if reqType == 'operation:create':
            payload = obj['payload']
            sessionId = obj['sessionId']
            sdata = ObjectMapper().readValue(payload, Object)
            sdata = YangServiceData(sdata, obj['params'])
            print 'sdata: %s' % (sdata)
            handler = self.prefix_map[sdata.getXPath()]
            print 'handler = %s' % (handler)
            try:
                if handler != None:
                    self.async_thread.add_job(handler_executor, handler.create, self, sessionId, 'id', sdata)
            except:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                tb = traceback.format_exc()
                self.send_exception_msg(exc_type, exc_value, sessionId, tb)
        elif reqType == 'operation:delete':
            payload = obj['payload']
            sessionId = obj['sessionId']
            sdata = ObjectMapper().readValue(payload, Object)
            sdata = YangServiceData(sdata, obj['params'])
            print 'sdata: %s' % (sdata)
            handler = self.prefix_map[sdata.getXPath()]
            print 'handler = %s' % (handler)
            try:
                if handler != None:
                    self.async_thread.add_job(handler_executor, handler.delete, self, sessionId, 'id', sdata)
            except:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                tb = traceback.format_exc()
                self.send_exception_msg(exc_type, exc_value, sessionId, tb)
        elif syncRequest == 'True' or syncRequest:
            self.queue.append(obj)
        else:
            print 'Dropping message: %s' % (obj)

    def send_exception_msg(self, exc_type, exc_value, sessionId, tb):
        msg = '%s: %s' % (exc_type, exc_value)
        tb = traceback.format_exc()
        obj = {'requestType' : 'exception', 'payload' : msg, 'sessionId' : sessionId, 'params' : {'stacktrace' : '%s' % (tb)}}
        json = ObjectMapper().writeValueAsString(obj)
        self.write_to_socket(json, True)

    def send_complete(self, sessionId):
        obj = {'requestType' : 'completion', 'payload' : 'completed successfully', 'sessionId' : sessionId}
        json = ObjectMapper().writeValueAsString(obj)
        self.write_to_socket(json)

    def write_to_socket(self, json, error_msg = False):
        if error_msg:
            sys.stderr.write( '-------------socket---------------------------')
            sys.stderr.write( json)
            sys.stderr.write( '-------------socket---------------------------')
        else:
            print '-------------socket---------------------------'
            print json
            print '-------------socket---------------------------'
        self.wsclient.writeTextFrame(json)
        
    def send_and_get_response(self, obj):
        obj['syncRequest'] = True
        obj['sessionId'] = str(self.sessionId)
        print 'obj: %s' % (obj)
        json = ObjectMapper().writeValueAsString(obj)
        self.write_to_socket(json)
        while len(self.queue) == 0 or self.queue[-1]['sessionId'] != self.sessionId:
            time.sleep(1)
        return self.queue.pop(-1)

    def close(self):
        self.async_thread.shutdown()
        
    @staticmethod
    def instance():
        return Session._instance

    @staticmethod
    def init(wsclient):
        Session._instance = Session(wsclient)

def register_module(module):
    import yang
    import ipam
    yang.Sdk._use_remote = True
    ipam.Infoblox._use_remote = True
    mod = __import__('%s.plugin' % (module))
    Session.setModuleName(module)
    plugin_info = mod.plugin.get_plugin_info()
    plugin_info.init()
