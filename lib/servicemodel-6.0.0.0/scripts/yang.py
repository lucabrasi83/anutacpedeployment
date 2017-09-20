#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2014-2015 Anuta Networks, Inc. All Rights Reserved.

from servicemodel import util
from com.anuta.api import DataNodeNotFoundException
from com.anuta.api import DataNodeReferenceType

import sys
import ncx
import re
try:
  from com.anuta.model.base import YangSessionThreadLocal
except ImportError:
  pass
try:
  from com.anuta.api.yang import RestconfOperationType
except ImportError:
  exc_type, exc_value, exc_traceback = sys.exc_info()
  util.log_error('Exception: type=%s, val=%s, traceback=%s\n%s' % (traceback.format_exception(exc_type, exc_value, exc_traceback)))
                      
try:
  from com.anuta.api.dto import RPCOperationResult
except ImportError:
  exc_type, exc_value, exc_traceback = sys.exc_info()
  util.log_error('Exception: type=%s, val=%s, traceback=%s\n%s' % (traceback.format_exception(exc_type, exc_value, exc_traceback)))
  
try:
  from com.anuta.yang.saxon import YangXPathResolver
except ImportError:
  pass

class Sdk:

    """ The base SDK class that wraps the service model APIs

    Provides wrappers for the utilities like query, add, delete APIs
    """
    _instance = None

    def __init__(self):
        if ncx.Config.is_remote():
            util.log_debug('Using remote api')
            pass
        try:
          from com.anuta.util import ApplicationContextProvider
          ctx = ApplicationContextProvider.getApplicationContext()
          self.ctx = ctx
          from com.anuta.api import RestconfService
          from com.anuta.api.provider import NetworkResourceMgmtService
          self.restconf = ctx.getBean(RestconfService)
          from com.anuta.service.yang import YangServiceProcessor
          self.yangServiceProcessor = ctx.getBean(YangServiceProcessor)
          self.networkResourceMgmtService = ctx.getBean(NetworkResourceMgmtService)
          from com.anuta.api import RestStyleYangService
          self.restStyleYangService = ctx.getBean(RestStyleYangService)
          from com.anuta.service import TaskManager
          self.taskmgr = ctx.getBean(TaskManager)
          self.ctx = ctx
	  from com.anuta.yang.rpc.datamodel import DataModelOperationService
          self.datamodel_svc = ctx.getBean(DataModelOperationService)
	  from com.anuta.network.comps.devicemgr import DeviceOperationAuditService
          self.device_operation_audit_service = ctx.getBean(DeviceOperationAuditService)
          from com.anuta.driver.service import DeviceDriverFactory
          self.deviceDriverFactory = ctx.getBean(DeviceDriverFactory)
          from com.anuta.model.server import TransactionHelper
          self.transactionHelper = ctx.getBean(TransactionHelper)
        except ImportError:
          exc_type, exc_value, exc_traceback = sys.exc_info()
          util.log_error('Exception: type=%s, val=%s, traceback=%s\n%s' % (traceback.format_exception(exc_type, exc_value, exc_traceback)))

    @staticmethod
    def resolveNamingTemplate(sdata, templateName, defaultName = None):
        util.log_debug('sdata.rcpath = %s, templateName = %s, defaultName = %s' % (sdata.getRcPath(), templateName, defaultName))
        template_svc = Sdk.getInstance().deviceDriverFactory.getNamingTemplateService()
        if template_svc == None:
            raise Exception('Naming template service is not available')
        resolved = template_svc.resolveNamingTemplate(sdata, templateName)
        if util.isEmpty(resolved):
            util.log_debug('Resolved value is empty')
        if util.isNotEmpty(defaultName):
            util.log_debug('Returning default name: %s' % (defaultName))
            return defaultName
        return resolved
    
    @staticmethod
    @util.wrappedmethod()
    def getInterfacesListForDevice(ipaddress):
        util.log_debug('Rxvd IpAddress = %s' % (ipaddress))
        deviceInfsList = svc = Sdk.getInstance().networkResourceMgmtService.fetchDeviceInterfaceByDeviceId(ipaddress)
        util.log_debug('DeviceInfsList = %s' % (deviceInfsList))
        return deviceInfsList


    @staticmethod
    def getBean(val):
        return Sdk.getInstance().ctx.getBean(val)    

    @staticmethod
    def getInstance():
        if(Sdk._instance == None):
            if ncx.Config.is_remote():
                import yangremote
                Sdk._instance = yangremote.YangRemote.getInstance()
            else:
                Sdk._instance = Sdk()
        return Sdk._instance

    @staticmethod
    def append_taskdetail(taskid, detail):
        Sdk.getInstance().taskmgr.appendTaskDetails(taskid, detail)
        
    @staticmethod
    @util.wrappedmethod()        
    def getXpath(rcpath):
        """
        Returns xpath for a given rcpath
        """
        exp = r'=.+?(?=\/)'
        return re.sub(exp,'',rcpath).split('=')[0]

    @staticmethod
    @util.wrappedmethod()
    def getRcPathListForXPathAndValue(xpath, value, level=1, taskId=None):
        """ Get a list of rcpaths for a given xpath and value
        The value need not be unique
        Args:
        xpath: xpath of the data node
        value: value of the data node
        level: number of levels up in the tree (Default 1)
        taskId: task Id 
        
        Returns a list of rcpaths
        """
        return Sdk.getInstance().restconf.getRcPathListForXPathAndValue(xpath, value, level, taskId)

    @staticmethod
    @util.wrappedmethod()
    def getRcPathListForXPath(xpath, level=1, taskId=None):
        """ Get a list of rcpaths for a given xpath 
        Args:
        xpath: xpath of the data node
        level: number of levels up in the tree (Default 1)
        taskId: Task Id
        
        Returns a list of rcpaths
        """
        return Sdk.getInstance().restconf.getRcPathListForXPath(xpath, level, taskId)


    @staticmethod
    @util.wrappedmethod()
    def createData(url, payload, yang_session, addReference=True, failOnExistingData=False):
        if payload == "" or payload is None:
            util.log_debug('payload is empty or none')
            return
        YangSessionThreadLocal.setDeviceAuditDisabled(True)
        try:
            Sdk.createDataWithTaskId(url, payload, yang_session, yang_session.getTaskId(), addReference, failOnExistingData)
        finally:
            YangSessionThreadLocal.setDeviceAuditDisabled(False)


    @staticmethod
    @util.wrappedmethod()
    def createDataWithTaskId(url, payload, yang_session, taskId, addReference=True, failOnExistingData=False):
        if payload == "" or payload is None:
            util.log_debug('payload is empty or none')
            return
        """ Create an xml payload under a give rcpath
        Args:
        url: the rcpath under which the subtree represented by the payload is to be created
        payload: xml payload
        yang_session: yang session
        addReference: flag indicating if the service model layer should create the reference (true by default)
        """
        util.log_debug('yang.createData: session = %s, addReference=%s\nurl = [%s] ' % (yang_session, addReference, url))
        util.log_debug('yang.createData: payload = \n-------------------\n%s\n-------------------------\n' % (payload))

        if ncx.Config.is_remote():
            Sdk.getInstance().restconf.createData(
                url, payload, yang_session, addReference, failOnExistingData)
            return

        if not failOnExistingData:
            oldval = YangSessionThreadLocal.shouldFailOnExisitngData()
            YangSessionThreadLocal.setShouldFailOnExisitngData(False)
        # FIXME: remove this in 5.7
        origTaskId = YangSessionThreadLocal.getTaskId()
        try:
            Sdk.getInstance().restconf.createData(
                url, payload, taskId, yang_session, addReference, None)
            YangSessionThreadLocal.setTaskId(yang_session.getTaskId())
        finally:
            YangSessionThreadLocal.setTaskId(origTaskId)
            if not failOnExistingData:
                YangSessionThreadLocal.setShouldFailOnExisitngData(oldval)

    @staticmethod
    # @util.wrappedmethod(detailed_log=True)
    def invokeRpc(rpcname, payload, log = True):
        if log:
            util.log_debug('rpcname = %s, payload = %s' % (rpcname, payload))
        # FIXME: remove this in 5.7
        origTaskId = YangSessionThreadLocal.getTaskId()
        try:
            ret = Sdk.getInstance().restconf.invokeRpc(rpcname, payload)
        finally:
            YangSessionThreadLocal.setTaskId(origTaskId)
        return ret

    @staticmethod
    @util.wrappedmethod()
    def dataExists(rcpath):
        payload = '<input><rcpath>%s</rcpath></input>' % (rcpath)
        xml = Sdk.invokeRpc('controller:check-entity-exists', payload)
        if util.isEmpty(xml):
            return False
        obj = util.parseXmlString(xml)
        try:
            if obj.output.exist == 'true':
                return True
        except:
            util.log_error('Unable to determine output from %s' % (xml))
        return False
    
    @staticmethod
    @util.wrappedmethod(detailed_log=True)
    def getData(url, payload, taskId, context=None):
        """ Get the data for a given rcpath 
        Args:
        url: the rcpath under which the subtree represented by the payload is to be created
        payload: xml payload
        taskId: task Id
        context: yang data node context 
        
        Returns a String containing the data
        """
        util.log_debug('getData: %s' % (url))
        try:
          orig = YangSessionThreadLocal.childCountNeeded()
          # FIXME: remove this in 5.7
          origTaskId = YangSessionThreadLocal.getTaskId()
          try:
                YangSessionThreadLocal.setChildCountNeeded(False)
                return Sdk.getInstance().restconf.getData(url, payload, taskId, context, False)
          finally:
                YangSessionThreadLocal.setChildCountNeeded(orig)
                YangSessionThreadLocal.setTaskId(origTaskId)
        except ImportError:
          pass
    @staticmethod
    @util.wrappedmethod()
    def deleteData(url, payload, taskId, session, fail_silently=False):
        """ Delete the data corresponding to a given rcpath 
        Args:
        url: the rcpath under which the subtree represented by the payload is to be deleted
        payload: xml payload
        taskId: task Id
        fail_silently: Fails silently in case the url does not exist
        """
        util.log_debug('deleteData: taskId = %s, url = %s, session = %s' % (taskId, url, session))
        # checking if the url exists
        if fail_silently == True:
            xpath = Sdk.getXpath(url)
            idx = url.find('controller:')
            if idx == -1:
                raise Exception("Invalid rcpath provided")
            if not str("%s%s" % ('/', url[idx:])) in Sdk.getRcPathListForXPath(xpath, level=0, taskId=None):
                util.log_debug("rcpath: %s not found" % url)
                return
                # FIXME: remove this in 5.7
        origTaskId = YangSessionThreadLocal.getTaskId()
        try:
            Sdk.getInstance().restconf.deleteData(url, payload, taskId, True, session, False)
        finally:
            YangSessionThreadLocal.setTaskId(origTaskId)

    @staticmethod
    @util.wrappedmethod(detailed_log=True)
    def patchData(url, payload, sdata, add_reference = False):
        YangSessionThreadLocal.setRestconfOperation(RestconfOperationType.PATCH)
        orig = YangSessionThreadLocal.getRestconfOperation()
        # FIXME: remove this in 5.7
        origTaskId = YangSessionThreadLocal.getTaskId()
        try:
            util.log_debug('restconf_patch: url = %s. payload:\n%s' % (url, payload))
            return Sdk.getInstance().restconf.handleRestconfPUT(url, payload, sdata.getTaskId(), sdata.getSession(), False, None)
        finally:
            YangSessionThreadLocal.setTaskId(origTaskId)
            YangSessionThreadLocal.setRestconfOperation(orig)

    @staticmethod
    @util.wrappedmethod(detailed_log=True)        
    def putData(url, payload, sdata, add_reference = False):
        YangSessionThreadLocal.setRestconfOperation(RestconfOperationType.PUT)
        orig = YangSessionThreadLocal.getRestconfOperation()
        # FIXME: remove this in 5.7
        origTaskId = YangSessionThreadLocal.getTaskId()
        try:
            util.log_debug('restconf_patch: url = %s. payload:\n%s' % (url, payload))
            return Sdk.getInstance().restconf.handleRestconfPUT(url, payload, sdata.getTaskId(), sdata.getSession(), False, None)
        finally:
            YangSessionThreadLocal.setTaskId(origTaskId)
            YangSessionThreadLocal.setRestconfOperation(orig)

    #
    # refType = OWNED, REFERRED, TRANSPARENT
    #
    @staticmethod
    @util.wrappedmethod()
    def addReference(dest_rcpath, session, refType = 'OWNED'):
        """ Add reference to a given rcpath
        Args:
        dest_rcpath: rcpath to the destination data node
        """
        util.log_debug('Adding reference to %s, refType = %s' % (dest_rcpath, refType))
        Sdk.getInstance().restconf.addReference(dest_rcpath, session, DataNodeReferenceType.valueOf(refType))

    @staticmethod
    @util.wrappedmethod()
    def removeReference(service_rcpath, dest_rcpath, session=None):
        """ Remove reference to a given rcpath
        Args:
        service_rcpath: 
        dest_rcpath: rcpath to the destination data node
        """
        util.log_debug('Remove reference %s ==> %s' % (service_rcpath, dest_rcpath))
        if session is not None:
            Sdk.getInstance().restconf.removeReference(service_rcpath, dest_rcpath, session)
        else:
            Sdk.getInstance().restconf.removeReference(service_rcpath, dest_rcpath)

    @staticmethod
    @util.wrappedmethod()
    def beginTask():
        rpc = RPCOperationResult()
        svc = Sdk.getBean('restStyleYangService')

        def func():
            svc.beginTask(rpc)
            return
        
        obj = TransactionObj(func)
        th = Sdk.getBean('transactionHelper')
        th.executeInsideNestedTransaction(obj)
        util.log_debug('rpc = %s' % (rpc.getTaskId()))
        return rpc
    
    @staticmethod
    def getEventLogsByDeviceId(deviceId):
        return Sdk.getInstance().device_operation_audit_service.getEventLogsByDeviceId(deviceId)

    @staticmethod
    def getEventLogsByDeviceAndEventType(deviceId, evtType):
        try:
          from com.anuta.network.comps.devicemgr import DeviceOperationEventType
        except ImportError:
          pass
        evt = DeviceOperationEventType.valueOf(evtType)
        util.log_debug('%s = %s' % (evtType, evt))
        return Sdk.getInstance().device_operation_audit_service.getEventLogsByDeviceAndEventType(deviceId, evt)

    @staticmethod
    def restconfGet(rcPath, payload):
        util.log_debug('restconfGet: rcPath = %s, payload = %s', rcPath, payload)
        rpc = Sdk.beginTask()
        return Sdk.getData(rcPath, payload, rpc.getTaskId(), None)

    @staticmethod
    def restconfBeginTask(payload):
        util.log_debug('restconfBeginTask: payload = %s', payload)
        return Sdk.getInstance().datamodel_svc.restconfBeginTask(payload)

    @staticmethod
    def restconfPost(rcPath, operName, payload, taskId=None, commit=True):
        util.log_debug('restconfPost: rcPath = %s, operName = %s, payload = %s, taskId = %s, commit = %s', rcPath, operName, payload, taskId, commit)
        return Sdk.getInstance().datamodel_svc.restconfPost(rcPath, operName, payload, taskId, commit)

    @staticmethod
    def restconfPut(rcPath, operName, payload, taskId=None, commit=True):
        util.log_debug('restconfPut: rcPath = %s, operName = %s, payload = %s, taskId = %s, commit = %s', rcPath, operName, payload, taskId, commit)
        return Sdk.getInstance().datamodel_svc.restconfPut(rcPath, operName, payload, taskId, commit)

    @staticmethod
    def restconfPatch(rcPath, operName, payload, taskId=None, commit=True):
        util.log_debug('restconfPatch: rcPath = %s, operName = %s, payload = %s, taskId = %s, commit = %s', rcPath, operName, payload, taskId, commit)
        return Sdk.getInstance().datamodel_svc.restconfPatch(rcPath, operName, payload, taskId, commit)

    @staticmethod
    def restconfDelete(rcPath, operName, payload, taskId=None, commit=True):
        util.log_debug('restconfDelete: rcPath = %s, operName = %s, payload = %s, taskId = %s, commit = %s', rcPath, operName, payload, taskId, commit)
        return Sdk.getInstance().datamodel_svc.deleteData(rcPath, operName, payload, taskId, commit)

    @staticmethod
    def restconfCommit(taskId, syncCommit=False):
        return Sdk.getInstance().datamodel_svc.restconfCommit(taskId, syncCommit)

