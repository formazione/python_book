import grab
import os


print("Loads the most updated book")
file = grab.grab("book29*.py")[-1]
os.startfile(file)