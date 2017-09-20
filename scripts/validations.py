#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2015-2016 Anuta Networks, Inc. All Rights Reserved.
#

import re
from servicemodel import yang
from servicemodel import util
from servicemodel import ipam
from servicemodel import devicemgr


from cpedeployment_lib import getLocalObject


def execute_cmds(device, cmds):
    from java.util import Arrays
    from com.anuta.api import DeviceId
    if device == None:
        raise Exception('Given device is either offline or not present in NCX')
    devid = DeviceId(None, device.device.id)

    from com.anuta.service.devicemgr.execplan import DeviceCommandExecutionService
    svc = yang.Sdk.getBean(DeviceCommandExecutionService)

    print 'Commands to be executed: %s' % (cmds)
    output = {}
    if len(cmds) == 0:
        print 'Empty commands'
        return output

    res = svc.executeExecCommands(devid, Arrays.asList(cmds), True, 60)
    if res == None or not res.isSuccessful():
        print 'res: %s' % (res)
        return output

    idx = 0
    for r in res.getSessionDetails():
        if idx < len(cmds):
            cmd = cmds[idx]
        else:
            cmd = ''
        idx = idx + 1
        response_buf = r.getResponse()
        print 'Response buf: %s' % (response_buf)
        output[cmd] = response_buf

    print '%s' % (output)
    return output


def interface_status_validation(smodelctx, sdata, dev, **kwarg):
    cmd = 'show interfaces %s' % (kwarg['inputdict']['interface_name'])
    output = execute_cmds(dev, [cmd])
    if output == {}:
        raise Exception("Failed to execute cmd: %s on device: %s" %(cmd, dev))

    if 'is up, line protocol is up' in output[cmd]:
        result = 'UP'
    else:
        result = 'DOWN'

    payload = "<%s>%s</%s>" % ('result', result, 'result')
    yang.Sdk.createData(sdata.getRcPath(), payload, sdata.getSession())


def ping_status_validation(smodelctx, sdata, dev, **kwarg):
    vrf = kwarg['inputdict']['vrf']
    destination_ip = kwarg['inputdict']['destination_ip']
    if util.isEmpty(vrf):
        cmd = 'ping %s' % (destination_ip)
    else:
        cmd = 'ping vrf %s %s' % (vrf, destination_ip)

    output = execute_cmds(dev, [cmd])

    exp = 'rate is (\d+) percent'
    res = re.search(exp, output[cmd])
    result = 'fail'
    if res:
        if int(res.group(1)) > 0:
            result = 'pass'
    
    payload = "<%s>%s</%s>" % ('result', result, 'result')
    yang.Sdk.createData(sdata.getRcPath(), payload, sdata.getSession())
