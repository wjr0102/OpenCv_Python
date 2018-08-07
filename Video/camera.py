#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-07 13:36:38
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-07 14:53:44

import cv2
import numpy
import matplotlib.pyplot as plot

# index or the name of a video file
cap = cv2.VideoCapture(0)

# VideoWriter
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
# filename, fourcc code, fps, size
out = cv2.VideoWriter('output.m4v', fourcc, 30.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (640, 480))
        out.write(frame)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
