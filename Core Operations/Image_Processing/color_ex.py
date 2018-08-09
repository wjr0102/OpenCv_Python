#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-08 17:18:21
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-08 17:42:32

import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while(1):
    _, frame = cap.read()
    frame = cv2.resize(frame, (200, 200))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])
    lower_green = np.array([50, 100, 100])
    upper_green = np.array([60, 255, 255])
    lower_red = np.array([-10, 100, 100])
    upper_red = np.array([10, 255, 255])

    # 1-bit
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.bitwise_or(mask_blue, mask_green, mask_red)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask_blue', mask_blue)
    cv2.imshow('mask_red', mask_red)
    cv2.imshow('mask_green', mask_green)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
