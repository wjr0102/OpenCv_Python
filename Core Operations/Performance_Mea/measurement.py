#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-08 16:11:13
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-08 16:19:07

import cv2

img1 = cv2.imread("1.png")

e1 = cv2.getTickCount()
for i in xrange(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)

e2 = cv2.getTickCount()
time = (e2 - e1) / cv2.getTickFrequency()
print time

'''
	cv2.useOptimized()
	
'''