from sys import argv

try:
    print(f'ЗП = {(float(argv[1]) * float(argv[2])) + float(argv[3])}')
except ValueError:
    print('Неверный тип данных')
except IndexError:
    print('Указаны не все параметры')
