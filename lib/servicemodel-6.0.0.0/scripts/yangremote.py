#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2014-2015 Anuta Networks, Inc. All Rights Reserved.

import remote

class YangRemote:
    _instance = None
    def __init__(self):
        self.restconf = self
        self.yangServiceProcessor = self
        
    def getData(self, url, payload, taskId, context=None, arg=False):
        print 'url: [%s]' % (url)
        if url == None:
            return None
        obj = {'requestType' : 'getData', 'url' : url, 'taskId' : taskId}
        print 'getData:'
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        print '-----------------\respobj: %s' % (resp_obj)
        #resp_payload = respobj['payload']
        #print '-----------------\nPAYLOAD: [%s]' % (resp_payload)
        return resp_obj['payload']
    
    def createData(self, url, payload, yang_session, addRef=True, failOnExistingData=False):
        obj = {'requestType' : 'createData', 'url' : url, 'payload' : payload, 'taskId' : yang_session.getTaskId(), 'params' : {'addReference' : addRef, 'failOnExistingData' : failOnExistingData}}
        print 'createData:'
        remote.Session.instance().send_and_get_response(obj)

    def deleteData(self, url, payload, taskId, session):
        obj = {'requestType' : 'deleteData', 'url' : url, 'payload' : payload, 'taskId' : taskId}
        print 'createData:'
        return remote.Session.instance().send_and_get_response(obj)

    def getRcPathListForXPathAndValue(self, xpath, value, level=1, taskId=None):
        obj = {'requestType' : 'getRcPathListForXPathAndValue', 'url' : xpath, 'payload' : value, 'taskId' : taskId, 'params' : {'level' : level}}
        print 'createData:'
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        print '-----------------\respobj: %s' % (resp_obj)
        return resp_obj['resultList']

    def getRcPathListForXPath(self, xpath, level=1, taskId=None):
        obj = {'requestType' : 'getRcPathListForXPathAndValue', 'url' : xpath, 'payload' : '', 'taskId' : taskId, 'params' : {'level' : level}}
        print 'createData:'
        resp_obj = remote.Session.instance().send_and_get_response(obj)
        print '-----------------\respobj: %s' % (resp_obj)
        return resp_obj['resultList']
    
    def registerYangServiceHandler(self, name, handler, globalMap=True):
        remote.Session.instance().register_yang_handler(name, handler, globalMap)
        
    def unregisterYangServiceHandler(self, name, globalMap=True):
        remote.Session.instance().unregister_yang_handler(name, globalMap)
        
    def registerFeatureHandler(self, name, handler):
        remote.Session.instance().register_feature_handler(name, handler)
        
    def unregisterFeatureHandler(self, name):
        remote.Session.instance().unregister_feature_handler(name)
    
    @staticmethod
    def getInstance():
        if YangRemote._instance == None:
            YangRemote._instance = YangRemote()
        return YangRemote._instance
