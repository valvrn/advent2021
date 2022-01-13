#!/bin/python3

import sys

# 1. Загрузить из файла входные данные в массив
with open('input', 'r') as file:
    input_lines = [line.strip() for line in file]
#print(len(input_lines))
# 2. получить начальное значение, равное сумме первых трех чисел из массива, записать в переменную X
X = int(input_lines[0]) + int(input_lines[1]) + int(input_lines[2])
# print(X)

# 3. Пока в массиве не считаны все значения - делаем:
result = 0
i = 1
for line in input_lines[1:]:
    # 3.1 получить следующее значение, состоящее из суммы трех значений из массива,
    # смещенное на единицу, относительно предыдущей итерации. Записать в переменную Y
    # Y = int(line)
    # if int(input_lines[2 + 1]) is None: -
    # if int(input_lines[2 + 2]) is None: -
    # if int(input_lines[2 + 3]) is None: +
    # ...
    # if int(input_lines[2 + 995]) is None: -
    # if int(input_lines[2 + 996]) is None: -
    # if int(input_lines[2 + 997]) is None: -
    # if int(input_lines[2 + 998]) is None: +

    if 2 + i == len(input_lines):
        break
    Y = int(input_lines[0 + i]) + int(input_lines[1 + i]) + int(input_lines[2 + i])
    i += 1
    # print(Y, i)
    # 3.2 Сравнить две переменные
    # 3.2.1 Если первая переменная меньше второй:
    if X < Y:
        # 3.2.1.1 тогда увеличиваем счетчик на единицу
        result += 1
    # 3.3 перезаписываем X на Y
    X = Y

# 4. Вывести на экран значение счетчика
print(result)
