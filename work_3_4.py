def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Введите числа с положительным x и целым y')
        return
    if x <= 0 or y >= 0:
        print('Введите числа с положительным x и отрицательным y')
        return
    return x ** y


print(my_func(input('Введите число с положительным x '), input('Введите число с отрицательным y ')))
