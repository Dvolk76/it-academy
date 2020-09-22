
def auth_required(func):
    def inn(n):
        creds = {'aaa': '111', 'login': 'pass', 'admin': 'admin'}
        login = input('log\n- ')
        parol = input('pass\n- ')
        para = (login, parol)
        if para in creds.items():
            print('Пароль верный')
        else: print('Неверный пароль')
        func(n)
    return inn

def square(n):
    print(n**2)

square = auth_required(square)
square(int(input('Введите число которое желаете возвести в квадрат \n- ')))
