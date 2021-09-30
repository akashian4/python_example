import cv2

img = cv2.imread('test.jpg', 1)

# edge = cv2.Laplacian(img, cv2.CV_8U)
# edge = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)   #soble x
# edge = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)     #soble y
# edge = cv2.Sobel(img, cv2.CV_8U, 1, 1, ksize=5)
# edge = cv2.Canny(img, 100, 200)
edge = cv2.Canny(img, 400, 800)


cv2.imshow("original", img)
cv2.imshow("edgeDetection", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
