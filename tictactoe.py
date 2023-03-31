# tic tac toe game
import random
import sys


board = [['', '', ''], ['', '', ''], ['', '', '']]
empty_spot = "|   |"
line = "_______________"
x_spot = "| X |"
o_spot = "| O |"
spot_chosen = None
first_turn = True
game_complete = False


def prompt_func():
    greeting_message = 'Hello there, lets play a game of tic-tac-toe. Whats your name?'
    print(greeting_message)
    player_name = get_name()
    print("{} place an X on the board".format(player_name))
    display_board()
    spot_chosen = get_spot()
    set_spot(spot_chosen)
    computer_spot()
    display_board()
    global game_complete

    while not game_complete:
        winner = check_for_winner()
        if winner == 'player' or winner == 'computer':
            game_complete = True
            print("Game is over. {} won the game".format(winner))
            break

        spot = get_spot()
        set_spot(spot)
        computer_spot()
        display_board()


def get_name():
    player_name = input('Enter your name: ')
    return player_name


def get_spot():
    spot = input("Enter coordinates for board (ex. A1)")
    is_spot_valid_choice = False
    is_spot_valid_input = check_for_valid_input(spot)
    if is_spot_valid_input == True:
        is_spot_valid_choice = check_if_spot_placement_valid(spot)

    while is_spot_valid_choice != True or is_spot_valid_input != True:
        print("Choice is invalid, please input another set of coordinates for the board that is empty and in the form of letter and number for row and column choice.")
        spot = input("Enter coordinates for board (ex. A1)")
        is_spot_valid_input = check_for_valid_input(spot)

        if is_spot_valid_input == True:
            is_spot_valid_choice = check_if_spot_placement_valid(spot)

    return spot


def check_for_valid_input(input):
    valid_char = ['a', 'b', 'c']
    if len(input) > 2:
        return False
    elif input[0].lower() not in valid_char:
        return False
    elif int(input[1]) < 1 or int(input[1]) > 3:
        return False

    return True


def convert_spot_input_into_array_coordinates(spot):
    col = spot[0].lower()
    if col == 'a':
        col = 0
    elif col == 'b':
        col = 1
    else:
        col = 2
    row = int(spot[1])-1

    spot = [row, col]
    return spot


def check_if_spot_placement_valid(spot):
    spot = convert_spot_input_into_array_coordinates(spot)
    row = spot[0]
    col = spot[1]

    if board[row][col] == '':
        return True
    else:
        return False


def set_spot(spot):
    col = spot[0].lower()
    if col == 'a':
        col = 0
    elif col == 'b':
        col = 1
    else:
        col = 2
    row = int(spot[1])-1

    board[row][col] = 'x'
    display_board()

    first_turn = False


def display_board():
    row1 = ""
    row2 = ""
    row3 = ""
    for idrow, row in enumerate(board):
        for spot in row:
            if spot == '':
                if idrow == 0:
                    row1 += empty_spot
                elif idrow == 1:
                    row2 += empty_spot
                else:
                    row3 += empty_spot

            if spot == 'x':
                if idrow == 0:
                    row1 += x_spot
                elif idrow == 1:
                    row2 += x_spot
                else:
                    row3 += x_spot

            if spot == 'o':
                if idrow == 0:
                    row1 += o_spot
                elif idrow == 1:
                    row2 += o_spot
                else:
                    row3 += o_spot
    print("  A      B    C")
    print("1 " + row1)
    print("---------------")
    print("2 " + row2)
    print("---------------")
    print("3 " + row3)


def computer_spot():
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    computer_placed_spot = False

    while computer_placed_spot == False:
        if board[row][col] == '':
            board[row][col] = 'o'
            computer_placed_spot = True
            print(row, col)
            break

        else:
            row = random.randint(0, 2)
            col = random.randint(0, 2)


def check_for_winner():
    # row check
    winner = None
    for row in board:
        if row == ['x', 'x', 'x']:
            winner = 'player'
        if row == ['o', 'o', 'o']:
            winner = 'computer'

    # column check
    for col in range(3):
        if board[0][col] == 'x' and board[1][col] == 'x' and board[2][col] == 'x':
            winner = 'player'
            break
        if board[0][col] == 'o' and board[1][col] == 'o' and board[2][col] == 'o':
            winner = 'computer'
            break

    # cross board check
    if board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        winner = "player"
    if board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        winner = "computer"
    if board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
        winner = "player"
    if board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
        winner = "computer"

    return winner


prompt_func()

while game_complete == True:
    play_again = input("Do you want to play again? Y/N")
    if play_again.lower() == "y" or play_again.lower() == "yes":
        board = [['', '', ''], ['', '', ''], ['', '', '']]
        spot_chosen = None
        first_turn = True
        game_complete = False

        prompt_func()
    else:
        sys.exit()
