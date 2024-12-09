from math import pi

radius = float(input("%40s" % "Введите радиус цилиндра в см.: "))
height = float(input("%40s" % "Введите высоту цилиндра в см.: "))

area = pi * radius ** 2
v = area * height

print("%39s" % "Объём цилиндра:", round(v, 1), "см^3")