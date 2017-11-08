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

#
#ALL THE CUSTOMIZATIONS REGARDING DATAPROCESSING SHOULD BE WRITTEN INTO THIS FILE
#
"""
Tree Structure of Handled XPATH:

services
        |
        managed-cpe-services
                            |
                            customer
                                    |
                                    analytics
                                             
Schema Representation:

/services/managed-cpe-services/customer/analytics
"""
"""
Names of Leafs for this Yang Entity
              update

"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr

from cpedeployment.cpedeployment_lib import getLocalObject
from cpedeployment.cpedeployment_lib import getDeviceObject
from cpedeployment.cpedeployment_lib import getCurrentObjectConfig
from cpedeployment.cpedeployment_lib import getPreviousObjectConfig
from cpedeployment.cpedeployment_lib import ServiceModelContext
from cpedeployment.cpedeployment_lib import getParentObject 
from cpedeployment.cpedeployment_lib import log

class ServiceDataCustomization:

    @staticmethod
    def process_service_create_data(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the inputs"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']

    @staticmethod
    def process_service_device_bindings(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the device bindings or Call the Business Login Handlers"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']
        devbindobjs = kwargs['devbindobjs']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return


    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']

        #Previous config and previous inputdict
        pconfig = kwargs['pconfig']
        pinputdict = kwargs['pinputdict']

        dev = kwargs['dev']

        uri = sdata.getRcPath()
        parent_uri = uri[:uri.find(uri.split('/')[-1])]
        util.log_debug('PARENT_URI:', parent_uri)
        single_path = '/controller:services/cpedeployment:managed-cpe-services/customer/single-cpe-site/single-cpe-site-services/site-name'
        single_count = count(single_path, parent_uri)
        yang.Sdk.createData(parent_uri, '<single-cpe>' + str(single_count) + '</single-cpe>', sdata.getSession(), False)

        single_dual_path = '/controller:services/cpedeployment:managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/site-name'
        single_dual_count = count(single_dual_path, parent_uri)
        yang.Sdk.createData(parent_uri, '<single-cpe-dual>' + str(single_dual_count) + '</single-cpe-dual>', sdata.getSession(), False)

        dual_path = '/controller:services/cpedeployment:managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/site-name'
        dual_count = count(dual_path, parent_uri)
        yang.Sdk.createData(parent_uri, '<dual-cpe>' + str(dual_count) + '</dual-cpe>', sdata.getSession(), False)

        dual_dual_path = '/controller:services/cpedeployment:managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/site-name'
        dual_dual_count = count(dual_dual_path, parent_uri)
        yang.Sdk.createData(parent_uri, '<dual-cpe-dual>' + str(dual_dual_count) + '</dual-cpe-dual>', sdata.getSession(), False)

        triple_path = '/controller:services/cpedeployment:managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/site-name'
        triple_count = count(triple_path, parent_uri)
        yang.Sdk.createData(parent_uri, '<triple-cpe>' + str(triple_count) + '</triple-cpe>', sdata.getSession(), False)

        total_count = single_count + single_dual_count + dual_count + dual_dual_count + triple_count
        yang.Sdk.createData(parent_uri, '<total-sites>' + str(total_count) + '</total-sites>', sdata.getSession(), False)

        dps_path = '/controller:services/cpedeployment:managed-cpe-services/customer/dps/dps-services/name'
        dps_count = count(dps_path, parent_uri)
        yang.Sdk.createData(parent_uri, '<total-dps>' + str(dps_count) + '</total-dps>', sdata.getSession(), False)

        single_gb_path = '/controller:services/cpedeployment:managed-cpe-services/customer/single-cpe-site/single-cpe-site-services/'
        single_result = count_days(single_gb_path, parent_uri, sdata)

        single_dual_gb_path = '/controller:services/cpedeployment:managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/'
        single_dual_result = count_days(single_dual_gb_path, parent_uri, sdata)

        dual_gb_path = '/controller:services/cpedeployment:managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/'
        dual_result = count_days(dual_gb_path, parent_uri, sdata)

        dual_dual_gb_path = '/controller:services/cpedeployment:managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/'
        dual_dual_result = count_days(dual_dual_gb_path, parent_uri, sdata)

        triple_gb_path = '/controller:services/cpedeployment:managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/'
        triple_result = count_days(triple_gb_path, parent_uri, sdata)

        green_7_count = int(single_result[0]) + int(single_dual_result[0]) + int(dual_result[0]) + int(dual_dual_result[0]) + int(triple_result[0])
        green_15_count = int(single_result[1]) + int(single_dual_result[1]) + int(dual_result[1]) + int(dual_dual_result[1]) + int(triple_result[1])
        green_30_count = int(single_result[2]) + int(single_dual_result[2]) + int(dual_result[2]) + int(dual_dual_result[2]) + int(triple_result[2])
        brown_7_count = int(single_result[3]) + int(single_dual_result[3]) + int(dual_result[3]) + int(dual_dual_result[3]) + int(triple_result[3])
        brown_15_count = int(single_result[4]) + int(single_dual_result[4]) + int(dual_result[4]) + int(dual_dual_result[4]) + int(triple_result[4])
        brown_30_count = int(single_result[5]) + int(single_dual_result[5]) + int(dual_result[5]) + int(dual_dual_result[5]) + int(triple_result[5])

        yang.Sdk.createData(parent_uri+'analytics', '<last-7-days-green>' + str(green_7_count) + '</last-7-days-green>', sdata.getSession(), False)
        yang.Sdk.createData(parent_uri+'analytics', '<last-15-days-green>' + str(green_15_count) + '</last-15-days-green>', sdata.getSession(), False)
        yang.Sdk.createData(parent_uri+'analytics', '<last-30-days-green>' + str(green_30_count) + '</last-30-days-green>', sdata.getSession(), False)

        yang.Sdk.createData(parent_uri+'analytics', '<last-7-days-brown>' + str(brown_7_count) + '</last-7-days-brown>', sdata.getSession(), False)
        yang.Sdk.createData(parent_uri+'analytics', '<last-15-days-brown>' + str(brown_15_count) + '</last-15-days-brown>', sdata.getSession(), False)
        yang.Sdk.createData(parent_uri+'analytics', '<last-30-days-brown>' + str(brown_30_count) + '</last-30-days-brown>', sdata.getSession(), False)

        last_7 = green_7_count + brown_7_count
        yang.Sdk.createData(parent_uri+'analytics', '<last-7-days>' + str(last_7) + '</last-7-days>', sdata.getSession(), False)

        last_15 = green_15_count + brown_15_count
        yang.Sdk.createData(parent_uri+'analytics', '<last-15-days>' + str(last_15) + '</last-15-days>', sdata.getSession(), False)

        last_30 = green_30_count + brown_30_count
        yang.Sdk.createData(parent_uri+'analytics', '<last-30-days>' + str(last_30) + '</last-30-days>', sdata.getSession(), False)


    @staticmethod
    def process_service_delete_data(smodelctx, sdata, **kwargs):
      """callback called for delete operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        dev = kwargs['dev']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

class DeletePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for Deletion"""
        log('operations: %s' % (operations))

class CreatePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for creation"""
        log('operations: %s' % (operations))


def count(path, parent_uri):
    result = yang.evaluate_xpath(path)
    count = 0
    for each_result in util.convert_to_list(result):
        path, leaf = str(each_result).split(':(')
        if path.__contains__(parent_uri):
            site_name = leaf.split('value=')[-1].split(')')[0]
            util.log_debug('SITE NAME:', site_name)
            count += 1
    return count


def count_days(global_path, parent_uri, sdata):
    result = []
    green_url = global_path + 'greenfield-site'
    green_result = yang.evaluate_xpath(green_url)
    green_site = {}
    for each_result in util.convert_to_list(green_result):
        path, leaf = str(each_result).split(':(')
        green = leaf.split('value=')[-1].split(')')[0]
        green_site[path] = green

    util.log_debug('GREEN:', green_site)

    brown_url = global_path + 'brownfield-site'
    brown_result = yang.evaluate_xpath(brown_url)
    brown_site = {}
    for each_result in util.convert_to_list(brown_result):
        path, leaf = str(each_result).split(':(')
        brown = leaf.split('value=')[-1].split(')')[0]
        brown_site[path] = brown

    util.log_debug('BROWN:', brown_site)

    created_on_url = global_path + 'created-on'
    created_on_result = yang.evaluate_xpath(created_on_url)
    create_date = {}
    for each_result in util.convert_to_list(created_on_result):
        path, leaf = str(each_result).split(':(')
        created_on = leaf.split('value=')[-1].split(')')[0]
        create_date[path] = created_on

    util.log_debug('CREATED_ON:', create_date)

    month = { 'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6',
                  'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12',
                  }

    green_7_count = 0
    green_15_count = 0
    green_30_count = 0
    for key in green_site:
        if key.__contains__(parent_uri):
            if green_site[key] == 'true':
                key_create = key[:key.find(key.split('/')[-1])] + 'created-on'
                creation = create_date[key_create]
                year, mon, day = creation.split(' ')[0].split('-')

                from datetime import datetime
                days = str(datetime(int(year), int(month[mon]), int(day)) - datetime.now())
                no_of_days = days.split(' day')[0].split('-')[1]

                if int(no_of_days) <= 7:
                    green_7_count += 1

                if int(no_of_days) <= 15:
                    green_15_count += 1

                if int(no_of_days) <= 30:
                    green_30_count += 1

    brown_7_count = 0
    brown_15_count = 0
    brown_30_count = 0
    for key in brown_site:
        if key.__contains__(parent_uri):
            if brown_site[key] == 'true':
                key_create = key[:key.find(key.split('/')[-1])] + 'created-on'
                creation = create_date[key_create]
                year, mon, day = creation.split(' ')[0].split('-')

                from datetime import datetime
                days = str(datetime(int(year), int(month[mon]), int(day)) - datetime.now())
                no_of_days = days.split(' day')[0].split('-')[1]

                if int(no_of_days) <= 7:
                    brown_7_count += 1

                if int(no_of_days) <= 15:
                    brown_15_count += 1

                if int(no_of_days) <= 30:
                    brown_30_count += 1

    result.append(green_7_count)
    result.append(green_15_count)
    result.append(green_30_count)
    result.append(brown_7_count)
    result.append(brown_15_count)
    result.append(brown_30_count)
    util.log_debug('RESULT:', result)
    return result
