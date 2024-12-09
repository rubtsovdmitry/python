BORDER = 21                                                                             # заведём переменные в верхнем регистре, т.к. это константы
FIRST = 10.5                                                                
SECOND = 4

age = float(input("%50s" % "Введите человеческий возраст в годах: "))

if age < 0:
    print("%49s" % "Вы ввели отрицательный возраст:", "-")
elif age == 0:
    print("%49s" % "Вы ввели ноль:", "-")
elif age > BORDER:
    age4year = age - BORDER
    age4year = (age4year // SECOND) + ((age4year % SECOND) / SECOND)     
    result = age4year + (BORDER // FIRST)
    print("%49s" % "Возраст в переводе на собачий:", round(result, 2))
else:
    result = (age // FIRST) + (age % FIRST / FIRST)
    print("%49s" % "Возраст в переводе на собачий составляет:", round(result, 2))