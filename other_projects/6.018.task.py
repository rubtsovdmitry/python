import random, sys, time, bext


bext.clear()
print()
input('Нажмите Enter, чтобы начать...')

while True:
    print()
    time.sleep(random.randint(20, 50) / 10.0)                                       # рандомная задержка перед выстрелом
    print('Выстрел!!!')
    drawTime = time.time()                                                          # фиксация времени (старт)
    input()  
    timeElapsed = time.time() - drawTime                                            # как только будет выполнен предыдущий input, станет зафиксировано время реакции в переменной

    if timeElapsed < 0.01:                                                          # фальтстарт
        print('Вы нажали enter раньше времени.')
    elif timeElapsed > 0.33:
        timeElapsed = round(timeElapsed, 4)
        print('Вы нажали enter очень поздно!!!', timeElapsed, 'секунд.')
    else:
        timeElapsed = round(timeElapsed, 4)
        print('Ваша реакция', timeElapsed, 'секунд.')
        print('Вы выиграли!')

    print('Нажмите QUIT для выхода, или Enter для продолжение.')
    response = input('> ').upper()
    if response == 'QUIT':
        print('Игра окончена!')
        sys.exit()