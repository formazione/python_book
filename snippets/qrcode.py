import pyqrcode
address = "https://www.youtube.com/watch?v=iy2aKf9AAvc"
url = pyqrcode.create(address)
# url.svg('uca-url.svg', scale=8)
# url.eps('uca-url.eps', scale=2)
url.png('uca-url.png', scale=8)
print(url.terminal(quiet_zone=1))
