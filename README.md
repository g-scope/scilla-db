# scilla-db

Welcome to scilla-db, a simple database tool for storing & automatically encrypting/decrypting account data.

The goal of this package is to create the easiest way to make accounts with encrypted data builtin.

This is not a scalable package, this is meant for small projects.

### How to use?
* Create an Account:
    ```python
    import scilla_db
      
    new_account, _err = scilla_db.create_account(
        username="username",
        password="password"  
    )
  
    if _err is not None:
        raise _err
  
    # Account creation succcessful!
    print(new_account.account_username) # username
    ```
* Assign Data to Account:
    ```python
    import scilla_db
    
    account, _err = scilla_db.get_account(
        username="username"
    )
    
    if _err is not None:
        raise _err
    
    new_data = {
        "hi": "i'm data!"
    }
  
    account_data, _err = scilla_db.set_data(
        account=account,
        password="password",
        data=new_data
    )
  
    if _err is not None:
        raise _err
    
    # successfully assigned and encrypted data to database!
    ```
* Get Data from Account:
  ```python
  import scilla_db
    
  account, _err = scilla_db.get_account(
    username="username"
  )
    
  if _err is not None:
    raise _err
    
  data, _err = scilla_db.get_data(
    account=account,
    password="password"
  )
  
  if _err is not None:
    raise _err
    
  # successfuly retrieved and decrypted data!
  print(data.get("hi")) #i'm data!
  ```