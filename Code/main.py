import AddUser as ad
import Encrypt as en
import Attack as at

if __name__ == "__main__":
    print("Hi! What you wanna do?\n\t\t1)Add new user\n\t\t2)Emulate an attack")
    selection = 0
    while selection != 1 or selection != 2:
        selection = int(input("Enter 1 or 2: "))

    if selection == 1:
        try:
            name = input("Enter a name: ")
            passwd = en.encrypt(input("Enter a password: "))
            ad.addUser(name,passwd)
            print("Added!")
        except:
            print("Error!")

    else:
        try:
            print("I start the attack...")
            print(at.attack())
        except:
            print("Error!")
