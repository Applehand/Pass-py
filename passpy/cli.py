import passpy.storage as storage
import passpy.crypto as crypto
import argparse
from dotenv import load_dotenv
load_dotenv()

parser = argparse.ArgumentParser(
    prog="Passpy",
    description="A simple and secure CLI tool for storing passwords."
    )
subparsers = parser.add_subparsers(dest="command")

# Add command
parser_add = subparsers.add_parser("add", help="Add a new account.")
parser_add.add_argument("account", help="The username, email, or domain to be associated with a password.")

# Get command
parser_get = subparsers.add_parser("get", help="Retrieve an account password.")
parser_get.add_argument("account", help="The username, email, or domain to retrieve the password for.")

# Update command
parser_update = subparsers.add_parser("update", help="Generate a new password for an existing account.")
parser_update.add_argument("account", help="The username, email, or domain to update the password for.")

# Delete command
parser_delete = subparsers.add_parser("delete", help="Delete an account.")
parser_delete.add_argument("account", help="The username, email, or domain to delete.")

# List command
parser_list = subparsers.add_parser("list", help="List all accounts.")

args = parser.parse_args()


def main():
    if not args.command:
        list_accounts()
    if args.command == "add":
        add_account(args.account)
    elif args.command == "get":
        get_account(args.account)
    elif args.command == "update":
        update_password(args.account)
    elif args.command == "delete":
        delete_account(args.account)
    elif args.command == "list":
        list_accounts()

def add_account(account):
    print(f"add {account}")

def get_account(account):
    print(f"get {account}")

def update_password(account):
    print(f"update {account}")

def delete_account(account):
    print(f"delete {account}")

def list_accounts():
    print("list accounts")
