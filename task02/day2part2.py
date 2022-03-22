import sys

class Submarine:
    def __init__(self, depth, distance, aim):
        self.depth = depth
        self.distance = distance
        self.aim = aim

    def print_result(self):
        print(self.depth * self.distance)

    def process(self, direction: str, value: int):
        if direction == "forward":
            self.distance = self.distance + value
            self.depth = self.depth + self.aim * value
        if direction == "up":
            self.aim = self.aim - value
        if direction == "down":
            self.aim = self.aim + value


with open('day2input', 'r') as file:
    input_lines = [line.strip() for line in file]

sub = Submarine(0, 0, 0)

for line in input_lines:
    line_split = line.split(" ")
    key = line_split[0]
    value = int(line_split[1])
    sub.process(key, value)

sub.print_result()
