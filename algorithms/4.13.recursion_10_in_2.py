def my_def(digit):
    if digit == 1:
        return 1
    result = str(my_def(digit // 2)) + str(digit % 2)                                       # первое слагаемое - это вернувшийся базовый случай, + с каждым шагом прибавляется остаток от деления на 2
    return result


while True:
    digit = input("%100s" % "Введите число в десятичной системе счисления: ")
    try:
        digit = int(digit)
        break
    except:
        print("%99s" % "Вы допустили ошибку в вводе.")

print("%99s" % my_def(digit))