import cv2

from matplotlib import pyplot as plt

img = cv2.imread("test.jpg")

##hist = cv2.calcHist([img], [0], None, [256], [0,256])
##plt.plot(hist)

plt.hist(img.ravel(), 256, [0,256])
plt.show()
