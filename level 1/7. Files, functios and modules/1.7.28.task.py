def my_2(digit):    
    while True:
        digit += 1
        temp = 2
        while temp < digit:            
            if digit % temp == 0:
                break
            elif temp == digit - 1:
                return digit
            temp += 1


def my(digit):
    denominator = 2
    result = False
    while denominator != digit:
        if result:
            break
        elif digit % denominator == 0:
            result = True        
        denominator += 1
    return result


while True:
    try:
        digit = int(input("%75s" % "Введите любое положительное число: "))
        if digit <= 1:
            print("%74s" % "Вы ввели ноль, один или отрицательное число.")
            print()
            continue        
        else:
            break
    except:
        print("%74s" % "Вы ввели что-то не то.")
        print()

if my(digit):
    print("%74s" % "Введённое число составное.", "%44s" % "Ближайшее простое число:", my_2(digit))
else:
    print("%74s" % "Введённое число простое.", "%44s" % "Следующее простое число:", my_2(digit))