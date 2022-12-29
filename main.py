import scilla_db

new_account = scilla_db.database.get_account(
    username="username",
)

current_data = scilla_db.database.encrypt_and_overwrite_account_data(
    account=new_account,
    password="password",
    data={
        "ha": "ha1!"
    }
)

returned_data = scilla_db.database.get_decrypted_account_data(
    account=new_account,
    password="password"
)

print(returned_data.get("ha"))