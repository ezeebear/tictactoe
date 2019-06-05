from os import system, name
from time import sleep

board = ["__","__","__",
         "__","__","__",
         "__","__","__"]
pos = 0
player = " X "
game_on = True
winner = None



def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def game():
    print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    print("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")
    print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|")
    print(player,"turn")

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
    while board[pos] != "__":
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
        if board[0] == board[1] == board[2] != "__":
            print(board[0]+"wins")
            game()
            quit()
        elif board[3] == board[4] == board[5] != "__":
            print(board[3]+"wins")
            game()
            quit()
        elif board[6] == board[7] == board[8] != "__":
            print(board[6]+"wins")
            game()
            quit()
        elif board[0] == board[3] == board[6] != "__":
            print(board[0]+"wins")
            game()
            quit()
        elif board[1] == board[4] == board[7] != "__":
            print(board[1]+"wins")
            game()
            quit()
        elif board[2] == board[5] == board[8] != "__":
            print(board[2]+"wins")
            game()
            quit()
        elif board[0] == board[4] == board[8] != "__":
            print(board[0]+"wins")
            game()
            quit()
        elif board[2] == board[4] == board[6] != "__":
            print(board[2]+"wins")
            game()
            quit()

def tie():
    if board[0] != "__" and board[0] != "__" and board[1] != "__" and board[2] != "__" and board[3] != "__" and board[4] != "__" and board[5] != "__" and board[6] != "__" and board[7] != "__" and board[8] != "__":
        print("It's a tie..!")
        game()
        quit()




main_game()
