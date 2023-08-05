# вводные, кот. необходимо привести к одному виду
nums = ['8 (999) 031 31 32', 79005552543, '7 (999) 031-31-32', 74997177804, '7 (499) 7816448', '8 916 599 87 17', '+7-499-717-78-04', '7 (960) 225 17 73', '+7 999 031 31 32', '7 (499) 381 85 94', '7-499-781-64-48', 84993818594, '7 915 861 14 30', '8 (926) 2006304', '+7 (499) 717 78 04', '7 999 251 14 96', '8 926 200 63 04', '+7 (900) 5552543', 89165998717, '+7 (960) 9921345', '+7 916 272 29 48', '8 (900) 5552543', '+79158611430', 79168571046, '8 (926) 200-63-04', '89165163715', 74997177804, 79600729120, 89990232281, '79162722948', '74956285138', '79600729120', '7-499-381-85-94', '8 499 717 78 04', 79161853299, 79602251773, '+79991820683', 84999731258, '+7-900-372-17-33', '+7 (495) 628 51 38', '+7 915 861 14 30', 89165163715, 84953524680, '7 (499) 973 12 58', 89262006304, '8-915-861-14-30', '+7 999 023 22 81', '7 916 185 32 99', '7 (499) 636 12 24', '+79165998717', '84997816448', '7 (916) 857 10 46', '+7 (960) 225 17 73', 89165163715, '7-960-072-91-20', '89602251773', 74995885010, '7-499-636-12-24', '+7 (900) 372 17 33', '7 (960) 0729120', '+7-499-781-64-48', 89262006304, '+7 (900) 5552543', 79005552543, '+7-960-810-64-12', 84995885010, 79600729120, 89608106412, '+7 495 352 46 80', 89005552543, '8 (916) 5163715', 89602251773, '7-916-599-87-17', '79608106412', '8 916 857 10 46', '8 (900) 555 25 43', '8-960-992-13-45', '7 (499) 7177804', 79165163715, '7 (495) 628 51 38', '7-499-588-50-10', 89158611430, '79602251773', 89165998717, 79158611430, '7 (926) 200 63 04', '89992511496', '7-495-628-51-38', '+7 (495) 6285138', '+7 (999) 2511496', '+79602251773', 89165163715, '79162722948', '8 (926) 200 63 04', '8 (916) 5163715', '7 (499) 5885010', '+7 916 516 37 15', '8-999-023-22-81', '8 (916) 857-10-46', 79990313132, '+7 495 628 51 38', '7 916 599 87 17', '+7 (915) 8611430', 89990313132, 79158611430, '8-960-225-17-73', '7 (499) 5885010', '+7 (916) 516 37 15', 89262006304, 79165163715, '+74997177804', 79165163715, 74997177804, '8 (960) 810 64 12', 89165998717, '8 (916) 8571046', '7-900-555-25-43', 79600729120, '+7 (499) 7177804', '8-916-516-37-15', 79005552543, 89990313132, 89992511496, '8 499 381 85 94', 79003721733, '+7 (495) 352-46-80', '+7 (499) 381-85-94', '+79168571046', '7-960-810-64-12', 79003721733, '+7 495 628 51 38', '7 (999) 031 31 32', 79262006304, '+7 (916) 599 87 17', 74997177804, '+74996361224', 89003721733, 79162722948, '7-495-352-46-80', '7 (900) 555-25-43', '+7 (900) 3208711', '8 (916) 5163715', '+7-960-810-64-12', '7 (915) 861 14 30', '7-495-628-51-38', 79005552543, '+7 (960) 225 17 73', '+7 495 628 51 38', '8-916-599-87-17', 79992511496, 89600729120, '+7-916-599-87-17', '7 (960) 9921345', '7 (916) 857 10 46', '+74997816448', '7 (499) 7816448', '+7-926-200-63-04', 79162722948, 79158611430, '8 (499) 5885010', '+7-916-857-10-46', '8 (499) 7177804', 89609921345, '8-916-857-10-46', 89609921345, '7 (499) 381 85 94', '8-495-352-46-80', '7 (495) 352 46 80', '+7 499 781 64 48', 84996361224, '74993818594', '8 999 031 31 32', 89992511496, 89262006304, '7 (916) 185 32 99', 89165998717, 89602251773, 89992511496, 74997816448, '8 (499) 781-64-48', 89600729120, 74997177804, '+7 (999) 251 14 96', '+7 (999) 182 06 83', 79005552543, '+79165163715', 84956285138, '+7 (960) 992 13 45', '84956285138', '+7 (916) 272-29-48', '8-499-717-78-04', 89003721733, 89262006304, '+7-915-861-14-30', '+7 916 272 29 48', '7 (495) 628 51 38', '+7 900 372 17 33', '8 (916) 5998717', '8 499 717 78 04', 89991820683, 89165163715, 79003721733, 89158611430, 79160923145, '8 916 599 87 17', '7 (999) 251 14 96', '7 960 225 17 73', '8 (960) 225-17-73', 84997177804]

# заведём переменные, совпадения с которыми будем искать. значения будут в скобках, так точно найдутся коды городов
cod499 = "(499)"            
cod495 = "(495)"

# начнём приводить элементы списка к одному виду
nums_str = [str(i) for i in nums]                           # так мы превратим все элементы списка в строки

# теперь нужно, чтобы во всех элементах списка коды городов имели вид (ххх)
nums_mod = list()                                           # в эту переменную будем добавлять модифицированные телефоны
for i in nums_str:                                          # обойдём все элементы в списке и будем их изменять по условию
    i = i.replace(" ", "")                                  # уберём все пробелы в номерах
    i = i.replace("-", "")                                  # уберём все "-" в номерах
    if len(i) == 11 and (i[0] == '7' or i[0] == '8'):        
        i = "+7(" + i[1:4] + ")" + i[4:]        
    if len(i) == 13 and (i[0] == '7' or i[0] == '8'):
        i = "+7(" + i[2:5] + i[5:]
    if len(i) == 12 and i[0] == '+':
        i = "+7(" + i[2:5] + ")" + i[5:]
    nums_mod.append(i)

# мы имееем новый список nums_mod. все элементы списка одного формата
nums_moscow = [i for i in nums_mod if cod499 in i or cod495 in i]
print(nums_moscow)
print()

# P.S.
# добавим в задачу условие: убрать дубликаты и воспользуемся множеством
nums_moscow = set(nums_moscow)
print("Московские номера, с которых звонили:")
for i in nums_moscow:
    print(i)