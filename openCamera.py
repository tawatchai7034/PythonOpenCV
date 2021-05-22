
import cv2
import datetime
# เปิดกล้อง
cap = cv2.VideoCapture(0)

Face_Cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")


while(True):
    # รับภาพจากกล่อง frame ต่อ frame
    check , frame = cap.read()
    # แปลง video เป็น grayscale
    VDOGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # แสดงวัน เวลา
    timeCurrent = str(datetime.datetime.now())
    cv2.putText(frame, timeCurrent, (25, 25), 5,1,(0, 0, 0), 2, cv2.LINE_AA)

    # จำแนกใบหน้า
    # scaleFactor คือการลดขนาดของภาพลงในอัตราส่วน 1.10 = 10% ,1.05 = 5%
    scaleFactor = 1.20
    # minNeighbors คือจำนวนรอบในการคำนวนตำแหน่งที่เจอใบหน้าเพื่อความแม่นยำ (k-mean)
    minNeighbors = 5
    face_detect = Face_Cascade.detectMultiScale(VDOGray, scaleFactor, minNeighbors)
    for (x, y, w, h) in face_detect:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow("Output", frame)

    # cv2.imshow("Output",VDOGray)
    # รอรับ key จากแป้นพิมเพื่อปิดกล้อง
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

# เปิด Video
capVDO = cv2.VideoCapture("image/Video.mp4")

# while(capVDO.isOpened()):
#     # รับ video เข้ามา
#     check , frame = capVDO.read()
#
#     # ตรวจสอบว่า video จบรึยัง
#     if check ==True:
#         # แปลง video ให้เป็น grayScale
#         # VDOGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#
#         # แสดงวัน เวลา
#         timeCurrent = str(datetime.datetime.now())
#         cv2.putText(frame, timeCurrent, (25, 25), 5,1,(0, 0, 0), 2, cv2.LINE_AA)
#
#         cv2.imshow("Output",frame)
#         # รอรับ key จากแป้นพิมเพื่อปิดกล้อง
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#             break
#
#     else:
#         break

cap.release()
cv2.destroyAllWindows()
