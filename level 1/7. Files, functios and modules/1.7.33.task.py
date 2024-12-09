def for_dict(digit):                                                                                                                                            # функция переводит по сути модуль числа
    global TABLE_DIGITS
    result = ""
    while digit > 15:
        next = digit - ((digit // 16) * 16)
        result += TABLE_DIGITS[next]
        digit //= 16
    result += TABLE_DIGITS[digit]
    return result[::-1]


def third(digit):                                                                                                                                               # функция переводит числа, которые меньше 15
    result = for_dict(digit * (-1))
    result = "-" + result
    return result


def second(digit):                                                                                                                                              # функция переводит числа, которые больше 15
    result = for_dict(digit)
    return result


def first(digit):                                                                                                                                               # функция переводит число, если оно в диапазоне от -15 до 15
    global TABLE_DIGITS
    return TABLE_DIGITS[digit]


TABLE_DIGITS = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

print()
while True:
    digit = input("%100s" % "Введите целое число в десятичной системе счисления для перевода в шестнадцатиричную: ")
    try:
        digit = int(digit)        
        print()
        break
    except:
        print("%99s" % "Вы ввели не число.")
        print()

if 0 <= digit <= 15:
    digit = first(digit)
elif -15 <= digit < 0:
    digit = "-" + first(digit * (-1))
elif digit > 15:
    digit = second(digit)
elif digit < -15:
    digit = third(digit)

print("%99s" % "Ваше число в шестнадцатиричной системе счисления:", digit)
print()