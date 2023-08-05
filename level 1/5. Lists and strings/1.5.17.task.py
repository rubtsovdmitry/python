number_credit = input("Введите номер кредитной карты в формате xxxxxxxxxxxxxxxx ")

number_credit = number_credit[::-1]                         # перевернём строку
number_credit_first = number_credit[0::2]                   # создадим строку только с нечётными цифрами
number_credit_second = number_credit[1::2]                  # создадим строку только с чётными цифрами

# посчитаем сумму цифр на нечётных местах
amount = list(number_credit_first)                          # преобразуем строку в список
amount = sum([int(i) for i in amount])                      # посчитаем сумму всех цифр на нечётных местах

# посчитаем сумму цифр на чётных местах с необходимым модом
amount_2 = list(number_credit_second)                       # преобразуем строку в список
amount_2 = [int(i) for i in amount_2]                       # поменяем значения в списке со str на int
for i in amount_2:                                          
    i *= 2
    if i > 9:
        amount += i // 10 + i % 10        
    else:
        amount += i        

result = "Карта валидна" if amount % 10 == 0 else "Карта не валидна"
print(result)