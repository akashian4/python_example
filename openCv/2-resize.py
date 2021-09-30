import cv2 


img = cv2.imread("test.jpg", cv2.IMREAD_COLOR)
print('Original Dimensions : ', img.shape)  

# scale = 60   
# width = int(img.shape[1] * scale / 100)  
# height = int(img.shape[0] * scale / 100)  
# dim = (width, height)  
# resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


# scale = 150   
# width = int(img.shape[1] * scale / 100)  
# height = int(img.shape[0] * scale / 100)  
# dim = (width, height)   
# resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) 


# width = img.shape[1] 
# height = 440   
# dim = (width, height)    
# resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)  


width = img.shape[1]  # keep original width  
height = 200  
dim = (width, height)   
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) 


print('Resized Dimensions : ', resized.shape)  
cv2.imshow("Resized image", resized) 
cv2.waitKey(0)
cv2.destroyAllWindows()