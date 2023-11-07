import random

rows, cols = (8, 8)
pieces_per_player = 12
# 2d array for a checker board with a new line after each row
board = [['0' for i in range(cols)] for j in range(rows)]
R = "R"
B = "B"
board[0][1] = R
board[1][0] = R
board[1][2] = R
board[2][1] = R
board[3][0] = R
board[3][2] = R
board[4][1] = R
board[5][0] = R
board[5][2] = R
board[6][1] = R
board[7][0] = R
board[7][2] = R

board[0][5] = B
board[0][7] = B
board[1][6] = B
board[2][5] = B
board[2][7] = B
board[3][6] = B
board[4][5] = B
board[4][7] = B
board[5][6] = B
board[6][5] = B
board[6][7] = B
board[7][6] = B
# Print the board with a new line after each row
for row in board:
    print(' '.join(row))