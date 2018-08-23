from __future__ import print_function
import cv2
import mahotas

# Loading image
image = cv2.imread("coins.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Image", image)

# Otsu's method
T = mahotas.thresholding.otsu(blurred)
print("Otsu's calculated threshold: {}".format(T))

thresh = gray.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

# Riddler-Calvard's method
T = mahotas.thresholding.rc(blurred)
print("RC's calculated threshold: {}".format(T))

thresh = gray.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("RC", thresh)

cv2.waitKey(0)