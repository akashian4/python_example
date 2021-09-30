import numpy as np
import cv2

image = cv2.imread('test.jpg')

B, G, R = cv2.split(image)

cv2.imshow("Original", image)

cv2.imshow("Blue", B)

cv2.imshow("Green", G)

cv2.imshow("Red", R)


# remove channel
# print(image.shape)
# image[:, :, 2] = np.zeros([image.shape[0], image.shape[1]])

cv2.waitKey(0)
cv2.destroyAllWindows()
