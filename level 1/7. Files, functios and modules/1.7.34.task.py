def next(digit):
    global TABLE_DIGITS
    digit = digit[::-1]
    amount = 0
    count = 0
    for i in digit:
        temp = [x for x in TABLE_DIGITS if TABLE_DIGITS[x] == i][0] * (16 ** count)
        count += 1
        amount += temp
    return amount


def perevod(digit):
    global TABLE_DIGITS
    if digit in TABLE_DIGITS.values():
        result = str([i for i in TABLE_DIGITS if TABLE_DIGITS[i] == digit][0])
    else:
        result = str(next(digit))
    return result


TABLE_DIGITS = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

print()
while True:
    digit = input("%100s" % "Введите число в шестнадцатиричной системе счисления для перевода в десятичную: ")    
    try:
        temp = "-" if digit[0] == "-" else ""
        digit = digit.removeprefix("-") if digit[0] == "-" else digit
        digit = perevod(digit)
        print()
        break
    except:
        print("%99s" % "Вы ввели что-то не то.")
        print()

print("%99s" % "Ваше число в шестнадцатиричной системе счисления:", (temp + str(digit)))
print()