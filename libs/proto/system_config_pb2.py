# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: daq/proto/system_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='daq/proto/system_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1d\x64\x61q/proto/system_config.proto\"\xe1\t\n\tDaqConfig\x12\x18\n\x10site_description\x18\x01 \x01(\t\x12\x18\n\x10monitor_scan_sec\x18\x02 \x01(\x05\x12\x1b\n\x13\x64\x65\x66\x61ult_timeout_sec\x18\x03 \x01(\x05\x12\x12\n\nsettle_sec\x18& \x01(\x05\x12\x11\n\tbase_conf\x18\x04 \x01(\t\x12\x11\n\tsite_path\x18\x05 \x01(\t\x12\x1f\n\x17initial_dhcp_lease_time\x18\x06 \x01(\t\x12\x17\n\x0f\x64hcp_lease_time\x18\x07 \x01(\t\x12\x19\n\x11\x64hcp_response_sec\x18\' \x01(\x05\x12\x1e\n\x16long_dhcp_response_sec\x18\x08 \x01(\x05\x12\"\n\x0cswitch_setup\x18\t \x01(\x0b\x32\x0c.SwitchSetup\x12\x12\n\nhost_tests\x18\x10 \x01(\t\x12\x13\n\x0b\x62uild_tests\x18$ \x01(\x08\x12\x11\n\trun_limit\x18\x11 \x01(\x05\x12\x11\n\tfail_mode\x18\x12 \x01(\x08\x12\x13\n\x0bsingle_shot\x18\" \x01(\x08\x12\x15\n\rresult_linger\x18\x13 \x01(\x08\x12\x0f\n\x07no_test\x18\x14 \x01(\x08\x12\x11\n\tkeep_hold\x18( \x01(\x08\x12\x14\n\x0c\x64\x61q_loglevel\x18\x15 \x01(\t\x12\x18\n\x10mininet_loglevel\x18\x16 \x01(\t\x12\x13\n\x0b\x66inish_hook\x18# \x01(\t\x12\x10\n\x08gcp_cred\x18\x17 \x01(\t\x12\x11\n\tgcp_topic\x18\x18 \x01(\t\x12\x13\n\x0bschema_path\x18\x19 \x01(\t\x12\x11\n\tmud_files\x18\x1a \x01(\t\x12\x14\n\x0c\x64\x65vice_specs\x18\x1b \x01(\t\x12\x13\n\x0btest_config\x18\x1c \x01(\t\x12\x19\n\x11port_debounce_sec\x18\x1d \x01(\x05\x12\x15\n\rtopology_hook\x18\x1e \x01(\t\x12\x17\n\x0f\x64\x65vice_template\x18\x1f \x01(\t\x12\x14\n\x0csite_reports\x18  \x01(\t\x12\x1f\n\x17run_data_retention_days\x18! \x01(\x02\x12.\n\ninterfaces\x18% \x03(\x0b\x32\x1a.DaqConfig.InterfacesEntry\x12/\n\x0b\x66\x61il_module\x18/ \x03(\x0b\x32\x1a.DaqConfig.FailModuleEntry\x12\x1d\n\x15port_flap_timeout_sec\x18\x30 \x01(\x05\x12\x1c\n\tusi_setup\x18\x31 \x01(\x0b\x32\t.UsiSetup\x12 \n\x0brun_trigger\x18\x32 \x01(\x0b\x32\x0b.RunTrigger\x12\x12\n\ndebug_mode\x18\x33 \x01(\x08\x12\x13\n\x0buse_console\x18\x34 \x01(\x08\x12*\n\x10\x64\x65vice_reporting\x18\x35 \x01(\x0b\x32\x10.DeviceReporting\x12%\n\x10\x65xternal_subnets\x18\x36 \x03(\x0b\x32\x0b.SubnetSpec\x12$\n\x0finternal_subnet\x18\x37 \x01(\x0b\x32\x0b.SubnetSpec\x1a=\n\x0fInterfacesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.Interface:\x02\x38\x01\x1a\x31\n\x0f\x46\x61ilModuleEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1c\n\nSubnetSpec\x12\x0e\n\x06subnet\x18\x01 \x01(\t\"0\n\x08UsiSetup\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x17\n\x0frpc_timeout_sec\x18\x02 \x01(\x05\"\xf4\x01\n\x0bSwitchSetup\x12\x11\n\tctrl_intf\x18\t \x01(\t\x12\x0f\n\x07ip_addr\x18\x0b \x01(\t\x12\x13\n\x0buplink_port\x18\r \x01(\x05\x12\x0f\n\x07lo_port\x18\x0e \x01(\x05\x12\x10\n\x08\x61lt_port\x18\x10 \x01(\x05\x12\x0f\n\x07lo_addr\x18\x12 \x01(\t\x12\x11\n\tmods_addr\x18\x14 \x01(\t\x12\x0f\n\x07of_dpid\x18) \x01(\t\x12\x11\n\tdata_intf\x18* \x01(\t\x12\x0e\n\x06\x65xt_br\x18+ \x01(\t\x12\r\n\x05model\x18, \x01(\t\x12\x10\n\x08username\x18- \x01(\t\x12\x10\n\x08password\x18. \x01(\t\"G\n\nRunTrigger\x12\x12\n\nvlan_start\x18\x01 \x01(\x05\x12\x10\n\x08vlan_end\x18\x02 \x01(\x05\x12\x13\n\x0b\x65gress_vlan\x18\x03 \x01(\x05\"\'\n\tInterface\x12\x0c\n\x04opts\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"&\n\x0f\x44\x65viceReporting\x12\x13\n\x0bserver_port\x18\x01 \x01(\x05*U\n\x08\x44hcpMode\x12\n\n\x06NORMAL\x10\x00\x12\r\n\tSTATIC_IP\x10\x01\x12\x0c\n\x08\x45XTERNAL\x10\x02\x12\x11\n\rLONG_RESPONSE\x10\x03\x12\r\n\tIP_CHANGE\x10\x04\x62\x06proto3')
)

