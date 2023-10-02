def my_function(music):
    listen_max = 0
    for i in music.values():    
        listen_max = i if i > listen_max else listen_max
    new_unit = str
    for a, b in music.items():
        new_unit = a if b == listen_max else new_unit
    return new_unit


# Дан словарь с композициями и количеством прослушиваний для каждой
music = {
    "МАРИ КРАЙМБРЕРИ - Мне Так Повезло": 50,
    "РУКИ ВВЕРХ - Чёрное Море": 90,
    "MARY GU - Обожай": 80,
    "АНИ ЛОРАК - Рядом, Но Не Вместе": 40,
    "NATAN, СЛАВА - Ой всё": 70,
    "БЬЯНКА - Любимый дождь": 30,
    "JONY - Воздушный Сарафан": 100,
    "ОЛЕГ МАЙАМИ - Мельница": 20,
    "GAYAZOV$ BROTHER$ - Невеста": 60,
    "КОРОЛЁВА НАТАША - Обниму": 20
}

music_sort = list()                                             # создадим список, в который будем складывать композиции в порядке убывания популярности
for i in range (0, len(music)):                                 # обработаем наш словарь в цикле столько раз, сколько у нас элементов в словаре, каждый раз выкидывая один элемент из словаря
    result = my_function(music)
    music_sort.append(result)
    del music[result]

for i in music_sort:
    print(i)