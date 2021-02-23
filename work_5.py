my_list = [9, 7, 5, 3, 1]
value = int(input('Введите одно число '))
n = my_list.count(value)
for factor in my_list:
    if n > 0:
        i = my_list.index(value)
        my_list.insert(i, value)
        break
    else:
        if factor < value:
            o = my_list.index(factor)
            my_list.insert(o, value)
            break
        elif value < my_list[len(my_list) - 1]:
            my_list.append(value)
print(my_list)
