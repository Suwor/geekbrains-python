my_dict = {}

with open("file6.txt") as f_obj_r:
    for line in f_obj_r:
        row_list = line.split()
        my_dict[row_list[0][:-1]] = sum(
            [int(num) for num in [''.join([i for i in el if i.isdigit()]) for el in row_list[1:]] if num.isdigit()]
        )

print(my_dict)
