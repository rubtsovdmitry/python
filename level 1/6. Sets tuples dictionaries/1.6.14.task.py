result_dict = {1:1}                                                        # этот словарь будем дополнять готовыми результатами, стартует уже с минимальными данными для цифры 1

number = int(input("Введите число:")    )                                  
while number > 0:                                                          # в цикле будет спрашивать о новом числе, пока не введёшь отрицательное число        
    if number in result_dict.keys(): 
        print("Для числа", number, "факториал равен", result_dict[number])
    elif number not in result_dict.keys():
        work_range = range((max(result_dict.keys()) + 1), number + 1)      # создание range, кот. будем обходить в цикле  
        composition = result_dict[max(result_dict.keys())]                 # вынимаем максимальное значение из существующего словаря
        for i in work_range:                                               # обойдём в цикле все числа в range        
            composition *= i                                               # считаем новое произведение факториала
            result_dict[i] = composition                                   # создаём ключ в словаре со значением переменной "composition"
        print("Для числа", number, "факториал равен", result_dict[number])
    number = int(input("Введите число:"))