import os
import shutil
import glob

book = glob.glob("G:\\python_book\\book2*.py")[-1].split("\\")[-1]
folders = glob.glob("G:\\*_book")
ind = folders.index("G:\\python_book")
folders.pop(ind)
folders = [x for x in folders if x != "python_book"]
# folders += glob.glob("G:\\pymemo_*")
print("Cartelle:")
print(*folders, sep="\n")
print()
print("To copy:")
print(book)
print()
for fold in folders:
	print(fold, book)
	shutil.copy("G:\\python_book\\" + book, fold)