import cv2
import math

img = cv2.imread("image/cow.jpg")
imgResize = cv2.resize(img,(800,600))
# array ใช้เก็บตำแน่งที่คลิ๊ก
positions = []
positions_x = []
positions_y = []

def position(event,x,y,flags,param):
    # แสดงตำแหน่งที่ mouse click
    textposition = "(" + str(x) + "," + str(y) + ")"

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imgResize, (x, y), 10, (0, 0, 255), 2)

        positions_x.append(x)
        positions_y.append(y)

        # เพิ่มตำแหน่งที่คลิ๊กไปใน array
        positions.append((x,y))

        # cv2.putText(imgResize, textposition, (x, y + 30), 5, 1, (0, 0, 255), 1, cv2.LINE_AA)

        # if len(positions)>=2:
        #     # สร้างเส้นตรงโดยยึดจากสมาชิกตำแหน่งสุดท้ายและรองสุดท้ายของ array
        #     cv2.line(imgResize,positions[-2],positions[-1],(0,0,255),1)

        if len(positions)%2 == 0:
            # สร้างเส้นตรงโดยยึดจากสมาชิกตำแหน่งสุดท้ายและรองสุดท้ายของ array
            cv2.line(imgResize,positions[-2],positions[-1],(0,0,255),5)

            DistanceBase = 105
            CentimeterBase = 60

            # คำนวณระยะห่างระหว่างสองจุดที่กำหนด
            DistancePixel = math.sqrt(((positions_x[-1] - positions_x[-2]) ** 2) + ((positions_y[-1] - positions_y[-2]) ** 2))
            DistanceCentimeter = (DistancePixel/DistanceBase)*CentimeterBase

            # แสดงระยะห่างระหว่างสองจุดที่กำหนด
            textDistance = "(" + str(int(DistanceCentimeter)) + " Cm )"

            # จุดกึ่งกลางระหว่างสองจุด
            meduimX =  int((positions_x[-1] - positions_x[-2])/2)
            meduimY = int((positions_y[-1] - positions_y[-2])/2)

            # print("X : " + str(positions_x[-1]) + " | Y : " + str(positions_y[-1]) + " | Distance : " + str(DistancePixel))

            cv2.putText(imgResize, textDistance , (positions_x[-2]+meduimX, positions_y[-2]+meduimY), 5, 1, (0,255, 0), 1, cv2.LINE_AA)

        cv2.imshow("Output",imgResize)

cv2.imshow("Output",imgResize)

# ทำงานร่วมกับ mouse
cv2.setMouseCallback("Output",position)

# เปิดภาพไว้ 5 วิ
# cv2.waitKey(delay=5000)
cv2.waitKey(0)

# คืนค่าให้กับ windows
cv2.destroyAllWindows()


