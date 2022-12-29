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