from com.anuta.service.task.execution import NaasCallable
class CallableWrapper(NaasCallable):
  def __init__(self, taskId, description, func, args, kwargs):
    NaasCallable.__init__(self, taskId, description)
    self.func = func
    self.args = args
    self.kwargs = kwargs
    util.log_error('taskid=%s, description=%s, func=%s, args=%s, kwargs=%s' % (taskId, description, func, args, kwargs))
    
  def execute(self):
    return self.func(*self.args, **self.kwargs)

from com.anuta.service.task.execution import NaasRunnable
class RunnableWrapper(NaasRunnable):
  def __init__(self, taskId, description, func, args, kwargs):
    NaasRunnable.__init__(self, taskId, description)
    self.func = func
    self.args = args
    self.kwargs = kwargs
    
  def execute(self):
    return self.func(*self.args, **self.kwargs)
    
def wrap_readwrite_tx(fn):
  def wrapped_fn(*args, **kwargs):
    description = '%s' % (fn)
    callable = CallableWrapper(YangSessionThreadLocal.getTaskId(), description, fn, args, kwargs)
    return Sdk.getInstance().transactionHelper.insideReadWriteTransaction(callable)

  return wrapped_fn

def readwritetx():
  return wrap_readwrite_tx

def wrap_readonly_tx(fn):
  def wrapped_fn(*args, **kwargs):
    description = fn.__name__
    callable = CallableWrapper(YangSessionThreadLocal.getTaskId(), description, fn, args, kwargs)
    return Sdk.getInstance().transactionHelper.insideReadOnlyTransaction(callable)

  return wrapped_fn

