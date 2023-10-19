import datetime

def my_function(year):
    result = (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)
    return result


year = range(1900, 2000)
month = range(1, 13)
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
no_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

leap_year = [range(1, (i + 1)) for i in leap_year]
no_leap_year = [range(1, (i + 1)) for i in no_leap_year]

result = []
for y in year:                                                              # обойдём в цикле каждый год
    if my_function(y):                                                      # своё условие для високосного года
        for m, l_i in zip(month, leap_year):                                        # свяжем zip-ом 12 месяцев (их номера) с 12 месяцев (диапазон дат в каждом месяце)
            for i in l_i:                                                           # обойдём в цикле каждый день месяца
                if str(m * i) == str(y)[-2:]:                                       # проверим магическое число или нет
                    result.append(str(datetime.date(y, m, i)))                    
    else:                                                                   # своё условие для не високосного года
        for m, l_i in zip(month, no_leap_year):                                     # ...
            for i in l_i:
                if str(m * i) == str(y)[-2:]:
                    result.append(str(datetime.date(y, m, i)))                    

for i in result:
    print(i)

print()
print(f"Всего {len(result)} магических дат в 20 веке.")