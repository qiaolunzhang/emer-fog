import os

os.system('ffmpeg -i traffic.mp4 -vf format=gray hello.avi')
