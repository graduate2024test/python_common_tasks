import zipfile

with zipfile.ZipFile("new.zip","r") as zip_ref:
    zip_ref.extractall("targetdir")
    
print('complite!')
