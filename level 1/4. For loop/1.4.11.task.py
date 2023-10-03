import itertools

diapazon = range(1, 101)                                                                                                   # диапазон чисел для игры
count = 1                                                                                                                  # счётчик игроков
names = dict()                                                                                                             # словарь игроков
while True:                                                                                                                # цикл, в котором идёт заполнение словаря игроками
    player = "Игрок " + str(count)
    name = input("%85s" % f"Введите имя для {count}-го игрока (для отмены оставьте пустым и нажмите enter): ")
    count += 1
    if name != "":
        names[player] = name
    else:
        break
while True:                                                                                                                # цикл для добавления ещё одного игрока - ВАС
    player = "Вы"
    name = input("%85s" % f"Введите Ваше имя: ")    
    if name != "":
        names[player] = name
        break
    else:
        continue
for a, b, c in zip(itertools.cycle(names.keys()), itertools.cycle(names.values()), diapazon):                              # функция zip должна обойти все значения в диапазоне чисел с коротким списком игроков. зациклим список игроков при помощи itertools.cycle
    if a != "Вы":
        if c % 3 == 0 and c % 5 == 0:
            answer = "Fizz-Buzz"
        elif c % 3 == 0:
            answer = "Fizz"
        elif c % 5 == 0:
            answer = "Buzz"    
        else:
            answer = c
    elif a == "Вы":
        print("%84s" % f"Цифра {c}")
        answer = input("%85s" % "Напишите (Fizz, Buzz или Fizz-Buzz):")
        if c % 3 == 0 and c % 5 == 0 and answer == "Fizz-Buzz":
            answer = "Fizz-Buzz"
        elif c % 3 == 0 and c % 5 == 0 and answer != "Fizz-Buzz":
            answer = "Проигрыш"
            break
        elif c % 3 == 0 and answer == "Fizz":
            answer = "Fizz"
        elif c % 3 == 0 and answer != "Fizz":
            answer = "Проигрыш"
            break
        elif c % 5 == 0 and answer == "Buzz":
            answer = "Buzz"
        elif c % 5 == 0 and answer != "Buzz":
            answer = "Проигрыш"
            break
        elif answer == str(c):
            answer = c
        elif answer != str(c):
            answer = "Проигрыш"
            break        
    print("%13s" % f"Цифра {c}", "%13s" % a, "%13s" % b, "%13s" % answer)
if answer == "Проигрыш":
    print("%13s" % f"Цифра {c}", "%13s" % a, "%13s" % b, "%13s" % answer)