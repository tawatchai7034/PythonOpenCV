import cv2

# อ่านไฟล์สำหรับ classification
Face_Cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")
Eye_Cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

# # detect ใบหน้าและดวงตาจากรูป
# path = r"image/MorePeple.jpg"
# path2 = r"image/girl.jpg"
#
# img = cv2.imread(path,1)
# img2 = cv2.imread(path2,1)
#
#
# grayScale = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#
# # จำแนกใบหน้า
# # scaleFactor คือการลดขนาดของภาพลงในอัตราส่วน 1.10 = 10% ,1.05 = 5%
# scaleFactor = 1.1
# # minNeighbors คือจำนวนรอบในการคำนวนตำแหน่งที่เจอใบหน้าเพื่อความแม่นยำ (k-mean)
# minNeighbors = 7
# face_detect = Face_Cascade.detectMultiScale(grayScale,scaleFactor,minNeighbors)
# eye_detect = Eye_Cascade.detectMultiScale(grayScale,scaleFactor,minNeighbors)
#
# # แสดงตำแหน่งใบหน้า
# for (x,y,w,h) in face_detect:
#     cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),2)
#     # แสดงตำแหน่งดวงตา
#     for (i, j, k, l) in eye_detect:
#         cv2.rectangle(img2, (i, j), (i + k, j + l), (0, 255, 0), 2)
#
# cv2.imshow("Output",img2)

# detect ใบหน้าและควงตาจาก video
capVDO = cv2.VideoCapture("image/Mark.mp4")

while (capVDO.isOpened()):
    # รับ video เข้ามา
    check, frame = capVDO.read()

    # ตรวจสอบว่า video จบรึยัง
    if check == True:
        # แปลง video ให้เป็น grayScale
        VDOGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # จำแนกใบหน้า
        # scaleFactor คือการลดขนาดของภาพลงในอัตราส่วน 1.10 = 10% ,1.05 = 5%
        scaleFactor = 1.20
        # minNeighbors คือจำนวนรอบในการคำนวนตำแหน่งที่เจอใบหน้าเพื่อความแม่นยำ (k-mean)
        minNeighbors = 5
        face_detect = Face_Cascade.detectMultiScale(VDOGray, scaleFactor, minNeighbors)
        eye_detect = Eye_Cascade.detectMultiScale(VDOGray, scaleFactor, minNeighbors)
        # แสดงตำแหน่งใบหน้า
        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            # แสดงตำแหน่งดวงตา
            for (i, j, k, l) in eye_detect:
                cv2.rectangle(frame, (i, j), (i + k, j + l), (0, 255, 0), 2)
            cv2.imshow("Output", frame)

        # รอรับ key จากแป้นพิมเพื่อปิดกล้อง
        if cv2.waitKey(200) & 0xFF == ord("e"):
            break

    else:
        break

capVDO.release()

cv2.waitKey(0)

# คืนค่าให้กับ windows
cv2.destroyAllWindows()