import scilla_db

new_account = scilla_db.database.create_account(
    username="username",
    password="password"
)

new_data = scilla_db.database.create_account_data(
    account=new_account,
    data={
        "wah": "wah2?"
    }
)