def my_func(**kwargs):
    print(' '.join(kwargs.values()))


my_func(
    name=input('Введите имя - '),
    surname=input('Введите фамилию - '),
    birth_year=input('Введите год рождения - '),
    residence_city=input('Введите город проживания - '),
    email=input('Введите email - '),
    phone=input('Введите телефон - ')
)
