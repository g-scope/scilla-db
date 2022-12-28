from peewee import *
from scilla_db import gate
import secrets
import hashlib
import base64

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


database.create_tables([AccountModel, DataModel])


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
) -> AccountModel:
    gate.username_valid(username=username)
    gate.password_valid(password=password)

    if get_account(username) is not None:
        raise Exception(
            "Account with that username already exists."
        )

    salt = secrets.token_bytes(16)

    new_account = AccountModel.create(
        account_username=username,
        account_password=base64.b64encode(
            hashlib.sha256(
                password.encode()
            ).digest()
        ),
        account_salt=base64.b64encode(salt)
    )

    return new_account
