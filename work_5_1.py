with open('text.txt', 'w', encoding='utf-8') as n:
    while True:
        line = input('Введите какой-нибудь текст ')
        if not line:
            break
        n.write(f'{line}\n')