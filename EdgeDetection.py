import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/currency.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# ลบสัญญารับกวน
Gaussian_3x3 = cv2.GaussianBlur(imgGray,(3,3),0)

# https://docs.opencv.org/3.4/d2/d2c/tutorial_sobel_derivatives.html
sobel_X = cv2.Sobel(imgGray,-1,1,0)
sobel_Y = cv2.Sobel(imgGray,-1,0,1)
sobel_XY = cv2.bitwise_or(sobel_X,sobel_Y)

#sytax : cv2.Laplacian(src, ddepth, other_options...)
# https://docs.opencv.org/3.4/d5/db5/tutorial_laplace_operator.html
laplacian = cv2.Laplacian(imgGray,-1)


#syntax: cv2.Canny(image, threshold1, threshold2, apertureSize, L2gradient)
canny = cv2.Canny(imgGray,100,200)

titles =["origin","sobel X","sobel Y","sobel XY","Laplacian","Canny"]
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
images = [imgGray,sobel_X,sobel_Y,sobel_XY,laplacian,canny]

for i in range(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray",vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()