import sys, bext


GOAL = 4                                                                                                                         # точное количество воды, которое должно быть в ведре, чтобы выиграть
steps = 0                                                                                                                        # сколько шагов сделал игрок, чтобы решить эту проблему

waterInBucket = {'8': 0, '5': 0, '3': 0}                                                                                         # Количество воды в каждом ведре

bext.clear()
width, height = bext.size()
bext.goto(0, int(height / 3))
bext.fg("purple")

"""основной цикл игры"""
while True:  
    """отображение текущего состояния вёдер"""
    print()
    print('Нужно набрать ровно ' + str(GOAL) + ' литра воды в одно из вёдер.\n')
    print('Вёдра:')

    waterDisplay = []                                                                                                            # переменная содержит строки для обозначения воды или пустого пространства

    """получим строковое значение для восьмилитрового ведра"""
    for i in range(1, 9):                                                                                                        
        if waterInBucket['8'] < i:
            waterDisplay.append('      ')                                                                                        # заполнить ведро пробелами (пустота)
        else:
            waterDisplay.append('🟦🟦🟦')                                                                                        # заполнить ведро синими квадратами (вода)

    """получим строковое значение для пятилитрового ведра"""
    for i in range(1, 6):
        if waterInBucket['5'] < i:
            waterDisplay.append('      ')  
        else:
            waterDisplay.append('🟦🟦🟦')  

    """получим строковое значение для трёхлитрового ведра"""
    for i in range(1, 4):
        if waterInBucket['3'] < i:
            waterDisplay.append('      ')  
        else:
            waterDisplay.append('🟦🟦🟦')  

    """отобразим на экране вёдра, каждое со своим объёмом воды"""
    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8л         5л         3л
'''.format(*waterDisplay))                                                                                                       # распаковать переменную waterDisplay на лету и подставить всё по индексам в фигурных скобках

    """проверим не содержится ли в вёдрах нужного количества воды"""
    for waterAmount in waterInBucket.values():
        if waterAmount == GOAL:
            print(f'Хорошая работа! Вы решили эту задачу за {steps} шагов!')
            sys.exit()

    """выбор действия, которое нужно совершить"""
    print('Какие можно совершить действия:')
    print('  (Н)аполнить ведро')
    print('  (В)ылить ведро')
    print('  (П)ерелейте одно ведро в другое')
    print('  (З)авершить программу')

    """спрашивать, пока пользователь не введёт подходящий ответ о действии"""
    while True:  
        move = input('> ').upper()
        if move == 'З':
            print('Спасибо за игру!')
            sys.exit()

        if move in ('Н', 'В', 'П'):
            break
        print('Вы ввели неправильно. Введите: "Н", "В", "П" или "З"')

    """спрашивать, пока пользователь не введёт подходящий ответ, какое ведро"""
    while True:  
        print('Выбрать ведро: 8, 5, 3, или (З)авершить программу.')
        srcBucket = input('> ').upper()

        if srcBucket == 'З':
            print('Спасибо за игру!')
            sys.exit()

        if srcBucket in ('8', '5', '3'):
            break 

    """произвести выбранное действие"""
    if move == 'Н':
        # Наполнить ведро по максимуму
        srcBucketSize = int(srcBucket)
        waterInBucket[srcBucket] = srcBucketSize
        steps += 1

    elif move == 'В':
        # Вылить ведро
        waterInBucket[srcBucket] = 0
        steps += 1

    elif move == 'П':
        # Перелить воду в другое ведро
        while True:  
            print('Выбирете ведро, в которое переливаем: 8, 5, or 3')
            dstBucket = input('> ').upper()
            if dstBucket in ('8', '5', '3'):
                break  

        # Определим наливаемый объём воды
        dstBucketSize = int(dstBucket)                                          # полный объём воды ведра, в которое переливаем
        emptySpaceInDstBucket = dstBucketSize - waterInBucket[dstBucket]        # незаполненный объём воды в ведре, в которое переливаем
        waterInSrcBucket = waterInBucket[srcBucket]                             # объём воды в ведре, из которого переливаем
        amountToPour = min(emptySpaceInDstBucket, waterInSrcBucket)             # объём воды, на который можно долить ведро

        # Выливаем воду из ведра
        waterInBucket[srcBucket] -= amountToPour

        # Налиывем вылитую воду в другое ведро
        waterInBucket[dstBucket] += amountToPour
        steps += 1