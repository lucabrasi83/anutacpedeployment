#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2016-2017 Anuta Networks, Inc. All Rights Reserved.
#


from servicemodel import yang
from servicemodel import util

from com.anuta.service.yang import YangServiceProcessor
from com.anuta.service.yang import YangRpcProcessor

class Cpedeployment_Ipsla_Threshold_Violation_Event_HandlerRpcProcessor(YangRpcProcessor):
    def __init__(self, rpc):
        self.rpc = rpc
        
    def processPostRpcOperation(self, res, result):
        return

    def processRpcOperation(self, result):
        payload = result.getOperationPayload();
        xmlObj = util.parseXmlString(payload)
        print '%s' % (xmlObj)

        #Custom code
        #yang.Sdk.data_model_post(rcpath, opername, payload)
        #result.setOutput('buffer', '<![CDATA[%s]]>' % ('Hello World'))
