import sys

from bcrypt import hashpw, gensalt

if len(sys.argv) != 2:
    print('The correct syntax is:\n    python generate_env.py <your-password>')
    sys.exit()

bytes_pw = sys.argv[-1].encode()
bytes_hashed_pw = hashpw(bytes_pw, gensalt())
str_hashed_pw = str(bytes_hashed_pw)[2:-1]

with open('.env', 'w', encoding='utf-8') as file:
    file.write(f"SYSGREMIO={str_hashed_pw}")