def readonlytx():
  return wrap_readonly_tx

def wrap_new_tx(fn):
  def wrapped_fn(*args, **kwargs):
    description = fn.__name__
    runnable = RunnableWrapper(YangSessionThreadLocal.getTaskId(), description, fn, args, kwargs)
    return Sdk.getInstance().transactionHelper.executeInsideNestedTransaction(runnable)

  return wrapped_fn

def newtx():
  return wrap_new_tx

def registerRpcOperationProcessor(request):
  Sdk.getInstance().yangServiceProcessor.registerRpcOperationProcessor(request)

def registerFeatureHandler(feature_name, handler):
    Sdk.getInstance().yangServiceProcessor.addFeatureHandler(feature_name, handler)

def unregisterFeatureHandler(feature_name):
    Sdk.getInstance().yangServiceProcessor.removeFeatureHandler(feature_name)

try:
  from java.lang import Runnable
except ImportError:
  exc_type, exc_value, exc_traceback = sys.exc_info()
  util.log_error('Exception: type=%s, val=%s, traceback=%s\n%s' % (traceback.format_exception(exc_type, exc_value, exc_traceback)))

try:
  class TransactionObj (Runnable):
      def __init__(self, func):
          util.log_debug(func)
          self.func = func
  
      def run(self):
          util.log_debug('Inside transaction')
          self.func()
          return
