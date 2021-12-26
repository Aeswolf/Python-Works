"""
This is a file that provides a console representation of the tic tac toe game
"""

from random import randint
from itertools import permutations
# Global variables for deciding the winner of the game
global player_position_options
global cpu_position_options
global item_to_place


# setting the global variables to an empty list
player_position_options, cpu_position_options = [], []


# a method to print the grid board for the game
def print_board(board_matrix=None):
    number_of_rows_on_the_board = len(board_matrix)
    number_of_columns_on_the_board = len(board_matrix[0])
    for row in range(number_of_rows_on_the_board):
        print("\n-------------------")
        print("|", end='')
        for column_value in range(number_of_columns_on_the_board):
            print("  " + board_matrix[row][column_value], end="  |")
    print("\n-------------------")


# function to place a piece on the board
def place_a_piece(player, position, gameboard=None):
    if player == "Player":
        item_to_place: str = "X"
    elif player == "CPU":
        item_to_place: str = "O"
    if position == 1:
        gameboard[0][0] = item_to_place
    elif position == 2:
        gameboard[0][1] = item_to_place
    elif position == 3:
        gameboard[0][2] = item_to_place
    elif position == 4:
        gameboard[1][0] = item_to_place
    elif position == 5:
        gameboard[1][1] = item_to_place
    elif position == 6:
        gameboard[1][2] = item_to_place
    elif position == 7:
        gameboard[2][0] = item_to_place
    elif position == 8:
        gameboard[2][1] = item_to_place
    elif position == 9:
        gameboard[2][2] = item_to_place
    else:
        print("Invalid entry")


# function to determine the winner of the game
def determine_winner():
    perm_top_row = permutations([1, 2, 3])
    perm_middle_row = permutations([4, 5, 6])
    perm_bottom_row = permutations([7, 8, 9])
    perm_first_column = permutations([1, 4, 7])
    perm_second_column = permutations([2, 5, 8])
    perm_third_column = permutations([3, 6, 9])
    perm_leading_diagonal = permutations( [1, 5, 9])
    perm_following_diagonal = permutations([3, 5, 7])
    winning_options = []
    winning_options.extend(perm_following_diagonal)
    winning_options.extend(perm_leading_diagonal)
    winning_options.extend(perm_third_column)
    winning_options.extend(perm_second_column)
    winning_options.extend(perm_first_column)
    winning_options.extend(perm_bottom_row)
    winning_options.extend(perm_middle_row)
    winning_options.extend(perm_top_row)
    return winning_options


# the main method to execute the game
def main():
    # boolean variable to allow game to run
    run_game = True

    # Possible winning arrangements
    possible_winning_arrangements = determine_winner()

    # introductory message
    print("\t\t\t\t\tWelcome, Let\'s play some tic-tac-toe")

    # The empty game board for the game
    game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # printing the empty game board
    print_board(game_board)

    # while loop to make the game run while the winner has been declared or a tie has occured
    while run_game:
        # Message to show player's turn
        print("PLAYER'S TURN")

        #  alerting the player to place a piece
        player_position = int(input("Enter position to place the piece : "))

        # placing the keyed-in value on the board and storing the value in the options made by the player
        while player_position in player_position_options or player_position in cpu_position_options:
            #  alerting the player to place a piece
            player_position = int(input("Enter position to place the piece : "))
        player_position_options.append(player_position)
        print(player_position_options)
        place_a_piece("Player", player_position, game_board)

        # printing the board to display the piece played
        print_board(game_board)

        # checking if player wins the game
        if tuple(player_position_options) in possible_winning_arrangements:
            print("Player wins")
            break
        elif tuple(cpu_position_options) in possible_winning_arrangements:
            print("CPU wins")
        elif len(player_position_options) + len(cpu_position_options) == 9 and (
                tuple(player_position_options) not in possible_winning_arrangements or tuple(
                cpu_position_options) not in possible_winning_arrangements):
            print("It\'s a tie")
            break

        # Message to show player's turn
        print("CPU IS THINKING.......")
        # making a choice for the cpu using the random variable and playing the piece on the board and storing the value in the cpu_position_options
        cpu_position = randint(1, 9)
        while cpu_position in cpu_position_options or cpu_position in player_position_options:
            cpu_position = randint(1, 9)
            print(cpu_position)
        cpu_position_options.append(cpu_position)
        print(cpu_position_options)
        place_a_piece("CPU", cpu_position, game_board)
        # printing the board to display the piece played
        print_board(game_board)
        # checking if cpu wins the game
        if tuple(player_position_options) in possible_winning_arrangements:
            print("Player wins")
            break
        elif tuple(cpu_position_options) in possible_winning_arrangements:
            print("CPU wins")
            break
        elif len(player_position_options) + len(cpu_position_options) == 9 and (tuple(player_position_options) not in possible_winning_arrangements or tuple(cpu_position_options) not in possible_winning_arrangements):
            print("It\'s a tie")
            break


main()


