import zipfile

def unzip(name):
    "Unzip zipped file"
    with zipfile.ZipFile(name, 'r') as zip_ref:
        zip_ref.extractall(".")

unzip("G:\\python_book\\book_update.zip")