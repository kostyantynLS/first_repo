from zipfile import ZipFile

file_name = "archive.zip"

with ZipFile(file_name, 'r') as zip:
    zip.printdir()
    # extracting all the files
    zip.extractall()

import os
import zipfile

def zip_doc_files(output_zip, file_pattern):
   with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
       for root, dirs, files in os.walk('.'):
           for filename in files:
               if filename.endswith(file_pattern):
                   abs_file_path = os.path.abspath(os.path.join(root, filename))
                   zipf.write(abs_file_path, arcname=os.path.relpath(abs_file_path, '.'))

output_zip = "doc_files.zip"
file_pattern = "*.doc"
zip_doc_files(output_zip, file_pattern)


import os
import zipfile
from datetime import datetime

def zip_txt_files():
    # Check if *.txt files exist
    txt_files = []
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if filename.endswith('.txt'):
                txt_files.append(os.path.abspath(os.path.join(root, filename)))

    if not txt_files:
        print("No .txt files found.")
        return

    # Create a ZIP file with the current date as its name
    now = datetime.now()
    zip_filename = f"{now.year}-{now.month}-{now.day}.zip"

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for txt_file in txt_files:
            zipf.write(txt_file, arcname=os.path.relpath(txt_file, '.'))

    print(f"ZIP file '{zip_filename}' created successfully.")

zip_txt_files()