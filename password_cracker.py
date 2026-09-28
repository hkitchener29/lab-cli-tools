from zipfile import ZipFile

with open('Ashley-Madison.txt') as f:
    passwords = f.read().splitlines()


with ZipFile('whitehouse_secrets.zip') as zf:
        for opt in passwords:
            try:
                zf.extractall(pwd=opt.encode())
                print (opt)
            except:
                pass