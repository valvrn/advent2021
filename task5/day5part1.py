import os

with open('day5input', 'r') as file:
    input_lines = [line.strip() for line in file]


def parse_string(line):
    mod_line = [0, 1, 0, 3]
    return mod_line


def write_data(board, mod_string):
    if mod_string[0] == mod_string[2]:
        for i in range(mod_string[1], mod_string[3]+1):
            board[i][mod_string[0]] = board[i][mod_string[0]] + 1
    else:
        for i in range(mod_string[0], mod_string[2]+1):
            board[mod_string[1]][i] = board[mod_string[1]][i] + 1


def count_result(board):
    count = 0
    for i in range(0, size):
        for j in range(0, size):
            if board[i][j] >= 2:
                count += 1
    return count


board = []
size = 10
for i in range(0, size):
    subboard = []
    for j in range(0, size):
        subboard.append(0)
    board.append(subboard)


board[1][1] = 3
board[2][2] = 1
board[4][4] = 7
# for i in range(0, len(input_lines)):
#     mod_string = parse_string(input_lines[i])
#     write_data(board, mod_string)
#
print(count_result(board))
