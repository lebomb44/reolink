#! /usr/bin/env python3
# coding: utf-8


""" Reolink Configuration file """

user = "admin"
password = "mypassword"
ext_ip = "mycameras.mydomain.com"
storage_root = "/home/osmc/HDD/cams"

class config:
    name = ""
    int_ip = ""
    ext_ip = ""
    port = ""
    user = ""
    password = ""
    storage = ""
    dl_age = 4
    tl_age = 3

bt_panoramix = config()
bt_panoramix.name="Bourdilot Panoramix"
bt_panoramix.int_ip="192.168.10.158"
bt_panoramix.ext_ip=ext_ip
bt_panoramix.int_port="80"
bt_panoramix.ext_port="89"
bt_panoramix.user=user
bt_panoramix.password=password
bt_panoramix.storage=storage_root+"/panoramix"

bt_entree = config()
bt_entree.name="Bourdilot Entree"
bt_entree.int_ip="192.168.10.159"
bt_entree.ext_ip=ext_ip
bt_entree.int_port="80"
bt_entree.ext_port="90"
bt_entree.user=user
bt_entree.password=password
bt_entree.storage=storage_root+"/entree"


bt_facade = config()
bt_facade.name="Bourdilot Facade"
bt_facade.int_ip="192.168.10.155"
bt_facade.ext_ip=ext_ip
bt_facade.int_port="80"
bt_facade.ext_port="85"
bt_facade.user=user
bt_facade.password=password
bt_facade.storage=storage_root+"/facade"

myconfig_list = { bt_panoramix, bt_entree, bt_facade }

