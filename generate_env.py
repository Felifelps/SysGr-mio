import getpass

from bcrypt import hashpw, gensalt

bytes_pw = getpass.getpass().encode()
bytes_hashed_pw = hashpw(bytes_pw, gensalt())
str_hashed_pw = str(bytes_hashed_pw)[2:-1]

with open('.env', 'w', encoding='utf-8') as file:
    file.write(f"SYSGREMIO={str_hashed_pw}")

print('Env generated succesfully')
