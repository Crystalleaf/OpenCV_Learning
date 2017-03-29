import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("1.jpg")

#px = img[100,100]
#print(px)

#blue = img[100,100,0]
#print(blue)

# Better pixel accessing and editing method : 
#img[100,100] = [255,255,255]
#print(img[100,100])

# Accessing Image Properties 
#print(img.shape)
#print(img.size)
#print(img.dtype)

# img.dtype is very important while debugging 
# because a large number of errors in OpenCV-Python code is caused by invalid datatype.

# copy sth to another region in the image:
#ball = img[280:340, 330:390]
#img[273:333, 100:160] = ball
#cv2.imshow("IMAGE", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# split image:
#b,g,r = cv2.split(img)
#cv2.imshow("image", r)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Making Borders for Images (Padding) 
BLUE = [255,0,0]
img1 = cv2.imread('opencv-logo.png')
replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()