#!/bin/python3

import sys

with open('input', 'r') as file:
    input_lines = [line.strip() for line in file]

X = int(input_lines[0]) + int(input_lines[1]) + int(input_lines[2])

result = 0
for i in range(1, len(input_lines)-2):
    Y = int(input_lines[i]) + int(input_lines[i + 1]) + int(input_lines[i + 2])
    if X < Y:
        result += 1

    X = Y

print(result)
