import os

from peewee import SqliteDatabase, Model, CharField, IntegerField

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
class Chapa(BaseModel):
    name = CharField()
    votes = IntegerField(default=0)

    def get_data(self):
        return self.__dict__['__data__']

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self) -> str:
        return str(self.name)

class Data(BaseModel):
    key = CharField()
    value = CharField()

    @classmethod
    def get_value(cls, key, default=None):
        obj = Data.get_or_none(key=key)
        return obj.value if obj else default

db.connect()

db.create_tables([Chapa, Data], safe=True)
