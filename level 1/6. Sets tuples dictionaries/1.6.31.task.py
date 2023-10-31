# ввод данных (без проверки)
zero = { "0": "ноль" }
under_ten = { "1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять", "6": "шесть", "7": "семь", "8": "восемь", "9": "девять" }
under_twenty = { "10": "десять", "11": "одиннадцать", "12": "двенадцать", "13": "тринадцать", "14": "четырнадцать", "15": "пятнадцать", "16": "шестнадцать", "17": "семнадцать", "18": "восемнадцать", "19": "девятнадцать" }
under_hundred = { "0": "", "2": "двадцать", "3": "тридцать", "4": "сорок", "5": "пятьдесят", "6": "шестьдесят", "7": "семьдесят", "8": "восемьдесят", "9": "девяносто" }
under_thousand = { "1": "сто", "2": "двести", "3": "триста", "4": "четыреста", "5": "пятьсот", "6": "шестьсот", "7": "семьсот", "8": "восемьсот", "9": "девятьсот" }
digit = input("%100s" % "Введите число от 0 до 999: ")

if digit in zero:
    print("%99s" % f"Ваше число прописью: {zero[digit].capitalize()}.")
elif digit in under_ten:
    print("%99s" % f"Ваше число прописью: {under_ten[digit].capitalize()}.")
elif digit in under_twenty:
    print("%99s" % f"Ваше число прописью: {under_twenty[digit].capitalize()}.")
elif len(digit) == 2:                                                                           # составим двузначное число
    result = ""
    for a, b in under_hundred.items():
        if a == digit[0]:
            result += b
            for c, d in under_ten.items():
                if c == digit[1]:
                    result += (" " + d)
    print("%99s" % f"Ваше число прописью: {result.capitalize()}.")
elif len(digit) == 3:                                                                           # составим трёхзначное число
    result = ""
    for a, b in under_thousand.items():                                                         # сотни
        if a == digit[0]:
            result +=b
            for c, d in under_hundred.items():                                                  # десятки                
                if c == digit[1]:
                    result += (" " + d + " ") 
                    if result[-2] == " ":                                                       # если вторая цифра ноль, то будет образовываться ещё один пробел, его надо удалить
                        result = result.removesuffix(" ")
                    for e, f in under_ten.items():                                              # единицы                        
                        if e == digit[2]:
                            result += f                                                
    if digit[-2:] in under_twenty:                                                              # теперь нужно поправить вывод, если последние две цифры были в словаре under_twenty
        result += (" " + under_twenty[digit[-2:]])
    result = result.removesuffix(" ")                                                           # если перед выводом будут пробелы в конце строки, то удалить (для круглых сотен)
    print("%99s" % f"Ваше число прописью: {result.capitalize()}.")