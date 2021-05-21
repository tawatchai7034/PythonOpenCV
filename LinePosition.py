import cv2
import numpy
img = cv2.imread("image/tree.jpg")
# array ใช้เก็บตำแน่งที่คลิ๊ก
positions = []

def position(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (0, 0, 255), 2)
        # เพิ่มตำแหน่งที่คลิ๊กไปใน array
        positions.append((x,y))

        if len(positions)>=2:
            # สร้างเส้นตรงโดยยึดจากสมาชิกตำแหน่งสุดท้ายและรองสุดท้ายของ array
            cv2.line(img,positions[-2],positions[-1],(0,0,255),1)

        # if len(positions)%2 == 0:
        #     # สร้างเส้นตรงโดยยึดจากสมาชิกตำแหน่งสุดท้ายและรองสุดท้ายของ array
        #     cv2.line(img,positions[-2],positions[-1],(0,0,255),5)

        cv2.imshow("Output",img)

cv2.imshow("Output",img)

# ทำงานร่วมกับ mouse
cv2.setMouseCallback("Output",position)

# เปิดภาพไว้ 5 วิ
# cv2.waitKey(delay=5000)
cv2.waitKey(0)

# คืนค่าให้กับ windows
cv2.destroyAllWindows()


