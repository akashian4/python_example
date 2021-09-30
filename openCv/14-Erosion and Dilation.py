import cv2
import numpy as np

image = cv2.imread('test.jpg')

kernel = np.ones((9,9))

img_erosion = cv2.erode(image, kernel)
img_dilation = cv2.dilate(image, kernel, iterations=1)  

cv2.imshow('Image Eroding', img_erosion)
cv2.imshow('Image Dilation', img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()