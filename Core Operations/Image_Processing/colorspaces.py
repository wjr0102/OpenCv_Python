#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-08 16:20:03
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-08 17:26:31

import cv2
import numpy as np

# To see the color spaces
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags

'''

Take each frame of the video
Convert from BGR to HSV color-space
We threshold the HSV image for a range of blue color
Now extract the blue object alone

'''

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # 1-bit
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()

'''
	Find the HSV you want:
	green = np.uint8([[[0,255,0 ]]])
	hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
	print hsv_green
	[[[ 60 255 255]]]
'''
