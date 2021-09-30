import cv2

image = cv2.imread('test.jpg')

window_name = "My Image"

text = "My Python Language"
font = cv2.FONT_HERSHEY_SIMPLEX

org = (0,250)
fontscale = 1
color = (255,0,255)

thickness = 2

image = cv2.putText(image, text, org, font, fontscale, color, thickness, cv2.LINE_AA, False)

cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()