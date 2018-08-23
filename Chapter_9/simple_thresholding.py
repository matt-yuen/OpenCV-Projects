import numpy as np
import cv2

# Loading image
image = cv2.imread("coins.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Blurred Image", blurred)

(T, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

(T, threshInv) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

coins = cv2.bitwise_and(image, image, mask = threshInv)
cv2.imshow("Coins", coins)

cv2.waitKey(0)