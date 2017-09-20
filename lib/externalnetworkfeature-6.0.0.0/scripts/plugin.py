#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2014-2015 Anuta Networks, Inc. All Rights Reserved.

def get_plugin_info():
    return Plugin('external-network', '1.0')

from com.anuta.service.python.plugin import PythonPlugin
from com.anuta.service.python.plugin import PythonPluginType

from servicemodel import util
import externalnetwork

class Plugin(PythonPlugin):

    def __init__(self, name, version):
        self.setName(name)
        self.setVersion(version)
        self.setPluginType(PythonPluginType.SERVICE_MODEL)
        self.setDescription('External Network Feature')

    def init(self):
        externalnetwork.ExternalNetworkFeature.getInstance().register()

    def shutdown(self):
        externalnetwork.ExternalNetworkFeature.getInstance().unregister()
