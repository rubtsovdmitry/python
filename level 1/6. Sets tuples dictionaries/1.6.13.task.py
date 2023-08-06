# ввод константы
NUMBER = 30

# создание range, кот. будем обходить в цикле
work_range = range(1, NUMBER + 1)

result_dict = dict()                                    # этот словарь будем заполнять готовыми результатами
composition = 1                                         # первое значение, кот. соответствует для 1 всегда равно 1
for i in work_range:                                    # обойдём в цикле все числа в range
    composition *= i                                    # считаем новое произведение факториала
    result_dict[(str(i) + "!")] = composition           # создаём ключ в словаре со значением переменной "composition"
print()

for i in result_dict.items():                           # выведем пары ключ-значения результатирующего словаря в цикле
    print(i)