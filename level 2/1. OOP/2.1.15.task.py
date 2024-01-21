"""ИГРА МОРСКОЙ БОЙ"""


import random, bext, playsound


class Sea_battle:
    """БУКВЕННЫЕ И ЦИФРОВЫЕ КООРДИНАТЫ"""
    letters = "АБВГДЕЖЗИК"                                                                                          
    letters_go = "  АБВГДЕЖЗИК"
    numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    """КОРТЕЖ С КОРАБЛЯМИ"""
    ships = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
    """ЗНАЧКИ ДЛЯ МОРЯ"""
    sea_icon = "🟦"
    sea_icon_block = "🟪"
    ship_icon = "⚓"    
    hit_icon = "❌"
    miss_icon = "⚪"    
    
    """В КОНСТРУКТОРЕ СОЗДАДИМ АТРИБУТ ОБЪЕКТА - ЭТО ИГРОВОЕ ПОЛЕ, ОДНО ДЛЯ РАССТАНОВКИ КОРАБЛЕЙ, ДРУГОЕ ДЛЯ ХОДОВ"""
    def __init__(self) -> None:                                                                                     
        self._field = self.__initialize()       
        self._field_go = self.__initialize()
        
    """МЕТОД ДЛЯ ОПРЕДЕЛЕНИЯ ПЕРЕМЕННЫХ ДЛЯ КОНСТРУКТОРА __init__ (ИНКАПСУЛИРОВАННЫЙ)"""
    def __initialize(self):                                                                                         
        self.__field = {}
        n = 1
        for a in self.__class__.numbers:
            for b in self.__class__.letters:
                self.__field[str(a) + b] = [n, self.__class__.sea_icon]
                n += 1
        return self.__field

    """МЕТОД, КОТОРЫЙ ВОЗВРАЩАЕТ ИГРОВОЕ ПОЛЕ В ТЕКУЩЕМ СОСТОЯНИИ + ПОЛЕ С ХОДАМИ (ВИЗУАЛИЗАЦИЯ ИГРОВОЙ ОБЛАСТИ)"""
    def show_field(self):                                                                                           
        for i in (self.__class__.letters + self.__class__.letters_go):
            print((i + " "), end="")
        print()            
        for a in self._field.values():           
            if a[0] % 10 != 0 and a[0] < 10:
                print(a[1], end="")
            elif a[0] == 10:
                print(a[1], int(a[0] / 10), end="")
        print("  ", end="")
        for a in self._field_go.values():           
            if a[0] % 10 != 0 and a[0] < 10:
                print(a[1], end="")
            elif a[0] == 10:
                print(a[1], int(a[0] / 10))
        for a in self._field.values():           
            if a[0] % 10 != 0 and 10 < a[0] < 20:
                print(a[1], end="")
            elif a[0] == 20:
                print(a[1], int(a[0] / 10), end="")
        print("  ", end="")
        for a in self._field_go.values():           
            if a[0] % 10 != 0 and 10 < a[0] < 20:
                print(a[1], end="")
            elif a[0] == 20:
                print(a[1], int(a[0] / 10))
        for a in self._field.values():           
            if a[0] % 10 != 0 and 20 < a[0] < 30:
                print(a[1], end="")
            elif a[0] == 30:
                print(a[1], int(a[0] / 10), end="")
        print("  ", end="")
        for a in self._field_go.values():           
            if a[0] % 10 != 0 and 20 < a[0] < 30:
                print(a[1], end="")
            elif a[0] == 30:
                print(a[1], int(a[0] / 10))
        for a in self._field.values():           
            if a[0] % 10 != 0 and 30 < a[0] < 40:
                print(a[1], end="")
            elif a[0] == 40:
                print(a[1], int(a[0] / 10), end="")
        print("  ", end="")
        for a in self._field_go.values():           
            if a[0] % 10 != 0 and 30 < a[0] < 40:
                print(a[1], end="")
            elif a[0] == 40:
                print(a[1], int(a[0] / 10))
        for a in self._field.values():           
            if a[0] % 10 != 0 and 40 < a[0] < 50:
                print(a[1], end="")
            elif a[0] == 50:
                print(a[1], int(a[0] / 10), end="")
        print("  ", end="")
        for a in self._field_go.values():           
            if a[0] % 10 != 0 and 40 < a[0] < 50:
                print(a[1], end="")
            elif a[0] == 50:
                print(a[1], int(a[0] / 10))
        for a in self._field.values():           
            if a[0] % 10 != 0 and 50 < a[0] < 60:
                print(a[1], end="")
            elif a[0] == 60:
                print(a[1], int(a[0] / 10), end="")
        print("  ", end="")
        for a in self._field_go.values():           
            if a[0] % 10 != 0 and 50 < a[0] < 60:
                print(a[1], end="")
            elif a[0] == 60:
                print(a[1], int(a[0] / 10))
        for a in self._field.values():           
            if a[0] % 10 != 0 and 60 < a[0] < 70:
                print(a[1], end="")
            elif a[0] == 70:
                print(a[1], int(a[0] / 10), end="")
        print("  ", end="")
        for a in self._field_go.values():           
            if a[0] % 10 != 0 and 60 < a[0] < 70:
                print(a[1], end="")
            elif a[0] == 70:
                print(a[1], int(a[0] / 10))
        for a in self._field.values():           
            if a[0] % 10 != 0 and 70 < a[0] < 80:
                print(a[1], end="")
            elif a[0] == 80:
                print(a[1], int(a[0] / 10), end="")
        print("  ", end="")
        for a in self._field_go.values():           
            if a[0] % 10 != 0 and 70 < a[0] < 80:
                print(a[1], end="")
            elif a[0] == 80:
                print(a[1], int(a[0] / 10))
        for a in self._field.values():           
            if a[0] % 10 != 0 and 80 < a[0] < 90:
                print(a[1], end="")
            elif a[0] == 90:
                print(a[1], int(a[0] / 10), end="")
        print("  ", end="")
        for a in self._field_go.values():           
            if a[0] % 10 != 0 and 80 < a[0] < 90:
                print(a[1], end="")
            elif a[0] == 90:
                print(a[1], int(a[0] / 10))
        for a in self._field.values():           
            if a[0] % 10 != 0 and 90 < a[0] < 100:
                print(a[1], end="")
            elif a[0] == 100:
                print(a[1], int(a[0] / 10), end="")
        print(" ", end="")
        for a in self._field_go.values():           
            if a[0] % 10 != 0 and 90 < a[0] < 100:
                print(a[1], end="")
            elif a[0] == 100:
                print(a[1], int(a[0] / 10))
            
    """МЕТОД, КОТОРЫЙ ПРОВОДИТ ДОПОЛНИТЕЛЬНУЮ ПРОВЕРКУ ПРИ УСТАНОВКЕ ТРЁХ-ПАЛУБНЫХ КОРАБЛЕЙ (ИНКАПСУЛИРОВАННЫЙ)"""
    def __arrange_ships_three(self, x, move):
        if move == "right":                                                                                                      # проверяет, есть ли три подходящих клетки для коробля по-горизонтали            
            return True if [(x), self.__class__.sea_icon] in self._field.values() and \
                [(x + 1), self.__class__.sea_icon] in self._field.values() and \
                [(x + 2), self.__class__.sea_icon] in self._field.values() else False                                                                   
        elif move == "down":                                                                                                     # проверяет, есть ли три подходящих клетки для коробля по-вертикали
            return True if [(x), self.__class__.sea_icon] in self._field.values() and \
                [(x + 10), self.__class__.sea_icon] in self._field.values() and \
                [(x + 20), self.__class__.sea_icon] in self._field.values() else False                                                       
                    
    """МЕТОД, КОТОРЫЙ ПРОВОДИТ ДОПОЛНИТЕЛЬНУЮ ПРОВЕРКУ ПРИ УСТАНОВКЕ ДВУХ-ПАЛУБНЫХ КОРАБЛЕЙ (ИНКАПСУЛИРОВАННЫЙ)"""
    def __arrange_ships_two(self, x, move):
        if move == "right":                                                                                                      # проверяет, есть ли две подходящие клетки для коробля по-горизонтали
            return True if [(x), self.__class__.sea_icon] in self._field.values() and \
                [(x + 1), self.__class__.sea_icon] in self._field.values() else False                                                                        
        elif move == "down":                                                                                                     # проверяет, есть ли две подходящие клетки для коробля по-вертикали
            return True if [(x), self.__class__.sea_icon] in self._field.values() and \
                [(x + 10), self.__class__.sea_icon] in self._field.values() else False                                                       
        
    """МЕТОД, КОТОРЫЙ ПРОВОДИТ ДОПОЛНИТЕЛЬНУЮ ПРОВЕРКУ ПРИ УСТАНОВКЕ ОДНО-ПАЛУБНЫХ КОРАБЛЕЙ (ИНКАПСУЛИРОВАННЫЙ)"""
    def __arrange_ships_one(self, x):                                                                                                              
            return True if [(x), self.__class__.sea_icon] in self._field.values() else False                                     # проверяет, есть ли две подходящие клетки для коробля по-горизонтали                                                                                                         
            
    """МЕТОД, КОТОРЫЙ РАССТАВЛЯЕТ КОРАБЛИ НА ИГРОВОМ ПОЛЕ"""
    def arrange_ships(self):
        for i in self.__class__.ships:                                                                                           # обходим в цикле кортеж с кораблями
            if i == 4:                                                                                                           # условие для четырех-палубного
                while True:                                                                                                      # цикл повторяется пока не будут найдены подходящие координаты для установки корабля                
                    x = random.randint(1, 100)                                                                                   # рандомные координаты, которые генерируются в цикле пока не будет найдена подходящая точка
                    move = random.choice(["right", "down"])                                                                      # направление расстановки корабля из точка (направо или вниз)
                    if move == "right" and 0 < int(str(x)[-1]) <= 7:                                                             # первое условие, при котором корабль может быть установлен горизонтально
                        for a, b in self._field.items():                                                                         # в цикле модернизируем игровое поле, клетки с кораблями и морем вокруг кораблей меняют свои значения
                            if b[0] == x:                                                        
                                self._field[a] = [x, self.__class__.ship_icon]                                       
                            if b[0] == x + 1:   
                                self._field[a] = [x + 1, self.__class__.ship_icon]                                
                            if b[0] == x + 2:   
                                self._field[a] = [x + 2, self.__class__.ship_icon]                                
                            if b[0] == x + 3:   
                                self._field[a] = [x + 3, self.__class__.ship_icon]                                       
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 10) or \
                                b[0] == (x - 9) or b[0] == (x - 8) or b[0] == (x - 7) or \
                                b[0] == (x + 13) or b[0] == (x + 12) or \
                                b[0] == (x + 11) or b[0] == (x + 10) else self._field[a]                                         # условие для верха и низа от корабля (помечаем морские клетки, рядом с кораблём)
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 6) \
                                and str(b[0])[-1] != "1" or b[0] == (x + 4) and str(b[0])[-1] != "1" \
                                or b[0] == (x + 14) and str(b[0])[-1] != "1" else self._field[a]                                 # условие для правой стороны от корабля (помечаем морские клетки, рядом с кораблём)
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x + 9) \
                                and str(b[0])[-1] != "0" or b[0] == (x - 1) and str(b[0])[-1] != "0" \
                                or b[0] == (x - 11) and str(b[0])[-1] != "0" else self._field[a]                                 # условие для левой стороны от корабля (помечаем морские клетки, рядом с кораблём)
                        break
                    elif move == "down" and x <= 70:                                                                             # второе условие, при котором корабль может быть установлен вертикально
                        for a, b in self._field.items():                                                                         # в цикле модернизируем игровое поле, клетки с кораблями и морем вокруг кораблей меняют свои значения
                            if b[0] == x:                                                        
                                self._field[a] = [x, self.__class__.ship_icon]                                 
                            if b[0] == x + 10:   
                                self._field[a] = [x + 10, self.__class__.ship_icon]                                
                            if b[0] == x + 20:   
                                self._field[a] = [x + 20, self.__class__.ship_icon]                                
                            if b[0] == x + 30:   
                                self._field[a] = [x + 30, self.__class__.ship_icon]                                                            
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 10) or \
                                b[0] == (x + 40) else self._field[a]                                                             # условие для верха и низа от корабля (помечаем морские клетки, рядом с кораблём)
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 9) \
                                and str(b[0])[-1] != "1" or b[0] == (x + 1) and str(b[0])[-1] != "1" or \
                                b[0] == (x + 11) and str(b[0])[-1] != "1" or \
                                b[0] == (x + 21) and str(b[0])[-1] != "1" or \
                                b[0] == (x + 31) and str(b[0])[-1] != "1" or \
                                b[0] == (x + 41) and str(b[0])[-1] != "1" else self._field[a]                                    # условие для правой стороны от корабля (помечаем морские клетки, рядом с кораблём)
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x + 39) \
                                and str(b[0])[-1] != "0" or b[0] == (x + 29) and str(b[0])[-1] != "0" or \
                                b[0] == (x + 19) and str(b[0])[-1] != "0" or \
                                b[0] == (x + 9) and str(b[0])[-1] != "0" or \
                                b[0] == (x - 1) and str(b[0])[-1] != "0" or \
                                b[0] == (x - 11) and str(b[0])[-1] != "0" else self._field[a]                                    # условие для левой стороны от корабля (помечаем морские клетки, рядом с кораблём)
                        break
            if i == 3:                                                                                                           # условие для трёх-палубного
                while True:                                                                                                      # цикл повторяется пока не будут найдены подходящие координаты для установки корабля                
                    x = random.randint(1, 100)                                                                                   # рандомные координаты, которые генерируются в цикле пока не будет найдена подходящая точка                    
                    move = random.choice(["right", "down"])                                                                      # направление расстановки корабля из точка (направо или вниз)                    
                    if move == "right" and 0 < int(str(x)[-1]) <= 8 and self.__arrange_ships_three(x, move):                     # первое условие, при котором корабль может быть установлен (горизонтально)
                        for a, b in self._field.items():                                                                         # в цикле модернизируем игровое поле, клетки с кораблями и морем вокруг кораблей меняют свои значения
                            if b[0] == x:                                                        
                                self._field[a] = [x, self.__class__.ship_icon]                                 
                            if b[0] == x + 1:   
                                self._field[a] = [x + 1, self.__class__.ship_icon]                                
                            if b[0] == x + 2:   
                                self._field[a] = [x + 2, self.__class__.ship_icon]  
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 10) or \
                                b[0] == (x - 9) or b[0] == (x - 8) or \
                                b[0] == (x + 12) or \
                                b[0] == (x + 11) or b[0] == (x + 10) else self._field[a]                                         # условие для верха и низа от корабля (помечаем морские клетки, рядом с кораблём)       
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 7) \
                                and str(b[0])[-1] != "1" or b[0] == (x + 3) and str(b[0])[-1] != "1" \
                                or b[0] == (x + 13) and str(b[0])[-1] != "1" else self._field[a]                                 # условие для правой стороны от корабля (помечаем морские клетки, рядом с кораблём)         
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x + 9) \
                                and str(b[0])[-1] != "0" or b[0] == (x - 1) and str(b[0])[-1] != "0" \
                                or b[0] == (x - 11) and str(b[0])[-1] != "0" else self._field[a]                                 # условие для левой стороны от корабля (помечаем морские клетки, рядом с кораблём)
                        break
                    elif move == "down" and x <= 80 and self.__arrange_ships_three(x, move):                                     # второе условие, при котором корабль может быть установлен (вертикально)
                        for a, b in self._field.items():                                                                         # в цикле модернизируем игровое поле, клетки с кораблями и морем вокруг кораблей меняют свои значения
                            if b[0] == x:                                                        
                                self._field[a] = [x, self.__class__.ship_icon]                                 
                            if b[0] == x + 10:                       
                                self._field[a] = [x + 10, self.__class__.ship_icon]
                            if b[0] == x + 20:                       
                                self._field[a] = [x + 20, self.__class__.ship_icon]
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 10) or \
                                b[0] == (x + 30) else self._field[a]                                                             # условие для верха и низа от корабля (помечаем морские клетки, рядом с кораблём)
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 9) \
                                and str(b[0])[-1] != "1" or b[0] == (x + 1) and str(b[0])[-1] != "1" or \
                                b[0] == (x + 11) and str(b[0])[-1] != "1" or \
                                b[0] == (x + 21) and str(b[0])[-1] != "1" or \
                                b[0] == (x + 31) and str(b[0])[-1] != "1" else self._field[a]                                    # условие для правой стороны от корабля (помечаем морские клетки, рядом с кораблём)
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x + 29) \
                                and str(b[0])[-1] != "0" or b[0] == (x + 19) and str(b[0])[-1] != "0" or \
                                b[0] == (x + 9) and str(b[0])[-1] != "0" or \
                                b[0] == (x - 1) and str(b[0])[-1] != "0" or \
                                b[0] == (x - 11) and str(b[0])[-1] != "0" else self._field[a]                                    # условие для левой стороны от корабля (помечаем морские клетки, рядом с кораблём)
                        break                            
            if i == 2:                                                                                                           # условие для двух-палубного
                while True:                                                                                                      # цикл повторяется пока не будут найдены подходящие координаты для установки корабля                
                    x = random.randint(1, 100)                                                                                   # рандомные координаты, которые генерируются в цикле пока не будет найдена подходящая точка
                    move = random.choice(["right", "down"])                                                                      # направление расстановки корабля из точка (направо или вниз)                    
                    if move == "right" and 0 < int(str(x)[-1]) <= 9 and self.__arrange_ships_two(x, move):                       # первое условие, при котором корабль может быть установлен (горизонтально)
                        for a, b in self._field.items():                                                                         # в цикле модернизируем игровое поле, клетки с кораблями и морем вокруг кораблей меняют свои значения
                            if b[0] == x:                                                        
                                self._field[a] = [x, self.__class__.ship_icon]                                 
                            if b[0] == x + 1:   
                                self._field[a] = [x + 1, self.__class__.ship_icon]                                                              
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 10) or \
                                b[0] == (x - 9) or \
                                b[0] == (x + 11) or \
                                b[0] == (x + 10) else self._field[a]                                                             # условие для верха и низа от корабля (помечаем морские клетки, рядом с кораблём)       
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 8) \
                                and str(b[0])[-1] != "1" or b[0] == (x + 2) and str(b[0])[-1] != "1" \
                                or b[0] == (x + 12) and str(b[0])[-1] != "1" else self._field[a]                                 # условие для правой стороны от корабля (помечаем морские клетки, рядом с кораблём)         
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x + 9) \
                                and str(b[0])[-1] != "0" or b[0] == (x - 1) and str(b[0])[-1] != "0" \
                                or b[0] == (x - 11) and str(b[0])[-1] != "0" else self._field[a]                                 # условие для левой стороны от корабля (помечаем морские клетки, рядом с кораблём)
                        break
                    elif move == "down" and x <= 90 and self.__arrange_ships_two(x, move):                                       # второе условие, при котором корабль может быть установлен (вертикально)
                        for a, b in self._field.items():                                                                         # в цикле модернизируем игровое поле, клетки с кораблями и морем вокруг кораблей меняют свои значения
                            if b[0] == x:                                                        
                                self._field[a] = [x, self.__class__.ship_icon]                                 
                            if b[0] == x + 10:                       
                                self._field[a] = [x + 10, self.__class__.ship_icon]                    
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 10) or \
                                b[0] == (x + 20) else self._field[a]                                                             # условие для верха и низа от корабля (помечаем морские клетки, рядом с кораблём)
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 9) \
                                and str(b[0])[-1] != "1" or b[0] == (x + 1) and str(b[0])[-1] != "1" or \
                                b[0] == (x + 11) and str(b[0])[-1] != "1" or \
                                b[0] == (x + 21) and str(b[0])[-1] != "1" else self._field[a]                                    # условие для правой стороны от корабля (помечаем морские клетки, рядом с кораблём)
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x + 19) \
                                and str(b[0])[-1] != "0" or b[0] == (x + 9) and str(b[0])[-1] != "0" or \
                                b[0] == (x - 1) and str(b[0])[-1] != "0" or \
                                b[0] == (x - 11) and str(b[0])[-1] != "0" else self._field[a]                                    # условие для левой стороны от корабля (помечаем морские клетки, рядом с кораблём)
                        break
            if i == 1:                                                                                                           # условие для одно-палубного
                while True:                                                                                                      # цикл повторяется пока не будут найдены подходящие координаты для установки корабля                
                    x = random.randint(1, 100)                                                                                   # рандомные координаты, которые генерируются в цикле пока не будет найдена подходящая точка
                    if self.__arrange_ships_one(x):                                                                              # условие, при котором корабль может быть установлен
                        for a, b in self._field.items():                                                                         # в цикле модернизируем игровое поле, клетки с кораблями и морем вокруг кораблей меняют свои значения
                            if b[0] == x:                                                        
                                self._field[a] = [x, self.__class__.ship_icon]                                                              
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 10) or \
                                b[0] == (x + 10) else self._field[a]                                                             # условие для верха и низа от корабля (помечаем морские клетки, рядом с кораблём)       
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x - 9) \
                                and str(b[0])[-1] != "1" or b[0] == (x + 1) and str(b[0])[-1] != "1" \
                                or b[0] == (x + 11) and str(b[0])[-1] != "1" else self._field[a]                                 # условие для правой стороны от корабля (помечаем морские клетки, рядом с кораблём)         
                            self._field[a] = [b[0], self.__class__.sea_icon_block] if b[0] == (x + 9) \
                                and str(b[0])[-1] != "0" or b[0] == (x - 1) and str(b[0])[-1] != "0" \
                                or b[0] == (x - 11) and str(b[0])[-1] != "0" else self._field[a]                                 # условие для левой стороны от корабля (помечаем морские клетки, рядом с кораблём)
                        break    

    """МЕТОД-addon, КОТОРЫЙ РЕАЛИЗУЕТ SETTER ДЛЯ ИГРОВОГО ПОЛЯ КОТОРОЕ ПРЕДНАЗНАЧЕНО ДЛЯ ХОДОВ (ИНКАПСУЛИРОВАННЫЙ)"""
    def __set_field_go_addon(self, value):                                                                                       # возвращает уже готовый правильный вид игрового поля в основной setter в виде словаря, в котором ключи - это координаты, а значения - это списки с номерами клетки и иконкой для неё
        coordinates = value[0]    
        icon = value[1]
        for a, b in self._field_go.items():
            if coordinates == a:
                self._field_go[a] = [b[0], icon]
        return self._field_go

    """МЕТОД, КОТОРЫЙ РЕАЛИЗУЕТ GETTER И SETTER ДЛЯ ЧАСТИ ИГРОВОГО ПОЛЯ КОТОРОЕ ПРЕДНАЗНАЧЕНО ДЛЯ ХОДОВ"""
    def get_field_go(self):                                                                                                      # getter, который возвращает сразу часть поля для ходов - это словарь, где ключи - это значения координат, а значения ключей - это список с номером клетки и её иконкой
        return self._field_go        
    def set_field_go(self, value):                                                                                               # setter меняет часть поля, предназначенную для ходов. Переменная value должна быть кортежом или словарём.
        self._field_go = self.__set_field_go_addon(value)                                                                        # требуется дополнительная обработка инкапсулированным методом "__set_field_go_addon"
    field_go = property(get_field_go, set_field_go) 

    """МЕТОД-addon, КОТОРЫЙ РЕАЛИЗУЕТ SETTER ДЛЯ ИГРОВОГО ПОЛЯ КОТОРОЕ С КОРАБЛЯМИ (ИНКАПСУЛИРОВАННЫЙ)"""
    def __set_field_addon(self, value):                                                                                          # возвращает уже готовый правильный вид игрового поля в основной setter в виде словаря, в котором ключи - это координаты, а значения - это списки с номерами клетки и иконкой для неё
        coordinates = value[0]    
        icon = value[1]
        for a, b in self._field.items():
            if coordinates == a:
                self._field[a] = [b[0], icon]
        return self._field

    """МЕТОД, КОТОРЫЙ РЕАЛИЗУЕТ GETTER И SETTER ДЛЯ ЧАСТИ ИГРОВОГО ПОЛЯ КОТОРОЕ СОДЕРЖИТ КОРАБЛИ"""
    def get_field(self):                                                                                                         # getter, который возвращает сразу часть поля для кораблей - это словарь, где ключи - это значения координат, а значения ключей - это список с номером клетки и её иконкой
        return self._field        
    def set_field(self, value):                                                                                                  # setter меняет часть поля, предназначенную для кораблей. Переменная value должна быть кортежом или списком.
        self._field = self.__set_field_addon(value)                                                                              # требуется дополнительная обработка инкапсулированным методом "__set_field_addon"
    field_ship = property(get_field, set_field) 

