import datetime


def pasxa_2(year, month, day):                                                       # функция определяет точное число Пасхи (уже с переносом на воскресенье)
    day_of_week = datetime.datetime(year, month, day, 00, 00, 00).weekday()          # определим день недели
    slagaemoe = 6 - day_of_week                                                      # дельта между воскресеньем и днём недели
    date = str(datetime.datetime(year, month, day, 00, 00, 00) + datetime.timedelta(days=slagaemoe))[0:10]      # прибавляет к дате дельту (получаем искомую дату)
    return date


def pasxa(year):                                                                    # функция определяет точное число Пасхи (без переноса на воскресенье)
    a = year % 19
    b = int(year / 100)
    c = year % 100
    d = int(b / 4)
    e = b % 4
    f = int((b + 8) / 25)
    g = int((b - f + 1) / 3)
    h = (19 * a + b - d - g + 15) % 30
    i = int(c / 4)
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7                                            # лучше не называть переменную буквой "l" - правило хорошего тона в python
    m = int((a + 11 * h + 22 * l) / 451)
    month = int((h + l + 7 * m + 114) / 31)
    day = 1 + (h + 1 - 7 * m + 114) % 31
    date = pasxa_2(year, month, day)    
    date = f"Пасха приходится на {date}"     
    return date
try:
    year = int(input("Введите год и программа определит, когда Пасха? Год: "))
    print(pasxa(year))    
except:
    print("Вы ввели неверно.")