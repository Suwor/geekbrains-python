def my_func(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(my_func(float(input('Введите основание степени - ')), int(input('Введите степень - '))))
