import numpy as np
import cv2
import argparse

# Loading image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Cropping the face of the corgi
cropped = image[20:300, 160:400]
cv2.imshow("Corgi Face", cropped)

cv2.waitKey(0)