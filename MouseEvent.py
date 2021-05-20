import cv2
# อ่านภาพ
path = r"image/color.jpg"


img = cv2.imread(path,-1)

def position(event,x,y,flags,param):

    blue = img[y,x,0]
    green = img[y,x,1]
    red = img[y,x,2]

    # แสดงตำแหน่งที่ mouse click
    textposition = "(" + str(x) + "," + str(y) + ")"

    # แสดงสีตรงตำแหน่งที่ mouse click
    textColor = "(" + str(red) + "," + str(green) +","+str(blue)+")"
    # ถ้ามีการคลิ๊กซ้ายในจังหวะ DOWN
    if event == cv2.EVENT_LBUTTONDOWN:

        cv2.putText(img, textColor, (x, y), 5,1,(0, 0,0), 1, cv2.LINE_AA)
        cv2.putText(img, textposition, (x, y+30), 5, 1, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow("Output",img)

# ปรับขนาดภาพ
# imgResize = cv2.resize(img,(400,600))

cv2.imshow("Output",img)

# ทำงานร่วมกับ mouse
cv2.setMouseCallback("Output",position)

# เปิดภาพไว้ 5 วิ
# cv2.waitKey(delay=5000)
cv2.waitKey(0)

# คืนค่าให้กับ windows
cv2.destroyAllWindows()

