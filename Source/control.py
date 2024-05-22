import os

from bcrypt import checkpw
from dotenv import load_dotenv

load_dotenv()

class Control:
    log_file_path = os.path.join(
        os.environ.get('LOCALAPPDATA'),
        'log.log'
    )
    pw = os.environ.get('DEVSYSTEMS_S_DATA').encode('utf-8')
    @classmethod
    def check_credentials(cls, password: str):
        return checkpw(
            password.encode('utf-8'),
            cls.pw
        )
