from pykeepass import PyKeePass
from pykeepass.exceptions import CredentialsError

filename = 'DATABASE.kdbx'  # Enter name of keepass database

with open('passwords.txt', 'r', encoding='utf-8') as f:
    for line in f:
        password = line.strip()
        if not password:
            continue
        try:
            kp = PyKeePass(filename, password=password)
            print("\n \n Password has been found. Your password is " + password)
            break
        except CredentialsError:
            print("Trying password:  " + password)
        except Exception as e:
            print(f"Error testing '{password}': {e}")

