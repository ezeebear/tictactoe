from os import system, name

board = ["___","___","___",
         "___","___","___",
         "___","___","___"]

pos = 0
player = " X "
game_on = True
winner = None
count = ""

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def game():
    print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    print("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")
    print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|")

def main_game():
    while game_on is True:
        clear()
        game()
        answer()
        switch_player()
        result()


def answer():
    global pos
    pos = input("Enter the position :")
    while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Wrong input..")
        pos = input("Choose a position from 1-9: ")
    pos = int(pos) - 1
    while board[pos] != "___":
        print("Wrong input..")
        pos = int(input("You cannot overwrite the value: "))
        pos = pos - 1
    board[pos] = player
    return

def switch_player():
    global player

    if player ==" X ":
        player =" O "
    else:
        player =" X "
    return

def result():
    win()
    tie()

def win():
        # Row wins
        global board, board2
        if board[0] == board[1] == board[2] != "___":
            print(board[0]+"wins")
            game()
            count = input("Do you wanna play the game again?(y/n): ")
            if count == "y":
                board = ["___","___","___",
                         "___","___","___",
                         "___","___","___"]
            else:
                quit()
        elif board[3] == board[4] == board[5] != "___":
            print(board[3]+"wins")
            game()
            count = input("Do you wanna play the game again?(y/n): ")
            if count == "y":
                board = ["___","___","___",
                         "___","___","___",
                         "___","___","___"]
            else:
                quit()
        elif board[6] == board[7] == board[8] != "___":
            print(board[6]+"wins")
            game()
            count = input("Do you wanna play the game again?(y/n): ")
            if count == "y":
                board = board2
            else:
                quit()
        elif board[0] == board[3] == board[6] != "___":
            print(board[0]+"wins")
            game()
            count = input("Do you wanna play the game again?(y/n): ")
            if count == "y":
                board = ["___","___","___",
                         "___","___","___",
                         "___","___","___"]
            else:
                quit()
        elif board[1] == board[4] == board[7] != "___":
            print(board[1]+"wins")
            game()
            count = input("Do you wanna play the game again?(y/n): ")
            if count == "y":
                board = ["___","___","___",
                         "___","___","___",
                         "___","___","___"]
            else:
                quit()
        elif board[2] == board[5] == board[8] != "___":
            print(board[2]+"wins")
            game()
            count = input("Do you wanna play the game again?(y/n): ")
            if count == "y":
                board = ["___","___","___",
                         "___","___","___",
                         "___","___","___"]
            else:
                quit()
        elif board[0] == board[4] == board[8] != "___":
            print(board[0]+"wins")
            game()
            count = input("Do you wanna play the game again?(y/n): ")
            if count == "y":
                board = ["___","___","___",
                         "___","___","___",
                         "___","___","___"]
            else:
                quit()
        elif board[2] == board[4] == board[6] != "___":
            print(board[2]+"wins")
            game()
            count = input("Do you wanna play the game again?(y/n): ")
            if count == "y":
                board = ["___","___","___",
                         "___","___","___",
                         "___","___","___"]
            else:
                quit()

def tie():
    global board, board2
    if board[0] != "___" and board[0] != "___" and board[1] != "___" and board[2] != "___" and board[3] != "___" and board[4] != "___" and board[5] != "___" and board[6] != "___" and board[7] != "___" and board[8] != "___":
        print("It's a tie..!")
        game()
        count = input("Do you wanna play the game again?(y/n): ")
        if count == "y":
            board = ["___","___","___",
                     "___","___","___",
                     "___","___","___"]
        else:
            quit()




main_game()
