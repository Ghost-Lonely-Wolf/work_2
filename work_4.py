string = input('Введите любое преложение ')
factor = string.split(' ')
for n, k in enumerate(factor, 1):
    if len(k) > 10:
        k = k[0: 10]
    print(f'{n}. - {k}')