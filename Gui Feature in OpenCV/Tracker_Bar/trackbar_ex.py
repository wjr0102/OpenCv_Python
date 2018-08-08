#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-07 17:03:14
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-07 17:25:05

import cv2
import numpy as np

#r, g, b = 0, 0, 0
ix, iy = -1, -1
drawing = False


def foo(x):
    pass


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing
    print r, g, b, radius
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img, (x, y), radius, (r, g, b), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Draw')

cv2.setMouseCallback('Draw', draw_circle)

cv2.createTrackbar('R', 'Draw', 0, 255, foo)
cv2.createTrackbar('G', 'Draw', 0, 255, foo)
cv2.createTrackbar('B', 'Draw', 0, 255, foo)

brush = "Bruch Radius"
cv2.createTrackbar(brush, 'Draw', 1, 100, foo)

while (1):
    cv2.imshow('Draw', img)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

    r = cv2.getTrackbarPos('R', 'Draw')
    g = cv2.getTrackbarPos('G', 'Draw')
    b = cv2.getTrackbarPos('B', 'Draw')

    radius = cv2.getTrackbarPos(brush, 'Draw')

cv2.destroyAllWindows()
