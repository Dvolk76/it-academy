print("Hello!")
d = dict()
while True:
        print("Добавить нового пользователя - 1")
        print("Посмотреть информацию о себе - 2")
        print("Посчитать ваш BMI - 3")
        print("Показать всех пользователей - 4")
        print("Выход - 0")
        function = input(" Ввод: ")
        if function == "0":
                break
        elif function == "1":
                name = str(input("Введите ваше имя\n:"))
                height = int(input("Введите ваш рост в см\n:"))
                weight = int(input("Введите ваш вес в кг\n:"))
                age = int(input("Введите ваш возраст (полных лет)\n:"))
                sex = input("Введите ваш пол m - Мужской\nw - Женский:")

                d[name] = {
                        "рост": height,
                        "вес": weight,
                        "возраст": age,
                        "пол": sex
                }
        elif function == "2":
                name = str(input("Введите ваше имя\n:"))
                print("Ваш рост - ", d[name]["рост"])
                print("Ваш вес - ", d[name]["вес"])
                print("Ваш возраст - ", d[name]["возраст"])
                print("Ваш пол - ", d[name]["пол"])
        elif function == "3":
                name = str(input("Введите ваше имя\n:"))
                bmi = d[name]["вес"] / (d[name]["рост"] * 0.01) ** 2
                print('Ваш ИМТ :', round(bmi))
                a = int(bmi) - 16
                b = 39 - int(bmi)
                first = a * '='
                second = b * '='

                scale = '15' + first + '|' + str(round(bmi)) + '|' + second + '40'
                print(scale)
                good = 'Вы в отличной форме, так держать!'
                slim = 'У вас недостаточная масса тела.'
                fat = 'У вас избыточная масса тела.'
                if bmi < 20 and d[name]["возраст"] <= 15:
                        print(good)
                elif bmi < 20 and d[name]["возраст"] > 15:
                        print(slim)
                elif 20 <= bmi <= 25 and d[name]["возраст"] > 15:
                        print(good)
                elif 20 <= bmi <= 25 and d[name]["возраст"] <= 15:
                        print(fat)
                elif 25 < bmi <= 30 and d[name]["возраст"] <= 35:
                        print(fat)
                elif 25 < bmi <= 30 and d[name]["возраст"] > 35:
                        print(good)
                elif bmi > 30:
                        print(fat)
                else:
                        print(good)
        elif function == "4":
                id = int(len(d))
                print("В системе зарегистрированы : ", d.keys())
