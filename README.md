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
