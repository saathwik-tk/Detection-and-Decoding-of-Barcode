# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 08:36:27 2022

@author: bhimr
"""

#importing the required modules
import numpy as np
#import argparse
import imutils
import cv2
from pyzbar import pyzbar

#reading the image from disk
image = cv2.imread("qr1.jpeg")

#since the most of our operations on image requires gray scale version of original image
#colored image--> 3 bytes per pixel and grayscale image--> 1 byte per pixel
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#calculation of desired depth which is used while calculating gradient
#depth represents the  "precision" of each pixel interms of number of bits used per pixel
#CV_32F --> 32 BIT floating point datatype
if imutils.is_cv2():
    ddepth =cv2.cv.CV_32F 
    
else:
    ddepth =cv2.CV_32F


#calculating gradient(first order) in x direction using sobel high pass filter with kernel size equals to 3
gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
cv2.imshow("gradient in x direction", cv2.resize(gradX,None,fx=3, fy=3, interpolation = cv2.INTER_LINEAR))

#calculating gradient(first order) in y direction using sobel high pass filter or sobel operator with kernel size equals to 3
gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)
cv2.imshow("gradient in y direction", cv2.resize(gradY,None,fx=3, fy=3, interpolation = cv2.INTER_LINEAR))

#subtract the gradient and get absolute value of gradient which gives rough estimate of edge detection
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)
cv2.imshow("absgradient", cv2.resize(gradient,None,fx=3, fy=3, interpolation = cv2.INTER_LINEAR))

#blurr the image and use this for threshold calculation where we use threshold type of binary 
#value of pixel below 225 is considered to be zero(black) and above to be considered as 255(white)
blurred = cv2.blur(gradient, (9, 9))
(_, thresh) = cv2.threshold(blurred, 235, 255, cv2.THRESH_BINARY)
cv2.imshow("after applying threshold", cv2.resize(thresh,None,fx=3, fy=3, interpolation = cv2.INTER_LINEAR))

#prepare the kernel for morphological operations and apply closed operation which is dilation followed by erosion 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow("after applying closer operations", cv2.resize(closed,None,fx=3, fy=3, interpolation = cv2.INTER_LINEAR))

#apply series of morphological operations to get image which is free from white noise so that boundary can be drawn across barcode
closed = cv2.erode(closed, None, iterations = 7)
closed = cv2.dilate(closed, None, iterations = 7)
cv2.imshow("after applying morphological operations", cv2.resize(closed,None,fx=3, fy=3, interpolation = cv2.INTER_LINEAR))

#finding the contours in which retrival mode used is external which will only return the eldest one family hireachy
contours = cv2.findContours(closed, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

#sort the contours to get proper contour which will represent the barcode region
c = sorted(contours, key = cv2.contourArea, reverse = True)[0]


#get the midpoint,height,width of rectangle and next using this information we will find four coordinates of rectangle
rect = cv2.minAreaRect(c)
box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
box = np.int0(box)

#draw the contour around the barcode region using red line 
cv2.drawContours(image, [box], -1, (0,0,255), 1)

#crop the image so that cropped iamge contains the barcode and given this image to decoding module will decode the barcode
crop_img = image[box[0][1]:box[2][1], box[0][0]:box[1][0]]

image = cv2.resize(image,None,fx=3, fy=3, interpolation = cv2.INTER_LINEAR)
cv2.imshow("detected image in entire picture", image)

cv2.waitKey(0)

