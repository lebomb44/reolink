# Overview
*rsync.py* will donwload the files from the sd card of the camera to the current folder
If the file already exists and has the same size of the remote one it will not be downloaded again

# Set up your configuration
Create a file named "myconfig.py" with the following variables

```python
ip="xxx.xxx.xxx.xxx"
port="80"
user="myusername"
password="mypassword"
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