"""ФУНКЦИЯ, КОТОРАЯ ОПРЕДЕЛЯЕТ СЛЕДУЮЩИЙ ВЫСТРЕЛ ДЛЯ КОМПЬЮТЕРА, ЕСЛИ КОРАБЛЬ РАНЕН И ИМЕЕТ ВЕРТИКАЛЬНУЮ ОРИЕНТАЦИЮ."""
def vertical_shot(temp_dict, shot_cpu):
    ### -1
    if (str(int(shot_cpu[0:-1]) - 1) + shot_cpu[-1]) in temp_dict \
        and temp_dict[(str(int(shot_cpu[0:-1]) - 1) + shot_cpu[-1])][-1] != Sea_battle.hit_icon \
        and temp_dict[(str(int(shot_cpu[0:-1]) - 1) + shot_cpu[-1])][-1] != Sea_battle.miss_icon:                                                                                          
        return (str(int(shot_cpu[0:-1]) - 1) + shot_cpu[-1])                                                                                                                                                    # 1 строка наверх
    ### +1
    elif (str(int(shot_cpu[0:-1]) + 1) + shot_cpu[-1]) in temp_dict \
        and temp_dict[(str(int(shot_cpu[0:-1]) + 1) + shot_cpu[-1])][-1] != Sea_battle.hit_icon \
        and temp_dict[(str(int(shot_cpu[0:-1]) + 1) + shot_cpu[-1])][-1] != Sea_battle.miss_icon:                                                                                          
        return (str(int(shot_cpu[0:-1]) + 1) + shot_cpu[-1])                                                                                                                                                    # 1 строка вниз
    ### -2
    elif (str(int(shot_cpu[0:-1]) - 2) + shot_cpu[-1]) in temp_dict \
        and temp_dict[(str(int(shot_cpu[0:-1]) - 2) + shot_cpu[-1])][-1] != Sea_battle.hit_icon \
        and temp_dict[(str(int(shot_cpu[0:-1]) - 2) + shot_cpu[-1])][-1] != Sea_battle.miss_icon \
        and temp_dict[(str(int(shot_cpu[0:-1]) - 1) + shot_cpu[-1])][-1] != Sea_battle.miss_icon:
        return (str(int(shot_cpu[0:-1]) - 2) + shot_cpu[-1])                                                                                                                                                    # 2 строки наверх
    ### +2
    elif (str(int(shot_cpu[0:-1]) + 2) + shot_cpu[-1]) in temp_dict \
        and temp_dict[(str(int(shot_cpu[0:-1]) + 2) + shot_cpu[-1])][-1] != Sea_battle.hit_icon \
        and temp_dict[(str(int(shot_cpu[0:-1]) + 2) + shot_cpu[-1])][-1] != Sea_battle.miss_icon \
        and temp_dict[(str(int(shot_cpu[0:-1]) + 1) + shot_cpu[-1])][-1] != Sea_battle.miss_icon:                                                                                          
        return (str(int(shot_cpu[0:-1]) + 2) + shot_cpu[-1])                                                                                                                                                    # 2 строки вниз
    ### -3
    elif (str(int(shot_cpu[0:-1]) - 3) + shot_cpu[-1]) in temp_dict \
        and temp_dict[(str(int(shot_cpu[0:-1]) - 3) + shot_cpu[-1])][-1] != Sea_battle.hit_icon \
        and temp_dict[(str(int(shot_cpu[0:-1]) - 3) + shot_cpu[-1])][-1] != Sea_battle.miss_icon \
        and temp_dict[(str(int(shot_cpu[0:-1]) - 2) + shot_cpu[-1])][-1] != Sea_battle.miss_icon \
        and temp_dict[(str(int(shot_cpu[0:-1]) - 1) + shot_cpu[-1])][-1] != Sea_battle.miss_icon:
        return (str(int(shot_cpu[0:-1]) - 3) + shot_cpu[-1])                                                                                                                                                    # 3 строки наверх
    ### +3
    elif (str(int(shot_cpu[0:-1]) + 3) + shot_cpu[-1]) in temp_dict \
        and temp_dict[(str(int(shot_cpu[0:-1]) + 3) + shot_cpu[-1])][-1] != Sea_battle.hit_icon \
        and temp_dict[(str(int(shot_cpu[0:-1]) + 3) + shot_cpu[-1])][-1] != Sea_battle.miss_icon \
        and temp_dict[(str(int(shot_cpu[0:-1]) + 2) + shot_cpu[-1])][-1] != Sea_battle.miss_icon \
        and temp_dict[(str(int(shot_cpu[0:-1]) + 1) + shot_cpu[-1])][-1] != Sea_battle.miss_icon:
        return (str(int(shot_cpu[0:-1]) + 3) + shot_cpu[-1])                                                                                                                                                    # 3 строки вниз
    else:
        return "ошибка"

