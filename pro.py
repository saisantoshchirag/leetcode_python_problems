import cv2
import numpy as np

img = cv2.imread("start.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
