# color_tracking.py

import cv2
import numpy as np

def getHSV(red, green, blue):
    color = np.uint8([[[blue, green, red]]])
    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    return hsv

#print getHSV(255, 0, 0)
#print getHSV(0, 255, 0)
#print getHSV(0, 0, 255)

# cattura un video dalla webcam e cerca elementi verdi

cap = cv2.VideoCapture(0)

lower_green = np.array([50, 50, 50])
upper_green = np.array([70, 255, 255])
lower_red = np.array([0, 50, 50])
upper_red = np.array([20, 255, 255])
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

while True:
    ret, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_green = cv2.inRange(hsv_frame, lower_green, upper_green)
    mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    mask = cv2.bitwise_or(mask_green, mask_red)
    mask = cv2.bitwise_or(mask, mask_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    #cv2.imshow('mask', mask)
    #cv2.imshow('mask_red', mask_red)
    #cv2.imshow('mask_blue', mask_blue)
    #cv2.imshow('mask_green', mask_green)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
