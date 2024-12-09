import sys, time, bext

"""Семисегментный дисплей с маркировкой, каждый сегмент которого помечен от A до G:
 __A__
|     |    Каждая цифра на семисегментном дисплее:
F     B     __       __   __        __   __  __   __   __
|__G__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
|     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
E     C
|__D__|"""
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


"""ОСНОВНАЯ ФУНКЦИЯ"""
def function_main():
    # ввод значения в секундах для обратного отсчёта
    while True:
        try:
            print()
            seconds_total = int(input("Введите количество секунд: "))
            print()
        except:
            print("Вы ввели не цифры")
        else:
            break

    try:
        while True: 
            bext.clear()
            hours = str(seconds_total // 3600)                                                          # количество часов
            minutes = str((seconds_total % 3600) // 60)                                                 # количество минут
            seconds = str(seconds_total % 60)                                                           # количество секунд

            hDigits = getSevSegStr(hours, 2)                                                            # часовая строка, две цифры длиной
            hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()                                      # разобъём строку по разделителю, где разделитель - это \n (перенос строки), получится список строк, который сразу разберём на переменные

            mDigits = getSevSegStr(minutes, 2)                                                          # минутная строка, две цифры длиной
            mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()                                      # разобъём строку по разделителю, где разделитель - это \n (перенос строки), получится список строк, который сразу разберём на переменные

            sDigits = getSevSegStr(seconds, 2)                                                          # секундная строка, две цифры длиной
            sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()                                      # разобъём строку по разделителю, где разделитель - это \n (перенос строки), получится список строк, который сразу разберём на переменные

            """соберём переменные со строками в единое целое"""
            print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
            print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
            print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

            if seconds_total == 0:
                print()
                print('    * * * * БУМ * * * *')
                print()
                break

            print()
            print('Нажмите Ctrl-C для выхода.')
            print()

            time.sleep(1)                                                                               # Пауза 1 секунда.
            seconds_total -= 1                                                                          # Обратный отсчёт
    except KeyboardInterrupt:
        sys.exit()                                                                                      # Чтобы не выдавало ошибку при нажатии Ctrl-C


if __name__ == "__main__":    
    print()
    print("Скрипт запущен напрямую.")                                                                   
    function_main()
else:    
    print()
    print("Скрипт импортирован.")
    print()