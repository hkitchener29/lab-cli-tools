from zipfile import ZipFile

with open('Ashley-Madison.txt') as f:
    passwords = f.read().splitlines()

found = False
with ZipFile('whitehouse_secrets.zip') as zf:
        for opt in passwords:
            try:
                zf.extractall(pwd=opt.encode())
                print ('Password found:', opt)
                found = True
                break
            except:
                pass

if not found:
    print('Password not found.')