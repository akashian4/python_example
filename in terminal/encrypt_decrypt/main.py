import encrypt as e

while True:
    x = input(
        "what do you want :\n1. encrypt\n2. decrept\n3. hard encrypy\n4. hard decrept\n5. exit\n==> ")
    if x == "1":
        z = input("enter your text (just a-z and 0-9) : ")
        if z != "" and e.isValidInput(z):
            print(e.encryptText(z))
        else:
            print("invalid input (just lowercase a-z and 0-9)")
            continue

    elif x == "2":
        z = input("enter your text (just a-z and 0-9) : ")
        if z != "" and e.isValidInput(z):
            print(e.decryptText(z))
        else:
            print("invalid input (just lowercase a-z and 0-9)")
            continue

    elif x == "3":
        z = input("enter your text (just a-z and 0-9) : ")
        if z != "" and e.isValidInput(z):
            print(e.hardEncrypt(z))
        else:
            print("invalid input (just lowercase a-z and 0-9)")
            continue
    elif x == "4":
        z = input("enter your text (just a-z and 0-9) : ")
        if z != "":
            z = e.extractValidText(z)
            print(e.decryptText(z))
        else:
            print("invalid input (just lowercase a-z and 0-9)")
            continue
    elif x == "5":
        break
    else:
        print("invalid input")
    print("\n************************\n")
