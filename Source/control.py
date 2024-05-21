import os

from bcrypt import checkpw
from dotenv import load_dotenv

load_dotenv()

class Control:
    log_file_path = os.path.join(
        os.environ.get('LOCALAPPDATA'),
        'log.log'
    )
    login = os.environ.get('DEVSYSTEMS_L_DATA').encode('utf-8')
    pw = os.environ.get('DEVSYSTEMS_S_DATA').encode('utf-8')
    @classmethod
    def check_credentials(cls, login: str, password: str):
        return checkpw(
            login.encode('utf-8'),
            cls.login
        ) and checkpw(
            password.encode('utf-8'),
            cls.pw
        )

    @classmethod
    def validate_form(cls, data: dict):
        for i in data:
            data[i] = data[i].strip()

        if '' in list(data.values()) or len(data) != 7:
            return 'Preencha todos os campos!'

        name = data['nome']
        if not name.count(' '):
            return 'Digite seu nome completo!'

        email = data['email']
        if any([
            '@' not in email,
            ' ' in email,
            '.' not in email.split('@')[-1],
            len(email) < 14,
            len(email) > 256,
        ]):
            return 'Email inválido!'

        tel = data['tel']
        if len(tel.replace(' ', '')) not in range(10, 14):
            return 'Telefone inválido!'

        cpf = data['cpf']
        if not cpf.isdigit():
            return 'Digite apenas os dígitos do CPF!'
        if len(cpf) != 11:
            return 'CPF inválido!'

        rg = data['rg']
        if not rg.isdigit():
            return 'Digite apenas os dígitos do RG!'
        if len(rg) != 11:
            return 'RG inválido!'

        return None

    @classmethod
    def log(cls, e):
        with open(cls.log_file_path, 'w', encoding='utf-8') as f:
            f.write(str(e))
