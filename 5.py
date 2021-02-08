my_sum = 0
is_continue = True

while is_continue:
    item = input('Введите числа через пробел или символ q для выхода - ')
    for num in item.split():
        if not num.isdigit() and num.upper() == 'Q':
            print('end')
            is_continue = False
            break
        else:
            my_sum += int(num)
    print(my_sum)
