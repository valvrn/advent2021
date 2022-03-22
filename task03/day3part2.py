import sys
import os

with open('day3input', 'r') as file:
    input_lines = [line.strip() for line in file]

gamma = ''
epsilon = ''
o2 = input_lines
co2 = input_lines


def filter_array(array, position, value):
    if len(array) == 1:
        return array
    #print(value)
    custom_array = []
    for row in range(0, len(array)):
        if array[row][position] == value:
            custom_array.append(array[row])

    return custom_array


def find_common(array, position, iso2):
    one = 0
    zero = 0
    for row in range(0, len(array)):
        if array[row][position] == "1":
            one += 1
        else:
            zero += 1

    if one >= zero:
        return "1" if iso2 else "0"
    else:
        return "0" if iso2 else "1"


for column in range(0, len(input_lines[0])):
    current_return_value_o2 = find_common(o2, column, True)
    #print(current_return_value_o2)
    o2 = filter_array(o2, column, current_return_value_o2)

    current_return_value_co2 = find_common(co2, column, False)
    co2 = filter_array(co2, column, current_return_value_co2)

    print("o2 is ", o2)
    print("co2 is ", co2)

result = int(co2[0], base=2) * int(o2[0], base=2)
print(result)
