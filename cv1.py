import cv2
import sys

image = cv2.imread('2.jpg')

grayimg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
grayimginv = 255 - grayimg

grayimginv = cv2.GaussianBlur(grayimginv,(21,21),0)
output = cv2.divide(grayimg,255-grayimginv,scale=256.0)

#cv2.namedWindow("image",cv2.WINDOW_AUTOSIZE)
#cv2.namedWindow("pencilsketch",cv2.WINDOW_AUTOSIZE)

#cv2.imshow("image",image)
cv2.imwrite("pencil.jpg",output)
cv2.waitKey(0)
cv2.destroyAllWindows()