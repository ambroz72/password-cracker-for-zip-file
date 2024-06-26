from termcolor import colored
from tqdm import tqdm
import zipfile

var =""
worldlist = [passwords.strip() for passwords in open("worldlist.txt")]
zip_file = zipfile.ZipFile("zero.zip")

for i in tqdm(worldlist,desc="Checking password in worldlist"):
    try:
        zip_file.extractall(pwd=i.encode())
        var=i
        print(colored ("[+] Password Found: {}".format(var),'green'))
        break
    except :
        continue
