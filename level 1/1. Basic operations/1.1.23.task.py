from math import sqrt

a = float(input("%40s" % "Введите длину первой стороны: "))
b = float(input("%40s" % "Введите длину второй стороны: "))
c = float(input("%40s" % "Введите длину третьей стороны: "))

s = (a + b + c) / 2
area = sqrt(s * (s - a) * (s - b) * (s - c))

print("%39s" % "Площадь треугольника:", "%.2f" % area)