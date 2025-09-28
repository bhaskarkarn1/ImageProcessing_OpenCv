import cv2

cap = cv2.VideoCapture(0)

# Read one frame to confirm dimensions
ret, frame = cap.read()
if not ret:
    print("Failed to capture from webcam")
    cap.release()
    exit()

height, width = frame.shape[:2]

# Use a codec that works on macOS
fourcc = cv2.VideoWriter_fourcc(*'mp4v')   # use 'MJPG' if you prefer .avi
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))

print("VideoWriter opened:", out.isOpened())

while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("webcam", img_gray)

    # Press 'q' to quit
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()