"""ФУНКЦИЯ, КОТОРАЯ ОПРЕДЕЛЯЕТ СЛЕДУЮЩИЙ ВЫСТРЕЛ ДЛЯ КОМПЬЮТЕРА, ЕСЛИ КОРАБЛЬ РАНЕН И ИМЕЕТ ГОРИЗОНТАЛЬНУ ОРИЕНТАЦИЮ."""
def horizontal_shot(temp_dict, shot_cpu):
#    ### -1"К" 
    if shot_cpu[-1] == "К" and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 2))][-1] != Sea_battle.hit_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 2))][-1] != Sea_battle.miss_icon:        
        return (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 2))                                                                     # -1 символ, если буква в координате первого выстрела "К"
#    ### -1 не "К"  
    elif shot_cpu[-1] != "К" and (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 1)) in temp_dict \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 1))][-1] != Sea_battle.hit_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 1))][-1] != Sea_battle.miss_icon:                                                                                          
        return (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 1))                                                                     # -1 символ, если буква в координате первого выстрела не "К"        
#    ### +1"И"
    elif shot_cpu[-1] == "И" and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 2))][-1] != Sea_battle.hit_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 2))][-1] != Sea_battle.miss_icon:                                                                                          
        return (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 2))                                                                     # +1 символ, если буква в координате первого выстрела "И"    
    ### +1 не "И"
    elif shot_cpu[-1] != "И" and (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 1)) in temp_dict \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 1))][-1] != Sea_battle.hit_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 1))][-1] != Sea_battle.miss_icon:                                                                                          
        return (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 1))                                                                     # +1 символ, если буква в координате первого выстрела не "И"
#    ### -2 "К"
    elif shot_cpu[-1] == "К" and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 3))][-1] != Sea_battle.hit_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 3))][-1] != Sea_battle.miss_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 2))][-1] != Sea_battle.miss_icon:        
        return (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 3))                                                                     # -2 символа, если буква в координате первого выстрела "К"
#    ### -2 не "К"
    elif shot_cpu[-1] != "К" and (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 2)) in temp_dict \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 1))][-1] != Sea_battle.miss_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 2))][-1] != Sea_battle.hit_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 2))][-1] != Sea_battle.miss_icon:                                                                                          
        return (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 2))                                                                     # -2 символа, если буква в координате первого выстрела не "К"
