import numpy as np
import cv2

# Loading image
image = cv2.imread("coins.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Blurred", blurred)

# Canny edge detector
canny = cv2.Canny(blurred, 30, 150)
cv2.imshow("Canny", canny)

cv2.waitKey(0)