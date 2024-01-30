import bext, sys


class Bucket:
    BUCKET_tuple = (8, 5, 3)
    CHECK_PASS = 4
    EMPTY = "      "
    WATER = "🟦🟦🟦"
    count_move = 0

    """конструктор"""
    def __init__(self) -> None:
        self.__bucket8 = self.__initialize_bucket8()                                                                # создадим пустое ведро первое в условии (8 литров) ['      ', '      ', '      ', '      ', '      ', '      ', '      ', '      ']
        self.__bucket5 = self.__initialize_bucket5()                                                                # создадим пустое ведро первое в условии (5 литров) ['      ', '      ', '      ', '      ', '      ']
        self.__bucket3 = self.__initialize_bucket3()                                                                # создадим пустое ведро первое в условии (3 литра) ['      ', '      ', '      ']
        
    """addon для конструктора"""
    def __initialize_bucket8(self):
        temp = []
        for i in range(__class__.BUCKET_tuple[0]):
            temp.append(__class__.EMPTY)
        return temp
    
    """addon2 для конструктора"""
    def __initialize_bucket5(self):
        temp = []
        for i in range(__class__.BUCKET_tuple[1]):
            temp.append(__class__.EMPTY)
        return temp
    
    """addon3 для конструктора"""
    def __initialize_bucket3(self):
        temp = []
        for i in range(__class__.BUCKET_tuple[2]):
            temp.append(__class__.EMPTY)
        return temp
    
    """создадим getter для атрибутов объектов класса (первое ведро)"""
    def get_1_bucket(self):
        return self.__bucket8
    """создадим setter для атрибутов объектов класса"""
    def set_1_bucket(self, value):
        self.__bucket8 = value
    my_object_1_bucket = property(get_1_bucket, set_1_bucket)

    """создадим getter для атрибутов объектов класса (второе ведро)"""
    def get_2_bucket(self):
        return self.__bucket5
    """создадим setter для атрибутов объектов класса"""
    def set_2_bucket(self, value):
        self.__bucket5 = value
    my_object_2_bucket = property(get_2_bucket, set_2_bucket)

    """создадим getter для атрибутов объектов класса (третье ведро)"""
    def get_3_bucket(self):
        return self.__bucket3
    """создадим setter для атрибутов объектов класса"""
    def set_3_bucket(self, value):
        self.__bucket3 = value
    my_object_3_bucket = property(get_3_bucket, set_3_bucket)

    """метод для визуализации объекта"""
    def visualization(self):            
        temp = self.__bucket8 + self.__bucket5 + self.__bucket3
        bext.clear()
        print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8л         5л         3л
