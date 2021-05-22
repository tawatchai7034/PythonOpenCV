import cv2
from matplotlib import pyplot as plt

img = cv2.imread("image/map.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
# syntax : cv2.threshold(src, thresholdValue, maxVal, thresholdingTechnique)
# ret,thresh1 = cv2.threshold(imgGray,127,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv2.threshold(imgGray,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3 = cv2.threshold(imgGray,127,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(imgGray,127,255,cv2.THRESH_TOZERO)
# ret,thresh5 = cv2.threshold(imgGray,127,255,cv2.THRESH_TOZERO_INV)
#
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(len(images)):
#     # plot Row = 2 ,column = 3,ตำแหน่งที่ i+1
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

# Color trackbar and Threshold
# cv2.namedWindow("Threshold value")
#
# def display(value):
#     pass
#
# cv2.createTrackbar("value","Threshold value",0,255,display)
#
# while True :
#     # ดึงค่าจาก Color trackbar มากำหนดสีของภาพ
#     ThresholdValue = cv2.getTrackbarPos("value","Threshold value")
#
#     ret, thresh1 = cv2.threshold(imgGray, ThresholdValue, 255, cv2.THRESH_BINARY)
#
#     # รอรับ key จากแป้นพิมเพื่อปิดกล้อง
#     if cv2.waitKey(200) & 0xFF == ord("e"):
#         break
#     cv2.imshow("Threshold value", thresh1)

# Adaptive thresholding
ret,th1 = cv2.threshold(imgGray,127,255,cv2.THRESH_BINARY)

# syntax : cv2.adaptiveThreshold(src, dst, maxValue, adaptiveMethod, thresholdType, blockSize, C = ค่าคงที่ในการหักล้่าง)
th2 = cv2.adaptiveThreshold(imgGray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(imgGray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)','Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
images = [img, th1, th2, th3]
for i in range(len(images)):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()