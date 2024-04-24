# Importing the sha256 hashing function from the hashlib module
from hashlib import sha256
# Importing the json module for working with JSON files
import json

# Defining the attack function that returns a string
def attack() -> str:
    """
    This function attempts to decrypt hashed passwords using a dictionary attack.
    It reads user data from a JSON file, generates hashes for passwords combined with salts,
    and checks if they match with the stored hashed passwords.
    """

    # Dictionary to store hashed passwords extracted from the JSON file
    passDict = {}
    # Dictionary to store decrypted passwords along with the number of attempts
    decryptedPassDict = {}
    # String to store the final output
    finalStr = "Decrypted passwords are: \n"

    # Opening and reading user data from the users.json file
    with open("Data/users.json", "r") as f:
        data = json.load(f)
        # Iterating over each user and their hashed password
        for i in data.keys():
            passDict[i] = data[i]

    # Variable to keep track of the number of attempts
    attempts = 0
    # Opening and reading the dataset containing passwords to try
    with open("Data/DataSet.txt", "r") as f:
        dataSet = f.readlines()
        # Iterating over each password in the dataset
        for line in dataSet:
            line = line.strip()
            # Opening and reading the salt from the Salt.txt file
            with open("Data/Salt.txt", "r") as u:
                salts = u.readlines()
                # Iterating over each salt
                for i in salts:
                    attempts += 1
                    i = i.strip()
                    # Iterating over each user's hashed password
                    for ident in passDict.keys():
                        # Generating the hash for the password combined with the salt
                        if sha256(line.encode() + i.encode()).hexdigest() == passDict[ident]:
                            # Storing the decrypted password along with the number of attempts
                            decryptedPassDict[ident] = [line]
                            decryptedPassDict[ident].append(attempts)

    # Generating the final output string with decrypted passwords and number of attempts
    for name, tempPass in decryptedPassDict.items():
        finalStr += f"\t-{name}: {tempPass[0]} in {tempPass[1]} attempts\n"
    # Returning the final output string
    return finalStr
