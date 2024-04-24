# Importing the sha256 hashing algorithm from the hashlib library
from hashlib import sha256
# Importing the datetime module and renaming it to 'dt' for convenience
import datetime as dt 

def encrypt(passwd : str) -> str:
    """
    Function to encrypt a password using SHA-256 hashing algorithm with salt.

    Args:
        passwd (str): The password to be encrypted.

    Returns:
        str: The encrypted password.
    """
    # Generating a salt
    salt = genSalt()
    # Reversing the salt
    salt = salt[::-1]
    # Appending the salt to a file for future reference
    with open("Data/SaltTest.salt", "a") as f:
        f.write(salt + "\n")
    # Encrypting the password using SHA-256 hash function with salt
    return sha256(passwd.encode() + salt.encode()).hexdigest()


def genSalt() -> str:
    """
    Function to generate a salt based on the current date and time.

    Returns:
        str: The generated salt.
    """
    # Getting the current date and time and formatting it
    return str(dt.datetime.now()).strip().replace(" ", "").replace(":", "").replace("-", "").replace(".", "")
