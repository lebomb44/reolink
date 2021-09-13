#!/usr/bin/python3

import requests
import shutil
import json
#import wget
#import urllib
import sys
import signal
import os
import datetime
import time
import traceback

import myconfig

print('Content-Type: text/html')
print('')
print('<html><head><title>Cameras records ' + time.strftime('%Y/%m/%d %H:%M:%S') + '</title><meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests"></head>')
print("<body>")

info_msg = ""
error_msg = ""

def log(name, msg, end="<br>", flush=True):
    """ Print message with a time header """
    global info_msg
    info_msg = info_msg + time.strftime('%Y/%m/%d %H:%M:%S: ') + name + " : " + msg + end


def log_exception(name, ex, msg="ERROR Exception", end="\n", flush=True):
    """ Print exception with a time header """
    log(name, msg + ": " + str(ex), end=end, flush=flush)
    log(name, traceback.format_exc(), end=end, flush=flush)


def buildSearch_url(ip, port, user, password):
    return "http://"+ip+":"+port+"/cgi-bin/api.cgi?cmd=Search&user="+user+"&password="+password+"&token=1234"

def buildSearch_query(name, last_days):
    start_date = datetime.datetime.now() - datetime.timedelta(days=last_days)
    start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_date = start_date.replace(hour=23, minute=59, second=59, microsecond=999999)
    log(name, "Search from " + str(start_date) + " to " + str(end_date))
    return '[{"cmd":"Search","action":1,"param":{"Search":{"channel":0,"onlyStatus":0,"streamType":"main","StartTime":{"year":'+str(start_date.year)+',"mon":'+str(start_date.month)+',"day":'+str(start_date.day)+',"hour":'+str(start_date.hour)+',"min":'+str(start_date.minute)+',"sec":'+str(start_date.second)+'},"EndTime":{"year":'+str(end_date.year)+',"mon":'+str(end_date.month)+',"day":'+str(end_date.day)+',"hour":'+str(end_date.hour)+',"min":'+str(end_date.minute)+',"sec":'+str(end_date.second)+'}}}}]'

def buildDl_url(ip, port, user, password, name):
    input_name = name
    output_name = name.replace("/", "_")
    return "http://"+ip+":"+port+"/cgi-bin/api.cgi?cmd=Download&source="+input_name+"&output="+output_name+"&user="+user+"&password="+password+"&token=1234"

def print_link(name, url):
	print('<a href="'+url+'">'+name+'</a><br>', flush=True)

def link_files(name, ip, port, user, password, age, output):
    log(name, "Request the list of available files from " + name)
    headers={"accept": "application/json", "content-type": "application/json", "accept-encoding": "gzip, deflate"}
    resp = None
    search_request_is_ok = False
    for i in range(0, 3):
        try:
            url_ = buildSearch_url(ip, port, user, password)
            #log(name, "SEARCH URL = " + url_)
            data_ = buildSearch_query(name, age)
            #log(name, "SEARCH DATA = " + data_)
            resp = requests.post(url_, headers=headers, data=data_, verify=False, timeout=3.0)
            if resp.status_code == 200:
                search_request_is_ok = True
                break
        except Exception as ex:
            log_exception(name, ex, "ERROR : " + name)
    if search_request_is_ok is False:
        log(name, "ERROR : " + name + " : Too many attempts for search request")
        return
    # Convert the answer to JSON format
    jr=resp.json()
    # Check the answer
    if len(jr) != 1:
        sys.exit("Answer to search query has bad length, "+ str(len(jr)) + " received, 1 expected")
    if "value" not in jr[0]:
        log(name, jr[0])
        sys.exit("'value' key not found in answer to search query")
    if "SearchResult" not in jr[0]["value"]:
        log(name, jr[0]["value"])
        sys.exit("'SearchResult' key not found in answer to search query")
    if "File" not in jr[0]["value"]["SearchResult"]:
        log(name, "    No file to download: " + str(jr[0]["value"]["SearchResult"]))
        return
        sys.exit("'File' key not found in answer to search query")

    log(name, "Create files links to " + name)
    for file in jr[0]["value"]["SearchResult"]["File"]:
        if "name" not in file:
            log(name, "'name' key not found")
            continue
        remote_name = file['name']
        local_name = remote_name.replace("/", "_")
        dl_file_full_path = output + "/" + local_name
        if "size" not in file:
            log(name, "'size' key not found for file " + remote_name)
            continue
        remote_size=int(file["size"])
        url_to_dl = buildDl_url(ip, port, user, password, remote_name)
        print_link(local_name, url_to_dl)

def rsync_files(config):
    global info_msg
    print("<h1>"+config.name+"</h1>")
    for age in range(config.dl_age, -1, -1):
        link_files(config.name, config.ip, config.port, config.user, config.password, age, config.storage + "/records")
    print("<h1>##### INFO #####</h1>")
    print("<p>"+info_msg+"</p>")

print("<table><tbody>")
print('<td style="vertical-align:top">')
rsync_files(myconfig.bt_panoramix)
print("</td>")
print('<td style="vertical-align:top">')
rsync_files(myconfig.np_facade)
print("</td>")
print('<td style="vertical-align:top">')
rsync_files(myconfig.fr_allee)
print("</td>")
print('<td style="vertical-align:top">')
rsync_files(myconfig.fr_veranda)
print("</td>")
print("</tbody></table>")

print("</body></html>")

