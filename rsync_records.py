#! /usr/bin/env python3
# coding: utf-8


""" Reolink RSYNC """


import requests
import shutil
import json
#import wget
#import urllib
import sys
import signal
import os
import datetime

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
                lsfile_date = datetime.datetime.strptime(eltfile[1], "%Y%m%d")
                if lsfile_date < rm_date:
                    os.remove(lspath + "/" + lsfile)
                    print("Removed: " + lspath + "/" + lsfile)
            except:
                os.remove(lspath + "/" + lsfile)
                print("Removed: " + lspath + "/" + lsfile)


def buildSearch_url(ip, port, user, password):
    return "http://"+ip+":"+port+"/cgi-bin/api.cgi?cmd=Search&rs=abcde&user="+user+"&password="+password

def buildSearch_query(last_days):
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=last_days)
    start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
    print("### Search from " + str(start_date) + " to " + str(end_date) + " ###")
    return '[{"cmd":"Search","action":0,"param":{"Search":{"channel":0,"onlyStatus":0,"streamType":"main","StartTime":{"year":'+str(start_date.year)+',"mon":'+str(start_date.month)+',"day":'+str(start_date.day)+',"hour":'+str(start_date.hour)+',"min":'+str(start_date.minute)+',"sec":'+str(start_date.second)+'},"EndTime":{"year":'+str(end_date.year)+',"mon":'+str(end_date.month)+',"day":'+str(end_date.day)+',"hour":'+str(end_date.hour)+',"min":'+str(end_date.minute)+',"sec":'+str(end_date.second)+'}}}}]'

def buildDl_url(ip, port, user, password, name):
    return "http://"+ip+":"+port+"/cgi-bin/api.cgi?cmd=Download&rs=abcde&source="+name+"&output="+name+"&user="+user+"&password="+password

def download_files(name, ip, port, user, password, age, output):
    print("### Request the list of available files from " + name + " ###")
    headers={"accept": "application/json", "content-type": "application/json", "accept-encoding": "gzip, deflate"}
    resp = None
    search_request_is_ok = False
    for i in range(0, 10):
        try:
            resp = requests.post(buildSearch_url(ip, port, user, password), headers=headers, data=buildSearch_query(age), verify=False, timeout=10.0)
            if resp.status_code == 200:
                search_request_is_ok = True
                break
        except Exception as ex:
            print("ERROR : " + name + " : " + str(ex))
    if search_request_is_ok is False:
        print("ERROR : " + name + " : Too many attempts for search request")
        return
    # Convert the answer to JSON format
    jr=resp.json()
    # Check the answer
    if len(jr) != 1:
        sys.exit("Answer to search query has bad length, "+ str(len(jr)) + " received, 1 expected")
    if "value" not in jr[0]:
        print(jr[0])
        sys.exit("'value' key not found in answer to search query")
    if "SearchResult" not in jr[0]["value"]:
        print(jr[0]["value"])
        sys.exit("'SearchResult' key not found in answer to search query")
    if "File" not in jr[0]["value"]["SearchResult"]:
        print(jr[0]["value"]["SearchResult"])
        sys.exit("'File' key not found in answer to search query")

    print("### Download the files from " + name + " ###")
    for file in jr[0]["value"]["SearchResult"]["File"]:
        if "name" not in file:
            print("'name' key not found")
            continue
        fname=file['name']
        if "size" not in file:
            print("'size' key not found for file " + fname)
            continue
        size=int(file["size"])
        try:
            if os.path.getsize(output + "/" + fname) == size:
                print(fname + " already downloaded (" + str(size) + " bytes) from " + name)
                continue
            else:
                print("Remote size is " + str(size) + ", local size is " + str(os.path.getsize(fname)))
                raise OSError
        except OSError as err:
            #print(err)
            for i in range(0, 10):
                try:
                    print("Downloading " + fname + " (" + str(size) + " bytes) from " + name + "...", end="", flush=True)
                    #wget.download(buildDl_url(ip, port, user, password, fname), output + "/" + fname)
                    #urllib.request.urlretrieve(buildDl_url(ip, port, user, password, fname), output + "/" + fname)
                    url_to_dl = buildDl_url(ip, port, user, password, fname)
                    dl_file_full_path = output + "/" + fname
                    with requests.get(url_to_dl, stream=True, verify=False, timeout=10.0) as r:
                        with open(dl_file_full_path, 'wb') as f:
                            shutil.copyfileobj(r.raw, f)
                    print("OK")
                    break
                except KeyboardInterrupt:
                    sys.exit("Exiting")
                except:
                    print("ERROR")

def rsync_files(config):
    remove_old_files(config.name, config.storage + "/records", config.dl_age+1)
    download_files(config.name, config.ip, config.port, config.user, config.password, config.dl_age, config.storage + "/records")

rsync_files(myconfig.fr_allee)
rsync_files(myconfig.fr_veranda)
rsync_files(myconfig.bt_panoramix)

