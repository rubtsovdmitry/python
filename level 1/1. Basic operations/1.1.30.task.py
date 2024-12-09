digit1 = int(input("Введите первое число: "))
digit2 = int(input("Введите второе число: "))
digit3 = int(input("Введите третье число: "))
digit_max = max(digit1, digit2, digit3)
digit_min = min(digit1, digit2, digit3)
digit_third = digit1 + digit2 + digit3 - digit_max - digit_min
print("Числа в порядке возрастания:", "%15i%15i%15i" % (digit_min, digit_third, digit_max))