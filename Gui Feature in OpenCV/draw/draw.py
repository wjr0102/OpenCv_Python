#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-07 14:56:45
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-07 15:09:49

import numpy as np
import cv2

# Black image
img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

cv2.circle(img, (477, 63), 63, (0, 0, 255), 1)

cv2.ellipse(img, (256, 256), (100, 50), 90, 0, 360, (125, 100, 12), -1)

pts = np.array([[100, 50], [200, 300], [170, 120], [310, 110]], np.int32)
pts = pts.reshape((-1, 1, 2))
print pts
cv2.polylines(img, [pts], True, (0, 255, 255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'W', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_4)

cv2.imshow('image', img)
cv2.waitKey(0)
