import cv2
import matplotlib.pyplot as  plt

img = cv2.imread("image/girl.jpg")
# BGR
cv2.imshow("Output",img)

# RGB
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()