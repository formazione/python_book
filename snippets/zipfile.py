# Unzip the files in a zipped file in the same dir of this script

import zipfile

with zipfile.ZipFile("pymemo.zip", 'r') as zip_ref:
    zip_ref.extractall(".")
