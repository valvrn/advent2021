#!/bin/python3

import sys

#1. Загрузить из файла входные данные в массив
with open('input', 'r') as file:
    input_lines = [line.strip() for line in file]
#2. получить начальное значение, записать в переменную X
X = int(input_lines[0])
#3. Пока в массиве не считаны все значения - делаем:
i = 0
for line in input_lines[1:]:
    #3.1 получить второе значение из массива, записать в переменную Y
    Y = int(line)
    #3.2 Сравнить две переменные
        #3.2.1 Если первая перменная меньше второй:
    if X < Y:
            #3.2.1.1 тогда увеличиваем счетчик на единицу
            i+=1
    #3.3 перезаписываем X на Y
    X = Y

#4. Вывести на экран значение счетчика
print(i)