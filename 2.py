source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = {key: val for key, val in enumerate(source_list) if key > 0 and source_list[key] > source_list[key - 1]}

print(list(new_list.values()))