except NameError:
  pass
def registerServiceHandler(name, handler, globalMap=True):
    """ Register a service handler
    Args:
    name: service name
    handler: service handler
    """
    util.log_debug('Registering %s. globalMap = %s' % (name, globalMap))
    util.log_debug('Sdk.getInstance() = %s' % (Sdk.getInstance()))
    Sdk.getInstance().yangServiceProcessor.registerYangServiceHandler(
        name, handler, globalMap)

def unregisterServiceHandler(name, globalMap = True):
    """ Unregister a service handler corresponding to a given name
    Args:
    name: service name
    """
    util.log_debug('Unregistering l3service')
    Sdk.getInstance().yangServiceProcessor.unregisterYangServiceHandler(name, globalMap)

# def unregisterServiceHandler(name):
#     util.log_debug('Unregistering l3service')
#     Sdk.getInstance().yangServiceProcessor.unregisterYangServiceHandler(name)

class ServiceModelContext(object):

    """ Common serivce model context that is used to represent the python plugin context

    The data passed from the java code is converted into this context. Specific handlers can 
    extend this and store custom data

    Attributes:
    payload_obj: the parsed object representing the payload
    service_obj: the service object (the subclasses can override and the fetch logic)
    session: yang session
    task_id: Id of the task related to the service
    sdata: service data
    service_rcpath: rcpath of the service
    """

    def __init__(self, id, sdata):
        self.id = id
        self.sdata = sdata
        self.session = sdata.getSession()
        self.task_id = sdata.getTaskId()
        util.log_debug('ServiceModelContext.__init__: id = %s, serviceData = %s' % (id, sdata))
        util.log_debug('ServiceModelContext.__init__: payload: %s' % (sdata.getPayload()))
        self.payload_obj = util.parseXmlString(sdata.getPayload())
        util.log_debug('ServiceModelContext.__init__: payload_obj: %s' % (self.payload_obj))
        self.service_xpath = sdata.getServiceXPath()
        self.service_rcpath = sdata.getServiceRcPath()
        self.service_xmlobj = None
        self.service_obj = None

    def load_service_object(self, service_rcpath=None):
        """ load the service object from the service rcpath 
        Args:
        service_rcpath: rcpath of the service
        """
        if service_rcpath == None:
            service_rcpath = self.service_rcpath
        util.log_debug('ServiceModelContext.load_service_object: service_rcpath = %s' % (service_rcpath))
        if service_rcpath == None:
            raise Exception('Invalid service rcpath')
        try:
            service_xml = Sdk.getData(service_rcpath, '', self.task_id, None)
            #util.log_debug('ServiceModelContext.load_service_object: service payload (rcpath=%s): %s' % (service_rcpath, service_xml))
            self.service_xmlobj = util.parseXmlString(service_xml)
        except DataNodeNotFoundException:
            raise Exception('Invalid service rcpath')

    def getSession(self):
        return self.session

    def getPayloadObject(self):
        return self.payload_obj

    def getTaskId(self):
        return self.task_id

    def getServiceData(self):
        return self.sdata

    def getServiceRcPath(self):
        return self.service_rcpath

    def setServiceRcPath(self, value):
        self.service_rcpath = value

    def getServiceObject(self):
        return self.service_obj

