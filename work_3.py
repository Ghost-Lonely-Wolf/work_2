season = int(input('Введите число от 1 до 12 '))
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
if season == 1 or season == 2 or season == 12:
    print(season_list[0])
elif season == 3 or season == 4 or season == 5:
    print(season_list[1])
elif season == 6 or season == 7 or season == 8:
    print(season_list[2])
elif season == 9 or season == 10 or season == 11:
    print(season_list[3])
else:
    print("Некорректное значение")
