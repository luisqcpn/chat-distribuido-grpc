# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: chat.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'chat.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\x04\x63hat\"0\n\x0b\x43hatMessage\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1f\n\x0bJoinRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"\'\n\x0cJoinResponse\x12\x17\n\x0fwelcome_message\x18\x01 \x01(\t2r\n\x0b\x43hatService\x12\x31\n\x08JoinChat\x12\x11.chat.JoinRequest\x1a\x12.chat.JoinResponse\x12\x30\n\x04\x43hat\x12\x11.chat.ChatMessage\x1a\x11.chat.ChatMessage(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHATMESSAGE']._serialized_start=20
  _globals['_CHATMESSAGE']._serialized_end=68
  _globals['_JOINREQUEST']._serialized_start=70
  _globals['_JOINREQUEST']._serialized_end=101
  _globals['_JOINRESPONSE']._serialized_start=103
  _globals['_JOINRESPONSE']._serialized_end=142
  _globals['_CHATSERVICE']._serialized_start=144
  _globals['_CHATSERVICE']._serialized_end=258
# @@protoc_insertion_point(module_scope)
