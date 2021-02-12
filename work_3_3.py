def sum_max(x, y, z):
    my_func = [x, y, z]
    my_func.remove(min(my_func))
    return sum(my_func)
print(sum_max(int(input('Введите первое число ')), int(input('Введите второе число ')),
      int(input('Введите третье число '))))