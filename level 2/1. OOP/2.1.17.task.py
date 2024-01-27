import copy, random, sys


class SudokuGrid:
    """конструктор объекта"""
    def __init__(self, originalSetup):                                                                          # в качестве парметра передаётся переменнная originalSetup, которая является готовой годной строкой для игры sudoku (строка состоит из 81 символа)
        self.originalSetup = originalSetup
        self.grid = {}                                                                                          # сетка-поле для игры - это словарь с ключами (x, y) и значениями числа (в виде строки)
        self.resetGrid()                                                                                        # Установите состояние сетки на исходное значение.
        self.moves = []                                                                                         # Отслеживает каждое движение для функции отмены.

    """Вспомогательный метод для конструктора.
    Восстановление состояние поля в self.grid до первоначального заполнения."""
    def resetGrid(self):
        for x in range(1, GRID_LENGTH + 1):                                                                     # двухэтажным циклом заполним сетку-поля ключами, но пока с пустыми значениями
            for y in range(1, GRID_LENGTH + 1):
                self.grid[(x, y)] = EMPTY_SPACE
        assert len(self.originalSetup) == FULL_GRID_SIZE                                                        # производим проверку, на допустимость входных данных
        i = 0                                                                                                   # i может быть от 0 до 80 (индексы для строк с шаблонами судоку)
        y = 0                                                                                                   # y может быть от 0 до 8 (строки поля)
        while i < FULL_GRID_SIZE:                               
            for x in range(GRID_LENGTH):
                self.grid[(x, y)] = self.originalSetup[i]                                                       # заполним сетку-поле значениями и точками (для закрытых квадратов) из файла
                i += 1
            y += 1

    """метод для отображения поля"""
    def display(self):        
        print('   A B C   D E F   G H I')
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                if x == 0:                    
                    print(str(y + 1) + '  ', end='')
                print(self.grid[(x, y)] + ' ', end='')
                if x == 2 or x == 5:                    
                    print('| ', end='')
            print()
            if y == 2 or y == 5:
                print('   ------+-------+------')

    """Возвращает значение True, если numbers содержит цифры от 1 до 9"""
    def _isCompleteSetOfNumbers(self, numbers):
        return sorted(numbers) == list('123456789')

    """Возвращает значение True, если текущая сетка-поле находится в решенном состоянии."""
    def isSolved(self):        
        """проверяем каждую из строк"""
        for row in range(GRID_LENGTH):
            rowNumbers = []
            for x in range(GRID_LENGTH):
                number = self.grid[(x, row)]
                rowNumbers.append(number)
            if not self._isCompleteSetOfNumbers(rowNumbers):
                return False

        """проверяем каждую колонку"""
        for column in range(GRID_LENGTH):
            columnNumbers = []
            for y in range(GRID_LENGTH):
                number = self.grid[(column, y)]
                columnNumbers.append(number)
            if not self._isCompleteSetOfNumbers(columnNumbers):
                return False

        """проверяем каждый квадрат 3х3"""
        for boxx in (0, 3, 6):
            for boxy in (0, 3, 6):
                boxNumbers = []
                for x in range(BOX_LENGTH):
                    for y in range(BOX_LENGTH):
                        number = self.grid[(boxx + x, boxy + y)]
                        boxNumbers.append(number)
                if not self._isCompleteSetOfNumbers(boxNumbers):
                    return False
        return True

    """Установить значение сетки-поля на предыдущее."""
    def undo(self):
        if self.moves == []:
            return None
        self.moves.pop()                                                                                        # удалим последнее состояние
        if self.moves == []:                                                                                    # если после удаления последнего состояния self.moves == [], сбрасываем self.grid в первоначальное состояние
            self.resetGrid()
        else:
            self.grid = copy.copy(self.moves[-1])                                                               # идёт присваивание для self.grid его предыдущего состояния, которое хранится в self.moves

    """модернизировать значение сетки-поля, сделать очередной ход"""
    def makeMove(self, column, row, number):
        x = 'ABCDEFGHI'.find(column)                                                                            # переведём column в индекс
        y = int(row) - 1

        if self.originalSetup[y * GRID_LENGTH + x] != EMPTY_SPACE:                                              # проверим, выполняется ли ход по "заданному" номеру
            return False

        self.grid[(x, y)] = number                                                                              # заполним поле
        self.moves.append(copy.copy(self.grid))                                                                 # нужно сохранить отдельную копию объекта сетки-поля
        return True


