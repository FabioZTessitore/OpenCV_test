# draw_figures.py

# disegna figure
import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.int8)

cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.rectangle(img, (50, 0), (200, 190), (255, 255, 0), 3)
cv2.circle(img, (100, 100), 40, (0, 255, 255), 3, cv2.LINE_AA)

while True:
    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()