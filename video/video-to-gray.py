import numpy as np
import cv2

cap = cv2.VideoCapture('traffic.mp4')
while (cap.isOpened()):
    ret, frame = cap.read()
<<<<<<< HEAD
    if ret == False:
=======
    if not ret:
>>>>>>> 2a77a2740699d6332f125fe53fdc209c5c9363a0
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
