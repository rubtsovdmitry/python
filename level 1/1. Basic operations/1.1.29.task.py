digit = int(input("Введите положительное целое четырехзначное число, например 3141: "))
amount = 0
amount = digit % 10
digit //= 10
amount += digit % 10
digit //= 10
amount += digit % 10
digit //= 10
amount += digit % 10
print("Сумма всех чисел равна", amount)