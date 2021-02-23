my_list = [77, 58, 89, 4, 7, 46, 33, 749, 400, 563]
new_list = [n for n in my_list if n > my_list[my_list.index(n)-1]]
print(new_list)