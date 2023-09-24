def temp(i):
    temperature_f = str(round((i * 9 / 5 + 32), 2))
    return temperature_f


temperature = range(10, 101, 10)
for i in temperature:
    print("%35s" % "Температура в градусах Цельсия:", f"{i:.<20}", "%35s" % "Температура в градусах Фаренгейта:", f"{temp(i):.<20}")