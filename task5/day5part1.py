import os

with open('day5input', 'r') as file:
    input_lines = [line.strip() for line in file]


def parse_string(line):
    mod_line = [0, 1, 2, 3]
    return mod_line


def write_data(board, mod_string):
    pass


def count_result(board):
    return 5


board = []
size = 10
for i in range(0, size):
    subboard = []
    for j in range(0, size):
        subboard.append(0)
    board.append(subboard)

print(board)
for i in range(0, len(input_lines)):
    mod_string = parse_string(input_lines[i])
    write_data(board, mod_string)

print(count_result(board))
