import random

class Human:
    def __init__(self, name, sex):
        self.__name = name                                                              # имя человека
        self.__sex = sex.upper()                                                        # пол человека
        self.__status = None                                                            # статус человека (на ком женат или замужем)

    def __repr__(self):
        return f"Имя: {self.__name}. Пол: {self.__sex}. Статус: {self.__status}."
    
    def marry(self, human):                                                             # метод "поженить человека"
        if isinstance(human, Human):                                                    # проверим является ли переданный параметр (в нашем случае ann) класса Human            
            self.__status = human.__name                                                # для john меняем статус на ann
            human.__status = self.__name                                                # для ann (human) меняес статус на john (self)
        else:
            raise TypeError("Объект не человек.")
        
    def born_child(self, partner):                                                      # метод "родить ребёнка"
        if self.__status == partner.__name and self.__sex != partner.__sex:             # если статус равен имени параметра в переданном методе и пол разный, то ребёнок получится
            return Human("child", random.choice(["man", "women"]))
        else:
            raise Exception("Не могут иметь детей.")

################### проверка программы ##################################################################################################################################

# создаём два объекта разного пола       
john = Human("John", "man")                                                             
ann = Human("Ann", "women")

# женим их
john.marry(ann)

# рожаем 2х детей
child_1 = john.born_child(ann)
child_2 = john.born_child(ann)

# печатаем все объекты класса (двух родителей и их двух детей)
print(ann)
print(john)
print(child_1)
print(child_2)