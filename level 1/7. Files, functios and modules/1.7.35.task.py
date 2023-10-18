def perevod_2_next(digit):                                                                                                                  # перевод из кастомной системы счсления в 10 систему счисления, если значений нет в словаре
    global table_digits
    digit = digit[::-1]
    amount = 0
    count = 0
    for i in digit:
        temp = [x for x in table_digits if table_digits[x] == i][0] * (custom_system ** count)
        count += 1
        amount += temp
    return amount


def perevod_2(digit):                                                                                                                       # перевод из кастомной системы счсления в 10 систему счисления, если значения есть в словаре значений
    global table_digits
    if digit in table_digits.values():
        result = str([i for i in table_digits if table_digits[i] == digit][0])
    else:                                                                                                                                   # здесь значений нет в словаре значений, идёт перевод на другую функцию
        result = str(perevod_2_next(digit))
    return result


def perevod_1_next(digit):                                                                                                                  # перевод из 10 в другую систему счисления, если значений нет в словаре
    global table_digits, custom_system
    result = ""
    while digit >= custom_system:
        next = digit - ((digit // custom_system) * custom_system)
        result += table_digits[next]
        digit //= custom_system
    result += table_digits[digit]
    return result[::-1]


def perevod_1(digit):                                                                                                                       # перевод из 10 в другую систему счисления, если значения есть в словаре значений
    global table_digits
    if digit in table_digits:
        result = table_digits[digit]
    else:
        result = str(perevod_1_next(digit))                                                                                                 # здесь значений нет в словаре значений, идёт перевод на другую функцию
    return result


while True:                                                                                                                                 # в результате будет переменная "custom_system" типа <int> с выбранной системой счисления
    print()
    custom_system = input("%100s" % "Выберите систему счисления, с которой будем работать в диапазоне от 2 до 16, кроме 10: ")
    try:
        custom_system = int(custom_system)
        if 2 <= custom_system <= 16 and custom_system != 10:
            break
        else:
            print("%99s" % "Вы ввели значения вне диапазона или 10.")
    except:
        print("%99s" % "Вы ввели что-то не то.")

while True:                                                                                                                                 # в результате будет переменная "perevod" типа <int> с выбором направления конвертации
    print()
    perevod = input("%100s" % "Введите (1) для переводя из 10 в кастомную систему счисления или (2) для обатного перевода: ")
    try:
        perevod = int(perevod)
        if perevod == 1 or perevod == 2:
            break
        else:
            print("%99s" % "Вы ввели что-то не то.")
    except:
        print("%99s" % "Вы ввели что-то не то.")

table_digits = dict()                                                                                                                       # в результате будет переменная "table_digits" типа <dict> со значениями цифр для разных систем счисления, где ключ - это десятичная, а значение ключа - это кастомная система счисления
digits_10 = range(0, custom_system)
digits_max = "0123456789ABCDEF"
digits_custom = digits_max[0:custom_system]
for a, b in zip(digits_10, digits_custom):
    table_digits[a] = b

if perevod == 1:                                                                                                                            # для перевода из 10 в другую систему счисления
    print()
    while True:
        digit = input("%100s" % "Введите целое число в десятичной системе счисления для перевода в кастомную систему: ")
        try:
            temp = "-" if digit[0] == "-" else ""
            digit = digit.removeprefix("-") if digit[0] == "-" else digit
            digit = perevod_1(int(digit))        
            print()
            break
        except:
            print("%99s" % "Вы ввели что-то не то.")
            print()
    print("%99s" % f"Ваше число из десятичной системы счисления равно {temp + str(digit)} в {custom_system}-й системе счисления.")
    print()
elif perevod == 2:                                                                                                                          # для перевода из кастомной в 10 систему счисления
    print()
    while True:
        digit = input("%100s" % "Введите число в кастомной системе счисления для перевода в десятичную: ")    
        try:
            temp = "-" if digit[0] == "-" else ""
            digit = digit.removeprefix("-") if digit[0] == "-" else digit
            digit = perevod_2(digit)
            print()
            break
        except:
            print("%99s" % "Вы ввели что-то не то.")
            print()
    print("%99s" % f"Ваше число из {custom_system}-й системы счисления равно {temp + str(digit)} в десятичной системе счисления.")
    print()