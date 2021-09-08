# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/tts_frontend_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from messages import tts_frontend_message_pb2 as messages_dot_tts__frontend__message__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services/tts_frontend_service.proto',
  package='com.grammatek.tts_frontend',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#services/tts_frontend_service.proto\x12\x1a\x63om.grammatek.tts_frontend\x1a#messages/tts_frontend_message.proto\x1a\x1bgoogle/protobuf/empty.proto2\xaf\x04\n\x0bTTSFrontend\x12j\n\tNormalize\x12,.com.grammatek.tts_frontend.NormalizeRequest\x1a-.com.grammatek.tts_frontend.NormalizeResponse\"\x00\x12~\n\x12NormalizeTokenwise\x12,.com.grammatek.tts_frontend.NormalizeRequest\x1a\x38.com.grammatek.tts_frontend.TokenBasedNormalizedResponse\"\x00\x12r\n\rTTSPreprocess\x12-.com.grammatek.tts_frontend.PreprocessRequest\x1a\x30.com.grammatek.tts_frontend.PreprocessedResponse\"\x00\x12h\n\x1cGetDefaultPhonemeDescription\x12\x16.google.protobuf.Empty\x1a..com.grammatek.tts_frontend.PhonemeDescription\"\x00\x12V\n\nGetVersion\x12\x16.google.protobuf.Empty\x1a..com.grammatek.tts_frontend.AbiVersionResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[messages_dot_tts__frontend__message__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TTSFRONTEND = _descriptor.ServiceDescriptor(
  name='TTSFrontend',
  full_name='com.grammatek.tts_frontend.TTSFrontend',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=134,
  serialized_end=693,
  methods=[
  _descriptor.MethodDescriptor(
    name='Normalize',
    full_name='com.grammatek.tts_frontend.TTSFrontend.Normalize',
    index=0,
    containing_service=None,
    input_type=messages_dot_tts__frontend__message__pb2._NORMALIZEREQUEST,
    output_type=messages_dot_tts__frontend__message__pb2._NORMALIZERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='NormalizeTokenwise',
    full_name='com.grammatek.tts_frontend.TTSFrontend.NormalizeTokenwise',
    index=1,
    containing_service=None,
    input_type=messages_dot_tts__frontend__message__pb2._NORMALIZEREQUEST,
    output_type=messages_dot_tts__frontend__message__pb2._TOKENBASEDNORMALIZEDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TTSPreprocess',
    full_name='com.grammatek.tts_frontend.TTSFrontend.TTSPreprocess',
    index=2,
    containing_service=None,
    input_type=messages_dot_tts__frontend__message__pb2._PREPROCESSREQUEST,
    output_type=messages_dot_tts__frontend__message__pb2._PREPROCESSEDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDefaultPhonemeDescription',
    full_name='com.grammatek.tts_frontend.TTSFrontend.GetDefaultPhonemeDescription',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=messages_dot_tts__frontend__message__pb2._PHONEMEDESCRIPTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetVersion',
    full_name='com.grammatek.tts_frontend.TTSFrontend.GetVersion',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=messages_dot_tts__frontend__message__pb2._ABIVERSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TTSFRONTEND)

DESCRIPTOR.services_by_name['TTSFrontend'] = _TTSFRONTEND

# @@protoc_insertion_point(module_scope)
