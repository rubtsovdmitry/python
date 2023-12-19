import os, copy, random

def my_def_3(finish):                                               # отсортируем варианты в словаре билетов
    for a, b in finish.items():
        b = sorted(b)
        finish[a] = b
    return finish


def my_def_2(ticket_temp, towns_list):                              # функция дополнения словаря неправильными ответами
    for a, b in ticket_temp.items():
        towns_list_copy = copy.copy(towns_list)
        towns_list_copy = [i for i in towns_list_copy if i not in b]
        random.shuffle(towns_list_copy)
        ticket_temp[a] += [towns_list_copy[-1]]
        towns_list_copy.pop()
        random.shuffle(towns_list_copy)
        ticket_temp[a] += [towns_list_copy[-1]]    
    return ticket_temp


def my_def(temp, questions):                                        # функция создаст рандомный список с правильными ответами вида ['Панама', 'Панама', 'Венесуэла', 'Каракас', 'Дания', 'Копенгаген', 'Польша', 'Варшава', 'Бельгия', 'Брюссель']        
    if len(temp) == (len(capitals) - questions):
        return []
    else:
        random.shuffle(temp)
        return (temp[0] + my_def(temp[1:], questions))              # создадим список рекурсивно


# ввод данных
capitals = {
    "Россия": "Москва",
    "Республика Беларусь": "Минск",
    "Казахстан": "Астана",
    "Япония": "Токио",
    "Китай": "Пекин",
    "Монголия": "Улан-Батор",
    "Турция": "Стамбул",
    "Сербия": "Белград",
    "Финляндия": "Хельсинки",
    "Швеция": "Стокгольм",
    "Норвегия": "Осло",
    "Польша": "Варшава",
    "Германия": "Берлин",
    "Франция": "Париж",
    "Великобритания": "Лондон",
    "Испания": "Мадрид",
    "Португалия": "Лиссабон",
    "Италия": "Рим",
    "Греция": "Афины",
    "Бельгия": "Брюссель",
    "Голландия": "Амстердам",
    "Дания": "Копенгаген",
    "Швейцария": "Берн",
    "США": "Вашингтон",
    "Канада": "Оттава",
    "Мексика": "Мехико",
    "Панама": "Панама",
    "Бразилия": "Бразилиа",
    "Венесуэла": "Каракас"
}
number_tickets = range(20)                                          # количество экзаменационных билетов
questions = 5

os.makedirs("./География_экзамен")                                  # создание каталога, в который будем сохранять билеты
capitals_mod = [[a, b] for a, b in capitals.items()]                # преобразуем словарь в список списков
towns_list = list(capitals.values())                                # создадим список из всех возможных городов
count = 0                                                           # счётчик билетов

for i in number_tickets:                                            # создадим в цикле все билеты
    count += 1
    temp = copy.deepcopy(capitals_mod)
    result = my_def(temp, questions)                                # описание функции в начале. result - это список вида ['Панама', 'Панама', 'Венесуэла', 'Каракас', 'Дания', 'Копенгаген', 'Польша', 'Варшава', 'Бельгия', 'Брюссель']    
    ticket_temp = dict()                                            # создадим словарь из списка выше, который позже дополним правильными и неправильными вариантами ответов 
    for index, item in enumerate(result[::2]):                      # заполнение словаря для каждого билета правильными ответами вида {'Казахстнан': {'Астана'}, 'Республика Беларусь': {'Минск'}, 'Германия': {'Берлин'}, 'Голландия': {'Амстердам'}, 'Италия': {'Рим'}}
        ticket_temp[item] = [result[(index + 1) * 2 - 1]]
    finish = my_def_2(ticket_temp, towns_list)                      # дополним словарь неправильными ответами
    finish = my_def_3(finish)                                       # отсортируем варианты в словаре билетов, имеющих вид {'Республика Беларусь': ['Минск', 'Каракас', 'Улан-Батор'], 'Голландия': ['Амстердам', 'Бразилиа', 'Москва'], 'Венесуэла': ['Каракас', 'Лиссабон', 'Стамбул'], 'Испания': ['Мадрид', 'Варшава', 'Токио'], 'Япония': ['Токио', 'Вашингтон', 'Астана']}    
    f = open(f"./География_экзамен/{count}.ticket.txt", "a")        # создадим файлы в нашем каталоге, согласно счётчика
    for a, b in finish.items():                                     # заполнение файлов
        s = (f"Страна: {a}. Варианты ответов: {b}." + "\n")
        f.write(s)
    f.close()