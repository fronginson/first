def user():
    login = input('login: ')
    pswrd = input('password: ')
    return login, pswrd



def logon():
    x = input('enter your login here: ')
    y = input('enter your password here: ')
    return x, y


def compare():
    if logon() == user():
        print('welcome, ' + login.user)
    else:
        print('Wrong login or password')


compare()
