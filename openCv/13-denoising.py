import cv2
from matplotlib import pyplot as plt

img = cv2.imread("image.png")

final = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 8, 15)

plt.subplot(121)
plt.imshow(img)

plt.subplot(122)
plt.imshow(final)

plt.show()
