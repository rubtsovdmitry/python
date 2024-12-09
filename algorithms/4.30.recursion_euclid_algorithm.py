def euclid(a, b):
    if b == 0:                                                          # базовый случай, при котором одно из чисел равно 0
        return a
    result = euclid(b, a % b)                                           # при каждом уровне стека числа меняются местами, и одно число пересчитывается
    return result

while True:
    try:
        print()
        a = int(input("%50s" % "Введите первое число: "))
        break
    except:
        print("%49s" % "Вы ввели не число. Попробуйте ещё раз.")

while True:
    try:
        print()
        b = int(input("%50s" % "Введите второе число: "))
        break
    except:
        print("%49s" % "Вы ввели не число. Попробуйте ещё раз.")

result = euclid(a, b)
print()
print("%49s" % "Наибольший общий делитель равен:", result)
print()