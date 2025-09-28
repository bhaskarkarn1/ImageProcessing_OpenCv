import cv2
import numpy as np

# Load image
img = cv2.imread('img/airplane.jpg')

flag = False
ix, iy = -1, -1

def crop(event, x, y, flags, params):
    global flag, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:   # Mouse press
        flag = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:   # Mouse release
        fx, fy = x, y
        flag = False

        # Draw rectangle
        cv2.rectangle(img, (ix, iy), (fx, fy), (0, 0, 0), 1)

        # Safe cropping
        cropped = img[min(iy, fy):max(iy, fy), min(ix, fx):max(ix, fx)]

        if cropped.size > 0:   # Only show if valid
            cv2.imshow("cropped", cropped)
            cv2.waitKey(0)

# Create window and set callback
cv2.namedWindow('window')
cv2.setMouseCallback('window', crop)

while True:
    cv2.imshow('window', img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()