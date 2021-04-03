import os
import shutil
import glob
from time import sleep
# book = glob.glob("G:\\python_book\\book2*.py")[-1].split("\\")[-1]
# folders = glob.glob("G:\\*_book")
# ind = folders.index("G:\\python_book")
# folders.pop(ind)
# folders = [x for x in folders if x != "python_book"]
# # folders += glob.glob("G:\\pymemo_*")
# print("Cartelle:")
# print(*folders, sep="\n")
# print()
# print("To copy:")
# print(book)
# print()

def copyfolder(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
def start():
	# copies the main file
	for fold in folders:
		print(f"copy in: {fold=}")
		shutil.copy("G:\\python_book\\" + book, fold)
		print(f"copied: {book=}\n")

	# for file in os.listdir("code"):
	# 	if file != "__init__.py" or file != "__pycache__":
	# 		print(f"To copy: {file=}")
	# 		print(f"in folder: {fold=}\\code\\\n")
	for fold in folders:
		print(fold)
		copyfolder("G:\\python_book\\code\\", fold )
	# copies the code folder
import errno, stat

def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise

books = [x for x in os.listdir("G:\\") if x.endswith("_book") if x != "python_book"]
print(books)
for fold in books:
	if os.path.isdir(f"G:\\{fold}\\code"):
		shutil.rmtree(f"G:\\{fold}\\code", ignore_errors=False, onerror=handleRemoveReadonly)
	else:
		os.mkdir(f"G:\\{fold}\\code")
		shutil.rmtree(f"G:\\{fold}\\code", ignore_errors=False, onerror=handleRemoveReadonly)

for fold in books:
	shutil.copytree("G:\\python_book\\code", f"G:\\{fold}\\code")