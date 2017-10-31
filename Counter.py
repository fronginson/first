name = input('What is your name?')
print('Hello, ', name + '!')


class Counter:
    count = 0

    def __init__(self):
        self.__class__.count += 1


print(Counter.count)
c = Counter()
print(c.count)
d = Counter()
print(d.count)
