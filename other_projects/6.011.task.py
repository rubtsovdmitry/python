import bext, random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

purse = 5000

bext.clear()

while True:                                                                                             # основной цикл игры
    """ВВОД ДАННЫХ"""
    bext.fg("magenta")
    print()
    print(f"Я вас есть {purse} денег, какую ставку желаете сделать? (для выхода наберите \"QUIT\")")
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Спасибо за игру.')
            sys.exit()
        elif not pot.isdecimal():
            print('Ошибка, повторите ввод!!!')
        elif int(pot) > purse:
            print('Вы сделали ставку, которая больше остатка денег, повторите ввод!!!')
        else:
            pot = int(pot) 
            break  

    """БРОСАЕМ КОСТИ"""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    """НА ЧТО СТАВИТЕ?"""
    bext.fg("cyan")
    print()
    print("""Сделайте вашу ставку.
CHO (чётный) или HAN (нечётный)?""")    
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Ошибка ввода!!! Введите "CHO" или "HAN".')
            continue
        else:
            break

    """ВЫВОД РЕЗУЛЬТАТА КОСТЕЙ"""
    bext.fg("blue")        
    print()
    print('На костях выпало:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)    
    
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'
    playerWon = bet == correctBet

    """ВЫВОД РЕЗУЛЬТАТА ИГРЫ"""
    bext.fg("red")        
    print()
    if playerWon:
        print(f"Вы выиграли!!! Заберите {pot} денег.")
        purse = purse + pot 
        print(f"Комиссия равна {pot // 10} денег.")
        purse = purse - (pot // 10)
    else:
        purse = purse - pot
        print("ВЫ ПРОИГРАЛИ!!!")

    """ПРОВЕРКА СЧЁТА"""   
    if purse == 0:
        bext.fg("green")
        print()
        print('ВЫ ПРОИГРАЛИ ВСЕ ДЕНЬГИ!!!')
        print('СПАСИБО ЗА ИГРУ!!!')
        sys.exit()