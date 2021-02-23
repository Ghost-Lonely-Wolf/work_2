def division(first, second):
    try:
        res = first / second
        return res
    except ZeroDivisionError:
       return 'Делить на ноль нельзя'
print(division(int(input('Введите первое число ')), int(input('Введите второе число '))))