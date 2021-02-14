import json
from statistics import mean

average_profit_list = []
firm_dict = {}

with open("file7.txt") as f_obj_r, open("file7.json", 'w') as f_obj_w:
    for line in f_obj_r:
        row_list = line.split()
        profit = int(row_list[2]) - int(row_list[3])
        firm_dict[row_list[0]] = profit
        if profit > 0:
            average_profit_list.append(profit)
    json.dump([firm_dict, {'average_profit': mean(average_profit_list)}], f_obj_w)
