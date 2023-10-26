import random, copy

MASTI = ["ПИКИ", "ЧЕРВЫ", "БУБНЫ", "ТРЕФЫ"]
NOMINAL = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]

koloda_sort = []                                                                                    # здесь будем хранить колоду отсортированную колоду
for a in MASTI:
    for b in NOMINAL:
        nominal_mast = b + " * " + a
        koloda_sort.append(nominal_mast)

koloda_sort_2 = copy.copy(koloda_sort)                                                              # копия списка, который будем менять в цикле
for index, item in enumerate(koloda_sort_2):                                                        # обходим в цикле сразу индексы и значения
    x = random.randint(index, 51)                                                                   # выводим случайный результат, с учётом изменения индекса в цикле
    temp_card = koloda_sort_2[index]                                                                # эта и следующие 2 строки меняют карты местами в списке "koloda_sort_2"
    koloda_sort_2[index] = koloda_sort_2[x]                                                         
    koloda_sort_2[x] = temp_card
    
for a, b in zip(koloda_sort, koloda_sort_2):                                                        # выведем на печать в цикле отсортированную колоду и перемешанную по парам
    print(a, b)

##############################################################################################
############# проверка #######################################################################
##############################################################################################

print()
for i in koloda_sort_2:
    koloda_sort.remove(i)
if len(koloda_sort) == 0:
    print("test pass")
else:
    print("test fail")