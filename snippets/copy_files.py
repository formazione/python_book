import os
import shutil
import glob

''' Take last version of a file and copy to folders ending with _book '''

# Take the last version of book
book = glob.glob("G:\\python_book\\book2*.py")[-1].split("\\")[-1]

# list of all the books folders
folders = glob.glob("G:\\*_book")

# delete the python_book from the folders
ind = folders.index("G:\\python_book")
folders.pop(ind)

print("Cartelle:")
print(*folders, sep="\n")
print()
print("To copy:")
print(book)
print()
for fold in folders:
	print(fold, book)
	shutil.copy(book, fold)


