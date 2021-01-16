import os
from glob import glob


last_file = glob("book2*.py")[-1]
print(last_file)
os.startfile(last_file)