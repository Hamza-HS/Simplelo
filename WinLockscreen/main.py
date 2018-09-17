""" Script for extracting Windows Lockscreens """

import os
from os.path import getsize, exists
from shutil import copy2

def make_newdir(newpath):
    if not exists(newpath):
        os.makedirs(newpath)

def extract_photos(path, newpath, photos):
    n = 1
    for photo in photos:
        size = getsize(fr"{path}\{photo}") / 1000
        if size > 150:
            copy2(fr"{path}\{photo}", fr"{newpath}\photo-{n}.jpg")
            n += 1

def main():
    try:
        PATH = fr"C:\Users\{os.getlogin()}\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
        NEWPATH = f"Windows Lockscreens"

        photos = os.listdir(PATH)
        make_newdir(NEWPATH)
        extract_photos(PATH, NEWPATH, photos)
        print("Successful! :)")
    except Exception:
        print("Unsuccessful! Looks like there is an error. :(")

if __name__ == "__main__":
    main()