if ncx.Config.is_remote():
    class YangServiceHandler:
        def __init__(self):
            pass
else:
    try:
      from com.anuta.service.yang import YangServiceHandler
    except ImportError:
      class YangServiceHandler:
          def __init__(self):
              pass
          def DeletePreProcessor(self):
              pass
          def CreatePreProcessor(self):
              pass
          def UpdatePreProcessor(self):
              pass

class AbstractYangServiceHandler(YangServiceHandler):

    """ Abstract YangServiceHandler implementation 
    
    Attributes:
    handler_map: Dictionary containing xpath as keys and corresponding service handlers as values
    """

    def __init__(self):
        self.handler_map = {}
        self.global_map = True
        
    def create(self, id, sdata):
        """ Empty create method, override while subclassing this class.
        Args:
        id: service id
        sdata: service data
        """
        util.log_debug('Empty create method')
        util.log_debug('sdata = %s' % (sdata))
        return

    def update(self, id, sdata):
        """ Empty update method. override while subclassing this class.
        Args:
        id: service id
        sdata: service data
        """
        util.log_debug('Empty update method')
        util.log_debug('id = %s, serviceData = %s' % (id, sdata))
        xmlObj = util.parseXmlString(sdata.getPayload())
        util.log_debug(xmlObj.toXml())
        return
    
    def isIncrementalOperationSupported(self, id, sdata):
        """ Returns true if incremental operation is supported for a given service id
        and false otherwise.
        Args:
        id: service id
        sdata: service data
        """
        return False

    def delete(self, id, sdata):
        """ Empty update method. override while subclassing this class.
        Args:
        id: service id
        sdata: service data
        """
        util.log_debug('Empty delete method')
        util.log_debug('id = %s, serviceData = %s' % (id, sdata))
        return

    def rollbackCreate(self, id, sdata):
        """ Empty rollback method. override while subclassing this class.
        Args:
        id: service id
        sdata: service data
        """
        util.log_debug('Empty rollbackCreate method')
        util.log_debug('id = %s, serviceData = %s' % (id, sdata))
        return

    def rollbackUpdate(self, id, sdata):
        """ Empty rollback method. override while subclassing this class.
        Args:
        id: service id
        sdata: service data
        """
        util.log_debug('Empty rollbackUpdate method')
        util.log_debug('id = %s, serviceData = %s' % (id, sdata))
        return

    def rollbackDelete(self, id, sdata):
        """ Empty rollback method. override while subclassing this class.
        Args:
        id: service id
        sdata: service data
        """
        util.log_debug('Empty rollbackDelete method')
        util.log_debug('id = %s, serviceData = %s' % (id, sdata))
        return

    def afterCreate(self, id, serviceData):
        pass

    def afterUpdate(self, id, serviceData):
        pass

    def afterDelete(self, id, serviceData):
        pass

    def beforeCreateCommit(self, id, sdata):
        pass

    def beforeUpdateCommit(self, id, sdata):
        pass

    def beforeDeleteCommit(self, id, sdata):
        pass

    def register(self):
        """ Register all resource unit handlers. This is called from the plugin code 
        when the plugin is started 
        """
        for xpath in self.handler_map.keys():
            handler = self.handler_map[xpath]
            util.log_debug('Registering %s => %s' % (xpath, handler))
            registerServiceHandler(xpath, handler, False)

    def unregister(self):
        """ Unregister all resource unit handlers. This is called from the plugin code 
        when the plugin is stopped 
        """
        for xpath in self.handler_map.keys():
            handler = self.handler_map[xpath]
            unregisterServiceHandler(xpath, self.global_map)

