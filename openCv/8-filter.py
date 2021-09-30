import cv2
import numpy as np  
from matplotlib import pyplot as plt

# img = cv2.imread('text.jpg', 1)
img = cv2.imread('text.png', 1)

# kernel = np.ones((5,5),np.float32)/25  
# blur = cv2.bilateralFilter(img,9,75,75)  
# plt.subplot(121),plt.imshow(img),plt.title('Original')  
# plt.xticks([]), plt.yticks([])  
# plt.subplot(122),plt.imshow(blur),plt.title('Bilateral Filter')  
# plt.xticks([]), plt.yticks([])  
# cv2.imshow("Image",blur)

# img_1 = cv2.boxFilter(img, 0, (2,1), img, (-1,-1), False, cv2.BORDER_DEFAULT)  
# cv2.imshow('Image',img_1)  

# kernel = np.ones((5,5),np.float32)/25  
# dst = cv2.filter2D(img,-1,kernel)  
# plt.subplot(121),plt.imshow(img),plt.title('Original')  
# plt.xticks([]), plt.yticks([])  
# plt.subplot(122),plt.imshow(dst),plt.title('Filter2D')  
# plt.xticks([]), plt.yticks([])  
# plt.show() 

retval, threshold = cv2.threshold(img, 62, 255, cv2.THRESH_BINARY)  
cv2.imshow("Original Image", img)  
cv2.imshow("Threshold",threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
