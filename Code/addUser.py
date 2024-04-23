# Importing the json library to work with JSON data
import json as js

def addUser(user : str, passwd : str) -> None:
    """
    Function to add a new user to the JSON file containing user information.
    
    Args:
        user (str): The username of the new user.
        passwd (str): The password associated with the username.

    Returns:
        None
    """
    # Opening the JSON file containing user data in read mode
    with open("Data/users.json","r") as file:
        # Loading the JSON data into a Python dictionary
        datas = js.load(file)
    
    # Adding the new user and password to the dictionary
    datas[user] = passwd

    # Opening the JSON file again in write mode to update it
    with open("Data/users.json","w") as file:
        # Writing the updated dictionary back to the JSON file
        js.dump(datas,file)
