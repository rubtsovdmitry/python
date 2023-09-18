########################## первый способ

year = int(input("%100s" % "Введите год: "))
leap_year = True if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 != 0) else False                 # определим високосный ли год (ранее такая задача встречалась)

days31 = [1, 3, 5, 7, 8, 10, 12]
days30 = [4, 6, 9, 11]
days28_29 = [2]
month = int(input("%100s" % "Введите месяц (в формате 1 ... 12): "))
number = int(input("%100s" % "Введите число (в формате 1 ... 28 .. 30 .. 31): "))

# проверка данных
test = True
if month > 12 or number > 31:
    test = False
    print("%99s" % "В году не может быть более 12 месяцев. В месяце не может быть более 31 дня.")
elif month in days30 and number > 30:
    test = False
    print("%99s" % "В этом месяце должно быть меньше дней.")
elif month in days28_29 and number > 29:
    test = False
    print("%99s" % "В этом месяце должно быть меньше дней")
elif leap_year == False and month == 2 and number > 28:
    test = False
    print("%99s" % "Это не високосный год и в феврале не может быть более 28 дней")

# решение
if test:
    if leap_year == True and month in days28_29 and number == 29:          
        print("%99s" % "Следующая дата:", year, (month + 1), 1)
    elif leap_year == False and month in days28_29 and number == 28:
        print("%99s" % "Следующая дата:", year, (month + 1), 1)
    elif month == 12 and number == 31:
        print("%99s" % "Следующая дата:", (year + 1), 1, 1)
    elif month in days31 and month != 12 and number == 31:
        print("%99s" % "Следующая дата:", year, (month + 1), 1)
    elif month in days30 and number == 30:
        print("%99s" % "Следующая дата:", year, (month + 1), 1)
    else:
        print("%99s" % "Следующая дата:", year, month, (number + 1))

########################## второй способ

import datetime

print()
year = int(input("%100s" % "Введите год: "))
month = int(input("%100s" % "Введите месяц (в формате 1 ... 12): "))
number = int(input("%100s" % "Введите число (в формате 1 ... 28 .. 30 .. 31): "))

d = datetime.date(year, month, number)                                                                                        # создадим переменную типа date из входных данных
d_new = d + datetime.timedelta(days=1)                                                                                        # прибавим 1 день с помощью функции timedelta
print("%99s" % "Следующая дата:", d_new)