#    ### +2 "З"
    elif shot_cpu[-1] == "З" and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 3))][-1] != Sea_battle.hit_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 3))][-1] != Sea_battle.miss_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 1))][-1] != Sea_battle.miss_icon:                                                                                          
        return (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 3))                                                                     # +2 символа, если буква в координате первого выстрела "З"
#    ### +2 не "З"
    elif shot_cpu[-1] != "З" and (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 2)) in temp_dict \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 2))][-1] != Sea_battle.hit_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 2))][-1] != Sea_battle.miss_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 1))][-1] != Sea_battle.miss_icon:                                                                                          
        return (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 2))                                                                     # +2 символа, если буква в координате первого выстрела не "З"
#    ### -3 "К"
    elif shot_cpu[-1] == "К" and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 4))][-1] != Sea_battle.hit_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 4))][-1] != Sea_battle.miss_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 3))][-1] != Sea_battle.miss_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 2))][-1] != Sea_battle.miss_icon:        
        return (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 4))                                                                     # -3 символа, если буква в координате первого выстрела "К"
#    ### -3 не "К"
    elif shot_cpu[-1] != "К" and (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 3)) in temp_dict \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 3))][-1] != Sea_battle.hit_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 3))][-1] != Sea_battle.miss_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 2))][-1] != Sea_battle.miss_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 1))][-1] != Sea_battle.miss_icon:                                                                                          
        return (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) - 3))                                                                     # -3 символа, если буква в координате первого выстрела не "К"
#    ### +3 "Ж"
    elif shot_cpu[-1] == "Ж" and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 4))][-1] != Sea_battle.hit_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 4))][-1] != Sea_battle.miss_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 3))][-1] != Sea_battle.miss_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 2))][-1] != Sea_battle.miss_icon:                                                                                          
        return (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 4))                                                                     # +3 символа, если буква в координате первого выстрела "Ж"
#    ### +3 не "Ж"
    elif shot_cpu[-1] != "Ж" and (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 3)) in temp_dict \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 3))][-1] != Sea_battle.hit_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 3))][-1] != Sea_battle.miss_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 2))][-1] != Sea_battle.miss_icon \
        and temp_dict[(shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 1))][-1] != Sea_battle.miss_icon:                                                                                          
        return (shot_cpu[0:-1] + chr(ord(shot_cpu[-1]) + 3))                                                                     # +3 символа, если буква в координате первого выстрела не "Ж"    
    else:
        return "ошибка"

"""ФУНКЦИЯ, КОТОРАЯ ПРОСТО ОПРЕДЕЛЯЕТ ВСЕХ СОСЕДЕЙ ТОЧКИ ПО ВЕРТИКАЛИ И ГОРИЗОНТАЛИ.
ВОЗВРАЩАЕТ СПИСОК КООРДИНАТ."""
def vertical_and_horizontal_neighborhood_check_3(point):                                                                                               
    if point == "1А":
        temp = ["1Б", "2А"]                             
    elif len(point) == 2 and point[0] == "1" and point != "1И" and point != "1К":
        left = point[0] + chr(ord(point[1]) - 1)
        right = point[0] + chr(ord(point[1]) + 1)
        down = str(int(point[0]) + 1) + point[1]
        temp = [left, right, down]
    elif point == "1И":
        left = point[0] + chr(ord(point[1]) - 1)
        right = point[0] + chr(ord(point[1]) + 2)
        down = str(int(point[0]) + 1) + point[1]
        temp = [left, right, down]
    elif point == "1К":
        temp = ["1И", "2К"]
    elif point[-1] == "К" and point != "10К":
        up = str(int(point[0]) - 1) + point[1]
        down = str(int(point[0]) + 1) + point[1]
        left = point[0] + chr(ord(point[1]) - 2)
        temp = [up, down, left]
    elif point == "10К":
        temp = ["10И", "9К"]
    elif point == "10И":
        up = str(int(point[0:-1]) - 1) + point[-1]
        right = point[0:-1] + chr(ord(point[-1]) + 2)
        left = point[0:-1] + chr(ord(point[-1]) - 1)                
        temp = [up, right, left]
    elif len(point) == 3 and point != "10А":
        up = str(int(point[0:-1]) - 1) + point[-1]
        right = point[0:-1] + chr(ord(point[-1]) + 1)
        left = point[0:-1] + chr(ord(point[-1]) - 1)  
        temp = [up, right, left]
    elif point == "10А":
        temp = ["9А", "10Б"]
    elif point[-1] == "А":
        up = str(int(point[0]) - 1) + point[1]
        left = point[0] + chr(ord(point[1]) + 1)
        down = str(int(point[0]) + 1) + point[1]
        temp = [up, left, down]
    elif point[-1] == "И":
        up = str(int(point[0]) - 1) + point[1]
        right = point[0] + chr(ord(point[1]) + 2)
        down = str(int(point[0]) + 1) + point[1]
        left = point[0] + chr(ord(point[1]) - 1)
        temp = [up, right, down, left]
    else:
        up = str(int(point[0]) - 1) + point[1]
        right = point[0] + chr(ord(point[1]) + 1)
        down = str(int(point[0]) + 1) + point[1]
        left = point[0] + chr(ord(point[1]) - 1)
        temp = [up, right, down, left]
    return temp

"""ФУНКЦИЯ, КОТОРАЯ ПРОВЕРЯЕТ ЕСТЬ ЛИ СОСЕДСТВО ПО ВЕРТИКАЛИ И ГОРИЗОНТАЛИ '⚓' с '❌', ТОЛЬКО ДЛЯ ТЕХ КЛЕТОК, КОТОРЫЕ САМИ с '❌'."""
def vertical_and_horizontal_neighborhood_check_2(point, field):                                                                 
    if point == "1А" and field[point][-1] == Sea_battle.hit_icon:
        temp = ["1Б", "2А"]                      
        result = set()
        for a in temp:
            if field[a][1] == Sea_battle.ship_icon:
                result.add("ранен")
            else:
                result.add("не ранен")
    elif len(point) == 2 and point[0] == "1" and point != "1И" and point != "1К" and field[point][-1] == Sea_battle.hit_icon:
        left = point[0] + chr(ord(point[1]) - 1)
        right = point[0] + chr(ord(point[1]) + 1)
        down = str(int(point[0]) + 1) + point[1]
        temp = [left, right, down]
        result = set()
        for a in temp:
            if field[a][1] == Sea_battle.ship_icon:
                result.add("ранен")
            else:
                result.add("не ранен")
    elif point == "1И" and field[point][-1] == Sea_battle.hit_icon:
        left = point[0] + chr(ord(point[1]) - 1)
        right = point[0] + chr(ord(point[1]) + 2)
        down = str(int(point[0]) + 1) + point[1]
        temp = [left, right, down]
        result = set()
        for a in temp:
            if field[a][1] == Sea_battle.ship_icon:
                result.add("ранен")
            else:
                result.add("не ранен")
    elif point == "1К" and field[point][-1] == Sea_battle.hit_icon:
        temp = ["1И", "2К"]
        result = set()
        for a in temp:
            if field[a][1] == Sea_battle.ship_icon:
                result.add("ранен")
            else:
                result.add("не ранен")
    elif point[-1] == "К" and point != "10К" and field[point][-1] == Sea_battle.hit_icon:
        up = str(int(point[0]) - 1) + point[1]
        down = str(int(point[0]) + 1) + point[1]
        left = point[0] + chr(ord(point[1]) - 2)
        temp = [up, down, left]
        result = set()
        for a in temp:
            if field[a][1] == Sea_battle.ship_icon:
                result.add("ранен")
            else:
                result.add("не ранен")
    elif point == "10К" and field[point][-1] == Sea_battle.hit_icon:
        temp = ["10И", "9К"]
        result = set()
        for a in temp:
            if field[a][1] == Sea_battle.ship_icon:
                result.add("ранен")
            else:
                result.add("не ранен")
    elif point == "10И" and field[point][-1] == Sea_battle.hit_icon:
        up = str(int(point[0:-1]) - 1) + point[-1]
        right = point[0:-1] + chr(ord(point[-1]) + 2)
        left = point[0:-1] + chr(ord(point[-1]) - 1)                
        temp = [up, right, left]
        result = set()
        for a in temp:
            if field[a][1] == Sea_battle.ship_icon:
                result.add("ранен")
            else:
                result.add("не ранен")
    elif len(point) == 3 and point != "10А" and field[point][-1] == Sea_battle.hit_icon:
        up = str(int(point[0:-1]) - 1) + point[-1]
        right = point[0:-1] + chr(ord(point[-1]) + 1)
        left = point[0:-1] + chr(ord(point[-1]) - 1)  
        temp = [up, right, left]
        result = set()
        for a in temp:
            if field[a][1] == Sea_battle.ship_icon:
                result.add("ранен")
            else:
                result.add("не ранен")
    elif point == "10А" and field[point][-1] == Sea_battle.hit_icon:
        temp = ["9А", "10Б"]
        result = set()
        for a in temp:
            if field[a][1] == Sea_battle.ship_icon:
                result.add("ранен")
            else:
                result.add("не ранен")
    elif point[-1] == "А" and field[point][-1] == Sea_battle.hit_icon:
        up = str(int(point[0]) - 1) + point[1]
        left = point[0] + chr(ord(point[1]) + 1)
        down = str(int(point[0]) + 1) + point[1]
        temp = [up, left, down]
        result = set()
        for a in temp:
            if field[a][1] == Sea_battle.ship_icon:
                result.add("ранен")
            else:
                result.add("не ранен")
    elif point[-1] == "И" and field[point][-1] == Sea_battle.hit_icon:
        up = str(int(point[0]) - 1) + point[1]
        right = point[0] + chr(ord(point[1]) + 2)
        down = str(int(point[0]) + 1) + point[1]
        left = point[0] + chr(ord(point[1]) - 1)
        temp = [up, right, down, left]
        result = set()
        for a in temp:
            if field[a][1] == Sea_battle.ship_icon:
                result.add("ранен")
            else:
                result.add("не ранен")
    elif field[point][-1] == Sea_battle.hit_icon:
        up = str(int(point[0]) - 1) + point[1]
        right = point[0] + chr(ord(point[1]) + 1)
        down = str(int(point[0]) + 1) + point[1]
        left = point[0] + chr(ord(point[1]) - 1)
        temp = [up, right, down, left]
        result = set()
        for a in temp:
            if field[a][1] == Sea_battle.ship_icon:
                result.add("ранен")
            else:
                result.add("не ранен")
    else:
        result = set()
    return result

