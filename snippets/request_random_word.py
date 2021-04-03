from urllib.request import Request, urlopen
import random


url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')
first500 = webpage.split("\n")[:500]
f = random.sample(first500, 10)
print(f)