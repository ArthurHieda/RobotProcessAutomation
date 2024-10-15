from pony.orm import DataBase, Required, PrimaryKey, Option
import datetime

db = DataBase()

class LogEvento(db.Entity):
    id = PrimaryKey(int, auto=True)
    descricao = Optional(str)
    tipo = Optional(str)
    data_criacao = Optional(datetime.datetime, default=datetime.datetime.now)
    usuario = Optional(str)

class Usuario(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str, unique=True)
    hashed_password = Required(str)

db.bind(provider='sqlite', filename='database.sqlite', create_db=True) #Nunca abrir o arquivo database.sqlite senão você perderá o banco de dados
db.generate_mapping(create_tables=True)