from __future__ import print_function
import numpy as np
import cv2

# Loading image
image = cv2.imread("coins2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
# cv2.imshow("Image", blurred)

# Finding edges
edged = cv2.Canny(blurred, 5, 250)
cv2.imshow("Edges", edged)

# Finding contours
(_, contours, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("There are {} coins in this image".format(len(contours)))

# Drawing contours
coins = image.copy()
cv2.drawContours(coins, contours, -1, (0, 0, 255), 5)
cv2.imshow("Coins", coins)

# Cropping coins
for (i, c) in enumerate(contours):
	(x, y, w, h) = cv2.boundingRect(c)

	# Cropping coin as rectangle
	print("Coin #{}".format(i + 1))
	coin = image[y:y + h, x:x + w]
	cv2.imshow("Coin", coin)

	# Cropping coin as circle
	mask = np.zeros(image.shape[:2], dtype = "uint8")
	((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
	cv2.circle(mask, (int(centerX), int(centerY), int(radius), 255, -1))
	mask = mask[y:y + h, x:x + w]
	cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))
	cv2.waitKey(0)

cv2.waitKey(0)