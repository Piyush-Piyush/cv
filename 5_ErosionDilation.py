import cv2

import numpy as np


# Read the image

image = cv2.imread('5_ErosionDilation\input_image.jpg')


# Create a kernel for erosion and dilation
frame = np.ones((5,5))


# Perform erosion

erosion = cv2.erode(image, frame, iterations=1)


# Perform dilation

dilation = cv2.dilate(image, frame, iterations=1)


# Display the original, erosion, and dilation images

cv2.imshow('Original Image', image)

cv2.imshow('Erosion', erosion)

cv2.imshow('Dilation', dilation)


# Wait for a key press and close all windows

cv2.waitKey(0)

cv2.destroyAllWindows()

