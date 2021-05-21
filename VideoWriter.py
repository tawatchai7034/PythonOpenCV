
# This time we create a VideoWriter object. We should specify the output file name (eg: output.avi).
# Then we should specify the FourCC code (details in next paragraph).
# Then number of frames per second (fps) and frame size should be passed.
# And the last one is the isColor flag. If it is True,
# the encoder expect color frame, otherwise it works with grayscale frame.
# https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html

import cv2

# เปิด Video
capVDO = cv2.VideoCapture("")

# In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable.
# MJPG results in high size video. X264 gives very small size video)

fourcc =cv2.VideoWriter_fourcc(*'XVID')

# ตั้งค่า video
result = cv2.VideoWriter("VideoWrite.avi",fourcc,20.0,(640,480))

while (capVDO.isOpened()):
    # รับ video เข้ามา
    check, frame = capVDO.read()

    # ตรวจสอบว่า video จบรึยัง
    if check == True:
        # แปลง video ให้เป็น grayScale
        # VDOGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Output", frame)

        # บันทึก video ไว้ใน result
        result.write(frame)

        # รอรับ key จากแป้นพิมเพื่อปิดกล้อง
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break

    else:
        break

capVDO.release()
cv2.destroyAllWindows()
