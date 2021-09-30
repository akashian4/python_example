import numpy as np  
import cv2

img = cv2.imread("test.jpg",1)  

# cv2.circle(img,(80,180), 55, (118,0,24), -1)  
# cv2.rectangle(img,(15,25),(200,150),(0,255,255),15)  
# cv2.ellipse(img, (250, 150), (80, 20), 5, 0, 360, (0,0,255), -1)  
# cv2.line(img,(10,0),(150,150),(0,0,0),15) 

# font = cv2.FONT_HERSHEY_SIMPLEX  
# cv2.putText(img,'Hack Projects',(10,500), font, 1,(255,255,255),2)  

# pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)  
# cv2.polylines(img, [pts], True, (0,255,255), 3)






# path = "pic.jpg"
# image = cv2.imread(path)
# window_name = "Image"
# start_point = (0,0)
# end_point = (250,250)
# color = (29, 150, 180)
# thickness = 2
# image = cv2.line(image, start_point, end_point, color, thickness)


# image = cv2.imread('pic.jpg')
# window_name = "Circle"
# center_c = (190,250)
# radius = 100
# color = (150,0,127)
# thickness = 30
# image = cv2.circle(image, center_c, radius, color, thickness)


# image = cv2.imread('pic.jpg')
# window_name = "My Image"
# start_point = (100,100)
# end_point = (200,300)
# color = (255,0,0)
# thickness = -1
# image = cv2.rectangle(image, start_point, end_point, color, thickness)


# image = cv2.imread('pic.jpg')
# window_name = "Ellipse"
# c_c = (250,250)
# axesLength = (200,100)
# angle = 0
# startAngle = 0
# endAngle = 360
# color = (0, 0, 255)
# thickness = -1
# image = cv2.ellipse(image, c_c, axesLength, angle, startAngle, endAngle, color, thickness)




#draw with numpy

# img = np.zeros((800,800,3))
# cv2.line(img, (20,160),(100,250), (255,0,255), 12)
# cv2.rectangle(img, (30,30),(250,250),( 255,0,0), 5)
# cv2.circle(img, (200,200), 80, (0,255,0), 3)
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, "Open CV Python", (50,50), font, 1.8, (255,255,0), 2 ,cv2.LINE_AA)


cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()