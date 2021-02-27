class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend, divisor = input("Введите делимое: "), input("Введите делитель: ")

try:
    dividend, divisor = int(dividend), int(divisor)
    if divisor == 0:
        raise MyZeroDivisionError("На ноль делить нельзя")
    result = dividend / divisor
except ValueError:
    print("Вы ввели не число")
except MyZeroDivisionError as err:
    print(err)
else:
    print(f"Все хорошо. Результат: {result}")
