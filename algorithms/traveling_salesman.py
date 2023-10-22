import copy
from math import acos, sin, cos, radians

def distance_f(town_tuple_1, town_tuple_2):
    latitude_1 = radians(town_tuple_1[0])
    longitude_1 = radians(town_tuple_1[-1])
    latitude_2 = radians(town_tuple_2[0])
    longitude_2 = radians(town_tuple_2[-1])
    radius_middle = 6371.01                                                                                                                     # это среднее значение радиуса Земли
    distance = radius_middle * acos(sin(latitude_1) * sin(latitude_2) + cos(latitude_1) * cos(latitude_2) * cos(longitude_1 - longitude_2))     # формула расстояния между двумя точками на планете Земля 
    return int(distance)


def coordinates_f():
    while True:
        x = input("%75s" % "Введите широту для города (в формате 55.78): ")
        y = input("%75s" % "Введите долготу для города (в формате 38.44): ")
        try:
            x = float(x)
            y = float(y)
            break
        except:
            print("%74s" % "Вы ввели не цифры или запятую вместо точки.")
    return (x, y)


#########################################################################################################################################################
# ввод данных
town1 = input("%75s" % "Ввделите название первого города: ")
coordinates1 = coordinates_f()
town2 = input("%75s" % "Ввделите название второго города: ")
coordinates2 = coordinates_f()
town3 = input("%75s" % "Ввделите название третьего города: ")
coordinates3 = coordinates_f()
town4 = input("%75s" % "Ввделите название четвёртого города: ")
coordinates4 = coordinates_f()
town5 = input("%75s" % "Ввделите название пятого города: ")
coordinates5 = coordinates_f()
print()
#########################################################################################################################################################
# создадим словарь, в котором ключ - это маршрут, а значение - это расстояние маршрута
distance_dict = dict()
points = [town1, town2, town3, town4, town5]
coordinates = [coordinates1, coordinates2, coordinates3, coordinates4, coordinates5]
coordinates_towns_dict = dict()
for a, b in zip(points, coordinates):
    coordinates_towns_dict[a] = b

for a in points:
    for b in points:
        if b != a:
            distance_dict[a + "-" + b] = distance_f(coordinates_towns_dict[a], coordinates_towns_dict[b])
#########################################################################################################################################################
# следующим сложнейшим циклом мы переберём все возможные комбинации городов, подставляя в очередной вложенный цикл один и тот же список
# на первый взгляд трудно себе это представить в голове, я рисовал на бумаге решение и картина сложилась
result = dict()
points = [town1, town2, town3, town4, town5]            # эту переменную я пересоздал только для того, чтобы она была в этом блоке для наглядности
for a in points:
    if a == town1:
        for b in points:
            if b != a:
                for c in points:
                    if c != a and c != b:
                        for d in points:
                            if d != a and d != b and d != c:
                                for e in points:
                                    if e != a and e != b and e != c and e != d:
                                        for f in points:
                                            if f == town1:
                                                result[a, b, c, d, e, f] = 0            # добавляем в словарь возможные маршруты, пока расстояние запишем 0

# заполним словарь с маршрутами и реальной дистанцией
temp_dict = copy.copy(result)
temp = ""
for a in temp_dict:
    for b in a:
        if (temp + "-" + b) in distance_dict:
            result[a] += distance_dict[(temp + "-" + b)]
        temp = b
del temp_dict

# вывод на печать всех возможных маршрутов и их протяжённости
count = 1
for a, b in result.items():
    print("%74s" % f"Маршрут № {count}:", a, "%20s" % f"  -   расстояние {b}км.")
    count += 1
print()
#########################################################################################################################################################

# вывод на печать ответа
km = (min(result.values()))
finish = [i for i in result if result[i] == km]
for i in finish:
    print(f"Маршрут: {i} является кротчайшим и составляет {km} км.")