"""ФУНКЦИЯ, КОТОРАЯ ГЕНЕРИРУЕТ ВЫСТРЕЛ ДЛЯ CPU."""
def function_input_coordinates_for_cpu(temp_dict):
    go = []
    for a, b in temp_dict.items():
        if b[1] != Sea_battle.hit_icon and b[1] != Sea_battle.miss_icon:
            go.append(a)
    return random.choice(go)

"""ФУНКЦИЯ, КОТОРАЯ ИЗМЕНЯЕТ СОСЕДЕЙ ВОКРУГ С КЛЕТКОЙ "🟪"."""
def changing_neighbors_around(point, field):                                                                                                         
        if point == "1А":
            temp = ["1Б", "2Б", "2А"]                
        elif len(point) == 2 and point[0] == "1" and point != "1И" and point != "1К" and field[point][-1] == Sea_battle.hit_icon:
            left = point[0] + chr(ord(point[1]) - 1)
            right = point[0] + chr(ord(point[1]) + 1)
            down = str(int(point[0]) + 1) + point[1]
            down_left = str(int(point[0]) + 1) + chr(ord(point[1]) - 1)
            down_right = str(int(point[0]) + 1) + chr(ord(point[1]) + 1)
            temp = [left, right, down, down_left, down_right]
        elif point == "1И" and field[point][-1] == Sea_battle.hit_icon:
            left = point[0] + chr(ord(point[1]) - 1)
            right = point[0] + chr(ord(point[1]) + 2)
            down = str(int(point[0]) + 1) + point[1]
            down_left = str(int(point[0]) + 1) + chr(ord(point[1]) - 1)
            down_right = str(int(point[0]) + 1) + chr(ord(point[1]) + 2)
            temp = [left, right, down, down_left, down_right]             
        elif point == "1К" and field[point][-1] == Sea_battle.hit_icon:
            temp = ["1И", "2И", "2К"]
        elif point[-1] == "К" and point != "10К" and field[point][-1] == Sea_battle.hit_icon:
            up = str(int(point[0]) - 1) + point[1]
            down = str(int(point[0]) + 1) + point[1]
            left = point[0] + chr(ord(point[1]) - 2)
            up_left = str(int(point[0]) - 1) + chr(ord(point[1]) - 2)
            down_left = str(int(point[0]) + 1) + chr(ord(point[1]) - 2) 
            temp = [up, down, left, up_left, down_left]
        elif point == "10К" and field[point][-1] == Sea_battle.hit_icon:
            temp = ["9И", "10И", "9К"]            
        elif point == "10И" and field[point][-1] == Sea_battle.hit_icon:
            up = str(int(point[0:-1]) - 1) + point[-1]
            right = point[0:-1] + chr(ord(point[-1]) + 2)
            left = point[0:-1] + chr(ord(point[-1]) - 1)                
            up_left = str(int(point[0:-1]) - 1) + chr(ord(point[-1]) - 1)
            up_right = str(int(point[0:-1]) - 1) + chr(ord(point[-1]) + 2)
            temp = [up, right, left, up_left, up_right]
        elif len(point) == 3 and point != "10А" and field[point][-1] == Sea_battle.hit_icon:
            up = str(int(point[0:-1]) - 1) + point[-1]
            right = point[0:-1] + chr(ord(point[-1]) + 1)
            left = point[0:-1] + chr(ord(point[-1]) - 1)  
            up_left = str(int(point[0:-1]) - 1) + chr(ord(point[-1]) - 1)
            up_right = str(int(point[0:-1]) - 1) + chr(ord(point[-1]) + 1)
            temp = [up, right, left, up_left, up_right]
        elif point == "10А" and field[point][-1] == Sea_battle.hit_icon:
            temp = ["9А", "9Б", "10Б"]            
        elif point[-1] == "А" and field[point][-1] == Sea_battle.hit_icon:
            up = str(int(point[0]) - 1) + point[1]
            left = point[0] + chr(ord(point[1]) + 1)
            down = str(int(point[0]) + 1) + point[1]
            up_left = str(int(point[0]) - 1) + chr(ord(point[1]) + 1)
            down_left = str(int(point[0]) + 1) + chr(ord(point[1]) + 1)
            temp = [up, left, down, up_left, down_left]            
        elif point[-1] == "И" and field[point][-1] == Sea_battle.hit_icon:
            up = str(int(point[0]) - 1) + point[1]
            right = point[0] + chr(ord(point[1]) + 2)
            down = str(int(point[0]) + 1) + point[1]
            left = point[0] + chr(ord(point[1]) - 1)
            up_left = str(int(point[0]) - 1) + chr(ord(point[1]) - 1)
            up_right = str(int(point[0]) - 1) + chr(ord(point[1]) + 2)
            down_left = str(int(point[0]) + 1) + chr(ord(point[1]) - 1)
            down_right = str(int(point[0]) + 1) + chr(ord(point[1]) + 2)
            temp = [up, right, down, left, up_left, up_right, down_left, down_right]
        elif field[point][-1] == Sea_battle.hit_icon:
            up = str(int(point[0]) - 1) + point[1]
            right = point[0] + chr(ord(point[1]) + 1)
            down = str(int(point[0]) + 1) + point[1]
            left = point[0] + chr(ord(point[1]) - 1)
            up_left = str(int(point[0]) - 1) + chr(ord(point[1]) - 1)
            up_right = str(int(point[0]) - 1) + chr(ord(point[1]) + 1)
            down_left = str(int(point[0]) + 1) + chr(ord(point[1]) - 1)
            down_right = str(int(point[0]) + 1) + chr(ord(point[1]) + 1)
            temp = [up, right, down, left, up_left, up_right, down_left, down_right]
        for i in temp:
            if field[i][1] == Sea_battle.sea_icon_block:
                field[i][1] = Sea_battle.miss_icon
        return field

"""addon №1 ПРОИЗВОДИТ ОТБОР СОСЕДЕЙ ТОЛЬКО С '❌' И ОПРЕДЕЛЯЕТ ПОТОПЛЕН КОРАБЛЬ ИЛИ НЕТ (НАЛИЧИЕ '⚓')."""
def determining_vertical_and_horizontal_neighbors_addon(temp, field):
    result = [[]]
    for a in temp:
        if field[a][1] == Sea_battle.hit_icon:
            result[0].append(a)
        if field[a][1] == Sea_battle.ship_icon:
            result.append("alive")                                                                                               # в списке "result" появляется метка "alive" (корабль жив)
    return result

"""ФУНКЦИЯ, КОТОРАЯ ВОЗВРАЩАЕТ СОСЕДЕЙ ПО ВЕРТИКАЛИ И ГОРИЗОНТАЛИ с '❌', ТОЛЬКО ДЛЯ ТЕХ КЛЕТОК, КОТОРЫЕ САМИ с '❌'.
ДОПОЛНИТЕЛЬНАЯ ПРОВЕРКА КЛЕТОК НАПИСАНА В <addon №1>. МОДИФИКАЦИЯ КЛЕТОК НАПИСАНА В <addon №2>."""
def determining_vertical_and_horizontal_neighbors(point, field, for_basic_case):                                                 # ФУНКЦИЯ БУДЕТ ВЫЗЫВАТЬСЯ РЕКУРСИВНО, А В РЕКУРСИИ БУДУТ ВЫЗЫВАТЬСЯ НЕ РЕКУРСИНО ДРУГИЕ ДВЕ ФУНКЦИИ
        if point in for_basic_case:                                                                                              # базовый случай                     
            pass
        else:
            for_basic_case.append(point)                                                                                         # модернизация переменной для базового случая, данная точка больше не будет учитываться (условие в базовом случае)                                                                                                                    
            if point == "1А" and field[point][-1] == Sea_battle.hit_icon:
                temp = ["1Б", "2А"]                
                result = determining_vertical_and_horizontal_neighbors_addon(temp, field) 
                for i in result[0]:
                    determining_vertical_and_horizontal_neighbors(i, field, for_basic_case)
                if len(result) == 1:
                    field = changing_neighbors_around(point, field)                    
            elif len(point) == 2 and point[0] == "1" and point != "1И" and point != "1К" and field[point][-1] == Sea_battle.hit_icon:
                left = point[0] + chr(ord(point[1]) - 1)
                right = point[0] + chr(ord(point[1]) + 1)
                down = str(int(point[0]) + 1) + point[1]
                temp = [left, right, down]
                result = determining_vertical_and_horizontal_neighbors_addon(temp, field)             
                for i in result[0]:
                    determining_vertical_and_horizontal_neighbors(i, field, for_basic_case)
                if len(result) == 1:
                    field = changing_neighbors_around(point, field)        
            elif point == "1И" and field[point][-1] == Sea_battle.hit_icon:
                left = point[0] + chr(ord(point[1]) - 1)
                right = point[0] + chr(ord(point[1]) + 2)
                down = str(int(point[0]) + 1) + point[1]
                temp = [left, right, down]
                result = determining_vertical_and_horizontal_neighbors_addon(temp, field)             
                for i in result[0]:
                    determining_vertical_and_horizontal_neighbors(i, field, for_basic_case)
                if len(result) == 1:
                    field = changing_neighbors_around(point, field)                
            elif point == "1К" and field[point][-1] == Sea_battle.hit_icon:
                temp = ["1И", "2К"]
                result = determining_vertical_and_horizontal_neighbors_addon(temp, field) 
                for i in result[0]:
                    determining_vertical_and_horizontal_neighbors(i, field, for_basic_case)              
                if len(result) == 1:
                    field = changing_neighbors_around(point, field)                    
            elif point[-1] == "К" and point != "10К" and field[point][-1] == Sea_battle.hit_icon:
                up = str(int(point[0]) - 1) + point[1]
                down = str(int(point[0]) + 1) + point[1]
                left = point[0] + chr(ord(point[1]) - 2)
                temp = [up, down, left]
                result = determining_vertical_and_horizontal_neighbors_addon(temp, field)             
                for i in result[0]:
                    determining_vertical_and_horizontal_neighbors(i, field, for_basic_case)
                if len(result) == 1:
                    field = changing_neighbors_around(point, field)
            elif point == "10К" and field[point][-1] == Sea_battle.hit_icon:
                temp = ["10И", "9К"]
                result = determining_vertical_and_horizontal_neighbors_addon(temp, field) 
                for i in result[0]:
                    determining_vertical_and_horizontal_neighbors(i, field, for_basic_case)
                if len(result) == 1:
                    field = changing_neighbors_around(point, field)        
            elif point == "10И" and field[point][-1] == Sea_battle.hit_icon:
                up = str(int(point[0:-1]) - 1) + point[-1]
                right = point[0:-1] + chr(ord(point[-1]) + 2)
                left = point[0:-1] + chr(ord(point[-1]) - 1)                
                temp = [up, right, left]
                result = determining_vertical_and_horizontal_neighbors_addon(temp, field)             
                for i in result[0]:
                    determining_vertical_and_horizontal_neighbors(i, field, for_basic_case)
                if len(result) == 1:
                    field = changing_neighbors_around(point, field)        
            elif len(point) == 3 and point != "10А" and field[point][-1] == Sea_battle.hit_icon:
                up = str(int(point[0:-1]) - 1) + point[-1]
                right = point[0:-1] + chr(ord(point[-1]) + 1)
                left = point[0:-1] + chr(ord(point[-1]) - 1)  
                temp = [up, right, left]
                result = determining_vertical_and_horizontal_neighbors_addon(temp, field)             
                for i in result[0]:
                    determining_vertical_and_horizontal_neighbors(i, field, for_basic_case)
                if len(result) == 1:
                    field = changing_neighbors_around(point, field)        
            elif point == "10А" and field[point][-1] == Sea_battle.hit_icon:
                temp = ["9А", "10Б"]
                result = determining_vertical_and_horizontal_neighbors_addon(temp, field) 
                for i in result[0]:
                    determining_vertical_and_horizontal_neighbors(i, field, for_basic_case)                
                if len(result) == 1:
                    field = changing_neighbors_around(point, field)
            elif point[-1] == "А" and field[point][-1] == Sea_battle.hit_icon:
                up = str(int(point[0]) - 1) + point[1]
                left = point[0] + chr(ord(point[1]) + 1)
                down = str(int(point[0]) + 1) + point[1]
                temp = [up, left, down]
                result = determining_vertical_and_horizontal_neighbors_addon(temp, field)             
                for i in result[0]:
                    determining_vertical_and_horizontal_neighbors(i, field, for_basic_case)
                if len(result) == 1:
                    field = changing_neighbors_around(point, field)
            elif point[-1] == "И" and field[point][-1] == Sea_battle.hit_icon:
                up = str(int(point[0]) - 1) + point[1]
                right = point[0] + chr(ord(point[1]) + 2)
                down = str(int(point[0]) + 1) + point[1]
                left = point[0] + chr(ord(point[1]) - 1)
                temp = [up, right, down, left]
                result = determining_vertical_and_horizontal_neighbors_addon(temp, field)             
                for i in result[0]:
                    determining_vertical_and_horizontal_neighbors(i, field, for_basic_case)
                if len(result) == 1:
                    field = changing_neighbors_around(point, field)
            elif field[point][-1] == Sea_battle.hit_icon:
                up = str(int(point[0]) - 1) + point[1]
                right = point[0] + chr(ord(point[1]) + 1)
                down = str(int(point[0]) + 1) + point[1]
                left = point[0] + chr(ord(point[1]) - 1)
                temp = [up, right, down, left]
                result = determining_vertical_and_horizontal_neighbors_addon(temp, field)             
                for i in result[0]:
                    determining_vertical_and_horizontal_neighbors(i, field, for_basic_case)
                if len(result) == 1:
                    field = changing_neighbors_around(point, field)
            return field
        
