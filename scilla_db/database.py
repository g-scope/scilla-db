from peewee import *
from scilla_db import gate
import secrets
import hashlib
import base64
import json

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


def decrypt_and_return_account_data(
    account: AccountModel,
    password: str = ""
) -> DataModel:
    pass


def encrypt_and_overwrite_account_data(
    account: AccountModel,
    password: str = "",
    data: dict = {}
) -> bool:
    pass


def get_data_by_account(
    account: AccountModel
) -> DataModel:
    __result = None
    try:
        __result = DataModel.get(
            DataModel.account == account
        )
    finally:
        return __result


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
        account_password=hashlib.sha256(
            password.encode()
        ).hexdigest(),
        account_salt=base64.b64encode(salt)
    )

    return new_account


def create_account_data(
    account: AccountModel,
    data: dict = {}
) -> DataModel:
    __account_type = type(account)
    __account_str = str(account)

    __data_type = type(data)
    __data_str = str(data)

    if __account_type is not AccountModel:
        gate.__generic_datatype_mismatch(
            value_str=__account_str,
            value_type=__account_type,
            value_name="Account",
            expected_name="AccountModel"
        )

    if __data_type is not dict:
        gate.__generic_datatype_mismatch(
            value_str=__data_str,
            value_type=__data_type,
            value_name="Data",
            expected_name="dictionary"
        )

    __existing_data = get_data_by_account(
        account=account
    )

    if __existing_data is not None:
        return __existing_data
    else:
        __new_data = DataModel.create(
            account=account,
            data=json.dumps(data),
            nonce=""
        )

        __new_data.save()

        return __new_data
