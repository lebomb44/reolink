#! /usr/bin/env python3
# coding: utf-8


""" Reolink Timelapse from Records """
 
# Copy from https://evigio.com/post/creating-a-time-lapse-video-editing-with-python
# Other: https://github.com/dannyvai/pylapse/blob/master/pylapse.py

import os
import datetime
import cv2
import myconfig


def remove_old_files(name, output, age):
    print("### Remove old local files from " + name + " ###")
    rm_date = datetime.datetime.now() - datetime.timedelta(days=age)
    rm_date = rm_date.replace(hour=0, minute=0, second=0, microsecond=0)
    print("### Older than " + str(rm_date) + " ###")
    for (lspath, lsdirs, lsfiles) in os.walk(output):
        for lsfile in lsfiles:
            try:
                eltfile = list(lsfile.split("_"))
                lsfile_date = datetime.datetime.strptime(eltfile[0], "%Y%m%d")
                if lsfile_date < rm_date:
                    os.remove(lspath + "/" + lsfile)
                    print("Removed: " + lspath + "/" + lsfile)
            except:
                os.remove(lspath + "/" + lsfile)
                print("Removed: " + lspath + "/" + lsfile)

def build_timelapse(name, records, output):
    print("### Building timelapses from " + records + " to " + output + " for " + name)
    for (lspath, lsdirs, lsfiles) in os.walk(records):
        workdays = []
        lsfiles.sort()
        for lsfile in lsfiles:
            if lsfile.startswith("Rec_") == True:
                workday = list(lsfile.split("_"))[1]
                if workday not in workdays:
                    workdays.append(workday)
                    print("New timelapse to do for " + name + ": " + workday)
        for workday in workdays:
            tl_filename = workday + "_timelapse.mp4"
            if tl_filename not in lsfiles:
                print("Building for " + name + ": " + output + "/" + tl_filename)
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
                    vid = cv2.VideoCapture(records + "/" + lsfile)
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
                print("    "  + output + "/" + tl_filename + " already exists for " + name)

def do_timelapses(config):
    remove_old_files(config.name, config.storage + "/timelapses", config.tl_age+1)
    build_timelapse(config.name, config.storage + "/records", config.storage + "/timelapses")

for cam in myconfig.myconfig_list:
    print("### " + cam.name + " ###")
    #do_timelapses(cam)

