def my_func():
    n = 0
    in_list = input('Введите числа через пробел или q для выхода: ').upper().split()
    for i in in_list:
        if i == 'Q':
            return n, True
        try:
            n += int(i)
        except ValueError:
            pass
    return n, False
res = 0
while True:
    x, y = my_func()
    res += x
    print(res)
    if y:
        break
