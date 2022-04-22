#! /usr/bin/env python3
# coding: utf-8


""" Reolink Configuration file """

user = "abcd"
password = "abcd"
storage_root = "/home/osmc/HDD/cams"

class config:
    name = ""
    ip = ""
    port = ""
    user = ""
    password = ""
    storage = ""
    dl_age = 4
    tl_age = 3

bt_panoramix = config()
bt_panoramix.name="Bourdilot Panoramix"
bt_panoramix.ip="192.168.10.158"
bt_panoramix.port="80"
bt_panoramix.user=user
bt_panoramix.password=password
bt_panoramix.storage=storage_root+"/panoramix"

bt_entree = config()
bt_entree.name="Bourdilot Entree"
bt_entree.ip="192.168.10.159"
bt_entree.port="80"
bt_entree.user=user
bt_entree.password=password
bt_entree.storage=storage_root+"/entree"


bt_facade = config()
bt_facade.name="Bourdilot Facade"
bt_facade.ip="192.168.10.155"
bt_facade.port="80"
bt_facade.user=user
bt_facade.password=password
bt_facade.storage=storage_root+"/facade"

myconfig_list = { bt_panoramix, bt_entree, bt_facade }

