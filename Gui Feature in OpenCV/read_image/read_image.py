#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-06 12:22:11
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-07 13:14:03

import numpy as np
import cv2
from matplotlib import pyplot as plt


if __name__ == '__main__':
    # 0 is cv2.IMREAD_GRAYSCALE
    # 1(DEFAULT) is cv2.IMREAD_COLOR
    # -1 is cv2.IMREAD_UNCHANGED
    img = cv2.imread('1.png', 0)
    # cv2.namedWindow is to determine whether window is resizable or not
    #cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow(name,image)
    #cv2.imshow('image', img)

    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    # Wait x milliseconds for a key event
    k = cv2.waitKey(0)
    if k == 27:  # ESC
        # DestroyWindow() to destroy exact window
        cv2.destroyAllWindows()
    elif k == ord("s"):
        # cv2.imwrite(name, image)
        cv2.imwrite("1_copy.png", img)
