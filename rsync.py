#! /usr/bin/env python3
# coding: utf-8


""" Reolink RSYNC """


import requests
import json
import wget
import sys
import os
import datetime

import myconfig


ip=myconfig.ip
port=myconfig.port
user=myconfig.user
password=myconfig.password
output=myconfig.output

print("### Remove old local files ###")
rm_date = datetime.datetime.now() - datetime.timedelta(32)
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

headers={"accept": "application/json", "content-type": "application/json", "accept-encoding": "gzip, deflate"}

def buildSearch_url(ip, port, user, password):
    return "http://"+ip+":"+port+"/cgi-bin/api.cgi?cmd=Search&rs=abcde&user="+user+"&password="+password

def buildSearch_query(last_days):
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(last_days)
    return '[{"cmd":"Search","action":0,"param":{"Search":{"channel":0,"onlyStatus":0,"streamType":"main","StartTime":{"year":'+str(start_date.year)+',"mon":'+str(start_date.month)+',"day":'+str(start_date.day)+',"hour":'+str(start_date.hour)+',"min":'+str(start_date.minute)+',"sec":'+str(start_date.second)+'},"EndTime":{"year":'+str(end_date.year)+',"mon":'+str(end_date.month)+',"day":'+str(end_date.day)+',"hour":'+str(end_date.hour)+',"min":'+str(end_date.minute)+',"sec":'+str(end_date.second)+'}}}}]'

def buildDl_url(ip, port, user, password, name):
    return "http://"+ip+":"+port+"/cgi-bin/api.cgi?cmd=Download&rs=abcde&source="+name+"&output="+name+"&user="+user+"&password="+password

print("### Request the list of available files ###")
resp = requests.post(buildSearch_url(ip, port, user, password), headers=headers, data=buildSearch_query(31), timeout=10.0)
if resp.status_code != 200:
    sys.exit("Search request invalid on "+ip+":"+port)
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

print("### Download the files ###")
for file in jr[0]["value"]["SearchResult"]["File"]:
    if "name" not in file:
        print("'name' key not found")
        continue
    name=file['name']
    if "size" not in file:
        print("'size' key not found for file " + name)
        continue
    size=int(file["size"])
    try:
        if os.path.getsize(name) == size:
            print(name + " already downloaded (" + str(size) + " bytes)")
            continue
        else:
            raise OSError
    except OSError:
        print("Downloading " + name + " (" + str(size) + " bytes)")
        wget.download(buildDl_url(ip, port, user, password, name), output + "/" + name)
        print("\r")

