from math import tan, pi

n = int(input("%33s" % "Введите количество сторон: "))
s = float(input("%33s" % "Введите длину стороны в см.: "))

area = (n * s ** 2) / (4 * tan(pi / n))

print("%32s" % "Площадь:", "%.2f" % area, "см^2")