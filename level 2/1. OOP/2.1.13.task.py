import abc, random, pyinputplus


class Math_operation(abc.ABC):                                                      
    '''Интерфейс для реализации математических операций.'''
     
    @abc.abstractmethod
    def action(self):
        '''Возвращает результат математической операции.'''
        pass

    @abc.abstractmethod
    def name_action(self):
        '''Возвращает описание математической операции.'''
        pass


class Plus(Math_operation):                                                         
    def __init__(self, a, b):                                                                                                  
        self._a = a
        self._b = b

    def action(self):                                                               
        return (self._a + self._b)
     
    def name_action(self):                                                          
        return f"Сумма {self._a} и {self._b}."


class Minus(Math_operation):                                                        
    def __init__(self, a, b):                                                                                                  
        self._a = a
        self._b = b

    def action(self):                                                               
        return (self._a - self._b)
     
    def name_action(self):                                                          
        return f"Разница {self._a} и {self._b}."
    

class Composition(Math_operation):                                                  
    def __init__(self, a, b):                                                                                                  
        self._a = a
        self._b = b

    def action(self):                                                               
        return (self._a * self._b)
     
    def name_action(self):                                                          
        return f"Произведение {self._a} и {self._b}."
    

class Division(Math_operation):                                                     # добавлен класс для операции деления                                                  
    def __init__(self, a, b):                                                                                                  
        self._a = a
        self._b = b

    def action(self):                                                               
        return int(self._a / self._b)
     
    def name_action(self):                                                          
        return f"Деление {self._a} на {self._b}."


class Test:
    count = 0
    max_count = 20
    mistakes = 0
    mistakes_list = []
    mistakes_2 = 0                                                                  # добавлен атрибут класса
    mistakes_list_2 = []                                                            # добавлен атрибут класса
    temp = []                                                                       # добавлен атрибут класса
    def __init__(self):
        raise Exception("Нельзя создать экземпляр данного класса!")
    
    @classmethod
    def __get_example(cls):                                                          
        x = random.randint(1, 4)                                                    # строка изменена
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
        elif x == 4:                                                                # добавлен блок для условия
            while True:
                a = random.randint(1, 99)
                b = random.randint(1, 99)
                if a % b == 0:
                    break
            return Division(a, b)

    @classmethod
    def __run(cls):                                                                 
        example = cls.__get_example()                                                                                            
        print(example.name_action())                                                
        answer = pyinputplus.inputNum()                                             
        if int(answer) != example.action():                                         
            cls.mistakes += 1
            cls.mistakes_list.append(example.name_action())
        cls.mistakes_list.sort()

    @classmethod                                                                    # добавлен метод для класса
    def __run_2(cls, i):                                                                 
        if "Сумма" in i:
            example = Plus(int(i[1]), int(i[-1][0:-1]))                                                                                            
            print(example.name_action())                                                
            answer = pyinputplus.inputNum()                                             
            if int(answer) != example.action():                                         
                cls.mistakes_2 += 1
                cls.mistakes_list_2.append(example.name_action())
        elif "Разница" in i:
            example = Minus(int(i[1]), int(i[-1][0:-1]))                                                                                            
            print(example.name_action())                                                
            answer = pyinputplus.inputNum()                                             
            if int(answer) != example.action():                                         
                cls.mistakes_2 += 1
                cls.mistakes_list_2.append(example.name_action())
        elif "Произведение" in i:
            example = Composition(int(i[1]), int(i[-1][0:-1]))                                                                                            
            print(example.name_action())                                                
            answer = pyinputplus.inputNum()                                             
            if int(answer) != example.action():                                         
                cls.mistakes_2 += 1
                cls.mistakes_list_2.append(example.name_action())
        elif "Деление" in i:
            example = Division(int(i[1]), int(i[-1][0:-1]))                                                                                            
            print(example.name_action())                                                
            answer = pyinputplus.inputNum()                                             
            if int(answer) != example.action():                                         
                cls.mistakes_2 += 1
                cls.mistakes_list_2.append(example.name_action())
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
        if len(cls.mistakes_list) > 0:
            print(f"Ошибки в {cls.mistakes_list}.") 
        print(f"Количество ошибок равно {cls.mistakes}.")           
        if len(cls.mistakes_list) > 0:                                              # добавлен блок условия для ошибок
            print()                                                                     
            print("Давайте попробуем их исправить.")                                    
            for i in cls.mistakes_list:
                i = i.split(" ")                
                cls.temp.append(i)
            for i in cls.temp:
                cls.__run_2(i)
            print()
            if len(cls.mistakes_list_2) > 0:                                                                                 
                print(f"Не исправленные ошибки: {cls.mistakes_list_2}.")                
            print(f"Количество не исправленных ошибок равно {cls.mistakes_2}.")     
        print()                                                                 
        print("Тест окончен.")                                                          
        print()                                                                     


if __name__ == "__main__":    
    print("Скрипт запущен напрямую.")
    Test.play()
else:    
    print("Скрипт импортирован.")