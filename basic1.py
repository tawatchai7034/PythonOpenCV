import cv2
# อ่านภาพ
path = r"image/cat.jpg"

# Using 0 to read image in grayscale mode
# Using 1 to read image in RGB mode
# Using -1 to read image in
img = cv2.imread(path,-1)

# ปรับขนาดภาพ
imgResize = cv2.resize(img,(400,600))

cv2.imshow("Output",imgResize)
# เปิดภาพไว้ 5 วิ
# cv2.waitKey(delay=5000)
cv2.waitKey(0)
# คืนค่าให้กับ windows
cv2.destroyAllWindows()




