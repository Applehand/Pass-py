import sqlite3

def initialize_db():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_name TEXT NOT NULL UNIQUE,
        encrypted_password BLOB NOT NULL
    )
    ''')
    
    connection.commit()
    cursor.close()
    connection.close()

def execute_db_query(query_func, *args):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    
    try:
        result = query_func(cursor, *args)
        connection.commit()
        return result
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        cursor.close()
        connection.close()

def add_account(account, encrypted_pass):    
    def query(cursor, account, encrypted_pass):
        cursor.execute("INSERT INTO accounts (account_name, encrypted_password) VALUES (?, ?)", (account, encrypted_pass))
    
    execute_db_query(query, account, encrypted_pass)

def get_password(account):
    def query(cursor, account):
        cursor.execute("SELECT encrypted_password FROM accounts WHERE account_name = ?", (account,))
        return cursor.fetchone()
    
    result = execute_db_query(query, account)
    return result[0] if result else None

def update_password(account, encrypted_pass):
    def query(cursor, account, encrypted_pass):
        cursor.execute("UPDATE accounts SET encrypted_password = ? WHERE account_name = ?", (encrypted_pass, account))
    
    execute_db_query(query, account, encrypted_pass)

def delete_account(account):
    def query(cursor, account):
        cursor.execute("DELETE FROM accounts WHERE account_name = ?", (account,))
    
    execute_db_query(query, account)

def list_accounts():
    def query(cursor):
        cursor.execute("SELECT account_name FROM accounts")
        return cursor.fetchall()
    
    accounts = execute_db_query(query)
    if accounts:
        return [account for account in accounts]
    else:
        return []
