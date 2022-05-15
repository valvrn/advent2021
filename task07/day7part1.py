import os

with open('day7input', 'r') as file:
    input_lines = [line.strip() for line in file]

horizon_list = input_lines[0]
horizon_list = horizon_list.split(',')
horizon_list = list(map(int, horizon_list))
    
min_total_consumption = None

for i in range (0, len(horizon_list)):
    level = horizon_list[i]    
    current_total_consumption = 0
    for j in range (0, len(horizon_list)):
        submarine_level = horizon_list[j]
        consumption = abs(submarine_level - level)
        current_total_consumption = current_total_consumption + consumption
    if min_total_consumption == None:
        min_total_consumption = current_total_consumption
    if current_total_consumption < min_total_consumption:
        min_total_consumption = current_total_consumption

print(min_total_consumption)