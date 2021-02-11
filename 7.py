def fact(n):
    result = 1
    for counter in range(2, n+1):
        result *= counter
        yield result


for el in fact(int(input('Введите n - '))):
    print(el)
