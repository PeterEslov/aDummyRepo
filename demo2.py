import zipfile
import shutil

print("Nu kör vi så det ryker....")
# NOTE comment out each section before you run it 

# Create a ZIP file..med two files
with zipfile.ZipFile('Files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('PB.docx')
    my_zip.write('Prosit.jpg')

# Extracting from a zip file
with zipfile.ZipFile('Files.zip', 'r') as my_zip:
    my_zip.extractall('files')
    print(my_zip.namelist())

# Extracting a single file from a zip file
with zipfile.ZipFile('Files.zip', 'r') as my_zip:
    my_zip.extract('Prosit.jpg')

# Before this, comment out all code above
#shutil.make_archive('another', 'zip', 'files')

shutil.unpack_archive('another.zip','another')

print("Nu var det klart.")