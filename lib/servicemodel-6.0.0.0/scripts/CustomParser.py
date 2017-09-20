try:
  from yangtypes import safe_name, YANGBool, RestrictedClassType
  import untangle
except ImportError:
  from pyangbind.lib.yangtypes import safe_name, YANGBool, RestrictedClassType
  from servicemodel import untangle
  from servicemodel import yang
  from servicemodel import util

import decimal
import copy
from pprint import pprint

class CustomParser(object):
  def __init__(self, debug=False, target='', platform='', target_schema={}, hardcoded_tokens_indexes={}, commands=[]):
    self.debug = debug
    self.test = True
    self.target = target
    self.platform = platform
    self.raw_commands = commands
    self.commands = []
    self.target_schema = target_schema
    self.hardcoded_tokens_indexes = hardcoded_tokens_indexes
    self.command_attr = {}
    self.fetch_command_from_target_platform()
    self.class_map = {
      'enumeration': {
          "base_type": True,
          "quote_arg": True,
          "pytype": RestrictedClassType,
          "args": {'base_type':unicode, 'restriction_type':"dict_key", 
                                        'restriction_arg':{}}
      },
      'boolean': {
          "base_type": True,
          "quote_arg": True,
          "pytype": YANGBool
      },
      'bits': {
          "base_type": True,
          "quote_arg": True,
          "pytype": unicode
      },    
      'uint8': {
          "base_type": True,
          "pytype": RestrictedClassType,
          "args": {'base_type':int,
                      'restriction_dict':{'range': ['0..255']}, 'int_size':8}
      },
      'uint16': {
          "base_type": True,
          "pytype": RestrictedClassType,
          "args": {'base_type':int,
                      'restriction_dict':{'range': ['0..65535']}, 'int_size':16}
      },
      'uint32': {
          "base_type": True,
          "pytype": RestrictedClassType,
          "args": {'base_type':long,
                      'restriction_dict':{'range': ['0..4294967295']}, 'int_size':32}
      },
      'uint64': {
          "base_type": True,
          "pytype": RestrictedClassType,
          "args": {'base_type':long,
                      'restriction_dict':{'range': ['0..18446744073709551615']},
                      'int_size':64}
      },
      'instance-identifier': {
          "base_type": True,
          "quote_arg": True,
          "pytype": unicode
      },
      'string': {
          "base_type": True,
          "quote_arg": True,
          "pytype": RestrictedClassType,
          "args": {'base_type':unicode, 'restriction_dict':{}}
      },
      'decimal64': {
          "base_type": True,
          "pytype": decimal.Decimal
      },
      'empty': {
          "base_type": True,
          "quote_arg": True,
          "pytype": YANGBool
      },
      'int8': {
          "base_type": True,
          "pytype": RestrictedClassType,
          "args": {'base_type':int,
                      'restriction_dict':{'range': ['-128..127']}, 'int_size':8}
      },
      'int16': {
          "base_type": True,
          "pytype": RestrictedClassType,
          "args": {'base_type':int,
                      'restriction_dict':{'range': ['-32768..32767']}, 'int_size':16}
      },
      'int32': {
          "base_type": True,
          "pytype": RestrictedClassType,
          "args": {'base_type':long,
                      'restriction_dict':{'range': ['-2147483648..2147483647']},
                      'int_size':32}
      },
      'int64': {
          "base_type": True,
          "pytype": RestrictedClassType,
          "args": {'base_type':long,
                      'restriction_dict':{'range':
                      ['-9223372036854775808..9223372036854775807']}, 'int_size':64}
      },
    }

  def refine_commands_strings(self):
    command_strings = self.raw_commands
    refined_command_string = []
    for command_string in command_strings:
      command_string = command_string.strip()
      #strip the conditional statement
      if command_string[0] == '#':
        command = ''
        cond_start = False
        cli_start = False
        for i in xrange(len(command_string)):
          if command_string[i] == '(':
            cond_start = True
          elif command_string[i] == ')' and cond_start:
            cli_start = True
            cond_start = False
            continue
          elif command_string[i] == '#':
            cli_start = False
            cond_start = True
            if command != '':
              refined_command_string.append(command.strip())
              command = ''

          if cli_start:
            command +=  command_string[i]

        if command != '':
          refined_command_string.append(command.strip())
      else:
        refined_command_string.append(command_string.strip())

    return refined_command_string

  def fetch_command_from_target_platform(self):
    if self.target != '' and self.platform != '':
      command_strings = []
      #fetch parse if present otherwise consider create commands from target and platform
      #todo get to leaf-level targets
      devopsstr = yang.Sdk.restconfGet('/controller:device-support/operations/operation=%s,%s/device-operations'%(target, platform), '')
      devopsobj = untangle.parse(devopstr).children[0]
      for devop in util.convert_to_list(devopsobj.device_operation):
        if str(devop.type).lower() == "create":
          for cs in util.convert_to_list(devop.command_string):
            command_strings.append(str(cs).strip())
      for devop in util.convert_to_list(devopsobj.device_operation):
        if str(devop.type).lower() == "parse":
          for cs in util.convert_to_list(devop.command_string):
            command_strings.append(str(cs).strip())
      self.raw_commands = command_strings
      self.commands = self.refine_commands_strings()
    else:
      self.commands = self.refine_commands_strings()

  def get_restriction_dict(self, leaf_schema):
    pattern_stmt = leaf_schema.get('pattern', False)
    length_stmt  = leaf_schema.get('length', False)
    range_stmt   = leaf_schema.get('range', False)

    restrictions = {}
    if pattern_stmt:
      restrictions['pattern'] = pattern_stmt
  
    if length_stmt:
      if "|" in length_stmt:
        restrictions['length'] = [i.replace(' ', '') for i in
                                    length_stmt.split("|")]
      else:
        restrictions['length'] = [length_stmt]
  
    if range_stmt:
      # Complex ranges are separated by pipes
      if "|" in range_stmt:
        restrictions['range'] = [i.replace(' ', '') for i in
                                    range_stmt.split("|")]
      else:
        restrictions['range'] = [range_stmt]

    return restrictions

  def check_value(self, type, value, attrib):
    try:
      if self.class_map[type]['pytype'].__name__ == 'RestrictedClassType':
        restrictions = self.get_restriction_dict(attrib)
        if type == 'enumeration':
          args = copy.deepcopy(self.class_map[type]['args'])
          args['restriction_arg'] =  restrictions['pattern']
          self.class_map[type]['pytype'](value, **args)
        elif type == 'identityref':
          args = copy.deepcopy(self.class_map[type]['args'])
          args['restriction_arg'] =  restrictions['pattern']
          self.class_map[type]['pytype'](value, **args)
        else:
          args = copy.deepcopy(self.class_map[type]['args'])
          if len(restrictions.keys()) > 0:
            args['restriction_dict'] =  restrictions

          #if restriction_dict is empty there is no restriction on the variable
          if len(args['restriction_dict']) > 0:
            self.class_map[type]['pytype'](value, **args)
      else:
        self.class_map[type]['pytype'](value)
    except (ValueError, TypeError):
      if self.debug:
        print("Values did not match for '%s' of type '%s' with args '%s'"%(value, type, args))
      return False

    return True

  def match_against_schema(self, name, value):
    if self.target_schema.get(name) is not None:
      attrib = self.target_schema[name]
      type = attrib['type']
      try:
        if type == 'union':
          for attribd in attrib:
            restrictions = self.get_restriction_dict(attrib)
            if self.check_value(attribd['type'], value, attribd):
              return True
          return False 
        else:
          if not self.check_value(type, value, attrib):
            return False
      except (ValueError, TypeError):
        return False

    return True

  def get_variable_count(self):
    #get variable count in the command
    for command in self.commands:
      optional_start = False
      var_count = 0
      optional_var_count = 0
      ctokens = command.split(' ')
      for ctoken in ctokens:
        if ctoken[0] == '[':
          ctoken = ctoken[1:]
          optional_start = True

        if ctoken[0] == '$':
          if optional_start:
            optional_var_count += 1
          else:
            var_count += 1

        if ctoken[-1] == ']':
          ctoken = ctoken[:-1]
          optional_start = False

      self.command_attr[command] = (optional_var_count, var_count)

  def extract_template_variables(self, incoming_command):
    commands = self.commands
    filled_values = {}
    candidate_command = {}
    tokens = incoming_command.split(' ')

    self.get_variable_count()

    for command in commands:
      optional_start = False
      ctokens = command.split(' ')
      mismatch = False
      if len(ctokens) < len(tokens):
        continue
      matched_token_index = 0
      for i, ctoken in enumerate(ctokens):
        try:
          if ctoken[0] == '$':
            if ctoken[-1] == ']':
              ctoken = ctoken[:-1]
            if self.match_against_schema(ctoken[1:], tokens[matched_token_index]):
              filled_values[ctoken[1:]] = tokens[matched_token_index]
              matched_token_index += 1
            else:
              if self.debug:
                print("schema mismatch for input token '%s' against token '%s' in command '%s'"%(tokens[matched_token_index], ctoken, command))
              mismatch = True
              break
            continue

          if ctoken[0] == '[':
            ctoken = ctoken[1:]
            optional_start = True

          if ctoken == tokens[matched_token_index] or optional_start:
            matched_token_index += 1
            continue
          else:
            if self.debug:
              print("mismatch in input token '%s' against token '%s' in command '%s'"%(tokens[matched_token_index], ctoken, command))
            mismatch = True
            break

          if ctoken[-1] == ']':
            ctoken = ctoken[:-1]
            optional_start = False

        except IndexError:
          if self.debug:
            print("IndexError in token index '%s' matched index '%s' against token '%s' in command '%s'"%(i, matched_token_index, ctoken, command))
          break

      if self.command_attr[command][1] <= len(filled_values.keys()) and not mismatch:
        candidate_command[command] = copy.deepcopy(filled_values)
        break
      else:
        if self.debug:
          print("Filled dictionary count mismatch attributes dict (optional_count, mandatory_count) '%s' filled_values '%s' command '%s'"%(self.command_attr[command], filled_values, command))

      #this mean that commands did not match
      filled_values = {}

    if len(candidate_command.keys()) == 1:
      if self.debug:
        print("Single commands matched candidate commands '%s'"%(candidate_command))
      filled_values = candidate_command[candidate_command.keys()[0]]
    else:
      if self.debug:
        print("Multiple commands matched candidate commands '%s', Selecting the command which does have more variable substitution"%(candidate_command))
      plen = 0
      for key, value in candidate_command.items():
        clen = len(value.keys())
        if clen > plen:
          filled_values = value
        plen = clen

    if len(filled_values.keys()) > 0 and len(hardcoded_tokens_indexes.keys()) > 0:
      ctokens = incoming_command.split(' ')
      for i, ctoken in enumerate(ctokens):
        if hardcoded_tokens_indexes.has_key(str(i+1)):
          filled_values[hardcoded_tokens_indexes[str(i+1)]] = ctoken

    if self.debug:
      print("matched command '%s'"%command)
    return filled_values

