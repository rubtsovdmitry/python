def my_def(digit, degree):
    if degree < 0:
        return 0
    amount = (digit ** degree) + my_def(digit, (degree - 1))
    return amount


while True:
    digit = input("%100s" % "Введите число, которое будем возводить в степень: ")
    degree = input("%100s" % "Введите степень, до которой будем возводить число: ")
    try:
        digit = int(digit)
        degree = int(degree)
        break
    except:
        print("%99s" % "Вы ввели не число.")

print("%99s" % f"Сумма всех степеней до {degree} числа {digit} равна {my_def(digit, degree)}.")