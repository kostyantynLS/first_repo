from zipfile import ZipFile

file_name = "archive.zip"

with ZipFile(file_name, 'r') as zip:
    zip.printdir()
    # extracting all the files
    zip.extractall()