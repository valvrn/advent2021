import sys

class Submarine:
    def __init__(self, depth1, distance1):
        self.depth = depth1
        self.distance = distance1

    def print_result(self):
        print(self.depth * self.distance)

    def process(self, direction: str, value: int):
        if direction == "forward":
            self.distance = self.distance + value
        if direction == "up":
            self.depth = self.depth - value
        if direction == "down":
            self.depth = self.depth + value


with open('day2input', 'r') as file:
    input_lines = [line.strip() for line in file]

sub = Submarine(0, 0)

for line in input_lines:
    line_split = line.split(" ")
    key = line_split[0]
    value = int(line_split[1])
    sub.process(key, value)

sub.print_result()
