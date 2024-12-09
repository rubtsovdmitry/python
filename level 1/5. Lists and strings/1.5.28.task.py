while True:
    digit = input("%100s" % "Введите целое число: ")
    try:
        digit = int(digit)
        break
    except:
        print("%99s" % "Вы ввели не число.")
print()

result_list = []
denominator = digit - 1
while denominator >= 1:
    if digit % denominator == 0:
        result_list.append(denominator)
    denominator -= 1

for i in result_list:
    print("%99s" % i)