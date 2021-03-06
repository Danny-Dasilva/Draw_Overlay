# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0emessages.proto\"B\n\x0bServerBound\x12(\n\x0estream_control\x18\x01 \x01(\x0b\x32\x0e.StreamControlH\x00\x42\t\n\x07message\" \n\rStreamControl\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"\xa9\x01\n\x0b\x43lientBound\x12\x17\n\x05start\x18\x01 \x01(\x0b\x32\x06.StartH\x00\x12\x15\n\x04stop\x18\x02 \x01(\x0b\x32\x05.StopH\x00\x12\x17\n\x05video\x18\x03 \x01(\x0b\x32\x06.VideoH\x00\x12\x1b\n\x07overlay\x18\x04 \x01(\x0b\x32\x08.OverlayH\x00\x12\x13\n\x03usb\x18\x05 \x01(\x0b\x32\x04.UsbH\x00\x12\x14\n\x0ctimestamp_us\x18\n \x01(\x04\x42\t\n\x07message\"&\n\x05Start\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\"\x06\n\x04Stop\"\x15\n\x05Video\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x16\n\x07Overlay\x12\x0b\n\x03svg\x18\x01 \x01(\t\"\x13\n\x03Usb\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x62\x06proto3')
)




_SERVERBOUND = _descriptor.Descriptor(
  name='ServerBound',
  full_name='ServerBound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_control', full_name='ServerBound.stream_control', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='ServerBound.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=18,
  serialized_end=84,
)


_STREAMCONTROL = _descriptor.Descriptor(
  name='StreamControl',
  full_name='StreamControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='StreamControl.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=86,
  serialized_end=118,
)


_CLIENTBOUND = _descriptor.Descriptor(
  name='ClientBound',
  full_name='ClientBound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='ClientBound.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='ClientBound.stop', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video', full_name='ClientBound.video', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overlay', full_name='ClientBound.overlay', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usb', full_name='ClientBound.usb', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_us', full_name='ClientBound.timestamp_us', index=5,
      number=10, type=4, cpp_type=4, label=1,
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
    _descriptor.OneofDescriptor(
      name='message', full_name='ClientBound.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=121,
  serialized_end=290,
)


_START = _descriptor.Descriptor(
  name='Start',
  full_name='Start',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='Start.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='Start.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=292,
  serialized_end=330,
)


_STOP = _descriptor.Descriptor(
  name='Stop',
  full_name='Stop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=332,
  serialized_end=338,
)


_VIDEO = _descriptor.Descriptor(
  name='Video',
  full_name='Video',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Video.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=340,
  serialized_end=361,
)


_OVERLAY = _descriptor.Descriptor(
  name='Overlay',
  full_name='Overlay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='svg', full_name='Overlay.svg', index=0,
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
  serialized_start=363,
  serialized_end=385,
)


_USB = _descriptor.Descriptor(
  name='Usb',
  full_name='Usb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Usb.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=387,
  serialized_end=406,
)

_SERVERBOUND.fields_by_name['stream_control'].message_type = _STREAMCONTROL
_SERVERBOUND.oneofs_by_name['message'].fields.append(
  _SERVERBOUND.fields_by_name['stream_control'])
_SERVERBOUND.fields_by_name['stream_control'].containing_oneof = _SERVERBOUND.oneofs_by_name['message']
_CLIENTBOUND.fields_by_name['start'].message_type = _START
_CLIENTBOUND.fields_by_name['stop'].message_type = _STOP
_CLIENTBOUND.fields_by_name['video'].message_type = _VIDEO
_CLIENTBOUND.fields_by_name['overlay'].message_type = _OVERLAY
_CLIENTBOUND.fields_by_name['usb'].message_type = _USB
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['start'])
_CLIENTBOUND.fields_by_name['start'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['stop'])
_CLIENTBOUND.fields_by_name['stop'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['video'])
_CLIENTBOUND.fields_by_name['video'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['overlay'])
_CLIENTBOUND.fields_by_name['overlay'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['usb'])
_CLIENTBOUND.fields_by_name['usb'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
DESCRIPTOR.message_types_by_name['ServerBound'] = _SERVERBOUND
DESCRIPTOR.message_types_by_name['StreamControl'] = _STREAMCONTROL
DESCRIPTOR.message_types_by_name['ClientBound'] = _CLIENTBOUND
DESCRIPTOR.message_types_by_name['Start'] = _START
DESCRIPTOR.message_types_by_name['Stop'] = _STOP
DESCRIPTOR.message_types_by_name['Video'] = _VIDEO
DESCRIPTOR.message_types_by_name['Overlay'] = _OVERLAY
DESCRIPTOR.message_types_by_name['Usb'] = _USB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerBound = _reflection.GeneratedProtocolMessageType('ServerBound', (_message.Message,), dict(
  DESCRIPTOR = _SERVERBOUND,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ServerBound)
  ))
_sym_db.RegisterMessage(ServerBound)

StreamControl = _reflection.GeneratedProtocolMessageType('StreamControl', (_message.Message,), dict(
  DESCRIPTOR = _STREAMCONTROL,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:StreamControl)
  ))
_sym_db.RegisterMessage(StreamControl)

ClientBound = _reflection.GeneratedProtocolMessageType('ClientBound', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBOUND,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ClientBound)
  ))
_sym_db.RegisterMessage(ClientBound)

Start = _reflection.GeneratedProtocolMessageType('Start', (_message.Message,), dict(
  DESCRIPTOR = _START,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Start)
  ))
_sym_db.RegisterMessage(Start)

Stop = _reflection.GeneratedProtocolMessageType('Stop', (_message.Message,), dict(
  DESCRIPTOR = _STOP,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Stop)
  ))
_sym_db.RegisterMessage(Stop)

Video = _reflection.GeneratedProtocolMessageType('Video', (_message.Message,), dict(
  DESCRIPTOR = _VIDEO,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Video)
  ))
_sym_db.RegisterMessage(Video)

Overlay = _reflection.GeneratedProtocolMessageType('Overlay', (_message.Message,), dict(
  DESCRIPTOR = _OVERLAY,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Overlay)
  ))
_sym_db.RegisterMessage(Overlay)

Usb = _reflection.GeneratedProtocolMessageType('Usb', (_message.Message,), dict(
  DESCRIPTOR = _USB,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Usb)
  ))
_sym_db.RegisterMessage(Usb)


# @@protoc_insertion_point(module_scope)