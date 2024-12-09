while True:
    digit = input("%100s" % "Введите до какого числа будем искать совершенные числа (к примеру, 10000): ")
    try:
        digit = int(digit)
        break
    except:
        print("%99s" % "Вы ввели не число.")
print()

result_list = []
diapazon = range(1, digit + 1)
for i in diapazon:                                          # проверим каждую цифру на совершенство
    temp_list_of_denominators = []
    for i2 in range(1, i):                                  # будем искать делители у каждой цифры        
        if i % i2 == 0:
            temp_list_of_denominators.append(i2)
    if sum(temp_list_of_denominators) == i:
        result_list.append(i)
        print("%99s" % f"Добавлено число: {i}.")