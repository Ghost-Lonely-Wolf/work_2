def print_id(**kwarg):
    return ' '.join(kwarg.values())

print(print_id(name=input('Введите своё имя '),
    surname=input('Введите свою фамилию '),
    date=input('Введите свой год рождения '),
    city=input('Введите свой город проживания '),
    email=input('Введите свой email '),
    number=input('Введите свой номер телефона ')))