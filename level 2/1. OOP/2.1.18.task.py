"""ИГРА ХАНОЙСКАЯ БАШНЯ"""


import bext, sys


class Hanoi:
    AMOUNT_DISKS = 5                                                                                                                               # кол-во дисков на столбе
    TOWERS_list = ["A", "B", "C"]                                                                                                                  # столбы
    NAME = "ИГРА ХАНОЙСКАЯ БАШНЯ"                                                      
    go = set()                                                                                                                                     # возможные варианты ходов; словарь вида: {'CA', 'BC', 'CB', 'AB', 'AC', 'BA'}
    for a in TOWERS_list:
        for b in TOWERS_list:
            if a != b:
                go.add(a + b)
    
    """проверка ввода"""
    @classmethod
    def check_entering_class(cls):
        while True:                                                                                                                                # спрашивать в цикле перемещение, пока не будет введено правильно
            print()                                                                                                                                
            print('Введите буквы башен "откуда" и "куда" или "ВЫЙДИТЕ" из программы.')
            print('Пример №1: "AB" перемещает диск из башни A в башню B (набирать по-английски).')
            print('Пример №2: набрать <QUIT> для выхода из системы (набирать по-английски).')
            response = input('> ').upper().strip()                                                                                                 # переменная содержит строку, в которой указан маршрут перемещения 
    
            if response == 'QUIT':
                print()
                print('Игра окончена!!!')
                print()
                sys.exit()
    
            """проверка валидности ввода маршрута для перемещения"""
            if response not in __class__.go:
                print('Введите правильно и по-английски. Пример: AB, AC, BA, BC, CA, или CB.')
                width, height = bext.size()
                print(width * "_")                
                continue
            
            from_tower, to_tower = response[0], response[1]
            break
        return from_tower, to_tower                                                                                                                # возвращает два строковых значения для двух переменных, вида: "A, B или C"

    """конструктор объектов"""                                                                          
    def __init__(self) -> None:                                                                         
        self.__state_towers = self.__initiliaze()                                                                                                  # отсылка на инкапсулированный вспомогательный метод для конструктора; в переменной словарь {"A": [5, 4, 3, 2, 1], "B": [], "C": []}

    """метод addon для конструктора объектов"""         
    def __initiliaze(self):         
        three_towers = {}           
        for i in __class__.TOWERS_list:         
            three_towers[i] = []            
        three_towers[__class__.TOWERS_list[0]] = list(range(__class__.AMOUNT_DISKS, 0, -1))         
        return three_towers         

    """создадим getter для объектов класса"""            
    def get_three_towers(self):         
        return self.__state_towers          
    game = property(get_three_towers)           

    """визуализируем объект addon; пустой столб"""
    def __visualization_addon(self):
        print("|" + " " * __class__.AMOUNT_DISKS + "❚❚" + " " * __class__.AMOUNT_DISKS + "|", end="")                                               

    """визуализируем объект addon2; заполненный столб"""
    def __visualization_addon_2(self, a, b):             
        print("|" + ((__class__.AMOUNT_DISKS - b[a]) * " ") + b[a] * "■" + "❚❚"\
               + b[a] * "■" + ((__class__.AMOUNT_DISKS - b[a]) * " ") + "|", end="")

    """визуализируем объект"""          
    def visualization(self):            
        print(" " + f"{__class__.TOWERS_list[0]}" + ((" " * __class__.AMOUNT_DISKS + " ") * 2)\
              + " " + f"{__class__.TOWERS_list[1]}" + ((" " * __class__.AMOUNT_DISKS + " ") * 2)\
              + " " + f"{__class__.TOWERS_list[2]}" + ((" " * __class__.AMOUNT_DISKS + " ") * 2))

        for a in range((__class__.AMOUNT_DISKS - 1), -1, -1):                                                                                      # в цикле индексы для списка
            for b in self.__state_towers.values():                                                                                                 # в цикле знаяения словаря, которые индексы
                if (a + 1) > len(b):
                    self.__visualization_addon()
                else:
                    self.__visualization_addon_2(a, b)
            print()

    """проверка возможности перемещения дисков"""
    def check_entering_object(self, from_tower, to_tower):
        if len(self.__state_towers[from_tower]) == 0:
            print('Первая башня пустая. Сделайте другой ход.')
            width, height = bext.size()
            print(width * "_")
            return False
        elif len(self.__state_towers[to_tower]) == 0:            
            return True
        elif self.__state_towers[to_tower][-1] < self.__state_towers[from_tower][-1]:
            print('Такой ход невозможен. Нельзя переместить больший диск на меньший.')
            width, height = bext.size()
            print(width * "_")
            return False
        else:            
            return True

    """перемещение диска"""        
    def go_method(self, from_tower, to_tower):
        disk = self.__state_towers[from_tower].pop()
        self.__state_towers[to_tower].append(disk)

    """проверка окончания игры"""
    def check_end(self):
        finish = False
        for i in __class__.TOWERS_list[1:]:
            if len(self.__state_towers[i]) == __class__.AMOUNT_DISKS:     
                finish = True
        return finish
            

def main():
    my_object = Hanoi()
    """основной цикл игры"""
    try:
        while True:
            bext.clear()
            width, height = bext.size()
            bext.goto(0, int(height / 3))
            bext.fg("purple")
            print(Hanoi.NAME, "\n")
            my_object.visualization()
            while True:
                from_tower, to_tower = Hanoi.check_entering_class()                                                                                # здесь хранятся два строковых значения в двух переменных, вида: "A, B или C"
                check = my_object.check_entering_object(from_tower, to_tower)                                                                      # здесь хранится True или False (проверка возможности перемещения дисков)
                if check:
                    break
            my_object.go_method(from_tower, to_tower)                                                                                              # просто перемещает диски у объекта
            finish = my_object.check_end()                                                                                                         # здесь хранится True или False (проверка окончания игры)
            if finish:            
                width, height = bext.size()
                print(width * "_")
                my_object.visualization()
                print("Игра окончена!!!")
                break
    except KeyboardInterrupt:
        sys.exit()
    

if __name__ == "__main__":
    main()