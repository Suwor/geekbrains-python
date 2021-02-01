# task 1
a = 55
b = 88.5
c = 'Hi!'

print(a, b, c)

a_label = 'целое число'
b_label = 'число с плавающей точкой'
c_label = 'строку'

input_label = 'Введите '
input_separator = ' - '
output_label = 'Вы ввели '
output_separator = ':'

a = int(input(input_label + a_label + input_separator))
b = float(input(input_label + b_label + input_separator))
c = input(input_label + c_label + input_separator)

print(output_label + a_label + output_separator, a)
print(output_label + b_label + output_separator, b)
print(output_label + c_label + output_separator, c)

# task 2
seconds = int(input('Введите время в секундах - '))

hours = seconds // (60 * 60)
seconds %= (60 * 60)
minutes = seconds // 60
seconds %= 60

print("%02d:%02d:%02d" % (hours, minutes, seconds))

# task 3
n = input('Введите число n - ')
nn = n * 2
nnn = n * 3
result = int(n) + int(nn) + int(nnn)

print(f"{n} + {nn} + {nnn} = {result}")

# task 4
n = int(input('Введите целое положительное число - '))
bigger_n = 0

while n > 0:
    remainder = n % 10
    if bigger_n < remainder:
        bigger_n = remainder
    n = n // 10

print('Самая большая цифра в числе:', bigger_n)

# task 5
proceeds = int(input('Введите значение выручки фирмы - '))
costs = int(input('Введите значение издержек фирмы - '))
profit = proceeds - costs

if profit > 0:
    print(f'Фирма отработала с прибылью. Рентабельность выручки составила {(profit / proceeds) * 100}%')
elif profit < 0:
    print('Фирма отработала с убытком')
else:
    print('Работа фирмы не принесла ни прибыли, ни убытков')

employees_count = int(input('Введите количество сотрудников фирмы - '))
print('Прибыль фирмы в расчете на одного сотрудника составила:', profit / employees_count)

# task 6
a = int(input('Введите результат, достигнутый спортсменом в первый день (км) - '))
b = int(input('Введите требуемый результат тренировок спортсмена - '))
counter = 1
print('Динамика результатов спортсмена по дням, если он будет улучшать результат на 10% в день:')

while True:
    print('%d-й день: %.2f' % (counter, a))
    if a >= b:
        break
    a *= 1.1
    counter += 1
print(f'Ответ: на {counter}-й день спортсмен достиг результата — не менее {b} км.')
