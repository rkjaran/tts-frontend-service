# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages/tts_frontend_message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages/tts_frontend_message.proto',
  package='com.grammatek.tts_frontend',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#messages/tts_frontend_message.proto\x12\x1a\x63om.grammatek.tts_frontend\"d\n\x10NormalizeRequest\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12?\n\x06\x64omain\x18\x02 \x01(\x0e\x32/.com.grammatek.tts_frontend.NormalizationDomain\"0\n\x11NormalizeResponse\x12\x1b\n\x13normalized_sentence\x18\x01 \x03(\t\"j\n\x1cTokenBasedNormalizedResponse\x12J\n\x08sentence\x18\x01 \x03(\x0b\x32\x38.com.grammatek.tts_frontend.TokenBasedNormalizedSentence\"\x83\x01\n\x1cTokenBasedNormalizedSentence\x12\x1b\n\x13normalized_sentence\x18\x01 \x01(\t\x12\x46\n\ntoken_info\x18\x02 \x03(\x0b\x32\x32.com.grammatek.tts_frontend.RawNormalizedTokenInfo\"w\n\x16RawNormalizedTokenInfo\x12\x16\n\x0eoriginal_token\x18\x01 \x01(\t\x12\x18\n\x10normalized_token\x18\x02 \x01(\t\x12\x16\n\x0eoriginal_index\x18\x03 \x01(\x05\x12\x13\n\x0bhas_changed\x18\x04 \x01(\x08\"i\n\x11PreprocessRequest\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x43\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32..com.grammatek.tts_frontend.PhonemeDescription\"v\n\x14PreprocessedResponse\x12\x19\n\x11processed_content\x18\x01 \x01(\t\x12\x43\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32..com.grammatek.tts_frontend.PhonemeDescription\"\xbb\x01\n\x12PhonemeDescription\x12>\n\x08\x61lphabet\x18\x01 \x01(\x0e\x32,.com.grammatek.tts_frontend.PhoneticAlphabet\x12\x39\n\x06\x66ormat\x18\x02 \x01(\x0e\x32).com.grammatek.tts_frontend.PhonemeFormat\x12\x13\n\x0bsyllabified\x18\x03 \x01(\x08\x12\x15\n\rstress_labels\x18\x04 \x01(\x08\"N\n\x12\x41\x62iVersionResponse\x12\x38\n\x07version\x18\x01 \x01(\x0e\x32\'.com.grammatek.tts_frontend.ABI_VERSION*\\\n\x13NormalizationDomain\x12\x17\n\x13NORM_DOMAIN_INVALID\x10\x00\x12\x15\n\x11NORM_DOMAIN_SPORT\x10\x01\x12\x15\n\x11NORM_DOMAIN_OTHER\x10\x02*i\n\x10PhoneticAlphabet\x12\x1d\n\x19PHONETIC_ALPHABET_INVALID\x10\x00\x12\x19\n\x15PHONETIC_ALPHABET_IPA\x10\x01\x12\x1b\n\x17PHONETIC_ALPHABET_SAMPA\x10\x02*H\n\rPhonemeFormat\x12\x13\n\x0fPHONEME_INVALID\x10\x00\x12\x0f\n\x0bPHONEME_CMU\x10\x01\x12\x11\n\rPHONEME_PLAIN\x10\x02*A\n\x0b\x41\x42I_VERSION\x12\x17\n\x13\x41\x42I_VERSION_INVALID\x10\x00\x12\x19\n\x13\x41\x42I_VERSION_CURRENT\x10\x80\x80\x04\x62\x06proto3'
)

_NORMALIZATIONDOMAIN = _descriptor.EnumDescriptor(
  name='NormalizationDomain',
  full_name='com.grammatek.tts_frontend.NormalizationDomain',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORM_DOMAIN_INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NORM_DOMAIN_SPORT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NORM_DOMAIN_OTHER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1079,
  serialized_end=1171,
)
_sym_db.RegisterEnumDescriptor(_NORMALIZATIONDOMAIN)

