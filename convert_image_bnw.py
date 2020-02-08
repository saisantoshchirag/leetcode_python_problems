import cv2

img = cv2.imread('2.jpg')
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('1.jpg',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
#save photo

#cv2.imwrite('1.jpg',img1)