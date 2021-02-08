def my_func(a, b, c):
    my_list = sorted([a, b, c], reverse=True)
    return my_list[0] + my_list[1]


def int_input(name):
    return int(input(f'Введите {name} число - '))


print(my_func(int_input('первое'), int_input('второе'), int_input('третье')))