"""addon ОПРЕДЕЛЯЕТ СОСЕДСТВО КЛЕТКИ С '❌' И КЛЕТОК С '⚓'."""
def vertical_and_horizontal_neighborhood_check_addon(temp, field):    
    result = []
    for a in temp:
        if field[a][1] == Sea_battle.ship_icon:
            result.append(True)
    return True if True in result else False

"""ФУНКЦИЯ, КОТОРАЯ ПРОВЕРЯЕТ ЕСТЬ ЛИ СОСЕДСТВО ПО ВЕРТИКАЛИ И ГОРИЗОНТАЛИ '⚓' с '❌', ТОЛЬКО ДЛЯ ТЕХ КЛЕТОК, КОТОРЫЕ САМИ с '❌'.
ФУНКЦИЯ ВОЗВРАЩАЕТ СПИСОК, КОТОРЫЙ МОЖЕТ СОДЕРЖАТЬ TRUE, А МОЖЕТ НЕ СОДЕРЖАТЬ."""
def vertical_and_horizontal_neighborhood_check(point, field, temp_list):                                                         # Определяет соседние клетки и передаёт в функцию-addon их список. Addon возвращает True или False (проверяет окончательно на соседство с '⚓').
    if point == "1А" and field[point][-1] == Sea_battle.hit_icon:
        temp = ["1Б", "2А"]                             
        result = vertical_and_horizontal_neighborhood_check_addon(temp, field)
        if result == True:
            temp_list.append(result)
    elif len(point) == 2 and point[0] == "1" and point != "1И" and point != "1К" and field[point][-1] == Sea_battle.hit_icon:
        left = point[0] + chr(ord(point[1]) - 1)
        right = point[0] + chr(ord(point[1]) + 1)
        down = str(int(point[0]) + 1) + point[1]
        temp = [left, right, down]
        result = vertical_and_horizontal_neighborhood_check_addon(temp, field)
        if result == True:
            temp_list.append(result)
    elif point == "1И" and field[point][-1] == Sea_battle.hit_icon:
        left = point[0] + chr(ord(point[1]) - 1)
        right = point[0] + chr(ord(point[1]) + 2)
        down = str(int(point[0]) + 1) + point[1]
        temp = [left, right, down]
        result = vertical_and_horizontal_neighborhood_check_addon(temp, field)
        if result == True:
            temp_list.append(result)
    elif point == "1К" and field[point][-1] == Sea_battle.hit_icon:
        temp = ["1И", "2К"]
        result = vertical_and_horizontal_neighborhood_check_addon(temp, field)
        if result == True:
            temp_list.append(result)
    elif point[-1] == "К" and point != "10К" and field[point][-1] == Sea_battle.hit_icon:
        up = str(int(point[0]) - 1) + point[1]
        down = str(int(point[0]) + 1) + point[1]
        left = point[0] + chr(ord(point[1]) - 2)
        temp = [up, down, left]
        result = vertical_and_horizontal_neighborhood_check_addon(temp, field)
        if result == True:
            temp_list.append(result)
    elif point == "10К" and field[point][-1] == Sea_battle.hit_icon:
        temp = ["10И", "9К"]
        result = vertical_and_horizontal_neighborhood_check_addon(temp, field)
        if result == True:
            temp_list.append(result)
    elif point == "10И" and field[point][-1] == Sea_battle.hit_icon:
        up = str(int(point[0:-1]) - 1) + point[-1]
        right = point[0:-1] + chr(ord(point[-1]) + 2)
        left = point[0:-1] + chr(ord(point[-1]) - 1)                
        temp = [up, right, left]
        result = vertical_and_horizontal_neighborhood_check_addon(temp, field)
        if result == True:
            temp_list.append(result)
    elif len(point) == 3 and point != "10А" and field[point][-1] == Sea_battle.hit_icon:
        up = str(int(point[0:-1]) - 1) + point[-1]
        right = point[0:-1] + chr(ord(point[-1]) + 1)
        left = point[0:-1] + chr(ord(point[-1]) - 1)  
        temp = [up, right, left]
        result = vertical_and_horizontal_neighborhood_check_addon(temp, field)
        if result == True:
            temp_list.append(result)
    elif point == "10А" and field[point][-1] == Sea_battle.hit_icon:
        temp = ["9А", "10Б"]
        result = vertical_and_horizontal_neighborhood_check_addon(temp, field)
        if result == True:
            temp_list.append(result)
    elif point[-1] == "А" and field[point][-1] == Sea_battle.hit_icon:
        up = str(int(point[0]) - 1) + point[1]
        left = point[0] + chr(ord(point[1]) + 1)
        down = str(int(point[0]) + 1) + point[1]
        temp = [up, left, down]
        result = vertical_and_horizontal_neighborhood_check_addon(temp, field)
        if result == True:
            temp_list.append(result)
    elif point[-1] == "И" and field[point][-1] == Sea_battle.hit_icon:
        up = str(int(point[0]) - 1) + point[1]
        right = point[0] + chr(ord(point[1]) + 2)
        down = str(int(point[0]) + 1) + point[1]
        left = point[0] + chr(ord(point[1]) - 1)
        temp = [up, right, down, left]
        result = vertical_and_horizontal_neighborhood_check_addon(temp, field)
        if result == True:
            temp_list.append(result)
    elif field[point][-1] == Sea_battle.hit_icon:
        up = str(int(point[0]) - 1) + point[1]
        right = point[0] + chr(ord(point[1]) + 1)
        down = str(int(point[0]) + 1) + point[1]
        left = point[0] + chr(ord(point[1]) - 1)
        temp = [up, right, down, left]
        result = vertical_and_horizontal_neighborhood_check_addon(temp, field)
        if result == True:
            temp_list.append(result)
    return temp_list

"""ФУНКЦИЯ, КОТОРАЯ ВОЗВРАЩАЕТ ОБНОВЛЁННЫЙ ОБЪЕКТ ВРАГА С ПОЛЕМ ДЛЯ КОРАБЛЕЙ ПОСЛЕ ХОДА ТЕКУЩЕГО ИГРОКА"""
def fuction_mod_object_of_enemy_ship_field_for_go_current_user(object, shot_player, package):
    object.field_ship = (shot_player, package)
    return object

"""ФУНКЦИЯ, КОТОРАЯ ВОЗВРАЩАЕТ ОБНОВЛЁННЫЙ ОБЪЕКТ С ПОЛЕМ ДЛЯ ТЕКУЩЕГО ИГРОКА (части для ходов) И ЗАМЕНЯЕТ ОБЪЕКТ НОВЫМ ЗНАЧЕНИЕМ"""
def fuction_mod_object_for_current_user_go(object, shot_player, package):
    object.field_go = (shot_player, package)
    return object

"""ФУНКЦИЯ, КОТОРАЯ ПРОВЕРЯЕТ СТАТУС КЛЕТКИ ИГРОВОГО ПОЛЯ С КОРАБЛЯМИ ПРОТИВНИКА"""
def function_check_cell(obj, shot):                                                                                              # в качестве параметров функция получает атрибут объект (словарь с расстановкой кораблей) и координаты выстрела игрока
    for a, b in obj.items():
        if a == shot:
            return b[1]

"""ФУНКЦИЯ, КОТОРАЯ РЕАЛИЗУЕТ ПРОЦЕСС ВВОДА КООРДИНАТ ВЫСТРЕЛА ОТ ИГРОКА"""
def function_input_coordinates():
    temp = []                                                                                                                    # в этот список будем класть все возможные варианты координат
    for a in Sea_battle.numbers:
        for b in  Sea_battle.letters:
            temp.append(a + b)                                                                                                   # кладём варианты координат в список
    while True:                                                                                                                  # повторяющийся цикл, пока не получим от пользователя существующие координаты
        result = input("Введите координаты выстрела (пример: 1А, 2А ... 10К): ").upper()
        if result in temp:
            break
        else:            
            print("Повторите ввод.")
            print()
    return result

