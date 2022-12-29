from scilla_db import database
from scilla_db import gate


def create_account(
    username: str = "",
    password: str = ""
) -> (database.AccountModel, Exception):
    __result, __exception = None, None
    try:
        __result = database.create_account(
            username=username,
            password=password
        )
    except Exception as e:
        __exception = e
    finally:
        return __result, __exception


def get_account(
    username: str = ""
) -> (database.AccountModel, Exception):
    __result, __exception = None, None
    try:
        __result = database.get_account(
            username=username
        )
    except Exception as e:
        __exception = e
    finally:
        return __result, __exception


def set_data(
    account: database.AccountModel,
    password: str = "",
    data: dict = ()
) -> (bool, Exception):
    __result, __exception = False, None
    try:
        __result = database.encrypt_and_overwrite_account_data(
            account=account,
            password=password,
            data=data
        )
    except Exception as e:
        __exception = e
    finally:
        return __result, __exception


def get_data(
    account: database.AccountModel,
    password: str = ""
) -> (dict, Exception):
    __result, __exception = None, None
    try:
        __result = database.get_decrypted_account_data(
            account=account,
            password=password
        )
    except Exception as e:
        __exception = e
    finally:
        return __result, __exception
