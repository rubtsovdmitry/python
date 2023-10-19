import datetime

def my_magic_date(result, day, month):
    mod = int(str(result)[2:4])
    if (day * month) == mod:
        return True


while True:
    year = input("%100s" % "Введите год (1, 2, ... 2023): ")
    month = input("%100s" % "Введите месяц (1, 2 ... 12): ")
    day = input("%100s" % "Введите день (1, 2 ... 31): ")
    print()
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        if year < 0 or month < 0 or day < 0:
            print(("%99s" % "Вы ввели отрицательные значения."))
            continue
        result = datetime.date(year, month, day)                                                    # так проверим существует ли эта дата (29 февраля)
        break
    except:
        print("%99s" % "Вы допустили ошибку при вводе или такой даты не существует.")

result_2 = my_magic_date(result, day, month)

if result_2:
    print("%99s" % f"Дата {result} магическая.")    
else:
    print("%99s" % f"Дата {result} не магическая.")