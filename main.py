# task 1
my_list = [2, 'text', 456, 45.3, None]

for el in my_list:
    print(type(el))

# task 2
my_list = []
while len(my_list) < 10:
    my_list.append(input('Введите элемент списка - '))

slice_1 = my_list[::2]
slice_2 = my_list[1::2]

my_list[1::2] = slice_1
my_list[::2] = slice_2

print(my_list)

# task 3.1
seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(seasons[int(input('Введите месяц - ')) - 1])

# task 3.2
seasons = {
    'зима': (1, 2, 12),
    'весна': (3, 4, 5),
    'лето': (6, 7, 8),
    'осень': (9, 10, 11),
}
month = int(input('Введите месяц - '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

# task 4
words = input('Введите несколько слов, разделённых пробелами - ')
word_list = words.split()
counter = 1

for word in word_list:
    print(f'{counter} : {word[:10]}')
    counter += 1

# task 5
my_list = [7, 5, 3, 3, 2, 0]
new_num = int(input('Введите новое число - '))
pos = 0

for num in my_list:
    if num <= new_num:
        my_list.insert(pos, new_num)
        break
    else:
        pos = pos+1

print(my_list)
