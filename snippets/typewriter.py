''' typewriter.py '''

import sys, time
from random import randrange

# create a file with a text varibale with the content and import this
# then texttime(text)

def typewrite(words):
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        # if c == " ":
        if randrange(1, 5) == 3:
            time.sleep(0.1)

print("You must texttime(text)")
text = "This is an example"
text += "."*100

if __name__ == "__main__":
    typewrite(text)











