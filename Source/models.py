import os

from peewee import SqliteDatabase, Model, CharField, TextField, DateField

path = os.path.join(os.environ.get('LOCALAPPDATA'), 'SysGremio')

if not os.path.exists(path):
    os.mkdir(path)

db = SqliteDatabase(
    os.path.join(path, 'database.db')
)

class BaseModel(Model):
    class Meta:
        database = db


# Create your models here.
class Cliente(BaseModel):
    nome = CharField(max_length=50)
    data_nasc = DateField()
    tel = CharField(max_length=20)
    email = CharField()
    endereco = TextField()
    cpf = CharField(max_length=14)
    rg = CharField(max_length=12)

    def __str__(self) -> str:
        return str(self.nome)

    def get_data(self) -> dict:
        return self.__dict__['__data__']

db.connect()

db.create_tables([Cliente], safe=True)
