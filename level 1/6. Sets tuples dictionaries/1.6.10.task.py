# ввод данных (без проверки)
number = int(input("Введите максимальное значение кубика (любое натуральное число): "))
number_range = range(1, number + 1)                                                                                 # эту переменную будем обходить в цикле
number_range2 = range(1, number + 1)                                                                                # эта переменная создана для второго кубика

for i in number_range:                                                                                              # обойдём значения кубиков в цикле 
    for i2 in number_range2:
        amount = i + i2                                                                                             # сумма меняется в цикле
        print(i, i2, amount)