"""ФУНКЦИЯ ДЛЯ ОКОНЧАТЕЛЬНОЙ ВИЗУАЛИЗАЦИИ ИГРОВОГО ПРОЦЕССА ПОЛЯ ИГРОКА (первая визуализация была описана в классе).
ФУНКЦИЯ В КАЧЕСТЕ ПАРАМЕТРА ПРИНИМАЕТ ОБЪЕКТ КЛАССА "Sea_battle"."""
def function_visualization(player):
    WIDTH, HEIGHT = bext.size()                                                                                                  # определить ширину и высоту экрана в em-(ах) (это размер символа) с помощью модуля bext
    bext.clear()                                                                                                                 # очистить экран с помощью модуля bext
    bext.goto(int(WIDTH / 75), int(HEIGHT / 4))                                                                                  # выберем расположение вывода поля игрока на экране с помощью модуля bext
    bext.fg("red")                                                                                                               # выберем цвет вывода шрифта на экране с помощью модуля bext
    print("ПОЛЕ ИГРОКА.\n")        
    player.show_field()                                                                                                          # используем методы класса, чтобы вывести игровое поле для игрока и поле для его выстрелов на экран
    print()

"""ОСНОВНАЯ ФУНКЦИЯ"""
def function_main():
    """В ЭТОМ БЛОКЕ СОЗДАДИМ ИГРОВЫЕ ПОЛЯ"""    
    player = Sea_battle()                                                                                                        # создадим объекты класса "игровое поле" для игрока 
    cpu = Sea_battle()                                                                                                           # создадим объекты класса "игровое поле" для компьютера 
    player.arrange_ships()                                                                                                       # используем метод класса, чтобы заполнить игровое поля для игрока кораблями
    cpu.arrange_ships()                                                                                                          # используем метод класса, чтобы заполнить игровое поля для компьютера кораблями   
    
    """ЗАПУСК ОСНОВНОГО ЦИКЛА ИГРЫ""" 
    response  = "Начинаем заново"                                                                                                # переменная понадобится для первого запуска условия в подцикле "для компьютера"
    init_vert_horizontal = set()                                                                                                 # переменная-множество понадобится для определения ориентации корабля (вертикаль или горизонталь)
    while True:                                                                                                                  # основной цикл прервётся только в случае окончания игры
        win = False                                                                                                              # переменная, по-умолчанию содержащая значение, что игра пока ещё не закончена

        """подцикл для игрока, следующий подцикл будет для компьютера"""
        while True:                                                                                                              
            function_visualization(player)                                                                                       # функция визуализации для поля игрока, поле компьютера выводить не надо                           
            shot_player = function_input_coordinates()                                                                           # функция, которая вызывает ввод координат выстрела от игрока и возвращает реальную, проверенную координату
            cell_status = function_check_cell(cpu.field_ship, shot_player)                                                       # функция проверки статуса клетки для компьютеного поля с расстановкой кораблей           
            if cell_status == Sea_battle.hit_icon or cell_status == Sea_battle.miss_icon:                                        # случай, если в эту клетку ранее уже производили выстрел, нужно отправить в начало цикла
                playsound.playsound("2.1.15.task_error.mp3")
                print()
                input("Такой выстрел ранее был произведён или это клетка рядом с потопленным кораблём. Нажмите <Enter> для повторения ввода. ")
                continue
            elif cell_status == Sea_battle.sea_icon or cell_status == Sea_battle.sea_icon_block:                                 # случай, при котором возможна модернизация основного поля компьютера и поля ходов у игрока
                package = Sea_battle.miss_icon                                                                                   # вводится переменная, которая содержит значение для иконки выстрела
                playsound.playsound("2.1.15.task_выстрел.mp3")
                playsound.playsound("2.1.15.task_вода.mp3")
            elif cell_status == Sea_battle.ship_icon:                                                                            # случай, при котором возможна модернизация основного поля компьютера и поля ходов у игрока
                package = Sea_battle.hit_icon                                                                                    # вводится переменная, которая содержит значение для иконки выстрела           
                playsound.playsound("2.1.15.task_выстрел.mp3")
                playsound.playsound("2.1.15.task_попадание.mp3")
            player = fuction_mod_object_for_current_user_go(player, shot_player, package)                                        # возвращает обновлённый объект с полем для текущего игрока (части для ходов) и заменяет объект новым значением            
            cpu = fuction_mod_object_of_enemy_ship_field_for_go_current_user(cpu, shot_player, package)                          # возвращает обновлённый объект с полем для cpu (части для кораблей) и заменяет объект новым значением
            """необходимо начать проверку убит/не убит"""
            temp_list = []
            for i in cpu.field_ship:
                temp_list = vertical_and_horizontal_neighborhood_check(i, cpu.field_ship, temp_list)    
            test = True if True not in temp_list else False                                                                      # проверка поля, если есть рядом '⚓' и '❌', то условие не выполняется и переменная будет False и следующую операцию выполнять нельзя          
            """обновим объект cpu (часть поля с кораблями), в случае уничтожения одного из кораблей вокруг этих клеток с кораблём
            появятся "⚪"."""
            if test:                                                                                                             # если рядом '⚓' и '❌', то условие не запустится
                for i in cpu.field_ship:
                    for_basic_case = []                                                                                          # эта переменная нужна для сбора информации, о том какие клетки уже посетили рекурсивно, и она должна быть именно здесь, а не в самой функции
                    cpu._field = determining_vertical_and_horizontal_neighbors(i, cpu.field_ship, for_basic_case)                # обновление словаря с полем для кораблей с обработкой каждой точки, проверяет убит ли корабль и ставаит "⚪" вокруг убитого корабля
            """обновим объект player (часть поля для ходов), в случае уничтожения одного из кораблей вокруг этих клеток с кораблём
            появятся "⚪". Перенесём "⚪" из cpu._field_ship в player._field_ship_go."""
            temp_dict = dict()
            for a, b in cpu.field_ship.items():
                if b[1] == Sea_battle.miss_icon:
                    temp_dict[a] = b
            for a, b in temp_dict.items():
                player._field_go[a] = b            
            """проверка победы игрока, конец игры"""
            check = set()
            for i in cpu.field_ship.values():
                if Sea_battle.ship_icon in i:
                    check.add(i[1])
            if Sea_battle.ship_icon not in check:
                win = True
                break
            """проверка повторного хода игрока, отправляем в начало цикла"""
            if cpu.field_ship[shot_player][1] == Sea_battle.hit_icon:
                continue
            break

        """Конец игры. Победа игрока!!!"""
        if win:
            function_visualization(player)
            print("Победа!!!")
            playsound.playsound("2.1.15.task_победа.mp3")
            break                                                                                                                # прерываем основной цикл
        
        """подцикл для компьютера"""
        while True:
            function_visualization(player)                                                                                       # функция визуализации для поля игрока, поле компьютера выводить не надо ----------> (НА ПОЛЕ ИГРОКА БУДУТ ВИДНЫ ХОДЫ КОМПТЮТЕРА!!!)                          
            if response == "Начинаем заново":                                                                                    # условие, если предыдущий корабль убит или это первый ход
                shot_cpu = function_input_coordinates_for_cpu(cpu.field_go)                                                      # функция, которая рандомно определяет выстрел cpu и возвращает реальную, проверенную координату, в которую раньше не стреляли
                cell_status = function_check_cell(player.field_ship, shot_cpu)                                                   # функция проверки статуса клетки для поля игрока, которое с кораблями
                if cell_status == Sea_battle.sea_icon or cell_status == Sea_battle.sea_icon_block:                               # случай, при котором возможна модернизация основного поля игрока и поля ходов у компьютера
                    package = Sea_battle.miss_icon                                                                               # вводится переменная, которая содержит значение для иконки выстрела
                elif cell_status == Sea_battle.ship_icon:                                                                        # случай, при котором возможна модернизация основного поля игрока и поля ходов у компьютера
                    package = Sea_battle.hit_icon                                                                                # вводится переменная, которая содержит значение для иконки выстрела          
                cpu = fuction_mod_object_for_current_user_go(cpu, shot_cpu, package)                                             # возвращает обновлённый объект с полем для компьютера (части для ходов) и заменяет объект новым значением
                player = fuction_mod_object_of_enemy_ship_field_for_go_current_user(player, shot_cpu, package)                   # возвращает обновлённый объект с полем для игрока (части для кораблей) и заменяет объект новым значением
                """необходимо начать проверку убит/не убит"""
                temp_list = []
                for i in player.field_ship:
                    temp_list = vertical_and_horizontal_neighborhood_check(i, player.field_ship, temp_list)    
                test = True if True not in temp_list else False                                                                  # проверка поля, если есть рядом '⚓' и '❌', то условие не выполняется и переменная будет False и следующую операцию выполнять нельзя         
                """обновим объект player (часть поля с кораблями), в случае уничтожения одного из кораблей вокруг этих клеток с кораблём
                появятся "⚪"."""
                if test:                                                                                                         # если рядом '⚓' и '❌', то условие не запустится                                                                                                         
                    for i in player.field_ship:
                        for_basic_case = []                                                                                      # эта переменная нужна для сбора информации, о том какие клетки уже посетили рекурсивно, и она должна быть именно здесь, а не в самой функции
                        player._field = determining_vertical_and_horizontal_neighbors(i, player.field_ship, for_basic_case)      # обновление словаря с полем для кораблей с обработкой каждой точки, проверяет убит ли корабль и ставаит "⚪" вокруг убитого корабля
                """обновим объект cpu (часть поля для ходов), в случае уничтожения одного из кораблей вокруг этих клеток с кораблём
                появятся "⚪". Перенесём "⚪" из player._field_ship в cpu._field_ship_go."""
                temp_dict = dict()
                for a, b in player.field_ship.items():
                    if b[1] == Sea_battle.miss_icon:
                        temp_dict[a] = b
                for a, b in temp_dict.items():
                    cpu._field_go[a] = b            
                """проверка победы игрока, конец игры"""
                check = set()
                for i in player.field_ship.values():
                    if Sea_battle.ship_icon in i:
                        check.add(i[1])
                if Sea_battle.ship_icon not in check:
                    win = True
                    break
                """необходимо начать проверку убит/не убит №2. для переменной response"""
                wounded_set = set()                                                                                              # множество, которое содержит "ранен" и "не ранен" или только "ранен". 
                for point in player.field_ship:
                    result = vertical_and_horizontal_neighborhood_check_2(point, player.field_ship)                              # переменная множество содержит "ранен" и "не ранен"
                    wounded_set = wounded_set | result                              
                if "ранен" in wounded_set:
                    response = "Ранен. Продолжаем стрелять."
                else:
                    response = "Начинаем заново"
                """проверка повторного хода игрока, отправляем в начало цикла"""
                if player.field_ship[shot_cpu][1] == Sea_battle.hit_icon:
                    continue
            
            elif response == "Ранен. Продолжаем стрелять.":                                                                      # условие, если предыдущий корабль ранен
                shot_cpu_neighborhood_list = vertical_and_horizontal_neighborhood_check_3(shot_cpu)                              # переменная содержит список соседей клетки, в которую произведено последнее попадание
                for a, b in cpu.field_go.items():                                                                                # в цикле выкинем из списка shot_cpu_neighborhood_list все не подходящие промахи
                    if b[1] == Sea_battle.miss_icon and a in shot_cpu_neighborhood_list:
                        shot_cpu_neighborhood_list.remove(a)
                """нужно определить ориентацию раненного корабля (вертикаль или горизонталь)"""
                init_vert_horizontal.add(shot_cpu)                                                                               # добавим первый выстрел в множество
                for a, b in cpu.field_go.items():                                                                                # в цикле добавим в множество вторую клетку с попаданием (если оно есть), которая поможет определить ориентацию корабля
                    if b[1] == Sea_battle.hit_icon and a in shot_cpu_neighborhood_list:
                        init_vert_horizontal.add(a)
                
                # если множество всё еще короткое и состоит из одного элемента, значит ориентация корабля еще не определена (он может оказаться 2-х палубным и определение ориентации в дальнейшем не понадобится)
                if len(init_vert_horizontal) == 1:
                    shot_cpu_second = random.choice(shot_cpu_neighborhood_list)                                
                    cell_status = function_check_cell(player.field_ship, shot_cpu_second)                                        # функция проверки статуса клетки для поля игрока, которое с кораблями
                    if cell_status == Sea_battle.sea_icon or cell_status == Sea_battle.sea_icon_block:                           # случай, при котором возможна модернизация основного поля игрока и поля ходов у компьютера
                        package = Sea_battle.miss_icon                                                                           # вводится переменная, которая содержит значение для иконки выстрела
                    elif cell_status == Sea_battle.ship_icon:                                                                    # случай, при котором возможна модернизация основного поля игрока и поля ходов у компьютера
                        package = Sea_battle.hit_icon                                                                            # вводится переменная, которая содержит значение для иконки выстрела          
                    cpu = fuction_mod_object_for_current_user_go(cpu, shot_cpu_second, package)                                  # возвращает обновлённый объект с полем для компьютера (части для ходов) и заменяет объект новым значением
                    player = fuction_mod_object_of_enemy_ship_field_for_go_current_user(player, shot_cpu_second, package)        # возвращает обновлённый объект с полем для игрока (части для кораблей) и заменяет объект новым значением
                    """необходимо начать проверку убит/не убит"""
                    temp_list = []
                    for i in player.field_ship:
                        temp_list = vertical_and_horizontal_neighborhood_check(i, player.field_ship, temp_list)    
                    test = True if True not in temp_list else False                                                              # проверка поля, если есть рядом '⚓' и '❌', то условие не выполняется и переменная будет False и следующую операцию выполнять нельзя         
                    """обновим объект player (часть поля с кораблями), в случае уничтожения одного из кораблей вокруг этих клеток с кораблём
                    появятся "⚪"."""
                    if test:                                                                                                     # если рядом '⚓' и '❌', то условие не запустится                                                                                                         
                        for i in player.field_ship:
                            for_basic_case = []                                                                                  # эта переменная нужна для сбора информации, о том какие клетки уже посетили рекурсивно, и она должна быть именно здесь, а не в самой функции
                            player._field = determining_vertical_and_horizontal_neighbors(i, player.field_ship, for_basic_case)  # обновление словаря с полем для кораблей с обработкой каждой точки, проверяет убит ли корабль и ставаит "⚪" вокруг убитого корабля
                    """обновим объект cpu (часть поля для ходов), в случае уничтожения одного из кораблей вокруг этих клеток с кораблём
                    появятся "⚪". Перенесём "⚪" из player._field_ship в cpu._field_ship_go."""
                    temp_dict = dict()
                    for a, b in player.field_ship.items():
                        if b[1] == Sea_battle.miss_icon:
                            temp_dict[a] = b
                    for a, b in temp_dict.items():
                        cpu._field_go[a] = b            
                    """проверка победы игрока, конец игры"""
                    check = set()
                    for i in player.field_ship.values():
                        if Sea_battle.ship_icon in i:
                            check.add(i[1])
                    if Sea_battle.ship_icon not in check:
                        win = True
                        break
                    """необходимо начать проверку убит/не убит №2. для переменной response"""
                    wounded_set = set()                                                                                              # множество, которое содержит "ранен" и "не ранен" или только "ранен". 
                    for point in player.field_ship:
                        result = vertical_and_horizontal_neighborhood_check_2(point, player.field_ship)                              # переменная множество содержит "ранен" и "не ранен"
                        wounded_set = wounded_set | result                              
                    if "ранен" in wounded_set:
                        response = "Ранен. Продолжаем стрелять."
                    else:
                        response = "Начинаем заново"
                    init_vert_horizontal = set()                                                                                     # переменная-множество понадобится для определения ориентации корабля (нужно её обнулять в конце каждого цикла, она заполнится заново)               
                    """проверка повторного хода игрока, отправляем в начало цикла"""
                    if player.field_ship[shot_cpu_second][1] == Sea_battle.hit_icon:
                        continue    
                     
                # если множество длинное и состоит из двух элементов, значит ориентацию корабля уже можно определить"""
                elif len(init_vert_horizontal) > 1:     
                    """определение ориентации корабля"""
                    if list(init_vert_horizontal)[0][0] == list(init_vert_horizontal)[1][0]:
                        orientation = "horizontal"
                    elif list(init_vert_horizontal)[0][1] == list(init_vert_horizontal)[1][1]:
                        orientation = "vertical"
                    """две ориентации и для каждой своя переменная shot_cpu_second, которая будет определяться соответствующей функцией"""
                    if orientation == "horizontal":
                        shot_cpu_second = horizontal_shot(cpu.field_go, shot_cpu)
                    else:
                        shot_cpu_second = vertical_shot(cpu.field_go, shot_cpu)
                    cell_status = function_check_cell(player.field_ship, shot_cpu_second)                                        # функция проверки статуса клетки для поля игрока, которое с кораблями
                    if cell_status == Sea_battle.sea_icon or cell_status == Sea_battle.sea_icon_block:                           # случай, при котором возможна модернизация основного поля игрока и поля ходов у компьютера
                        package = Sea_battle.miss_icon                                                                           # вводится переменная, которая содержит значение для иконки выстрела
                    elif cell_status == Sea_battle.ship_icon:                                                                    # случай, при котором возможна модернизация основного поля игрока и поля ходов у компьютера
                        package = Sea_battle.hit_icon                                                                            # вводится переменная, которая содержит значение для иконки выстрела          
                    cpu = fuction_mod_object_for_current_user_go(cpu, shot_cpu_second, package)                                  # возвращает обновлённый объект с полем для компьютера (части для ходов) и заменяет объект новым значением
                    player = fuction_mod_object_of_enemy_ship_field_for_go_current_user(player, shot_cpu_second, package)        # возвращает обновлённый объект с полем для игрока (части для кораблей) и заменяет объект новым значением
                    """необходимо начать проверку убит/не убит"""
                    temp_list = []
                    for i in player.field_ship:
                        temp_list = vertical_and_horizontal_neighborhood_check(i, player.field_ship, temp_list)    
                    test = True if True not in temp_list else False                                                              # проверка поля, если есть рядом '⚓' и '❌', то условие не выполняется и переменная будет False и следующую операцию выполнять нельзя         
                    """обновим объект player (часть поля с кораблями), в случае уничтожения одного из кораблей вокруг этих клеток с кораблём
                    появятся "⚪"."""
                    if test:                                                                                                     # если рядом '⚓' и '❌', то условие не запустится                                                                                                         
                        for i in player.field_ship:
                            for_basic_case = []                                                                                  # эта переменная нужна для сбора информации, о том какие клетки уже посетили рекурсивно, и она должна быть именно здесь, а не в самой функции
                            player._field = determining_vertical_and_horizontal_neighbors(i, player.field_ship, for_basic_case)  # обновление словаря с полем для кораблей с обработкой каждой точки, проверяет убит ли корабль и ставаит "⚪" вокруг убитого корабля
                    """обновим объект cpu (часть поля для ходов), в случае уничтожения одного из кораблей вокруг этих клеток с кораблём
                    появятся "⚪". Перенесём "⚪" из player._field_ship в cpu._field_ship_go."""
                    temp_dict = dict()
                    for a, b in player.field_ship.items():
                        if b[1] == Sea_battle.miss_icon:
                            temp_dict[a] = b
                    for a, b in temp_dict.items():
                        cpu._field_go[a] = b            
                    """проверка победы игрока, конец игры"""
                    check = set()
                    for i in player.field_ship.values():
                        if Sea_battle.ship_icon in i:
                            check.add(i[1])
                    if Sea_battle.ship_icon not in check:
                        win = True
                        break
                    """необходимо начать проверку убит/не убит №2. для переменной response"""
                    wounded_set = set()                                                                                              # множество, которое содержит "ранен" и "не ранен" или только "ранен". 
                    for point in player.field_ship:
                        result = vertical_and_horizontal_neighborhood_check_2(point, player.field_ship)                              # переменная множество содержит "ранен" и "не ранен"
                        wounded_set = wounded_set | result                              
                    if "ранен" in wounded_set:
                        response = "Ранен. Продолжаем стрелять."
                    else:
                        response = "Начинаем заново"
                    init_vert_horizontal = set()                                                                                     # переменная-множество понадобится для определения ориентации корабля (нужно её обнулять в конце каждого цикла, она заполнится заново)               
                    """проверка повторного хода игрока, отправляем в начало цикла"""
                    if player.field_ship[shot_cpu_second][1] == Sea_battle.hit_icon:
                        continue                    
            break
            
        """Конец игры. Победа компьютера!!!"""
        if win:
            function_visualization(player)
            print("Вы проиграли!!!")
            playsound.playsound("2.1.15.task_game_over.mp3")
            break                                                                                                                # прерываем основной цикл 
        

if __name__ == "__main__":    
    print()
    print("Скрипт запущен напрямую.")                                                                                            # сообщение не будет видно на экране, т.к. экран далее будет очищен с помощью модуля bext
    print()
    function_main()
else:    
    print()
    print("Скрипт импортирован.")
    print()