_DHCPMODE = _descriptor.EnumDescriptor(
  name='DhcpMode',
  full_name='DhcpMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATIC_IP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LONG_RESPONSE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IP_CHANGE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1766,
  serialized_end=1851,
)
_sym_db.RegisterEnumDescriptor(_DHCPMODE)

DhcpMode = enum_type_wrapper.EnumTypeWrapper(_DHCPMODE)
NORMAL = 0
STATIC_IP = 1
EXTERNAL = 2
LONG_RESPONSE = 3
IP_CHANGE = 4



_DAQCONFIG_INTERFACESENTRY = _descriptor.Descriptor(
  name='InterfacesEntry',
  full_name='DaqConfig.InterfacesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DaqConfig.InterfacesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DaqConfig.InterfacesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1171,
  serialized_end=1232,
)

_DAQCONFIG_FAILMODULEENTRY = _descriptor.Descriptor(
  name='FailModuleEntry',
  full_name='DaqConfig.FailModuleEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DaqConfig.FailModuleEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DaqConfig.FailModuleEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1234,
  serialized_end=1283,
)

_DAQCONFIG = _descriptor.Descriptor(
  name='DaqConfig',
  full_name='DaqConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='site_description', full_name='DaqConfig.site_description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='monitor_scan_sec', full_name='DaqConfig.monitor_scan_sec', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_timeout_sec', full_name='DaqConfig.default_timeout_sec', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settle_sec', full_name='DaqConfig.settle_sec', index=3,
      number=38, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_conf', full_name='DaqConfig.base_conf', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='site_path', full_name='DaqConfig.site_path', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_dhcp_lease_time', full_name='DaqConfig.initial_dhcp_lease_time', index=6,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dhcp_lease_time', full_name='DaqConfig.dhcp_lease_time', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dhcp_response_sec', full_name='DaqConfig.dhcp_response_sec', index=8,
      number=39, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_dhcp_response_sec', full_name='DaqConfig.long_dhcp_response_sec', index=9,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='switch_setup', full_name='DaqConfig.switch_setup', index=10,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host_tests', full_name='DaqConfig.host_tests', index=11,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_tests', full_name='DaqConfig.build_tests', index=12,
      number=36, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_limit', full_name='DaqConfig.run_limit', index=13,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fail_mode', full_name='DaqConfig.fail_mode', index=14,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='single_shot', full_name='DaqConfig.single_shot', index=15,
      number=34, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_linger', full_name='DaqConfig.result_linger', index=16,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_test', full_name='DaqConfig.no_test', index=17,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keep_hold', full_name='DaqConfig.keep_hold', index=18,
      number=40, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='daq_loglevel', full_name='DaqConfig.daq_loglevel', index=19,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mininet_loglevel', full_name='DaqConfig.mininet_loglevel', index=20,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finish_hook', full_name='DaqConfig.finish_hook', index=21,
      number=35, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gcp_cred', full_name='DaqConfig.gcp_cred', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gcp_topic', full_name='DaqConfig.gcp_topic', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schema_path', full_name='DaqConfig.schema_path', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mud_files', full_name='DaqConfig.mud_files', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_specs', full_name='DaqConfig.device_specs', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_config', full_name='DaqConfig.test_config', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port_debounce_sec', full_name='DaqConfig.port_debounce_sec', index=28,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topology_hook', full_name='DaqConfig.topology_hook', index=29,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_template', full_name='DaqConfig.device_template', index=30,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='site_reports', full_name='DaqConfig.site_reports', index=31,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_data_retention_days', full_name='DaqConfig.run_data_retention_days', index=32,
      number=33, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interfaces', full_name='DaqConfig.interfaces', index=33,
      number=37, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fail_module', full_name='DaqConfig.fail_module', index=34,
      number=47, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port_flap_timeout_sec', full_name='DaqConfig.port_flap_timeout_sec', index=35,
      number=48, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usi_setup', full_name='DaqConfig.usi_setup', index=36,
      number=49, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_trigger', full_name='DaqConfig.run_trigger', index=37,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='debug_mode', full_name='DaqConfig.debug_mode', index=38,
      number=51, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_console', full_name='DaqConfig.use_console', index=39,
      number=52, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_reporting', full_name='DaqConfig.device_reporting', index=40,
      number=53, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_subnets', full_name='DaqConfig.external_subnets', index=41,
      number=54, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal_subnet', full_name='DaqConfig.internal_subnet', index=42,
      number=55, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DAQCONFIG_INTERFACESENTRY, _DAQCONFIG_FAILMODULEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=1283,
)


