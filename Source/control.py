import os
import winreg

from bcrypt import checkpw
from dotenv import load_dotenv

from .models import Data, Chapa

load_dotenv()

with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders") as key:
    desktop_dir, _ = winreg.QueryValueEx(key, "Desktop")

class Control:
    desktop_dir = desktop_dir.replace(
        '%USERPROFILE%', 
        os.environ.get('USERPROFILE')
    )
    pw = os.environ.get('SYSGREMIO').encode('utf-8')

    @classmethod
    def check_credentials(cls, password: str):
        return checkpw(
            password.encode('utf-8'),
            cls.pw
        )

    @classmethod
    def get_and_save_results(cls):
        chapas = list(sorted(Chapa.select(), key=lambda c: c.votes, reverse=True))

        votes = 0
        results = []
        for c in chapas:
            votes += c.votes
            results.append(
                f'{c.name}: {c.votes} voto{"" if c.votes == 1 else "s"}'
            )
            c.votes = 0
            c.save()

        file_path = os.path.join(
            cls.desktop_dir,
            f'votacao-{Data.get_value("ID_VOTACAO")}.txt',
        )

        with open(
            file_path, 'w', encoding='utf-8'
        ) as file:
            file.write('\n'.join(results))

        return results, votes, file_path

    @classmethod
    def start_voting(self):
        vote_id = Data.get_or_none(key="ID_VOTACAO")
        if vote_id:
            vote_id.value = int(vote_id.value) + 1
            vote_id.save()
        else:
            Data.create(key="ID_VOTACAO", value="1")
