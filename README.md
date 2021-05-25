# Overview
*rsync.py* will donwload the files from the sd card of the camera to the current folder
If the file already exists and has the same size of the remote one it will not be downloaded again

# Set up your configuration
Create a file named "myconfig.py" with the following variables

```python
#! /usr/bin/env python3
# coding: utf-8


""" Reolink COnfiguration file """

class config:
    ip = ""
    port = ""
    user = ""
    password = ""
    output = ""

fr_allee = config()
fr_allee.ip="x.x.x.x"
fr_allee.port="x"
fr_allee.user="x"
fr_allee.password="x"
fr_allee.output="/path/to/allee"

fr_veranda = config()
fr_veranda.ip="x.x.x.x"
fr_veranda.port="x"
fr_veranda.user="x"
fr_veranda.password="x"
fr_veranda.output="/path/to/veranda"

bt_panoramix = config()
bt_panoramix.ip="x.x.x.x"
bt_panoramix.port="x"
bt_panoramix.user="x"
bt_panoramix.password="x"
bt_panoramix.output="/path/to/panoramix"

```

# Run the script
```console
> python3 rsync.py 
Rec_20210313_150125_541_M.mp4 already downloaded (13483587 bytes)
Rec_20210313_150250_541_M.mp4 already downloaded (14720848 bytes)
Rec_20210313_160824_541_M.mp4 already downloaded (14180924 bytes)
Rec_20210313_175841_541_M.mp4 already downloaded (12486711 bytes)
Rec_20210314_010047_541_M.mp4 already downloaded (9546709 bytes)
Rec_20210314_065857_541_M.mp4 already downloaded (14665120 bytes)
Downloading Rec_20210314_090509_541_M.mp4 (42660376 bytes)
 39% [............................                                            ] 16703488 / 42660376
```
