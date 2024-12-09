import abc, random, pyinputplus


class Math_operation(abc.ABC):                                                      # создание абстрактного класса, методы в подклассах которого нужно обязательно описать
    '''Интерфейс для реализации математических операций.'''
     
    @abc.abstractmethod
    def action(self):
        '''Возвращает результат математической операции.'''
        pass

    @abc.abstractmethod
    def name_action(self):
        '''Возвращает описание математической операции.'''
        pass


class Plus(Math_operation):                                                         # создание подкласса, в котором супер-классом является Math_operation
    def __init__(self, a, b):                                                       # обязательное описание метода в подклассе                                           
        self._a = a
        self._b = b

    def action(self):                                                               # обязательное описание метода в подклассе
        return (self._a + self._b)
     
    def name_action(self):                                                          # обязательное описание метода в подклассе
        return f"Сумма {self._a} и {self._b}."


class Minus(Math_operation):                                                        # создание подкласса, в котором супер-классом является Math_operation (можно было сделать наследование от class Plus)
    def __init__(self, a, b):                                                       # обязательное описание метода в подклассе                                           
        self._a = a
        self._b = b

    def action(self):                                                               # обязательное описание метода в подклассе
        return (self._a - self._b)
     
    def name_action(self):                                                          # обязательное описание метода в подклассе
        return f"Разница {self._a} и {self._b}."
    

class Composition(Math_operation):                                                  # создание подкласса, в котором супер-классом является Math_operation (можно было сделать наследование от class Plus)
    def __init__(self, a, b):                                                       # обязательное описание метода в подклассе                                           
        self._a = a
        self._b = b

    def action(self):                                                               # обязательное описание метода в подклассе
        return (self._a * self._b)
     
    def name_action(self):                                                          # обязательное описание метода в подклассе
        return f"Произведение {self._a} и {self._b}."
    

class Test:
    count = 0
    max_count = 20
    mistakes = 0
    mistakes_list = []
    def __init__(self):
        raise Exception("Нельзя создать экземпляр данного класса!")
    
    @classmethod
    def __get_example(cls):                                                          # создан приватный метод, доступен только внутри класса
        x = random.randint(1, 3)
        if x == 1:
            return Plus(random.randint(1, 99), random.randint(1, 99))
        elif x == 2:
            while True:
                a = random.randint(1, 99)
                b = random.randint(1, 99)
                if a >= b:
                    break
            return Minus(a, b)       
        elif x == 3:
            return Composition(random.randint(1, 9), random.randint(1, 9))

    @classmethod
    def __run(cls):                                                                 # создан приватный метод, доступен только внутри класса
        example = cls.__get_example()                                               # создание объекта рандомного класса                                             
        print(example.name_action())                                                # вывод на печать действие/задачу класса, используя полиморфизм
        answer = pyinputplus.inputNum()                                             # модуль pyinputplus позволяет гарантированно получить ввод строки, которая может быть float или int с помощью функции inputNum
        if int(answer) != example.action():                                         # условие, которое ищет ошибки ответов теста
            cls.mistakes += 1
            cls.mistakes_list.append(example.name_action())
        cls.mistakes_list.sort()

    @classmethod                                                                    
    def play(cls):                                                                  
        print()
        print(f"Тест по математике для второго класса.")
        while cls.count != cls.max_count:
            cls.count += 1            
            print(f"№ {cls.count}")
            cls.__run()
        print()
        print(f"Ошибки в {cls.mistakes_list}.") 
        print(f"Количество ошибок равно {cls.mistakes}.")   
        print("Тест окончен.")
        print()


if __name__ == "__main__":    
    print("Скрипт запущен напрямую.")
    Test.play()
else:    
    print("Скрипт импортирован.")