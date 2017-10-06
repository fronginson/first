class Dog:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


pluto = Dog('blue', 4)
bobik = Dog('red', 4)

print(pluto)

class fruits:
    def __init__(self, w, n=0):
        self.what = w
        self.numbers = n


f1 = fruits("apple", 150)
f2 = fruits("pineapple")

print(f1.what, f1.numbers)
print(f2.what, f2.numbers)

# параметры, аргументы которых должны быть обязательно указаны при создании объектов, указываются первыми,
# а параметры со значениями по умолчанию — после. def __init__(self,n=0,w): выдаст ERROR
