import imutils
import cv2
import numpy as np

interval = 30
outfilename = 'output.avi'
threshold=100.
fps = 10

cap = cv2.VideoCapture("traffic.mp4")

ret, frame = cap.read()
height, width, nchannels = frame.shape

#fourcc = cv2.cv.CV_FOURCC(*'DIVX')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter( outfilename,fourcc, fps, (width,height))

ret, frame = cap.read()
frame = imutils.resize(frame, width=500)
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

while(True):

  frame0 = frame

  ret, frame = cap.read()
  frame = imutils.resize(frame, width=500)
  frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

  if not ret:
    deletedcount +=1
    break

  if np.sum( np.absolute(frame-frame0) )/np.size(frame) > threshold:
    out.write(frame)
  else:
    print("Deleted")

  cv2.imshow('Feed - Press "q" to exit',frame)

  key = cv2.waitKey(interval) & 0xFF

  if key == ord('q'):
    print('received key q' )
    break

cap.release()
out.release()
print('Successfully completed')
