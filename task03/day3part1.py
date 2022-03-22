import sys

with open('day3input', 'r') as file:
    input_lines = [line.strip() for line in file]

gamma = ''
epsilon = ''

for column in range(0, len(input_lines[0])):
    one = 0
    zero = 0
    for row in range(0, len(input_lines)):
        if input_lines[row][column] == "1":
            one += 1
        else:
            zero += 1

    if one > zero:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"

#Реализовать или перевод из 2 в 10, или не использовать двоичную систему совсем
#Подумай, у тебя целая неделя
#В отдельной ветке

result = int(gamma, base=2) * int(epsilon, base=2)
print(result)

