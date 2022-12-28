def __generic_datatype_mismatch(
    value_str: str = "",
    value_type: type = "",
    value_name: str = "",
    expected_name: str = ""
):
    raise Exception(
        "%s is not a %s, got: '%s'[%s]" % (
            value_name,
            expected_name,
            value_str,
            value_type
        )
    )


def __generic_string_length(
    value_str: str = "",
    value_length: int = 1,
    value_name: str = "",
    too_type: str = ""
):
    raise Exception(
        "%s is too %s, %d char(s) long. '%s'" % (
            value_name,
            too_type,
            value_length,
            value_str
        )
    )


def username_valid(
    username: str = ""
):
    __username_type = type(username)
    __username_str = str(username)

    if __username_type is not str:
        __generic_datatype_mismatch(
            value_str=__username_str,
            value_type=__username_type,
            value_name="Username",
            expected_name="string"
        )

    __username_len = len(username)
    __too_something = __username_len < 3 or __username_len > 16

    if __too_something is True:
        __generic_string_length(
            value_str=__username_str,
            value_length=__username_len,
            value_name="Username",
            too_type=__username_len < 3 and "short" or "long"
        )


def password_valid(
    password: str = ""
):
    __password_type = type(password)
    __password_str = str(password)

    if __password_type is not str:
        __generic_datatype_mismatch(
            value_str=__password_str,
            value_type=__password_type,
            value_name="Password",
            expected_name="string"
        )

    __password_len = len(password)
    __too_something = __password_len < 8 or __password_len > 16

    if __too_something is True:
        __generic_string_length(
            value_str="#"*__password_len,
            value_length=__password_len,
            value_name="Password",
            too_type=__password_len < 3 and "short" or "long"
        )


