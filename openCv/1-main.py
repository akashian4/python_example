import cv2




# read image
# img = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("test.jpg", cv2.IMREAD_COLOR)


# # save image
# status = cv2.imwrite('test2.jpg', img)
# print("Image written to file-system : ", status)


# #Accessing and Modifying pixel values
# pixel = img[100,100]  
# pixel = img[50:80,6:100] 
# print(pixel) 
# img[50:80,6:100]=(255,0,0) #or [255,0,0]  
# part1=img[100:270,150:400]
# img[300:470,250:500]=part1

# y = 0
# x = 0
# h = 300
# w = 500
# crope_image = img[x:w, y:h]



# #Accessing Image Properties
# # height, width, number of channels in image  
# height = img.shape[0]  
# width = img.shape[1]  
# channels = img.shape[2]  
# size1 = img.size  
# print('Image Height       : ',height)  
# print('Image Width        : ',width)  
# print('Number of Channels : ',channels)  
# print('Image Size  :', size1)


# img = cv2.imread("test.jpg")
# image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )   
# cv2.imshow('image', image)
    

#draw border
# image = cv2.copyMakeBorder("image", 2,10,10,20, cv2.BORDER_CONSTANT)


cv2.imshow('image', img)
# cv2.imshow('image', part1)
cv2.waitKey(0)
cv2.destroyAllWindows()
