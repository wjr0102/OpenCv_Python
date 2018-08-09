#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-08 11:22:53
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-08 12:19:02

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("1.png")
# Pixel values
px = img[100, 100]
print px

print img.item(100, 100, 2)
img.itemset((100, 100, 2), 100)
print img.item(100, 100, 2)

# Image properties
print img.shape
print img.size
print img.dtype

# Image ROI
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# copy = img[100:200, 100:200]
# img[0:100, 100:200] = copy
# cv2.imshow('Image2', img)
# cv2.waitKey(0)

# Splitting and Merging
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
# cv2.imshow('B', b)
# cv2.waitKey(0)
# cv2.imshow('G', g)
# cv2.waitKey(0)
# cv2.imshow('R', r)
# cv2.waitKey(0)
# img[:, :, 2] = 0
# cv2.imshow('Image3', img)
# cv2.waitKey(0)

# Borders
BLUE = [255, 0, 0]

img1 = cv2.imread("opencv_logo.png")
img1 = img1[256 - 85 - 90:256 + 85 + 90, 256 - 85 - 90:256 + 50 + 90]
'''	src
	top,bottom,left,right,  
	border type:
		BORDER_CONSTANT: constant colored border
		BORDER_REFLECT:	MIRROR REFLECTION OF THE BORDER ELEMENTS
		BORDER_REFLECT_101/ DEFAULT: SLIGHT CHANGE
		BORDER_WARP
'''
replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(
    img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()
