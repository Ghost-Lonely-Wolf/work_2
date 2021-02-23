from sys import argv


def salary():
    try:
        time, rate, prize = map(float, argv[1:])
        print(f'Зарплата - {time * rate + prize}')
    except ValueError:
        print('You need to enter three values')


salary()