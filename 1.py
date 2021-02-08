
def my_func(a, b):
    """Функция возвращает результат деления

    a - делимое
    b - делитель
    """
    if b == 0:
        return 'На ноль делить нельзя!'
    else:
        return a / b


a = float(input('Введите делимое - '))
b = float(input('Введите делитель - '))

print(my_func(a, b))
