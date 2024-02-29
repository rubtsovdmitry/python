import copy
from math import inf

"""ФУНКЦИЯ ПРОВЕРКИ ПРОДОЛЖЕНИЯ ОСНОВНОГО ЦИКЛА"""
def function_check(LAST):
    check = False
    for i in distance:
        if LAST not in i:
            check = True
            break
    return check


"""ВХОДНЫЕ ДАННЫЕ."""
distance = {
    "Электросталь***Казань": 760,
    "Электросталь***Кисловодск": 1640,
    "Электросталь***Минск": 770,
    "Электросталь***Санкт-Петербург": 770,
    "Казань***Санкт-Петербург": 1510,
    "Казань***Кисловодск": 1690,
    "Казань***Минск": 1520,
    "Минск***Казань": 1520,
    "Минск***Кисловодск": 2100,
    "Минск***Санкт-Петербург": 810,
    "Санкт-Петербург***Минск": 810,
    "Санкт-Петербург***Казань": 1510,
    "Санкт-Петербург***Кисловодск": 2300
}
FIRST = "Электросталь"
LAST = "Кисловодск"

result = []                                                         # в эту переменную будем помещать следующий пункт назначения
towns = []                                                          # здесь города, в которых мы уже были

# разберёмся с первым городом               
min_distance = inf              
best_way = None             
last_town = None
for a, b in distance.items():                   
    if FIRST == a[0:len(FIRST)]:                
        if b < min_distance:                
            min_distance = b                
            best_way = a                
result.append(best_way)                                             # --> ['Электросталь-Казань']
towns.append(FIRST)                                                 # --> {'Электросталь'}
last_town = best_way.split("***")[1]                                # --> "Казань"
temp = copy.copy(distance)                                          # создадим копию словаря distance
for i in temp:                                                      # в цикле уберём лишнее из словаря distance
    if i.split("***")[0] in towns:
        del distance[i]


"""ОСНОВНОЙ ЦИКЛ"""
while function_check(LAST):
    min_distance = inf
    best_way = None
    for a, b in distance.items():
        if last_town == a[0:len(last_town)]:
            if b < min_distance:
                min_distance = b
                best_way = a
    result.append(best_way)
    towns.append(best_way.split("***")[0])
    last_town = best_way.split("***")[1]    
    temp = copy.copy(distance)
    for i in temp:                                                      
        if best_way.split("***")[0] in i:
            del distance[i]
towns.append(last_town)                                             # дополним окончательный список городов последним из предыдущего цикла
for i in distance:                                                  # окончательно сформируем список городов в маршруте
    towns.append(i.split("***")[1])

print(towns)