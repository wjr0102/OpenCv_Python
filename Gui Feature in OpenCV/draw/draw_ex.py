#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-07 15:10:42
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-07 15:47:37

import numpy as np
import cv2
import math

# Black image
img = np.full((512, 512, 3), 255, np.uint8)

cv2.circle(img, (256 - 85, 306), 60, (0, 255, 0), 40)
cv2.circle(img, (256, 156), 60, (0, 0, 255), 40)

pts = np.array([[256 - 85, 306], [256, 156], [256 + 85, 306]], np.int32)
#pts = pts.reshape(-1, 1, 2)
#cv2.polylines(img, [pts], True, (255, 255, 255))
cv2.fillPoly(img, [pts], (255, 255, 255), 1)
cv2.circle(img, (256 + 85, 306), 60, (255, 0, 0), 40)
cv2.ellipse(img, (256 + 85, 306), (100, 100), 240, 0, 60, (255, 255, 255), -1)
cv2.imshow('opencv logo', img)
key = cv2.waitKey(0)
if key == ord("q") or key == 27:
    cv2.destroyAllWindows()
elif key == ord("s"):
    cv2.imwrite('opencv log.png', img)
