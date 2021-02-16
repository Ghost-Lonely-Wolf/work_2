from random import randint
my_list = [randint(0, 15) for _ in range(20)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Изначальный список\n{my_list}\nНовый список\n {new_list}')
