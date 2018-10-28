import numpy as np
import cv2

cap = cv2.VideoCapture('traffic.mp4')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#out = cv2.VideoWriter('output.avi', fourcc, 10.0, (int(cap.get(3)),int(cap.get(4))))
out = cv2.VideoWriter('output.avi', fourcc, 10, (int(cap.get(3)),int(cap.get(4))))

count = 1

while (cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    #frame = cv2.flip(frame, 0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(gray)
    out.write(gray)
    cv2.imwrite('./images/'+str(count)+'.png', gray)
    count = count + 1
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
