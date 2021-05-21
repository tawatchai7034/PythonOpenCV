import cv2

path = r"image/MorePeple.jpg"

img = cv2.imread(path,1)

# อ่านไฟล์สำหรับ classification
Face_Cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")

grayScale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# จำแนกใบหน้า
# scaleFactor คือการลดขนาดของภาพลงในอัตราส่วน 1.10 = 10% ,1.05 = 5%
scaleFactor = 1.1
# minNeighbors คือจำนวนรอบในการคำนวนตำแหน่งที่เจอใบหน้าเพื่อความแม่นยำ (k-mean)
minNeighbors = 7
face_detect = Face_Cascade.detectMultiScale(grayScale,scaleFactor,minNeighbors)

# แสดงตำแหน่งใบหน้า
for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("Output",img)
# เปิดภาพไว้ 5 วิ
# cv2.waitKey(delay=5000)
cv2.waitKey(0)
# คืนค่าให้กับ windows
cv2.destroyAllWindows()