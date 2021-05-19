# เปิดกล้อง
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # รับภาพจากกล่อง frame ต่อ frame
    check , frame = cap.read()
    cv2.imshow("Output",frame)
    # รอรับ key จากแป้นพิมเพื่อปิดกล้อง
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break
cap.release()
cv2.destroyAllWindows()
