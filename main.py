import scilla_db

new_account, __acc_failure = scilla_db.create_account(
    username="cool_guy",
    password="coolpassword"
)

if __acc_failure is not None:
    print("Account Creation Failed: " + str(__acc_failure))

target_data = {
    "look_at_me": "i'm data!",
    "hey": "how are ya!"
}

success, __fail_msg = scilla_db.set_data(
    account=new_account,
    password="coolpassword",
    data=target_data
)

if not success:
    print("set_data failed!: " + str(__fail_msg))

data, __err = scilla_db.get_data(
    account=new_account,
    password="coolpassword"
)

if __err is not None:
    print("get_data failed!: " + str(__err))
else:
    print("Hi!", data.get("hey"))