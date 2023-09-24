digit = int(input("%50s" % "Введите целое число (кроме нуля): "))
while True:
    if digit == 0:
        digit = int(input("%50s" % "Введите целое число (кроме нуля): "))
    else:
        break
amount = digit
count = 1
while True:
    digit = int(input("%50s" % "Введите целое число (нуля для выхода): "))
    if digit == 0:
        break
    else:
        amount += digit
        count += 1
result = amount / count
print("%49s" % "Среднее значение округлённое до целого:", int(result + 0.5))