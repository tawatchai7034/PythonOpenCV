import cv2
import numpy as np

img = np.zeros([400,400,3],np.uint8)

cv2.namedWindow("Color trackbar")

def display(value):
    pass

# สร้าง trackbar or slider
# https://docs.opencv.org/3.4/da/d6a/tutorial_trackbar.html
cv2.createTrackbar("B","Color trackbar",0,255,display)
cv2.createTrackbar("G","Color trackbar",0,255,display)
cv2.createTrackbar("R","Color trackbar",0,255,display)

while True :
    cv2.imshow("Color trackbar",img)

    # ดึงค่าจาก Color trackbar มากำหนดสีของภาพ
    blue = cv2.getTrackbarPos("B","Color trackbar")
    green = cv2.getTrackbarPos("G","Color trackbar")
    red = cv2.getTrackbarPos("R", "Color trackbar")

    # กำหนดค่าสีให้ภาพ
    img[:] = [blue,green,red]

    # รอรับ key จากแป้นพิมเพื่อปิดกล้อง
    if cv2.waitKey(200) & 0xFF == ord("e"):
        break

# cv2.waitKey(0)
# คืนค่าให้กับ windows
cv2.destroyAllWindows()