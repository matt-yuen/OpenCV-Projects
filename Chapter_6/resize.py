import numpy as np
import cv2
import argparse
import imutils

# Loading image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Computing the aspect ratio
r = 150.0 / image.shape[1] # New desired image width = 150
dim = (150, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

r2 = 50.0 / image.shape[0]
dim2 = (int(image.shape[1] * r2), 50)

resized2 = cv2.resize(image, dim2, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized2)

# Utilizing imutils functions
resized = imutils.resize(image, width = 100)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)