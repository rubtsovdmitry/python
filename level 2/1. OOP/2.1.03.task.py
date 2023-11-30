class Point:    

    def __init__(self, x=0, y=0):                                                   # гарантировано создадим атрибуты __x и __y для объекта         
        self.__x = x                                                                # состояние по-умолчанию для атрибута __x, если не указан другой - это 0
        self.__y = y                                                                # состояние по-умолчанию для атрибута __y, если не указан другой - это 0
      
    def __repr__(self):                                                             # создаёт печатную форму для объекта
        return f"Координаты x: {self.__x}, координаты y: {self.__y}"

    def get_x(self):                                                                # создаём geter и seter для x
        return self.__x
    def set_x(self, value):
        self.__x = value
    def move_x(self, value):
        self.__x += value
    x = property(get_x, set_x)
    x_move = property(get_x, move_x)

    def get_y(self):                                                                # создаём geter и seter для y
        return self.__y
    def set_y(self, value):
        self.__y = value
    def move_y(self, value):
        self.__y += value
    y = property(get_y, set_y)
    y_move = property(get_x, move_y)

################################################################################################################################################################

one = Point()                                                                       # создание объекта, не задавая координат, значений для x и y

print(one)

one.x = 1                                                                           # меняем координаты x
one.y = 2                                                                           # меняем координаты y
print(one)                                                                          # печатная форма для объекта

one.x_move = 1                                                                      # изменяем координаты x на дельту
one.y_move = -1                                                                     # изменяем координаты y на дельту
print(one)