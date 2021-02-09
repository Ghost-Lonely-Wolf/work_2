first = list(input('Введите любое значение '))
n = 0
if len(first) % 2 == 0:
    while n < len(first):
        value = first[n]
        first[n] = first[n + 1]
        first[n + 1] = value
        n += 2
elif n < len(first) - 1:
    value = first[n]
    first[n] = first[n + 1]
    first[n + 1] = value
    n += 2
print(first)