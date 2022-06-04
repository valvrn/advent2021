import os

fish_start = [1,2,5,1,1,4,1,5,5,5,3,4,1,2,2,5,3,5,1,3,4,1,5,2,5,1,4,1,2,2,1,5,1,1,1,2,4,3,4,2,2,4,5,4,1,2,3,5,3,4,1,1,2,2,1,3,3,2,3,2,1,2,2,3,1,1,2,5,1,2,1,1,3,1,1,5,5,4,1,1,5,1,4,3,5,1,3,3,1,1,5,2,1,2,4,4,5,5,4,4,5,4,3,5,5,1,3,5,2,4,1,1,2,2,2,4,1,2,1,5,1,3,1,1,1,2,1,2,2,1,3,3,5,3,4,2,1,5,2,1,4,1,1,5,1,1,5,4,4,1,4,2,3,5,2,5,5,2,2,4,4,1,1,1,4,4,1,3,5,4,2,5,5,4,4,2,2,3,2,1,3,4,1,5,1,4,5,2,4,5,1,3,4,1,4,3,3,1,1,3,2,1,5,5,3,1,1,2,4,5,3,1,1,1,2,5,2,4,5,1,3,2,4,5,5,1,2,3,4,4,1,4,1,1,3,3,5,1,2,5,1,2,5,4,1,1,3,2,1,1,1,3,5,1,3,2,4,3,5,4,1,1,5,3,4,2,3,1,1,4,2,1,2,2,1,1,4,3,1,1,3,5,2,1,3,2,1,1,1,2,1,1,5,1,1,2,5,1,1,4]

max_day = 256

def fish_count(born, end_day):
    old_fish = 6
    new_fish = 8
    fish_list = [born]
    for i in range (1, end_day + 1):
        for j in range (0, len(fish_list)):
            fish_list[j] = fish_list[j] - 1
            if fish_list[j] == -1:
                fish_list[j] = old_fish
                fish_list.append(new_fish)
        print(f'Day {i} array {len(fish_list)}')
    return len(fish_list)

def fish_count_fix(born, max_day):
    fish_dict_template = {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
    fish_dict_current = fish_dict_template.copy()
    fish_dict_new = fish_dict_current.copy()

    fish_dict_current[born] = 1
    for i in range (1, max_day+1):
        for j in range (0, 9):
            if j >= 1:
                fish_dict_new[j - 1] = fish_dict_current[j] + fish_dict_new[j - 1]
            else:
                fish_dict_new[6] = fish_dict_current[0]
                fish_dict_new[8] = fish_dict_current[0]
                fish_dict_current[0] = 0
        fish_dict_current = fish_dict_new
        fish_dict_new = fish_dict_template.copy()
    return sum(fish_dict_current.values())


result = 0
for i in range (1, 6):
    result = result + (fish_start.count(i) * fish_count_fix(i, max_day))
print(result)