print('''Судоку:

    5 3 . | . 7 . | . . .     5 3 4 | 6 7 8 | 9 1 2
    6 . . | 1 9 5 | . . .     6 7 2 | 1 9 5 | 3 4 8
    . 9 8 | . . . | . 6 .     1 9 8 | 3 4 2 | 5 6 7
    ------+-------+------     ------+-------+------
    8 . . | . 6 . | . . 3     8 5 9 | 7 6 1 | 4 2 3
    4 . . | 8 . 3 | . . 1 --> 4 2 6 | 8 5 3 | 7 9 1
    7 . . | . 2 . | . . 6     7 1 3 | 9 2 4 | 8 5 6
    ------+-------+------     ------+-------+------
    . 6 . | . . . | 2 8 .     9 6 1 | 5 3 7 | 2 8 4
    . . . | 4 1 9 | . . 5     2 8 7 | 4 1 9 | 6 3 5
    . . . | . 8 . | . 7 9     3 4 5 | 2 8 6 | 1 7 9
''')
input('Нажмите Enter для начала...')

# Константы
EMPTY_SPACE = '.'
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH

"""загрузить шаблоны раскладки игры из sudokupuzzles.txt"""
with open('sudokupuzzles.txt') as puzzleFile:
    puzzles = puzzleFile.readlines()                                                                            # в переменной находится список с элементами-строками

"""удалим знак переноса строки в каждом элементе списка"""
for i, puzzle in enumerate(puzzles):
    puzzles[i] = puzzle.strip()

"""создадим объект-поле"""
grid = SudokuGrid(random.choice(puzzles))                                                                       

try:
    """основной цикл игры"""
    while True:  
        """отобразим сетку-поле"""
        grid.display()

        """проверим окончание игры"""
        if grid.isSolved():
            print('Поздравления!!!')
            sys.exit()

        # Ход игрока
        while True:                                                                                                 # цикл пока не будет введено валидное значение
            print()   
            print('Сделайте выбор, введите: RESET, NEW, UNDO, ORIGINAL, or QUIT:')
            print('Для примера: "B4 9".')
            action = input('> ').upper().strip()

            if len(action) > 0 and action[0] in ('R', 'N', 'U', 'O', 'Q') and \
                ("RESET" in action or \
                "NEW" in action or \
                "UNDO" in action or \
                "ORIGINAL" in action or \
                "QUIT" in action):                                                                                  # валидное значение
                break

            if len(action.split()) == 2:
                space, number = action.split()                                                                      # с помощью метода split разделим ответ на две элемента, где разделитель - это пробел
                if len(space) != 2:
                    continue
                if not number.isdecimal():
                    input("Для клетки введено не подходящее значение. Нажмите Enter для продолжения.")
                    continue
                column, row = space                                                                                 # так как в переменной space хранится строка из 2-х элементов, то её можно разобрать на два элемента
                if column not in list('ABCDEFGHI'):
                    print(f'Такой колонки нет: {column}.')
                    continue
                if not row.isdecimal() or not (1 <= int(row) <= 9):
                    print(f'Такого ряда нет: {row}.')
                    continue
                if not (1 <= int(number) <= 9):
                    print(f'Значение для клетки {number} не подходит.')
                    continue
                break
        print() 

        if action.startswith('RESET'):
            grid.resetGrid()
            continue

        if action.startswith('NEW'):        
            grid = SudokuGrid(random.choice(puzzles))
            continue

        if action.startswith('UNDO'):
            grid.undo()
            continue

        if action.startswith('ORIGINAL'):                                                                           # просмотр исходных чисел в поле
            originalGrid = SudokuGrid(grid.originalSetup)
            print('Стартовое поле выглядит:')
            originalGrid.display()
            input('Нажмите Enter для продолжения...')
            continue

        if action.startswith('QUIT'):
            print('ИГРА ОКОНЧЕНА!')
            sys.exit()

        """ход игрока"""
        if grid.makeMove(column, row, number) == False:
            print('Вы не можете перезаписать исходные номера поля.')
            print('Введите ORIGINAL, чтобы просмотреть исходную сетку.')
            input('Нажмите Enter для продолжения...')
except KeyboardInterrupt:
    sys.exit() 