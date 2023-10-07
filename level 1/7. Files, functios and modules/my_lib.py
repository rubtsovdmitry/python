def my_function(digit):                                                                           
    our_dict = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }
    return our_dict[digit]


# возвращает кортеж с двумя элементами, где первый элемент - это True или False (определяет существует такая дата или нет), а второй элемент - это порядковый номер дня в году для кокретной даты 
def true_date(year, month, day):
    dict_1 = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}                                                                # словарь для обычного года
    dict_2 = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}                                                                # словарь для високосного года
    if ((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)) and (month in dict_2) and (1 <= day <= dict_2[month]):                        # проверка даты, если год високосный (раньше такая задача встречалась, называется високосный год)
        flag = True                                                                                                                                                 # флаг, если год прошёл проверку на существование даты
        number = 0                                                                                                                                                  # будем копить сюда порядковый номер дня в году
        for a, b in dict_2.items():                                                                                                                                 # обойдем словарь в цикле и накопим порядковый номер пока будет удовлетворять условие
            if a < month:
                number += b
            elif a == month:
                number += day        
    elif (((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)) == False) and (month in dict_2) and (1 <= day <= dict_1[month]):           # повторение, только для другого словаря
        flag = True
        number = 0
        for a, b in dict_1.items():
            if a < month:
                number += b
            elif a == month:
                number += day
    else:                                                                                                                                                           # этот блок, когда дата не прошла проверку, т.е. не существует
        flag = False
        number = 0
    return (flag, number)                                                                                                                                           # возвращаем кортеж, первый элемент которого является флагом прошла дата проверку на существование или нет, а второй элемент это порядковый номер дня для этой даты в году.


# определяет дату по номеру дня в году
def our_date(leap, day):
    dict_1 = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}                                                                # словарь для обычного года
    dict_2 = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}                                                                # словарь для високосного года
    dict_1_mod = dict()                                                                                                                                             # составим более интересный словарь, где значением ключа (месяца) является range из порядковых номеров в году
    dict_2_mod = dict()                                                                                                                                             # -||-
    if leap:                                                                                                                                                        # определение даты для високосного года
        temp_1 = 1        
        temp_2 = 1
        for a, b in dict_2.items():     
            temp_2 += b       
            dict_2_mod[a] = range(temp_1, temp_2)
            temp_1 += b
        max_of_last_month = 0
        for a, b in dict_2_mod.items():
            if day in b:
                result = str(a) + "-" + str(day - max_of_last_month)
            max_of_last_month = max(b)
    else:                                                                                                                                                           # определение даты для не високосного года
        temp_1 = 1        
        temp_2 = 1
        for a, b in dict_1.items():     
            temp_2 += b       
            dict_1_mod[a] = range(temp_1, temp_2)
            temp_1 += b
        max_of_last_month = 0
        for a, b in dict_1_mod.items():
            if day in b:
                result = str(a) + "-" + str(day - max_of_last_month)
            max_of_last_month = max(b)
    return result


# возвращает кортеж с двумя элементами, где первый элемент - это True или False (определяет существует такая дата или нет), а второй элемент - это реальная дата (определение даты переадресована в другую функцию)
def digit_date_of_year(year, day):    
    if (((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)) == False) and (day > 365 or day < 1):                                                  
        flag = False
        number = 0
    elif ((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)) and (day > 366 or day < 1):                  
        flag = False                                                                                                                                               
        number = 0       
    elif ((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)):                    
        flag = True
        leap = True
        number = our_date(leap, day)
    elif (((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)) == False):                    
        flag = True
        leap = False
        number = our_date(leap, day)    
    return (flag, (str(year) + "-" + number))                                                                                                                        # возвращаем кортеж, первый элемент которого является флагом прошла дата проверку на существование или нет, а второй элемент это реальная дата