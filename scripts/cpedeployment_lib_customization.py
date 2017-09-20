
from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr


import copy

from cpedeployment_lib import getLocalObject
from cpedeployment_lib import getDeviceObject
from cpedeployment_lib import getCurrentObjectConfig
from cpedeployment_lib import ServiceModelContext
from cpedeployment_lib import getParentObject
from cpedeployment_lib import log

"""

Schema Representation:

/services/managed-cpe-services/customer/dmvpn-tunnel-profiles/dmvpn-tunnel-profile
"""
"""
Names of Leafs for this Yang Entity
                name
       tunnel-prefix
          nhrp-nw-id
          tunnel-key
           tunnel-id
nhrp-authentication-key
       wan-tunnel-ip
       wan-public-ip
                 mtu
      tcp-adjust-mss
       ipsec-profile
 no-nhrp-route-watch
    nhrp-reg-no-uniq
    nhrp-reg-timeout
       nhrp-holdtime
       nhrp-redirect
       nhrp-shortcut
tunnel-keepalive-period
tunnel-keepalive-retries
               delay

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dmvpn_tunnel_profiles_dmvpn_tunnel_profile

def custom_input_managed_cpe_services_customer_dmvpn_tunnel_profiles_dmvpn_tunnel_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dmvpn-tunnel-profiles/dmvpn-tunnel-profile
"""
"""
Names of Leafs for this Yang Entity
                name
       tunnel-prefix
          nhrp-nw-id
          tunnel-key
           tunnel-id
nhrp-authentication-key
       wan-tunnel-ip
       wan-public-ip
                 mtu
      tcp-adjust-mss
       ipsec-profile
 no-nhrp-route-watch
    nhrp-reg-no-uniq
    nhrp-reg-timeout
       nhrp-holdtime
       nhrp-redirect
       nhrp-shortcut
tunnel-keepalive-period
tunnel-keepalive-retries
               delay

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dmvpn_tunnel_profiles_dmvpn_tunnel_profile

def custom_managed_cpe_services_customer_dmvpn_tunnel_profiles_dmvpn_tunnel_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dmvpn-tunnel-profiles/dmvpn-tunnel-profile/nhrp-maps
"""
"""
Names of Leafs for this Yang Entity
       wan-tunnel-ip
       wan-public-ip

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_dmvpn_tunnel_profiles_dmvpn_tunnel_profile

def check_managed_cpe_services_customer_dmvpn_tunnel_profiles_dmvpn_tunnel_profile_nhrp_maps_1(dev, sdata, inputdict, dmvpn_tunnel_profile_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dmvpn-tunnel-profiles/dmvpn-tunnel-profile/nhrp-maps
"""
"""
Names of Leafs for this Yang Entity
       wan-tunnel-ip
       wan-public-ip

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dmvpn_tunnel_profiles_dmvpn_tunnel_profile_nhrp_maps_1

def custom_input_managed_cpe_services_customer_dmvpn_tunnel_profiles_dmvpn_tunnel_profile_nhrp_maps_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dmvpn-tunnel-profiles/dmvpn-tunnel-profile/nhrp-maps
"""
"""
Names of Leafs for this Yang Entity
       wan-tunnel-ip
       wan-public-ip

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dmvpn_tunnel_profiles_dmvpn_tunnel_profile_nhrp_maps_1

def custom_managed_cpe_services_customer_dmvpn_tunnel_profiles_dmvpn_tunnel_profile_nhrp_maps_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dmvpn_tunnel_profiles_dmvpn_tunnel_profile_nhrp_maps_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dmvpn-tunnel-profiles/update-dmvpn-tunnel-profile
"""
"""
Names of Leafs for this Yang Entity
                  id
           tunnel-id
           operation
          nhrp-nw-id
          tunnel-key
nhrp-authentication-key
       wan-tunnel-ip
       wan-public-ip
                 mtu
      tcp-adjust-mss
    tunnel-bandwidth
       ipsec-profile
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dmvpn_tunnel_profiles_update_dmvpn_tunnel_profile

def custom_input_managed_cpe_services_customer_dmvpn_tunnel_profiles_update_dmvpn_tunnel_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dmvpn-tunnel-profiles/update-dmvpn-tunnel-profile
"""
"""
Names of Leafs for this Yang Entity
                  id
           tunnel-id
           operation
          nhrp-nw-id
          tunnel-key
nhrp-authentication-key
       wan-tunnel-ip
       wan-public-ip
                 mtu
      tcp-adjust-mss
    tunnel-bandwidth
       ipsec-profile
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dmvpn_tunnel_profiles_update_dmvpn_tunnel_profile

def custom_managed_cpe_services_customer_dmvpn_tunnel_profiles_update_dmvpn_tunnel_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/ipsec/crypto-profiles/crypto-profile
"""
"""
Names of Leafs for this Yang Entity
 crypto-profile-name
         crypto-type
             keyring
           allow-all
      pre-shared-key
                 vrf
          encryption
      authentication
       policy-number
           auth-type
               group
           life-time

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_ipsec_crypto_profiles_crypto_profile

def custom_input_managed_cpe_services_customer_ipsec_crypto_profiles_crypto_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/ipsec/crypto-profiles/crypto-profile
"""
"""
Names of Leafs for this Yang Entity
 crypto-profile-name
         crypto-type
             keyring
           allow-all
      pre-shared-key
                 vrf
          encryption
      authentication
       policy-number
           auth-type
               group
           life-time

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_ipsec_crypto_profiles_crypto_profile

def custom_managed_cpe_services_customer_ipsec_crypto_profiles_crypto_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/ipsec/transform-sets/transform-set
"""
"""
Names of Leafs for this Yang Entity
  transform-set-name
                mode
          encryption
      authentication

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_ipsec_transform_sets_transform_set

def custom_input_managed_cpe_services_customer_ipsec_transform_sets_transform_set(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/ipsec/transform-sets/transform-set
"""
"""
Names of Leafs for this Yang Entity
  transform-set-name
                mode
          encryption
      authentication

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_ipsec_transform_sets_transform_set

def custom_managed_cpe_services_customer_ipsec_transform_sets_transform_set(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/ipsec/ipsec-profiles/ipsec-profile
"""
"""
Names of Leafs for this Yang Entity
  ipsec-profile-name
         sa-lifetime
       transform-set
      crypto-profile
              shared

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_ipsec_ipsec_profiles_ipsec_profile

def custom_input_managed_cpe_services_customer_ipsec_ipsec_profiles_ipsec_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/ipsec/ipsec-profiles/ipsec-profile
"""
"""
Names of Leafs for this Yang Entity
  ipsec-profile-name
         sa-lifetime
       transform-set
      crypto-profile
              shared

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_ipsec_ipsec_profiles_ipsec_profile

def custom_managed_cpe_services_customer_ipsec_ipsec_profiles_ipsec_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/ipsec/delete-ipsec-profile
"""
"""
Names of Leafs for this Yang Entity
                  id
  ipsec-profile-name
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_ipsec_delete_ipsec_profile

def custom_input_managed_cpe_services_customer_ipsec_delete_ipsec_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/ipsec/delete-ipsec-profile
"""
"""
Names of Leafs for this Yang Entity
                  id
  ipsec-profile-name
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_ipsec_delete_ipsec_profile

def custom_managed_cpe_services_customer_ipsec_delete_ipsec_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps/class-map
"""
"""
Names of Leafs for this Yang Entity
                name
         description
          match-type
                dscp
        access-group
           qos-group
            protocol
            http-url

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_class_maps_class_map

def custom_input_managed_cpe_services_customer_qos_service_class_maps_class_map(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps/class-map
"""
"""
Names of Leafs for this Yang Entity
                name
         description
          match-type
                dscp
        access-group
           qos-group
            protocol
            http-url

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_class_maps_class_map

def custom_managed_cpe_services_customer_qos_service_class_maps_class_map(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy
"""
"""
Names of Leafs for this Yang Entity
                name
         description

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_policies_policy

def custom_input_managed_cpe_services_customer_qos_service_policies_policy(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy
"""
"""
Names of Leafs for this Yang Entity
                name
         description

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_policies_policy

def custom_managed_cpe_services_customer_qos_service_policies_policy(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_policies_policy

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_1(dev, sdata, inputdict, policy_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_1

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_1

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_1

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_2(dev, sdata, inputdict, classes_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_2

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_2(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_2

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_2(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_2(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling
"""
"""
Names of Leafs for this Yang Entity
        parent-class

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_2

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_3(dev, sdata, inputdict, class_name_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/queue-limit
"""
"""
Names of Leafs for this Yang Entity
         queue-limit
             packets

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_2

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_queue_limit_3(dev, sdata, inputdict, class_name_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/qos-group
"""
"""
Names of Leafs for this Yang Entity
           qos-group

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_2

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_qos_group_3(dev, sdata, inputdict, class_name_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling
"""
"""
Names of Leafs for this Yang Entity
        parent-class

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_3

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_3(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling
"""
"""
Names of Leafs for this Yang Entity
        parent-class

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_3

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_3(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/remarking
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_3

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_remarking_4(dev, sdata, inputdict, packet_handling_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police
"""
"""
Names of Leafs for this Yang Entity
            bit-rate
police-cir-percentage

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_3

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_4(dev, sdata, inputdict, packet_handling_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/priority
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_3

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_priority_4(dev, sdata, inputdict, packet_handling_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/bandwidth
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_3

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_bandwidth_4(dev, sdata, inputdict, packet_handling_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/remarking
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_remarking_4

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_remarking_4(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/remarking
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_remarking_4

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_remarking_4(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police
"""
"""
Names of Leafs for this Yang Entity
            bit-rate
police-cir-percentage

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_4

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_4(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police
"""
"""
Names of Leafs for this Yang Entity
            bit-rate
police-cir-percentage

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_4

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_4(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate
"""
"""
Names of Leafs for this Yang Entity
            bit-rate

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_4

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_5(dev, sdata, inputdict, police_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/actions
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_4

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_5(dev, sdata, inputdict, police_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate
"""
"""
Names of Leafs for this Yang Entity
            bit-rate

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_5

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_5(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate
"""
"""
Names of Leafs for this Yang Entity
            bit-rate

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_5

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_5(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate/actions
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_5

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_6(dev, sdata, inputdict, rate_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate/actions
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_6

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_6(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate/actions
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_6

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_6(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate/actions/conform-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_6

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_conform_handling_7(dev, sdata, inputdict, actions_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate/actions/exceed-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_6

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_exceed_handling_7(dev, sdata, inputdict, actions_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate/actions/violate-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_6

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_violate_handling_7(dev, sdata, inputdict, actions_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate/actions/conform-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_conform_handling_7

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_conform_handling_7(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate/actions/conform-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_conform_handling_7

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_conform_handling_7(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate/actions/exceed-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_exceed_handling_7

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_exceed_handling_7(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate/actions/exceed-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_exceed_handling_7

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_exceed_handling_7(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate/actions/violate-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_violate_handling_7

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_violate_handling_7(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/rate/actions/violate-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_violate_handling_7

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_rate_actions_violate_handling_7(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/actions
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_5

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_5(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/actions
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_5

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_5(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/actions/conform-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_5

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_conform_handling_6(dev, sdata, inputdict, actions_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/actions/exceed-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_5

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_exceed_handling_6(dev, sdata, inputdict, actions_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/actions/conform-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_conform_handling_6

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_conform_handling_6(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/actions/conform-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_conform_handling_6

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_conform_handling_6(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/actions/exceed-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_exceed_handling_6

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_exceed_handling_6(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/police/actions/exceed-handling
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_exceed_handling_6

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_police_actions_exceed_handling_6(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/priority
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_priority_4

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_priority_4(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/priority
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_priority_4

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_priority_4(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/bandwidth
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_bandwidth_4

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_bandwidth_4(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/bandwidth
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_bandwidth_4

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_bandwidth_4(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/bandwidth/random-detect
"""
"""
Names of Leafs for this Yang Entity
       random-detect

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_bandwidth_4

def check_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_bandwidth_random_detect_5(dev, sdata, inputdict, bandwidth_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/bandwidth/random-detect
"""
"""
Names of Leafs for this Yang Entity
       random-detect

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_bandwidth_random_detect_5

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_bandwidth_random_detect_5(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/packet-handling/bandwidth/random-detect
"""
"""
Names of Leafs for this Yang Entity
       random-detect

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_bandwidth_random_detect_5

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_packet_handling_bandwidth_random_detect_5(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/queue-limit
"""
"""
Names of Leafs for this Yang Entity
         queue-limit
             packets

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_queue_limit_3

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_queue_limit_3(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/queue-limit
"""
"""
Names of Leafs for this Yang Entity
         queue-limit
             packets

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_queue_limit_3

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_queue_limit_3(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/qos-group
"""
"""
Names of Leafs for this Yang Entity
           qos-group

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_qos_group_3

def custom_input_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_qos_group_3(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policies/policy/classes/class-name/qos-group
"""
"""
Names of Leafs for this Yang Entity
           qos-group

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_qos_group_3

def custom_managed_cpe_services_customer_qos_service_policies_policy_classes_class_name_qos_group_3(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/hierarchical-policy/policy
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_hierarchical_policy_policy

def custom_input_managed_cpe_services_customer_qos_service_hierarchical_policy_policy(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/hierarchical-policy/policy
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_hierarchical_policy_policy

def custom_managed_cpe_services_customer_qos_service_hierarchical_policy_policy(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/hierarchical-policy/policy/classes
"""
"""
Names of Leafs for this Yang Entity
          class-name
    child-qos-policy

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_hierarchical_policy_policy

def check_managed_cpe_services_customer_qos_service_hierarchical_policy_policy_classes_1(dev, sdata, inputdict, policy_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/hierarchical-policy/policy/classes
"""
"""
Names of Leafs for this Yang Entity
          class-name
    child-qos-policy

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_hierarchical_policy_policy_classes_1

def custom_input_managed_cpe_services_customer_qos_service_hierarchical_policy_policy_classes_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/hierarchical-policy/policy/classes
"""
"""
Names of Leafs for this Yang Entity
          class-name
    child-qos-policy

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_hierarchical_policy_policy_classes_1

def custom_managed_cpe_services_customer_qos_service_hierarchical_policy_policy_classes_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_qos_service_hierarchical_policy_policy_classes_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policy-update/update-policy
"""
"""
Names of Leafs for this Yang Entity
                name
         policy-name
     packet-handling
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_policy_update_update_policy

def custom_input_managed_cpe_services_customer_qos_service_policy_update_update_policy(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policy-update/update-policy
"""
"""
Names of Leafs for this Yang Entity
                name
         policy-name
     packet-handling
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_policy_update_update_policy

def custom_managed_cpe_services_customer_qos_service_policy_update_update_policy(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policy-update/update-policy/classes
"""
"""
Names of Leafs for this Yang Entity
               class
          percentage

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_policy_update_update_policy

def check_managed_cpe_services_customer_qos_service_policy_update_update_policy_classes_1(dev, sdata, inputdict, update_policy_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policy-update/update-policy/classes
"""
"""
Names of Leafs for this Yang Entity
               class
          percentage

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policy_update_update_policy_classes_1

def custom_input_managed_cpe_services_customer_qos_service_policy_update_update_policy_classes_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policy-update/update-policy/classes
"""
"""
Names of Leafs for this Yang Entity
               class
          percentage

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_qos_service_policy_update_update_policy_classes_1

def custom_managed_cpe_services_customer_qos_service_policy_update_update_policy_classes_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_qos_service_policy_update_update_policy_classes_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps-update/create-class-map
"""
"""
Names of Leafs for this Yang Entity
                name
         description
          match-type
                dscp
        access-group
           qos-group
            protocol
            http-url
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_class_maps_update_create_class_map

def custom_input_managed_cpe_services_customer_qos_service_class_maps_update_create_class_map(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps-update/create-class-map
"""
"""
Names of Leafs for this Yang Entity
                name
         description
          match-type
                dscp
        access-group
           qos-group
            protocol
            http-url
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_class_maps_update_create_class_map

def custom_managed_cpe_services_customer_qos_service_class_maps_update_create_class_map(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps-update/update-class-map
"""
"""
Names of Leafs for this Yang Entity
                  id
                name
                dscp
        access-group
           qos-group
            protocol
            http-url
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_class_maps_update_update_class_map

def custom_input_managed_cpe_services_customer_qos_service_class_maps_update_update_class_map(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps-update/update-class-map
"""
"""
Names of Leafs for this Yang Entity
                  id
                name
                dscp
        access-group
           qos-group
            protocol
            http-url
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_class_maps_update_update_class_map

def custom_managed_cpe_services_customer_qos_service_class_maps_update_update_class_map(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps-update/delete-class-map
"""
"""
Names of Leafs for this Yang Entity
                  id
                name
                dscp
        access-group
           qos-group
            protocol
            http-url
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_class_maps_update_delete_class_map

def custom_input_managed_cpe_services_customer_qos_service_class_maps_update_delete_class_map(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/class-maps-update/delete-class-map
"""
"""
Names of Leafs for this Yang Entity
                  id
                name
                dscp
        access-group
           qos-group
            protocol
            http-url
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_class_maps_update_delete_class_map

def custom_managed_cpe_services_customer_qos_service_class_maps_update_delete_class_map(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policy-class-map-update/update-policy-class-map
"""
"""
Names of Leafs for this Yang Entity
                name
         policy-name
               class
     packet-handling
          percentage
         queue-limit
             packets
           qos-group
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_policy_class_map_update_update_policy_class_map

def custom_input_managed_cpe_services_customer_qos_service_policy_class_map_update_update_policy_class_map(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/qos-service/policy-class-map-update/update-policy-class-map
"""
"""
Names of Leafs for this Yang Entity
                name
         policy-name
               class
     packet-handling
          percentage
         queue-limit
             packets
           qos-group
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_qos_service_policy_class_map_update_update_policy_class_map

def custom_managed_cpe_services_customer_qos_service_policy_class_map_update_update_policy_class_map(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/route-map
"""
"""
Names of Leafs for this Yang Entity
      route-map-name
         description

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_route_maps_route_map

def custom_input_managed_cpe_services_customer_route_maps_route_map(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/route-map
"""
"""
Names of Leafs for this Yang Entity
      route-map-name
         description

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_route_maps_route_map

def custom_managed_cpe_services_customer_route_maps_route_map(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/route-map/route-map-entries
"""
"""
Names of Leafs for this Yang Entity
     sequence-number
         description
              action
            continue

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_route_maps_route_map

def check_managed_cpe_services_customer_route_maps_route_map_route_map_entries_1(dev, sdata, inputdict, route_map_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/route-map/route-map-entries
"""
"""
Names of Leafs for this Yang Entity
     sequence-number
         description
              action
            continue

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_route_maps_route_map_route_map_entries_1

def custom_input_managed_cpe_services_customer_route_maps_route_map_route_map_entries_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/route-map/route-map-entries
"""
"""
Names of Leafs for this Yang Entity
     sequence-number
         description
              action
            continue

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_route_maps_route_map_route_map_entries_1

def custom_managed_cpe_services_customer_route_maps_route_map_route_map_entries_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_route_maps_route_map_route_map_entries_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/route-map/route-map-entries/match-condition
"""
"""
Names of Leafs for this Yang Entity
      condition-type
               value

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_route_maps_route_map_route_map_entries_1

def check_managed_cpe_services_customer_route_maps_route_map_route_map_entries_match_condition_2(dev, sdata, inputdict, route_map_entries_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/route-map/route-map-entries/set-action
"""
"""
Names of Leafs for this Yang Entity
            set-type
                  ip
               value

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_route_maps_route_map_route_map_entries_1

def check_managed_cpe_services_customer_route_maps_route_map_route_map_entries_set_action_2(dev, sdata, inputdict, route_map_entries_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/route-map/route-map-entries/match-condition
"""
"""
Names of Leafs for this Yang Entity
      condition-type
               value

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_route_maps_route_map_route_map_entries_match_condition_2

def custom_input_managed_cpe_services_customer_route_maps_route_map_route_map_entries_match_condition_2(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/route-map/route-map-entries/match-condition
"""
"""
Names of Leafs for this Yang Entity
      condition-type
               value

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_route_maps_route_map_route_map_entries_match_condition_2

def custom_managed_cpe_services_customer_route_maps_route_map_route_map_entries_match_condition_2(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_route_maps_route_map_route_map_entries_match_condition_2(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/route-map/route-map-entries/set-action
"""
"""
Names of Leafs for this Yang Entity
            set-type
                  ip
               value

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_route_maps_route_map_route_map_entries_set_action_2

def custom_input_managed_cpe_services_customer_route_maps_route_map_route_map_entries_set_action_2(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/route-map/route-map-entries/set-action
"""
"""
Names of Leafs for this Yang Entity
            set-type
                  ip
               value

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_route_maps_route_map_route_map_entries_set_action_2

def custom_managed_cpe_services_customer_route_maps_route_map_route_map_entries_set_action_2(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_route_maps_route_map_route_map_entries_set_action_2(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/update-route-maps
"""
"""
Names of Leafs for this Yang Entity
                  id
      route-map-name
     sequence-number
              action
               entry
      condition-type
               value
            set-type
                  ip
           set-value
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_route_maps_update_route_maps

def custom_input_managed_cpe_services_customer_route_maps_update_route_maps(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/update-route-maps
"""
"""
Names of Leafs for this Yang Entity
                  id
      route-map-name
     sequence-number
              action
               entry
      condition-type
               value
            set-type
                  ip
           set-value
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_route_maps_update_route_maps

def custom_managed_cpe_services_customer_route_maps_update_route_maps(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/delete-route-maps
"""
"""
Names of Leafs for this Yang Entity
                  id
      route-map-name
     sequence-number
              action
               entry
      condition-type
               value
            set-type
                  ip
           set-value
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_route_maps_delete_route_maps

def custom_input_managed_cpe_services_customer_route_maps_delete_route_maps(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/route-maps/delete-route-maps
"""
"""
Names of Leafs for this Yang Entity
                  id
      route-map-name
     sequence-number
              action
               entry
      condition-type
               value
            set-type
                  ip
           set-value
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_route_maps_delete_route_maps

def custom_managed_cpe_services_customer_route_maps_delete_route_maps(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/prefix-lists/prefix-list
"""
"""
Names of Leafs for this Yang Entity
    prefix-list-name

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_prefix_lists_prefix_list

def custom_input_managed_cpe_services_customer_prefix_lists_prefix_list(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/prefix-lists/prefix-list
"""
"""
Names of Leafs for this Yang Entity
    prefix-list-name

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_prefix_lists_prefix_list

def custom_managed_cpe_services_customer_prefix_lists_prefix_list(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/prefix-lists/prefix-list/prefix
"""
"""
Names of Leafs for this Yang Entity
         prefix-name
            rule-num
         ipv4-prefix
           condition
exact-matching-prefix-length
minimum-matching-prefix-length
maximum-matching-prefix-length

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_prefix_lists_prefix_list

def check_managed_cpe_services_customer_prefix_lists_prefix_list_prefix_1(dev, sdata, inputdict, prefix_list_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/prefix-lists/prefix-list/prefix
"""
"""
Names of Leafs for this Yang Entity
         prefix-name
            rule-num
         ipv4-prefix
           condition
exact-matching-prefix-length
minimum-matching-prefix-length
maximum-matching-prefix-length

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_prefix_lists_prefix_list_prefix_1

def custom_input_managed_cpe_services_customer_prefix_lists_prefix_list_prefix_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/prefix-lists/prefix-list/prefix
"""
"""
Names of Leafs for this Yang Entity
         prefix-name
            rule-num
         ipv4-prefix
           condition
exact-matching-prefix-length
minimum-matching-prefix-length
maximum-matching-prefix-length

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_prefix_lists_prefix_list_prefix_1

def custom_managed_cpe_services_customer_prefix_lists_prefix_list_prefix_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_prefix_lists_prefix_list_prefix_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/prefix-lists/update-prefix-list
"""
"""
Names of Leafs for this Yang Entity
                  id
    prefix-list-name
           operation
         prefix-name
            rule-num
         ipv4-prefix
           condition
exact-matching-prefix-length
minimum-matching-prefix-length
maximum-matching-prefix-length
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_prefix_lists_update_prefix_list

def custom_input_managed_cpe_services_customer_prefix_lists_update_prefix_list(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/prefix-lists/update-prefix-list
"""
"""
Names of Leafs for this Yang Entity
                  id
    prefix-list-name
           operation
         prefix-name
            rule-num
         ipv4-prefix
           condition
exact-matching-prefix-length
minimum-matching-prefix-length
maximum-matching-prefix-length
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_prefix_lists_update_prefix_list

def custom_managed_cpe_services_customer_prefix_lists_update_prefix_list(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/community-lists/community-list
"""
"""
Names of Leafs for this Yang Entity
        extcommunity
community-list-entry
 community-list-name
           condition
               value
             extcomm

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_community_lists_community_list

def custom_input_managed_cpe_services_customer_community_lists_community_list(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/community-lists/community-list
"""
"""
Names of Leafs for this Yang Entity
        extcommunity
community-list-entry
 community-list-name
           condition
               value
             extcomm

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_community_lists_community_list

def custom_managed_cpe_services_customer_community_lists_community_list(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/community-lists/update-community-list
"""
"""
Names of Leafs for this Yang Entity
                  id
 community-list-name
           operation
community-list-entry
           condition
               value
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_community_lists_update_community_list

def custom_input_managed_cpe_services_customer_community_lists_update_community_list(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/community-lists/update-community-list
"""
"""
Names of Leafs for this Yang Entity
                  id
 community-list-name
           operation
community-list-entry
           condition
               value
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_community_lists_update_community_list

def custom_managed_cpe_services_customer_community_lists_update_community_list(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-site/single-cpe-site-services/wan
"""
"""
Names of Leafs for this Yang Entity
                name
    wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_wan

def custom_input_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-site/single-cpe-site-services/wan
"""
"""
Names of Leafs for this Yang Entity
                name
    wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_wan

def custom_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-site/single-cpe-site-services/lan
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_lan

def custom_input_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_lan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-site/single-cpe-site-services/lan
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_lan

def custom_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_lan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-site/single-cpe-site-services/cpe-lan/lan-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
      inbound-policy
hierarchical-inbound-policy
 hierarchical-policy
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_cpe_lan_lan_profile

def custom_input_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_cpe_lan_lan_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-site/single-cpe-site-services/cpe-lan/lan-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
      inbound-policy
hierarchical-inbound-policy
 hierarchical-policy
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_cpe_lan_lan_profile

def custom_managed_cpe_services_customer_single_cpe_site_single_cpe_site_services_cpe_lan_lan_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/primary-wan
"""
"""
Names of Leafs for this Yang Entity
                name
primary-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_primary_wan

def custom_input_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_primary_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/primary-wan
"""
"""
Names of Leafs for this Yang Entity
                name
primary-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_primary_wan

def custom_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_primary_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/secondary-wan
"""
"""
Names of Leafs for this Yang Entity
                name
secondary-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_secondary_wan

def custom_input_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_secondary_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/secondary-wan
"""
"""
Names of Leafs for this Yang Entity
                name
secondary-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_secondary_wan

def custom_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_secondary_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/lan
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_lan

def custom_input_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_lan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/lan
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_lan

def custom_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_lan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/cpe-lan/lan-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
      inbound-policy
hierarchical-inbound-policy
 hierarchical-policy
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length
        hsrp-version
     hsrp-standby-ip
          hsrp-group
        hsrp-preempt
hsrp-preempt-reload-delay
           auth-type
       auth-password
         hsrp-timers
  hello-interval-sec
 hello-interval-msec
       hold-time-sec
      hold-time-msec

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_cpe_lan_lan_profile

def custom_input_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_cpe_lan_lan_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/cpe-lan/lan-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
      inbound-policy
hierarchical-inbound-policy
 hierarchical-policy
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length
        hsrp-version
     hsrp-standby-ip
          hsrp-group
        hsrp-preempt
hsrp-preempt-reload-delay
           auth-type
       auth-password
         hsrp-timers
  hello-interval-sec
 hello-interval-msec
       hold-time-sec
      hold-time-msec

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_cpe_lan_lan_profile

def custom_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_cpe_lan_lan_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/policy-update-services
"""
"""
Names of Leafs for this Yang Entity
         rtt-trigger

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services

def custom_input_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/policy-update-services
"""
"""
Names of Leafs for this Yang Entity
         rtt-trigger

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services

def custom_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/policy-update-services/cpe-primary
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services

def check_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_cpe_primary_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/policy-update-services/cpe-secondary
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services

def check_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_cpe_secondary_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/policy-update-services/hsrp-update-service
"""
"""
Names of Leafs for this Yang Entity
cpe-primary-hsrp-priority
cpe-secondary-hsrp-priority

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services

def check_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_hsrp_update_service_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/policy-update-services/cpe-primary
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_cpe_primary_1

def custom_input_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_cpe_primary_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/policy-update-services/cpe-primary
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_cpe_primary_1

def custom_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_cpe_primary_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_cpe_primary_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/policy-update-services/cpe-secondary
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_cpe_secondary_1

def custom_input_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_cpe_secondary_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/policy-update-services/cpe-secondary
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_cpe_secondary_1

def custom_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_cpe_secondary_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_cpe_secondary_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/policy-update-services/hsrp-update-service
"""
"""
Names of Leafs for this Yang Entity
cpe-primary-hsrp-priority
cpe-secondary-hsrp-priority

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_hsrp_update_service_1

def custom_input_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_hsrp_update_service_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-site/dual-cpe-site-services/policy-update-services/hsrp-update-service
"""
"""
Names of Leafs for this Yang Entity
cpe-primary-hsrp-priority
cpe-secondary-hsrp-priority

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_hsrp_update_service_1

def custom_managed_cpe_services_customer_dual_cpe_site_dual_cpe_site_services_policy_update_services_hsrp_update_service_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/cpe-primary-cpe-secondary-ic/ic-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_cpe_primary_cpe_secondary_ic_ic_profile

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_cpe_primary_cpe_secondary_ic_ic_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/cpe-primary-cpe-secondary-ic/ic-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_cpe_primary_cpe_secondary_ic_ic_profile

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_cpe_primary_cpe_secondary_ic_ic_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/primary-mpls-wan
"""
"""
Names of Leafs for this Yang Entity
                name
primary-mpls-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_primary_mpls_wan

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_primary_mpls_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/primary-mpls-wan
"""
"""
Names of Leafs for this Yang Entity
                name
primary-mpls-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_primary_mpls_wan

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_primary_mpls_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/primary-inet-wan
"""
"""
Names of Leafs for this Yang Entity
                name
primary-inet-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_primary_inet_wan

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_primary_inet_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/primary-inet-wan
"""
"""
Names of Leafs for this Yang Entity
                name
primary-inet-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_primary_inet_wan

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_primary_inet_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/secondary-mpls-wan
"""
"""
Names of Leafs for this Yang Entity
                name
secondary-mpls-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_secondary_mpls_wan

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_secondary_mpls_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/secondary-mpls-wan
"""
"""
Names of Leafs for this Yang Entity
                name
secondary-mpls-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_secondary_mpls_wan

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_secondary_mpls_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/secondary-inet-wan
"""
"""
Names of Leafs for this Yang Entity
                name
secondary-inet-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_secondary_inet_wan

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_secondary_inet_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/secondary-inet-wan
"""
"""
Names of Leafs for this Yang Entity
                name
secondary-inet-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_secondary_inet_wan

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_secondary_inet_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/lan
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_lan

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_lan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/lan
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_lan

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_lan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/cpe-lan/lan-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
      inbound-policy
hierarchical-inbound-policy
 hierarchical-policy
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length
        hsrp-version
     hsrp-standby-ip
          hsrp-group
        hsrp-preempt
hsrp-preempt-reload-delay
           auth-type
       auth-password
         hsrp-timers
  hello-interval-sec
 hello-interval-msec
       hold-time-sec
      hold-time-msec

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_cpe_lan_lan_profile

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_cpe_lan_lan_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/cpe-lan/lan-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
      inbound-policy
hierarchical-inbound-policy
 hierarchical-policy
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length
        hsrp-version
     hsrp-standby-ip
          hsrp-group
        hsrp-preempt
hsrp-preempt-reload-delay
           auth-type
       auth-password
         hsrp-timers
  hello-interval-sec
 hello-interval-msec
       hold-time-sec
      hold-time-msec

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_cpe_lan_lan_profile

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_cpe_lan_lan_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services
"""
"""
Names of Leafs for this Yang Entity
         rtt-trigger

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services
"""
"""
Names of Leafs for this Yang Entity
         rtt-trigger

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/cpe-primary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services

def check_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_primary_mpls_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/cpe-primary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services

def check_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_primary_inet_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/cpe-secondary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services

def check_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_secondary_mpls_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/cpe-secondary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services

def check_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_secondary_inet_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/hsrp-update-service
"""
"""
Names of Leafs for this Yang Entity
cpe-primary-hsrp-priority
cpe-secondary-hsrp-priority

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services

def check_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_hsrp_update_service_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/cpe-primary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_primary_mpls_1

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_primary_mpls_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/cpe-primary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_primary_mpls_1

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_primary_mpls_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_primary_mpls_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/cpe-primary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_primary_inet_1

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_primary_inet_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/cpe-primary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_primary_inet_1

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_primary_inet_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_primary_inet_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/cpe-secondary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_secondary_mpls_1

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_secondary_mpls_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/cpe-secondary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_secondary_mpls_1

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_secondary_mpls_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_secondary_mpls_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/cpe-secondary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_secondary_inet_1

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_secondary_inet_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/cpe-secondary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_secondary_inet_1

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_secondary_inet_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_cpe_secondary_inet_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/hsrp-update-service
"""
"""
Names of Leafs for this Yang Entity
cpe-primary-hsrp-priority
cpe-secondary-hsrp-priority

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_hsrp_update_service_1

def custom_input_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_hsrp_update_service_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dual-cpe-dual-wan-site/dual-cpe-dual-wan-site-services/policy-update-services/hsrp-update-service
"""
"""
Names of Leafs for this Yang Entity
cpe-primary-hsrp-priority
cpe-secondary-hsrp-priority

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_hsrp_update_service_1

def custom_managed_cpe_services_customer_dual_cpe_dual_wan_site_dual_cpe_dual_wan_site_services_policy_update_services_hsrp_update_service_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/primary-wan
"""
"""
Names of Leafs for this Yang Entity
                name
primary-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_primary_wan

def custom_input_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_primary_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/primary-wan
"""
"""
Names of Leafs for this Yang Entity
                name
primary-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_primary_wan

def custom_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_primary_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/secondary-wan
"""
"""
Names of Leafs for this Yang Entity
                name
secondary-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_secondary_wan

def custom_input_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_secondary_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/secondary-wan
"""
"""
Names of Leafs for this Yang Entity
                name
secondary-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_secondary_wan

def custom_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_secondary_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/lan
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_lan

def custom_input_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_lan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/lan
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_lan

def custom_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_lan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/cpe-lan/lan-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
      inbound-policy
hierarchical-inbound-policy
 hierarchical-policy
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_cpe_lan_lan_profile

def custom_input_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_cpe_lan_lan_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/cpe-lan/lan-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
      inbound-policy
hierarchical-inbound-policy
 hierarchical-policy
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_cpe_lan_lan_profile

def custom_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_cpe_lan_lan_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/policy-update-services/cpe
"""
"""
Names of Leafs for this Yang Entity
           end-point
                name
          end-point1
          end-point2
    import-route-map
    export-route-map

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_policy_update_services_cpe

def custom_input_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_policy_update_services_cpe(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/single-cpe-dual-wan-site/single-cpe-dual-wan-site-services/policy-update-services/cpe
"""
"""
Names of Leafs for this Yang Entity
           end-point
                name
          end-point1
          end-point2
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_policy_update_services_cpe

def custom_managed_cpe_services_customer_single_cpe_dual_wan_site_single_cpe_dual_wan_site_services_policy_update_services_cpe(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf
"""
"""
Names of Leafs for this Yang Entity
            vrf-name
         description
                  rd
 vrf-definition-mode

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_vrfs_vrf

def custom_input_managed_cpe_services_customer_vrfs_vrf(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf
"""
"""
Names of Leafs for this Yang Entity
            vrf-name
         description
                  rd
 vrf-definition-mode

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_vrfs_vrf

def custom_managed_cpe_services_customer_vrfs_vrf(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf/rt-import
"""
"""
Names of Leafs for this Yang Entity
           rt-import

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_vrfs_vrf

def check_managed_cpe_services_customer_vrfs_vrf_rt_import_1(dev, sdata, inputdict, vrf_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf/rt-export
"""
"""
Names of Leafs for this Yang Entity
           rt-export

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_vrfs_vrf

def check_managed_cpe_services_customer_vrfs_vrf_rt_export_1(dev, sdata, inputdict, vrf_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf/import-map
"""
"""
Names of Leafs for this Yang Entity
          import-map
                ipv4
             traffic
         upper-limit

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_vrfs_vrf

def check_managed_cpe_services_customer_vrfs_vrf_import_map_1(dev, sdata, inputdict, vrf_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf/export-map
"""
"""
Names of Leafs for this Yang Entity
          export-map
                ipv4
             traffic
         upper-limit

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_vrfs_vrf

def check_managed_cpe_services_customer_vrfs_vrf_export_map_1(dev, sdata, inputdict, vrf_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf/rt-import
"""
"""
Names of Leafs for this Yang Entity
           rt-import

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_vrfs_vrf_rt_import_1

def custom_input_managed_cpe_services_customer_vrfs_vrf_rt_import_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf/rt-import
"""
"""
Names of Leafs for this Yang Entity
           rt-import

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_vrfs_vrf_rt_import_1

def custom_managed_cpe_services_customer_vrfs_vrf_rt_import_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_vrfs_vrf_rt_import_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf/rt-export
"""
"""
Names of Leafs for this Yang Entity
           rt-export

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_vrfs_vrf_rt_export_1

def custom_input_managed_cpe_services_customer_vrfs_vrf_rt_export_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf/rt-export
"""
"""
Names of Leafs for this Yang Entity
           rt-export

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_vrfs_vrf_rt_export_1

def custom_managed_cpe_services_customer_vrfs_vrf_rt_export_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_vrfs_vrf_rt_export_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf/import-map
"""
"""
Names of Leafs for this Yang Entity
          import-map
                ipv4
             traffic
         upper-limit

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_vrfs_vrf_import_map_1

def custom_input_managed_cpe_services_customer_vrfs_vrf_import_map_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf/import-map
"""
"""
Names of Leafs for this Yang Entity
          import-map
                ipv4
             traffic
         upper-limit

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_vrfs_vrf_import_map_1

def custom_managed_cpe_services_customer_vrfs_vrf_import_map_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_vrfs_vrf_import_map_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf/export-map
"""
"""
Names of Leafs for this Yang Entity
          export-map
                ipv4
             traffic
         upper-limit

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_vrfs_vrf_export_map_1

def custom_input_managed_cpe_services_customer_vrfs_vrf_export_map_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/vrfs/vrf/export-map
"""
"""
Names of Leafs for this Yang Entity
          export-map
                ipv4
             traffic
         upper-limit

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_vrfs_vrf_export_map_1

def custom_managed_cpe_services_customer_vrfs_vrf_export_map_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_vrfs_vrf_export_map_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/host-label
"""
"""
Names of Leafs for this Yang Entity
     host-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/host-label-name

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label

def custom_input_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/host-label
"""
"""
Names of Leafs for this Yang Entity
     host-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/host-label-name

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label

def custom_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/host-label/hostname
"""
"""
Names of Leafs for this Yang Entity
            hostname            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/hostname/hostname

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label

def check_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_hostname_1(dev, sdata, inputdict, host_label_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/host-label/subnet
"""
"""
Names of Leafs for this Yang Entity
              subnet            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/subnet/subnet

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label

def check_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_subnet_1(dev, sdata, inputdict, host_label_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/host-label/hostname
"""
"""
Names of Leafs for this Yang Entity
            hostname            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/hostname/hostname

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_hostname_1

def custom_input_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_hostname_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/host-label/hostname
"""
"""
Names of Leafs for this Yang Entity
            hostname            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/hostname/hostname

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_hostname_1

def custom_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_hostname_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/host-label/subnet
"""
"""
Names of Leafs for this Yang Entity
              subnet            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/subnet/subnet

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_subnet_1

def custom_input_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_subnet_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/host-label/subnet
"""
"""
Names of Leafs for this Yang Entity
              subnet            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/subnet/subnet

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_subnet_1

def custom_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_host_label_subnet_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/update-host-label
"""
"""
Names of Leafs for this Yang Entity
     host-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/host-label-name
           operation
          type1-site
         type1-sites
          type2-site
         type2-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_update_host_label

def custom_input_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_update_host_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/host-labels/update-host-label
"""
"""
Names of Leafs for this Yang Entity
     host-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/host-label/host-label-name
           operation
          type1-site
         type1-sites
          type2-site
         type2-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_update_host_label

def custom_managed_cpe_services_customer_wanop_services_label_configuration_host_labels_update_host_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/domain-labels/domain-label
"""
"""
Names of Leafs for this Yang Entity
   domain-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/domain-label/domain-label-name
              domain            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/domain-label/domain

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_domain_label

def custom_input_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_domain_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/domain-labels/domain-label
"""
"""
Names of Leafs for this Yang Entity
   domain-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/domain-label/domain-label-name
              domain            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/domain-label/domain

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_domain_label

def custom_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_domain_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/domain-labels/update-domain-label
"""
"""
Names of Leafs for this Yang Entity
   domain-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/domain-label/domain-label-name
              domain            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/domain-label/domain
           operation
          type1-site
         type1-sites
          type2-site
         type2-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_update_domain_label

def custom_input_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_update_domain_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/domain-labels/update-domain-label
"""
"""
Names of Leafs for this Yang Entity
   domain-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/domain-label/domain-label-name
              domain            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/domain-label/domain
           operation
          type1-site
         type1-sites
          type2-site
         type2-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_update_domain_label

def custom_managed_cpe_services_customer_wanop_services_label_configuration_domain_labels_update_domain_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/port-labels/port-label
"""
"""
Names of Leafs for this Yang Entity
     port-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port-label-name
                port            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label

def custom_input_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/port-labels/port-label
"""
"""
Names of Leafs for this Yang Entity
     port-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port-label-name
                port            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label

def custom_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_port_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/port-labels/update-port-label
"""
"""
Names of Leafs for this Yang Entity
     port-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port-label-name
                port            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port
           operation
          type1-site
         type1-sites
          type2-site
         type2-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_update_port_label

def custom_input_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_update_port_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/label-configuration/port-labels/update-port-label
"""
"""
Names of Leafs for this Yang Entity
     port-label-name            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port-label-name
                port            maps-to  /ac:devices/ac:device/wanop-device:label-configuration/port-label/port
           operation
          type1-site
         type1-sites
          type2-site
         type2-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_update_port_label

def custom_managed_cpe_services_customer_wanop_services_label_configuration_port_labels_update_port_label(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/applications/application
"""
"""
Names of Leafs for this Yang Entity
    application-name            maps-to  /ac:devices/ac:device/wanop-device:applications/application/application-name
               group            maps-to  /ac:devices/ac:device/wanop-device:applications/application/group
       business-crit            maps-to  /ac:devices/ac:device/wanop-device:applications/application/business-crit
            category            maps-to  /ac:devices/ac:device/wanop-device:applications/application/category
         description            maps-to  /ac:devices/ac:device/wanop-device:applications/application/description
        traffic-type            maps-to  /ac:devices/ac:device/wanop-device:applications/application/traffic-type
      transport-prot            maps-to  /ac:devices/ac:device/wanop-device:applications/application/transport-prot
                dscp            maps-to  /ac:devices/ac:device/wanop-device:applications/application/dscp
                vlan            maps-to  /ac:devices/ac:device/wanop-device:applications/application/vlan
          local-port            maps-to  /ac:devices/ac:device/wanop-device:applications/application/local-port
         remote-port            maps-to  /ac:devices/ac:device/wanop-device:applications/application/remote-port
           local-net            maps-to  /ac:devices/ac:device/wanop-device:applications/application/local-net
          remote-net            maps-to  /ac:devices/ac:device/wanop-device:applications/application/remote-net
            app-prot            maps-to  /ac:devices/ac:device/wanop-device:applications/application/app-prot

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_applications_application

def custom_input_managed_cpe_services_customer_wanop_services_applications_application(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/applications/application
"""
"""
Names of Leafs for this Yang Entity
    application-name            maps-to  /ac:devices/ac:device/wanop-device:applications/application/application-name
               group            maps-to  /ac:devices/ac:device/wanop-device:applications/application/group
       business-crit            maps-to  /ac:devices/ac:device/wanop-device:applications/application/business-crit
            category            maps-to  /ac:devices/ac:device/wanop-device:applications/application/category
         description            maps-to  /ac:devices/ac:device/wanop-device:applications/application/description
        traffic-type            maps-to  /ac:devices/ac:device/wanop-device:applications/application/traffic-type
      transport-prot            maps-to  /ac:devices/ac:device/wanop-device:applications/application/transport-prot
                dscp            maps-to  /ac:devices/ac:device/wanop-device:applications/application/dscp
                vlan            maps-to  /ac:devices/ac:device/wanop-device:applications/application/vlan
          local-port            maps-to  /ac:devices/ac:device/wanop-device:applications/application/local-port
         remote-port            maps-to  /ac:devices/ac:device/wanop-device:applications/application/remote-port
           local-net            maps-to  /ac:devices/ac:device/wanop-device:applications/application/local-net
          remote-net            maps-to  /ac:devices/ac:device/wanop-device:applications/application/remote-net
            app-prot            maps-to  /ac:devices/ac:device/wanop-device:applications/application/app-prot

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_applications_application

def custom_managed_cpe_services_customer_wanop_services_applications_application(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/applications/update-application
"""
"""
Names of Leafs for this Yang Entity
    application-name            maps-to  /ac:devices/ac:device/wanop-device:applications/application/application-name
               group            maps-to  /ac:devices/ac:device/wanop-device:applications/application/group
       business-crit            maps-to  /ac:devices/ac:device/wanop-device:applications/application/business-crit
            category            maps-to  /ac:devices/ac:device/wanop-device:applications/application/category
         description
        traffic-type            maps-to  /ac:devices/ac:device/wanop-device:applications/application/traffic-type
      transport-prot            maps-to  /ac:devices/ac:device/wanop-device:applications/application/transport-prot
                dscp            maps-to  /ac:devices/ac:device/wanop-device:applications/application/dscp
                vlan            maps-to  /ac:devices/ac:device/wanop-device:applications/application/vlan
          local-port            maps-to  /ac:devices/ac:device/wanop-device:applications/application/local-port
         remote-port            maps-to  /ac:devices/ac:device/wanop-device:applications/application/remote-port
           local-net            maps-to  /ac:devices/ac:device/wanop-device:applications/application/local-net
          remote-net            maps-to  /ac:devices/ac:device/wanop-device:applications/application/remote-net
            app-prot            maps-to  /ac:devices/ac:device/wanop-device:applications/application/app-prot
           operation
          type1-site
         type1-sites
          type2-site
         type2-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_applications_update_application

def custom_input_managed_cpe_services_customer_wanop_services_applications_update_application(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/wanop-services/applications/update-application
"""
"""
Names of Leafs for this Yang Entity
    application-name            maps-to  /ac:devices/ac:device/wanop-device:applications/application/application-name
               group            maps-to  /ac:devices/ac:device/wanop-device:applications/application/group
       business-crit            maps-to  /ac:devices/ac:device/wanop-device:applications/application/business-crit
            category            maps-to  /ac:devices/ac:device/wanop-device:applications/application/category
         description
        traffic-type            maps-to  /ac:devices/ac:device/wanop-device:applications/application/traffic-type
      transport-prot            maps-to  /ac:devices/ac:device/wanop-device:applications/application/transport-prot
                dscp            maps-to  /ac:devices/ac:device/wanop-device:applications/application/dscp
                vlan            maps-to  /ac:devices/ac:device/wanop-device:applications/application/vlan
          local-port            maps-to  /ac:devices/ac:device/wanop-device:applications/application/local-port
         remote-port            maps-to  /ac:devices/ac:device/wanop-device:applications/application/remote-port
           local-net            maps-to  /ac:devices/ac:device/wanop-device:applications/application/local-net
          remote-net            maps-to  /ac:devices/ac:device/wanop-device:applications/application/remote-net
            app-prot            maps-to  /ac:devices/ac:device/wanop-device:applications/application/app-prot
           operation
          type1-site
         type1-sites
          type2-site
         type2-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_wanop_services_applications_update_application

def custom_managed_cpe_services_customer_wanop_services_applications_update_application(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-primary-cpe-secondary-ic/ic-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_primary_cpe_secondary_ic_ic_profile

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_primary_cpe_secondary_ic_ic_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-primary-cpe-secondary-ic/ic-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_primary_cpe_secondary_ic_ic_profile

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_primary_cpe_secondary_ic_ic_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-secondary-cpe-tertiary-ic/ic-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_secondary_cpe_tertiary_ic_ic_profile

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_secondary_cpe_tertiary_ic_ic_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-secondary-cpe-tertiary-ic/ic-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_secondary_cpe_tertiary_ic_ic_profile

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_secondary_cpe_tertiary_ic_ic_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-tertiary-cpe-primary-ic/ic-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_tertiary_cpe_primary_ic_ic_profile

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_tertiary_cpe_primary_ic_ic_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-tertiary-cpe-primary-ic/ic-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_tertiary_cpe_primary_ic_ic_profile

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_tertiary_cpe_primary_ic_ic_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/primary-mpls-wan
"""
"""
Names of Leafs for this Yang Entity
                name
primary-mpls-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_primary_mpls_wan

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_primary_mpls_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/primary-mpls-wan
"""
"""
Names of Leafs for this Yang Entity
                name
primary-mpls-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_primary_mpls_wan

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_primary_mpls_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/primary-inet-wan
"""
"""
Names of Leafs for this Yang Entity
                name
primary-inet-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_primary_inet_wan

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_primary_inet_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/primary-inet-wan
"""
"""
Names of Leafs for this Yang Entity
                name
primary-inet-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_primary_inet_wan

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_primary_inet_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/secondary-mpls-wan
"""
"""
Names of Leafs for this Yang Entity
                name
secondary-mpls-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_secondary_mpls_wan

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_secondary_mpls_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/secondary-mpls-wan
"""
"""
Names of Leafs for this Yang Entity
                name
secondary-mpls-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_secondary_mpls_wan

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_secondary_mpls_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/secondary-inet-wan
"""
"""
Names of Leafs for this Yang Entity
                name
secondary-inet-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_secondary_inet_wan

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_secondary_inet_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/secondary-inet-wan
"""
"""
Names of Leafs for this Yang Entity
                name
secondary-inet-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_secondary_inet_wan

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_secondary_inet_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/tertiary-mpls-wan
"""
"""
Names of Leafs for this Yang Entity
                name
tertiary-mpls-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_tertiary_mpls_wan

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_tertiary_mpls_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/tertiary-mpls-wan
"""
"""
Names of Leafs for this Yang Entity
                name
tertiary-mpls-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_tertiary_mpls_wan

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_tertiary_mpls_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/tertiary-inet-wan
"""
"""
Names of Leafs for this Yang Entity
                name
tertiary-inet-wan-connectivity

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_tertiary_inet_wan

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_tertiary_inet_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/tertiary-inet-wan
"""
"""
Names of Leafs for this Yang Entity
                name
tertiary-inet-wan-connectivity

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_tertiary_inet_wan

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_tertiary_inet_wan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/lan
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_lan

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_lan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/lan
"""
"""
Names of Leafs for this Yang Entity
                name

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_lan

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_lan(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-lan/lan-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
      inbound-policy
hierarchical-inbound-policy
 hierarchical-policy
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length
        hsrp-version
     hsrp-standby-ip
          hsrp-group
        hsrp-preempt
hsrp-preempt-reload-delay
           auth-type
       auth-password
         hsrp-timers
  hello-interval-sec
 hello-interval-msec
       hold-time-sec
      hold-time-msec

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_lan_lan_profile

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_lan_lan_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/cpe-lan/lan-profile
"""
"""
Names of Leafs for this Yang Entity
        profile-name
                cidr
      inbound-policy
hierarchical-inbound-policy
 hierarchical-policy
    auto-negotiation
               speed
              duplex
       load-interval
 load-interval-delay
       hold-queue-in
     in-queue-length
      hold-queue-out
    out-queue-length
        hsrp-version
     hsrp-standby-ip
          hsrp-group
        hsrp-preempt
hsrp-preempt-reload-delay
           auth-type
       auth-password
         hsrp-timers
  hello-interval-sec
 hello-interval-msec
       hold-time-sec
      hold-time-msec

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_lan_lan_profile

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_cpe_lan_lan_profile(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services
"""
"""
Names of Leafs for this Yang Entity
         rtt-trigger

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services
"""
"""
Names of Leafs for this Yang Entity
         rtt-trigger

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-primary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services

def check_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_primary_mpls_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-primary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services

def check_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_primary_inet_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-secondary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services

def check_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_secondary_mpls_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-secondary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services

def check_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_secondary_inet_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-tertiary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services

def check_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_tertiary_mpls_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-tertiary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services

def check_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_tertiary_inet_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/hsrp-update-service
"""
"""
Names of Leafs for this Yang Entity
cpe-primary-hsrp-priority
cpe-secondary-hsrp-priority
cpe-tertiary-hsrp-priority

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services

def check_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_hsrp_update_service_1(dev, sdata, inputdict, policy_update_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-primary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_primary_mpls_1

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_primary_mpls_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-primary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_primary_mpls_1

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_primary_mpls_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_primary_mpls_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-primary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_primary_inet_1

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_primary_inet_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-primary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_primary_inet_1

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_primary_inet_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_primary_inet_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-secondary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_secondary_mpls_1

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_secondary_mpls_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-secondary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_secondary_mpls_1

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_secondary_mpls_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_secondary_mpls_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-secondary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_secondary_inet_1

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_secondary_inet_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-secondary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_secondary_inet_1

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_secondary_inet_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_secondary_inet_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-tertiary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_tertiary_mpls_1

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_tertiary_mpls_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-tertiary-mpls
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_tertiary_mpls_1

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_tertiary_mpls_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_tertiary_mpls_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-tertiary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_tertiary_inet_1

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_tertiary_inet_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/cpe-tertiary-inet
"""
"""
Names of Leafs for this Yang Entity
           end-point
    import-route-map
    export-route-map

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_tertiary_inet_1

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_tertiary_inet_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_cpe_tertiary_inet_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/hsrp-update-service
"""
"""
Names of Leafs for this Yang Entity
cpe-primary-hsrp-priority
cpe-secondary-hsrp-priority
cpe-tertiary-hsrp-priority

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_hsrp_update_service_1

def custom_input_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_hsrp_update_service_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/triple-cpe-site/triple-cpe-site-services/policy-update-services/hsrp-update-service
"""
"""
Names of Leafs for this Yang Entity
cpe-primary-hsrp-priority
cpe-secondary-hsrp-priority
cpe-tertiary-hsrp-priority

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_hsrp_update_service_1

def custom_managed_cpe_services_customer_triple_cpe_site_triple_cpe_site_services_policy_update_services_hsrp_update_service_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/access-lists/access-list
"""
"""
Names of Leafs for this Yang Entity
                name
   access-list-entry

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_access_lists_access_list

def custom_input_managed_cpe_services_customer_access_lists_access_list(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/access-lists/access-list
"""
"""
Names of Leafs for this Yang Entity
                name
   access-list-entry

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_access_lists_access_list

def custom_managed_cpe_services_customer_access_lists_access_list(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/access-lists/access-list/access-list-rules
"""
"""
Names of Leafs for this Yang Entity
                name
              action
            protocol
    service-obj-name
    source-condition
       source-object
 source-object-group
         source-port
destination-condition
  destination-object
destination-object-group
         port-number
       match-packets
          precedence
                dscp

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_access_lists_access_list

def check_managed_cpe_services_customer_access_lists_access_list_access_list_rules_1(dev, sdata, inputdict, access_list_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/access-lists/access-list/access-list-rules
"""
"""
Names of Leafs for this Yang Entity
                name
              action
            protocol
    service-obj-name
    source-condition
       source-object
 source-object-group
         source-port
destination-condition
  destination-object
destination-object-group
         port-number
       match-packets
          precedence
                dscp

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_access_lists_access_list_access_list_rules_1

def custom_input_managed_cpe_services_customer_access_lists_access_list_access_list_rules_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/access-lists/access-list/access-list-rules
"""
"""
Names of Leafs for this Yang Entity
                name
              action
            protocol
    service-obj-name
    source-condition
       source-object
 source-object-group
         source-port
destination-condition
  destination-object
destination-object-group
         port-number
       match-packets
          precedence
                dscp

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_access_lists_access_list_access_list_rules_1

def custom_managed_cpe_services_customer_access_lists_access_list_access_list_rules_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_access_lists_access_list_access_list_rules_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/access-lists/update-access-list
"""
"""
Names of Leafs for this Yang Entity
                  id
    access-list-name
           operation
            acl-name
              action
            protocol
    service-obj-name
    source-condition
       source-object
 source-object-group
         source-port
destination-condition
  destination-object
destination-object-group
         port-number
       match-packets
          precedence
                dscp
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_access_lists_update_access_list

def custom_input_managed_cpe_services_customer_access_lists_update_access_list(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/access-lists/update-access-list
"""
"""
Names of Leafs for this Yang Entity
                  id
    access-list-name
           operation
            acl-name
              action
            protocol
    service-obj-name
    source-condition
       source-object
 source-object-group
         source-port
destination-condition
  destination-object
destination-object-group
         port-number
       match-packets
          precedence
                dscp
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_access_lists_update_access_list

def custom_managed_cpe_services_customer_access_lists_update_access_list(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services
"""
"""
Names of Leafs for this Yang Entity
                name
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_dps_dps_services

def custom_input_managed_cpe_services_customer_dps_dps_services(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services
"""
"""
Names of Leafs for this Yang Entity
                name
     single-cpe-site
    single-cpe-sites
       dual-cpe-site
      dual-cpe-sites
single-cpe-dual-wan-site
single-cpe-dual-wan-sites
dual-cpe-dual-wan-site
dual-cpe-dual-wan-sites
     triple-cpe-site
    triple-cpe-sites

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_dps_dps_services

def custom_managed_cpe_services_customer_dps_dps_services(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name
"""
"""
Names of Leafs for this Yang Entity
                 cpe
                 vrf
       lan-interface
hierarchical-inbound-policy
 hierarchical-policy
      inbound-policy
          pbr-policy
         next-hop-ip
         vrf-receive
          bgp-policy
      bgp-policy-qos
       b2b-interface
             vlan-id
                cidr
        interface-ip
     b2b-description
            loopback
loopback-interface-id
         description
       cidr-loopback
         loopback-ip
                ospf
             ospf-id
           router-id
    static-route-map
 connected-route-map
lan-ospf-redistribution
      ospf-route-map
         ospf-metric
    ospf-metric-type
            ospf-tag
ospf-redistribution-id
lan-ebgp-redistribution
       bgp-route-map
          bgp-metric
     bgp-metric-type
             bgp-tag
            vrf-lite
                 bgp
         qppb-policy
redistribute-connected
 redistribute-static
    import-route-map
              tunnel
                 hub
       dmvpn-profile
tunnel-interface-ip-address
    tunnel-bandwidth

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_dps_dps_services

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_1(dev, sdata, inputdict, dps_services_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name
"""
"""
Names of Leafs for this Yang Entity
                 cpe
                 vrf
       lan-interface
hierarchical-inbound-policy
 hierarchical-policy
      inbound-policy
          pbr-policy
         next-hop-ip
         vrf-receive
          bgp-policy
      bgp-policy-qos
       b2b-interface
             vlan-id
                cidr
        interface-ip
     b2b-description
            loopback
loopback-interface-id
         description
       cidr-loopback
         loopback-ip
                ospf
             ospf-id
           router-id
    static-route-map
 connected-route-map
lan-ospf-redistribution
      ospf-route-map
         ospf-metric
    ospf-metric-type
            ospf-tag
ospf-redistribution-id
lan-ebgp-redistribution
       bgp-route-map
          bgp-metric
     bgp-metric-type
             bgp-tag
            vrf-lite
                 bgp
         qppb-policy
redistribute-connected
 redistribute-static
    import-route-map
              tunnel
                 hub
       dmvpn-profile
tunnel-interface-ip-address
    tunnel-bandwidth

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_1

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name
"""
"""
Names of Leafs for this Yang Entity
                 cpe
                 vrf
       lan-interface
hierarchical-inbound-policy
 hierarchical-policy
      inbound-policy
          pbr-policy
         next-hop-ip
         vrf-receive
          bgp-policy
      bgp-policy-qos
       b2b-interface
             vlan-id
                cidr
        interface-ip
     b2b-description
            loopback
loopback-interface-id
         description
       cidr-loopback
         loopback-ip
                ospf
             ospf-id
           router-id
    static-route-map
 connected-route-map
lan-ospf-redistribution
      ospf-route-map
         ospf-metric
    ospf-metric-type
            ospf-tag
ospf-redistribution-id
lan-ebgp-redistribution
       bgp-route-map
          bgp-metric
     bgp-metric-type
             bgp-tag
            vrf-lite
                 bgp
         qppb-policy
redistribute-connected
 redistribute-static
    import-route-map
              tunnel
                 hub
       dmvpn-profile
tunnel-interface-ip-address
    tunnel-bandwidth

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_1

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dps_dps_services_cpe_name_1(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/ospf-networks
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_1

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_ospf_networks_2(dev, sdata, inputdict, cpe_name_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/advertise-networks
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_1

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_advertise_networks_2(dev, sdata, inputdict, cpe_name_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/static-routes
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_1

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_2(dev, sdata, inputdict, cpe_name_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/route-maps
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_1

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_route_maps_2(dev, sdata, inputdict, cpe_name_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/community-lists
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_1

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_community_lists_2(dev, sdata, inputdict, cpe_name_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/prefix-lists
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_1

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_prefix_lists_2(dev, sdata, inputdict, cpe_name_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/ospf-networks
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_ospf_networks_2

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_ospf_networks_2(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/ospf-networks
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_ospf_networks_2

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_ospf_networks_2(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/ospf-networks/ospf-network
"""
"""
Names of Leafs for this Yang Entity
                name
             ospf-id
              prefix
                area
                nssa
            vrf-name

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_ospf_networks_2

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_ospf_networks_ospf_network_3(dev, sdata, inputdict, ospf_networks_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/ospf-networks/ospf-network
"""
"""
Names of Leafs for this Yang Entity
                name
             ospf-id
              prefix
                area
                nssa
            vrf-name

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_ospf_networks_ospf_network_3

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_ospf_networks_ospf_network_3(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/ospf-networks/ospf-network
"""
"""
Names of Leafs for this Yang Entity
                name
             ospf-id
              prefix
                area
                nssa
            vrf-name

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_ospf_networks_ospf_network_3

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_ospf_networks_ospf_network_3(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dps_dps_services_cpe_name_ospf_networks_ospf_network_3(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/advertise-networks
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_advertise_networks_2

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_advertise_networks_2(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/advertise-networks
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_advertise_networks_2

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_advertise_networks_2(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/advertise-networks/advertise-network
"""
"""
Names of Leafs for this Yang Entity
                name
              prefix
           route-map
            vrf-name

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_advertise_networks_2

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_advertise_networks_advertise_network_3(dev, sdata, inputdict, advertise_networks_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/advertise-networks/advertise-network
"""
"""
Names of Leafs for this Yang Entity
                name
              prefix
           route-map
            vrf-name

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_advertise_networks_advertise_network_3

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_advertise_networks_advertise_network_3(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/advertise-networks/advertise-network
"""
"""
Names of Leafs for this Yang Entity
                name
              prefix
           route-map
            vrf-name

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_advertise_networks_advertise_network_3

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_advertise_networks_advertise_network_3(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dps_dps_services_cpe_name_advertise_networks_advertise_network_3(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/static-routes
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_2

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_2(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/static-routes
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_2

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_2(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/static-routes/static-route
"""
"""
Names of Leafs for this Yang Entity
     dest-ip-address
           dest-mask

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_2

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_3(dev, sdata, inputdict, static_routes_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/static-routes/static-route
"""
"""
Names of Leafs for this Yang Entity
     dest-ip-address
           dest-mask

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_3

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_3(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/static-routes/static-route
"""
"""
Names of Leafs for this Yang Entity
     dest-ip-address
           dest-mask

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_3

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_3(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_3(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/static-routes/static-route/options
"""
"""
Names of Leafs for this Yang Entity
                  id
         next-hop-ip
      global-address
              metric
      interface-name
                name
                 vrf
                 tag
               track

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_3

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_options_4(dev, sdata, inputdict, static_route_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/static-routes/static-route/options
"""
"""
Names of Leafs for this Yang Entity
                  id
         next-hop-ip
      global-address
              metric
      interface-name
                name
                 vrf
                 tag
               track

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_options_4

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_options_4(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/static-routes/static-route/options
"""
"""
Names of Leafs for this Yang Entity
                  id
         next-hop-ip
      global-address
              metric
      interface-name
                name
                 vrf
                 tag
               track

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_options_4

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_options_4(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dps_dps_services_cpe_name_static_routes_static_route_options_4(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/route-maps
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_route_maps_2

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_route_maps_2(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/route-maps
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_route_maps_2

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_route_maps_2(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/route-maps/route-map
"""
"""
Names of Leafs for this Yang Entity
      route-map-name

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_route_maps_2

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_route_maps_route_map_3(dev, sdata, inputdict, route_maps_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/route-maps/route-map
"""
"""
Names of Leafs for this Yang Entity
      route-map-name

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_route_maps_route_map_3

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_route_maps_route_map_3(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/route-maps/route-map
"""
"""
Names of Leafs for this Yang Entity
      route-map-name

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_route_maps_route_map_3

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_route_maps_route_map_3(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dps_dps_services_cpe_name_route_maps_route_map_3(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/community-lists
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_community_lists_2

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_community_lists_2(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/community-lists
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_community_lists_2

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_community_lists_2(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/community-lists/community-list
"""
"""
Names of Leafs for this Yang Entity
 community-list-name

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_community_lists_2

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_community_lists_community_list_3(dev, sdata, inputdict, community_lists_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/community-lists/community-list
"""
"""
Names of Leafs for this Yang Entity
 community-list-name

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_community_lists_community_list_3

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_community_lists_community_list_3(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/community-lists/community-list
"""
"""
Names of Leafs for this Yang Entity
 community-list-name

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_community_lists_community_list_3

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_community_lists_community_list_3(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dps_dps_services_cpe_name_community_lists_community_list_3(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/prefix-lists
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_prefix_lists_2

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_prefix_lists_2(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/prefix-lists
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_prefix_lists_2

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_prefix_lists_2(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/prefix-lists/prefix-list
"""
"""
Names of Leafs for this Yang Entity
    prefix-list-name

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_dps_dps_services_cpe_name_prefix_lists_2

def check_managed_cpe_services_customer_dps_dps_services_cpe_name_prefix_lists_prefix_list_3(dev, sdata, inputdict, prefix_lists_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/prefix-lists/prefix-list
"""
"""
Names of Leafs for this Yang Entity
    prefix-list-name

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_prefix_lists_prefix_list_3

def custom_input_managed_cpe_services_customer_dps_dps_services_cpe_name_prefix_lists_prefix_list_3(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/dps/dps-services/cpe-name/prefix-lists/prefix-list
"""
"""
Names of Leafs for this Yang Entity
    prefix-list-name

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_dps_dps_services_cpe_name_prefix_lists_prefix_list_3

def custom_managed_cpe_services_customer_dps_dps_services_cpe_name_prefix_lists_prefix_list_3(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_dps_dps_services_cpe_name_prefix_lists_prefix_list_3(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/object-groups/object-group
"""
"""
Names of Leafs for this Yang Entity
                type
                name
         description

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_object_groups_object_group

def custom_input_managed_cpe_services_customer_object_groups_object_group(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/object-groups/object-group
"""
"""
Names of Leafs for this Yang Entity
                type
                name
         description

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_object_groups_object_group

def custom_managed_cpe_services_customer_object_groups_object_group(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/object-groups/object-group/networks
"""
"""
Names of Leafs for this Yang Entity

"""
#Check for any conditional statements in this API, this API is called from API set_specific_managed_cpe_services_customer_object_groups_object_group

