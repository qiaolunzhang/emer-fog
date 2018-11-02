import cv2
import time

used_time = 0
for i in range(10):
    start_time = time.time()
    vidcap = cv2.VideoCapture('traffic.mp4')
    success, image = vidcap.read()
    count = 0
    while success:
        if count % 1000 == 0:
            cv2.imwrite("./image/frame%d.jpg" % count, image)
        success, image = vidcap.read()
        # print("Read a new frame: ", success)
        count += 1
    used_time = used_time + time.time() - start_time
    print("%s seconds", used_time)
# print("--- %s seconds ---" % (time.time() - start_time))
print("--- %s seconds ---" % (used_time / 10))
print(type(used_time))
