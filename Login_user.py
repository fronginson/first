class user:
    def __init__(self, login, password):
        self.l = login
        self.p = password



login = user(input('login: '), input('password: '))


def logon():
    x = input('enter your login here: ')
    y = input('enter your password here: ')
    return x, y


def compare():
    if logon() == (login.l, login.p):
        print('welcome, ' + login.l)
    else:
        print('Wrong login or password')
        compare()


compare()
