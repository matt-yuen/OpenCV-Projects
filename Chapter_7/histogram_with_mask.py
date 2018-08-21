from matplotlib import pyplot as plt
import numpy as np
import cv2

def plot_histogram(image, title, mask = None):
	chans = cv2.split(image)
	colors = ["b", "g", "r"]
	plt.figure()	
	plt.title(title)
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")

	for i in range(3):
		hist = cv2.calcHist([chans[i]], [0], mask, [256], [0, 256])
		plt.plot(hist, color = colors[i])
		plt.xlim([0, 256])

# Loading original image and histogram
image = cv2.imread("corgi.png")
cv2.imshow("Original", image)
plot_histogram(image, "Histogram for Original Image")

# Cropping image and creating histogram
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (160, 20), (400, 300), (255, 255, 255), -1)
maskedImage = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Masked Image", maskedImage)
plot_histogram(image, "Histogram for Masked Image", mask = mask)

plt.show()
cv2.waitKey(0)