import os

with open('day4input', 'r') as file:
    input_lines = [line.strip() for line in file]
    

class Board:
    def __init__(self, current_number, current_board_name, current_board_data):
        self.number = current_number
        self.name = current_board_name
        self.board = current_board_data

    def process(self, current_number, current_board_name, current_board_data):
        # if [sum(i) for i in zip(*input_boards)] or
        # while summ !=0:
        #     try:
        pass

    def result(self):
        pass

    def print(self):
        print(self[0])


number_selection = input_lines[0]
number_selection = number_selection.split(",")

# print(number_selection)
# print(type(number_selection))
# print(number_selection[2])

raw_data = input_lines[1:len(input_lines)]

boards = []
subgroup = []
boards_name = []
num = 1

for i in range(0, len(raw_data)):
    if raw_data[i] == '':
        continue
    # да, это сложное выражение, но тут мы делаем один список-ряд, из входящих сырых данных и убираем пустые
    # элементы, которые появились в результате разного количества пробелов
    subgroup.append(list(filter(None, raw_data[i].split(" "))))

    if len(subgroup) == 5:
        boards.append(subgroup)
        # еще один список с создаваемыми именами бордов
        boards_name.append("board" + str(num))
        num += 1
        subgroup = []

# print(boards)
# print(boards_name)
# Объединяем два списка в словарь
dict_boards = dict(zip(boards_name, boards))

# print(dict_boards["board1"])

for select in range(0, len(number_selection)):
    current_number_selection = number_selection[select]
    for i in range(0, len(boards_name)):
        current_board_name = boards_name[i]
        current_board_data = dict_boards[current_board_name]
        print(current_number_selection, current_board_name, current_board_data)
        Board(current_number_selection, current_board_name, current_board_data)
#
# for i in range(1, len(input_lines)):
#     Board(input_lines(i), number_selection)