def check_managed_cpe_services_customer_object_groups_object_group_networks_1(dev, sdata, inputdict, object_group_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/object-groups/object-group/networks
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_object_groups_object_group_networks_1

def custom_input_managed_cpe_services_customer_object_groups_object_group_networks_1(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/object-groups/object-group/networks
"""
"""
Names of Leafs for this Yang Entity

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_object_groups_object_group_networks_1

def custom_managed_cpe_services_customer_object_groups_object_group_networks_1(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/object-groups/object-group/networks/network
"""
"""
Names of Leafs for this Yang Entity
                name
        group-object
                host
              prefix

"""
#Check for any conditional statements in this API, this API is called from API managed_cpe_services_customer_object_groups_object_group_networks_1

def check_managed_cpe_services_customer_object_groups_object_group_networks_network_2(dev, sdata, inputdict, networks_obj, top_obj, config, devbindobjs, id, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/object-groups/object-group/networks/network
"""
"""
Names of Leafs for this Yang Entity
                name
        group-object
                host
              prefix

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_object_groups_object_group_networks_network_2

def custom_input_managed_cpe_services_customer_object_groups_object_group_networks_network_2(dev, sdata, inputdict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/object-groups/object-group/networks/network
"""
"""
Names of Leafs for this Yang Entity
                name
        group-object
                host
              prefix

"""
#Write any custom code in the below API, this API is called from managed_cpe_services_customer_object_groups_object_group_networks_network_2

def custom_managed_cpe_services_customer_object_groups_object_group_networks_network_2(dev, sdata, inputdict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

def filter_managed_cpe_services_customer_object_groups_object_group_networks_network_2(dev, sdata, inputdict, top_obj, id, config, **opaque_args):
  return True

"""

Schema Representation:

/services/managed-cpe-services/customer/as-path-acls/as-path-acl
"""
"""
Names of Leafs for this Yang Entity
              number
           condition
          expression

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_as_path_acls_as_path_acl

def custom_input_managed_cpe_services_customer_as_path_acls_as_path_acl(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/as-path-acls/as-path-acl
"""
"""
Names of Leafs for this Yang Entity
              number
           condition
          expression

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_as_path_acls_as_path_acl

def custom_managed_cpe_services_customer_as_path_acls_as_path_acl(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/bgp-peer-groups/bgp-peer-group
"""
"""
Names of Leafs for this Yang Entity
          peer-group
    peer-description
           remote-as
            password
    import-route-map
    export-route-map
       next-hop-self
soft-reconfiguration
   default-originate
default-originate-route-map
      send-community
advertisement-interval
         time-in-sec
              timers
  keepalive-interval
            holdtime

"""
#Write any custom code to modifiy inputs in the below API, this API is called from API set_specific_managed_cpe_services_customer_bgp_peer_groups_bgp_peer_group

def custom_input_managed_cpe_services_customer_bgp_peer_groups_bgp_peer_group(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, id, **opaque_args):
  pass

"""

Schema Representation:

/services/managed-cpe-services/customer/bgp-peer-groups/bgp-peer-group
"""
"""
Names of Leafs for this Yang Entity
          peer-group
    peer-description
           remote-as
            password
    import-route-map
    export-route-map
       next-hop-self
soft-reconfiguration
   default-originate
default-originate-route-map
      send-community
advertisement-interval
         time-in-sec
              timers
  keepalive-interval
            holdtime

"""
#Write any custom code in the below API, this API is called from API set_specific_managed_cpe_services_customer_bgp_peer_groups_bgp_peer_group

def custom_managed_cpe_services_customer_bgp_peer_groups_bgp_peer_group(dev, sdata, inputdict, inputparent_key_dict, top_obj, config, devbindobjs, id, **opaque_args):
  pass
