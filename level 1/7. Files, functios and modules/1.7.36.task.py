def my_simplify(numerator, denomenator):
    min_value = min(numerator, denomenator)
    divider = 2
    while divider <= min_value:
        if numerator % divider == 0 and denomenator % divider == 0:
            numerator /= divider; denomenator /= divider; min_value /= divider            
            divider = 2
        else:
            divider += 1
    return (int(numerator), int(denomenator))   


while True:
    numerator = input("%100s" % "Введите числитель дроби (целое число): ")
    denomenator = input("%100s" % "Введите знаменатель дроби (целое число): ")
    print()
    try:
        numerator = int(numerator)
        denomenator = int(denomenator)
        if denomenator == 0:
            print(("%99s" % "Знаменатель не может быть равным нулю."))
            continue
        break
    except:
        print("%99s" % "Вы допустили ошибку при вводе.")

if numerator in [0, 1, -1] or denomenator in [1, -1]:
    result = (numerator, denomenator)
else:
    result = my_simplify(numerator, denomenator)

print("%99s" % "Сокращённая дробь:", f"{result[0]}/{result[-1]}")