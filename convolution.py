import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/noise.png")

kernel1 = np.ones((3,3),np.float32)/9
kernel2 = np.ones((5,5),np.float32)/25

# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
convolution_3x3 = cv2.filter2D(img,-1,kernel1)
convolution_5x5 = cv2.filter2D(img,-1,kernel2)

# ตัวกรองค่าเฉลี่ย
blur_3x3 = cv2.blur(img,(3,3))
blur_5x5 = cv2.blur(img,(5,5))

# ตัวกรองค่ากลาง
median_3x3 = cv2.medianBlur(img,3)
median_5x5 = cv2.medianBlur(img,5)

# Gaussian Blur
Gaussian_3x3 = cv2.GaussianBlur(img,(3,3),0)
Gaussian_5x5 = cv2.GaussianBlur(img,(5,5),0)

titles = ["original","convolution 3x3","convolution 5x5","blur 3x3","blur 5x5","median 3x3","median 5x5",\
          "Gaussian 3x3","Gaussian 5x5"]
images = [img,convolution_3x3,convolution_5x5,blur_3x3,blur_5x5,median_3x3,median_5x5,Gaussian_3x3,Gaussian_5x5]

for  i in range(len(images)):
    plt.subplot(3,3,i+1),plt.imshow(images[i],"gray",vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()