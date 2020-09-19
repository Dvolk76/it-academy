name = input("Введите ваше имя")
height = int(input("Введите ваш рост"))
weight = int(input("Введите ваш вес"))
age = input("Введите ваш возраст")
sex = input("Введите ваш пол")
name = dict(height ='Рост', weight ='Вес')
log = {}
log = {"Имя": name}



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



#
def getDict():
    r={}
    while (True):
        print('Enter key (empty enter - exit)')
        k=input()
        if k=='':
            break
        print('Enter value')
        v=input()
        r[k]=v
    return r

d=getDict()
print(d)