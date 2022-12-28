from peewee import *
from scilla_db import gate

database = SqliteDatabase("test.db")
database.connect()


class __BaseModel(Model):
    class Meta:
        database = database


class AccountModel(__BaseModel):
    account_username = CharField(unique=True, default="")
    account_password = CharField(default="")
    account_email = CharField(default="")
    account_salt = CharField(default="")


class DataModel(__BaseModel):
    account = ForeignKeyField(AccountModel, backref='account-data')
    data = TextField(default="")
    nonce = CharField(default="")


def get_account(
    username: str = ""
) -> AccountModel:
    gate.username_valid(username)
    __result = None
    try:
        __result = AccountModel.get(
            AccountModel.account_username == username
        )
    finally:
        return __result


def create_account(
    username: str = "",
    password: str = "",
    email: str = ""
) -> AccountModel:
    gate.username_valid(username=username)
    gate.password_valid(password=password)

    if get_account(username) is AccountModel:
        raise Exception(
            "Account with that username already exists."
        )
