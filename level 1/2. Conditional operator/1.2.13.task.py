# ввод переменных
diapazon_letters = "abcdefgh"                                   # вертикали
diapazon_digits = "12345678"                                    # горизонтали
diapazon_values = {}                                            # создадим словарь, в кот. будем хранить соответствие клетки и цвета

# заполнение словаря по нечётным столбцам
count = 1                                                   
for a in diapazon_letters[::2]:
    for b in diapazon_digits:         
        color = "black" if count % 2 != 0 else "white"
        diapazon_values[a + b] = color
        count += 1

# заполнение словаря по чётным столбцам
count = 1
for a in diapazon_letters[1::2]:
    for b in diapazon_digits:         
        color = "black" if count % 2 == 0 else "white"
        diapazon_values[a + b] = color
        count += 1

# запрос координат клетки от пользователя
letter = input("%100s" % "Введите столбец (буква): ")
digit = input("%100s" % "Введите строку (цифра): ")
plus = letter + digit

# вывод результата
print("%99s" % "Координаты:", plus, "Цвет:", diapazon_values[plus])