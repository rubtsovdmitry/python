def my_days_in_february(year):
    result = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0) else 28
    return result    


def my_days_in_month(year, month):
    days_in_month = { 1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 }
    if month in days_in_month:
        result = days_in_month[month]
    else:
        result = my_days_in_february(year)
    return result


while True:
    year = input("%100s" % "Введите год (1, 2 ... 2023): ")
    month = input("%100s" % "Введите месяц (1, 2 ... 12): ")
    print()
    try:
        year = int(year)
        month = int(month)
        if year < 0 or month < 0 or month > 12:
            print(("%99s" % "Вы ввели отрицательные значения или месяц, который больше 12."))
            continue
        break
    except:
        print("%99s" % "Вы допустили ошибку при вводе.")

result = my_days_in_month(year, month)

print("%99s" % "Количество дней в месяце:", result)