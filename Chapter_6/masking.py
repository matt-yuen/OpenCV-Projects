import numpy as np
import cv2
import argparse

# Loading image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Creating the mask for the corgi's face
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (160, 20), (400, 300), (255, 255, 255), -1)
cv2.imshow("Mask", mask)

# Applying the mask using bitwise and operator
maskedImage = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Applying the Mask", maskedImage)

cv2.waitKey(0)

# Repeating with a different shape
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (mask.shape[1] // 2, mask.shape[0] // 2), 100, (255, 255, 255), -1)
cv2.imshow("Mask", mask)

maskedImage = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Applying the Mask", maskedImage)

cv2.waitKey(0)