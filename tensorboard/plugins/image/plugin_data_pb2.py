# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/plugins/image/plugin_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/plugins/image/plugin_data.proto',
  package='tensorboard',
  syntax='proto3',
  serialized_pb=_b('\n+tensorboard/plugins/image/plugin_data.proto\x12\x0btensorboard\"\"\n\x0fImagePluginData\x12\x0f\n\x07version\x18\x01 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IMAGEPLUGINDATA = _descriptor.Descriptor(
  name='ImagePluginData',
  full_name='tensorboard.ImagePluginData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='tensorboard.ImagePluginData.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['ImagePluginData'] = _IMAGEPLUGINDATA

ImagePluginData = _reflection.GeneratedProtocolMessageType('ImagePluginData', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEPLUGINDATA,
  __module__ = 'tensorboard.plugins.image.plugin_data_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.ImagePluginData)
  ))
_sym_db.RegisterMessage(ImagePluginData)


# @@protoc_insertion_point(module_scope)
