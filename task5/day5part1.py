import os

with open('day5input', 'r') as file:
    input_lines = [line.strip() for line in file]


def parse_string(mod_line):
    mod_line = mod_line.split(" -> ")
    mod_line[0] = mod_line[0].split(",")
    mod_line[1] = mod_line[1].split(",")
    mod_line = [mod_line[0][0], mod_line[0][1], mod_line[1][0], mod_line[1][1]]
    return mod_line


def write_data(board, mod_string):
    if mod_string[0] == mod_string[2]:
        for i in range(min(mod_string[1], mod_string[3]), max(mod_string[1], mod_string[3])+1):
            board[i][mod_string[0]] = board[i][mod_string[0]] + 1
    else:
        for i in range(min(mod_string[0], mod_string[2]), max(mod_string[0], mod_string[2])+1):
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

write_data(board, [9, 8, 9, 2])
print(board)
# for i in range(0, len(input_lines)):
#     mod_string = parse_string(input_lines[i])
#     write_data(board, mod_string)
#
# print(parse_string(input_lines[2]))
