import random

amount_try = 0
count = 0                                           # счётчик попыток (должно быть 10)
while count < 10:
    count += 1                                      # прибавляем 1 попытку
    result_list = []                                # при новой попытке список выпаданий обнуляется
    count_int = 2
    result_list.append(random.randint(1, 2))        # заполним 1-е значение для списка
    if result_list[0] == 1:                         # печать орел или решка
        print("О ", end="")
    else:
        print("Р ", end="")
    result_list.append(random.randint(1, 2))        # заполним 2-е значение для списка
    if result_list[1] == 1:                         # печать орел или решка
        print("О ", end="")
    else:
        print("Р ", end="")    
    while True:                                     # будем искать три совпадения подряд для орла или решки
        count_int += 1
        x = random.randint(1, 2)
        result_list.append(x)
        if result_list[-1] == 1:                    # печать орел или решка
            print("О ", end="")
        else:
            print("Р ", end="")
        if result_list[-1] == result_list[-2] == result_list[-3]:
            print(f"(попыток: {count_int})")
            break
    amount_try += count_int
print()
print("Среднее количество попыток:", round((amount_try / 10), 1))
print()