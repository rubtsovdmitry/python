def my_function(divider):                                                       # функция будет искать следующий простой делитель по возрастанию
    while True:
        divider += 1                                                            # увеличивает делитель на 1 для дальнейшей проверки (является ли он простым делителем)
        digit = divider - 1
        while digit != 1 or divider % digit != 0:                               # проверка (простой ли новый делитель)
            digit -= 1
        if digit == 1:                                                          # нашли новый простой делитель. прерываем цикл
            break
    return divider                 


while True:
    try:
        digit = int(input("%50s" % "Введите целое число, которое больше или равно 2: "))
        if digit >= 2:
            break
    except:
        print("%50s" % "Вы ввели не число.")

divider = 2

result = list()

# этот блок нужен для того, чтобы получить первый делитель, который не подходит, ну или убедится, что 2 сразу не подходит
while digit % divider == 0:                                     
    digit = int(digit / divider)
    result.append(divider)

while digit % divider != 0 and digit > divider:                                 # в этом цикле мы ищем новый простой делитель, который растёт
    divider = my_function(divider)                                              # передадим старый делитель нашей функции, для поиска нового
    while digit % divider == 0:                                                 # этот блок нужен для того, чтобы определить, что новый делитель, уже отработал (устарел) или просто не подходит
        digit = int(digit / divider)
        result.append(divider)

for i in result:
    print("%40s" % f"{i:<5}")