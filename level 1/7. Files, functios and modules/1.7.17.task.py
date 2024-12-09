def my_function(*custom):                                                                           # *custom - такая запись даёт на вход кортеж custom из входящих аргументов
    return ((min(custom) + max(custom)) / 2)

# ввод цифр
while True:
    digit = input("%75s" % "Введите первое число: ")
    digit_2 = input("%75s" % "Введите второе число: ")
    digit_3 = input("%75s" % "Введите третье число: ")
    try:
        digit = int(digit)
        digit_2 = int(digit_2)
        digit_3 = int(digit_3)
        break
    except:
        print("%74s" % "Вы ввели не цифры.")

print("%74s" % "Медиана числового ряда равна:", my_function(digit, digit_2, digit_3))