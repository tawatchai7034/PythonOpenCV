import cv2
# อ่านภาพ
path = r"image/cat.jpg"

# Using 0 to read image in grayscale mode
# Using 1 to read image in RGB mode
# Using -1 to read image in
img = cv2.imread(path,0)

imgResize = cv2.resize(img,(400,600))

# export image
cv2.imwrite("cat2.jpg",imgResize)

cv2.imshow('output',imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()