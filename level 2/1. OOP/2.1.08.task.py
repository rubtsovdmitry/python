class Field:
    def __init__(self):                                                                         
        self.__field = {}                                                                               # создадим пустое игровое поле для игры (словарь, в котором ключ - это номер поля, а значение - это " ")
        for i in CELLS:                                                                         
            self.__field[i] = BLANK        

    def method_show_field(self):                                                                        # метод выводит текстовое представление игрового поля
        return f"""
        {self.__field["1"]}|{self.__field["2"]}|{self.__field["3"]} 1 2 3
        -+-+-
        {self.__field["4"]}|{self.__field["5"]}|{self.__field["6"]} 4 5 6
        -+-+-
        {self.__field["7"]}|{self.__field["8"]}|{self.__field["9"]} 7 8 9"""

    def method_test_free(self, move):                                                                   # проверка: вернёт True, если клетка есть среди ключей словаря self.__field и она пуста
        return self.__field.get(move) == BLANK                     
    
    def method_update_field(self, move, player):                                                        # заполняет словарь после очередного хода
        self.__field[move] = player   
    
    def method_win(self, player):                                                                       # проверяет победу
        result = True if (self.__field["1"] == self.__field["2"] == self.__field["3"] == player) \
            or (self.__field["4"] == self.__field["5"] == self.__field["6"] == player) \
            or (self.__field["7"] == self.__field["8"] == self.__field["9"] == player) \
            or (self.__field["1"] == self.__field["4"] == self.__field["7"] == player) \
            or (self.__field["2"] == self.__field["5"] == self.__field["8"] == player) \
            or (self.__field["3"] == self.__field["6"] == self.__field["9"] == player) \
            or (self.__field["3"] == self.__field["5"] == self.__field["7"] == player) \
            or (self.__field["1"] == self.__field["5"] == self.__field["9"] == player) else False
        return result
    
    def method_no_win(self):                                                                            # проверяет ничью
        result = True if BLANK not in self.__field.values() else False
        return result        

# основная функция
def function_main():
    print()
    print("Игра \"Креcтики-нолики\".")    
    field = Field()                                                                                     # создадим объект класса Field
    player_1, player_2 = X, O
    print(field.method_show_field())                                                                    # вывести поле на печать
    while True:        
        move = 0                                                                                        # это значение недопустимо и требует коррекции
        while not field.method_test_free(move):                                                         # цикл гарантирует, что клетка в очередном ходе существует и пуста
            print()
            move = input("Игрок 1, Ваш ход: ")
        field.method_update_field(move, player_1)                                                       # заполним поле после очередного хода
        print(field.method_show_field())                                                                # вывести поле на печать
        if field.method_win(player_1):                                                                  # проверка выиграл ли первый игрок
            print("Игрок 1 победил.")
            print()
            print("Конец игры.")
            break
        elif field.method_no_win():                                                                     # условие для проверки ничьи
            print()
            print("Ничья.")
            print()
            print("Конец игры.")
            break        
        move = 0                                                                                        # это значение недопустимо и требует коррекции
        while not field.method_test_free(move):                                                         # цикл гарантирует, что клетка в очередном ходе существует и пуста
            print()
            move = input("Игрок 2, Ваш ход: ")
        field.method_update_field(move, player_2)                                                       # заполним поле после очередного хода
        print(field.method_show_field())                                                                # вывести поле на печать
        if field.method_win(player_2):                                                                  # проверка выиграл ли первый игрок
            print()
            print("Игрок 2 победил.")
            print()
            print("Конец игры.")
            break
        elif field.method_no_win():                                                                     # условие для проверки ничьи
            print()
            print("Ничья.")
            print()
            print("Конец игры.")
            break        


CELLS = "123456789"                                                                                     # ключи для словаря с игровым полем. Ключ - это клетка поля
X, O, BLANK = "X", "O", " "                                                                             # константы для значений клеток

if __name__ == "__main__":    
    print("Скрипт запущен напрямую.")
    function_main()
else:    
    print("Скрипт импортирован.")