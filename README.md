# Dictionary Attack
A **dictionary attack** [(Wikipedia)](https://it.wikipedia.org/wiki/Attacco_a_dizionario)
is a cybersecurity technique that involves attempting to guess login credentials of a system using a predefined list of common words or phrases. This method exploits the weakness of passwords based on common or easily guessable words. Attackers use automated programs to test thousands of combinations quickly, trying to gain unauthorized access to protected accounts or systems.
Now we would go and see a simulation of this via Python.
## Add User
##### Import 
We import the json library and renames it to js for convenience.
```python
import json as js
```

##### Function
This defines a function named *addUser* that takes two parameters: user, which represents the username of the new user, and passwd, which represents the password associated with that username. This function does not return any value (None). The function is documented using a docstring explaining its purpose and parameters.

```python
def addUser(user : str, passwd : str) -> None:
```

##### Work with JSON file 

Here, the code opens a JSON file named "users.json" located in the *"Data"* directory in read mode. It then uses the json.load() function to load the JSON data from the file into a Python dictionary named datas.

```python
    with open("Data/users.json","r") as file:
        datas = js.load(file)
```

This line adds a new key-value pair to the datas dictionary. The key is the user parameter (username), and the value is the passwd parameter (password), effectively adding a new user and associated password to the dictionary.

```python
    datas[user] = passwd
```

Finally, the code opens the same JSON file, "users.json", but this time in write mode. It then uses the json.dump() function to write the updated dictionary datas back to the JSON file, effectively saving the changes made by adding the new user and password. The file is automatically closed when the with block is exited.

```python
    with open("Data/users.json","w") as file:
        js.dump(datas,file)
```

##### Result

What we have wrote inside the JSON's file
```json
{
    "andrea": "c4400c702dfbd1766427e54268f9573ca90c2756b03e8946be852a927d5f3561"
}
```
To encrypt the password we used the Hash function: **SHA256**, but we will deepen it later.

## Encrypt
##### Import
This line imports the sha256 hashing algorithm from the hashlib library. This algorithm is used for cryptographic purposes, like hashing passwords.
Also the code imports the datetime module and renames it to dt for convenience. This module allows working with dates and times in Python.
```python
from hashlib import sha256
import datetime as dt 
```
##### Function 1
This line defines a function named encrypt that takes a string parameter passwd, representing the password to be encrypted. It specifies that the function will return a string (-> str).
```python
def encrypt(passwd : str) -> str:
```
##### Salt creation
This line calls the **genSalt()** function to generate a salt, which is a random value used in the encryption process to add complexity and make the encrypted passwords more secure.
```python
    salt = genSalt()
```

Here, the code reverses the generated salt. This manipulation adds an extra layer of complexity to the salt, making it harder for attackers to guess.
```python
    salt = salt[::-1]
```

This block of code opens a file named "SaltTest.salt" located in the "Data" directory in append mode ("a"). It then writes the generated salt to this file followed by a newline character. This file is typically used to store salts for later use or reference.
```python
    with open("Data/SaltTest.salt", "a") as f:
        f.write(salt + "\n")
```

This line hashes the password using the SHA-256 algorithm along with the generated salt. First, it encodes both the password and the salt into bytes using the .encode() method. Then, it concatenates them and computes their SHA-256 hash. Finally, it converts the hash to its hexadecimal representation using .hexdigest() before returning it.
```python
    return sha256(passwd.encode() + salt.encode()).hexdigest()
```

##### Function 2

This line defines a function named genSalt that does not take any parameters and returns a string (-> str).
```python
def genSalt() -> str:
```
Here, the function gets the current date and time using dt.datetime.now(), converts it to a string, and then strips any leading or trailing whitespace. It then removes spaces, colons, dashes, and periods from the string to create a unique salt based on the current date and time. Finally, it returns this salt.
```python
    return str(dt.datetime.now()).strip().replace(" ", "").replace(":", "").replace("-", "").replace(".", "")
```

# Attack
##### Import
Here, we're importing the sha256 hashing function from the hashlib module and the json module for working with JSON files.

```python
from hashlib import sha256
import json
```
##### Function
This line defines a function named attack that takes no arguments and returns a string. The -> str indicates that the function returns a string.

```python
def attack() -> str:
```
Here, we initialize three empty dictionaries. passDict will store the hashed passwords extracted from a JSON file, decryptedPassDict will store decrypted passwords along with the number of attempts, and finalStr will store the final output string.
```python
    passDict = {}
    decryptedPassDict = {}
    finalStr = "Decrypted passwords are: \n"
```

This block of code opens and reads user data from the users.json file located in the Data directory. It loads the JSON data into a Python dictionary (data) and then iterates over each key-value pair in the dictionary, storing the keys (user identifiers) and values (hashed passwords) in the passDict dictionary.
```python
    with open("Data/users.json", "r") as f:
        data = json.load(f)
        for i in data.keys():
            passDict[i] = data[i]
```
This block of code reads a dataset containing passwords to try from the DataSet.txt file and a salt from the Salt.txt file, both located in the Data directory. It iterates over each line in the dataset, removing any leading or trailing whitespace. Then, it iterates over each line in the Salt.txt file, again removing whitespace. For each combination of password and salt, it generates a hash using SHA-256 and compares it with the hashed passwords stored in passDict. If a match is found, it stores the decrypted password and the number of attempts in the decryptedPassDict dictionary.
```python
    attempts = 0
    with open("Data/DataSet.txt", "r") as f:
        dataSet = f.readlines()
        for line in dataSet:
            line = line.strip()
            with open("Data/Salt.txt", "r") as u:
                salts = u.readlines()
                for i in salts:
                    attempts += 1
                    i = i.strip()
                    for ident in passDict.keys():
                        if sha256(line.encode() + i.encode()).hexdigest() == passDict[ident]:
                            decryptedPassDict[ident] = [line]
                            decryptedPassDict[ident].append(attempts)
```
This loop iterates over each key-value pair in the decryptedPassDict dictionary, where the key is the user identifier and the value is a list containing the decrypted password and the number of attempts. It appends a formatted string to the finalStr variable for each user, indicating the decrypted password and the number of attempts. Finally, it returns the finalStr variable, which contains the final output string.
```python
    for name, tempPass in decryptedPassDict.items():
        finalStr += f"\t-{name}: {tempPass[0]} in {tempPass[1]} attempts\n"
    return finalStr
```


# Run the code
If you want to try this code, open a terminal inside the folder of the project
```bash
.\start.sh
```
or open the **main.py** file.