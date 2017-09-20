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
from servicemodel import devicemgr
from servicemodel import l3feature

from servicemodel import util
from servicemodel import yang

class VRouterFeature(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        yang.AbstractYangServiceHandler.__init__(self)
        self.handler_map = {}

    def create(self, id, sdata):
        print 'id = %s, sdata = %s' % (id, sdata)
        xmlobj = util.parseXmlString(sdata.getPayload())
        print 'payload: (%s)' % (sdata.getPayload())
        print 'xmlobj: (%s)'% (xmlobj)
        relpath = sdata.getFeatureRelativePath()
        print 'relpath: %s' % (relpath)

        l3zone = xmlobj.get_first_field()
        print 'l3zone: [%s]' % (l3zone)
        vrf = util.create_yang_subtree('vrf')
        vrf_name = l3zone.get_field_value('vrf_name')
        if util.isEmpty(vrf_name):
            return
        vrf.name = vrf_name
        deploy_on = l3zone.get_field_value('deploy_on')
        if util.isNotEmpty(deploy_on):
            print 'deploy_on: %s' % (deploy_on)
            for ip in util.convert_to_list(deploy_on):
                print 'device_ip: %s' % (ip)
                dev = devicemgr.getDeviceByIp(ip)
                dev.addVrf(vrf, sdata.getSession())
                #if relpath is not None:
                #    self.create_child_feature(sdata, relpath)

    def create_child_feature(self, sdata, relpath):
        name = relpath.getLastToken()
        print 'relpath = %s' % (relpath)

    @staticmethod
    def getInstance():
        if(VRouterFeature._instance == None):
            VRouterFeature._instance = VRouterFeature()
        return VRouterFeature._instance

    def register(self):
        yang.registerFeatureHandler('vrouter', self)

    def unregister(self):
        yang.unregisterFeatureHandler('vrouter')
