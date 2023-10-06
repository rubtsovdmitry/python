def my_function(a, r, n):
    if r == 1:
        return (a * n)    
    else:
        return int(a * (1 - r ** n) / (1 - r))


# проверка входных данных №1
while True:
    a = input("%50s" % "Введите первый элемент последовательности: ")
    try:
        a = int(a)
        break
    except:
        print("%49s" % "Вы ввели не число.")

# проверка входных данных №2
while True:
    r = input("%50s" % "Введите знаменатель последовательности: ")
    try:
        r = int(r)
        if r < 0:
            print("%49s" % "Вы ввели отрицательный знаменатель.")
            continue
        else:
            break
    except:
        print("%49s" % "Вы ввели не число.")

# проверка входных данных №3
while True:
    n = input("%50s" % "Введите количество элементов последовательности: ")
    try:
        n = int(n)
        if n >= 1:
            break
        else:
            print("%49s" % "Вы ввели количество элементов меньше 1.")
            continue
    except:
        print("%49s" % "Вы ввели не число.")

amount = my_function(a, r, n)
print("%49s" % "Сумма геометрической прогрессии:", amount)