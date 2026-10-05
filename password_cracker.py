from zipfile import ZipFile

with open('Ashley-Madison.txt') as f:
    passwords = [line.strip() for line in f]

found = False
with ZipFile('whitehouse_secrets.zip') as zf:
        for opt in passwords:
            try:
                zf.extractall(pwd=opt.encode())
                print ('Password found:', opt)
                found = True
                break
            except RuntimeError as e:
                print("ZIP operation failed:", e)
            except Exception as e:
                print("Unexpected error:", e)

if not found:
    print('Password not found.')