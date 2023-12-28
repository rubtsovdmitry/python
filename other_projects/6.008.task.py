"""Парадокс дней рождения, также известный как задача о днях рождения, заключается в удивительно высокой вероятности того,
что у двух человек совпадает день рождения даже в относительно небольшой группе людей. В группе из 70 человек вероятность 
совпадения дней рождения у двух людей составляет 99,99%. Но даже в группе всего лишь из 23 человек вероятность совпадения
дней рождения составляет 50%. Приведённая программа производит несколько экспериментов, чтобы определить процентные соотношения
для групп различного размера."""

import datetime, random


def get_match(birthdays):                                                                                                                   # возвращает объекты даты дня рождения, встречающегося несколько раз с списке дней рождения
    if len(birthdays) == len(set(birthdays)):                                                                                               # проверяет на отсутствие дубликатов дней рождения
        return None  
    repeat_dict = {}
    for i in birthdays:
        if i not in repeat_dict:
            repeat_dict[i] = 1
        else:
            repeat_dict[i] += 1
    repeat_dict = {a: b for a, b in repeat_dict.items() if b > 1}                                                                           # в этом словаре дата и количество повторов равное 2 и больше
    return repeat_dict

def get_birthdays(number_of_birthdays):                                                                                                     # сгенерируем список дней рождения
    birthdays = []                                                                                                                          # пока этот список пуст
    for i in range(number_of_birthdays):                                                        
        start_of_year = datetime.date(2000, 1, 1)                                                                                           # здесь не важно какой именно год, начнём с высокосного         
        random_number_of_days = datetime.timedelta(random.randint(0, 1460))                                                                 # 365 дней для высокосного (+ 1 день это 366), т.е 365 + 365 * 3 = 1460 дней
        birthday = start_of_year + random_number_of_days                                                                                    # определим очередное число для i-го дня рождения                                                                 
        birthdays.append(str(birthday.month) + "." + str(birthday.day))                                                                     # добавим в список birthdays очередную дату дня рождения, но только без года, для этого обратимся к объекту birthday класса date, конкретнее к его атрибутам month и day (тема ООП)
    return birthdays


def main():                                                                                                                                 # основная функция
    print(f"""
    Birthday Paradox
    """)

    while True:                                                                                                                             # спрашиваем в цикле, пока не будет введён правильный
        print('Сколько дней рождения нужно сгенерировать? Максимум 100.')
        response = input('Ответ: ')
        if response.isdecimal() and (0 < int(response) <= 100):                                                                             # если первая часть условия выполняется, то и преобразование второй в int исполнится 
            num_b_days = int(response)
            break 
    print()

    birthdays = get_birthdays(num_b_days)                                                                                                   # передадим в качестве параметра функции количество дней для генерации списка дней рождения
    for i in birthdays:                                                                                                                     # выведем на печать все дни рождения
        print(i, end=" / ")
    print()

    match = get_match(birthdays)                                                                                                            # найдём дубликаты дней рождения
    
    if match != None:
        for a, b in match.items():
            print(f"Дата: {a: >5}. Количество дней рождений: {b}.")
    else:
        print('Нет совпадающих дней рождений.')
    print()

    print('Генерация', num_b_days, 'дней рождений 100,000 раз...')
    input('Press Enter to begin...')

    sim_match = 0
    for i in range(100_000):        
        if i % 10000 == 0:
            print(i, 'симуляций')
        birthdays = get_birthdays(num_b_days)
        if get_match(birthdays) != None:
            sim_match += 1

    probability = round(sim_match / 100_000 * 100, 2)                                                                                       # процент выпадания дубликатов
    print(f"""
При количестве {num_b_days} человек в группе вероятность совпадения хотя бы двух дней рождений составляет {probability}%.
""")
    

if __name__ == '__main__':
    main()