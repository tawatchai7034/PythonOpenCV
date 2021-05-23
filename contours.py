import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/ant.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,threshold = cv2.threshold(imgGray,215,255,cv2.THRESH_BINARY)

# ลบสัญญารับกวน
Gaussian_3x3 = cv2.GaussianBlur(threshold,(3,3),0)

# https://docs.opencv.org/master/d4/d73/tutorial_py_contours_begin.html
contours, hierarchy = cv2.findContours(Gaussian_3x3 , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

imgContours = cv2.imread("image/ant.jpg")
cv2.drawContours(imgContours,contours,-1,(0,0,0),2)

titles =["origin","Grayscale","threshold","Contours"]
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# imgContours = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
images = [img,imgGray,threshold,imgContours]

for i in range(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray",vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()