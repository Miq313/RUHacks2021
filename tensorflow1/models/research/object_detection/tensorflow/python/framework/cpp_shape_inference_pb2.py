# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/python/framework/cpp_shape_inference.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2
from tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/python/framework/cpp_shape_inference.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=_b('Z\\github.com/tensorflow/tensorflow/tensorflow/go/python/framework/cpp_shape_inference_go_proto\370\001\001'),
  serialized_pb=_b('\n5tensorflow/python/framework/cpp_shape_inference.proto\x12\ntensorflow\x1a%tensorflow/core/framework/types.proto\x1a,tensorflow/core/framework/tensor_shape.proto\"\xa5\x03\n\x17\x43ppShapeInferenceResult\x12+\n\x05shape\x18\x01 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12\x43\n\x0bhandle_data\x18\x04 \x01(\x0b\x32..tensorflow.CppShapeInferenceResult.HandleData\x1a\x9d\x01\n\x12HandleShapeAndType\x12+\n\x05shape\x18\x01 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12#\n\x05\x64type\x18\x02 \x01(\x0e\x32\x14.tensorflow.DataType\x12\x35\n\x10specialized_type\x18\x03 \x01(\x0e\x32\x1b.tensorflow.SpecializedType\x1al\n\nHandleData\x12\x0e\n\x06is_set\x18\x01 \x01(\x08\x12N\n\x0eshape_and_type\x18\x02 \x03(\x0b\x32\x36.tensorflow.CppShapeInferenceResult.HandleShapeAndTypeJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04\"e\n\x1d\x43ppShapeInferenceInputsNeeded\x12\x1c\n\x14input_tensors_needed\x18\x01 \x03(\x05\x12&\n\x1einput_tensors_as_shapes_needed\x18\x02 \x03(\x05\x42\x61Z\\github.com/tensorflow/tensorflow/tensorflow/go/python/framework/cpp_shape_inference_go_proto\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,])




_CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE = _descriptor.Descriptor(
  name='HandleShapeAndType',
  full_name='tensorflow.CppShapeInferenceResult.HandleShapeAndType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorflow.CppShapeInferenceResult.HandleShapeAndType.shape', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tensorflow.CppShapeInferenceResult.HandleShapeAndType.dtype', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='specialized_type', full_name='tensorflow.CppShapeInferenceResult.HandleShapeAndType.specialized_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=297,
  serialized_end=454,
)

_CPPSHAPEINFERENCERESULT_HANDLEDATA = _descriptor.Descriptor(
  name='HandleData',
  full_name='tensorflow.CppShapeInferenceResult.HandleData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_set', full_name='tensorflow.CppShapeInferenceResult.HandleData.is_set', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape_and_type', full_name='tensorflow.CppShapeInferenceResult.HandleData.shape_and_type', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=456,
  serialized_end=564,
)

_CPPSHAPEINFERENCERESULT = _descriptor.Descriptor(
  name='CppShapeInferenceResult',
  full_name='tensorflow.CppShapeInferenceResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorflow.CppShapeInferenceResult.shape', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='handle_data', full_name='tensorflow.CppShapeInferenceResult.handle_data', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE, _CPPSHAPEINFERENCERESULT_HANDLEDATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=576,
)


_CPPSHAPEINFERENCEINPUTSNEEDED = _descriptor.Descriptor(
  name='CppShapeInferenceInputsNeeded',
  full_name='tensorflow.CppShapeInferenceInputsNeeded',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_tensors_needed', full_name='tensorflow.CppShapeInferenceInputsNeeded.input_tensors_needed', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_tensors_as_shapes_needed', full_name='tensorflow.CppShapeInferenceInputsNeeded.input_tensors_as_shapes_needed', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=578,
  serialized_end=679,
)

_CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE.fields_by_name['shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE.fields_by_name['dtype'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE.fields_by_name['specialized_type'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._SPECIALIZEDTYPE
_CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE.containing_type = _CPPSHAPEINFERENCERESULT
_CPPSHAPEINFERENCERESULT_HANDLEDATA.fields_by_name['shape_and_type'].message_type = _CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE
_CPPSHAPEINFERENCERESULT_HANDLEDATA.containing_type = _CPPSHAPEINFERENCERESULT
_CPPSHAPEINFERENCERESULT.fields_by_name['shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_CPPSHAPEINFERENCERESULT.fields_by_name['handle_data'].message_type = _CPPSHAPEINFERENCERESULT_HANDLEDATA
DESCRIPTOR.message_types_by_name['CppShapeInferenceResult'] = _CPPSHAPEINFERENCERESULT
DESCRIPTOR.message_types_by_name['CppShapeInferenceInputsNeeded'] = _CPPSHAPEINFERENCEINPUTSNEEDED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CppShapeInferenceResult = _reflection.GeneratedProtocolMessageType('CppShapeInferenceResult', (_message.Message,), {

  'HandleShapeAndType' : _reflection.GeneratedProtocolMessageType('HandleShapeAndType', (_message.Message,), {
    'DESCRIPTOR' : _CPPSHAPEINFERENCERESULT_HANDLESHAPEANDTYPE,
    '__module__' : 'tensorflow.python.framework.cpp_shape_inference_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.CppShapeInferenceResult.HandleShapeAndType)
    })
  ,

  'HandleData' : _reflection.GeneratedProtocolMessageType('HandleData', (_message.Message,), {
    'DESCRIPTOR' : _CPPSHAPEINFERENCERESULT_HANDLEDATA,
    '__module__' : 'tensorflow.python.framework.cpp_shape_inference_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.CppShapeInferenceResult.HandleData)
    })
  ,
  'DESCRIPTOR' : _CPPSHAPEINFERENCERESULT,
  '__module__' : 'tensorflow.python.framework.cpp_shape_inference_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.CppShapeInferenceResult)
  })
_sym_db.RegisterMessage(CppShapeInferenceResult)
_sym_db.RegisterMessage(CppShapeInferenceResult.HandleShapeAndType)
_sym_db.RegisterMessage(CppShapeInferenceResult.HandleData)

CppShapeInferenceInputsNeeded = _reflection.GeneratedProtocolMessageType('CppShapeInferenceInputsNeeded', (_message.Message,), {
  'DESCRIPTOR' : _CPPSHAPEINFERENCEINPUTSNEEDED,
  '__module__' : 'tensorflow.python.framework.cpp_shape_inference_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.CppShapeInferenceInputsNeeded)
  })
_sym_db.RegisterMessage(CppShapeInferenceInputsNeeded)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
