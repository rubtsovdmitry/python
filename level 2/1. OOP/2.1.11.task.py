import abc, random


class IShape(abc.ABC):                                                              # создание абстрактного класса, методы в подклассах которого нужно обязательно описать
    '''Интерфейс для реализации геометрических фигур'''
     
    @abc.abstractmethod
    def get_perimeter(self):
        '''Возвращает периметр фигуры'''
        pass
 
    @abc.abstractmethod
    def get_area(self):
        '''Возвращает площадь фигуры'''
        pass

    @abc.abstractmethod
    def get_description(self):
        '''Возвращает произвольное описание фигуры'''
        pass


class Circle(IShape):                                                               # создание подкласса, в котором супер-классом является IShape
    PI = 3.14                                                                       # создание константы в атрибутах класса, не воспользовался библиотекой math для тренировки ООП

    def __init__(self, radius):                                                     # обязательное описание метода в подклассе                                           
        self._radius = radius

    def get_perimeter(self):                                                        # обязательное описание метода в подклассе
        return float(round(2 * self.__class__.PI * self._radius, 2))                # self.__class__.PI - такая запись обращается к классу (самому себе) динамически
    
    def get_area(self):                                                             # обязательное описание метода в подклассе
        return float(round(self.__class__.PI * self._radius ** 2, 2))
    
    def get_description(self):                                                      # обязательное описание метода в подклассе
        return f"Окружность с радиусом {self._radius}"


class Rectangul(IShape):                                                            # создание подкласса, в котором супер-классом является IShape
    def __init__(self, width, height):                                              # обязательное описание метода в подклассе                                           
        self._width = width
        self._height = height

    def get_perimeter(self):                                                        # обязательное описание метода в подклассе
        return float(round(2 * (self._width + self._height), 2))                    # self.__class__.PI - такая запись обращается к классу (самому себе) динамически
    
    def get_area(self):                                                             # обязательное описание метода в подклассе
        return float(round(self._width * self._height, 2))
    
    def get_description(self):                                                     # обязательное описание метода в подклассе
        return f"Прямоугольник с высотой {self._width} и шириной {self._height}"


class Square(Rectangul):                                                            # создание подкласса, в котором супер-классом является IShape
    def __init__(self, side):                                                       # обязательное описание метода в подклассе                                           
        super().__init__(side, side)                                                # поскольку у нас фигура квадрат, то мы передаём его сторону в качестве параметра старшему классу два раза

# два метода get_perimeter и get_area описывать не нужно, они будут наследоваться.
    
    def get_description(self):                                                     # обязательное описание метода в подклассе
        return f"Квадрат со стороной {self._width}"                                # состояние атрибута находится в старшем классе в переменной self._width


class Game:
    QUESTION_COUNT = 2
    def __init__(self):
        raise Exception("Нельзя создать экземпляр данного класса!")
    
    @staticmethod
    def __get_shape():                                                              # создан приватный метод, доступен только внутри класса
        x = random.randint(1, 3)
        if x == 1:
            return Circle(random.randint(1, 10))
        if x == 2:
            return Rectangul(random.randint(1, 10), random.randint(1, 10))
        if x == 3:
            return Square(random.randint(1, 10))

    @staticmethod                                                                   
    def __calculate(string, answer):                                                # создан приватный метод, доступен только внутри класса
        while True:
            try:
                guess = float(input(f"Укажите {string} этой фигуры: "))
                break
            except:
                print("Ошибка! Повторите ввод.")
        if guess == answer:
            print("Правильно!")
        else:
            print(f"Ошибка! Правильный ответ: {answer}.")

    @ classmethod
    def __run(cls):                                                                 # создан приватный метод, доступен только внутри класса
        shape = cls.__get_shape()                                                   # создаём объект рандомный из трёх классов Circle, Rectangul, Square
        print(shape.get_description())
        cls.__calculate("площадь", shape.get_area())
        cls.__calculate("периметр", shape.get_perimeter())

    @classmethod                                                                    
    def play(cls):                                                                  
        print()
        print(f"Привет! Мы фигуры и у нас есть {cls.QUESTION_COUNT} вопроса.")
        while True:
            is_game_over = input("Играем Y/N: ").upper()
            if is_game_over == "N":
                break
            cls.__run()
        print("Игра окончена.")
        print()

Game.play()