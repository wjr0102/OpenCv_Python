#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-08 12:49:52
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-08 16:07:49

import cv2

# Blending: Must of the same size
img1 = cv2.imread("1.png")
img2 = cv2.imread("opencv_logo.png")
img3 = cv2.resize(img2, (320, 240))
print img1.shape,img3.shape

dst = cv2.addWeighted(img1, 0.7, img3, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bitwise
img1 = cv2.imread("1.png")
img2 = cv2.imread("opencv_logo.png")
img3 = cv2.resize(img2, (50, 50))
rows,cols,channels = img3.shape
roi = img1[0:rows,0:cols]

# Create a mask of logo and create is inverse mask
img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
cv2.imshow('img2gray',img2gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Input: the gray image 
ret, mask = cv2.threshold(img2gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv',mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Block-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
cv2.imshow('img1_bg',img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Take only region of logo from logo image
img3_fg = cv2.bitwise_and(img3,img3,mask = mask_inv)
cv2.imshow('img3_bg',img3_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img3_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()