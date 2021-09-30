import random
import os


def checkInput(randomNumber, repeat):
    os.system('cls||clear')
    print("\n************* start game ****************\n")
    # print(f"javab ====>>>> {randomNumber}")
    for i in range(repeat):
        print(f"(( {repeat - i} fosat ))")
        inp = int(input("please enter number : "))
        isWin = False
        if inp == randomNumber:
            os.system('cls||clear')
            print("\neyvall dorost gofti. bordi  👍👍👍👍👍👍👍👍\n")
            isWin = True
            break
        elif inp > randomNumber:
            if i == repeat - 1:
                print("bakhti 😢😢😢😢😜😜😜😜")
            else:
                print("kochiktar bogo 👇👇👇👇")
        elif inp < randomNumber:
            if i == repeat - 1:
                print("bakhti 😢😢😢😢😜😜😜😜")
            else:
                print("bozorgtar bogo 👆👆👆👆")


while True:
    n = input(
        '''
choice level :

1. amateur level (number between 0 and 10 - 3 forsat) 
2. mid level (number between 0 and 100 - 10 forsat)
3. advance level (number between 0 and 1000 - 30 forsat)
4. custom level
5. exit

((in all level you can guess 5 number except 4))

--->> ''')
    if n == "1":
        r = random.randint(1, 10)
        checkInput(r, 3)
    elif n == "2":
        r = random.randint(1, 100)
        checkInput(r, 10)
    elif n == "3":
        r = random.randint(1, 1000)
        checkInput(r, 30)
    elif n == "4":
        i = int(input("enter max number (between 10 and 10000) : "))
        while i < 10 or i > 10000:
            print("invalid input 😒😒😒😒")
            i = int(input("enter max number (between 10 and 10000) : "))
        repeat = int(input("enter repeat number (between 3 nad 100) : "))
        while repeat < 3 or repeat > 100:
            print("invalid input 😒😒😒😒")
            repeat = int(input("enter repeat number (between 3 nad 100) : "))
        r = random.randint(1, i)
        checkInput(r, repeat)
    elif n == "5":
        break
    else:
        os.system('cls||clear')
        print("\ninvalid input 😒😒😒😒\n")
