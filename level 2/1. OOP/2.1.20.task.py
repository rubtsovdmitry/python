import random, time, bext, sys


"""КЛАСС ТАБЛИЦА УМНОЖЕНИЯ"""
class Multiplication:
    test_pass, test_no = 0, 0  # правильные и неправильные ответы
    count = 0  # счётчик объектов
    wrong_answeres = []  # неправильные ответы
    time_limit = 15
    # конструктор
    def __init__(self, multiplicator):
        self._digit = random.randint(1, multiplicator)  # первый множитель
        self._digit2 = random.randint(1, multiplicator)  # второй множитель
        self._composition = self._digit * self._digit2  # произведение
        Multiplication.count += 1  # при создании объекта увеличивает на 1 счётчик объектов (атрибут класса)

    # метод, задающий вопрос
    def question(self):
        print(f"\nУ вас 15 секунд для ответа !!!\n\nПриготовьтесь !!! {Multiplication.count}-й вопрос.\n")
        # обратный отсчёт
        print("3 сек...")
        time.sleep(1)
        print("2 сек...")
        time.sleep(1)
        print("1 сек...")
        time.sleep(1)
        print(f"\nВопрос: произведение {self._digit} на {self._digit2} ???\n")

    # метод, получающий ответ
    def answer(self):
        time_count_start = time.time()  # старт счётчика времени
        test = input("Ваш ответ: \n")
        time_count_end = time.time()  # конец счётчика времени
        time_count = time_count_end - time_count_start  # затраченное время на ответ
        if test == str(self._composition) and time_count <= Multiplication.time_limit:
            Multiplication.test_pass += 1
        else:
            Multiplication.test_no += 1
            Multiplication.wrong_answeres.append(f"{self._digit} * {self._digit2}")

    # метод класса, визуализация списка неправильных ответов
    @classmethod
    def class_method(cls):
        print()
        print("ИТОГО:")
        print(f"Количество вопросов: {Multiplication.count}.")
        print(f"Количество правильных ответов: {Multiplication.count - len(Multiplication.wrong_answeres)}.")
        print(f"Количество неправильных ответов: {len(Multiplication.wrong_answeres)}.")
        if len(Multiplication.wrong_answeres) > 0:
            print("По следующим вопросам были даны неправильные ответы:")
            for i in cls.wrong_answeres:
                print(i)
        print()


# функция для ВВОДА ДАННЫХ
def main():
    while True:
        try:
            mult = int(input("Введите мультипликатор от 2 до 9: \n"))
            if mult < 2 or mult > 9:
                print()
                continue
            break
        except:
            print("\nВы ввели не мультипликатор!!!\n")
    return mult
    

try:
    # КОД ПРОГРАММЫ
    bext.clear()
    bext.fg("magenta")
    quantity_tests = 20  # количество вопросов
    print(f"\nТЕСТ. \nТАБЛИЦА УМНОЖЕНИЯ.\nВсего {quantity_tests} вопросов.")
    mult = main()  # ввод мультипликатора
    # ОВНОВНОЙ ЦИКЛ
    while Multiplication.count < quantity_tests:
        a = Multiplication(mult)
        a.question()
        a.answer()
    # ИТОГИ ТЕСТА (ВЫВОД)
    Multiplication.class_method()

except KeyboardInterrupt:
    sys.exit()