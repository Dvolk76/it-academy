a = int(input("Введите значение 1:"))
b = int(input("Введите значение 2:"))
c = int(input("Введите значение 3:"))
z = {a: '0', b: '0', c: '0'}
print("1. ", a and b and c and "Нет нулевых значений!!!")
print("2. ", a or b or c or "Введены все нули!!!")
if a > b + c:
    print("3. ", a - b - c)
else:
    print("3.\n4. ", b + c - a)
if a > 50 and (b > a or c > a):
    print("5. ", "Вася")
else:
    print("5. ")
if a > 5 or b == 7 and c == 7:
    print("6. ", "Петя")
else:
    print("6. ")
