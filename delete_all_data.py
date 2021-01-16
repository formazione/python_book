# Unzip the files in a zipped file in the same dir of this script
import os
import shutil
import glob
import zipfile

def unzip(name):
    "Unzip zipped file"
    with zipfile.ZipFile(name, 'r') as zip_ref:
    	zip_ref.extractall(".")


def delete_all_data():
	"This will erase all the data in the snippets folder"
	
	folders = glob.glob("G:\\*_book")
	ind = folders.index("G:\\python_book")
	folders.pop(ind)
	print("Cartelle:")
	print(*folders, sep="\n")
	for fold in folders:
		os.chdir(fold)
		unzip("G:\\python_book\\book.zip")


unzip()