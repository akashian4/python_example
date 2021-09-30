import cv2
import numpy

img = cv2.imread('test.jpg', 1)

# blur1 = cv2.blur(img, (3, 3))

# dst = median = cv2.medianBlur(img,5)  
# blur2 = numpy.hstack((img, dst))

dst = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT) 
blur3=numpy.hstack((img, dst))

cv2.imshow("blur", blur3)
cv2.waitKey(0)
cv2.destroyAllWindows()
