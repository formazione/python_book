# Unzip the files in a zipped file in the same dir of this script
import os
import shutil
import glob
import zipfile

def unzip(name):
    "Unzip zipped file"
    with zipfile.ZipFile(name, 'r') as zip_ref:
    	zip_ref.extractall(".")


unzip()