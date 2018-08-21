import numpy as np
import argparse
import cv2

# Loading image and convert to grayscale
image = cv2.imread("wave.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Equalize image
eq = cv2.equalizeHist(image)
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))

cv2.waitKey(0)