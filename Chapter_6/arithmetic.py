from __future__ import print_function
import cv2
import argparse
import numpy as np

# Loading image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

first = np.uint8([50])
second = np.uint8([100])
third = np.uint8([200])

# Showcasing OpenCV's clipping arithmetic
print("----- OpenCV Arithmetic -----")
print("max of 255: {}".format(cv2.add(second, third)))
print("min of 0: {}".format(cv2.subtract(first, second)))

# Showcasing NumPy's wrapping arithmetic
print("----- NumPy Arithmetic -----")
print("wrap around: {}".format(second + third))
print("wrap around: {}".format(first - second))

M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)