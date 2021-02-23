with open('text.txt', 'r', encoding='utf-8') as n:
    line = n.readlines()
    for index, value in enumerate(line, 1):
        num = len(value.split())
        print(f'Строка - {index}, число слов - {num}')