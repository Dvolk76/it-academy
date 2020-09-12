text = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!'


print('Исходный текст',  text)

text_sym = len(text)
print('\nЗадание 1  \nКоличество символов в предложении:', text_sym)


text_rev = text[::-1]
print('\nЗадание 2 \nЕсли прочитать текст наоборот:', text_rev)


text_ttl = text.title()
print('\nЗадание 3 \nКаждое слово начинается с большой буквы:', text_ttl)


text_UP = text.upper()
print(text_UP)
print('\nЗадание 4 \nВесь текст прописными буквами:', text_UP)


text_count_1 = text.count('нд')
text_count_2 = text.count('ам')
text_count_3 = text.count('о')
print('\nЗадание 5\n')
print('Число вхождений в строку "нд" :', text_count_1)
print('Число вхождений в строку "ам" :', text_count_2)
print('Число вхождений в строку "о" :', text_count_3)


text_sym2 = text_sym - text.count(' ')
text_sym3 = text.count(' ')
print('\nЗадание 6\n')


print('Количество символов в предложении без пробелов :', text_sym2)
print('Количество пробелов в предложении :', text_sym3)
