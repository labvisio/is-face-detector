# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: options.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from is_msgs import validate_pb2 as is__msgs_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\roptions.proto\x12\x02is\x1a\x16is_msgs/validate.proto\"\xa7\x01\n\x05Model\x12\x0c\n\x04path\x18\x01 \x01(\t\x12)\n\x0e\x63onf_threshold\x18\x02 \x01(\x02\x42\x11\xba\xe9\xc0\x03\x0c\n\n\x1d\x00\x00\x80?-\x00\x00\x00\x00\x12(\n\rnms_threshold\x18\x03 \x01(\x02\x42\x11\xba\xe9\xc0\x03\x0c\n\n\x1d\x00\x00\x80?-\x00\x00\x00\x00\x12!\n\x05top_k\x18\x04 \x01(\x05\x42\x12\xba\xe9\xc0\x03\r\x1a\x0b(\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x0b\n\x03gpu\x18\x05 \x01(\x08\x12\x0b\n\x03\x66\x31\x36\x18\x06 \x01(\x08\"W\n\x13\x46\x61\x63\x65\x44\x65tectorOptions\x12\x12\n\nbroker_uri\x18\x01 \x01(\t\x12\x12\n\nzipkin_uri\x18\x02 \x01(\t\x12\x18\n\x05model\x18\x03 \x01(\x0b\x32\t.is.Modelb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'options_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MODEL.fields_by_name['conf_threshold']._options = None
  _MODEL.fields_by_name['conf_threshold']._serialized_options = b'\272\351\300\003\014\n\n\035\000\000\200?-\000\000\000\000'
  _MODEL.fields_by_name['nms_threshold']._options = None
  _MODEL.fields_by_name['nms_threshold']._serialized_options = b'\272\351\300\003\014\n\n\035\000\000\200?-\000\000\000\000'
  _MODEL.fields_by_name['top_k']._options = None
  _MODEL.fields_by_name['top_k']._serialized_options = b'\272\351\300\003\r\032\013(\377\377\377\377\377\377\377\377\377\001'
  _MODEL._serialized_start=46
  _MODEL._serialized_end=213
  _FACEDETECTOROPTIONS._serialized_start=215
  _FACEDETECTOROPTIONS._serialized_end=302
# @@protoc_insertion_point(module_scope)
