digit = int(input("Введите целое число: "))
amount = int(digit * (digit + 1) / 2)
print("Сумма всех натуральных чисел от 1 до числа равна:", "%10i" % (amount))        # здесь явным способом указано, что на вывод идёт целое число с выделением под него 10em