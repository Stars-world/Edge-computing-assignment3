#!/usr/bin/python3
#
# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#

from operator import truediv
import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
# camera = jetson.utils.videoSource("csi://0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file

# while display.IsStreaming():
# 	img = camera.Capture()
# 	detections = net.Detect(img)
# 	display.Render(img)
# 	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
image = jetson.utils.loadImage("test.jpg")
detections = net.Detect(image)
# print(detections)
for detection in detections:
    print('detections:',detection)
if detections:
    for i,detection in enumerate(detections):
        print(f"Dectection{i+1}:")
        for attr in dir(detection):
            if not attr.startswith("__"):
                value = getattr(detection,attr)
                print(f" {attr}: {value}")
else:
    print("No detections found.")
jetson.utils.saveImage('test_result.jpg',image)
while display.IsStreaming():
    display.Render(image)