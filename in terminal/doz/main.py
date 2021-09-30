import os

gameList = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
nobat = 1


def setValue(nobat, value):
    if value == 1 and gameList[0][0] == 0:
        gameList[0][0] = nobat
        return True
    elif value == 2 and gameList[0][1] == 0:
        gameList[0][1] = nobat
        return True
    elif value == 3 and gameList[0][2] == 0:
        gameList[0][2] = nobat
        return True
    elif value == 4 and gameList[1][0] == 0:
        gameList[1][0] = nobat
        return True
    elif value == 5 and gameList[1][1] == 0:
        gameList[1][1] = nobat
        return True
    elif value == 6 and gameList[1][2] == 0:
        gameList[1][2] = nobat
        return True
    elif value == 7 and gameList[2][0] == 0:
        gameList[2][0] = nobat
        return True
    elif value == 8 and gameList[2][1] == 0:
        gameList[2][1] = nobat
        return True
    elif value == 9 and gameList[2][2] == 0:
        gameList[2][2] = nobat
        return True
    else:
        print("\nthis position is full\n")
        return False


def display():
    n = 1
    for i in range(3):
        s = ''
        for j in range(3):
            if gameList[i][j] == 0:
                s += f'  {n}  '
            elif gameList[i][j] == 1:
                s += f'  -  '
            elif gameList[i][j] == 2:
                s += f'  +  '
            n += 1
        print(s + "\n")
    print("\n-----------------------\n")


def isWin():
    if ((gameList[0][0] == gameList[0][1] == gameList[0][2] and gameList[0][0] != 0) or (
            gameList[1][0] == gameList[1][1] == gameList[1][2] and gameList[1][0] != 0) or (
            gameList[2][0] == gameList[2][1] == gameList[2][2] and gameList[2][0] != 0) or (
            gameList[0][0] == gameList[1][0] == gameList[2][0] and gameList[0][0] != 0) or (
            gameList[0][1] == gameList[1][1] == gameList[2][1] and gameList[0][1] != 0) or (
            gameList[0][2] == gameList[1][2] == gameList[2][2] and gameList[0][2] != 0) or (
            gameList[0][0] == gameList[1][1] == gameList[2][2] and gameList[0][0] != 0) or (
            gameList[0][2] == gameList[1][1] == gameList[2][0] and gameList[0][2] != 0)):
        return True
    else:
        return False


def checkFinishGame():
    if (0 not in gameList[0]) and (0 not in gameList[1]) and (0 not in gameList[2]):
        return True
    return False


def resetGame():
    global gameList
    gameList = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


while True:
    display()
    value = int(input(f"nobat player {nobat} : "))
    os.system('cls||clear')
    if value in range(1, 10):
        isSet = setValue(nobat, value)
        if not isSet:
            continue
        else:
            if isWin():
                print(
                    f"\n************************ player {nobat} is win *************************\n")
                i = input("do you want to play again : (y / another keyword)")
                if i == "y":
                    resetGame()
                    continue
                else:
                    break

    else:
        print("\ninvalid input\n")
        continue
    if checkFinishGame():
        i = input("do you want to play again : (y / another keyword)")
        if i == "y":
            resetGame()
            continue
        else:
            break

    if nobat == 1:
        nobat = 2
    else:
        nobat = 1
