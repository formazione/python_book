from urllib import request
import os



def download_shakespeare(books):
	"Download all the files in the books multiline string"
	books = books[1:].split("\n\n")
	books = [x.split("\n") for x in books]
	print(books)
	title = [data[0] for data in books]
	address = [data[1] for data in books]
	print(title)
	for n, x in enumerate(books):
		if title[n] not in os.listdir():
			request.urlretrieve(address[n], title[n])
			os.startfile(title[n])

books = """
Hamlet.txt
https://gist.githubusercontent.com/provpup/2fc41686eab7400b796b/raw/b575bd01a58494dfddc1d6429ef0167e709abf9b/hamlet.txt

Romeo_and_Juliet.txt
https://www.gutenberg.org/files/1112/1112.txt

Othello.txt
https://formazione.github.io/books/Othello.txt
"""

download_shakespeare(books)