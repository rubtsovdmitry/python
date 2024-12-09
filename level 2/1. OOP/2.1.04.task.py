class Calculator:    
    def __init__(self, x=0, y=0):                                                   # создание переменных
        self.__x = x                                                               
        self.__y = y
        self.__sign = "не определён"
        self.__result = "не определён"                                                                   

    def get_x(self):                                                                # geter и seter для первого числа x
        return self.__x
    def set_x(self, value):
        self.__x = value
    x = property(get_x, set_x)

    def get_y(self):                                                                # geter и seter для второго числа y
        return self.__y
    def set_y(self, value):
        self.__y = value
    y = property(get_y, set_y)

    def plus(self):                                                                 # вызов метода для сложения 
        self.__sign = "+"
        self.__result = (self.__x + self.__y)
        
    def minus(self):                                                                # вызов метода для сложения 
        self.__sign = "-"
        self.__result = (self.__x - self.__y)

    def multiplication(self):                                                       # вызов метода для умножения 
        self.__sign = "*"
        self.__result = (self.__x * self.__y)

    def division(self):                                                             # вызов метода для деления
        self.__sign = "/"
        self.__result = (self.__x / self.__y)

    def degree(self):                                                               # вызов метода для деления
        self.__sign = "^"
        self.__result = (self.__x ** self.__y)

    def __repr__(self):                                                             # печатная форма
        return f"{self.__x} {self.__sign} {self.__y} = {self.__result}"

################################# тест программы ####################################################################################3

first = Calculator()                                                                # создание объекта
first.x = 90                                                                        # задание первого числа через свойство
first.y = 10                                                                        # задание второго числа черех свойство

first.plus()
print(first)
print()
first.minus()
print(first)
print()
first.multiplication()
print(first)
print()
first.division()
print(first)
print()
first.degree()
print(first)
print()