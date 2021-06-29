# Copy from https://evigio.com/post/creating-a-time-lapse-video-editing-with-python
# Other: https://github.com/dannyvai/pylapse/blob/master/pylapse.py

import os
import cv2
import myconfig


def build_timelapse(config):
    records = config.storage + "/records"
    output = config.storage + "/timelapses"
    print("### Building timelapses from " + records)
    for (lspath, lsdirs, lsfiles) in os.walk(records):
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
                print("Building: " + output + "/" + tl_filename)
                lsfiles_wd = []
                for lsfile in lsfiles:
                    if lsfile.startswith("Rec_") == True:
                        if lsfile.endswith(".mp4") == True:
                            if workday in lsfile:
                                if lsfile not in lsfiles_wd:
                                    lsfiles_wd.append(lsfile)
                                    print("    to be added: " + lsfile)
                speed = 60
                writer = None
                for lsfile in lsfiles_wd:
                    print("    adding: " + lsfile + "...", end="", flush=True)
                    vid = cv2.VideoCapture(lsfile)
                    if writer == None:
                        w = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
                        h = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        fps = int(vid.get(cv2.CAP_PROP_FPS))
                        writer = cv2.VideoWriter(output + "/" + tl_filename, cv2.VideoWriter_fourcc('m','p','4','v'), fps, (w, h))
                    frames_nb_ori = 0
                    frames_nb_tl = 0
                    while vid.isOpened():
                        success, image = vid.read()
                        if not success:
                            break
                        if (frames_nb_ori % speed) == 0:
                            writer.write(image)
                            frames_nb_tl += 1
                        frames_nb_ori += 1
                    print(str(frames_nb_tl) + " frames added over " + str(frames_nb_ori) + " with speed " + str(speed))
                writer.release()
            else:
                print("    "  + output + "/" + tl_filename + " already exists")

build_timelapse(myconfig.fr_allee)
build_timelapse(myconfig.fr_veranda)
build_timelapse(myconfig.bt_panoramix)

