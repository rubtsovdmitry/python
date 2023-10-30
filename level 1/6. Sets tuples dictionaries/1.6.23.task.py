import pprint, random

# создадим шахматную доску (словарь) и список с названиями клеток
y = range(1, 9)
x = "abcdefgh"
board_dict = {}                                                                             # этот словарь пока будет содержать только ключи с пустым значением
for a in x:
    for b in y:
        board_dict[(a, b)] = ""
board_list = []                                                                             # этот список состоит из ключей словаря, который описан чуть выше
for i in board_dict:
    board_list.append(i)

# создадим два списка для черных и для белых фигур и объединим их
figures_dict = { "pawn": 8, "rook": 2, "horse": 2, "elephant": 2, "queen": 1, "king": 1 }
black_figures = []                                                      
white_figures = []
for a, b in figures_dict.items():
    count = 0
    while count < b:
        black_figures.append(("b-" + a))
        white_figures.append(("w-" + a))
        count += 1
black_and_white = black_figures + white_figures                                             # в итоге получился один общий список всех фигур белых и чёрных

# расставим фигуры хаотично на доске
while len(board_list) != 32:
    random.shuffle(board_list)                                                              # мешаем список координат клеток на поле, чтобы выбрать одно последнее значение
    random.shuffle(black_and_white)                                                         # мешаем список фигур, чтобы выбрать одно последнее значение
    board_dict[board_list[-1]] = black_and_white[-1]                                        # добавляем рандомно выбранную фигуру в рандомно выбранную клетку
    board_list.pop()                                                                        # удаляем последнее значение
    black_and_white.pop()                                                                   # удаляем последнее значение
pprint.pprint(board_dict)