import numpy as np
import argparse
import imutils
import cv2

# Loading image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Defining translation matrix
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

M2 = np.float32([[1, 0, -50], [0, 1, -90]])
shifted2 = cv2.warpAffine(image, M2, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted2)

# Utilizing imutils for convenience
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)