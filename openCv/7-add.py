import cv2

img1 = cv2.imread('test.jpg', 1)
img2 = cv2.imread("merge.jpg", 1)

add = img1+img2
add = cv2.addWeighted(img1, 0.5, img2, 0.9, 0)
add = cv2.add(img1, img2)


cv2.imshow("add", add)
cv2.waitKey(0)
cv2.destroyAllWindows()
