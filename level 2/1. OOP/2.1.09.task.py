# создание супер-класса
class Field:
    def __init__(self, BLANK, answer):                                                                                                      # входящие аргументы для класса - пустой знак " ", количество клеток                     
        self._blank = BLANK
        self._answer = answer
        self._field = dict.fromkeys([str(i) for i in range(1,10)] if self._answer == 9 else [str(i) for i in range(1,17)], self._blank)     # создадим пустое игровое поле

    def method_show_field(self):                                                                                                            # метод выводит текстовое представление игрового поля        
        return f"""
        {self._field["1"]}|{self._field["2"]}|{self._field["3"]} 1 2 3
        -+-+-
        {self._field["4"]}|{self._field["5"]}|{self._field["6"]} 4 5 6
        -+-+-
        {self._field["7"]}|{self._field["8"]}|{self._field["9"]} 7 8 9"""

    def method_test_free(self, move):                                                                                                       # проверка: вернёт True, если клетка есть среди ключей словаря self.__field и она пуста
        return self._field.get(move) == self._blank                     

    def method_update_field(self, move, player):                                                                                            # заполняет словарь после очередного хода
        self._field[move] = player

    def method_win(self, player):                                                                                                           # проверяет победу
        result = True if (self._field["1"] == self._field["2"] == self._field["3"] == player) \
            or (self._field["4"] == self._field["5"] == self._field["6"] == player) \
            or (self._field["7"] == self._field["8"] == self._field["9"] == player) \
            or (self._field["1"] == self._field["4"] == self._field["7"] == player) \
            or (self._field["2"] == self._field["5"] == self._field["8"] == player) \
            or (self._field["3"] == self._field["6"] == self._field["9"] == player) \
            or (self._field["3"] == self._field["5"] == self._field["7"] == player) \
            or (self._field["1"] == self._field["5"] == self._field["9"] == player) else False
        return result
    
    def method_no_win(self):                                                                                                                # проверяет ничью
        result = True if self._blank not in self._field.values() else False
        return result        

# класс-наследник
class Big_field(Field):
    def __init__(self, BLANK, answer):
        super().__init__(BLANK, answer)
    
    def method_show_field(self):                                                                                                            # метод выводит текстовое представление игрового поля        
        return f"""
        {self._field["1"]}|{self._field["2"]}|{self._field["3"]}|{self._field["4"]}     1  2  3  4
        -+-+-+-
        {self._field["5"]}|{self._field["6"]}|{self._field["7"]}|{self._field["8"]}     5  6  7  8
        -+-+-+-
        {self._field["9"]}|{self._field["10"]}|{self._field["11"]}|{self._field["12"]}     9 10 11 12
        -+-+-+-
        {self._field["13"]}|{self._field["14"]}|{self._field["15"]}|{self._field["16"]}    13 14 15 16"""
    
    def method_win(self, player):                                                                                                           # проверяет победу
        result = True if (self._field["1"] == self._field["2"] == self._field["3"] == self._field["4"] == player) \
            or (self._field["5"] == self._field["6"] == self._field["7"] == self._field["8"] == player) \
            or (self._field["9"] == self._field["10"] == self._field["11"] == self._field["12"] == player) \
            or (self._field["13"] == self._field["14"] == self._field["15"] == self._field["16"] == player) \
            or (self._field["1"] == self._field["5"] == self._field["9"] == self._field["13"] == player) \
            or (self._field["2"] == self._field["6"] == self._field["10"] == self._field["14"] == player) \
            or (self._field["3"] == self._field["7"] == self._field["11"] == self._field["15"] == player) \
            or (self._field["4"] == self._field["8"] == self._field["12"] == self._field["16"] == player) \
            or (self._field["1"] == self._field["6"] == self._field["11"] == self._field["16"] == player) \
            or (self._field["4"] == self._field["7"] == self._field["10"] == self._field["13"] == player) else False
        return result
        
# основная функция
def function_main_2(X, O, BLANK, answer):
    if answer == 9:
        field = Field(BLANK, answer)                                                                                                         # создадим объект класса Field
    else:
        field = Big_field(BLANK, answer)                                                                                                     # создадим объект класса Big_field (наследник Field)
    print(field.method_show_field())                                                                                                         # вывести поле на печать
    player_1, player_2 = X, O
    while True:        
        move = 0                                                                                                                             # это значение недопустимо и требует коррекции
        while not field.method_test_free(move):                                                                                              # цикл гарантирует, что клетка в очередном ходе существует и пуста
            print()
            move = input("Игрок 1, Ваш ход: ")
        field.method_update_field(move, player_1)                                                                                            # заполним поле после очередного хода
        print(field.method_show_field())                                                                                                     # вывести поле на печать
        if field.method_win(player_1):                                                                                                       # проверка выиграл ли первый игрок
            print("Игрок 1 победил.")
            print()
            print("Конец игры.")
            break
        elif field.method_no_win():                                                                                                          # условие для проверки ничьи
            print()
            print("Ничья.")
            print()
            print("Конец игры.")
            break        
        move = 0                                                                                                                             # это значение недопустимо и требует коррекции
        while not field.method_test_free(move):                                                                                              # цикл гарантирует, что клетка в очередном ходе существует и пуста
            print()
            move = input("Игрок 2, Ваш ход: ")
        field.method_update_field(move, player_2)                                                                                            # заполним поле после очередного хода
        print(field.method_show_field())                                                                                                     # вывести поле на печать
        if field.method_win(player_2):                                                                                                       # проверка выиграл ли первый игрок
            print()
            print("Игрок 2 победил.")
            print()
            print("Конец игры.")
            break
        elif field.method_no_win():                                                                                                          # условие для проверки ничьи
            print()
            print("Ничья.")
            print()
            print("Конец игры.")
            break        

# проверка ввода и создание входных данных
def function_main():
    print()
    print("Игра \"Креcтики-нолики\".")    
    X, O, BLANK = "X", "O", " "
    while True:
        try:
            print()
            answer = int(input("Введите на каком поле хотите играть 9 или 16: "))
            if answer == 9 or answer == 16:
                break
            else:
                print()
                print("Вы ввели не тот размер поля.")
        except:
            print()
            print("Повторите ввод. Вы ввели недопустимые символы. ") 
    function_main_2(X, O, BLANK, answer)


if __name__ == "__main__":    
    print("Скрипт запущен напрямую.")
    function_main()
else:    
    print("Скрипт импортирован.")