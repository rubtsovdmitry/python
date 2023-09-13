try:
    height = int(input("Введите свой рост в см: "))
    weight = int(input("Введите свой вес в кг: "))
    bmi = weight / (height / 100) ** 2
    print("Индекс массы тела равен", round(bmi,2))
except ValueError:
    print("Ошибка в вводе.")
except ZeroDivisionError:
    print("Вес введён равный нулю (деление на нуль невозможно).")