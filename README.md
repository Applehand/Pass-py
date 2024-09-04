# Passpy

Passpy is a simple and secure CLI tool for managing passwords. It allows you to add, retrieve, update, and delete passwords associated with your various accounts.

## Installation

Install Passpy using pip:

```bash
pip install git+https://github.com/Applehand/Pass-py.git
```

## Usage

Run `passpy` followed by one of the available commands. The `account` argument is required for most commands.

- **Add a new account**:

  ```bash
  passpy add <account>
  ```

  Example:

  ```bash
  passpy add my_email@example.com
  ```

- **Retrieve an account password**:

  ```bash
  passpy get <account>
  ```

  Example:

  ```bash
  passpy get my_email@example.com
  ```

- **Update an existing account password**:

  ```bash
  passpy update <account>
  ```

  Example:

  ```bash
  passpy update my_email@example.com
  ```

- **Delete an account**:

  ```bash
  passpy delete <account>
  ```

  Example:

  ```bash
  passpy delete my_email@example.com
  ```

- **List all accounts**:

  ```bash
  passpy
  ```

  or

  ```bash
  passpy list
  ```
