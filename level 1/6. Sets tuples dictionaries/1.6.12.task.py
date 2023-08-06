# ввод данных (без проверки)
number = int(input("Введите максимальное значение кубика (любое натуральное число): "))
number_range = range(1, number + 1)                                                                                 # эту переменную будем обходить в цикле
number_range2 = range(1, number + 1)                                                                                # эта переменная создана для второго кубика

result_dict = dict()                                                                                                # составим словарь, где ключ - это сумма, а его значения - это комбинации очков на кубиках
for i in number_range:                                                                                              # обойдём значения кубиков в цикле 
    for i2 in number_range2:
        amount = i + i2                                                                                             # сумма меняется в цикле
        if amount not in result_dict.keys():                                        
            result_dict[amount] = {(i, i2)}                                                                         # создаём ключ в словаре (это сумма) со значением, значение - множество из кортежей
        elif amount in result_dict.keys() and (i2, i) not in result_dict[amount]:  
            result_dict[amount] |= {(i, i2)}                                                                        # ключ в словаре уже есть, прибавляем ещё одну вариацию к значению ключа (это сумма) в словаре с помощью объединения множеств

# обойдем в цикле значения ключ:значение для печати
for i in result_dict.items():
    print(i)