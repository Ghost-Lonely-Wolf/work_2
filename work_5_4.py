
from googletrans import Translator
translator = Translator()
with open('number.txt', 'w', encoding='utf-8') as num_2:
    with open(r'C:\Users\Lonely_Wolf\OneDrive\Рабочий стол\work\number.txt', 'r', encoding='utf-8') as num:
        numeral = num.read()
    try:
        num_2.write(translator.translate(numeral, dest='ru').text)
    except AttributeError:
        print('Что-то пошло не так')