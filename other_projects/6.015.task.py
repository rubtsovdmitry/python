import sys, time, bext


def getSevSegStr(number, minWidth=0):
    number = str(number).zfill(minWidth)

    rows = ['', '', '']                                                                                 # в дальнейшем элементы будут заполняться в цикле
    for i, numeral in enumerate(number):
        if numeral == '.':                                                                              # точка
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue                                                                                    # отправимся в начало цикла, не дожидаясь дальнейших проверок (пробела не будет)
        elif numeral == '-':                                                                            # тире
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':                                                                            # 0
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':                                                                            # 1
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':                                                                            # 2
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':                                                                            # 3
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':                                                                            # 4
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':                                                                            # 5
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':                                                                            # 6
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':                                                                            # 7
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':                                                                            # 8
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':                                                                            # 9
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        """установка пробелов между цифрами"""
        if i != len(number) - 1:                                                                        # если это не конец цифры, то ставить пробелы
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
    return '\n'.join(rows)                                                                              # преобразуем элементы списка в строку, соединив их '\n' - переносом строки


try:
    """ОСНОВНОЙ ЦИКЛ ПРОГРАММЫ"""
    while True:
        bext.clear()       
        currentTime = time.localtime()
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'                                                                    # 12-часов 12:00, не 00:00.
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        hDigits = getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        print()
        print('Нажмите <Ctrl-C> для выхода.')

        while True:                                                                         # этот подцикл позволяет не выполнять основной, пока не выполнится этот. он нужен, чтобы экран не мерцал.
            time.sleep(0.1)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    sys.exit()