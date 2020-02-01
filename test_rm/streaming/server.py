import contextlib

import logging
import queue
import struct
import threading
import time
from time import sleep
from itertools import cycle
from enum import Enum

from .proto import messages_pb2 as pb2


class NAL:
    CODED_SLICE_NON_IDR = 1  # Coded slice of a non-IDR picture
    CODED_SLICE_IDR     = 5  # Coded slice of an IDR picture
    SEI                 = 6  # Supplemental enhancement information (SEI)
    SPS                 = 7  # Sequence parameter set
    PPS                 = 8  # Picture parameter set

ALLOWED_NALS = {NAL.CODED_SLICE_NON_IDR,
                NAL.CODED_SLICE_IDR,
                NAL.SPS,
                NAL.PPS,
                NAL.SEI}

def StartMessage(resolution):
    
    width, height = resolution
    return pb2.ClientBound(timestamp_us=int(time.monotonic() * 1000000),
                           start=pb2.Start(width=width, height=height))

def StopMessage():
    return pb2.ClientBound(timestamp_us=int(time.monotonic() * 1000000),
                           stop=pb2.Stop())

def VideoMessage(data):
    return pb2.ClientBound(timestamp_us=int(time.monotonic() * 1000000),
                           video=pb2.Video(data=data))

def OverlayMessage(svg):
    return pb2.ClientBound(timestamp_us=int(time.monotonic() * 1000000),
                           overlay=pb2.Overlay(svg=svg))



class StreamingServer:
    def __enter__(self):
        pass
    def __exit__(self):
        pass
    def __init__(self, camera, q, qu, bitrate=1000000,):
        self._bitrate = bitrate
        self._camera = camera
        self.q = q
        self.qu = qu
        self._commands = queue.Queue()
        self.client = Clientt(self._commands, self._camera.resolution, self.q, self.qu)
        self._start_recording()


  

    def _start_recording(self):
        self._camera.start_recording(self, format='h264', profile='baseline',
            inline_headers=True, bitrate=self._bitrate, intra_period=0)
        self._camera.start_recording1(self, format='h264', profile='baseline',
            inline_headers=True, bitrate=self._bitrate, intra_period=0)



    def write(self, data):
        """Called by camera thread for each compressed frame."""
        assert data[0:4] == b'\x00\x00\x00\x01'
        frame_type = data[4] & 0b00011111
        if frame_type in ALLOWED_NALS:
            
            states = self.client.send_video(frame_type, data)
    def write1(self, data):
        print(len(data))
        
        """Called by camera thread for each compressed frame."""
        assert data[0:4] == b'\x00\x00\x00\x01'
        frame_type = data[4] & 0b00011111
        if frame_type in ALLOWED_NALS:
            
            pass
            states = self.client.send_video1(frame_type, data)

    


class ClientState(Enum):
    DISABLED = 1
    ENABLED_NEEDS_SPS = 2
    ENABLED = 3

class ClientCommand(Enum):
    STOP = 1
    ENABLE = 2
    DISABLE = 3

class Clientt:
    def __init__(self, command_queue, resolution, q, qu):
        self._lock = threading.Lock()
        self._commands = command_queue
        self.q = q
        self.qu = qu
        self._resolution = resolution
        message = StartMessage([640, 480])
        packet = self.WsPacket()
        packet.append(message.SerializeToString())
        buf = packet.serialize()
        self.q.put(buf)
        self.qu.put(buf)
    class WsPacket:
        def __init__(self):
            self.fin = True
            self.opcode = 2
            self.masked = False
            self.mask = None
            self.length = 0
            self.payload = bytearray()

        def append(self, data):
            if self.masked:
                data = bytes([c ^ k for c, k in zip(data, cycle(self.mask))])
            self.payload.extend(data)

        def serialize(self):
            self.length = len(self.payload)
            buf = bytearray()
            b0 = 0
            b1 = 0
            if self.fin:
                b0 |= 0x80
            b0 |= self.opcode
            buf.append(b0)
            if self.length <= 125:
                b1 |= self.length
                buf.append(b1)
            elif self.length >= 126 and self.length <= 65535:
                b1 |= 126
                buf.append(b1)
                buf.extend(struct.pack('!H', self.length))
            else:
                b1 |= 127
                buf.append(b1)
                buf.extend(struct.pack('!Q', self.length))
            if self.payload:
                buf.extend(self.payload)
            return bytes(buf)

    def send_video(self, frame_type, data):
        message = VideoMessage(data)
        packet = self.WsPacket()
        packet.append(message.SerializeToString())
        buf = packet.serialize()
        self.q.put(buf)
        return None
    def send_video1(self, frame_type, data):
        message = VideoMessage(data)
        packet = self.WsPacket()
        packet.append(message.SerializeToString())
        buf = packet.serialize()
        print(len(buf), " len")
        self.qu.put(buf)
        return None

  