_SUBNETSPEC = _descriptor.Descriptor(
  name='SubnetSpec',
  full_name='SubnetSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subnet', full_name='SubnetSpec.subnet', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1285,
  serialized_end=1313,
)


_USISETUP = _descriptor.Descriptor(
  name='UsiSetup',
  full_name='UsiSetup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='UsiSetup.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rpc_timeout_sec', full_name='UsiSetup.rpc_timeout_sec', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1315,
  serialized_end=1363,
)


_SWITCHSETUP = _descriptor.Descriptor(
  name='SwitchSetup',
  full_name='SwitchSetup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ctrl_intf', full_name='SwitchSetup.ctrl_intf', index=0,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_addr', full_name='SwitchSetup.ip_addr', index=1,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uplink_port', full_name='SwitchSetup.uplink_port', index=2,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lo_port', full_name='SwitchSetup.lo_port', index=3,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alt_port', full_name='SwitchSetup.alt_port', index=4,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lo_addr', full_name='SwitchSetup.lo_addr', index=5,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mods_addr', full_name='SwitchSetup.mods_addr', index=6,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='of_dpid', full_name='SwitchSetup.of_dpid', index=7,
      number=41, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_intf', full_name='SwitchSetup.data_intf', index=8,
      number=42, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ext_br', full_name='SwitchSetup.ext_br', index=9,
      number=43, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='SwitchSetup.model', index=10,
      number=44, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='SwitchSetup.username', index=11,
      number=45, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='SwitchSetup.password', index=12,
      number=46, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1366,
  serialized_end=1610,
)


_RUNTRIGGER = _descriptor.Descriptor(
  name='RunTrigger',
  full_name='RunTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vlan_start', full_name='RunTrigger.vlan_start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vlan_end', full_name='RunTrigger.vlan_end', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='egress_vlan', full_name='RunTrigger.egress_vlan', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1612,
  serialized_end=1683,
)


_INTERFACE = _descriptor.Descriptor(
  name='Interface',
  full_name='Interface',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opts', full_name='Interface.opts', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='Interface.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1685,
  serialized_end=1724,
)


_DEVICEREPORTING = _descriptor.Descriptor(
  name='DeviceReporting',
  full_name='DeviceReporting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_port', full_name='DeviceReporting.server_port', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1726,
  serialized_end=1764,
)

