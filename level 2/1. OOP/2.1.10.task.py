# создание класса 
class Field:
    def __init__(self, BLANK, CELLS):                                                                                                       # входящие аргументы для класса - пустой знак " ", количество клеток                     
        self._blank = BLANK
        self._cells = CELLS
        self._field = dict.fromkeys([str(i) for i in range(1, self._cells ** 2 + 1)], self._blank)                                          # создадим пустое игровое поле

    def method_show_field(self):                                                                                                            # метод выводит текстовое представление игрового поля                        
        temp, temp_2 = 1, (self._cells + 1)
        for a in range(1, self._cells + 1):            
            for b in range(temp, temp_2):
                print(f"|{self._field[str(b)]}", end="")
            print("|     ", end="")
            for b in range(temp, temp_2):
                print(f"|{b:<3}", end="")
            print("|")
            temp += self._cells; temp_2 += self._cells
        return "Игровое поле"

    def method_test_free(self, move):                                                                                                       # проверка: вернёт True, если клетка есть среди ключей словаря self.__field и она пуста
        return self._field.get(move) == self._blank                     

    def method_update_field(self, move, player):                                                                                            # заполняет словарь после очередного хода
        self._field[move] = player

    def method_win(self, player, move, WIN):                                                                                                # проверяет победу
        move = int(move)        
        result = False
        # проверка на выигрыш по горизонтали        
        if result == False:
            if move % self._cells != 0:
                left_limit = move - move % self._cells + 1                                                                                  # левая граница поля
                right_limit = self._cells + left_limit - 1                                                                                  # правая граница поля
            else:
                left_limit = move - self._cells + 1                                                                                         # левая граница поля
                right_limit = move                                                                                                          # правая граница поля        
            set_gorizont_1 = set(range(left_limit, right_limit + 1))                                                                        # составим множество клеток в реальных границах поля
            set_gorizont_2 = set(range((move - WIN + 1), (move + WIN)))                                                                     # составим множество клеток + и - выигрышное количетсво клеток от настоящей клетки
            list_gorizont = sorted(set_gorizont_1 & set_gorizont_2)                                                                         # найдём клетки в горизонтальной плоскости, которое необходимо проверить
            count = 0                                                                                                                                   
            for i in list_gorizont:            
                count = (count + 1) if self._field[str(i)] == player else 0                
                result = True if count == WIN else False                
                if result == True:
                    break              
        # проверка на выигрыш по вертикали
        if result == False:
            set_vertikal = set()                                                                                                                
            set_vertikal.add(move)                                                                                                          
            temp = move
            for i in range(WIN - 1):
                temp -= self._cells
                set_vertikal.add(temp)
            temp = move
            for i in range(WIN - 1):
                temp += self._cells
                set_vertikal.add(temp)            
            set_total_cells = set(range(1, self._cells ** 2 + 1))
            list_vertikal = sorted(set_vertikal & set_total_cells)            
            count = 0                                                                                                                                   
            for i in list_vertikal:            
                count = (count + 1) if self._field[str(i)] == player else 0
                result = True if count == WIN else False                
                if result == True:
                    break          
        # проверка на выигрыш по диагонали №1
        if result == False:
            set_diagonal = set()                                                                                                                
            set_diagonal.add(move)                   
            temp = move
            for i in range(WIN - 1):
                temp -= (self._cells + 1)
                set_diagonal.add(temp)                
            temp = move
            for i in range(WIN - 1):
                temp += (self._cells + 1)
                set_diagonal.add(temp)                            
            set_total_cells = set(range(1, self._cells ** 2 + 1))
            list_diagonal = sorted(set_diagonal & set_total_cells)                        
            count = 0                                                                                                                                   
            for i in list_diagonal:            
                count = (count + 1) if self._field[str(i)] == player else 0
                result = True if count == WIN else False                
                if result == True:
                    break         
        # проверка на выигрыш по диагонали №2
        if result == False:
            set_diagonal = set()                                                                                                                
            set_diagonal.add(move)                   
            temp = move
            for i in range(WIN - 1):
                temp -= (self._cells - 1)
                set_diagonal.add(temp)                
            temp = move
            for i in range(WIN - 1):
                temp += (self._cells - 1)
                set_diagonal.add(temp)                            
            set_total_cells = set(range(1, self._cells ** 2 + 1))
            list_diagonal = sorted(set_diagonal & set_total_cells)                        
            count = 0                                                                                                                                   
            for i in list_diagonal:            
                count = (count + 1) if self._field[str(i)] == player else 0
                result = True if count == WIN else False                
                if result == True:
                    break            
        return result
    
    def method_no_win(self):                                                                                                                # проверяет ничью
        result = True if self._blank not in self._field.values() else False
        return result        
        
# основная функция
def function_main_2(X, O, BLANK, CELLS, WIN):
    field = Field(BLANK, CELLS)                                                                                                             # создадим объект "поле" класса Field
    print(field.method_show_field())                                                                                                        # вывести поле на печать
    player_1, player_2 = X, O
    while True:        
        move = 0                                                                                                                            # это значение недопустимо и требует коррекции
        while not field.method_test_free(move):                                                                                             # цикл гарантирует, что клетка в очередном ходе существует и пуста
            print()
            move = input("Игрок 1, Ваш ход: ")
        field.method_update_field(move, player_1)                                                                                           # заполним поле после очередного хода
        print(field.method_show_field())                                                                                                    # вывести поле на печать        
        if field.method_win(player_1, move, WIN):                                                                                           # проверка выиграл ли первый игрок
            print()
            print("Игрок 1 победил.")
            print()
            print("Конец игры.")
            break        
        elif field.method_no_win():                                                                                                         # условие для проверки ничьи
            print()
            print("Ничья.")
            print()
            print("Конец игры.")
            break        
        move = 0                                                                                                                            # это значение недопустимо и требует коррекции
        while not field.method_test_free(move):                                                                                             # цикл гарантирует, что клетка в очередном ходе существует и пуста
            print()
            move = input("Игрок 2, Ваш ход: ")
        field.method_update_field(move, player_2)                                                                                           # заполним поле после очередного хода
        print(field.method_show_field())                                                                                                    # вывести поле на печать
        if field.method_win(player_2, move, WIN):                                                                                           # проверка выиграл ли первый игрок
            print()
            print("Игрок 2 победил.")
            print()
            print("Конец игры.")
            break
        elif field.method_no_win():                                                                                                         # условие для проверки ничьи
            print()
            print("Ничья.")
            print()
            print("Конец игры.")
            break        

# создание входных данных
def function_main():
    print()
    print("Игра \"Креcтики-нолики\".")    
    X, O, BLANK, CELLS, WIN = "X", "O", " ", 20, 5
    function_main_2(X, O, BLANK, CELLS, WIN)


if __name__ == "__main__":    
    print("Скрипт запущен напрямую.")
    function_main()
else:    
    print("Скрипт импортирован.")