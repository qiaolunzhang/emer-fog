import cv2
import time

start_time = time.time()
vidcap = cv2.VideoCapture('traffic.mp4')
success, image = vidcap.read()
count = 0
while success:
    if count % 500 == 0:
        cv2.imwrite("./image/frame%d.jpg" % count, image)
    success, image = vidcap.read()
    # print("Read a new frame: ", success)
    count += 1
print("--- %s seconds ---" % (time.time() - start_time))
print(type(start_time))
