import random, time, sys, bext

# ввод констант
MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40

# спросим в цикле сколько улиток
bext.clear()
while True:
    print('Сколько улиток учавствует в забеге? Максимум:', MAX_NUM_SNAILS)
    response = input('> ')
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
    
# ввод имени каждой улитки
snailNames = []  
for i in range(1, numSnailsRacing + 1):
    while True:  
        print(f"Введите имя {i}-й улитки.")
        name = input('> ')
        if len(name) == 0:
            print('Введите имя.')
        elif name in snailNames:
            print('Такое имя уже есть')
        else:
            break
    snailNames.append(name)

# Отобразим улитки на старте
bext.clear()
print('СТАРТ' + (' ' * (FINISH_LINE - len('START')) + 'ФИНИШ'))
print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))
snailProgress = {}
for snailName in snailNames:
    print(snailName[:MAX_NAME_LENGTH])                                                          # обрезает отображение имени на установленном в константах максимальной длине имени
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5) 

# основной цикл программы
while True:  
    for i in range(random.randint(1, numSnailsRacing // 2)):                                    # стартуют не более половины улиток
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1                                                     # копим прогресс пути для каждой улитке в словаре snailProgress

        if snailProgress[randomSnailName] == FINISH_LINE:
            print(f"{randomSnailName}-я улитка выигрывает!")
            sys.exit()

    time.sleep(0.5) 

    bext.clear()
    print('СТАРТ' + (' ' * (FINISH_LINE - len('START')) + 'ФИНИШ'))
    print('|' + (' ' * (FINISH_LINE - 1) + '|'))

    # напечатаем путь улитки
    for snailName in snailNames:
        spaces = snailProgress[snailName]
        print((' ' * spaces) + snailName[:MAX_NAME_LENGTH])
        print(('.' * snailProgress[snailName]) + '@v')