class YangObject:
    def __init__(self, rcpath, task_id, rootelem):
        self.rcpath = rcpath
        self.task_id = task_id
        self.rootelem = rootelem
        self.xml = None
        self.rootobj = None

    def load(self):
        self.xml = Sdk.getData(self.rcpath, '', self.task_id, None)
        util.log_debug('YangObject.load(): rcpath = %s' % (self.rcpath))
        util.log_debug('YangObject.load(): xml = %s' % (self.xml))
        self.parsed_obj = util.parseXmlString(self.xml)
        self.rootobj = self.parsed_obj.get_field_value(self.rootelem)
        util.log_debug('YangObject.load(): root_object = %s' % (self.rootobj))
        return self

if ncx.Config.is_remote():
    class SessionPreProcessor:
        def __init__(self):
            pass
        def processBeforeReserve(self, session):
            util.log_debug('Empty method. session: %s' % (session))
            pass
else:
    try:
      from com.anuta.yang.session import YangSessionPreReserveProcessor
      class SessionPreProcessor(YangSessionPreReserveProcessor):
          def __init__(self):
              pass
          def processBeforeReserve(self, session):
              util.log_debug('Empty method. session: %s' % (session))
              pass
    except ImportError, NameError:
      class SessionPreProcessor():
          def __init__(self):
              pass
          def processBeforeReserve(self, session):
              util.log_debug('Empty method. session: %s' % (session))
              pass

