import os

with open('day4input', 'r') as file:
    input_lines = [line.strip() for line in file]


class Board:
    def __init__(self, board_data):
        self.board_data = board_data

    def process_board(self, current_number_selection):
        for line in self.board_data:
            for n, x in enumerate(line):
                if x == current_number_selection:
                    line[n] = -1

    def checking(self):
        for line in self.board_data:
            if sum(line) == -5:
                return True

        sum_rows = [sum(i) for i in zip(*self.board_data)]
        for n, x in enumerate(sum_rows):
            if x == -5:
                return True

        return False

    def result(self, current_number_selection):
        final_summ = 0
        for line in self.board_data:
            for n, x in enumerate(line):
                if x != -1:
                    final_summ = final_summ + x
        final_result = final_summ * current_number_selection
        print("result is ", final_result)


class Boards:
    def __init__(self, boards, number):
        self.number = number
        self.boards = boards

    def process(self):
        for select in range(0, len(self.number)):
            current_number_selection = self.number[select]
            for i in range(0, len(self.boards)):
                current_board = self.boards[i]
                current_board.process_board(current_number_selection)

                if current_board.checking() is True:
                    current_board.result(current_number_selection)
                    return


number_selection = input_lines[0]
number_selection = number_selection.split(",")
number_selection = [int(n) for n in number_selection]

raw_data = input_lines[1:len(input_lines)]
boards_list = []
subgroup = []

for i in range(0, len(raw_data)):
    if raw_data[i] == '':
        continue

    current_subgroup = filter(None, raw_data[i].split(" "))
    current_subgroup = [int(n) for n in current_subgroup]
    subgroup.append(list(current_subgroup))

    if len(subgroup) == 5:
        new_board = Board(subgroup)
        boards_list.append(new_board)
        subgroup = []

boards = Boards(boards_list, number_selection)
boards.process()
