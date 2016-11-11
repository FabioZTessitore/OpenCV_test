import cv2

img = cv2.imread('../images/person.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Display Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
