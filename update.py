import os
import shutil
import glob
from time import sleep
import errno, stat
book = glob.glob("G:\\python_book\\book2*.py")[-1].split("\\")[-1]


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
	for fold in books:
		print(f"copy in: {fold=}")
		shutil.copy("G:\\python_book\\" + book, fold)
		print(f"copied: {book=}\n")



def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise
books = [x for x in os.listdir("G:\\") if x.endswith("_book") if x != "python_book"]
print(books)
start()
for fold in books:
	# check if there is a folder called code
	if os.path.isdir(f"G:\\{fold}\\code"):
		# delete it
		shutil.rmtree(f"G:\\{fold}\\code", ignore_errors=False, onerror=handleRemoveReadonly)
	else:
		# if there is not, it create it and then delete it (I may have done some stupid code here, but it works)
		os.mkdir(f"G:\\{fold}\\code")
		shutil.rmtree(f"G:\\{fold}\\code", ignore_errors=False, onerror=handleRemoveReadonly)

for fold in books:
	# copies all the folder in a new position (fold)
	shutil.copytree("G:\\python_book\\code", f"G:\\{fold}\\code")