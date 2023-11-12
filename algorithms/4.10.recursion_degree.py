def my_def(digit, degree):
    if degree < 0:
        return None
    my_def(digit, (degree - 1))
    print()
    print(f"Возведение числа {digit} в степень {degree} равно: {digit ** degree}")


while True:
    digit = input("%100s" % "Введите число, которое будем возводить в степень: ")
    degree = input("%100s" % "Введите степень, в которую будем возводить число: ")
    try:
        digit = int(digit)
        degree = int(degree)
        break
    except:
        print("%99s" % "Вы ввели не число.")

my_def(digit, degree)