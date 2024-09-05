import passpy.storage as storage
import passpy.crypto as crypto
import argparse
import pyperclip

fernet_key = crypto.get_fernet_key()

parser = argparse.ArgumentParser(
    prog="Passpy",
    description="A simple and secure CLI tool for storing passwords."
    )
subparsers = parser.add_subparsers(dest="command")

# Add command
parser_add = subparsers.add_parser("add", help="Add a new account and an associated password.")
parser_add.add_argument("account", help="The username, email, or domain to be associated with a password.")
parser_add.add_argument("password", help="The password to be securely stored and associated with an account.")

# Get command
parser_get = subparsers.add_parser("get", help="Retrieve a password for an account.")
parser_get.add_argument("account", help="The username, email, or domain to retrieve the password for.")

# Update command
parser_update = subparsers.add_parser("update", help="Update an existing password with a new one.")
parser_update.add_argument("account", help="The username, email, or domain to update the password for.")
parser_update.add_argument("password", help="The new password that will replace the old one.")

# Delete command
parser_delete = subparsers.add_parser("delete", help="Delete an account.")
parser_delete.add_argument("account", help="The username, email, or domain to delete.")

# List command
parser_list = subparsers.add_parser("list", help="List all accounts.")

args = parser.parse_args()

def main():
    if not args.command:
        list_accounts()
    elif args.command == "add":
        add_account(args.account, args.password)
    elif args.command == "get":
        get_account(args.account)
    elif args.command == "update":
        update_password(args.account, args.password)
    elif args.command == "delete":
        delete_account(args.account)
    elif args.command == "list":
        list_accounts()

def add_account(account, password):
    encryped_pass = crypto.encrypt_password(password, fernet_key)
    storage.add_account(account, encryped_pass)
    print(f"Account '{account}' added successfully.")

def get_account(account):
    encryped_pass = storage.get_password(account)
    if not encryped_pass:
        print("Account not found.")
        return
    password = crypto.decrypt_password(encryped_pass, fernet_key)
    pyperclip.copy(password)
    print("Password copied to clipboard!")

def update_password(account, password):
    new_encryped_password = crypto.encrypt_password(password, fernet_key)
    storage.update_password(account, new_encryped_password)
    print(f"Password for '{account}' updated successfully.")

def delete_account(account):
    result = storage.delete_account(account)
    print(result)

def list_accounts():
    accounts = storage.list_accounts()
    if accounts:
        print("Accounts:")
        for account in accounts:
            print(f"- {account[0]}")
    else:
        print("No accounts found.")
