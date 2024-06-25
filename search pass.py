from termcolor import colored
from tqdm import tqdm
import zipfile

var = ""
worldlist = [passwords.strip() for passwords in open("worldlist.txt")]
zip_file = zipfile.ZipFile("ufo.zip")

for password in tqdm(worldlist, desc="Checking passwords in worldlist"):
    try:
        password_bytes = password.encode('utf-8')  # Encode password as bytes
        zip_file.extractall(pwd=password_bytes)
        var = password
        print(colored("[+] Password Found: {}".format(var), 'green'))
        break
    except RuntimeError as e:
        continue
    except Exception as e:
        print(colored("[-] Failed with password: {}".format(password), 'red'))
        print(e)
        continue
