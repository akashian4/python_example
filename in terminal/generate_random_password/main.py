from library import generate_random_password

while True:
    length = int(input("please enter length of password : "))
    generate_random_password(length)
    i=input("do you want to continue (y or not) : ")
    if i=="y":
        continue
    else:
        break


