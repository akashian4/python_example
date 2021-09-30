import functions as f
import os

while True:
    n = int(input(" for exit enter 0 and for play game enter 1 : "))
    os.system('cls||clear')

    if n == 0:
        break
    elif n == 1:
        f.playGame()
        continue
    else:
        print("input is invalid")
        continue
