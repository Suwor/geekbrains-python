source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [val for val in source_list if source_list.count(val) < 2]

print(new_list)
