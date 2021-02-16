from functools import reduce
def my_func(prev_n, n):
    return prev_n * n
my_list = [n for n in range(100, 1001) if n % 2 == 0]

print(f'Список \n{my_list}\nРезультат вычисления произведения всех чисел\n{reduce(my_func, my_list)}')