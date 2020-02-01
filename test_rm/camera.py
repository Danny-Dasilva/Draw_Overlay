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
import gstreamer
from time import sleep
from TPUCameraManager.TPUCameraManager import CameraManager, GStreamerPipelines

from gst import *
camMan = CameraManager() #Creates new camera manager object
USBCam = camMan.newCam(1) #Creates new RGB CSI-camera
CSICam = camMan.newCam(0)
CV = USBCam.addPipeline(GStreamerPipelines.H264,(640,480),30,"CV") #Creates an RGB stream at 30 fps and 640x480 for openCV
AI = CSICam.addPipeline(GStreamerPipelines.H264,(640,480),30,"h264sink")

CSICam.startPipeline() #Start gstreamer Streams
USBCam.startPipeline()




class Camera:
    def __init__(self, render_size, loop):
        
        self._layout = gstreamer.make_layout(render_size)
        self._loop = loop
        self._thread = None
        self.render_overlay = None

    @property
    def resolution(self):
        return self._layout.render_size

    def request_key_frame(self):
        pass

    def start_recording(self, obj, format, profile, inline_headers, bitrate, intra_period):
        # global AI 
        def on_buffer(data, _):
            obj.write(data)

     
        objFunc = obj.write
        AI.addListener(objFunc)

    def start_recording1(self, obj, format, profile, inline_headers, bitrate, intra_period):
        # global AI
        def on_buffer(data, _):
            print(data, "ahh")
            #obj.write1(data)

   
        objFunc = obj.write1
        CV.addListener(objFunc)
  


class DeviceCamera(Camera):
    def __init__(self, fmt):
        super().__init__(fmt.size, loop=False)
        self._fmt = fmt

    def make_pipeline(self, fmt, profile, inline_headers, bitrate, intra_period):
        return pipelines.camera_streaming_pipeline(self._fmt, profile, bitrate, self._layout)

def make_camera(source):
    fmt = parse_format(source)
    
    if fmt:
        return DeviceCamera(fmt)

    

    return None
