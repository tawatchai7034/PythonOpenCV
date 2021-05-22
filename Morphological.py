import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("image/CoinNoise.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(imgGray,170,255,cv2.THRESH_BINARY_INV)

# สร้างตัวกรองข้อมูล 2x2, 3x3
kernel = np.ones((2,2),np.uint8)

# https://www.geeksforgeeks.org/erosion-dilation-images-using-opencv-python/
dilation = cv2.dilate(thresh1, kernel, iterations=2)
erosion = cv2.erode(thresh1,kernel,iterations=2)
dilationANDerosion = cv2.erode(dilation,kernel,iterations=2)
opening = cv2.morphologyEx(thresh1,cv2.MORPH_OPEN,kernel,iterations=7)
closing = cv2.morphologyEx(thresh1,cv2.MORPH_CLOSE,kernel,iterations=7)


titles = ["original","Threshold","dilation","erosion","dilation AND erosion","opening","closing"]
images = [imgGray,thresh1,dilation,erosion,dilationANDerosion,opening,closing]

for i in range(len(images)):
    plt.subplot(2,4,i+1),plt.imshow(images[i],"gray",vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
