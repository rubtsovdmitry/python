import random, itertools, time

#####################################################################################################################################################################################
# перемешаем карты
MASTI = ["ПИКИ", "ЧЕРВЫ", "БУБНЫ", "ТРЕФЫ"]
NOMINAL = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]

koloda_sort = []                                                                                  # здесь будем хранить колоду отсортированную колоду
for a in MASTI:
    for b in NOMINAL:
        nominal_mast = b + " * " + a
        koloda_sort.append(nominal_mast)

for index, item in enumerate(koloda_sort):                                                        # обходим в цикле сразу индексы и значения
    x = random.randint(index, 51)                                                                 # выводим случайный результат, с учётом изменения индекса в цикле
    temp_card = koloda_sort[index]                                                                # эта и следующие 2 строки меняют карты местами в списке "koloda_sort_2"
    koloda_sort[index] = koloda_sort[x]                                                         
    koloda_sort[x] = temp_card
#####################################################################################################################################################################################
# ввод данных
while True:
    number_card = input("%100s" % "Введите количество карт от 4 до 6: ")
    try:
        number_card = int(number_card)
        if 4 <= number_card <= 6:
            break
        else:
            print("%99s" % "Вы ввели не то количество.")            
    except:
        print("%99s" % "Вы ввели не цифры.")
while True:
    number_player = input("%100s" % "Введите количество игроков от 2 до 6: ")
    try:
        number_player = int(number_player)
        if 2 <= number_player <= 6:
            break
        else:
            print("%99s" % "Вы ввели не то количество.")            
    except:
        print("%99s" % "Вы ввели не цифры.")
#####################################################################################################################################################################################
# раздадим карты
player_1 = []
player_2 = []
player_3 = []
player_4 = []
player_5 = []
player_6 = []
amount_card = number_card * number_player
for a, b in zip(koloda_sort[:(amount_card)], itertools.cycle(range(1, number_player + 1))):
    if b == 1:
        print()
        player_1.append(a)
        print("%99s" % f"{a} для {b} игрока.")
        time.sleep(1)
    elif b == 2:
        player_2.append(a)
        print("%99s" % f"{a} для {b} игрока.")
        time.sleep(1)
    elif b == 3:
        player_3.append(a)
        print("%99s" % f"{a} для {b} игрока.")
        time.sleep(1)
    elif b == 4:
        player_4.append(a)
        print("%99s" % f"{a} для {b} игрока.")
        time.sleep(1)
    elif b == 5:
        player_5.append(a)
        print("%99s" % f"{a} для {b} игрока.")
        time.sleep(1)
    elif b == 6:
        player_6.append(a)
        print("%99s" % f"{a} для {b} игрока.")
        time.sleep(1)