NormalizationDomain = enum_type_wrapper.EnumTypeWrapper(_NORMALIZATIONDOMAIN)
_PHONETICALPHABET = _descriptor.EnumDescriptor(
  name='PhoneticAlphabet',
  full_name='com.grammatek.tts_frontend.PhoneticAlphabet',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PHONETIC_ALPHABET_INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PHONETIC_ALPHABET_IPA', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PHONETIC_ALPHABET_SAMPA', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1173,
  serialized_end=1278,
)
_sym_db.RegisterEnumDescriptor(_PHONETICALPHABET)

PhoneticAlphabet = enum_type_wrapper.EnumTypeWrapper(_PHONETICALPHABET)
_PHONEMEFORMAT = _descriptor.EnumDescriptor(
  name='PhonemeFormat',
  full_name='com.grammatek.tts_frontend.PhonemeFormat',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PHONEME_INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PHONEME_CMU', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PHONEME_PLAIN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1280,
  serialized_end=1352,
)
_sym_db.RegisterEnumDescriptor(_PHONEMEFORMAT)

PhonemeFormat = enum_type_wrapper.EnumTypeWrapper(_PHONEMEFORMAT)
_ABI_VERSION = _descriptor.EnumDescriptor(
  name='ABI_VERSION',
  full_name='com.grammatek.tts_frontend.ABI_VERSION',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ABI_VERSION_INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ABI_VERSION_CURRENT', index=1, number=65536,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1354,
  serialized_end=1419,
)
_sym_db.RegisterEnumDescriptor(_ABI_VERSION)

ABI_VERSION = enum_type_wrapper.EnumTypeWrapper(_ABI_VERSION)
NORM_DOMAIN_INVALID = 0
NORM_DOMAIN_SPORT = 1
NORM_DOMAIN_OTHER = 2
PHONETIC_ALPHABET_INVALID = 0
PHONETIC_ALPHABET_IPA = 1
PHONETIC_ALPHABET_SAMPA = 2
PHONEME_INVALID = 0
PHONEME_CMU = 1
PHONEME_PLAIN = 2
ABI_VERSION_INVALID = 0
ABI_VERSION_CURRENT = 65536



_NORMALIZEREQUEST = _descriptor.Descriptor(
  name='NormalizeRequest',
  full_name='com.grammatek.tts_frontend.NormalizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='com.grammatek.tts_frontend.NormalizeRequest.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain', full_name='com.grammatek.tts_frontend.NormalizeRequest.domain', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=67,
  serialized_end=167,
)


_NORMALIZERESPONSE = _descriptor.Descriptor(
  name='NormalizeResponse',
  full_name='com.grammatek.tts_frontend.NormalizeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='normalized_sentence', full_name='com.grammatek.tts_frontend.NormalizeResponse.normalized_sentence', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=169,
  serialized_end=217,
)


_TOKENBASEDNORMALIZEDRESPONSE = _descriptor.Descriptor(
  name='TokenBasedNormalizedResponse',
  full_name='com.grammatek.tts_frontend.TokenBasedNormalizedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sentence', full_name='com.grammatek.tts_frontend.TokenBasedNormalizedResponse.sentence', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=219,
  serialized_end=325,
)


_TOKENBASEDNORMALIZEDSENTENCE = _descriptor.Descriptor(
  name='TokenBasedNormalizedSentence',
  full_name='com.grammatek.tts_frontend.TokenBasedNormalizedSentence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='normalized_sentence', full_name='com.grammatek.tts_frontend.TokenBasedNormalizedSentence.normalized_sentence', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token_info', full_name='com.grammatek.tts_frontend.TokenBasedNormalizedSentence.token_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=328,
  serialized_end=459,
)


_RAWNORMALIZEDTOKENINFO = _descriptor.Descriptor(
  name='RawNormalizedTokenInfo',
  full_name='com.grammatek.tts_frontend.RawNormalizedTokenInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='original_token', full_name='com.grammatek.tts_frontend.RawNormalizedTokenInfo.original_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='normalized_token', full_name='com.grammatek.tts_frontend.RawNormalizedTokenInfo.normalized_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='original_index', full_name='com.grammatek.tts_frontend.RawNormalizedTokenInfo.original_index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_changed', full_name='com.grammatek.tts_frontend.RawNormalizedTokenInfo.has_changed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=461,
  serialized_end=580,
)


