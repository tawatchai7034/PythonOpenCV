
import cv2
import datetime
# เปิดกล้อง
cap = cv2.VideoCapture(0)
while(True):
    # รับภาพจากกล่อง frame ต่อ frame
    check , frame = cap.read()

    # แสดงวัน เวลา
    timeCurrent = str(datetime.datetime.now())
    cv2.putText(frame, timeCurrent, (25, 25), 5,1,(0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Output",frame)
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
