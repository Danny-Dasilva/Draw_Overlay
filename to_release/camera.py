# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import threading
import numpy as np
import gstreamer
import pipelines

from gst import *
import os
import threading
from time import sleep
from CameraManager.TPUCameraManager import CameraManager, GStreamerPipelines
import numpy as np
from gst import *
camMan = CameraManager() #Creates new camera manager object
# USBCam = camMan.newCam(1) #Creates new RGB CSI-camera
CSICam = camMan.newCam(0)
# CV = USBCam.addPipeline(GStreamerPipelines.H264,(640,480),30,"CV") #Creates an RGB stream at 30 fps and 640x480 for openCV
AI = CSICam.addPipeline(GStreamerPipelines.H264,(640,480),30,"h264sink")
CV = CSICam.addPipeline(GStreamerPipelines.RGB,(320, 320),30,"CV")

CSICam.startPipeline() 

# USBCam.startPipeline()

class Camera:
    def __init__(self, model_res):
        #def __init__(self, render_size, inference_size, loop):
        # self._layout = gstreamer.make_layout(inference_size, render_size)
        # self._loop = loop
        self.model_res = model_res
        self._thread = None
        self.render_overlay = None

    @property
    def resolution(self):
        return [640, 480]

    def request_key_frame(self):
        pass

    def start_recording(self, obj, format, profile, inline_headers, bitrate, intra_period):
        #Start gstreamer Streams
        def on_buffer(data, _):
            
            obj.write(data)

        def render_overlay(tensor, layout, command):

            if self.render_overlay:
                print("ahhhhh")
                # if(CV):
                #     print("Camera Streaming")
                #     t = bytes(CV) #RGB Byte Stream that can be converted to a numpy array\
                #     print(np.frombuffer(t).shape, "tttttt")

                self.render_overlay(tensor, layout, command)
            return None
        
        objFunc = obj.write
        AI.addListener(objFunc)
        
        
        
    def stop_recording(self):
        raise NotImplemented

    def make_pipeline(self, fmt, profile, inline_headers, bitrate, intra_period):
        raise NotImplemented

# class FileCamera(Camera):
#     def __init__(self, filename, inference_size, loop):
#         info = gstreamer.get_video_info(filename)
#         super().__init__((info.get_width(), info.get_height()), inference_size,
#                           loop=loop)
#         self._filename = filename

#     def make_pipeline(self, fmt, profile, inline_headers, bitrate, intra_period):
#         return pipelines.video_streaming_pipeline(self._filename, self._layout)

# class DeviceCamera(Camera):
#     def __init__(self, fmt, inference_size):
#         super().__init__(fmt.size, inference_size, loop=False)
#         self._fmt = fmt

#     def make_pipeline(self, fmt, profile, inline_headers, bitrate, intra_period):
#         return pipelines.camera_streaming_pipeline(self._fmt, profile, bitrate, self._layout)

# def make_camera(source, inference_size, loop):
#     fmt = parse_format(source)
#     if fmt:
#         return DeviceCamera(fmt, inference_size)

#     filename = os.path.expanduser(source)
#     if os.path.isfile(filename):
#         return FileCamera(filename, inference_size, loop)

#     return None
