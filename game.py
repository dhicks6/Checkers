import random


def create_starting_board():
    rows, cols = (9, 9)
    # Setting up the board
    # 2d array for a checker board with a new line after each row
    board = [['0' for i in range(cols)] for j in range(rows)]
    R = "R"
    B = "B"

    board[0][0] = " "

    board[0][1] = "A"
    board[0][2] = "B"
    board[0][3] = "C"
    board[0][4] = "D"
    board[0][5] = "E"
    board[0][6] = "F"
    board[0][7] = "G"
    board[0][8] = "H"


    board[1][0] = "1"
    board[2][0] = "2"
    board[3][0] = "3"
    board[4][0] = "4"
    board[5][0] = "5"
    board[6][0] = "6"
    board[7][0] = "7"
    board[8][0] = "8"

    board[1][2] = R
    board[2][1] = R
    board[2][3] = R
    board[3][2] = R
    board[4][1] = R
    board[4][3] = R
    board[5][2] = R
    board[6][1] = R
    board[6][3] = R
    board[7][2] = R
    board[8][1] = R
    board[8][3] = R

    board[1][6] = B
    board[1][8] = B
    board[2][7] = B
    board[3][6] = B
    board[3][8] = B
    board[4][7] = B
    board[5][6] = B
    board[5][8] = B
    board[6][7] = B
    board[7][6] = B
    board[7][8] = B
    board[8][7] = B


    # Print the board with a new line after each row
    for row in board:
        print(' '.join(row))
    
    return board


# Set up arrays for the coordinates of the pieces for red and black



# Set up the logic for moving pieces around the board



# Set up the logic for taking pieces
    #