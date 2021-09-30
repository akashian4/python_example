import random


def is_win(inputOfPlayer1, inputOfPlayer2):
    if inputOfPlayer1 == "rock" and inputOfPlayer2 == "paper":
        return False
    elif inputOfPlayer1 == "rock" and inputOfPlayer2 == "scissor":
        return True
    elif inputOfPlayer1 == "paper" and inputOfPlayer2 == "rock":
        return True
    elif inputOfPlayer1 == "paper" and inputOfPlayer2 == "scissor":
        return False
    elif inputOfPlayer1 == "scissor" and inputOfPlayer2 == "rock":
        return False
    elif inputOfPlayer1 == "scissor" and inputOfPlayer2 == "paper":
        return True


def get_input(player):
    while True:
        print("\nplease enter number of choice  : (1)rock   (2)paper   (3)scissor")
        inp = input(f" player {player} ==> ")
        if inp == "1":
            return "rock"
        elif inp == "2":
            return "paper"
        elif inp == "3":
            return "scissor"
        else:
            print("input is invalid")
            continue


def random_input():
    r = random.randint(1, 3)
    if r == 1:
        return "rock"
    elif r == 2:
        return "paper"
    elif r == 3:
        return "scissor"


def playGame():
    r = 1
    numberWinPlayer1 = 0
    numberWinPlayer2 = 0
    while numberWinPlayer1 != 3 and numberWinPlayer2 != 3:
        print(f'\n----------------- round {r} ------------------')
        inputOfPlayer1 = get_input(1)
        inputOfPlayer2 = random_input()
        if inputOfPlayer1 == inputOfPlayer2:
            print("\nis equal")
            r = r + 1
            continue
        else:
            if is_win(inputOfPlayer1, inputOfPlayer2):
                numberWinPlayer1 += 1
                winPlayer = "you"
            else:
                winPlayer = "computer"
                numberWinPlayer2 += 1
            print(f"\nplayer 1 : {inputOfPlayer1}   ,   player 2 : {inputOfPlayer2}\nwin in round -> {winPlayer} ")
            print(f"\n<<< player 1 : {numberWinPlayer1}   ,   player 2 : {numberWinPlayer2} >>>")
        r = r + 1
    if numberWinPlayer1 == 3:
        print("\n\nyou win\n")
    else:
        print("\n\nyou loss\n")
    print('************************* end ********************\n\n')
