
def auth_required(func):
    def inn(number):
        creds = {'aaa': '111', 'login': 'pass', 'admin': 'admin'}
        login = input('log\n- ')
        parol = input('pass\n- ')
        para = (login, parol)
        if para in creds.items():
            print('Пароль верный')
        else:
            print('Неверный пароль')
        func(number)
    return inn


@auth_required
def square(x):
    print(x**2)


# square = auth_required(square)
square(int(input('Введите число которое желаете возвести в квадрат \n- ')))
