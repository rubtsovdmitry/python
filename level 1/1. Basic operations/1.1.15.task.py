from math import acos, sin, cos, radians                                                                                                    # подключение дополнительных функций из модуля math
print()

latitude_1 = radians(float(input("%60s" % "Введите широту первой точки: ")))                                                                # с помощью дополнительной функции переводим градусы на входе в радианы
longitude_1 = radians(float(input("%60s" % "Введите долготу первой точки: ")))
latitude_2 = radians(float(input("%60s" % "Введите широту первой точки: ")))
longitude_2 = radians(float(input("%60s" % "Введите долготу первой точки: ")))
radius_middle = 6371.01                                                                                                                     # это среднее значение радиуса Земли

distance = radius_middle * acos(sin(latitude_1) * sin(latitude_2) + cos(latitude_1) * cos(latitude_2) * cos(longitude_1 - longitude_2))     # формула расстояния между двумя точками на планете Земля 
print("%59s" % "Расстояние между двумя координатами по прямой, в км.:", "%.2f" % distance)