import datetime

def getCalendarFor(year, month):
    calText = ''                                                                                                                            # это календарь-строка   
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'                                                                      # разместим названия месяца и год календаря в верхней строке
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'                                           # добавим названия дней недели в английском стиле, где воскресенье первый день недели
    
    weekSeparator = ('+----------' * 7) + '+\n'                                                                                             # переменная с разделителем
    blankRow = ('|          ' * 7) + '|\n'                                                                                                  # переменная с разделителем
    currentDate = datetime.date(year, month, 1)                                                                                             # получение первой даты месяца в формате 2024-01-01

    while currentDate.weekday() != 6:                                                                                                       # в цикле будем отнимать по дню пока не дойдём до воскресенья (это 6, понедельник - это 0)
        currentDate -= datetime.timedelta(days=1)                                                                                           # дата начала календаря (возможно из другого месяца)

    while True:  
        calText += weekSeparator                                                                                                            # добавляем разделитель недели

        dayNumberRow = ''
        for i in range(7):                                                                                                                  
            dayNumberLabel = str(currentDate.day).rjust(2)                                                                                  # переменная с номером дня в месяце, выравненная по правому краю с длиной строковой переменной 2 
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Go to next day.
        dayNumberRow += '|\n'  # Add the vertical line after Saturday.

        calText += dayNumberRow                                                                                                             # заполнить секцию с числами внутри календаря для недели
        for i in range(3):                                                                                                                  # заполнить секцию с пробелами внутри календаря для недели
            calText += blankRow

        if currentDate.month != month:                                                                                                      # если месяц сменился, то прерываем цикл
            break
    
    calText += weekSeparator                                                                                                                # добавим закрывающую нижнюю линию для календаря
    return calText                                                                                                                          # функция возвращает гототый календарь


DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

while True:                                                                                                                                 # цикл для правильного ввода года
    print()
    response = input('Введите год: ')
    if response.isdecimal() and int(response) > 0:
        year = int(response)                                                                                                                # создадим переменную для года
        break
    print('Ошибка ввода.')
    continue

while True:                                                                                                                                 # цикл для правильного ввода месяца
    print()
    response = input('Введите месяц: ')
    if response.isdecimal() and 1 <= int(response) <= 12:
        month = int(response)                                                                                                               # создадим переменную для месяца
        break
    print('Ошибка ввода.')
    continue

calText = getCalendarFor(year, month)
print(calText)