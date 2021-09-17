#! /usr/bin/env python3
# coding: utf-8


""" Reolink Configuration file """

class config:
    name = ""
    ip = ""
    port = ""
    user = ""
    password = ""
    storage = ""
    dl_age = 4
    tl_age = 3

fr_allee = config()
fr_allee.name="Frenes Allee"
fr_allee.ip="x.x.x.x"
fr_allee.port="82"
fr_allee.user="admin"
fr_allee.password="mypassword"
fr_allee.storage="/home/lebomb/cams/Frenes/Allee"

fr_veranda = config()
fr_veranda.name="Frenes Veranda"
fr_veranda.ip="x.x.x.x"
fr_veranda.port="83"
fr_veranda.user="admin"
fr_veranda.password="mypassword"
fr_veranda.storage="/home/lebomb/cams/Frenes/Veranda"

bt_panoramix = config()
bt_panoramix.name="Bourdilot Panoramix"
bt_panoramix.ip="x.x.x.x"
bt_panoramix.port="89"
bt_panoramix.user="admin"
bt_panoramix.password="mypassword"
bt_panoramix.storage="/home/lebomb/cams/Bourdilot/Panoramix"

np_facade = config()
np_facade.name="Niepce Facade"
np_facade.ip="x.x.x.x"
np_facade.port="80"
np_facade.user="admin"
np_facade.password="mypassword"
np_facade.storage="/home/lebomb/cams/Niepce/Facade"

myconfig_list = { bt_panoramix, np_facade, fr_veranda, fr_allee }

