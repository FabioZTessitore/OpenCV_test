# mouse_events.py

# gli eventi del mouse
import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)

def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'DBL Click to Draw a Circle', (10, 500), font, 1, (255, 255, 255), 2)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
