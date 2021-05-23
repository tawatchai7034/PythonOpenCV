
import cv2

# เปิด Video
capVDO = cv2.VideoCapture("image/Walking.mp4")
# รับ video เข้ามา
check, frame1 = capVDO.read()
check, frame2 = capVDO.read()

while (capVDO.isOpened()):

    # ตรวจสอบความแตกต่างกันของ 2 video
    motionDiff = cv2.absdiff(frame1,frame2)

    # ตรวจสอบว่า video จบรึยัง
    if check == True:
        # แปลง video ให้เป็น grayScale
        VDOGray = cv2.cvtColor(motionDiff , cv2.COLOR_BGR2GRAY)

        # ลบสัญญารับกวน
        blur = cv2.GaussianBlur(VDOGray,(3,3),0)

        ret, threshold = cv2.threshold(blur, 15, 255, cv2.THRESH_BINARY)

        dilation = cv2.dilate(threshold, None, iterations=3)

        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

        for contour in contours:
            (x,y,w,h) = cv2.boundingRect(contour)

            # กำหนดขอบเขตของกล่องสี่เหลี่ยม
            if cv2.contourArea(contour)<1700:
                continue

            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("Output", frame1)

        frame1 = frame2
        check ,frame2 = capVDO.read()

        # รอรับ key จากแป้นพิมเพื่อปิดกล้อง
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break

    else:
        break

capVDO.release()
cv2.destroyAllWindows()