#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-08 12:49:52
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-08 12:53:27

import cv2

img1 = cv2.imread("../images/1.png")
img2 = cv2.imread("../images/opencv_logo.png")
cv2.imshow('dst', img1)

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