if '__main__' == __name__:
  #sample tested commands
  commands=[
    "#if ($protocol) redistribute bgp $bgp-as-number [metric $value1] [metric-type $value2] subnets [tag $tag] [route-map $route-map]",
    "#else if ($protocol) redistribute eigrp $eigrp-as-number [metric $value1] [metric-type $value2] subnets [tag $tag] [route-map $route-map]",
    "#else if ($protocol) redistribute $protocol subnets route-map $route-map",
    "#else ($protocol) redistribute $protocol [metric $value1] [metric-type $value2] subnets [tag $tag] [route-map $route-map]",
    "#else if ($protocol) redistribute ospf $process-id-entry [metric $value1] [metric-type $value2] subnets [tag $tag] [route-map $route-map]",
  ]

  target_schema={'protocol':{'type':"enumeration", 'pattern':{u'bgp': {}, u'ospf': {}, u'connected': {}}},
    'bgp-as-number':{'type':"uint8"},
    'eigrp-as-number':{'type':"uint8"},
    'process-id-entry':{'type':"uint8"},
    'value1':{'type':"uint8"},
    'value2':{'type':"uint8"},
    'tag':{'type':"uint8"},
    'route-map':{'type':"string"},
  }

  #usage example
  hardcoded_tokens_indexes={"2":"protocol"}
  #incoming_command="redistribute ospf 10 metric 100"
  incoming_command="redistribute ospf 101 metric 10 metric-type 100 subnets tag 10"

  cp = CustomParser(debug=True,commands=commands, hardcoded_tokens_indexes=hardcoded_tokens_indexes, target_schema=target_schema)
  pprint(cp.extract_template_variables(incoming_command))
  print('\n')

  #test2
  commands=[
    "#if($../side == \"inside\" AND $../address-translation == \"source\" AND $overload == \"true\" AND $oer == \"false\" AND $extended == \"false\" AND $vrf == null)  ip nat $../side $../address-translation $../nat-list $../value interface $interface-name overload  #else if($../side == \"inside\" AND $../address-translation == \"source\" AND $overload == \"true\" AND $oer == \"false\" AND $extended == \"false\" AND $vrf != null)  ip nat $../side $../address-translation $../nat-list $../value interface $interface-name vrf $vrf overload  #else if($../side == \"inside\" AND $../address-translation == \"source\" AND $overload == \"false\" AND $oer == \"false\" AND $extended == \"false\")  ip nat $../side $../address-translation $../nat-list $../value interface $interface-name [vrf $vrf]  #else if($../side == \"inside\" AND $../address-translation == \"source\" AND $overload == \"true\" AND $oer == \"true\" AND $extended == \"false\")  ip nat $../side $../address-translation $../nat-list $../value interface $interface-name [vrf $vrf] oer overload  #else if($../side == \"inside\" AND $../address-translation == \"source\" AND $overload == \"true\" AND $oer == \"true\" AND $extended == \"true\")  ip nat $../side $../address-translation $../nat-list $../value interface $interface-name [vrf $vrf] oer overload extended",
  ]

  target_schema={'../side':{'type':"enumeration", 'pattern':{u'inside': {}, u'outside': {}}},
    '../address-translation':{'type':"string"},
    '../nat-list':{'type':"enumeration", 'pattern':{u'route-map': {}, u'list': {}}},
    '../value':{'type':"string"},
    'interface-name':{'type':"string"},
    'vrf':{'type':"uint8"},
  }

  #usage example
  #incoming_command="redistribute ospf 10 metric 100"
  hardcoded_tokens_indexes={}
  incoming_command="ip nat inside test route-map hello interface gigabitethernet0/0 overload"

  cp = CustomParser(debug=True, commands=commands, target_schema=target_schema)
  pprint(cp.refine_commands_strings())
  print('\n')
  pprint(cp.extract_template_variables(incoming_command))
