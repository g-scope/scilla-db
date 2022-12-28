from peewee import *

__database = SqliteDatabase("test.db")
__database.connect()


class BaseModel(Model):
    class Meta:
        global __database
        database = __database


class AccountModel(BaseModel):
    account_username = CharField(unique=True,default="")
    account_password = CharField(default="")
    account_email = CharField(default="")
    account_salt = CharField(default="")


class DataModel(BaseModel):
    account = ForeignKeyField(AccountModel, backref='account-data')
    data = TextField(default="")
    nonce = CharField(default="")