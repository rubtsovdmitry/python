S_weight = 75
T_weight = 112
souvenirs = int(input("%33s" % "Введите количество сувениров: "))           # выделим 33em под строку
trinkets = int(input("%33s" % "Введите количество безделушек: "))
total_weight = S_weight * souvenirs + T_weight * trinkets
print("%32s" % "Общий вес посылки в граммах:", total_weight)                # здесь выделение 32em (print даёт 1em)