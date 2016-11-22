# mouse_events_2.py

# gli eventi del mouse
import numpy as np
import cv2

drawing = False
fill = False

img = np.zeros((512, 512, 3), np.uint8)

def draw_circle(event, x, y, flags, params):
    global drawing, fill

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if fill:
                cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (255, 0, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Click and Drag to Draw', (10, 470), font, 1, (255, 255, 255), 2)
cv2.putText(img, 'f to fill', (10, 500), font, 1, (255, 255, 255), 2)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('f'):
        fill = not fill
    elif k == ord('q'):
        break

cv2.destroyAllWindows()
