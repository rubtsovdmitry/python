import random

print()
print("%99s" % "Играем в рулетку")
print()
print("%99s" % "Коэффициент для угаданного цвета равен 1 к 0.90")
print("%99s" % "Коэффициент для чётности равен 1 к 0.90")
print("%99s" % "Коэффициент для числа равен 1 к 50")
print("%99s" % "Коэффициент для 0 равен 1 к 30")
print()

COLOUR = {
    "red": (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36),
    "black": (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
}
score = float(input("%100s" % "Введите сколько у Вас денег в руб. (в формате 1000.00): "))
print()

# ввод данных только для старта цикла
stavka = float(input("%100s" % "Введите ставку в руб. (в формате 1000.00): "))
print("")
print("%99s" % "Введите на что ставите, если будет ошибка ввода, то деньги сразу спишутся.")
forecast = input("%100s" % "красное / чёрное / чётное / нечётное / (цифра от 0 до 36): ")
x = random.randint(0,37)
print()
print("%99s" % "Проверка", x)
print()

# запуск цикла
while score > 0 and stavka <= score: 
    if forecast == "красное" and x in COLOUR["red"]:
        print("%99s" % "Выигрыш")
        score = round((score + stavka * 0.9), 2)
    elif forecast == "чёрное" and x in COLOUR["black"]:
        print("%99s" % "Выигрыш")
        score = round((score + stavka * 0.9), 2)
    elif forecast == "чётное" and x % 2 == 0:
        print("%99s" % "Выигрыш")
        score = round((score + stavka * 0.9), 2)
    elif forecast == "нечётное" and x % 2 != 0:
        print("%99s" % "Выигрыш")
        score = round((score + stavka * 0.9), 2)   
    elif (forecast == "0" and x == 0) or (forecast == "0" and x == 37):
        print("%99s" % "Выигрыш")
        score = round((score + stavka * 30), 2)
    elif forecast == str(x):
        print("%99s" % "Выигрыш")
        score = round((score + stavka * 50), 2)
    else:
         print("%99s" % "Проигрыш")
         score = round((score - stavka), 2)
    print("%99s" % "Ваш счет:", score)
    print()
    # в цикле проверяем не закончились ли деньги
    if score == 0:
        print("%99s" % "Вы проиграли все деньги")
    else:      
        print("%99s" % "Ваша следующая ставка:")
        stavka = float(input("%100s" % "Введите ставку в руб. (в формате 1000.00): "))
        forecast = input("%100s" % "красное / чёрное / чётное / нечётное / (цифра от 0 до 36): ")
    x = random.randint(0,37)
    print("%99s" % "Проверка", x)