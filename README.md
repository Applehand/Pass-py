# Passpy
Passpy is a lightweight command-line interface (CLI) tool for securely storing, retrieving, updating, and managing passwords. It uses AES encryption to protect passwords, storing them in a SQLite database.

## Installation

Install Passpy using pip:

```bash
pip install git+https://github.com/Applehand/Pass-py.git
```

## Usage

### **Add a new account**:
If no password is given, one will be generated for you.


  ```bash
  passpy add <account> <password>
  ```

  Example:

  ```bash
  passpy add my_email@example.com thisismypassword1
  ```

### **Retrieve an account password**:

  ```bash
  passpy get <account>
  ```

  Example:

  ```bash
  passpy get my_email@example.com
  ```

### **Update an existing account password**:
If no password is given, one will be generated for you.
  ```bash
  passpy update <account> <password>
  ```

  Example:

  ```bash
  passpy update my_email@example.com thisismynewpassword2
  ```

### **Delete an account**:

  ```bash
  passpy delete <account>
  ```

  Example:

  ```bash
  passpy delete my_email@example.com
  ```

### **List all accounts**:

  ```bash
  passpy
  ```

  or

  ```bash
  passpy list
  ```
