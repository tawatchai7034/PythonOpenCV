import cv2

# อ่านภาพ
img = cv2.imread("image/cat.jpg")

cv2.imshow("Output",img)
# เปิดภาพไว้ 5 วิ
cv2.waitKey(0)
# คืนค่าให้กับ windows
cv2.destroyAllWindows()

