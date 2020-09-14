print('Введите ваш рост в см')
height = int(input())
print('Введите ваш вес в кг')
weight = int(input())
bmi = weight / (height * 0.01) ** 2
print('Ваш ИМТ :', round(bmi))

a = int(bmi) - 16
b = 39 - int(bmi)
first = a * '='
second = b * '='

scale = '15' + first + '|' + str(round(bmi)) + '|' + second + '40'
print(scale)  # после этого решил попробовать if, elif, else

if bmi < 20:
    print('У вас недостаточная масса тела.')
elif bmi > 30:
    print('У вас избыточная масса тела.')
else:
    print('Вы в отличной форме, так держать!')
