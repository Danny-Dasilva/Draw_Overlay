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
from time import sleep
from gst import *
import os
import threading
from time import sleep
from CameraManager.TPUCameraManager import CameraManager, GStreamerPipelines
import numpy as np
from gst import *
camMan = CameraManager() #Creates new camera manager object

CSICam = camMan.newCam(0)
#
H264 = CSICam.addPipeline(GStreamerPipelines.H264,(640,480),30,"h264sink")
AI = CSICam.addPipeline(GStreamerPipelines.RGB,(320, 320),30,"AI")

CSICam.startPipeline() 
if os.path.exists('/dev/video1'):
    USBCam = camMan.newCam(1) #Creates new RGB CSI-camera
    SB = USBCam.addPipeline(GStreamerPipelines.H264,(640,480),30,"usb_cam") #Creates an RGB stream at 30 fps and 640x480 for openCV
    USBCam.startPipeline()
else:
    USBCam = None
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
        
        objFunc = obj.write
        H264.addListener(objFunc)

        if USBCam is not None:

            objFunc = obj.write_usb
            SB.addListener(objFunc)



        self._thread = threading.Thread(target=self.ai_stream)
        self._thread.start()


        
        
    def ai_stream(self):
            while True:
                if self.render_overlay:
                    tensor = np.frombuffer(bytes(AI),dtype=np.uint8)
                    layout = None
                    command = None
                    self.render_overlay(tensor, layout, command)
                sleep(.03)
    def stop_recording(self):
        raise NotImplemented

    def make_pipeline(self, fmt, profile, inline_headers, bitrate, intra_period):
        raise NotImplemented

