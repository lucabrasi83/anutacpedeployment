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
from servicemodel import yang


class ExternalNetworkFeature(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        yang.AbstractYangServiceHandler.__init__(self)
        self.handler_map = {}

    def create(self, id, sdata):
        print 'reserving external network feature'
        print 'id = %s, sdata = %s' % (id, sdata)
        relpath = sdata.getFeatureRelativePath()
        print 'relpath: %s' % (relpath)
        if relpath is not None:
            self.create_child_feature(sdata, relpath)

    def create_child_feature(self, sdata, relpath):
        name = relpath.getLastToken()
        print 'relpath = %s' % (relpath)

    @staticmethod
    def getInstance():
        if(ExternalNetworkFeature._instance == None):
            ExternalNetworkFeature._instance = ExternalNetworkFeature()
        return ExternalNetworkFeature._instance

    def register(self):
        yang.registerFeatureHandler('external-network', self)

    def unregister(self):
        yang.unregisterFeatureHandler('external-network')
