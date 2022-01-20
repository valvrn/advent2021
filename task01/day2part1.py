import sys

with open('day2input', 'r') as file:
    input_lines = [line.strip() for line in file]
distance = 0
depth = 0


# Process next line

def process(direction, value):
    # Get key and value
    #print(direction, value)
    return 1, 10


for line in input_lines:
    line_split = line.split(" ")
    key = line_split[0]
    value = line_split[1]
    dX, dY = process(key, value)
    distance = distance + dX
    depth = depth + dY

print(distance * depth)