_PREPROCESSREQUEST = _descriptor.Descriptor(
  name='PreprocessRequest',
  full_name='com.grammatek.tts_frontend.PreprocessRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='com.grammatek.tts_frontend.PreprocessRequest.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='com.grammatek.tts_frontend.PreprocessRequest.description', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=582,
  serialized_end=687,
)


_PREPROCESSEDRESPONSE = _descriptor.Descriptor(
  name='PreprocessedResponse',
  full_name='com.grammatek.tts_frontend.PreprocessedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='processed_content', full_name='com.grammatek.tts_frontend.PreprocessedResponse.processed_content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='com.grammatek.tts_frontend.PreprocessedResponse.description', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=689,
  serialized_end=807,
)


_PHONEMEDESCRIPTION = _descriptor.Descriptor(
  name='PhonemeDescription',
  full_name='com.grammatek.tts_frontend.PhonemeDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alphabet', full_name='com.grammatek.tts_frontend.PhonemeDescription.alphabet', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format', full_name='com.grammatek.tts_frontend.PhonemeDescription.format', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='syllabified', full_name='com.grammatek.tts_frontend.PhonemeDescription.syllabified', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stress_labels', full_name='com.grammatek.tts_frontend.PhonemeDescription.stress_labels', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=810,
  serialized_end=997,
)


_ABIVERSIONRESPONSE = _descriptor.Descriptor(
  name='AbiVersionResponse',
  full_name='com.grammatek.tts_frontend.AbiVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='com.grammatek.tts_frontend.AbiVersionResponse.version', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=999,
  serialized_end=1077,
)

_NORMALIZEREQUEST.fields_by_name['domain'].enum_type = _NORMALIZATIONDOMAIN
_TOKENBASEDNORMALIZEDRESPONSE.fields_by_name['sentence'].message_type = _TOKENBASEDNORMALIZEDSENTENCE
_TOKENBASEDNORMALIZEDSENTENCE.fields_by_name['token_info'].message_type = _RAWNORMALIZEDTOKENINFO
_PREPROCESSREQUEST.fields_by_name['description'].message_type = _PHONEMEDESCRIPTION
_PREPROCESSEDRESPONSE.fields_by_name['description'].message_type = _PHONEMEDESCRIPTION
_PHONEMEDESCRIPTION.fields_by_name['alphabet'].enum_type = _PHONETICALPHABET
_PHONEMEDESCRIPTION.fields_by_name['format'].enum_type = _PHONEMEFORMAT
_ABIVERSIONRESPONSE.fields_by_name['version'].enum_type = _ABI_VERSION
DESCRIPTOR.message_types_by_name['NormalizeRequest'] = _NORMALIZEREQUEST
DESCRIPTOR.message_types_by_name['NormalizeResponse'] = _NORMALIZERESPONSE
DESCRIPTOR.message_types_by_name['TokenBasedNormalizedResponse'] = _TOKENBASEDNORMALIZEDRESPONSE
DESCRIPTOR.message_types_by_name['TokenBasedNormalizedSentence'] = _TOKENBASEDNORMALIZEDSENTENCE
DESCRIPTOR.message_types_by_name['RawNormalizedTokenInfo'] = _RAWNORMALIZEDTOKENINFO
DESCRIPTOR.message_types_by_name['PreprocessRequest'] = _PREPROCESSREQUEST
DESCRIPTOR.message_types_by_name['PreprocessedResponse'] = _PREPROCESSEDRESPONSE
DESCRIPTOR.message_types_by_name['PhonemeDescription'] = _PHONEMEDESCRIPTION
DESCRIPTOR.message_types_by_name['AbiVersionResponse'] = _ABIVERSIONRESPONSE
DESCRIPTOR.enum_types_by_name['NormalizationDomain'] = _NORMALIZATIONDOMAIN
DESCRIPTOR.enum_types_by_name['PhoneticAlphabet'] = _PHONETICALPHABET
DESCRIPTOR.enum_types_by_name['PhonemeFormat'] = _PHONEMEFORMAT
DESCRIPTOR.enum_types_by_name['ABI_VERSION'] = _ABI_VERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NormalizeRequest = _reflection.GeneratedProtocolMessageType('NormalizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _NORMALIZEREQUEST,
  '__module__' : 'messages.tts_frontend_message_pb2'
  # @@protoc_insertion_point(class_scope:com.grammatek.tts_frontend.NormalizeRequest)
  })
