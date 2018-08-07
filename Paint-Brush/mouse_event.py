#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-07 15:58:57
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-07 16:36:01

import cv2
import numpy as np

drawing = False
mode = True
ix, iy = -1, -1

def draw_circle(event, x, y, flags, param):
	global ix, iy, drawing, mode
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			if mode == True:
				cv2.rectangle(img, (ix,iy),(x,y),(0,255,0),1)
			else:
				cv2.circle(img, (x,y), 5, (255,0,0),-1)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if mode == True:
			cv2.rectangle(img, (ix,iy),(x,y),(0,255,0),1)
		else:
			cv2.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_circle)

while (1):
	cv2.imshow('Image',img)
	key = cv2.waitKey(1) & 0xFF
	if key == ord('m'):
		mode = not mode
	elif key == 27:
		break

cv2.destroyAllWindows()