import cv2


img = cv2.imread("test.jpg", cv2.IMREAD_COLOR)


# get image height, width  
(h, w) = img.shape[:2]  
# calculate the center of the image  
center = (w / 2, h / 2)  
  
angle90 = 90  
angle180 = 180  
angle270 = 270  
  
scale = 1.0  
  
# Perform the counterclockwise rotation holding at the center  
# 90 degrees  
M = cv2.getRotationMatrix2D(center, angle90, scale)  
rotated90 = cv2.warpAffine(img, M, (h, w))  
  
# 180 degrees  
M = cv2.getRotationMatrix2D(center, angle180, scale)  
rotated180 = cv2.warpAffine(img, M, (w, h))  
  
# 270 degrees  
M = cv2.getRotationMatrix2D(center, angle270, scale)  
rotated270 = cv2.warpAffine(img, M, (h, w))  
  
cv2.imshow('Original Image', img)  
cv2.waitKey(0)  # waits until a key is pressed  
cv2.destroyAllWindows()  # destroys the window showing image  
  
cv2.imshow('Image rotated by 90 degrees', rotated90)  
cv2.waitKey(0)  # waits until a key is pressed  
cv2.destroyAllWindows()  # destroys the window showing imag  
  
cv2.imshow('Image rotated by 180 degrees', rotated180) 

cv2.waitKey(0)
cv2.destroyAllWindows()






# img1 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# cv2.imwrite('image1.jpg', img1)

# img2 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.imwrite('image2.jpg', img2)

# img3 = cv2.rotate(img, cv2.ROTATE_180)
# cv2.imwrite('image3.jpg', img3)


# img4 = cv2.flip(img, 0)
# cv2.imwrite('image4.jpg', img4)

# img5 = cv2.flip(img, 1)
# cv2.imwrite('image5.jpg', img5)

# img6 = cv2.flip(img, -1)
# cv2.imwrite('image6.jpg', img6)