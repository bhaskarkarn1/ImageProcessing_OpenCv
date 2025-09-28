import cv2
import numpy as np

# Flags and initial points
flag = False
ix, iy = -1, -1

def draw(event, x, y, flags, param):
    global flag, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:     # Mouse pressed
        flag = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:     # Mouse move with button down
        if flag:
            temp = img.copy()
            cv2.rectangle(temp, (ix, iy), (x, y), (0, 255, 255), -1)
            cv2.imshow("image", temp)

    elif event == cv2.EVENT_LBUTTONUP:     # Mouse released
        flag = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 255), -1)

# Create black image
img = np.zeros((512,512,3), dtype=np.uint8)

cv2.namedWindow("image")
cv2.setMouseCallback("image", draw)

while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
