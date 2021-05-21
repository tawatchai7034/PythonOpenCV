import cv2
import  numpy

path = r"image/ball2d.jpg"

img = cv2.imread(path,1)
while True :
    # red
    # upper = numpy.array([219, 0, 11])
    # lower = numpy.array([219, 145, 149])

    # green
    upper = numpy.array([96,255,123])
    lower = numpy.array([4,105,7])

    # blue
    # upper = numpy.array([253,231,136])
    # lower = numpy.array([161,50,2])

    # purple
    # upper = numpy.array([255, 143, 244])
    # lower = numpy.array([179, 9, 128])

    # https://docs.opencv.org/3.4/da/d97/tutorial_threshold_inRange.html
    mask = cv2.inRange(img,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("original",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result", result)

    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cv2.destroyAllWindows()
