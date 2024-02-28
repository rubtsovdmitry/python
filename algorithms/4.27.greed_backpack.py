import copy


"""ФУНКЦИЯ ДОБАВЛЕНИЯ ПРЕДМЕТОВ В result (КОНЕЧНЫЙ РЕЗУЛЬТАТ)."""
def function_mod_result():
    global result
    a = max(dict(things.values()).keys())
    temp = [[x, y] for x, y in things.items() if y[0] == a]
    result += temp


"""ФУНКЦИЯ МОДЕРНИЗАЦИИ ГЛАВНОЙ ХЕШ-ТАБЛИЦЫ. УБЕРЁМ СЛИШКОМ ТЯЖЁЛЫЕ ТОВАРЫ."""
def function_mod():
    free_for_weight = 0
    for i in result:
        free_for_weight += i[-1][-1]
    free_for_weight = backpack - free_for_weight
    temp = copy.copy(things)
    for a, b in temp.items():
        if b[-1] > free_for_weight:
            del things[a]


"""ФУНКЦИЯ ПРОВЕРКИ ОКОНЧАНИЯ ЦИКЛА. МОЖНО ЛИ ЕЩЁ ПОЛОЖИТЬ ЧТО-НИБУДЬ В РЮКЗАК."""
def function_check():
    temp = False
    free_for_weight = 0
    for i in result:
        free_for_weight += i[-1][-1]
    free_for_weight = backpack - free_for_weight
    for i in things.values():
        if i[-1] <= free_for_weight:
            temp = True            
            break
    return temp


"""ВХОДНЫЕ ДАННЫЕ. ХЕШ-ТАБЛИЦА для предметов."""
things = {
    "Магнитофон": [3000, 30],
    "Ноутбук": [2000, 20],
    "Гитара": [1500, 15]    
}
backpack = 35                                                                                           # грузоподъёмность рюкзака

"""ОПРЕДЕЛЕНИЕ ПЕРВОГО ПРЕДМЕТА."""
a = max(dict(things.values()).keys())                                                                   # самая дорогая вещь, которую можно положить (вес для первой вещи не проверяется)
result = [[x, y] for x, y in things.items() if y[0] == a]                                               # результат с первой вещью, который будет дополняться далее --> [['Магнитофон', [3000, 30]]]

"""УБРАТЬ ПЕРВЫЙ ПРЕДМЕТ ИЗ things."""
for i in result:                                                                                        # в цикле убрать вещи, который стали определены в result из things
        if i[0] in things:
            del things[i[0]]

"""ОСНОВНОЙ ЦИКЛ."""
while function_check():                                                                                 # при наших входных данных условие для цикла будет False, но если изменить backpack, к примеру на 45, то цикл запустится    
    function_mod()                                                                                      # уберём слишком тяжёлые товары из списка подходящих для рюкзака из things
    function_mod_result()                                                                               # переместим один товар из things в result
    for i in result:                                                                                    # в цикле убрать вещи, который стали определены в result из things
        if i[0] in things:
            del things[i[0]]

"""выведем список вещей в stdout"""
print()
usd = int()
for i in result:
    usd += i[-1][0]
    print(i[0])
print(f"Сумма: ${usd}")
print()