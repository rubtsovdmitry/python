while True:
    try:
        digit_1 = int(input("%65s" % "Введите первое положительное число (больше или равно 1): "))
        digit_2 = int(input("%65s" % "Введите второе положительное число (больше или равно 1): "))
        if digit_1 > 0 and digit_2 > 0:
            break
        else:
            print("%64s" % "Одно или оба числа меньше 1.")
    except:
        print("%64s" % "В вводе ошибка.")

min_digit = min(digit_1, digit_2)
while min_digit >= 1:
    if digit_1 % min_digit == 0 and digit_2 % min_digit == 0:
        print("%64s" % "Наибольший общий делитель равен:", min_digit)
        break
    min_digit -= 1