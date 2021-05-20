import cv2
# อ่านภาพ
path = r"image/cat.jpg"

# Using 0 to read image in grayscale mode
# Using 1 to read image in RGB mode
# Using -1 to read image in
img = cv2.imread(path,1)

# ปรับขนาดภาพ
imgResize = cv2.resize(img,(400,600))

# เปิดภาพไว้ 5 วิ
# cv2.waitKey(delay=5000)

# วาดเส้นตรง Syntax: cv2.line(image, start_point, end_point, color, thickness)
# cv2.arrowedLine(imgResize,(0,0),(100,100),(0,0,255),5)
# cv2.arrowedLine(imgResize,(0,0),(200,100),(0,255,0),5)
# cv2.arrowedLine(imgResize,(0,0),(300,100),(255,0,0),5)

# วาดสี่เหลี่ยม Syntax: cv2.rectangle(image, start_point, end_point, color, thickness or -1)
# cv2.rectangle(imgResize,(100,100),(400,400),(255,255,0),2)

# วาดวงกลม Syntax: cv2.circle(image, center_coordinates, radius, color, thickness or -1)
# cv2.circle(imgResize,(150,150),50,(150,150,0),15)

# ใส่ข้อความ Syntax: cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
# https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html
cv2.putText(imgResize, 'OpenCV', (150, 300), 5,2,(102, 56, 199), 2, cv2.LINE_AA)

cv2.imshow("Output",imgResize)

cv2.waitKey(0)

# คืนค่าให้กับ windows
cv2.destroyAllWindows()