_DAQCONFIG_INTERFACESENTRY.fields_by_name['value'].message_type = _INTERFACE
_DAQCONFIG_INTERFACESENTRY.containing_type = _DAQCONFIG
_DAQCONFIG_FAILMODULEENTRY.containing_type = _DAQCONFIG
_DAQCONFIG.fields_by_name['switch_setup'].message_type = _SWITCHSETUP
_DAQCONFIG.fields_by_name['interfaces'].message_type = _DAQCONFIG_INTERFACESENTRY
_DAQCONFIG.fields_by_name['fail_module'].message_type = _DAQCONFIG_FAILMODULEENTRY
_DAQCONFIG.fields_by_name['usi_setup'].message_type = _USISETUP
_DAQCONFIG.fields_by_name['run_trigger'].message_type = _RUNTRIGGER
_DAQCONFIG.fields_by_name['device_reporting'].message_type = _DEVICEREPORTING
_DAQCONFIG.fields_by_name['external_subnets'].message_type = _SUBNETSPEC
_DAQCONFIG.fields_by_name['internal_subnet'].message_type = _SUBNETSPEC
DESCRIPTOR.message_types_by_name['DaqConfig'] = _DAQCONFIG
DESCRIPTOR.message_types_by_name['SubnetSpec'] = _SUBNETSPEC
DESCRIPTOR.message_types_by_name['UsiSetup'] = _USISETUP
DESCRIPTOR.message_types_by_name['SwitchSetup'] = _SWITCHSETUP
DESCRIPTOR.message_types_by_name['RunTrigger'] = _RUNTRIGGER
DESCRIPTOR.message_types_by_name['Interface'] = _INTERFACE
DESCRIPTOR.message_types_by_name['DeviceReporting'] = _DEVICEREPORTING
DESCRIPTOR.enum_types_by_name['DhcpMode'] = _DHCPMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DaqConfig = _reflection.GeneratedProtocolMessageType('DaqConfig', (_message.Message,), dict(

  InterfacesEntry = _reflection.GeneratedProtocolMessageType('InterfacesEntry', (_message.Message,), dict(
    DESCRIPTOR = _DAQCONFIG_INTERFACESENTRY,
    __module__ = 'daq.proto.system_config_pb2'
    # @@protoc_insertion_point(class_scope:DaqConfig.InterfacesEntry)
    ))
  ,

  FailModuleEntry = _reflection.GeneratedProtocolMessageType('FailModuleEntry', (_message.Message,), dict(
    DESCRIPTOR = _DAQCONFIG_FAILMODULEENTRY,
    __module__ = 'daq.proto.system_config_pb2'
    # @@protoc_insertion_point(class_scope:DaqConfig.FailModuleEntry)
    ))
  ,
  DESCRIPTOR = _DAQCONFIG,
  __module__ = 'daq.proto.system_config_pb2'
  # @@protoc_insertion_point(class_scope:DaqConfig)
  ))
_sym_db.RegisterMessage(DaqConfig)
_sym_db.RegisterMessage(DaqConfig.InterfacesEntry)
_sym_db.RegisterMessage(DaqConfig.FailModuleEntry)

SubnetSpec = _reflection.GeneratedProtocolMessageType('SubnetSpec', (_message.Message,), dict(
  DESCRIPTOR = _SUBNETSPEC,
  __module__ = 'daq.proto.system_config_pb2'
  # @@protoc_insertion_point(class_scope:SubnetSpec)
  ))
_sym_db.RegisterMessage(SubnetSpec)

UsiSetup = _reflection.GeneratedProtocolMessageType('UsiSetup', (_message.Message,), dict(
  DESCRIPTOR = _USISETUP,
  __module__ = 'daq.proto.system_config_pb2'
  # @@protoc_insertion_point(class_scope:UsiSetup)
  ))
_sym_db.RegisterMessage(UsiSetup)

SwitchSetup = _reflection.GeneratedProtocolMessageType('SwitchSetup', (_message.Message,), dict(
  DESCRIPTOR = _SWITCHSETUP,
  __module__ = 'daq.proto.system_config_pb2'
  # @@protoc_insertion_point(class_scope:SwitchSetup)
  ))
_sym_db.RegisterMessage(SwitchSetup)

RunTrigger = _reflection.GeneratedProtocolMessageType('RunTrigger', (_message.Message,), dict(
  DESCRIPTOR = _RUNTRIGGER,
  __module__ = 'daq.proto.system_config_pb2'
  # @@protoc_insertion_point(class_scope:RunTrigger)
  ))
_sym_db.RegisterMessage(RunTrigger)

Interface = _reflection.GeneratedProtocolMessageType('Interface', (_message.Message,), dict(
  DESCRIPTOR = _INTERFACE,
  __module__ = 'daq.proto.system_config_pb2'
  # @@protoc_insertion_point(class_scope:Interface)
  ))
_sym_db.RegisterMessage(Interface)

DeviceReporting = _reflection.GeneratedProtocolMessageType('DeviceReporting', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEREPORTING,
  __module__ = 'daq.proto.system_config_pb2'
  # @@protoc_insertion_point(class_scope:DeviceReporting)
  ))
_sym_db.RegisterMessage(DeviceReporting)


_DAQCONFIG_INTERFACESENTRY._options = None
_DAQCONFIG_FAILMODULEENTRY._options = None
# @@protoc_insertion_point(module_scope)
