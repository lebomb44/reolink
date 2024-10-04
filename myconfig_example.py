#! /usr/bin/env python3
# coding: utf-8


""" Reolink Configuration file """

class config:
    name = ""
    ip = ""
    port = "80"
    user = "user"
    password = "password"
    url_ext = ""
    storage = ""
    dl_age = 4
    tl_age = 3

fr_allee = config()
fr_allee.name="Frenes Allee"
fr_allee.ip="192.168.1.152"
fr_allee.url_ext = "https://mysite.com/camallee"
fr_allee.storage="/home/osmc/cams/Frenes/Allee"

fr_veranda = config()
fr_veranda.name="Frenes Veranda"
fr_veranda.ip="192.168.1.153"
fr_veranda.url_ext = "https://mysite.com/camveranda"
fr_veranda.storage="/home/osmc/cams/Frenes/Veranda"

bt_facade = config()
bt_facade.name="Bourdilot Facade"
bt_facade.ip="192.168.10.155"
bt_facade.url_ext = "https://mysite.com/camfacade"
bt_facade.storage="/home/osmc/cams/Bourdilot/Facade"

bt_galerie = config()
bt_galerie.name="Bourdilot Galerie"
bt_galerie.ip="192.168.10.157"
bt_galerie.url_ext = "https://mysite.com/camgalerie"
bt_galerie.storage="/home/osmc/cams/Bourdilot/Galerie"

bt_panoramix = config()
bt_panoramix.name="Bourdilot Panoramix"
bt_panoramix.ip="192.168.10.158"
bt_panoramix.url_ext = "https://mysite.com/campanoramix"
bt_panoramix.storage="/home/osmc/cams/Bourdilot/Panoramix"

bt_entree = config()
bt_entree.name="Bourdilot Entree"
bt_entree.ip="192.168.10.159"
bt_entree.url_ext = "https://mysite.com/camentree"
bt_entree.storage="/home/osmc/cams/Bourdilot/Entree"

np_entree = config()
np_entree.name="Niepce Entree"
np_entree.ip="192.168.10.151"
np_entree.url_ext = "https://mysite.com/camentree"
np_entree.storage="/media/HDD/cams/Niepce/Entree"

np_facade = config()
np_facade.name="Niepce Facade"
np_facade.ip="192.168.10.152"
np_facade.url_ext = "https://mysite.com/camfacade"
np_facade.storage="/media/HDD/cams/Niepce/Facade"

np_terrasse = config()
np_terrasse.name="Niepce Terrasse"
np_terrasse.ip="192.168.10.153"
np_terrasse.url_ext = "https://mysite.com/camterrasse"
np_terrasse.storage="/media/HDD/cams/Niepce/Terrasse"

myconfig_list = { fr_allee, fr_veranda }
myconfig_list = { bt_facade, bt_galerie, bt_panoramix, bt_entree }
myconfig_list = { np_entree, np_facade, np_terrasse }