def removeOperations(operations, arr):
    try:
      import java.util.ArrayList as ArrayList
      from com.anuta.service.yang import YangServiceProcessor
    except ImportError:
      pass
    alist = ArrayList()
    for op in arr:
        alist.add(op)
    util.log_debug('removing operations: %s' % (alist))
    YangServiceProcessor.removeOperations(operations, alist)
    
def moveOperations(operations, srcOperationList, destOperationList, after = True):
    """args:
    after: denotes if the list srcOperationList must be appended after or before destOperationList
    """
    try:
      import java.util.ArrayList as ArrayList
      from com.anuta.service.yang import YangServiceProcessor
    except ImportError:
      pass
    srcOprArr = ArrayList()
    for op in srcOperationList:
        srcOprArr.add(op)
    destOprArr = ArrayList()
    for op in destOperationList:
        destOprArr.add(op)    
    util.log_debug('src operations: %s dest operations: %s' % (srcOperationList, destOperationList))
    YangServiceProcessor.moveOperations(operations, srcOprArr, destOprArr, after)

class XPathResult(object):
    def __init__(self, is_leaf = True, value = None, xpath = None, rcpath = None):
        self.xpath = xpath
        self.rcpath = rcpath
        self.is_leaf = is_leaf
        self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '%s:(leaf=%s,value=%s)' % (self.rcpath, self.is_leaf, self.value)