'''.format(*temp))  

    """метод для наполнения ведра водой полностью"""
    def fill_the_bucket(self, liters):
        if liters == 8:
            self.__bucket8 = []
            for i in range(__class__.BUCKET_tuple[0]):
                self.__bucket8.append(__class__.WATER)
        elif liters == 5:
            self.__bucket5 = []
            for i in range(__class__.BUCKET_tuple[1]):
                self.__bucket5.append(__class__.WATER)
        elif liters == 3:
            self.__bucket3 = []
            for i in range(__class__.BUCKET_tuple[2]):
                self.__bucket3.append(__class__.WATER)       

    """метод для опустошения ведра"""
    def empty_the_bucket(self, liters):
        if liters == 8:
            self.__bucket8 = []
            for i in range(__class__.BUCKET_tuple[0]):
                self.__bucket8.append(__class__.EMPTY)
        elif liters == 5:
            self.__bucket5 = []
            for i in range(__class__.BUCKET_tuple[1]):
                self.__bucket5.append(__class__.EMPTY)
        elif liters == 3:
            self.__bucket3 = []
            for i in range(__class__.BUCKET_tuple[2]):
                self.__bucket3.append(__class__.EMPTY)       

    """метод, который проверяет названия вёдер при периливании"""
    def check_name_overflow_water(self, first, second):
        if first in __class__.BUCKET_tuple and second in __class__.BUCKET_tuple:
            return True
        else:
            return False

    """метод для перелива воды из ведра в ведро, который отнимает воду из ведра источника.  
    метод возвращает количество воды, которое доливаем во второе ведро"""
    def out_overflow_water(self, first, second):
        if first == __class__.BUCKET_tuple[0]:
            first = self.__bucket8
        elif first == __class__.BUCKET_tuple[1]:
            first = self.__bucket5
        else:
            first = self.__bucket3 
        if second == __class__.BUCKET_tuple[0]:
            second = self.__bucket8
        elif second == __class__.BUCKET_tuple[1]:
            second = self.__bucket5
        else:
            second = self.__bucket3
                
        liters_in_first = first.count(__class__.WATER)                                                              # int. Литров в ведре источнике
        empty_space_in_second = second.count(__class__.EMPTY)                                                       # int. Пустое место в целевом ведре
        transferable_liters = min(liters_in_first, empty_space_in_second)                                           # int. Кол-во воды, которое перельётся в итоге
        
        """уменьшим воду в источнике, т.е. в первом ведре"""
        temp = transferable_liters                                                                                  # временный каунтер
        first = first[::-1]                                                                                         # перевернём список с водой, чтобы правильно отливать воду из ведра
        for index, i in enumerate(first):
            if temp == 0:
                break
            if i == __class__.WATER:
                first[index] = __class__.EMPTY
                temp -= 1
        first = first[::-1]                                                                                         # перевернём список с водой обратно, в итоге у нас этот список и список самого объекта имеют одинаковый адрес в памяти и везде меняются одинаково
        if len(self.my_object_1_bucket) == len(first):
            self.my_object_1_bucket = first
        elif len(self.my_object_2_bucket) == len(first):
            self.my_object_2_bucket = first
        elif len(self.my_object_3_bucket) == len(first):
            self.my_object_3_bucket = first
        return transferable_liters                                                                                  # int
    
    """метод, который добавляет воду во второе ведро"""
    def in_overflow_water(self, second, liters):
        if second == __class__.BUCKET_tuple[0]:
            second = self.__bucket8
        elif second == __class__.BUCKET_tuple[1]:
            second = self.__bucket5
        else:
            second = self.__bucket3

        """увеличем воду в целевом ведре"""
        for index, i in enumerate(second):
            if liters == 0:
                break
            if i == __class__.EMPTY:
                second[index] = __class__.WATER
                liters -= 1
        if len(self.my_object_1_bucket) == len(second):
            self.my_object_1_bucket = second
        elif len(self.my_object_2_bucket) == len(second):
            self.my_object_2_bucket = second
        elif len(self.my_object_3_bucket) == len(second):
            self.my_object_3_bucket = second

    """метод, который проверяет закончена ли игра"""
    def finish(self):
        if self.my_object_1_bucket.count(__class__.WATER) == __class__.CHECK_PASS:
            print("Победа!!!")
            sys.exit()
        elif self.my_object_2_bucket.count(__class__.WATER) == __class__.CHECK_PASS:
            print("Победа!!!")
            sys.exit()
        elif self.my_object_3_bucket.count(__class__.WATER) == __class__.CHECK_PASS:
            print("Победа!!!")
            sys.exit()


def main():
    text = "ГОЛОВОЛОМКА С ВЁДРАМИ." 
    bext.clear()
    bext.fg("magenta")
    WIDTH, HEIGHT = bext.size()
    bext.goto((int(WIDTH / 2) - int(len(text) / 2)), int(HEIGHT / 3))
    print(text)

    text = "Дано три ведра: 8л, 5л и 3л. Нужно набрать 4л воды в любом из вёдер."
    WIDTH, HEIGHT = bext.size()
    bext.goto((int(WIDTH / 2) - int(len(text) / 2)), (int(HEIGHT / 3) + 3))
    print(text)

    text = "Нажмите <Enter> для начала. "
    WIDTH, HEIGHT = bext.size()
    bext.goto((int(WIDTH / 2) - int(len(text) / 2 - 1)), (int(HEIGHT / 3) + 6))
    input(f"{text} >")
    
    game = Bucket()
    
    """ОСНОВНОЙ ЦИКЛ ИГРЫ"""
    while True:        
        print()
        game.visualization()
        print('Какие можно совершить действия:')
        print('(Н)аполнить ведро')
        print('(В)ылить ведро')
        print('(П)ерелейте одно ведро в другое')
        print('(З)авершить программу')
        
        # выбор действия
        while True:
            print()  
            move = input('Введите первую букву > ').upper()
            if move == 'З':
                print()
                print('Спасибо за игру!')
                sys.exit()
            if move in ('Н', 'В', 'П'):
                break
            print()
            print('Вы ввели неправильно. Введите: "Н", "В", "П" или "З"')

        # наполнить ведро
        if move == "Н":
            while True:  
                print()
                print('Выбрать ведро: 8, 5, 3.')
                bucket_1 = input('> ').upper()
                if bucket_1 in [str(i) for i in Bucket.BUCKET_tuple]:
                    break
                else:
                    print("Вы ввели что-то не так.")
            game.fill_the_bucket(int(bucket_1))

        
        # вылить ведро
        elif move == "В":
            while True:  
                print()
                print('Выбрать ведро: 8, 5, 3.')
                bucket_1 = input('> ').upper()
                if bucket_1 in [str(i) for i in Bucket.BUCKET_tuple]:
                    break
                else:
                    print("Вы ввели что-то не так.")
            game.empty_the_bucket(int(bucket_1))

        # перелить ведро в другое
        elif move == "П":
            while True:  
                print()
                print('Выбрать ведро, из которого переливаем воду: 8, 5, 3.')
                bucket_1 = input('> ').upper()
                print('Выбрать ведро, в которое переливаем воду: 8, 5, 3.')
                bucket_2 = input('> ').upper()
                if bucket_1 in [str(i) for i in Bucket.BUCKET_tuple] and bucket_2 in [str(i) for i in Bucket.BUCKET_tuple]:
                    break
                else:
                    print("Вы ввели что-то не так.")
            amount_liters = game.out_overflow_water(int(bucket_1), int(bucket_2))
            game.in_overflow_water(int(bucket_2), amount_liters)
            game.visualization()

        # проверить победу
        game.finish()
            

if __name__ == '__main__':
    main()