# Copy from https://evigio.com/post/creating-a-time-lapse-video-editing-with-python
# Other: https://github.com/dannyvai/pylapse/blob/master/pylapse.py

import cv2

vid = cv2.VideoCapture('./assets/key.mov')
frames = []
success = 1
count = 0
speed = 8

while success:
    success, image = vid.read()
    if(count % speed == 0):
        frames.append(image)
    count += 1

writer = cv2.VideoWriter('./output/tl.mp4', cv2.VideoWriter_fourcc(*"MP4V"), 29.98, (1280, 720))

for frame in frames:
    writer.write(frame)
writer.release()
