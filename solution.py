import zipfile
from os import getcwd, listdir, chdir
import shutil
Name=""
Origin=getcwd()+"/"
while True:
    listing=listdir()
    print(listing)
    f=""
    for f in listing:
        if 'zip' in f.split('.'):break
    if f=="":break
    d=f.split('.')[0]
    try:
        with zipfile.ZipFile(f,'r') as zip_ref:
            zip_ref.extractall()
    except: break
    if d !="unzipMe200":chdir(d)
    else :break
with zipfile.ZipFile("FinalWork.zip",'r') as zip_ref:
    zip_ref.extractall()

shutil.move("Congratulations.pdf", Origin+"Congratulations.pdf")