# без проверки входных данных
number = int(input("%100s" % "Введите число месяца: "))
month = input("%100s" % "Введите месяц: ")

if (month == "март" and number >= 20) or (month == "апрель" or month == "май") or (month == "июнь" and number < 21):
    print("%99s" % "Сейчас весна.")
elif (month == "июнь" and number >= 21) or (month == "июль" or month == "август") or (month == "сентябрь" and number < 22):
    print("%99s" % "Сейчас лето.")
elif (month == "сентябрь" and number >= 22) or (month == "октябрь" or month == "ноябрь") or (month == "декабрь" and number < 21):
    print("%99s" % "Сейчас осень.")
elif (month == "декабрь" and number >= 21) or (month == "январь" or month == "февраль") or (month == "март" and number < 20):
    print("%99s" % "Сейчас зима.")