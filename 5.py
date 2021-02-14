from random import randint

my_list = [randint(0, 1000) for _ in range(10, randint(20, 100))]
with open("file5.txt", 'w') as f_obj_w:
    f_obj_w.write(' '.join([str(el) for el in my_list]))
print(f'Сумма чисел: {sum(my_list)}')