_sym_db.RegisterMessage(NormalizeRequest)

NormalizeResponse = _reflection.GeneratedProtocolMessageType('NormalizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _NORMALIZERESPONSE,
  '__module__' : 'messages.tts_frontend_message_pb2'
  # @@protoc_insertion_point(class_scope:com.grammatek.tts_frontend.NormalizeResponse)
  })
_sym_db.RegisterMessage(NormalizeResponse)

TokenBasedNormalizedResponse = _reflection.GeneratedProtocolMessageType('TokenBasedNormalizedResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOKENBASEDNORMALIZEDRESPONSE,
  '__module__' : 'messages.tts_frontend_message_pb2'
  # @@protoc_insertion_point(class_scope:com.grammatek.tts_frontend.TokenBasedNormalizedResponse)
  })
_sym_db.RegisterMessage(TokenBasedNormalizedResponse)

TokenBasedNormalizedSentence = _reflection.GeneratedProtocolMessageType('TokenBasedNormalizedSentence', (_message.Message,), {
  'DESCRIPTOR' : _TOKENBASEDNORMALIZEDSENTENCE,
  '__module__' : 'messages.tts_frontend_message_pb2'
  # @@protoc_insertion_point(class_scope:com.grammatek.tts_frontend.TokenBasedNormalizedSentence)
  })
_sym_db.RegisterMessage(TokenBasedNormalizedSentence)

RawNormalizedTokenInfo = _reflection.GeneratedProtocolMessageType('RawNormalizedTokenInfo', (_message.Message,), {
  'DESCRIPTOR' : _RAWNORMALIZEDTOKENINFO,
  '__module__' : 'messages.tts_frontend_message_pb2'
  # @@protoc_insertion_point(class_scope:com.grammatek.tts_frontend.RawNormalizedTokenInfo)
  })
_sym_db.RegisterMessage(RawNormalizedTokenInfo)

PreprocessRequest = _reflection.GeneratedProtocolMessageType('PreprocessRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREPROCESSREQUEST,
  '__module__' : 'messages.tts_frontend_message_pb2'
  # @@protoc_insertion_point(class_scope:com.grammatek.tts_frontend.PreprocessRequest)
  })
_sym_db.RegisterMessage(PreprocessRequest)

PreprocessedResponse = _reflection.GeneratedProtocolMessageType('PreprocessedResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREPROCESSEDRESPONSE,
  '__module__' : 'messages.tts_frontend_message_pb2'
  # @@protoc_insertion_point(class_scope:com.grammatek.tts_frontend.PreprocessedResponse)
  })
_sym_db.RegisterMessage(PreprocessedResponse)

PhonemeDescription = _reflection.GeneratedProtocolMessageType('PhonemeDescription', (_message.Message,), {
  'DESCRIPTOR' : _PHONEMEDESCRIPTION,
  '__module__' : 'messages.tts_frontend_message_pb2'
  # @@protoc_insertion_point(class_scope:com.grammatek.tts_frontend.PhonemeDescription)
  })
_sym_db.RegisterMessage(PhonemeDescription)

AbiVersionResponse = _reflection.GeneratedProtocolMessageType('AbiVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _ABIVERSIONRESPONSE,
  '__module__' : 'messages.tts_frontend_message_pb2'
  # @@protoc_insertion_point(class_scope:com.grammatek.tts_frontend.AbiVersionResponse)
  })
_sym_db.RegisterMessage(AbiVersionResponse)


# @@protoc_insertion_point(module_scope)