def evaluate_xpath(xpath, skip_deleted = True):
    util.log_debug('Evaluating %s' % (xpath))
    resolver = YangXPathResolver(None, xpath)
    result = []
    for dn in resolver.resolve():
        if skip_deleted and dn.isMarkedForDeletion():
            continue
        res = XPathResult(dn.getPropertyNode(), dn.getValue(), dn.getXPath(), dn.getRcPath())
        result.append(res)

    return result

try:
  from com.anuta.service.yang.data import YangServiceData
except ImportError:
  class YangSession(object):
    def addYangSessionPreReserveProcessor(self, pr):
        pass

  class YangServiceData(object):
   def __init__(self):
     self.payload = None
     self.rcpath = None

   def setSessionItem(self):
     pass

   def getSessionItem(self):
     pass

   def getSession(self):
     Session = YangSession()
     return Session

   def getXPath(self):
     pass

   def getRcPath(self):
     return self.rcpath

   def setRcPath(self,rcpath):
     self.rcpath= rcpath

   def getPath(self):
     pass

   def setPayload(self, string):
     self.payload = string
     pass

   def getPayload(self):
     return self.payload

   def getPreviousPayload(self):
     pass

   def getDepth(self):
     pass
 
   def getServiceType(self):
     pass

   def getTaskId(self):
     pass

   def setTaskId(self):
     pass

   def getServiceRcPath(self):
     pass

   def getServiceXPath(self):
     pass

   def toString(self):
     pass

   def getFeatureRelativePath(self):
     pass

   def setFeatureRelativePath(self):
     pass

   def getFeatureServiceNodeRcPath(self):
     pass

   def setFeatureServiceNodeRcPath(self):
     pass

from com.anuta.dataengine.api.engine.component import YangRpcRequestProcessor
class AbstractYangRpcRequestProcessor(YangRpcRequestProcessor):
  def __init__(self):
    pass

  def processRequest(self, result):
    result.setTaskStatusManaged(False)
    

