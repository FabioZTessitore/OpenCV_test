# trackbar.py

import numpy as np
import cv2

drawing = False
fill = False

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

def nothing(x):
    pass

cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

switch = '0: OFF\n1: ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()