# проверяет ничью
def function_no_win(field, blank):
    result = True if blank not in field.values() else False
    return result

# проверяет победу
def function_win(field, player):
    result = True if (field["1"] == field["2"] == field["3"] == player) \
        or (field["4"] == field["5"] == field["6"] == player) \
        or (field["7"] == field["8"] == field["9"] == player) \
        or (field["1"] == field["4"] == field["7"] == player) \
        or (field["2"] == field["5"] == field["8"] == player) \
        or (field["3"] == field["6"] == field["9"] == player) \
        or (field["3"] == field["5"] == field["7"] == player) \
        or (field["1"] == field["5"] == field["9"] == player) else False
    return result

# заполняет игровое поле после очередного хода
def function_mod_field(field, move, player):
    field[move] = player
    return field

# проверка: вернёт True, если клетка есть среди ключей словаря field и она пуста
def function_test_free(field, move):
    return field.get(move) == BLANK                     

# выведем текстовое представление игрового поля
def function_show_field(field):
    return f"""
    {field["1"]}|{field["2"]}|{field["3"]} 1 2 3
    -+-+-
    {field["4"]}|{field["5"]}|{field["6"]} 4 5 6
    -+-+-
    {field["7"]}|{field["8"]}|{field["9"]} 7 8 9"""

# создадим пустое игровое поле для игры
def function_game_field():    
    field = dict()    
    for i in CELLS:
        field[i] = BLANK
    return field

# основная функция
def function_main():
    print()
    print("Игра \"Креcтики-нолики\".")    
    field = function_game_field()                                                          # создадим пустое игровое поле
    player_1, player_2 = X, O    
    print(function_show_field(field))                                                      # выводим игровое поле на экран
    while True:        
        ############################### первый игрок
        move = 0                                                                           # это значение недопустимо и требует коррекции
        while not function_test_free(field, move):                                         # цикл гарантирует, что клетка в очередном ходе существует и пуста
            print()
            move = input("Игрок 1, Ваш ход: ")
        function_mod_field(field, move, player_1)                                          # отправим поле в функцию на модификацию
        print(function_show_field(field))                                                  # выводим игровое поле на экран        
        if function_win(field, player_1):                                                  # условие для проверки победы
            print()
            print("Игрок 1 победил.")
            print()
            print("Конец игры.")
            break
        elif function_no_win(field, BLANK):                                                # условие для проверки ничьи
            print()
            print("Ничья.")
            print()
            print("Конец игры.")
            break
        ############################### второй игрок    
        move = 0                                                                           # это значение недопустимо и требует коррекции
        while not function_test_free(field, move):                                         # цикл гарантирует, что клетка в очередном ходе существует и пуста
            print()
            move = input("Игрок 2, Ваш ход: ")
        function_mod_field(field, move, player_2)                                          # отправим поле в функцию на модификацию
        print(function_show_field(field))                                                  # выводим игровое поле на экран        
        if function_win(field, player_2):                                                  # условие для проверки победы
            print()
            print("Игрок 2 победил.")
            print()
            print("Конец игры.")
            break
        elif function_no_win(field, BLANK):                                                # условие для проверки ничьи
            print()
            print("Ничья.")
            print()
            print("Конец игры.")
            break
    

CELLS = "123456789"                                                                        # ключи для словаря с игровым полем. Ключ - это клетка поля
X, O, BLANK = "X", "O", " "                                                                # константы для значений клеток

if __name__ == "__main__":    
    print("Скрипт запущен напрямую.")
    function_main()
else:    
    print("Скрипт импортирован.")