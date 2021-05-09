# Copy from https://evigio.com/post/creating-a-time-lapse-video-editing-with-python
# Other: https://github.com/dannyvai/pylapse/blob/master/pylapse.py

import os
import cv2
import myconfig

ip=myconfig.ip
port=myconfig.port
user=myconfig.user
password=myconfig.password
output=myconfig.output

for (lspath, lsdirs, lsfiles) in os.walk(output):
    workdays = []
    lsfiles.sort()
    for lsfile in lsfiles:
        if lsfile.startswith("Rec_") == True:
            workday = list(lsfile.split("_"))[1]
            if workday not in workdays:
                workdays.append(workday)
                print("New timelapse to do: " + workday)
    for workday in workdays:
        tl_filename = workday + "_timelapse.mp4"
        if tl_filename not in lsfiles:
            print("Building: " + tl_filename)
            lsfiles_wd = []
            for lsfile in lsfiles:
                if lsfile.startswith("Rec_") == True:
                    if workday in lsfile:
                        if lsfile not in lsfiles_wd:
                            lsfiles_wd.append(lsfile)
                            print("   to be added: " + lsfile)
            success = 1
            count = 0
            speed = 60
            writer = None
            for lsfile in lsfiles_wd:
                vid = cv2.VideoCapture(lsfile)
                if writer == None:
                    w = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
                    h = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    fps = int(vid.get(cv2.CAP_PROP_FPS))
                    writer = cv2.VideoWriter(output + "/" + tl_filename, cv2.VideoWriter_fourcc('m','p','4','v'), fps, (w, h))
                while vid.isOpened():
                    success, image = vid.read()
                    if not success:
                        break
                    if (count % speed) == 0:
                        writer.write(image)
                    count += 1
                print("    added: " + lsfile)
            writer.release()

